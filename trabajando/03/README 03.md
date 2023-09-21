# Bit
La práctica numero tres empieza con la funcion mas básica para hacer registros en una memoria, guardar un bit. Este chip se encarga precisamente de eso, su función es la de guardar el valor que tenga un bit de entrada "in" en la salida "out". Además, el dato guardado en out debe cambiar unicamente cuando un "clock" predefinido del sistema tenga un tiempo alto (vease la figura).
![clock](https://github.com/jorge1b3/G_Poject/assets/131718783/19a86ddb-f72f-4e01-a213-1d4265fb6412)

para ello usaremos dos chips, un Mux (multiplexor) encargado de decidir si se guardará o no el dato y un DFF (D flip-flop) que leerá el dato y lo retornará en un output llamado "callback" que funcionará como una entrada al Mux anteriormente mencionado para que este decida si se hará el cambio en base a si ya se presentó un cambio en el DFF y si la entrada "load" es "1".

# Register


# RAM8


# RAM64


# PC


# RAM512


# RAM4K


# RAM16K

