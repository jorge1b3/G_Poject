# Suma 16

| a | b | out | carry |
|---|---|-----|-------|
| 0 | 0 |  0  |   0   |
| 0 | 1 |  1  |   0   |
| 1 | 0 |  1  |   0   |
| 1 | 1 |  0  |   1   |

Para realizar la suma, observamos que la salida de la suma es la operación XOR entre los dos bits de entrada, y el carry es la operación AND entre los dos bits de entrada. Por lo tanto, la suma se puede realizar con una compuerta XOR y una compuerta AND.
