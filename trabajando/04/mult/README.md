# Mult 

El código de mult funciona de la siguiente manera:
 1. Se tiene una variable, en nuestro caso en la posición de memoria 2, que contiene el resultado de la multiplicación
 2. Se tiene una variable, en nuestro caso en la posición de memoria 1, que contiene el multiplicando
 3. Se tiene una variable, en nuestro caso en la posición de memoria 0, que contiene el multiplicador

Creamos un iterador i, que va a llevar la cuenta de las veces que se ha sumado el multiplicando, y lo inicializamos a 1.

Lo primero que hacemos es verificar cual de los 2, es el mayor, y utlizando esto, hacemos el número de iteraciones igual al menor, y sumamos el mayor, el número de veces del menor.

Para hacer esto, hacemos una resta de los valores. Así
```hack
@0
D=M
@1
D=D-M
```

Por lo que si el valor es negativo, el mayor es el valor en la posición 1, y si es positivo, el mayor es el valor en la posición 0. Luego, pasamos a la parte de la suma.

Tomando la variable que se encuentra en el mayor, iteramos i veces, y sumamos el valor del menor a la variable que contiene el resultado. Para verificar si el iterador terminó, se le resta a i el valor del menor, y si es positivo, significa que el iterador superó al menor, así que termina la iteración.

