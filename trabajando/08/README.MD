## Documentacion del proyecto 08

Este laboratorio es una continuacion del anterior hecha para dar mas funcionalidad al traductor agregando distintas funciones como:

1. En la clase "CodeWriter" se agregaron las funciones "label," "goto," "if-goto," "function," "call," y "return." encargadas de traducir etiquetas, saltos condicionales e incondicionales a diferentes lineas, declaración de funciones, llamado de funciones y retorno de funciones.
2. Este programa no está limitado a recibir solo un archivo .vm, tambien soporta el ingreso de un directorio con varios archivos del mismo tipo que al final convierte en un unico archivo asm.
3. Ya que los archivos recibidos tienen un grado de complejidad considerablemente mayor a los anteriores se hace necesario incluir un código de arranque o "bootstrap code" que se encarga de diversas cosas como configurar el estado inicial de la maquina virtual, llamar en primer lugar a la función principal del archivo VM que generalmente se llama "Sys.init", entre otras configuraciones de menor relevancia.
