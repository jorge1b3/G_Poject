# HalfAdder

Para el HalfAdder, primero podemos observar que necesitamos obtener la siguiente tabla:

| a | b | out | carry |
|---|---|-----|-------|
| 0 | 0 |  0  |   0   |
| 0 | 1 |  1  |   0   |
| 1 | 0 |  1  |   0   |
| 1 | 1 |  0  |   1   |

Como podemos observar, nuestro "out" corresponde a una compuerta XOR, y nuestro carry a una compuerta AND. Así, tenemos las dos salidas deseadas como out = XOR(a,b) y carry = AND(a,b).

# FullAdder

En nuestro anterior ejemplo, podemos observar que el valor máximo que puede sumar es $10$, pero el valor máximo para 2 bits es $11$ que equivale a 3. Así, debemos definir una función que sea capaz de sumar hasta el 3. Para ello, podemos realizar un HalfAdder entre nuestras entradas $a$ y $b$. lo que resulta en un out, y un carry. Luego de ellos, podemos sumar un tercer elemento, $c$, haciendo que el valor máximo a sumar sea $3$, osea $11$. El carry de  la suma entre $a$ y $b$ se ejecuta en un or con la suma de $out$ y $c$, por que tenemos 3 posibilidades:

1. Carry1 = 1, carry2 = 0, total 1.
2. Carry1 = 0, Carry2 = 1, total 1.
3. Carry1 = 0, Carry2 = 0, total 0.

Por lo que con alguno de los dos carry sean 1, el carry total es 1. El caso donde los dos carry sean 1 no es posible, por que debería poder sumar hasta 4.

# Add16

En este caso, estamos sumando dos entradas de 16 bits cada una. En el primer paso, podemos aplicar un HalfAdder pues sabemos que máximo puede dar hasta 10. Luego, el carry de esta suma se lleva a las siguientes, donde con el FullAdder sumamos los a y b correspondientes y el carry de la anterior operación, haciendo que el total sea la suma de las dos entradas.

# Inc16

Para realizar un Inc16, debemos a una entrada de 16 bits sumarle $0000000000000001$. Sabemos que True en binario se representa como 16 unos, osea, $1111111111111111$, que resulta ser $-1$. si lo sumamos con otro true, la operación resultante es igual a $1111111111111110$ (-2). Si negamos esta entrada, obtenemos, $0000000000000001$ que es el valor que necesitamos sumar. Ahora solo sumamos la entrada con nuestro uno y obtenemos el resultado.

# ALU

En el alu, debemos realizar multiples operaciones:

1. Si algún (o ambos) zx o zy son 1, se deben inicializar el correspondiente como 16 ceros.
2. Si algún (o ambos) nx o ny son 1, se debe negar la entrada.
3. Si f es 1, se deben sumar la entrada. De lo contrario, se debe aplicar AND16.
4. Si no es 1, la salida debe ir negada. De lo contrario, la salida es normal.

Como cada una de estas instrucciones son sucesivas, primero aplicamos $zx$ y $zy$.

Podemos observar que un multiplexor actúa como un $if$ de programación, donde si es verdadero hace algo, y si es falso, otra cosa. Para ello, primero calculamos las posibles salidas. El caso de $zx$, calculamos x y una fila de ceros. Luego, al multiplexor, pasamos como entrada los valores calculamos y elegimos en función del selector zx. Para zy, nx, ny, f y "no", realizamos la misma operación, en forma de árbol.

![Screenshot_20230921_153544](https://github.com/jorge1b3/G_Poject/assets/16739365/7913e644-09bc-498c-b943-96abfb9849c7)

Ahora, debemos considerar dos salidas más, zr y ng. Para zr, es sencillo. Con un "or" observamos si alguna de los bits de la salida es igual a 1 (lo hacemos en cadena para usar or8way). Luego, negamos la salida. Así, si al menos uno de los elementos es 1, la salida es false. Si todos son 0, es true.

Para ng, tomamos el el bit más a la izquierda de la salida, out[15], pues este representa el signo y lo comparamos con un and y una de las entradas en true, haciendo que la salida solo dependa del signo. Si es 1, es negativo, y si no, positivo.
