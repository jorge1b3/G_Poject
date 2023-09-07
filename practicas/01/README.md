# Primera práctica. Segunda parte.

## NOT

| in  | out |
|:---:|:---:|
| 0   | 1   |
| 1   | 0   |

Esta es la compuerta más sencilla que podemos realizar. Partiendo de la compuerta nand, donde tenemos lo siguiente:

| a   | b   | out |
|:---:|:---:|:---:|
| 0   | 0   | 1   |
| 0   | 1   | 1   |
| 1   | 0   | 1   |
| 1   | 1   | 0   |

Ahora, como podemos ver, todos los casos nos dan 1, excepto cuando ambos valores son 0. Podemos tomar esto a nuestro favor. Si asumimos el caso $(1,1) \rightarrow 0$, como nuesto "1" y el resto como "0", podemos hacer una compuerta not muy sencilla, haciendo que la entrada de nuestro not "in", sea la entrada de la compuerta nand, resultando solo dos casos: 

1. Ambas entradas del nand son 0
2. Ambas entradas del nand son 1

En cada uno de los casos, la salida sera lo contrario a las entradas, haciendo que consigamos el comportamiento deseado de obtener un not.

| a   | b   | out |
|:---:|:---:|:---:|
| 0   | 0   | 1   |
| 1   | 1   | 0   |

## AND

| a   | b   | out |
|:---:|:---:|:---:|
| 0   | 0   | 0   |
| 0   | 1   | 0   |
| 1   | 0   | 0   |
| 1   | 1   | 1   |

Para nuestra compuerta and, podemos observar que es lo contrario a la compuerta nand (oviamente). Así que realizar esta compuerta es trivial, simplemente negando la salida de la compuerta nand con una compuerta not al final, y pasando las entradas de nuestro and a las entradas del nand, obteniendo nuestra compuerta and.

| a   | b   | out | not out |
|:---:|:---:|:---:|:-------:|
| 0   | 0   | 1   | 0       |
| 0   | 1   | 1   | 0       |
| 1   | 0   | 1   | 0       |
| 1   | 1   | 0   | 1       |

## OR

| a   | b   | out |
|:---:|:---:|:---:|
| 0   | 0   | 0   |
| 0   | 1   | 1   |
| 1   | 0   | 1   |
| 1   | 1   | 1   |

Como podemos ver en la tabla de verdad, la compuerta or es muy similar a la compuerta nand, solo que el valor de salida de $(0,0)$ y $(1,1)$ se encuentran "intercambiados". Nuestra solución es tan simple como negar las entradas de la compuerta nand, haciendo que la entrada $(0,0)$ se comporte como la entrada $(1,1)$ y la entrada $(1,1)$ como la $(0,0)$. Nótese que las demás combinaciones no se ven afectadas, debido a que intercambian valor, pero el valor de salida ya era el mismo en ámbas.

## XOR

Para el xor, primero nos fijamos que es el resultado de un and entre la compuerna nand y la compuerta or, dejando solo las entradas donde hay valores comunes, como digamos, $(1,0)$ y $(0,1)$, dejando la compuerta xor deseada.

| a   | b   | or  | nand | out |
|:---:|:---:|:---:| ---- | --- |
| 0   | 0   | 0   | 1    | 0   |
| 0   | 1   | 1   | 1    | 1   |
| 1   | 0   | 1   | 1    | 1   |
| 1   | 1   | 1   | 0    | 0   |

## MUX

El funcionamiento de la compurta Mux pemite elegir que entrada se verá reflejada en la salida, teniendo como entradas "a", "b" y un selector que en este caso llamamos "sel".

| a | b | sel | out |
|:-:|:-:|:---:|:---:|
| 0 | 0 | 0   | 0   |
| 0 | 0 | 1   | 0   |
| 0 | 1 | 0   | 0   |
| 0 | 1 | 1   | 1   |
| 1 | 0 | 0   | 1   |
| 1 | 0 | 1   | 0   |
| 1 | 1 | 0   | 1   |
| 1 | 1 | 1   | 1   |

Cuando "sel" es cero, la entrada que se verá reflejada es la "a", mientras que si es uno se verá reflejada la entrada "b". Para lograr esta funcionalidad se negó la entrada sel para saber cuando es cero, despues de esto se tienen dos And que tienen "a","notSel" y "b","sel" respectivamente, por ultimo se puso un Or para comprobar cuando alguno de los dos And reflejó un 1.

## DMUX

La compuerta Mux tiene como entradas "in" y "sel" y se encarga de decidir que salida será activada de esta forma:

| in | sel | out1 | out2 |
|:--:|:---:|:----:|:----:|
| 0  | 0   | 0    | 0    |
| 0  | 1   | 0    | 0    |
| 1  | 0   | 1    | 0    |
| 1  | 1   | 0    | 1    |

