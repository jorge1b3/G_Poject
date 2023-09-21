# Bit
La práctica numero tres empieza con la funcion mas básica para hacer registros en una memoria, guardar un bit. Este chip se encarga precisamente de eso, su función es la de guardar el valor que tenga un bit de entrada "in" en la salida "out". Además, el dato guardado en out debe cambiar unicamente cuando un "clock" predefinido del sistema tenga un tiempo alto (vease la figura).
![clock](https://github.com/jorge1b3/G_Poject/assets/131718783/19a86ddb-f72f-4e01-a213-1d4265fb6412)

para ello usaremos dos chips, un Mux (multiplexor) encargado de decidir si se guardará o no el dato y un DFF (D flip-flop) que leerá el dato y lo retornará en un output llamado "callback" que funcionará como una entrada al Mux anteriormente mencionado para que este decida si se hará el cambio en base a si ya se presentó un cambio en el DFF y si la entrada "load" es "1".

# Register
Register tiene la función de guardar una entrada "in[16]" de 16 bits en un "out[16]", para ello, llamamos sucesivamente al chip anterior, de esta forma se guardará posición por posicion un total de 16 veces (esto de la misma manera que el chip "Bit", cambiando unicamente con el tiempo alto del clock).

# RAM8
Entrando al mundo de la memoria RAM se empezará por una memoria sencilla y pequeña, en este caso tan solo tendremos 8 espacios para guardar datos. Para esta funcionalidad tendremos unas entrada extra en cuanto a los anteriores chips, esta es "address" la cual indicará en que puerto o espacio guardaremos el dato de "in[16]", un "DMux" será el encargado de escoger el que espacio entrará el dato de acuerdo al address, posterior al DMux se tendrá una sucesion de 8 "register" que representa cada uno de los espacios de memoria y finalmente, un chip "Mux" será el que imprima el dato guardado en el espacio especifico en que se deba haber guardado.

# RAM64
RAM64 funciona de manera analoga al chip "RAM8", en este caso se aumentará el espacio de ram poniendo 8 chips RAM8 sucesivamente creando 64 espacios de memoria, el "address" en este caso tendrá un tamaño de 6 bits en el cual escogerá tanto la "RAM8" en la que se guardará el dato (primeros 3 digitos) como el espacio dentro de la RAM8 en la que se guardará (ultimos 3 digitos). Por ultimo el DMux de igual forma imprimirá en que espacio de memoria se guardó el dato e imprimirá el dato correspondiente. 

# PC
Un Chip "PC" tiene la función de guardar, incrementar o reiniciar el valor de una posicion en memoria, para este fin se simplificó la memoria con un solo espacio de 16 bits, un chip "Register". Para lograr esta funcionalidad, primero se deben hacer las operaciones posibles, en este caso un vector de cero para el "reset" y un incremento al dato que esté guardado en un tiempo anterior del clock. Posteriormente se ecogerá cual es el dato que se guardará, la entrada normal, el incremento o el reinicio. Por último, dos condiciones Or dicen si se debe o no actualizar el dato de acuerdo a si alguna de las entradas equivale a "1", para luego ingresar el dato en un register y actualizar.

# RAM512
Este caso sigue la misma forma que el chip "RAM64", las diferencias entre estos dos son: en lugar de "RAM8" se tienen "RAM64" 8 veces de nuevo, y la otra diferencia en cuanto al anterior es que el "address" ahora tiene 9 digitos, los primeros 3 indican en que "RAM64"  se ingresará el dato y los otros 6 bits se ingresan a la RAM64 respectiva.

# RAM4K
Este chip funciona de la misma manera que el chip "RAM512", en este caso en lugar de usar chips "RAM64" se usan RAM512 y el address tiene 12 digitos, los tres primeros escogen a  cual RAM512 irá el dato y los otros 9 van a la RAM512 respectivo.

# RAM16K
De igual forma, este chip recurre al anterior para aumentar su tamaño, sin embargo este tiene una peculiaridad y es que no usa 8 veces el chip anterior, sino 4 veces, para su acceso usa un addres de 14 digitos y en este caso los dos primeros son los que escogen el puerto de RAM4K al que va el dato y los otros 12 van al chip RAM4K especifico.
