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

 - [Introducción a QnA Maker](#introducción-a-qna-maker)
    - [¿Cuándo usar QnA Maker?](#cuándo-usar-qna-maker)
    - [¿Qué es una base de conocimiento?](#qué-es-una-base-de-conocimiento)
    - [Creación de un bot de chat mediante programación](#creación-de-un-bot-de-chat-mediante-programación)
    - [Creación de bots de chat con poco código](#creación-de-bots-de-chat-con-poco-código)
    - [Respuestas de alta calidad con clasificación por capas](#respuestas-de-alta-calidad-con-clasificación-por-capas)
    - [Conversaciones multiturno](#conversaciones-multiturno)
    - [Ciclo de vida del desarrollo](#ciclo-de-vida-del-desarrollo)
- [Practica 16](#practica-16-creación-de-bot-de-preguntas-y-respuestas)
    - [Creación de "bases de conocimiento"](#creación-de-bases-de-conocimiento)
    - [Agregar preguntas y respuestas](#agregar-preguntas-y-respuestas)
    - [Creando el bot e implementando en Microsoft Teams](#creando-el-bot-e-implementando-en-microsoft-teams)
    - [Pruebas](#pruebas)

-------

# 【Introducción a QnA Maker】

![](https://www.outsystems.com/forge/DownloadResource.aspx?FileName=&ImageBinaryId=40153)

*QnA Maker* es un servicio de Procesamiento de lenguaje natural (NLP) basado en la nube que le permite crear una capa de conversación natural con los datos. Se utiliza para encontrar la respuesta más apropiada para una entrada de la knowledge base personalizada (KB) de información.

QnA Maker se usa normalmente para crear aplicaciones cliente de conversación, entre las que se incluyen aplicaciones de medios sociales, bots de chat y aplicaciones de escritorio habilitadas para voz.

QnA Maker no almacena datos de clientes. Todos los datos de clientes (respuestas de preguntas y registros de chat) se almacenan en la región en la que el cliente implementa las instancias de servicio dependientes. 

### 〔¿Cuándo usar QnA Maker?〕
- **Cuando tiene información estática**: use QnA Maker cuando tenga información estática en la base de conocimiento de las respuestas. Esta base de conocimiento está personalizada para sus necesidades, que ha creado con documentos como archivos PDF y direcciones URL.
- **Si desea proporcionar la misma respuesta a una solicitud, una pregunta o un comando**: cuando distintos usuarios envían la misma pregunta, se devuelve la misma respuesta.
- **Si desea filtrar la información estática en función de la metainformación**: agregue etiquetas de metadatos para proporcionar opciones de filtrado adicionales relacionadas con los usuarios de la aplicación cliente y la información. La información común de los metadatos incluye el tipo de contenido o formato de charla, y el propósito y la actualización del contenido.
- **Si desea administrar una conversación de bot que incluya información estática**: la base de conocimiento toma el texto o el comando de conversación de un usuario y lo responde. Si la respuesta forma parte de un flujo de conversación determinado previamente, representado en la base de conocimiento con contexto multiturno, el bot puede proporcionar fácilmente este flujo.

### 〔¿Qué es una base de conocimiento?〕
QnA Maker importa el contenido en una base de conocimiento de pares de preguntas y respuestas. En el proceso de importación se extrae información sobre la relación entre las partes del contenido estructurado y semiestructurado para insinuar relaciones entre los conjuntos de preguntas y respuestas. Puede editar estos pares de preguntas y respuestas o agregar otros nuevos.

El contenido del par de preguntas y respuestas incluye:

- Todas las formas alternativas de la pregunta
- Etiquetas de metadatos utilizadas para filtrar las opciones de respuesta durante la búsqueda
- Indicaciones de seguimiento para continuar con el perfeccionamiento de la búsqueda

![](https://docs.microsoft.com/es-es/azure/cognitive-services/qnamaker/media/qnamaker-overview-learnabout/example-question-and-answer-with-metadata.png)

Después de publicar la base de conocimiento, una aplicación cliente envía una pregunta de usuario al punto de conexión. El servicio de QnA Maker procesa la pregunta y responde con la mejor respuesta.

### 〔Creación de un bot de chat mediante programación〕
Una vez publicada una base de conocimiento de QnA Maker, una aplicación cliente envía una pregunta al punto de conexión de la base de conocimiento y recibe los resultados como una respuesta JSON. Una aplicación cliente común para QnA Maker es un bot de chat.

![](https://docs.microsoft.com/es-es/azure/cognitive-services/qnamaker/media/qnamaker-overview-learnabout/bot-chat-with-qnamaker.png)

| Paso  | Acción |
| ------------- | ------------- |
| 1 | La aplicación cliente envía la pregunta del usuario (texto en sus propias palabras) "Cómo actualizo mi base de conocimiento mediante programación?" al punto de conexión de knowledge base.  |
| 2 | QnA Maker usa la base de conocimiento entrenada para proporcionar la respuesta correcta y las solicitudes de seguimiento que se pueden usar para refinar la búsqueda de la mejor respuesta. QnA Maker devuelve una respuesta con formato JSON.  |
| 3 | La aplicación cliente usa la respuesta JSON para tomar decisiones acerca de cómo continuar con la conversación. Estas decisiones pueden incluir mostrar la respuesta principal y presentar más opciones para refinar la búsqueda de la mejor respuesta.  |

### 〔Creación de bots de chat con poco código〕
En el portal de QnA Maker se proporciona toda la experiencia de creación de la base de conocimiento. Puede importar documentos en su formulario actual a la base de conocimiento. Estos documentos (como las preguntas frecuentes, el manual del producto, la hoja de cálculo o la página web) se convierten en pares de preguntas y respuestas. En cada par se analizan los mensajes de seguimiento y cada par se conecta a otros pares. El formato de marcado final admite una presentación enriquecida que incluye imágenes y vínculos.

Una vez editada la base de conocimiento, publíquela en un bot de Azure Web App en funcionamiento sin escribir ningún código. Pruebe el bot en Azure Portal o descárguelo y continúe el desarrollo.

### 〔Respuestas de alta calidad con clasificación por capas〕
El sistema de QnA Maker es un enfoque de clasificación por capas. Los datos se almacenan en la búsqueda de Azure, que también actúa como la primera capa de clasificación. Los resultados principales de la búsqueda de Azure se pasan en el modelo de reclasificación NLP de QnA Maker para generar los resultados finales y la puntuación de confianza.

### 〔Conversaciones multiturno〕
QnA Maker proporciona solicitudes multiturno y aprendizaje activo para ayudarle a mejorar sus pares de preguntas y respuestas básicos.

Los mensajes multiturno le ofrecen la oportunidad de conectar pares de preguntas y respuestas. Esta conexión permite a la aplicación cliente proporcionar una respuesta superior y proporciona más preguntas para refinar la búsqueda de una respuesta final.

Una vez que la base de conocimiento recibe las preguntas de los usuarios en el punto de conexión publicado, QnA Maker aplica el aprendizaje activo a estas preguntas reales para sugerir cambios en la base de conocimiento y mejorar la calidad.

### 〔Ciclo de vida del desarrollo〕
QnA Maker permite la creación, el entrenamiento y la publicación, además de ofrecer permisos de colaboración para integrarse en el ciclo de vida de desarrollo completo.

![](https://docs.microsoft.com/es-es/azure/cognitive-services/qnamaker/media/qnamaker-overview-learnabout/development-cycle.png)

--------------

# 【Practica 16: Creación de bot de preguntas y respuestas〕
Muy similar a la práctica anterior, vamos a emplear una nueva herramienta para la actual práctica. Iremos a este **[enlace](https://www.qnamaker.ai/)**.

Veremos una página como esta. Se nos explicará brevemente la función de esta herramienta y sus ventajas.

![](https://i.imgur.com/Hb8Ea2k.png)

Hacemos clic en *Sign in* y nos logearemos con nuestra cuenta de Azure.

### 〔Creación de "bases de conocimiento"〕
Una *base de conocimiento* es el almacenamiento de todas las preguntas y respuestas que nosotros le agreguemos a nuestro bot para que sea capaz de aprenderlas y responder en consecuencia.

1. Vamos a hacer clic en *Create a knowledge base*.

![](https://i.imgur.com/bGK23ND.png)

2. Hacemos clic en *Create a QnA Service*.

![](https://i.imgur.com/iSW1gVw.png)

3. Esta opción nos redirigirá al portal de Azure, donde deberemos crear un recurso *QnA Maker*

![](https://i.imgur.com/XQ4rjGA.png)

4. Rellenamos los datos solicitados: *Suscripción*, *grupo de recursos*, *nombre* y *región*.

![](https://i.imgur.com/Ca5VWTm.png)

5. Después, debemos rellenar otros campos de un recurso que va en conjunto con el QnA. Dicho recurso se usa para indexar los datos que se vayan guardando del QnA. Y además de eso, se crea un App Service para alojar el servicio y se ejecuta por consulta del usuario.

![](https://i.imgur.com/NDkLcKs.png)

6. Dejamos lo demás por defecto y hacemos clic en *Revisar y crear*.

![](https://i.imgur.com/mfvZxmJ.png)

7. Y luego clic en *Crear*.

![](https://i.imgur.com/mQKbW1G.png)

8. Esperamos a que termine la implementación.

![](https://i.imgur.com/Bu53BSW.png)
![](https://i.imgur.com/RTskCuM.png)

9. De vuelta en la creación del Knowledge Base, vamos al paso 2. Tenemos un botón para refrescar los parámetros en caso de que no reconozca que hemos creado el QnA Service.

![](https://i.imgur.com/5AdJNtm.png)

10. Seleccionamos nuestros elementos en las casillas. Y elegimos el idioma el cual utilizaremos para el bot (en este caso, español).

![](https://i.imgur.com/QwpXdRb.png)

11. Le ponemos un *nombre*.

![](https://i.imgur.com/8uHowZn.png)

12. Esta parte es para ajustar el tipo de interacción que tendrá el bot. Para fines prácticos, utilizaremos "none" que será una interacción plana/neutra.

![](https://i.imgur.com/0vFm8xS.png)

13. Para finalizar, clic en *Create your KB*.

![](https://i.imgur.com/H3DqPu8.png)
![](https://i.imgur.com/68aK1Hq.png)

### 〔Agregar preguntas y respuestas〕
Una vez creada la base, debemos rellenarla con nuestro conjunto de preguntas y respuestas.

1. Damos clic en *Add QnA pair*.

![](https://i.imgur.com/0gKj2z8.png)

2. Empezamos a escribir nuestras preguntas (lado izquierdo) y nuestras respuestas (lado derecho).

![](https://i.imgur.com/gY8l1dI.png)

3. Pueden ser preguntas simples con solo texto, o podemos agregar imágenes, como podemos apreciar en la siguiente captura:

![](https://i.imgur.com/TN0S1CK.png)
![](https://i.imgur.com/3RpHunU.png)

> Cada vez que se haga esta pregunta, saldrá la imagen.

También podemos agregar hipervínculos a enlaces externos, por ejemplo, quiero que una respuesta tenga un hipervínculo a mi perfil de Linkedin.

4. Copiamos el link que queramos agregar.

![](https://i.imgur.com/9HgPhGx.png)

5. Seleccionamos la palabra que tendrá el hipervínculo, y pegamos el link respectivo.

![](https://i.imgur.com/4NhUTG2.png)
![](https://i.imgur.com/YNQIcHi.png)

6. También, podemos hacer más de una pregunta que tengan la misma respuesta. Por ejemplo, preguntamos por nuestros *pasatiempos* o por nuestros *hobbies* o "*a que nos dedicamos*", y todas deberian ser respondidas de la misma manera.

![](https://i.imgur.com/thJww2O.png)

7. Después, hacemos clic en *Save and train*. Tardará un rato, pero esperamos a que termine el proceso.

![](https://i.imgur.com/5QMxVkn.png)

8. Para probar el bot, damos clic en *Test*. Se nos desplegará un chat de prueba donde podemos escribir lo que queramos.

![](https://i.imgur.com/AEK7Q6u.png)

9. Aquí ocurre algo interesante, en mi pregunta yo respeté las acentos correspondientes a las palabras, pero en el chat los escribí sin dichos signos, y aún así fue reconocido por el bot, por ende, podemos decir que hay un margen de tolerancia en cuanto a la interpretación de las preguntas/palabras.

![](https://i.imgur.com/HwNQ11S.png)

10. Aquí lo escribí tal cual fue creada la pregunta, con su respectiva ortografía.

![](https://i.imgur.com/bkYmNpQ.png)

Para poder apreciar más este margen de tolerancia, volví a escribir otra pregunta dos veces de diferente forma.

11. Hacemos clic en la palabra *Inspect*, y se nos desplegará un menú con mucha información al respecto de la pregunta.

![](https://i.imgur.com/X4ExZNy.png)

12. Lo que nos interesa es donde dice *Confidence score*. En términos simples, es el puntaje de coincidencia que tiene la pregunta escrita, con las que hay en la base de conocimientos. Al ser comparadas, resulta en que tiene 100% de parecido.

![](https://i.imgur.com/yHNdh1F.png)

13. Por otro lado, la segunda vez que lo escribí de forma errónea, la reconoció, pero si vemos el *Confidence score*, tuvo una puntuación de 89.19%.

![](https://i.imgur.com/hSDcAqE.png)

Aquí tenemos dos ejemplo más.

![](https://i.imgur.com/C197Uho.png)
![](https://i.imgur.com/TgHrnpa.png)

14. Una vez comprobamos que el entrenamiento resultó de forma correcta y las respuestas del bot corresponden con lo que se pregunta, vamos a hacer clic en *Publish*.

15. Clic al botón *Publish*.

![](https://i.imgur.com/1qLkwRW.png)

16. Esperamos a que termine el proceso.

![](https://i.imgur.com/yTQPRus.png)

17. Una vez terminado, estaremos en una ventana como la siguiente, indicándonos que se publicó satisfactoriamente. Ahora podemos manipular el KB en donde queramos.

![](https://i.imgur.com/4HQYXfC.png)

> Podemos usar este código para implementar en HTML.

18. Ahora solo falta crear el bot. Hacemos clic en *Create bot*.

![](https://i.imgur.com/HTDcYNl.png)

### 〔Creando el bot e implementando en Microsoft Teams〕
Una vez presionado el botón, nos redirigirá a esta ventana del portal de Azure.

1. Rellenamos los parámetros que nos solicita, tales como *identificador* (lo más recomendable es no modificarlo), *suscripción*, *grupo de recursos*, *ubicación* y *plan de tarifa*.

![](https://i.imgur.com/iCsoarG.png)

2. Para el plan de tarifa, lo cambiaremos del *plan Standard* al *plan Free*.

![](https://i.imgur.com/N5LNVVK.png)

3. En *nombre* lo dejé por defecto, en *idioma del SDK* le puse *Node.js*. Todo lo demás por defecto.

![](https://i.imgur.com/XRxZ3WE.png)

4. Damos clic en *Crear*.

5. Esperamos a que se implemente.

![](https://i.imgur.com/OQTWSwG.png)

6. Vamos al recurso haciendo clic en *Ir al recurso*.

![](https://i.imgur.com/rZEuHvz.png)

7. Nos dirigimos al apartado *Configuración* y en *Canales*.

![](https://i.imgur.com/BXU4uZ2.png)

8. Bajamos el scroll hasta encontrar la plataforma donde queremos implementar el bot, en mi caso, usaré *Microsoft Teams*. Hacemos clic en él.

![](https://i.imgur.com/KmpNtib.png)

9. Aceptamos los términos del servicio. 

![](https://i.imgur.com/fHW6dJc.png)

10. Damos clic en *Aplicar*.

![](https://i.imgur.com/gyW9fR1.png)
![](https://i.imgur.com/UQB3aiI.png)

11. Regresamos al apartado *Canales* y podemos ver que ya está disponible el canal que creamos para el bot. Damos clic en *Open in Teams*.

![](https://i.imgur.com/9r92Asg.png)

12. Nos solicitará abrir la aplicación de Microsoft Teams (en dado caso de tenerla). Le damos clic al botón *Abrir Microsoft Teams*

![](https://i.imgur.com/LcomP9z.png)

### 〔Pruebas〕
Es momento de hacerle pruebas al bot una vez puesto en funcionamiento.

Pregunta: **¿Quién creó este bot?**

- Fue creado por Roberto Jimenez

![](https://i.imgur.com/Qea2MTf.png)

Pregunta: **¿Cuál es su perfil de Linkedin?**

- Puedes acceder a su perfil haciendo clic [aquí](https://www.linkedin.com/in/roberto-jimenez-garcia-b16199214/)

![](https://i.imgur.com/QmqST76.png)
![](https://i.imgur.com/J3VxAKk.png)
![](https://i.imgur.com/oNDzeCV.png)

> El hipervínculo funciona correctamente.

Pregunta: **¿A qué se dedica?/Pasatiempos**

- Estudiar, programar y jugar
[Foto de gatito]

![](https://i.imgur.com/7n1e6rf.png)

Pregunta: **¿Cuál es su fruta favorita?**

- Su fruta favorita es la sandía
[Foto de sandía]

![](https://i.imgur.com/BpUM9ZP.png)