Para conseguir esta funcionalidad se hizo un procedimiento muy parecido al Mux, sin embargo en este caso las compuertas And comparan "a","sel" y "a","notSel" respectivamente, y la salida de cada And son "Out1" y "Out2" respectivamente.

## OR16

Habiendo hecho previamente la compuerta Or, esta es particularmente sencilla y mecanica, como entradas tenemos un vector "a" de tamaño 16 y un vector "b" del mismo tamaño, despues compararemos una por una las posiciones de los vectores, ej: "Or(a=a[0], b=b[0], out=out[0])". Finalmente, como se pudo ver en el ejemplo anterior, la salida, llamada "out" es un vector de 16 valores.

## AND16

Este caso es muy similar al anterior, se tienen las mismas entradas y las mismas salidas, la unica diferencia es que en lugar de ser una serie de 16 Or, es una serie de 16 And comparando cada una de las posiciones de los dos vectores de entrada, Ej: "And(a=a[0], b=b[0], out=out[0])"

## MUX16

En este caso, de nuevo, debemos repetir 16 veces la compuerta original, en este caso la compuerta Mux. Como entradas se tendrán dos vectores de 16 valores "a" y "b" y un selector "sel". A continuación se repetirá 16 veces la compuerta Mux para cada una de las entradas de los vectores, Ej: "Mux(a=a[0], b=b[0], sel=sel, out=out[0])"

## MUX4WAY16

Para realizar el MUX4W16, primero observamos la tabla de verdad de la compuerta:


## DMUX4WAY


Para realizar el DMux4Way, primero observamos la tabla de verdad de la compuerta:

|sel\[1\]|sel\[0\]|out|
|:------:|:------:|:-:|
|    0   |    0   | a |
|    0   |    1   | b |
|    1   |    0   | c |
|    1   |    1   | d |

Siendo la entrada in $0$ o $1$. Ahora, como podemos observar, las salida $(a,b)$ y las salidas $(c,d)$ tienen el mismo bit en el selector $sel[1]$, por lo que podríamos gruparlas, obteniendo:



|sel\[1\]|  out  |
|:------:|:-----:|
|    0   |$(a,b)$|
|    1   |$(c,d)$|

Que es precisamente un demultiplexor sencillo. Al aplicarlo, aún requerimos los valores de $a$, $b$, $c$ y $d$ por separado, pero si nos fijamos bien, estos a su vez, generan un demultiplexor por cada par:

> Dmux $(a,b)$

|sel\[0\]|out|
|:------:|:-:|
|    0   |$a$|
|    1   |$b$|


> Dmux $(c,d)$

|sel\[0\]|out|
|:------:|:-:|
|    0   |$c$|
|    1   |$d$|


Teniendo así, nuestro demultiplexor.
## MUX8WAY16

## DMUX8WAY

Primero, observemos la tabla de verdad de nuestro demultiplexor.

| sel\[2\] | sel\[1\] | sel\[0\] | out |
|:--------:|:--------:|:--------:|:---:|
|     0    |     0    |     0    |  a  |
|     0    |     0    |     1    |  b  |
|     0    |     1    |     0    |  c  |
|     0    |     1    |     1    |  d  |
|     1    |     0    |     0    |  e  |
|     1    |     0    |     1    |  f  |
|     1    |     1    |     0    |  g  |
|     1    |     1    |     1    |  h  |

Pero como con el DMux4Way, podemos observar que se puede separar en dos grúpos. Donde tenemos el grupo del sel\[2\] igual a 0 con $abcd$ y el grupo con sel\[2\] igual a 1 con $efgh$. Ahora, obtenemos la siguiente tabla

| sel\[2\] |   out  |
|:--------:|:------:|
|     0    | $abcd$ |
|     1    | $efgh$ |

Que, como podemos ver, corresponde a un demutiplexor sencillo. Ahora, para obtener cada una de las salidas por separado, pasamos cada salida de nuestro aplicado demutiplexor por dos demultiplexores de 4 entradas.

>Dmux4Way $(abcd)$

| sel\[1\] | sel\[0\] | out |
|:--------:|:--------:|:---:|
|     0    |     0    |  a  |
|     0    |     1    |  b  |
|     1    |     0    |  c  |
|     1    |     1    |  d  |

>Dmux4Way $(efgh)$

| sel\[1\] | sel\[0\] | out |
|:--------:|:--------:|:---:|
|     0    |     0    |  e  |
|     0    |     1    |  f  |
|     1    |     0    |  g  |
|     1    |     1    |  h  |

Obteniendo así, nuestro Dmux8Way.
