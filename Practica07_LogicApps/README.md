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

 - [Introducción a Azure Logic Apps](#introducción-a-azure-logic-apps)
    - [Términos clave](#términos-clave)
        - [Aplicación lógica](#aplicación-lógica)
        - [Flujo de trabajo](#flujo-de-trabajo)
        - [Desencadenador](#desencadenador)
        - [Acción](#acción)
        - [Operaciones integradas](#operaciones-integradas)
        - [Conector administrado](#conector-administrado)
        - [Cuenta de integración](#cuenta-de-integración)
    - [Cómo funcionan las aplicaciones lógicas](#cómo-funcionan-las-aplicaciones-lógicas)
- [Practica 7](#practica-7-uso-de-azure-logic-apps-y-cognitive-services)
    - [Creación del recurso](#creación-del-recurso)
    - [Creación de la aplicación lógica](#creación-de-la-aplicación-lógica)
    - [Uso de Cognitive Services](#uso-de-cognitive-services)
    - [Creación de la aplicación lógica: continuación](#creación-de-la-aplicación-lógica-continuación)
    - [Conexión con Microsoft Teams](#conexión-con-microsoft-teams)
    - [Pruebas de ejecución](#pruebas-de-ejecución)
        - [Prueba 1](#prueba-1)
        - [Prueba 2](#prueba-2)
        - [Prueba 3](#prueba-3)

-------

# 【Introducción a Azure Logic Apps】

![](https://csharpcorner-mindcrackerinc.netdna-ssl.com/article/what-is-azure-logic-apps/Images/Azure%20Logic%20Apps.png)

*Azure Logic Apps* es una plataforma basada en la nube para crear y ejecutar *flujos de trabajo* automatizados que integren sus aplicaciones, datos, servicios y sistemas. Esta plataforma permite desarrollar rápidamente soluciones de integración altamente escalables para escenarios intraempresariales y de negocio a negocio (B2B). Azure Logic Apps forma parte de Azure Integration Services, por lo que simplifica la forma de conectar sistemas heredados, modernos y vanguardistas a través de entornos híbridos, locales y en la nube.

En la lista siguiente se describen solo algunas tareas, procesos empresariales y cargas de trabajo de ejemplo que puede automatizar con el servicio Azure Logic Apps:

- Programación y envío de notificaciones por correo electrónico mediante Office 365 cuando se produce un evento específico, por ejemplo, cuando se ha cargado un archivo nuevo.

- Procesamiento y enrutamiento de pedidos entre sistemas locales y servicios en la nube.

- Traslado de archivos cargados de un servidor SFTP o FTP a Azure Storage.

- Supervisión de tuits, análisis de opiniones y creación de alertas o tareas para los elementos que se deben revisar.

### 〔Términos clave〕
Los términos siguientes son conceptos importantes en el servicio Azure Logic Apps.

#### 〔Aplicación lógica〕
Una aplicación lógica es un recurso de Azure que se crea cuando se quiere desarrollar un flujo de trabajo. Hay varios tipos de recursos de aplicación lógica que se ejecutan en entornos diferentes.

#### 〔Flujo de trabajo〕
Un flujo de trabajo es una serie de pasos que definen una tarea o un proceso. Cada flujo de trabajo comienza con un único desencadenador, después del cual debe agregar una o varias acciones.

#### 〔Desencadenador〕
Un desencadenador es siempre el primer paso de cualquier flujo de trabajo y especifica la condición para ejecutar los demás pasos de ese flujo de trabajo. Por ejemplo, un evento de desencadenador podría recibir un correo electrónico en la bandeja de entrada o detectar un nuevo archivo en una cuenta de almacenamiento.

#### 〔Acción〕
Una acción es cada paso de un flujo de trabajo después del desencadenador. Cada acción ejecuta alguna operación en un flujo de trabajo.

#### 〔Operaciones integradas〕
Un desencadenador o una acción integrados son una operación que se ejecuta de forma nativa en Azure Logic Apps. Por ejemplo, las operaciones integradas proporcionan maneras de controlar la programación o estructura del flujo de trabajo, ejecutar su propio código, administrar y manipular datos, enviar o recibir solicitudes en un punto de conexión y llevar a cabo otras tareas del flujo de trabajo.

La mayoría de las operaciones integradas no están asociadas a ningún servicio o sistema, pero algunas operaciones integradas están disponibles para servicios específicos, como Azure Functions o Azure App Service. Muchas tampoco requieren que primero cree una conexión desde el flujo de trabajo y autentique su identidad. Para obtener más información y ejemplos, consulte Desencadenadores y acciones integrados para Logic Apps.

Por ejemplo, puede iniciar casi cualquier flujo de trabajo según una programación mediante el desencadenador Periodicidad. O bien, puede hacer que el flujo de trabajo espere hasta que se le llame mediante el desencadenador Solicitud.

#### 〔Conector administrado〕
Un conector administrado es un proxy o contenedor precompilado para una API REST que puede usar para acceder a una aplicación, datos, un servicio o un sistema específicos. Para poder crear la mayoría de los conectores administrados, primero debe crear una conexión desde el flujo de trabajo y autenticar su identidad. Microsoft se encarga de publicar, hospedar y administrar los conectores administrados. Para más información, consulte Conectores administrados para Logic Apps.

Por ejemplo, puede iniciar un flujo de trabajo con un desencadenador o ejecutar una acción que funcione con un servicio como Office 365, Salesforce o servidores de archivos.

#### 〔Cuenta de integración〕
Una cuenta de integración es un recurso de Azure que se crea cuando se desea definir y almacenar artefactos B2B para usarlos en flujos de trabajo. Después de crear y vincular una cuenta de integración con la aplicación lógica, los flujos de trabajo pueden usar estos artefactos B2B. Los flujos de trabajo también pueden intercambiar mensajes que sigan los estándares de intercambio electrónico de datos (EDI) e integración de aplicaciones empresariales (EAI).

Por ejemplo, puede definir socios comerciales, contratos, esquemas, mapas y otros artefactos B2B. Puede crear flujos de trabajo que usen estos artefactos e intercambiar mensajes a través de protocolos como AS2, EDIFACT, X12 y RosettaNet.


### 〔Cómo funcionan las aplicaciones lógicas〕

En una aplicación lógica, cada flujo de trabajo siempre se inicia con un único *desencadenador*. Un desencadenador se desencadena cuando se cumple una condición, por ejemplo, cuando se produce un evento específico o cuando los datos cumplen criterios específicos. Muchos desencadenadores incluyen funcionalidades de programación que controlan la frecuencia con la que se ejecuta el flujo de trabajo. Después del desencadenador, hay una o varias *acciones* que ejecutan operaciones que, por ejemplo, procesan, controlan o convierten datos que recorren el flujo de trabajo, o que avanzan el flujo de trabajo al paso siguiente.

En la siguiente captura de pantalla, se muestra parte de un flujo de trabajo empresarial de ejemplo. Este flujo de trabajo usa condiciones y modificadores para determinar la acción siguiente. Supongamos que tiene un sistema de pedidos y el flujo de trabajo procesa los pedidos entrantes. Quiere revisar manualmente los pedidos que estén por encima de un costo determinado. El flujo de trabajo ya tiene pasos anteriores que determinan cuánto cuesta un pedido entrante. Por tanto, crea una condición inicial basada en ese valor del costo. Por ejemplo:

- Si el pedido está por debajo de una cantidad determinada, la condición es false. En este caso, el flujo de trabajo procesa el pedido.

- Si la condición es true, el flujo de trabajo envía un correo electrónico para su revisión manual. Un modificador determina el paso siguiente.

    - Si el revisor lo aprueba, el flujo de trabajo continúa procesando el pedido.

    - Si el revisor remite el pedido a otra instancia, el flujo de trabajo envía un correo electrónico de remisión para obtener más información sobre el pedido.

        - Si se cumplen los requisitos de la remisión, la condición de respuesta es true. Por tanto, se procesa el pedido.

        - Si la condición de respuesta es false, se envía un correo electrónico sobre el problema.

![](https://docs.microsoft.com/es-es/azure/logic-apps/media/logic-apps-overview/example-enterprise-workflow.png#lightbox)

Puede crear visualmente flujos de trabajo mediante el diseñador de flujos de trabajo de Azure Logic Apps en Azure Portal, Visual Studio Code o Visual Studio. Cada flujo de trabajo también tiene una definición subyacente que se describe mediante notación de objetos JavaScript (JSON). Si lo prefiere, puede editar flujos de trabajo cambiando la definición de este JSON. Para algunas tareas de creación y administración, Azure Logic Apps proporciona compatibilidad con comandos de Azure PowerShell y la CLI de Azure. Para la implementación automatizada, Azure Logic Apps admite plantillas de Azure Resource Manager.

--------------

# 【Practica 7: Uso de Azure Logic Apps y Cognitive Services】
### 〔Creación del recurso〕
Primero que nada, empezaremos creador nuestra Aplicación Lógica, la cual se encargará de analizar Tweets publicados por los usuarios en relación a un Hashtag.
Dicha aplicación será capaz de capturar datos importantes, como *usuario*, *id*, *mensaje*, *fecha*, etc, y ajustarlos dentro de una tabla de excel (o sheets de google); además de ello, emplearemos google teams para enlazar las publicaciones de Twitter y republicarlas dentro de un grupo.

1. Empezamos buscando *Logic apps* en la barra de navegación.

![](https://i.imgur.com/hvwuZor.png)

2. Una vez en la pestaña de administración de Logic Apps, vamos a *Agregar*.

![](https://i.imgur.com/SXEMf7u.png)

3. Como cualquier recurso de Azure, se nos solicitará unos parametros necesarios para su funcionamiento. Elegimos la suscripción de nuestra preferencia. Creé un grupo de recursos para ésta práctica: **Practica7_Darki**. El nombre que le asigné es **LogicApp-P7**. Y en cuanto a región, seleccioné una región válida para nuestra suscripción, en este caso **Australia East**.

![](https://i.imgur.com/Kp3xnbP.png)

4. Configuramos el Plan. Aquí elegimos el tipo *Consumo*, esto hará que nuestra aplicación funcione y sea cobrada derivado del número de ejecuciones realizadas.

5. Lo demás lo dejamos por defecto. Damos al botón *Revisar y crear*.

![](https://i.imgur.com/xS10BmF.png)

6. Verificamos los parámetros y damos clic en *Crear*.

![](https://i.imgur.com/zjQqGEM.png)

7. Esperamos a que nuestro recurso esté implementado correctamente y damos a *Ir al recurso*.

![](https://i.imgur.com/oSP0roX.png)

![](https://i.imgur.com/RI3rHAo.png)
> Esta es la pestaña Diseñador de una aplicación lógica, más adelante trabajaremos con ella.

### 〔Creación de la aplicación lógica〕

Previamente, debemos crear una tabla de excel (en este caso, usé sheets y el archivo fue subido a Drive), con las siguientes columnas que vemos: *ID del Tweet*, *Twitteado por*, *Texto del Tweet*, *Localización*, *Sentimiento* y *Fecha*. Todos estos datos serán extraidos por nuestra Aplicación Lógica.

![](https://i.imgur.com/001196F.png)

Dentro del Diseñador, bajamos el scroll y veremos este apartado de *Plantillas*. Logic Apps ya viene con diseñor prefabricados de operaciones listas para usar dentro de Azure.
Nosotros omitiremos el usar alguna de esas plantillas y vamos a *crear aplicación lógica en blanco*.

1. Hacemos clic en *Aplicación lógica en blanco*. Y nos desplegará el apartado de creación de *pasos* de la Aplicación Lógica.

![](https://i.imgur.com/7JarBGh.png)

2. En la barra de busqueda de conectores y desencadenadores, buscamos *Twitter* (de donde sacaremos los Tweets evidentemente).

![](https://i.imgur.com/m3J3fpc.png)

3. Tenemos el *desencadenador* (Trigger) correspondiente: "Cuando se publica un tweet nuevo".

![](https://i.imgur.com/0aoOKwK.png)

4. Cuando seleccionemos el Trigger, nos pedirá unos parámetros. En primera el nombre de la conexión, seguido de una autentificación. (Nos pedirá logearnos con nuestra cuenta de Twitter y solicitará unos permisos los cuales autorizaremos)

![](https://i.imgur.com/2642PIX.png)
![](https://i.imgur.com/QaLUY1R.png)

5. Ahora, se nos pedirá ajustar el *paso* con algunos parámetros, por ejemplo, el texto que tomará como referencia para agarrar el tweet. Para este caso, usé el Hashtag **Stray** (es el nombre de un videojuego que está en tendencias actualmente a la fecha del 19 de julio del 2022). Después, se ajusta el comprobador en un timer de 5 segundos, esto quiere decir que cada 5 segundos hará un Check y Refresh de todos los cambios realizados en Twitter, siempre basandose en la *Palabra Clave*.

![](https://i.imgur.com/AMU0c8G.png)

6. Creamos un nuevo paso, ahora necesitaremos algo con lo que podamos analizar los tweets, y para ello usaremos un servicio de Azure, *Azure Cognitive Services para idioma*, que de igual forma, contiene sus propios Triggers y Acciones.

![](https://i.imgur.com/iC2aJmk.png)

7. Elegiremos la acción *Sentimiento V3.0*, recordemos que en nuestro Sheet hay una columna el cual se llenará con los datos de sentimientos que transmita el texto del usuario que lo publica.

![](https://i.imgur.com/6QrtE7x.png)

8. Aquí se nos solicitan otros parámetros extra, en este caso, *nombre de la conexión* y un tipo de conexión (usaremos Clave de API).

![](https://i.imgur.com/ohC6GIq.png)

9. Se nos solicita una Clave de cuenta y URL de Sitio. Estos datos los sacaremos en el siguiente tema.

### 〔Uso de Cognitive Services〕

Ahora, emplearemos un nuevo servicio de Azure. Cognitive Service sirve como servicios que usan Inteligencia Artificial para hacer cierto tipo de acciones, tales como analisis, traducción, reconocimiento, bots, etc.

1. Primero que nada, necesitamos algo que comprenda el lenguaje natural de un texto determinado. Creamos un Cognitive Service de tipo *Servicio de Lenguaje*.

![](https://i.imgur.com/AOLTgeo.png)

2. Aquí dejaremos por defecto y damos clic en *Continuar con la creación del recurso*.

![](https://i.imgur.com/lgdE73A.png)

3. Como siempre, *suscripción*, *grupo de recursos*, *región* y *nombre*, indispensables y necesarios para cualquier recurso de Azure. Y elegimos el plan de tarifa *Free F0*.

4. Clic en *Revisar y crear*.

![](https://i.imgur.com/LvjV9LK.png)

5. Después de la validación, clic en *Crear*.

![](https://i.imgur.com/rJyh09F.png)

6. Y esperamos a que se complete la implementación.

![](https://i.imgur.com/UPzDH8Q.png)

### 〔Creación de la aplicación lógica: continuación〕
Continuando con la creación del App Logic, del Cognitive Service creado, necesitamos extraer los siguientes datos: *Clave* y *Extremo*, que son los datos que nos solicitaba nuestra App para el *Azure Cognitive Service para idioma*.

![](https://i.imgur.com/uaKgpt5.png)

1. Rellenamos los campos con sus respectivos datos, y luego en *Crear*.

![](https://i.imgur.com/AgSojg3.png)

2. Después, nos pedirá agregar un identificador, para que cuando se cree una nueva Fila en nuestro Sheet, se cree con una clave ID para mayor control de cada una de ellas. (Elegimos el ID del Tweet)

![](https://i.imgur.com/q7LT6j1.png)
![](https://i.imgur.com/evxhSL3.png)

3. Lo mismo que el anterior, pero ahora solo será el contenido de dicho Tweet. (Elegimos el texto del Tweet)

![](https://i.imgur.com/Cl90mtr.png)

Ahora, dentro del mismo paso, crearemos un subpaso, el cual será una conexión con Google Sheets (esto nos permitirá manipular nuestra tabla de excel y su contenido, el cual fue subido a Google Drive).

4. Creamos un nuevo paso, y buscamos *Google Sheets*.

![](https://i.imgur.com/NN7R0yn.png)

5. Elegimos la acción *Insertar fila*.

![](https://i.imgur.com/xGXkRkX.png)

6. Y ahora nos pide logearnos con nuestra cuenta de Google Sheets. (Más bien, nuestra cuenta de Google Drive)

![](https://i.imgur.com/jGYNkia.png)

7. Ahora podemos localizar nuestro archivo. Al clickear en la carpeta azul de la derecha, se nos despliega un menú como el que se muestra en la imagen, y podemos ir navegando entre Google Sheets para buscar nuestro documento.

![](https://i.imgur.com/YKUtEyp.png)

8. Vemos que tenemos una carpeta llamada Google Drive, donde está almacenado nuestro archivo.

![](https://i.imgur.com/ktm7w5F.png)

9. Una vez que analice todas las carpetas y documentos, podemos ver que nuestro documento está localizado. Luego, le damos clic.

![](https://i.imgur.com/9elBX2C.png)

10. Seleccionamos la hoja de cálculo (dentro del documento) donde queremos trabajar.

![](https://i.imgur.com/vv4VNEL.png)

11. Seguido de ello, seleccionamos las columnas con las que vamos a trabajar. En este caso, usaremos todas, entonces las marcamos.

![](https://i.imgur.com/fKoY0Xd.png)

12. Ahora solo queda rellenar los espacios en blanco con parámetros que se usarán para rellenar las celdas correspondientes. (Como previamente ya hemos visto, seleccionamos por cada uno, su respectivo valor)

![](https://i.imgur.com/XKbr6Uh.png)
![](https://i.imgur.com/Auxka3W.png)

### 〔Conexión con Microsoft Teams〕
Ahora, realizaremos un nuevo paso, el cual nos permitirá republicar los tweets que se hacen en Twitter, pero ahora en un canal de Microsoft Teams.

1. Creamos el nuevo paso, y buscamos *Microsoft Teams*.

![](https://i.imgur.com/PKEm5O2.png)

2. Elegimos nuestra acción, en este caso *Publicar mensaje en un chat o canal*.

![](https://i.imgur.com/qLwY0bw.png)

3. Nos pedirá logearnos con Microsoft Teams.

![](https://i.imgur.com/jPy3dwX.png)

4. Ahora podemos especificar ciertas cosas, por ejemplo, como se publicará el mensaje, si será un *usuario* o un *bot*; a su vez, en donde será publicado *en un chat* o *en un canal*, especificaremos el *equipo* (grupo) donde se localiza nuestro canal, y posteriormente, selecionar el *canal* correspondiente.

![](https://i.imgur.com/xpYyzAC.png)

5. Podemos personalizar el mensaje que será publicado en el canal usando los datos de nuestro Sheet (se agregan como todos los demás elementos previamente vistos).

![](https://i.imgur.com/RLD6qBD.png)

### 〔Pruebas de ejecución〕
Una vez finalizado, procederemos a mostrar 3 ejecuciones de prueba y sus resultados encontrados.

Como especifiqué previamente, el **#Stray** está en tendencias a la fecha del 19 de julio del 2022, entonces habrá mucha gente publicando al respecto. La Logic App analizará los Tweets, filtrará cada uno y acomodará respecto a cada columna del Sheet.

#### 〔Prueba 1〕

1. Una vez guardada la aplicación, damos clic en *Ejecutar desencadenador* y en *Ejecutar*.

![](https://i.imgur.com/2Wufmxd.png)

2. Después de los 5 segundos que asignamos al principio, podemos empezar a ver resultados.

![](https://i.imgur.com/zQj5qxw.png)

3. Si miramos nuestra tabla de Tweets Obtenidos, vemos encontró 2 Tweets relacionados, y todos los datos fueron puestos en sus respectivas columnas. La palabra clave **#Stray** o **Stray** se encuentra presente en ambos resultados, inclusive el *Cognitive Service* reconoció el sentimiento de cada uno de ellos, aunque en este caso, los categorizó como **Neutrales**.

![](https://i.imgur.com/ZnrCZfG.png)

4. Yo creé un *Equipo* y un *Canal* específicos para esta prueba, y podemos observar que la aplicación usó mi cuenta de Teams para publicar los mensajes de los correspondientes Tweets.

![](https://i.imgur.com/chJw5xN.png)

#### 〔Prueba 2〕
Repetimos los mismos pasos de ejecución.

1. Clic en *Ejecutar desencadenador* y luego *Ejecutar*.

![](https://i.imgur.com/4XnWZ91.png)

2. Se agregaron nuevos Tweets a nuestra tabla.

![](https://i.imgur.com/PpKhJ19.png)

3. Y en Teams se publicaron una cantidad enorme de mensajes, esto es porque Microsoft Teams se actualiza más rápido que Google Sheets.

![](https://i.imgur.com/k8MKIrD.png)

#### 〔Prueba 3〕
Repetimos una última vez la ejecución de la aplicación.

![](https://i.imgur.com/WQ8EWBV.png)
![](https://i.imgur.com/IxFkZEa.png)
![](https://i.imgur.com/DRBSl42.png)