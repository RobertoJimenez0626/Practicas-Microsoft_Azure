### 【Requisito previo】
#### 〔Azure Sponsorships〕
Antes de empezar con cualquiera de las practicas mostradas por su servidor, es necesario verificar si contamos con la posibilidad de emplear las herramientas de Microsoft Azure.
Para ello, es necesario realizar la siguiente verificación:

1. Entrar al siguiente enlace: [**Microsoft Azure Sponsorships**](https://www.microsoftazuresponsorships.com/)
![Azure Sponsorships](https://i.imgur.com/OxY5WPf.png)
> Página de Microsoft Azure Sponsorships.

2. Después, hacemos clic en el apartado de **Check Your Balance**
![Azure Balance](https://i.imgur.com/e65k3qe.png)
> Balance de Azure.

3. En este apartado podemos **verificar** los siguientes datos:
- **Total de Crédito** de Azure: En este caso, tenemos un **total** de $100 USD.
- **Usado**: Crédito que hemos usado o **gastado** a lo largo del tiempo.
- **Restante**: Crédito con el cual **contamos** para su respectivo uso en la plataforma.
- **Suscripciones**: Cantidad de suscripciones que se encuentran **Activas** y que estan ligadas a nuestro Saldo/Crédito de Azure Sponsorships.
- Y por ultimo, la **dirección de correo** de nuestra cuenta de Azure.

Con esto, ya podemos saber si disponemos del uso de los servicios de Azure. Para una mayor comprobación, se puede intentar crear cualquier recurso de Azure, y si no existe restricción de algún tipo significaría que vamos por buen camino.

Una vez dicho todo esto, podemos empezar.

---

**Tabla de Contenidos**

 - [Introducción a Custom Vision](#introducción-a-custom-vision)
    - [¿Qué hace?](#qué-hace)
    - [Clasificación y detección de objetos](#clasificación-y-detección-de-objetos)
    - [Optimization](#optimization)
    - [¿Qué incluye?](#qué-incluye)
    - [Copia de seguridad y recuperación ante desastres](#copia-de-seguridad-y-recuperación-ante-desastres)
    - [Seguridad y privacidad de datos](#seguridad-y-privacidad-de-datos)
    - [Residencia de datos](#residencia-de-datos)
- [Practica 15](#practica-15-uso-de-custom-vision)
    - [Crear y configurar un nuevo proyecto](#crear-y-configurar-un-nuevo-proyecto)
    - [Añadiendo imágenes para aprendizaje](#añadiendo-imágenes-para-aprendizaje)
    - [Añadiendo un TAG Negativo](#añadiendo-un-tag-negativo)
    - [Entrenamiento de la IA](#entrenamiento-de-la-ia)
    - [Pruebas de reconocimiento](#pruebas-de-reconocimiento)

-------

# 【Introducción a Custom Vision】

![](https://i0.wp.com/sebastianbirk.org/wp-content/uploads/2021/08/azure_custom_vision.png?fit=1600%2C900&ssl=1)

*Azure Custom Vision* es un servicio de reconocimiento de imágenes que permite compilar, implementar y mejorar sus propios identificadores de imágenes. Los identificadores de imágenes aplican etiquetas a las imágenes en función de sus características visuales. Cada etiqueta representa una clasificación u objeto. A diferencia del servicio Computer Vision, Custom Vision te permite especificar sus propias etiquetas y entrenar modelos personalizados para detectarlas.

![](https://docs.microsoft.com/es-es/azure/cognitive-services/custom-vision-service/media/overview/image-example.png)

### 〔¿Qué hace?〕
El servicio Custom Vision usa un algoritmo de aprendizaje automático para analizar las imágenes. Primero, debe enviar grupos de imágenes que presenten y carezcan de las características en cuestión. Las imágenes se etiquetan con sus propias etiquetas personalizadas en el momento del envío. Después, el algoritmo se entrena con esos datos y calcula su propia precisión probándose a sí mismo con esas mismas imágenes. Una vez que el modelo se haya entrenado, puede probarlo y volver a entrenarlo hasta que pueda usarlo en la aplicación de reconocimiento de imágenes para clasificar imágenes o detectar objetos. También puede exportar el mismo modelo para su uso sin conexión.

### 〔Clasificación y detección de objetos〕
La funcionalidad de Custom Vision puede dividirse en dos características. La clasificación de las imágenes aplica una o varias etiquetas a una imagen completa. La detección de objetos es similar, pero también devuelve las coordenadas de la imagen donde pueden encontrarse las etiquetas aplicadas.

### 〔Optimization〕
El servicio Custom Vision está optimizado para reconocer rápidamente las diferencias principales entre las imágenes, para que pueda empezar a crear el prototipo de su modelo con una pequeña cantidad de datos. Cincuenta imágenes por etiqueta suele ser un buen comienzo. Sin embargo, el servicio no es óptimo para detectar diferencias sutiles en las imágenes (por ejemplo, detectar grietas menores o abolladuras en escenarios de control de calidad).

Además, puede elegir entre distintas variaciones del algoritmo de Custom Vision que están optimizadas para imágenes con cierto material temático, por ejemplo, puntos de referencia o artículos en venta. Para obtener más información, vea Selección de un dominio.

### 〔¿Qué incluye?〕
El servicio Custom Vision está disponible como un conjunto de SDK nativos, así como mediante una interfaz basada en web desde el portal de Custom Vision. Puede crear, probar y entrenar un modelo mediante cualquiera de las interfaces, o usar ambas.


### 〔Copia de seguridad y recuperación ante desastres〕
Como parte de Azure, Custom Vision Service incluye componentes que se ofrecen en varias regiones. Todos nuestros servicios se ofrecen de forma continua a los clientes en las regiones y zonas de servicio. Para más información sobre las regiones y zonas, consulte Regiones de Azure. Si necesita información adicional o tiene algún problema, póngase en contacto con el equipo de soporte técnico.

### 〔Seguridad y privacidad de datos〕
Al igual que sucede con todas las instancias de Cognitive Services, los desarrolladores que usan Custom Vision Service deben estar al tanto de las directivas de Microsoft sobre los datos de clientes. Para más información, consulte la página de Cognitive Services en Microsoft Trust Center.

### 〔Residencia de datos〕
Custom Vision no replica los datos fuera de la región especificada, excepto en el caso de una región, `NorthCentralUS`, donde no hay soporte técnico local de Azure.


--------------

# 【Practica 15: Uso de Custom Vision〕
Para esta práctica usaremos otra página externa de Azure, llamada *Custom Vision*, a la cual podemos acceder desde **[aquí](https://www.customvision.ai/)**.

Y entraremos a un portal web como el siguiente:

![](https://i.imgur.com/43ZrRT8.png)

Para empezar, daremos clic en *Sign in* para logearnos con nuestra cuenta de Azure. Aceptamos los términos de servicio.

![](https://i.imgur.com/Qx0CAr5.png)

### 〔Crear y configurar un nuevo proyecto〕
Vamos a empezar creando un nuevo proyecto donde realizaremos el anexado de imágenes y los tags.

1. Hacemos clic en *New project*.

![](https://i.imgur.com/xngcdS6.png)

2. Asignamos un *nombre* y una *descripción*. En resource, seleccionamos el que queramos, pero como estamos trabajando desde cero, no tenemos ninguno. Por lo tanto, debemos crear uno.

![](https://i.imgur.com/rsg0laQ.png)

3. Para crearlo, damos clic en *create new*. Se nos desplegará una ventana como ésta.

![](https://i.imgur.com/LAz6eAL.png)

4. Llenamos los valores que nos pide, hasta el apartado de Grupo de recursos, el cual tampoco tenemos, por ende, también lo crearemos desde cero. Clic en *create new*.

![](https://i.imgur.com/sqcBBum.png)

5. Aquí es un poco más sencillo, solo nos solicita *nombre* y *localización*. Damos clic en *Create resource group*.

![](https://i.imgur.com/rGiVoW6.png)

6. Ahora si, podemos elegir nuestro grupo de recursos correspondiente, al igual que completar los campos vacíos restantes.

![](https://i.imgur.com/QP7qsaj.png)

7. Pulsamos el botón *Create resource*.

![](https://i.imgur.com/Brr94yk.png)

8. Aparecerán más opciones a configurar con respecto al tipo de IA que utilizaremos. El *tipo de proyecto* será *Clasificación*, y el *tipo de clasificación* usaremos *Multiclase*. Ahora, en *dominio*, es el tipo de inteligencia de reconocimiento que usaremos, en este caso, usaremos de tipo *general A2*.

![](https://i.imgur.com/jzd9GM4.png)

9. Después, hacemos clic en *Create project*.

### 〔Añadiendo imágenes para aprendizaje〕
En esta sección, le daremos unas imágenes de muestra a nuestra IA para que sean analizadas y aprenda de ellas.

Las imágenes pueden ser de cualquier lado, yo opté por imágenes sacadas de *Google imágenes*.

Las categorías fueron:

- Galaxias
- Nebulosas
- Planetas
- Estrellas (negativo)

1. Primero, una vez teniendo todas las imágenes deseadas, procederemos a hacer clic en *Add images*.

![](https://i.imgur.com/9bmRlYE.png)

2. Se nos abrirá el explorador de archivos, y podemos elegir que imagen o imágenes usar. (Podemos seleccionar tantas queramos)

![](https://i.imgur.com/jfO6N9H.png)

> Esta primera tanda de imágenes son de **Galaxias**.

3. Una vez que Custom Vision sepa qué queremos subir, nos pedirá poner categorías a las imágenes (también llamados **Tags**). Esto será para hacer una clasificación más ordenada de cada uno de los elementos.

![](https://i.imgur.com/ktoozHg.png)

4. En este caso, el Tag será *Galaxia*. Después, hacemos clic en *Upload files*.

5. Esperamos a que termine de procesar.

![](https://i.imgur.com/OhDduVV.png)

6. Es muy probable que algunas imágenes sean incapaces de subirse, y esto se debe a la compatibilidad de formatos de imagen que acepta Custom Vision.

![](https://i.imgur.com/cF7TWk3.png)

7. Repetimos el mismo proceso con las siguientes tandas de imágenes.

![](https://i.imgur.com/VYqiF8w.png)

> Esta tanda de imágenes son **Nebulosas**.

![](https://i.imgur.com/XMrdu5q.png)
![](https://i.imgur.com/piVnZ5v.png)
![](https://i.imgur.com/2jaM2va.png)

> Esta tanda de imágenes son **Planetas**.

![](https://i.imgur.com/GkMvlCg.png)
![](https://i.imgur.com/fvyz5lZ.png)
![](https://i.imgur.com/Z3rD03q.png)

### 〔Añadiendo un TAG Negativo〕
Para ésta sección, luego de agregados los elementos que deseamos que nuestra IA sea capaz de reconocer, debemos agregar una Tag "Especial".

**¿A qué se refiere con Tag negativo?** 

Esto hace referencia a todo aquello que nosotros no queramos que nuestra IA interprete de una imagen. 

Por ejemplo: supongamos que le enviamos una imagen completamente llena de estrellas, pero sin ninguno de los elementos antes mencionados. La IA se confundirá e interpretará de forma erronea toda la imagen; no sabrá como clasificarla y elegirá lo que ella crea que es.

1. Tomemos esta imagen de referencia, vamos a decirle a la IA que ésta imagen no contienen ninguno de los tags antes usados. Por ende, será el tag que queremos que él reconozca como "neutro".

![](https://i.imgur.com/Zs5PKGb.png)

2. Descargamos la cantidad que nosotros deseemos.

![](https://i.imgur.com/tcV46Ly.png)

3. Las subimos, y en Tag ponemos *Negativo*.

![](https://i.imgur.com/CqREOTw.png)

4. Hacemos clic en *Upload*.

![](https://i.imgur.com/2AWrlG9.png)

5. Y esperamos a que termine el proceso.

![](https://i.imgur.com/zRinwm8.png)
![](https://i.imgur.com/x4LZEDR.png)


### 〔Entrenamiento de la IA〕
Ahora, la parte más importante de la práctica será "entrenar la IA". 

1. Vamos a hacer clic en *Train*.

![](https://i.imgur.com/hWolvpA.png)

2. Nos aparecerá este recuadro emergente, preguntandonos que tipo de entrenamiento queremos. El primero es el *Quick train* que es entrenamiento "default". Y el segundo es el *Avanzado*, en el cual nos permite elegir la cantidad de horas que queremos dejar entrenando la IA. Para fines educativos, elegiremos la primera.

![](https://i.imgur.com/BpZWgCs.png)

3. Empezará el entrenamiento. Tenemos que esperar a que termine según lo que nos había previsto el CV.

![](https://i.imgur.com/jSKO88A.png)

También podemos ajustar el *Threshold*, que es la probabilidad para que una predicción sea válida al calcular la precisión (precision) y la recuperación (recall). Por ahora lo dejaremos en 50% por defecto.

![](https://i.imgur.com/B7R7lb4.png)

4. Una vez terminado, nos dejará unos resultados como éstos:

- Precision
- Recall
- AP

![](https://i.imgur.com/ewSwggx.png)

**Precision**
Este valor significa algo así: *si tu modelo predice una etiqueta, ¿cuál es la probabilidad de que sea correcta?*

![](https://i.imgur.com/5yUCjvp.png)

**Recall**
Este valor significa algo así: *de las etiquetas que deben predecirse correctamente, ¿qué porcentaje encontró correctamente su modelo?*

![](https://i.imgur.com/0WkYEjq.png)

**AP**
Una medida del rendimiento del modelo, resume la precisión (precision) y la recuperación (recall) en diferentes umbrales.

![](https://i.imgur.com/vjgCQq4.png)

### 〔Pruebas de reconocimiento〕
Vamos a probar como funciona nuestra IA.

1. Hacemos clic en *Quick test*.

![](https://i.imgur.com/MDa8rs6.png)

2. En nuestro motor de búsqueda favorito, buscamos imagenes de lo que queramos.

3. Tomé de ejemplo ésta. Podemos apreciar que no contiene **galaxias**, ni **planetas** y mucho menos **nebulosas**.

![](https://i.imgur.com/r9fQDmf.png)

4. Clic derecho sobre la imagen, y luego seleccionamos *Copiar dirección de imagen*.

![](https://i.imgur.com/0SkjVAw.png)

5. Pegamos el link de nuestra imagen donde corresponde y luego hacemos clic en la flecha azul.

![](https://i.imgur.com/pHJ7wPY.png)

6. La IA reconoce el link de la imagen y nos da los resultados que interpretó a partir de la imagen.

![](https://i.imgur.com/E7Z3JGF.png)

Podemos apreciar como efectivamente el Tag más predominante es el **negativo**, ya que, como mencioné antes, la imagen no posee galaxias, ni planetas, ni nebulosas, por ende, la IA interpretó que está viendo un valor neutro (o negativo).

![](https://i.imgur.com/RyGS0ys.png)

7. Hagamos otro intento, ahora busqué al **planeta** *55 Cancri e*.

8. Repetimos el proceso.

![](https://i.imgur.com/CQuSgt0.png)
![](https://i.imgur.com/Q3qMGXu.png)

Ahora nuestro resultado predominante fue **planeta**.

9. Aunque la IA **no siempre será perfecta**.

![](https://i.imgur.com/7iEtPeo.png)
![](https://i.imgur.com/SYYH4jo.png)

Lo detecto como un **planeta**. Aunque esto se debe más a que tampoco cuenta como una estrella, así que faltaría agregar los agujeros negros a los *tags negativos*

10. Y aquí un último ejemplo.

![](https://i.imgur.com/S5BUMYL.png)
![](https://i.imgur.com/ZtbTuAO.png)

Predominó el tag **Negativo** puesto que efectivamente son puras estrellas.