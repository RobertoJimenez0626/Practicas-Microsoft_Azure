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

# 【Azure】

![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Microsoft_Azure.svg/150px-Microsoft_Azure.svg.png)

**Tabla de Contenidos**

 - [Introducción a Azure](#introducción-a-azure)
    - [Categorías y servicios de Azure](#categorías-y-servicios-de-azure)
        - [Compute](#compute)
        - [Network](#network)
        - [Storage](#storage)
        - [Database (DB)](#database-db)
        - [Web](#web)
        - [Internet of Things (IoT)](#internet-of-things-iot)
        - [Big Data](#big-data)
        - [Inteligencia Artificial (IA)](#inteligencia-artificial-ia)
        - [DevOps](#devops)
- [Practica 1](#practica-1---página-wordpress-con-azure-app-service)
    - [Creación de la página WordPress](#creación-de-la-página-wordpress)
    - [Configuración y vista predeterminada de WordPress](#configuración-y-vista-predeterminada-de-wordpress)
    - [Explicación de componentes del grupo de recursos](#explicación-de-componentes-del-grupo-de-recursos)
    - [Rediseño y acabados finales de la página WordPress](#rediseño-y-acabados-finales-de-la-página-wordpress)
- [Resultado final](#resultado-final)

-------

# 【Introducción a Azure】
Azure es un conjunto de servicios en la nube en expansión constante que ayudan a las organizaciones a cumplir los desafíos empresariales actuales y futuros. Azure le ofrece la libertad de compilar, administrar e implementar aplicaciones en una red global masiva mediante sus herramientas y plataformas favoritas.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Microsoft_Azure_Logo.svg/640px-Microsoft_Azure_Logo.svg.png)

Azure proporciona más de cien servicios que permiten hacer todo tipo de cosas: desde ejecutar las aplicaciones existentes en máquinas virtuales hasta explorar nuevos paradigmas de software, como bots inteligentes y realidad mixta.

Muchos equipos comienzan a explorar la nube mediante la migración de sus aplicaciones existentes a máquinas virtuales que se ejecutan en Azure. Si bien este es un buen comienzo, la nube es mucho más que "un lugar diferente donde ejecutar las máquinas virtuales".

Por ejemplo, Azure proporciona servicios de inteligencia artificial y aprendizaje automático que pueden comunicarse naturalmente con los usuarios mediante la vista, el oído y la voz. También facilita soluciones de almacenamiento que crecen dinámicamente para dar cabida a grandes cantidades de datos. Los servicios de Azure permiten soluciones que no son factibles sin la potencia de la nube.

## 〔Categorías y servicios de Azure〕
### 〔Compute〕
Proporciona servicios de cómputo o procesamiento bajo demanda. Por ejemplo:
- Maquinas virtuales (VM).
- Kubernetes.
- Azure Virtual Machine Scale Sets.
- Azure Functions.
- Azure Container Instances.

![](https://connectoricons-prod.azureedge.net/releases/v1.0.1555/1.0.1555.2715/azurevm/icon.png)
> Azure Virtual Machine.

### 〔Network〕
Proporciona servicios de red que permiten conectar los recursos con el mundo exterior. Por ejemplo:
- Azure Virtual Network.
- Azure Traffic Manager.
- Azure DDoS Protection.
- Balanceadores de carga (Load Balancer).

![](https://symbols.getvecta.com/stencil_27/99_virtual-network.e43fa52244.png)
> Azure Virtual Network.

### 〔Storage〕
Proporciona servicios de almacenamiento de archivos y objetos. Por ejemplo:
- Azure Blob Storage.
- Azure File Storage.
- Azure Queue Storage.
- Azure Table Storage.

![](https://symbols.getvecta.com/stencil_27/89_storage-table.5f25f9c0b3.png)
> Azure File Storage.

### 〔Database (DB)〕
Proporciona servicios de bases de datos para una amplia variedad de tipos y volumenes de datos. Por ejemplo:
- Cosmos DB.
- Azure SQL Database.
- Azure Database Migration Service.

![](https://www.pinclipart.com/picdir/big/125-1259340_how-to-easily-start-using-cosmosdb-in-your.png)
> Azure Cosmos DB.

### 〔Web〕
Proporciona servicios para compilar y hospedar aplicaciones y servicios web basados en HTTP. Por ejemplo:
- Azure App Service.
- Azure Notification Hubs.
- Azure API Management.
- Azure Cognitive Search.
- Característica Web Apps de Azure App Service.
- Servicio Azure SignalR.

![](https://stefanos.cloud/wp-content/uploads/2021/09/Azure-App-Service-Redundancy-e1631817455805.png)
> Azure App Service.

### 〔Internet of Things (IoT)〕
Proporciona servicios de IoT para conectar y recibir información de sensores, relojes inteligentes, maquinaria, etc. Por ejemplo:
- IoT Central.
- Azure IoT hub.
- IoT Edge.

![](https://2yqpsp4hm422vu40d2itdbu1-wpengine.netdna-ssl.com/wp-content/uploads/2020/02/azure-iot.png)
> Azure IoT hub.

### 〔Big Data〕
Porporciona servicios para el procesamiento y análisis de grandes cantidades de registros. Por ejemplo:
- Azure Synapse Analytics.
- Azure Databricks.
- Azure HDInsight.

![](https://symbols.getvecta.com/stencil_27/51_hdinsight.c90b5f74e0.png)
> Azure HDInsight.

### 〔Inteligencia Artificial (IA)〕
Proporciona servicios de aprendizaje automático (prefabricados o no). Por ejemplo:
- Azure Machine Learning Service.
- Azure Machine Learning Studio.
- Azure Cognitive Services.

![](https://miro.medium.com/max/382/1*xr5cOLRaJZuqSeaWoKHsnA.png)
> Azure Cognitive Services.

### 〔DevOps〕
Ayuda a los equipos de desarrollo de software a automatizar y hacer eficientes sus procesos. Por ejemplo:
- Azure DevOps.
- Azure DevTest Labs.

![](https://cdn.iconscout.com/icon/free/png-256/azure-devops-3628645-3029870.png)
> Azure DevOps.

--------------

# 【Practica 1 - Página Wordpress con Azure App Service】
### 〔Creación de la página Wordpress〕
1. Entramos al siguiente enlace: https://portal.azure.com/
![Portal de Azure](https://i.imgur.com/tS5Ky0l.png)
> Página Portal de Microsoft Azure.

2. Empezamos buscando en la barra de busquedas "**Marketplace**". Podemos definir Marketplace como un conexión entre los Usuarios y los Partners de Microsoft, los cuales son proveedores de software independientes y nuevas empresas que ofrecen sus soluciones y servicios, optimizados para ser utilizados en Azure.
![](https://i.imgur.com/2jYMqh5.png)

3. Aquí podemos navegar entre los distintos complementos y software que se nos brinda de parte de Microsoft u otros proveedores, los cuales están listos para usarse a nuestro gusto.
![](https://i.imgur.com/JRfnKtL.png)
> Interfaz de busqueda de Marketplace.

4. **Nota:** Existe la posibilidad de conseguir software de terceros de empresas "competencia" de Microsoft, como se muestran en las imagenes:
![](https://i.imgur.com/GARmRlu.png)
![](https://i.imgur.com/8fktJ2t.png)

5. En el buscador de Marketplace, escribimos: **WordPress**.
6. Seleccionamos el primero:
![](https://i.imgur.com/WUjPBHT.png)

7. Seguidamente elegimos el plan "WordPress" y luego en **Crear**.
![](https://i.imgur.com/0Lfc2iL.png)
> Al momento de finalizar las configuraciones, nos creará varios recursos de Azure. Estos mismos serán explicados posteriormente en esta misma práctica.

8. Ahora entramos en la pantalla de configuraciones del recurso "**WordPress**" empleando "**App Service**" (Recurso **encargado** de todo lo relacionado a **Web**)
![](https://i.imgur.com/P9yb82Q.png)

9. **MUY IMPORTANTE**: Lo minimo que todo recurso de Azure **necesita** para ser creado son 4 cosas fundamentales: **Suscripción**, **Grupo de recursos**, **Región** y **Nombre del recurso**

10. Suscripción: En este caso, solo contamos con la suscripción de tipo **Estudiante**, y es la que seleccionamos.
![](https://i.imgur.com/Cgh7uOU.png)

11. Grupo de recursos: Si no hemos tocado nada por el momento, nos encontraremos sin ningún grupo de recursos; por ende, debemos crear uno. Podemos ver los grupos de recursos como "carpetas" de nuestros recursos. En mi caso, yo le puse **Practica1_Darki** (Darki es mi sobrenombre)
![](https://i.imgur.com/uf2uLx9.png)
> De este modo iré nombrando tanto mis grupos de recursos como mis demás elementos que ocupe en todas mis prácticas para mejor organización.

12. Región: Aquí elegimos en que región de Azure estará localizado nuestro recurso. En este caso elegí **Australia East** (y esto es debido a que nuestra suscripción no cuenta con toda la cobertura de regiones que ofrece Azure, impidiendonos configurar ciertos parametros de nuestros recursos; esto quiere decir: Australia tiene bastante facilidad para operar de esta forma siendo estudiantes)
![](https://i.imgur.com/gZdYd7J.png)

13. Nombre del recurso: Y por ultimo, asignamos el nombre que llevará nuestro recurso y con el cual se le identificará. En mi caso usé: **PagWordpress-P1**
![](https://i.imgur.com/en9kG7I.png)
> Algo a tener en cuenta es que el Sistema Operativo con el cual se trabajará dependerá del gusto del usuario, en mi caso yo elegí Windows, pero pude haber elegido Linux sin problema.

14. Ahora, pasamos a un apartado **NO OBLIGATORIO**, pero **SI IMPORTANTE**, las **Etiquetas**. Estas cumplen 3 funciones: 1) Sacar reportes de costos, 2) Cumplir normativas de seguridad y, 3) Para brindar información a algún asociado que no se familiarice con Azure.
![](https://i.imgur.com/NoYBpf2.png)
> Ejemplo de uso de etiquetas.

15. Después de la configuración anterior, le damos en "**Revisar y crear**". Nos posiciona en la siguiente pestaña, en la cual nos mostrará los datos generales de nuestro recurso, tantos los que vimos previamente, como el S.O. a utilizar, el plan que usaremos (Al igual que el crédito que se nos cobrará en caso de ser un servicio de paga), y el rendimiento que tendrá dicho recurso (como vemos en la imagen, contará con 1GB de memoria)
![](https://i.imgur.com/LzzOvg3.png)

16. También nos creará una instancia de Base de Datos MySQL:
![](https://i.imgur.com/rZO5Deh.png)

17. Finalmente, le damos clic al botón **Crear**

18. Una vez Azure haya verificado que todos los datos están correctos, empezará a hacer la implementación (no es más que la creación de cada recurso necesario para el correcto funcionamiento de nuestro recurso App Service, clasificados en nuestro grupo de recursos antes creado).
![](https://i.imgur.com/e3XbP0w.png)
![](https://i.imgur.com/B3koZ4g.png)
> La implementación se completó. Ahora podemos **Ir al recurso**

19. Una vez le demos al botón, nos redirigirá al panel de configuración de todo el recurso Azure a profundidad, tanto si se quiere editar la Escalabilidad, Seguridad, Control de acceso, y muchas cosas más que se irán describiendo a lo largo de las demás prácticas.
![](https://i.imgur.com/G6hHiYb.png)
> Para la explicación del siguiente subtema, hacemos clic en la **URL** que se nos proporciona.

### 〔Configuración y vista predeterminada de WordPress〕
Para empezar, aquí veremos la configuración requerida por WordPress, necesaria para ser instalado adecuadamente, al igual que mostrar como acceder al panel de Administración.

1. Empezamos con la configuración de nuestro WordPress. Iniciando con la selección del **idioma**
![](https://i.imgur.com/iyZng7C.png)

2. Rellenamos los datos solicitados, tales como **Nombre de la pagina**, **Usuario**, **Contraseña**, **Correo electrónico**, etc. Esto con el fin de identificarnos a nosotros como los propietarios de la página, y que se nos brinde el acceso a la **Edición** de la misma.
![](https://i.imgur.com/WnGVzNl.png)
![](https://i.imgur.com/YwuvVlB.png)
> Seguidamente, damos clic en **Instalar WordPress**

3. Se nos da indicación de que WordPress ha quedado instalado, configurado y listo para ser usado/visualizado.
![](https://i.imgur.com/etxxiFG.png)

4. Por el momento, la página solo muestra una plantilla por defecto que trae WordPress al inicio, pero que conforme a nuestros conocimientos, podremos ir cambiando a nuestro gusto o a petición del cliente.
![](https://i.imgur.com/VMmB11t.png)

5. Si en la barra de dirección, le anexamos /wp/admin, entraremos en el login de WordPress, ahí colocaremos nuestros datos de registro que hicimos previamente, y nos dará acceso total a la manipulación de la página.
![](https://i.imgur.com/3Jwmw7B.png)
![](https://i.imgur.com/uvCStqB.png)

6. Para finalizar este tema, aquí tenemos la interfaz de administrador de WordPress. Ahora tenemos control total sobre la modificación de la página, la cual veremos en el tema **Rediseño y acabados finales**.
![](https://i.imgur.com/vKLBxIv.png)


### 〔Explicación de componentes del grupo de recursos〕
En este tema, explicaré cada parte que compone nuestro grupo de recursos, para darnos una mejor idea de que ocurrió al momento de crear nuestro App Service.

Nuestro grupo de recursos se llama **Practica1_Darki**. De forma simple, así se llama nuestra carpeta que contiene nuestros recursos creados por Azure.
En esta podemos encontrar 3 elementos:
- **PagWordpress-P1** (de tipo App Service)
- **ASP-Practica1Darki** (de tipo Plan de App Service)
- **dbserver** (de tipo S.U de Azure Database for MySQL)
[Quiero explicarlos en este orden]
![](https://i.imgur.com/saZDT8w.png)

1. Primero, tenemos nuestro recurso **App Service** llamado PagWordpress-P1. Es el encargado de almacenar toda la instalación y configuración de Wordpress, así como la página en si. (Recordemos que App Service sirve para todo lo relacionado a aplicaciones Web)
![](https://i.imgur.com/irGfAPd.png)

2. Continuamos con **Plan de App Service**, ASP-Practica1Darki. Bien, este recurso podemos definirlo como el encargado de manipular/ajustar la cantidad de memoria o almacenamiento asignado al recurso. Recordemos que en el tema anterior dije que el plan seleccionado le asignó a nuestra página una memoria de 1GB. Con eso en mente, este recurso es capaz de alterar ese valor para incrementarlo si llegase a ser necesario por cuestiones de limitaciones o para evitar saturación.
![](https://i.imgur.com/P8nxJtL.png)
>⠀
![](https://i.imgur.com/JdHwBcS.png)
> Escalabilidad Vertical.
![](https://i.imgur.com/l6xsmeo.png)
> Escalabilidad Horizontal. (en este caso, así es)

3. El ultimo recurso, dbserver es un recurso de tipo **Database for MySQL**. Es el encargado de almacenar información/datos del usuario, recopila todo lo relacionado al cliente o persona que se conecte a la página e ingrese algún dato. Ejemplo, supongamos que pedimos al usuario que nos brinde su **Nombre** y **Dirección de correo** para que nosotros le mandemos información de actualizaciones. Estos datos serán almacenados directamente en nuestra base de datos, para que podamos posteriormente trabajar con ellos.
![](https://i.imgur.com/3hwvYkQ.png)

De los tres recursos, este es el más pesado de mantener, debido a que es un servicio de paga caro para una "primera página" o una página de principiantes. Es por eso que se nos hizo énfasis en apagar o borrar este recurso una vez concluida esta práctica.
Aquí les indico como apagar el recurso antes mencionado:
- Basta con darle al botón **Detener**, y seguidamente darle en **Si**
![](https://i.imgur.com/6IcObhc.png)
![](https://i.imgur.com/ZYmqrc4.png)
> Servicio apagado.

![](https://i.imgur.com/EzKcsMK.png)
> Al intentar abrir nuestra página de WordPress, nos mostrará el siguiente mensaje de error, esto es porque falta la base de datos necesaria para que funcione.

### 〔Rediseño y acabados finales de la página WordPress〕
Para finalizar con la práctica, explicaré paso a paso como fue que rediseñe la página Default que brinda WordPress, a una página con diseño profesional. Anexaré al final un gif de como se mira la página completa.

1. Añadimos un tema. Para esto nos vamos a la pestaña **Apariencia** y luego en **Temas**; después en **Añadir tema**. Para esta ocasión elegí el tema ***"Astra"***.
![](https://i.imgur.com/ZnILfON.png)
> El tema es la estructura del sitio.

2. Lo **instalamos** y luego lo **activamos**.
3. Seguido de eso, nos dirigimos al apartado **Plugins**>**Plugins instalados**, y eliminamos todos. Estos plugins son los que se instalan por defecto junto con WordPress, así que no nos serán de utilidad.
4. Ahora, en **Añadir nuevo**, buscamos lo siguiente: **Astra Starter Sites** (también conocido como **Starter Templates**). Procederemos a **Instalar** y **Activar**
![](https://i.imgur.com/OZs4WvT.png)

5. De nueva cuenta en la pestaña de **Plugins instalados**, clic en **Ver biblioteca** del **Starter Templates**.
6. Se nos pedirá elegir un **Maquetador**. Se le podría considerar como un complemento que tiene WordPress para poder permitirnos editar cualquier parte de la página. Elegimos **Elementor**.
![](https://i.imgur.com/Tvtixwk.png)

7. Ahora, el plugin nos desplegará un montón de plantillas de sitios Web, listos para instalar, usar y modificar como nosotros queramos (o como quiera el cliente).
![](https://i.imgur.com/qDVnoop.png)

8. Una vez elegida la plantilla, le das al botón **Importar el sitio completo**. Algo super útil de este plugin, es que automaticamente nos instalará y configurará los plugins necesarios respecto a la plantilla seleccionada para que ésta funcione de la manera correcta.
![](https://i.imgur.com/f0dIhBL.png)
> Astra configurando todo lo que la plantilla necesita para funcionar.

9. Listo, creado y configurado.
![](https://i.imgur.com/yCtgbw5.png)

# 【Resultado final】 
Para finalizar, les dejo este VIDEO de como se ve a detalle la página completa una vez finalizado el diseño/modificación.
[![](https://yt-embed.herokuapp.com/embed?v=-xTWCwV8PPg)](https://www.youtube.com/watch?v=-xTWCwV8PPg "Practica1 - Darki")
