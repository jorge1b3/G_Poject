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

## DMUX

La compuerta Mux tiene como entradas "a", "b" y un selector que en este caso llamamos "sel" y se encarga de decidir que salida será activada de esta forma:

## OR16

## AND16

## MUX16

## MUX4W16

## DMUX4W16

## MUX8W16

## DMUX8W16
