# Bit
La práctica numero tres empieza con la funcion mas básica para hacer registros en una memoria, guardar un bit. Este chip se encarga precisamente de eso, su función es la de guardar el valor que tenga un bit de entrada "in" en la salida "out". Además, el dato guardado en out debe cambiar unicamente cuando un "clock" predefinido del sistema tenga un tiempo alto (vease la figura).
![clock](https://github.com/jorge1b3/G_Poject/assets/131718783/19a86ddb-f72f-4e01-a213-1d4265fb6412)

para ello usaremos dos chips, un Mux (multiplexor) encargado de decidir si se guardará o no el dato y un DFF (D flip-flop) que leerá el dato y lo retornará en un output llamado "callback" que funcionará como una entrada al Mux anteriormente mencionado para que este decida si se hará el cambio en base a si ya se presentó un cambio en el DFF y si la entrada "load" es "1".

# Register
Register tiene la función de guardar una entrada "in[16]" de 16 bits en un "out[16]", para ello, llamamos sucesivamente al chip anterior, de esta forma se guardará posición por posicion un total de 16 veces (esto de la misma manera que el chip "Bit", cambiando unicamente con el tiempo alto del clock).

# RAM8
Entrando al mundo de la memoria RAM se empezará por una memoria sencilla y pequeña, en este caso tan solo tendremos 8 espacios para guardar datos. Para esta funcionalidad tendremos unas entrada extra en cuanto a los anteriores chips, esta es "address" la cual indicará en que puerto o espacio guardaremos el dato de "in[16]", un "DMux" será el encargado de escoger el que espacio entrará el dato de acuerdo al address, posterior al DMux se tendrá una sucesion de 8 "register" que representa cada uno de los espacios de memoria y finalmente, un chip "Mux" será el que imprima el dato guardado en el espacio especifico en que se deba haber guardado.

# RAM64


# PC


# RAM512


# RAM4K


# RAM16K

