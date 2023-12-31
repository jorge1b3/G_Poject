import os
import glob


class Parser(object):
    def __init__(self, vm_filename):
        self.VM_archive = VM_archive
        self.vm = open(VM_archive, 'r')
        self.commands = self.commands_dict()
        self.curr_instruction = None
        self.start_file()

    def advance(self):
        self.curr_instruction = self.next_instruction
        self.load_next_instruction()

    @property
    def has_more_commands(self):
        return bool(self.next_instruction)

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
        '''Only return if C_PUSH, C_POP, C_FUNCTION, C_CALL'''
        return self.argn(2)

    def start_file(self):
        self.vm.seek(0)
        line = self.vm.readline().strip()
        while not self.is_instruction(line):
            line = self.vm.readline().strip()
        self.load_next_instruction(line)

    def load_next_instruction(self):
        stripped_lines = (line.strip().split("//")[0].strip().split() for line in self.vm)
        self.next_instruction = next((line for line in stripped_lines if self.is_instruction(line)), None)

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


class CodeWriter(object):
    def __init__(self, asm_filename):
        self.asm = open(asm_filename, 'w')
        self.curr_file = None
        self.bool_count = 0 
        self.addresses = self.address_dict()

    def set_file_name(self, vm_filename):
        self.curr_file = vm_filename.replace('.vm', '').split('/')[-1]

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

    def close(self):
        self.asm.close()

    def write(self, command):
        self.asm.write(command + '\n')

    def raise_unknown(self, argument):
        raise ValueError('{} is an invalid argument'.format(argument))

    def resolve_address(self, segment, index):
        address = self.addresses.get(segment)
        if segment == 'constant':
            self.write(f'@{index}')
        elif segment == 'static':
            self.write(f'@{self.curr_file}.{index}')
        elif segment in ['pointer', 'temp']:
            self.write(f'@R{address + int(index)}') 
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
        self.write('@SP') 
        self.write('M=M+1')

    def pop_stack_to_D(self):
        self.write('@SP')
        self.write('M=M-1') 
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


class Main(object):
    def __init__(self, file_path):
        self.parse_files(file_path)
        self.cw = CodeWriter(self.asm_file)
        for vm_file in self.vm_files:
            self.translate(vm_file)

    def translate(self, vm_file):
        parser = Parser(vm_file)
        self.cw.set_file_name(vm_file)
        while parser.has_more_commands:
            parser.advance()
            self.cw.write('// ' + ' '.join(parser.curr_instruction))
            if parser.command_type == 'C_PUSH':
                self.cw.write_push_pop('C_PUSH', parser.arg1, parser.arg2)
            elif parser.command_type == 'C_POP':
                self.cw.write_push_pop('C_POP', parser.arg1, parser.arg2)
            elif parser.command_type == 'C_ARITHMETIC':
                self.cw.write_arithmetic(parser.arg1)

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