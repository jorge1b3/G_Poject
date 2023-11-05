
# Project 08 - VM Traductor

import os
import glob


class CodeWriter(object):

    def __init__(self, asm_filename):
        self.asm = open(asm_filename, 'w')
        self.curr_file = None
        self.addresses = self.address_dict()
        self.line_count = 0
        self.bool_count = 0
        self.call_count = 0

    def write_init(self):
        # Initialize the stack pointer to 256
        # This is the starting location of our stack in the RAM
        self.write('@256')  
        self.write('D=A')  
        self.write('@SP')  
        self.write('M=D')  

        # This is a predefined function that sets up the system
        self.write_call('Sys.init', 0)

    def set_file_name(self, VM_archive):
        self.curr_file = VM_archive.replace('.vm', '').split('/')[-1]


    def write_arithmetic(self, operation):
        operations = {
            'add': 'M=M+D',
            'sub': 'M=M-D',
            'and': 'M=M&D',
            'or': 'M=M|D',
            'neg': 'M=-M',
            'not': 'M=!M',
        }

        jumps = {
            'eq': 'D;JEQ',
            'gt': 'D;JGT',
            'lt': 'D;JLT',
        }

        if operation not in ['neg', 'not']:
            self.pop_stack_to_D()
        self.decrement_SP()
        self.set_A_to_stack()

        if operation in operations:
            self.write(operations[operation])
        elif operation in jumps:
            self.write('D=M-D')
            self.write(f'@BOOL{self.bool_count}')
            self.write(jumps[operation])
            self.set_A_to_stack()
            self.write('M=0')
            self.write(f'@ENDBOOL{self.bool_count}')
            self.write('0;JMP')
            self.write(f'(BOOL{self.bool_count})')
            self.set_A_to_stack()
            self.write('M=-1')
            self.write(f'(ENDBOOL{self.bool_count})')
            self.bool_count += 1
        else:
            self.raise_unknown(operation)
        self.increment_SP()

    def write_push_pop(self, command, segment, index):
        self.resolve_address(segment, index)
        if command == 'C_PUSH':
            if segment == 'constant':
                self.write('D=A')
            else:
                self.write('D=M')
            self.push_D_to_stack()
        elif command == 'C_POP': 
            self.write('D=A')
            self.write('@R13')
            self.write('M=D')
            self.pop_stack_to_D()
            self.write('@R13')
            self.write('A=M')
            self.write('M=D')
        else:
            self.raise_unknown(command)

    def write_label(self, label):
        self.write('({}${})'.format(self.curr_file, label))

    def write_goto(self, label):
        self.write('@{}${}'.format(self.curr_file, label))
        self.write('0;JMP')

    def write_if(self, label):
        self.pop_stack_to_D()
        self.write('@{}${}'.format(self.curr_file, label))
        self.write('D;JNE')

    def write_function(self, function_name, num_locals):
        self.write('({})'.format(function_name))

        for _ in range(num_locals): 
            self.write('D=0')
            self.push_D_to_stack()

    def write_call(self, function_name, num_args):
        RET = function_name + 'RET' +  str(self.call_count) 
        self.call_count += 1

        self.write('@' + RET)
        self.write('D=A')
        self.push_D_to_stack()

        for address in ['@LCL', '@ARG', '@THIS', '@THAT']:
            self.write(address)
            self.write('D=M')
            self.push_D_to_stack()

        self.write('@SP')
        self.write('D=M')
        self.write('@LCL')
        self.write('M=D')

        self.write('@' + str(num_args + 5))
        self.write('D=D-A')
        self.write('@ARG')
        self.write('M=D')

        self.write('@' + function_name)
        self.write('0;JMP')

        self.write('({})'.format(RET))

    def write_return(self):
        FRAME = 'R13'
        RET = 'R14'

        self.write('@LCL')
        self.write('D=M')
        self.write('@' + FRAME)
        self.write('M=D')

        self.write('@' + FRAME)
        self.write('D=M') 
        self.write('@5')
        self.write('D=D-A') 
        self.write('A=D') 
        self.write('D=M') 
        self.write('@' + RET)
        self.write('M=D') 

        self.pop_stack_to_D()
        self.write('@ARG')
        self.write('A=M')
        self.write('M=D')

        self.write('@ARG')
        self.write('D=M')
        self.write('@SP')
        self.write('M=D+1')

        offset = 1
        for address in ['@THAT', '@THIS', '@ARG', '@LCL']:
            self.write('@' + FRAME)
            self.write('D=M')
            self.write('@' + str(offset))
            self.write('D=D-A')
            self.write('A=D')
            self.write('D=M')
            self.write(address)
            self.write('M=D')
            offset += 1

        self.write('@' + RET)
        self.write('A=M')
        self.write('0;JMP')

    def write(self, command):
        self.asm.write(command + '\n')

    def close(self):
        self.asm.close()

    def raise_unknown(self, argument):
        raise ValueError('{} is an invalid argument'.format(argument))

    def resolve_address(self, segment, index):
        address = self.addresses.get(segment)
        if segment == 'constant':
            self.write(f'@{index}')
        elif segment == 'static':
            self.write(f'@{self.curr_file}.{index}')
        elif segment in ['pointer', 'temp']:
            self.write(f'@R{address + index}')
        elif segment in ['local', 'argument', 'this', 'that']:
            self.write(f'@{address}')
            self.write('D=M')
            self.write(f'@{index}')
            self.write('A=D+A')
        else:
            self.raise_unknown(segment)

    def address_dict(self):
        return {
            'local': 'LCL',
            'argument': 'ARG',
            'this': 'THIS',
            'that': 'THAT',
            'pointer': 3,
            'temp': 5,
            'static': 16,
        }

    def push_D_to_stack(self):
        self.write('@SP')
        self.write('A=M') 
        self.write('M=D') 
        self.increment_SP()

    def pop_stack_to_D(self):
        self.decrement_SP()
        self.write('A=M')
        self.write('D=M') 

    def decrement_SP(self):
        self.write('@SP')
        self.write('M=M-1')

    def increment_SP(self):
        self.write('@SP')
        self.write('M=M+1')

    def set_A_to_stack(self):
        self.write('@SP')
        self.write('A=M')


