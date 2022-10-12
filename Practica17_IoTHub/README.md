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

 - [Introducción a Internet of Things](#introducción-a-internet-of-things)
    - [Dispositivos IoT](#dispositivos-iot)
    - [Autenticación e identidad de dispositivo](#autenticación-e-identidad-de-dispositivo)
    - [Comunicación de dispositivos](#comunicación-de-dispositivos)
    - [Telemetría de dispositivo](#telemetría-de-dispositivo)
    - [Propiedades de dispositivo](#propiedades-de-dispositivo)
    - [Comandos de dispositivo](#comandos-de-dispositivo)
    - [Un punto de conexión integrado recopila datos del dispositivo de manera predeterminada](#un-punto-de-conexión-integrado-recopila-datos-del-dispositivo-de-manera-predeterminada)
- [Practica 17](#practica-17-uso-de-iot-hub-y-simulación-de-dispositivo)
    - [Creando el IoT Hub](#creando-el-iot-hub)
    - [Añadiendo dispositivos](#añadiendo-dispositivos)
    - [Graficación de señal IoT](#graficación-de-señal-iot)
    - [Ejecutando el proyecto](#ejecutando-el-proyecto)
    - [Subiendo el proyecto a la nube](#subiendo-el-proyecto-a-la-nube)

-------

# 【Introducción a Internet of Things】

![](https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/06/azure-IoT.jpg)

Por lo general, *Internet de las cosas* (IoT) se define como una red de dispositivos físicos que se conectan a otros dispositivos y servicios a través de Internet u otra red e intercambian datos con ellos. Actualmente, hay más de diez mil millones de dispositivos conectados en el mundo y se agregan más cada año. Todo lo que se pueda insertar con los sensores y software necesarios se puede conectar a través de Internet.

Azure IoT Hub es un servicio administrado, hospedado en la nube, que actúa como centro de mensajes para la comunicación entre una aplicación de IoT y los dispositivos conectados. Puede conectar millones de dispositivos y sus soluciones de back-end con confianza y de forma segura. La mayoría de los dispositivos se pueden conectar a un centro de IoT.

Se admiten varios patrones de mensajería, como telemetría del dispositivo a la nube, carga de archivos desde dispositivos y métodos de solicitud-respuesta para controlar los dispositivos desde la nube. IoT Hub también admite la supervisión para ayudarlo a realizar un seguimiento de la creación de dispositivos, la conexión de dispositivos y los errores de los dispositivos.

IoT Hub escala a millones de dispositivos conectados de manera simultánea y a millones de eventos por segundo para admitir las cargas de trabajo de IoT. 

Puede integrar IoT Hub con otros servicios de Azure para compilar soluciones completas de un extremo a otro. Por ejemplo, use:

- *Azure Event Grid* para permitir que la empresa responda rápidamente a eventos críticos de forma confiable, escalable y segura.

- *Azure Logic Apps* para automatizar procesos de negocio.

- *Azure Machine Learning* para agregar aprendizaje automático y modelos de AI a la solución.

- *Azure Stream Analytics* para ejecutar cálculos de análisis en tiempo real en los flujos de datos de los dispositivos.

Las aplicaciones de IoT Central usan varios centros de IoT como parte de su infraestructura escalable y resistente.

Las suscripciones de Azure disponen de límites de cuota predeterminados para evitar el uso abusivo del servicio. Estos límites podrían afectar el ámbito de su solución IoT. El límite actual es de 50 de centros de IoT Hub por suscripción. Puede solicitar un aumento de la cuota si se pone en contacto con el soporte técnico.

- Límites de servicio de suscripción de Azure

- IoT Hub throttling and you (Limitación de IoT Hub)

### 〔Dispositivos IoT〕
Los dispositivos IoT son distintos de otros clientes como exploradores y aplicaciones móviles. En concreto, los dispositivos de IoT:

- A menudo son sistemas insertados sin operador humano.
- Se pueden implementar en ubicaciones remotas, donde el acceso físico resulta costoso.
- Es posible que solo sean accesibles a través del back-end de soluciones.
- Es posible que tengan limitaciones de recursos de procesamiento y alimentación.
- Es posible que tengan conectividad de red intermitente, lenta o costosa.
- Es posible que necesiten usar protocolos de aplicación propios, personalizados o específicos de determinados sectores.

### 〔Autenticación e identidad de dispositivo〕
Cada centro de IoT tiene un registro de identidades que almacena información acerca de los dispositivos y módulos que pueden conectarse a él. Para que un dispositivo o un módulo se pueda conectar, debe haber una entrada para ese dispositivo o módulo en el registro de identidades del centro de IoT. Un dispositivo o un módulo se puede autenticar en el centro de IoT en función de las credenciales almacenadas en el registro de identidades.

Se admiten dos métodos de autenticación entre el dispositivo e IoT Hub. Puede usar una autenticación basada en tokens de SAS o una autenticación de certificado X.509.

El método de token de SAS proporciona la opción de autenticación para cada llamada que realice el dispositivo a IoT Hub mediante la asociación de la clave simétrica a cada llamada. La autenticación de X.509 permite la autenticación de un dispositivo IoT en la capa física como parte del establecimiento de la conexión estándar mediante Seguridad de la capa de transporte (TLS). La elección de un método u otro viene determinada principalmente por lo segura que deba ser la autenticación del dispositivo y la disponibilidad de almacenamiento seguro en este (para almacenar la clave privada de forma segura).

Puede configurar y aprovisionar muchos dispositivos a la vez mediante el servicio IoT Hub Device Provisioning.

### 〔Comunicación de dispositivos〕
Después de seleccionar el método de autenticación, la conexión a Internet entre el dispositivo IoT e IoT Hub se protege con el estándar de Seguridad de la capa de transporte (TLS). Azure IoT admite TLS 1.2, TLS 1.1 y TLS 1.0, en este orden. La compatibilidad con TLS 1.0 solo se proporciona para permitir versiones anteriores. Compruebe la compatibilidad con TLS en IoT Hub para ver cómo configurar el centro a fin de usar TLS 1.2, ya que proporciona la máxima seguridad.

Habitualmente, los dispositivos IoT envían datos de telemetría desde sus sensores a los servicios back-end en la nube. Pero hay otros tipos de comunicación posibles, como un servicio de back-end que envía comandos a los dispositivos. Algunos ejemplos de otros tipos de comunicación son los siguientes:

- Un camión refrigerado que envía datos de temperatura cada 5 minutos a un centro de IoT.
- Un servicio de back-end que envía un comando a un dispositivo para cambiar la frecuencia con la que envía los datos de telemetría que ayudan a diagnosticar un problema.
- Un dispositivo que supervisa un reactor por lotes en una planta química y envía una alerta cuando la temperatura supera un valor determinado.

### 〔Telemetría de dispositivo〕
Entre los ejemplos de telemetría recibidos de un dispositivo se incluyen datos de sensor como los de velocidad o temperatura, un mensaje de error como un evento perdido o un mensaje de información para indicar que el dispositivo está en buen estado. Los dispositivos IoT envían eventos a una aplicación a fin de obtener información. Las aplicaciones pueden necesitar subconjuntos específicos de eventos para el procesamiento o el almacenamiento en distintos puntos de conexión.

### 〔Propiedades de dispositivo〕
Las propiedades se pueden leer o establecer desde la instancia de IoT Hub y se pueden usar para enviar notificaciones cuando se ha completado una acción. Un ejemplo de una propiedad específica en un dispositivo es la temperatura. La temperatura puede ser una propiedad grabable que se puede actualizar en el dispositivo o leer desde un sensor de temperatura conectado al dispositivo.

En IoT Hub puede habilitar propiedades mediante dispositivos gemelos o Plug and Play.

### 〔Comandos de dispositivo〕
Un ejemplo de un comando es el reinicio de un dispositivo. Para implementar comandos, IoT Hub le permite invocar métodos directos en los dispositivos. Los métodos directos representan una interacción entre solicitudes y respuestas con un dispositivo similar a una llamada HTTP en la que se completan correctamente o generan un error de inmediato (tras un tiempo de espera especificado por el usuario). Este enfoque es útil en escenarios donde el curso de una acción inmediata es distinto en función de si el dispositivo pudo responder.

### 〔Un punto de conexión integrado recopila datos del dispositivo de manera predeterminada〕
Un punto de conexión integrado recopila datos del dispositivo de forma predeterminada. Los datos se recopilan mediante un patrón de solicitud-respuesta por medio de puntos de conexión de dispositivo IoT dedicados, están disponibles por una duración máxima de siete días y se pueden usar para realizar acciones en un dispositivo. Estos son los datos aceptados por el punto de conexión del dispositivo:

- Envío de mensajes de dispositivo a nube
- Recepción de mensajes de nube a dispositivo
- Iniciar cargas de archivos
- Recuperación y actualización de las propiedades del dispositivo gemelo
- Recepción de solicitudes de métodos directos

--------------

# 【Practica 17: Uso de IoT Hub y simulación de dispositivo〕
Para esta práctica, crearemos un recurso IoT Hub, simularemos un dispositivo inteligente que reciba señales de un sensor, lo conectaremos y haremos pruebas para ver como se ve la información que recibe el Hub desde dicho dispositivo.

### 〔Creando el IoT Hub〕
Trabajaremos creando el IoT Hub, o "Centro de IoT", el cual se usará para conectar los dispositivos inteligentes que tengamos a nuestra disposición para posteriormente manipularlos.

1. En la barra de búsqueda, escribimos *IoT Hub*, y seleccionamos la primera opción.

![](https://i.imgur.com/uaruIVK.png)

2. Damos clic en *Crear*.

![](https://i.imgur.com/uLbJQRJ.png)

3. Se nos solicitará llenar unos campos necesarios, como *suscripción*, *grupo de recursos*, *nombre* y región*. 

![](https://i.imgur.com/rjiCORJ.png)

4. Nos vamos al apartado de *redes*, y seleccionamos *Acceso público*.

![](https://i.imgur.com/YBbDBkT.png)

5. Aquí en *Administración* podemos ver un poco más de información acerca del plan que se usará en el Hub y los precios.

![](https://i.imgur.com/JfmAZXT.png)
![](https://i.imgur.com/6jmISaJ.png)

6. Clic en *Revisar y crear*.

![](https://i.imgur.com/tl8c9Zm.png)

7. Después en *Crear*.

![](https://i.imgur.com/bHTET24.png)

8. Una vez terminada la implementación, vamos al recurso.

![](https://i.imgur.com/Qmfas43.png)

### 〔Añadiendo dispositivos〕
Ahora, añadiremos a nuestro Hub un dispositivo. Hay que dejar en claro que esto no funciona como un dispositivo que se conecta a internet/wifi, aquí funciona al revés, nosotros debemos conectar el Hub al dispositivo. Esto se hace, creando los puntos de conexión y asignandoselo al dispositivo en cuestión.

1. Una vez dentro de la interfaz del recurso, vamos a ir en el apartado *Administración* y luego en *Dispositivos*.

![](https://i.imgur.com/wa4Zt4F.png)

2. Después, hacemos clic en *Agregar dispositivo*.

![](https://i.imgur.com/jGDZgKT.png)

3. Para fines prácticos, solo asignaremos el *nombre* que queramos. Y clic en *Guardar*.

![](https://i.imgur.com/1VDMCVS.png)

4. De vuelta aquí, vamos a darle clic al *nombre del dispositivo*.

![](https://i.imgur.com/1R0KuFN.png)

5. Aquí tendremos las *claves* y *enlaces de conexión* para el dispositivo IoT que vayamos a estar manipulando.

![](https://i.imgur.com/QNMwl4c.png)

6. Copiamos la *cadena de conexión principal*.

Ahora, tendremos que usar un dispositivo al cual programaremos la conexión. Como en mi caso, no poseo nada similar, usaremos un simulador Raspberry Pi que cumpla exactamente los mismos requisitos para la práctica.

Para ello, vamos al siguiente **[enlace](https://azure-samples.github.io/raspberry-pi-web-simulator/#getstarted)**. Este simulador funciona de la siguiente manera, tendremos un *sensor* de temperatura y humedad, conectado por medio de una protoboard a un Raspberry Pi. El sensor mandará sus correspondientes datos al raspberry, y éste los mandará a nuestro IoT Hub.

7. Lo que debemos hacer ahora, es pegar la cadena que copiamos antes, en la linea donde dice: "**Your IoT Hub device connection string**"

![](https://i.imgur.com/xZLBGxL.png)

8. Después, damos clic en *Run*.

![](https://i.imgur.com/PralP2u.png)

Si todo salió bien, en la consola debemos empezar a recibir información de que los mensajes han sido enviados a Azure IoT Hub. (Desde este punto, toda la información "simulada" que nuestro sensor está recibiendo, será mandado a Azure)

### 〔Graficación de señal IoT〕
Pero, ¿cómo veremos que datos está recibiendo nuestro IoT Hub?

Podemos apreciar que el simulador está mandando información, pero esa información nosotros no la estamos viendo, no sabemos que valores son y tampoco si está variando con el tiempo. Tampoco es posible verlo dentro del IoT Hub en si, porque IoT Hub solo se encarga de recibir y generar peticiones en base a lo que recibe.

Para que podamos observar visualmente que está sucediendo, tendremos que hacer un paso extra. Entonces, nos dirigimos a este **[repositorio](https://github.com/azure-samples/web-apps-node-iot-hub-data-visualization)**.

Este proyecto fue realizado para que nosotros podamos conectar nuestro IoT Hub y que transmita esas señales recibidas del dispositivo, en un proyecto de graficación con sus respectivos valores y resultados.

![](https://i.imgur.com/2MJK9hZ.png)

1. Primero que nada, vamos a clonar este repositorio en nuestro entorno local. En la ubicación que queramos, usaremos Git Bash para hacer un `git clone` y la `url` que nos proporciona GitHub.

![](https://i.imgur.com/wOr2KLT.png)

2. Regresamos a Azure, y abrimos el *Cloud Shell*. Creamos una *cuenta de almacenamiento*.

![](https://i.imgur.com/yquVkG2.png)

3. Escrbimios el siguiente comando, que en términos simples, sirve para extraer una clave de conexión (diferente a las anteriores), la cual nos servirá para hacer la conexión con el proyecto que usaremos para graficar.

![](https://i.imgur.com/dIoZ4t5.png)

4. Nos pedirá instalar una extensión, solo escribimos `Y`, y pulsamos `Enter`.

![](https://i.imgur.com/idId3pU.png)

5. Copiamos la información que aparece en la imagen.

![](https://i.imgur.com/rugPR7m.png)

Lo siguiente se podría haber hecho en Cloud Shell, pero solo por probar decidí hacerlo en Git Bash (con el CLI ya instalado).

6. Escribimos toda la siguiente linea de comando. El *ConsumerGroup* es algo necesario que nos solicita la conexión, y solo nos quedaremos con el nombre que le hayamos puesto. Pulsamos `Enter`.

![](https://i.imgur.com/ynr4YMG.png)

7. Copiamos la información seleccionada en la imagen.

![](https://i.imgur.com/dGpf4hO.png)

Mantenemos los datos guardados en algún lugar, los usaremos pronto.

8. Con la carpeta del proyecto abierta (en mi caso, usando Visual Studio Code), vamos a escribir en una terminal lo siguiente: `npm install`

![](https://i.imgur.com/nPIERzx.png)

9. Esperamos a que termine el proceso de instalación.

![](https://i.imgur.com/9JpcZXS.png)

Ahora, a los datos que teníamos guardados, vamos a agregarles lo siguiente:

- **set IotHubConnectionString=** 
(seguido de todo el código previamente copiado)

- **set EventHubConsumerGroup=** 
(de igual forma, con el código copiado anteriormente)

![](https://i.imgur.com/jcQWsBN.png)
![](https://i.imgur.com/tLHL3hc.png)

Ambos los copiamos y vamos a *Git Bash*. Pegamos el primero y luego presionamos `Enter`. Lo mismo para el segundo.

![](https://i.imgur.com/TaAZMo9.png)


### 〔Ejecutando el proyecto〕
Volvemos al Visual Studio Code, y vamos a echar a andar el proyecto.

1. Hacemos clic en *Ejecutar*, y en *Iniciar depuración*.

![](https://i.imgur.com/2d3XRXT.png)

2. El proyecto habrá identificado los valores de *Connection String* y *ConsumerGroup*. Y ahora la gráfica está escuchando en el puerto 3000.

![](https://i.imgur.com/aEB4EsM.png)

3. Ahora podemos ver que la terminal ya empieza a mostrar valores recibidos, y dichos valores corresponden a nuestro sensor que aún sigue estando activo desde el momento que le dimos a *Run*.

![](https://i.imgur.com/pjnOxya.png)
![](https://i.imgur.com/VabCtE2.png)

Ahora, abrimos nuestro navegador de preferencia, y escribimos lo siguiente: `http://localhost:3000`

![Mi video1 00_00_00-00_00_30](https://user-images.githubusercontent.com/105999936/184457982-16b4f082-7a83-4dcc-a387-241cc381fb8c.gif)

Lo que podemos apreciar aquí, son aquellos valores que está mandando nuestro *sensor* a *IoT Hub*, y éste a su vez lo está mandando al *graficador* para que sean interpretados y graficados apropiadamente en tiempo real.

### 〔Subiendo el proyecto a la nube〕
Como hemos visto, gracias al repositorio hemos sido capaces de graficar los datos de forma local, pero éste mismo proyecto podemos mandarlo a la nube para que funcione como una aplicación web.

1. Para ello, vamos a crear un App Service donde alojaremos nuestra aplicación. En esta ocasión lo haremos con *Cloud Shell*. Escribimos la siguiente linea de código que vemos en la imagen y pulsamos `Enter`

![](https://i.imgur.com/lyrbR80.png)

Las características que asignamos son:

- Nombre: **AppServiceIoT**
- Grupo de recursos: **Practica17_Darki**
- Plan/SKU: **Free**

2. Cuando aparezca `ProvisioningState: Succeeded`, sabremos que se implementó correctamente.

![](https://i.imgur.com/u7uO0tM.png)

3. Ahora, crearemos una WebApp con la linea de código siguiente, y pulsamos `Enter`.

- Nombre: **paginaIoT2606**
- Grupo de recursos: **Practica17_Darki**
- App Service: **AppServiceIoT**
- Runtime: **Node|14LTS**
- Implementación: **Local Git**

![](https://i.imgur.com/O0DdwMm.png)

4. Habilitamos el protocolo `HTTPS` de la siguiente forma:

![](https://i.imgur.com/SmEMeh2.png)

5. Pulsamos `Enter`.

![](https://i.imgur.com/k6dAFxb.png)

6. Por último, habilitamos los *Sockets Web* así:

![](https://i.imgur.com/FfGiBka.png)

7. Pulsamos `Enter`.

![](https://i.imgur.com/7hPEw89.png)

8. AHora vamos al apartado *Centro de implementación*. Y hacemos clic en *Credenciales FTPS*.

![](https://i.imgur.com/7F2IEvp.png)

9. Bajamos el scroll, y llenamos los siguientes parámetros: *Usuario* y *contraseña*.

![](https://i.imgur.com/DbwKQt0.png)

10. Clic en *Guardar*.

![](https://i.imgur.com/TIiaJ2w.png)

11. Volvemos a *Configuración*, y en donde dice *URI de Git Clone*, pulsamos el botón de *copiar en portapapeles*

![](https://i.imgur.com/JJnZPCb.png)

12. Regresamos a Visual Studio Code, y abrimos una terminal. Hacemos la conexión remota con `git remote add webapp [URI]`. Pulsamos `Enter`

![](https://i.imgur.com/fXzwogA.png)

13. Una vez hecha la conexión, hacemos un push para enviar el proyecto a la nube con `git push webapp master`.

14. Después de presionar `Enter`, nos aparecerá esta ventana emergente donde nos solicitará nuestras credenciales (usuario y contraseña). Las ingresamos y presionamos `Enter`.

![](https://i.imgur.com/xyg2mbV.png)

15. Empezará a subirse nuestro proyecto.

![](https://i.imgur.com/JqfvWF9.png)
![](https://i.imgur.com/HuLDju6.png)

16. El resultado deberá verse así, representando que se subió exitosamente a Azure.

17. Volviendo al App Service, vamos a *Configuración* y hacemos clic en *Nueva configuración de la aplicación*. (En este apartado, será como lo que vimos de hacer **Set** a los valores de Connection String y ConsumerGroup)

![](https://i.imgur.com/mW5gsar.png)

18. Agregamos el "nombre" de `IoTHubConnectionString`, y se le asignará para su valor nuestra *ConnectionString*.

![](https://i.imgur.com/NepKYCG.png)

19. El mismo procedimiento, pero para el `EventHubConsumerGroup`.

![](https://i.imgur.com/KJFeGx7.png)

20. Guardamos los cambios.

![](https://i.imgur.com/e3dxBlG.png)
![](https://i.imgur.com/zN1fGXn.png)
![](https://i.imgur.com/sIBrIJ5.png)

21. Y todo está listo. Volvemos a *Introducción* y podemos acceder a nuestra aplicación web desde *URL*.

![](https://i.imgur.com/34zIFkY.png)

Podemos apreciar que conseguimos el mismo resultado que en la versión local, pero ahora no necesitamos el `localhost:3000`, sino que ahora está alojado en una página web de Azure.

![Mi video 2 00_00_00-00_00_30](https://user-images.githubusercontent.com/105999936/184457648-507bcb8f-adb8-4425-a888-90293a6f35f5.gif)
