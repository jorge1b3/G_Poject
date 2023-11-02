## Documentación de proyecto 07

En este laboratorio, se alcanzó un nivel de complejidad superior al anterior al desarrollar un traductor que convierte un lenguaje de alto nivel a un lenguaje de bajo nivel. Para lograrlo, se utilizó el lenguaje de programación Python para codificar el programa que se detalla a continuación:

El codigo consta de tres partes, "CodeWriter", "Parser" y "Main".

La clase encargada de la traduccion del codigo como tal es "CodeWriter" la cual consta de una serie de funciones encargadas de:
  1) inicializar tanto las variables necesarias para la traduccion como el mismo archivo en el cual se va a cargar lo traducido, en este caso un archivo ".asm" 
  2) Escribir el codigo asm para los comandos aritmeticos 'add', 'sub', 'and', 'or', 'neg', 'not', 'eq', 'gt' y 'lt' siendo estas ultimas tres operaciones mas complejas de traducir que el resto y teniendo algunas lineas mas de código.
  3) Escribir el codigo correspondiente a: push, pop y cierre del codigo .asm.
  4) generar excepcion en caso de econtrar un argunmento desconocido.
  5) Devolver el diccionario con las direcciones de los diferentes segmentos de memoria.

Sin embargo, la clase CodeWriter no funcionará si antes no se prepara el archivo para ser ingresado a la misma. Para ello, se utilizará la clase "Parser" encargada de:
1) 