class Parser(object):
    def __init__(self, VM_archive):
        self.VM_archive = VM_archive
        self.vm = open(VM_archive, 'r')
        self.EOF = False
        self.commands = self.commands_dict()
        self.curr_instruction = None
        self.start_file()

    def advance(self):
        self.curr_instruction = self.next_instruction
        self.load_next_instruction()

    @property
    def has_more_commands(self):
        return not self.EOF

    @property
    def command_type(self):
        return self.commands.get(self.curr_instruction[0].lower())

    @property
    def arg1(self):
        if self.command_type == 'C_ARITHMETIC':
            return self.argn(0)
        return self.argn(1)

    @property
    def arg2(self):
        return self.argn(2)

    def close(self):
        self.vm.close()

    def start_file(self):
        self.vm.seek(0)
        self.load_next_instruction()

    def load_next_instruction(self):
        stripped_lines = (line.strip().split("//")[0].strip().split() for line in self.vm)
        self.next_instruction = next((line for line in stripped_lines if self.is_instruction(line)), None)
        self.EOF = self.next_instruction is None

    def is_instruction(self, line):
        return line and line[:2] != "//"

    def argn(self, n):
        if len(self.curr_instruction) >= n+1:
            return self.curr_instruction[n]
        return None

    def commands_dict(self):
        return {
            'add': 'C_ARITHMETIC',
            'sub': 'C_ARITHMETIC',
            'neg': 'C_ARITHMETIC',
            'eq': 'C_ARITHMETIC',
            'gt': 'C_ARITHMETIC',
            'lt': 'C_ARITHMETIC',
            'and': 'C_ARITHMETIC',
            'or': 'C_ARITHMETIC',
            'not': 'C_ARITHMETIC',
            'push': 'C_PUSH',
            'pop': 'C_POP',
            'label': 'C_LABEL',
            'goto': 'C_GOTO',
            'if-goto': 'C_IF',
            'function': 'C_FUNCTION',
            'return': 'C_RETURN',
            'call': 'C_CALL'
        }


class Main(object):
    def __init__(self, file_path):
        self.parse_files(file_path)
        self.cw = CodeWriter(self.asm_file)
        self.cw.write_init()
        for vm_file in self.vm_files:
            self.translate(vm_file)
        self.cw.close()

    def translate(self, vm_file):
        parser = Parser(vm_file)
        self.cw.set_file_name(vm_file)
        command_map = {
            'C_PUSH': self.cw.write_push_pop,
            'C_POP': self.cw.write_push_pop,
            'C_ARITHMETIC': self.cw.write_arithmetic,
            'C_LABEL': self.cw.write_label,
            'C_GOTO': self.cw.write_goto,
            'C_IF': self.cw.write_if,
            'C_FUNCTION': self.cw.write_function,
            'C_CALL': self.cw.write_call,
            'C_RETURN': self.cw.write_return
        }
        while parser.has_more_commands:
            parser.advance()
            self.cw.write('// ' + ' '.join(parser.curr_instruction))
            command_type = parser.command_type
            if command_type in command_map:
                if command_type in ['C_PUSH', 'C_POP']:
                    command_map[command_type](command_type, parser.arg1, int(parser.arg2))
                elif command_type in ['C_FUNCTION', 'C_CALL']:
                    command_map[command_type](parser.arg1, int(parser.arg2))
                elif command_type == 'C_RETURN':
                    command_map[command_type]()
                else:
                    command_map[command_type](parser.arg1)
        parser.close()


    def parse_files(self, file_path):
        file_path = file_path.rstrip('/')
        if file_path.endswith('.vm'):
            self.asm_file = file_path.replace('.vm', '.asm')
            self.vm_files = [file_path]
        else:
            self.asm_file = os.path.join(file_path, os.path.basename(file_path) + '.asm')
            self.vm_files = glob.glob(os.path.join(file_path, '*.vm'))


if __name__ == '__main__':
    import sys

    file_path = sys.argv[1]
    Main(file_path)
