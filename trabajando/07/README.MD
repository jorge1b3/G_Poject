## Documentación de proyecto 07

En este laboratorio, se alcanzó un nivel de complejidad superior al anterior al desarrollar un traductor que convierte un lenguaje de alto nivel a un lenguaje de bajo nivel. Para lograrlo, se utilizó el lenguaje de programación Python para codificar el programa que se detalla a continuación:

El código consta de tres partes: "CodeWriter", "Parser" y "Main".

La clase encargada de la traducción del código en sí es "CodeWriter", la cual consta de una serie de funciones encargadas de:
  1. Inicializar tanto las variables necesarias para la traducción como el mismo archivo en el cual se va a cargar lo traducido, en este caso, un archivo ".asm".
  2. Escribir el código asm para los comandos aritméticos 'add', 'sub', 'and', 'or', 'neg', 'not', 'eq', 'gt' y 'lt', siendo estas últimas tres operaciones más complejas de traducir que el resto y teniendo algunas líneas más de código.
  3. Escribir el código correspondiente a: push, pop y cierre del código .asm.
  4. Generar una excepción en caso de encontrar un argumento desconocido.
  5. Devolver el diccionario con las direcciones de los diferentes segmentos de memoria.

Sin embargo, la clase CodeWriter no funcionará si antes no se prepara el archivo para ser ingresado en la misma. Para ello, se utilizará la clase "Parser", encargada de:
  1. Inicializar atributos como el contador de líneas de comando o una lista con los comandos del código.
  2. Recorrer uno por uno la lista de comandos del código cargado, identificando y determinando el tipo de comando de cada línea como una instrucción "C_ARITHMETIC" para comandos aritméticos, "C_PUSH" para comandos push, y "C_POP" para comandos pop, y devolverá las partes del comando en "arg1" y/o "arg2" según sea necesario.

Por último, la clase Main o clase principal del programa se encarga, en primer lugar, de verificar si el archivo recibido cumple con ciertos requisitos para ser procesado; de lo contrario, imprime un error. Posteriormente, crea dos objetos de tipo "Parser" y "CodeWriter" con sus respectivos nombres que servirán como archivos de entrada y salida, respectivamente. Finalmente, el código avanza a través del objeto Parser y va guardando las líneas traducidas y demás información en el objeto CodeWriter hasta que se terminan en su totalidad las líneas de código del Parser, y finalmente cierra el archivo CodeWriter.
