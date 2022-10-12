### 【Requisito previo】
#### 〔Python y Visual Studio Code〕
Antes de esta práctica en concreto, es necesario descargar todo lo necesario para empezar a programar con Python. En mi caso, descargué Python desde la página principal de Python, en conjunto con el entorno de desarrollo Visual Studio Code

1. Entrar al siguiente enlace: [**Python**](https://www.python.org/)
![Python](https://i.imgur.com/QLUjzQl.png)
> Página de Python.
2. Damos clic en **Downloads** y en mi caso **Download for Windows**.
3. Lo instalamos como cualquier programa.

4. Después, vamos a este otro enlace: [**Visual Studio Code**](https://code.visualstudio.com/)
![Visual Studio Code](https://i.imgur.com/cfSIYhG.png)
> Página de Visual Studio Code.

5. Clic en **Download for Windows** y repetimos el mismo proceso del paso 3.

Con esto, nos aseguramos de tener:
- Python listo para ser usado en nuestra PC.
- Un entorno que interprete las ejecuciones de Python.

# 【Python】

![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/240px-Python-logo-notext.svg.png)

**Tabla de Contenidos**

 - [Introducción a Python](#introducción-a-python)
    - [Características del lenguaje](#características-del-lenguaje)
    - [El intérprete de Python](#el-intérprete-de-python)
        - [¿Qué versión de Python tengo instalada?](#¿qué-versión-de-python-tengo-instalada)
        - [Primer programa en Python](#primer-programa-en-python)
    - [Operadores, expresiones y sentencias en Python](#operadores-expresiones-y-sentencias-en-python)
        - [Operador](#operador)
        - [Expresión](#expresión)
        - [Sentencia](#sentencia)
    - [Bloques de código (Indentación)](#bloques-de-código-indentación)
    - [Palabras reservadas de Python](#palabras-reservadas-de-python)
    - [Comentarios en Python](#comentarios-en-python)
    - [Constantes en Python](#constantes-en-python)
- [Practica 3: Python básico](#practica-3-python-básico)
    - [Programa #1: Hola mundo](#programa-1-hola-mundo)
    - [Programa #2: Saludo](#programa-2-saludo)
    - [Programa #3: Tipos de Variables](#programa-3-tipos-de-variables)
    - [Programa #4: Condicionales](#programa-4-condicionales)
    - [Programa #5: Arreglos](#programa-5-arreglos)

-------

# 【Introducción a Python】
Python es un lenguaje de programación de propósito general muy poderoso y flexible, a la vez que sencillo y fácil de aprender. Es un lenguaje de alto nivel, que permite procesar fácilmente todo tipo de estructuras de datos, tanto numéricos como de texto.

![](https://www.alvarodeleon.net/wp-content/uploads/2019/08/1566031787-cda5d6086d4ce18478c4843bea602476.jpg)

## 〔Características del lenguaje〕

Las principales características de Python son las siguientes:
- **Es multiparadigma**, ya que soporta la programación imperativa, programación orientada a objetos y funcional.
- **Es multiplataforma**: Se puede encontrar un intérprete de Python para los principales sistemas operativos: Windows, Linux y Mac OS. Además, se puede reutilizar el mismo código en cada una de las plataformas.
- **Es dinámicamente tipado**: Es decir, el tipo de las variables se decide en tiempo de ejecución.
- **Es fuertemente tipado**: No se puede usar una variable en un contexto fuera de su tipo. Si se quisiera, habría que hacer una conversión de tipos.
- **Es interpretado**: El código no se compila a lenguaje máquina.

> ❗ El hecho de que Python sea **interpretado** quiere decir que **hace falta un intérprete** que permita ejecutar un programa o script escrito en Python sin necesidad de compilarlo.

## 〔El intérprete de Python〕
Cuando instalas Python correctamente (en cualquier sistema operativo) ocurren, entre otras, dos cosas: se añade el comando `python` (o `python3`, en caso de que instales la versión 3.x de Python) al path y se instala el intérprete de Python correspondiente.

### 〔¿Qué versión de Python tengo instalada?〕
Si ya has instalado Python, abre una consola o terminal y ejecuta el comando `python3`. Este comando lanzará el intérprete de Python correspondiente. Debes ver algo similar a esta imagen:
![](https://j2logo.com/wp-content/uploads/introduccion-a-python-version.png)
> Imagen de referencia

Si te fijas bien, en la primera línea podemos ver la versión del intérprete de Python que tenemos instalado en nuestro ordenador. En el caso de la imagen de referencia, su version es la 3.7.4.

En el intérprete de Python podemos escribir expresiones e instrucciones que este interpretará y ejecutará, como veremos a continuación.

### 〔Primer programa en Python〕
Normalmente, los programas en Python se escriben en archivos con la extensión `.py`. Estos archivos se pasan al intérprete de Python para que los interprete y ejecute.

Vamos a verlo con un ejemplo. Crea con un editor de texto un fichero llamado `suma.py` con el siguiente contenido:

```javascript
suma = 2 + 3
print(suma)
```

A continuación abre un terminal, sitúate en el directorio en el que creaste el archivo `suma.py` y ejecuta lo siguiente:

```javascript
python3 suma.py
```
En el terminal verás que aparece el número `5` como resultado de ejecutar el programa anterior. 

> Esta es la manera más común de crear y ejecutar programas en Python.

## 〔Operadores, expresiones y sentencias en Python〕
En esta sección se aprenderá la diferencia entre operador, expresión y sentencia, ya que son las formas básicas que componen la estructura de cualquier programa.

### 〔Operador〕
Un **operador** es un carácter o conjunto de caracteres que actúa sobre una, dos o más **variables** y/o **literales** para llevar a cabo una **operación** con un **resultado** determinado.

Ejemplos de operadores comunes son los operadores aritméticos `+` (suma), `-` (resta) o `*` (producto), aunque en Python existen otros operadores.

### 〔Expresión〕
Una expresión es una unidad de código que devuelve un valor y está formada por una combinación de operandos (variables y literales) y operadores. Los siguientes son ejemplos de expresiones (cada línea es una expresión diferente):

```javascript
5 + 2  # Suma del número 5 y el número 2
a < 10  # Compara si el valor de la variable a es menor que 10
b is None  # Compara si la identidad de la variable b es None
3 * (200 - c) # Resta a 200 el valor de c y lo multiplica por 3
```

### 〔Sentencia〕
Por su parte, una sentencia o declaración es una instrucción que define una acción. Una sentencia puede estar formada por una o varias expresiones, aunque no siempre es así.

En definitiva, las sentencias son las instrucciones que componen nuestro programa y determinan su comportamiento.

Ejemplos de sentencias son la asignación **=** o las instrucciones **if**, **if ... else ...**, **for** o **while** entre otras.

> ❗ Una sentencia está delimitada por el carácter `Enter (\n)`.

## 〔Bloques de código (Indentación)〕
Un bloque de código es un grupo de sentencias relacionadas bien delimitadas. A diferencia de otros lenguajes como JAVA o C, en los que se usan los caracteres `{}` para definir un bloque de código, en Python se usa la indentación o sangrado.

El sangrado o indentación consiste en mover un bloque de texto hacia la derecha insertando espacios o tabuladores al principio de la línea, dejando un margen a la izquierda.

> 👉🏻 Esta es una de las principales características de Python.

Un bloque comienza con un nuevo sangrado y acaba con la primera línea cuyo sangrado sea menor. De nuevo, la guía de estilo de Python recomienda usar los espacios en lugar de las tabulaciones para realizar el sangrado.

> ❗️ Configura tu IDE de desarrollo para que use los espacios en lugar de los tabuladores para el sangrado. Establece el número de espacios a 4 ó 2.

Ejemplo: 

```javascript
def suma_numeros(numeros):  # Bloque 1
    suma = 0                # Bloque 2
    for n in numeros:       # Bloque 2
        suma += n           # Bloque 3
        print(suma)         # Bloque 3
    return suma             # Bloque 2
```

Debes comprender que en la línea 1 se define la función `suma_numeros`. El cuerpo de esta función está definido por el grupo de sentencias que pertenecen al bloque 2 y 3. A su vez, la sentencia `for` define las acciones a realizar dentro de la misma en el conjunto de sentencias que pertenecen al bloque 3.

## 〔Palabras reservadas de Python〕
Python tiene una serie de palabras clave **reservadas**, por tanto, **no pueden usarse como nombres de variables, funciones, etc.**

Estas palabras clave se utilizan para definir la sintaxis y estructura del lenguaje Python.

La lista de palabras reservadas es la siguiente:

`and`, `as`, `assert`, `break`, `class`, `continue`, `def`, `del`, `elif`, `else`, `except`, `False`, `finally`, `for`, `from`, `global`, `if`, `import`, `in`, `is`, `lambda`, `None`, `nonlocal`, `not`, `or`, `pass`, `raise`, `return`, `True`, `try`, `yield`, `while` y `with`

## 〔Comentarios en Python〕
Como cualquier otro lenguaje de programación, Python permite escribir comentarios en el código. Los comentarios son útiles para explicar por qué estamos programando algo de un modo concreto o añadir indicaciones. Te aseguro que son de utilidad cuando se retoma un programa o aplicación en el futuro

Los comentarios son ignorados por el intérprete de Python. Solo tienen sentido para los programadores.

Para añadir un comentario a tu código simplemente comienza una línea con el carácter `#`:

```javascript
# Esta línea es un comentario

a = 5

# Resultado de multiplicar a por 2
print(a * 2)
```

## 〔Constantes en Python〕
Terminamos esta introducción a Python señalando que, a diferencia de otros lenguajes, **en Python no existen las constantes**.

Entendemos como _constante_ una variable que una vez asignado un valor, este no se puede modificar. Es decir, que a la variable no se le puede asignar ningún otro valor una vez asignado el primero.

Se puede simular este comportamiento, siempre desde el punto de vista del programador y atendiendo a convenciones propias, pero no podemos cambiar la naturaleza mutable de las variables.

No obstante, sí que es cierto que el propio Python define una serie de valores constantes en su propio namespace. Los más importantes son:

- **False:** El valor _false_ del tipo `bool`.
- **True:** El valor _true_ del tipo `bool`.
- **None:** El valor del tipo `NoneType`. Generalmente `None` se utiliza para representar la ausencia de valor de una variable.

--------------

# 【Practica 3: Python básico】
Una vez realizados los pasos previos, abriremos nuestro entorno de desarrollo.
![](https://i.imgur.com/5nLMrIN.png)
Veremos una interfaz como en la imagen. y podemos empezar a crear nuestros archivos en la parte señalada.

Es muy importante esta parte. Podemos colocar el nombre que quedamos a nuestro archivo, sin embargo, es necesario especificar la extension del lenguaje con el que se quiera trabajar. VSCode es un entorno que trabaja con multiples lenguajes de programación, por ende, si nosotros escribimos un nombre sin especificar la extensión, lo tomará como un archivo sin tipo y no se podrá interpretar de ninguna forma.
![](https://i.imgur.com/rujBs15.png)
> Para Python, su extención correspondiente es `.py`.

## 〔Programa #1: Hola mundo〕
1. Creamos nuestro archivo con el nombre `Holamundo.py`

![](https://i.imgur.com/GrPr3IV.png)

2. La primera linea de código es un comentario indicando la función del programa.

3. Creamos un `print` con la siguiente cadena de texto "*Hola mundo*".

4. Para ejecutar el programa, vamos a darle clic al botón **play**, desplegamos las opciones, y luego en **Run Python File**. 

![](https://i.imgur.com/S0Mw2f3.png)

5. Se nos abrirá la consola/terminal donde nos mostrará **nombre de la terminal** (en este caso PowerShell), **ruta del archivo ejecutado** y **ejecución** (lo que esta ejecutando el programa).

![](https://i.imgur.com/vpPD4G9.png)
> Señalé en rojo la ejecución o acción realizada por nuestro programa. En este caso el Print de "Hola mundo".

## 〔Programa #2: Saludo〕
1. Creamos nuestro archivo con el nombre `saludo.py`

![](https://i.imgur.com/1nF2mpz.png)

2. Creamos una variable llamada `nombre` en la cual se almacenará un dato. Este dato, será uno el cual proporcione el usuario (el usuario lo escribirá, y el programa lo almacenará en nombre).

3. Para ello, le asignamos la palabra reservada `input` la cual cumple la función de recibir texto o dígitos del usuario por medio de la consola. A este input, le anexamos una cadena de texto para preguntarle al usuario "*¿Como te llamas?*"

4. Cuando el programa se ejecute, te preguntará *¿Como te llamas?* y seguido de ello, podrás escribir lo que quieras. Eso será almacenado por el programa para proceder con lo siguiente.

5. En la tercera linea, hacemos un `print` **concatenado**. Lo que significa esto, es que vamos pedirle al print que imprima tanto un texto, como una variable, todo en una misma linea y misma oración. Es como pedirle que "sume" ambos textos, y los escriba todo en una sola oración.

6. Para lograrlo, escribimos primero nuestro texto que el usuario recibirá, en este caso un "Hola", separamos con una coma, y luego concatenamos el nombre del usuario con un `+` seguido de nuestra variable nombre.

7. Al ejecutar el programa nos saldrá lo siguiente.

![](https://i.imgur.com/EzBHExW.png)

> Señalé en 🟢Verde la parte en donde el programa me pide mi nombre. Y en 🔴Rojo donde el programa usa mi nombre para la concatenación.

## 〔Programa #3: Tipos de Variables〕
Este programa está conformado de varias secciones pequeñas que explican cada apartado de "Tipos de variables"

1. Una vez creado nuestro archivo de nombre `tiposVariables.py`, podemos empezar a trabajar con lo siguiente:

**Strings**. Es todo aquello que engloba una cadena de texto o cadena de carácteres. Por ejemplo: *Roberto*, *Alfonso*, *Tres*, *Manzana*, etc.

![](https://i.imgur.com/ny05fIm.png)

2. Aquí tenemos una variable llamada `nombre` que contiene el `String` "Roberto".
3. Seguido de eso, lo mandamos a imprimir con `print`
> Al final del tema, mostraré la consola con los resultados.

**Int**. Hace referencia a numeros enteros sin decimal. Por ejemplo: *3*, *18*, *154*, *2606*, etc.

![](https://i.imgur.com/WkZHbQl.png)

4. Aquí tenemos una variable llamada `edad` que contiene el `Int` "21".
5. Seguido de eso, lo mandamos a imprimir con `print` con una concatenación de `+`. Recordemos que estamos trabajando con numeros, por lo que las operaciones básicas aritméticas son válidas aquí.

6. **NOTA**: la diferencia entre **edad** y **edads**, aunque parezca que por usar números, funcionaría de la misma forma, **edad** está siendo considerado un **INT** y **edads** se considera un **STRING**, esto es debido a que el número 26 está contenido entre comillas (").
Por ende, las operaciones aritméticas serán invalidas en **edads** y el programa imprimirá de forma erronea *2626*

**Float**. Hace referencia a numeros con decimal. Por ejemplo: *0.5*, *3.1415*, *7.24*, *1.024*, etc.

![](https://i.imgur.com/DMylyMM.png)

7. Aquí tenemos una variable llamada `pi` que contiene el `Float` "3.141592"(los primeros digitos de pi).

8. ¿Como sabemos que estamos trabajando con un flotante? Esto se nota cuando un número entero pasa a tener un **punto decimal**. Python automaticamente interpreta que estamos trabajando con un `float`.

9. **Dato importante**, en la siguiente linea, podemos ver que trabajamos con la variable anterior `edad`, pero recordemos que esa variable es de tipo `int`, por ende, usando la función `float()` somos capaces de "Castetar" esa variable a **flotante** y asignarsela de nuevo a `edad`.

10. Luego, mandamos a imprimir ambas variables. Se daran cuenta como **edad** pasó de ser `int` a ser `float`.

**Bool**. Son las variables de decisión, solo puede ser **si** o **no**.

![](https://i.imgur.com/zJglCtr.png)

11. Este es más sencillo. Colocamos dos variables, **diaLluvioso** y **diaSoleado**, y les asignamos *False* y *True* respectivamente

12. Después los mandamos a imprimir en consola. Deberia mostrarnos el valor de los booleanos, o sea, false y true.

![](https://i.imgur.com/CHERz7j.png)

Aquí podemos ver los resultados de la ejecución, tras todos los códigos realizados.
- `String` = **Roberto**
- `Int(edad+edad)` = **42**
- `Int(edads+edads)` = **2626** *recordemos que este es un error.*
- `Float(pi)` = **3.141592**
- `Float(edad)` = **21.0**
- `Type(nombre,edad)` = **[str] [float]**
- `Bool(diaLluvioso,diaSoleado` = **False - True**

## 〔Programa #4: Condicionales〕
Creamos un archivo de nombre `condicionales.py`. Aquí veremos dos ejemplos de como podemos hacer que un programa interactue de varias formas dependiendo de las acciones del usuario (En este caso, vamos a darle valores numericos al programa).

Ahora, el primer programa.

1. Nuestro primer programa, como indica el comentario, es un verificador de calificaciones. Este cumplirá la función de decirnos si, al ingresar una calificación, hemos aprobado, reprobado o sacamos la calificación justa para pasar.

2. Primero, declaramos nuestra variable `calificacion`, que tendrá un `input` que diga "*Introduce tu calificación:*". Aquí es donde el usuario ingresará el número de su calificación a ser evaluada.
![](https://i.imgur.com/4MKFRUG.png)

3. Seguido de ello, los números que ingresa el usuario serán de tipo `String`, por ende, las convertiremos a tipo `Int` con la linea número 4.

4. Ahora pasamos a la parte de condiciones. Podemos ver nuevas palabras reservadas, tales como: `if`, `elif` y `else`.

- **if**, viene a significa "Si". Podemos interpretarlo de la siguiente forma. _**Si** ocurre esto, haz esto_. _**Si** calificación es menor a 700, imprime calificación reprobatoria_ (como vemos en las lineas 7 y 8)
- **elif**, significaría "Sino, si". Se interpreta de la siguiente manera. _Se debe cumplir lo anterior. **Si no**, **Si** ocurre esto otro, haz esto._
- **else**, significa "Si no". Se interpreta de esta forma. _Debio haberse cumplido alguno de los anteriores. **Si no**, haz esto_

5. Ahora podemos explicar todo lo demás.

6. Empezamos con un `if` que nos dice que `calificacion` es menor a 700. Entonces haz un `print` de "_Calificación reprobatoria_".
7. Si no se cumplió eso, entra en acción el `elif` y nos asigna una nueva condición de `calificacion` es igual a 700. Entonces haz un `print` de "_Calificación minima aprobatoria_".

![](https://i.imgur.com/X4lQBuy.png)

8. Si no se cumplió eso, entra en acción el segundo `elif` y nos asigna una nueva condición de `calificacion` es mayor a 1000. Entonces haz un `print` de "_No es posible sacar una calificación mayor a 1000_". (Aquí nos aseguramos de que nadie ponga una cantidad que supere 1000)

9. Y ahora, si nada de lo anterior se cumplió, pasamos a `else`. Hay que tener en cuenta que en else, no se asigna nuevas reglas, porque este apartado es en caso de que todo falle, y es como un estado por defecto que se asignará cuando no hayan condiciones especiales por analizar. El estado por defecto, será un `print` que diga "*Felicidades, tu calificación es aprobatoria*"

Ahora el segundo programa.

1. Nuestro segundo programa, como indica el comentario, es un verificador de edad. Este cumplirá la función de decirnos si después de ingresar nuestra edad, podemos ingresar al club nocturno, si no podemos ingresar, si nuestra edad es negativa o si superamos los 100 años.

2. Primero, declaramos nuestra variable `edad`, que tendrá un `input` que diga "*Introduce tu edad:*". Aquí es donde el usuario ingresará el número de su edad a ser evaluada.

![](https://i.imgur.com/myle46D.png)

3. Seguido de ello, los números que ingresa el usuario serán de tipo `String`, por ende, las convertiremos a tipo `Int` con la linea número 4.

4. Empezamos con un `if` que nos dice que `edad` es **mayor o igual** a 18 **y** `edad` es **menor o igual** a 100. Entonces haz un `print` de "_¡Bienvenido, puedes pasar!_".
> Es importante hacer énfasis en las parte negritas, puesto que esas son las condiciones que necesitamos para que se cumpla ese `if`. "and" sirve como "y", significa que deben cumplirse ambas condiciones para que el `if` se ejecute.

5. Si no se cumplió eso, entra en acción el `elif` y nos asigna una nueva condición de `edad` es mayor a 100. Entonces haz un `print` de "_No pueden ingresar personas de edad avanzada_". (Verificación de gente anciana)

![](https://i.imgur.com/kY92a5V.png)

6. Si no se cumplió eso, entra en acción el segundo `elif` y nos asigna una nueva condición de `edad` es menor a 0. Entonces haz un `print` de "_No existen edades negativas_". (Verificación de edad negativa, por si alguien quiere poner -18 años)

7. Para terminar, si nada de lo anterior se cumplió, pasamos a `else` que será un `print` que diga "*No pueden entrar menores de edad*" (En caso de no cumplir los 18, deberá salir este mensaje diciendo que no puedes pasar)

Estos son los resultados de una ejecución del programa.

![](https://i.imgur.com/FDhjXNL.png)

En mi caso, yo puse una calificación de 850, y me salió "*Felicidades, tu calificación es aprobatoria*".
De igual forma, puse una edad de 21, y me salió el mensaje "*¡Bienvenido, puedes pasar!*"


## 〔Programa #5: Arreglos〕
Para finalizar, voy a explicar el ultimo programa que realicé, donde hago una pequeña explicación sobre los arreglos.

Las listas en Python forman parte de lo que se conoce como estructuras de datos que nos ofrece Python (son un tipo de array). En otros lenguajes de programación, se los conoce como vectores. Las listas en Python son utilizadas para almacenar múltiples valores en una única variable.

> Recordemos que las listas empiezan a contarse desde 0.

1. La primera lista se llama `listaNumeros`, y como su propio nombre lo indica, solo contiene números. En la segunda podemos ver que igualmente podemos almacenar `Strings` entre comillas.

2. Y luego, mandar a imprimir la lista de números con `print` y el nombre de la lista.

![](https://i.imgur.com/4Uk8RL5.png)

3. También podemos imprimir un solo valor dentro de una lista de objetos, por ejemplo, en la segunda lista, tenemos nombres, pero solo quiero imprimir el **numero 3**, referente a **Diego**. Para eso, hacemos un `print`, y al final de `listaNombres`, ponemos el index al que queremos referirnos, o sea `[3]` (se coloca entre corchetes).

4. Podemos saber el tamaño de la lista de elementos, con la función **len**. Al momento de imprimir con `print`, especificamos que queremos el `len` de `listaElementos`.

5. De igual forma, podemos agregar elementos a una lista ya predefinida mediante la opción `.append(" ")` y entre las comillas, el elemento que será agregado.

6. Después, imprimir la lista.

![](https://i.imgur.com/UBbgGuh.png)

7. Por ultimo, podemos eliminar elementos a una lista mediante la opción `.pop(X)` y sustituimos la X por el número index, del elemento que queremos eliminar dentro de la lista.

8. Después, imprimir la lista.

Aquí podemos ver los resultados de las impresiones de las listas.

![](https://i.imgur.com/bcPCC0T.png)

- Imprimimos la `listaNumeros`: **[1, 2, 3, 4, 5]**
- Imprimimos el elemento `Diego` de la `listaNombres`: **Diego**
- Imprimimos el tamaño de la `listaElementos`: **6**
- Agregamos el elemento `Mango` a la `listaFrutas1`: **['Manzana', 'Melon', 'Uvas', 'Sandia', '_Mango_']**
- Eliminamos el elemento `Manzana` de la `listaFrutas2`: **['Melon', 'Uvas', 'Sandia']**