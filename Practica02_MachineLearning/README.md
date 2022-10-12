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
- [Practica 2](#practica-2---entorno-de-ejecución-azure-machine-learning)
    - [Creación del entorno](#creación-del-entorno)
    - [Primer programa en Python](#primer-programa-en-python)
    - [Enlace con Visual Code Studio](#enlace-con-visual-code-studio)
    - [Programa de codificación Binaria](#programa-de-codificación-binaria-hecho-en-azure-ml-en-la-nube)

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

# 【Practica 2 - Entorno de ejecución Azure Machine Learning】
### 〔Creación del entorno〕
1. Entramos al siguiente enlace: https://ml.azure.com/home. Nos logueamos con una cuenta de nuestra preferencia.
![Estudio de Azure Machine Learning](https://i.imgur.com/fTJxkit.png)
> Estudio de Azure Machine Learning.

2. Para trabajar con esta herramienta, nos pedirá que creemos un **Area de trabajo** nueva, pero omitiremos el crearla desde esta página, esto debido a que en el portal de Azure, es más eficiente el poder crear dichas **áreas**.

3. Con lo anterior en mente, nos dirigimos a nuestro [portal Azure](https://portal.azure.com/)
![](https://i.imgur.com/pnj6wr6.png)
4. Una vez aquí, en la barra de busqueda, escribimos **Machine Learning** o **Azure Machine Learning**, seleccionamos la opción. Seguido de ello, nos redirigirá a la ventana de trabajo de recursos.

5. Clic en el botón **Crear**.
![](https://i.imgur.com/ctr2iGn.png)

6. Volvemos a la pantalla de creación de recursos, similar a la que vimos en la práctica anterior (ahora, enfocado a Machine Learning):
![](https://i.imgur.com/zLMWkna.png)
7. Recordando lo mencionado en la práctica 1.
> Lo minimo que todo recurso de Azure **necesita** para ser creado son 4 cosas fundamentales: **Suscripción**, **Grupo de recursos**, **Región** y **Nombre del recurso**

8. Suscripción: En este caso, solo contamos con la suscripción de tipo **Estudiante**, y es la que seleccionamos.
![](https://i.imgur.com/Cgh7uOU.png)

9. Grupo de recursos: Si no hemos tocado nada por el momento, nos encontraremos sin ningún grupo de recursos; por ende, debemos crear uno. Podemos ver los grupos de recursos como "carpetas" de nuestros recursos. En mi caso, yo le puse **Practica2_Darki**.
![](https://i.imgur.com/qogxuZn.png)
> De este modo iré nombrando tanto mis grupos de recursos como mis demás elementos que ocupe en todas mis prácticas para mejor organización.

10. Nombre del recurso (en este caso, **Área de trabajo**): Asignamos el nombre que llevará nuestro recurso y con el cual se le identificará. En mi caso usé: **MachineLearning-P2**
![](https://i.imgur.com/FieEtZb.png)

11. Región: Por ultimo, aquí elegimos en que región de Azure estará localizado nuestro recurso. En este caso elegí **Australia East** (y esto es debido a que nuestra suscripción no cuenta con toda la cobertura de regiones que ofrece Azure, impidiendonos configurar ciertos parametros de nuestros recursos; esto quiere decir: Australia tiene bastante facilidad para operar de esta forma siendo estudiantes)
![](https://i.imgur.com/WUvW0M7.png)

12. Después de la configuración anterior, le damos en "**Revisar y crear**". Nos posiciona en la siguiente pestaña, en la cual nos mostrará los datos generales de nuestro recurso.
![](https://i.imgur.com/X754kMb.png)
13. Finalmente, clic en el botón **Crear**

14. Una vez Azure haya verificado que todos los datos están correctos, empezará a hacer la implementación.
![](https://i.imgur.com/eNjBisd.png)
![](https://i.imgur.com/Nt2wXFA.png)
> La implementación se completó.

15. Una vez implementado, nos regresamos al Estudio de Azure Machine Learning.
![](https://i.imgur.com/OnAXlLt.png)
> Bastará con recargar la página para que nos salga el área de trabajo que hemos creado.

16. Ahora podemos ingresar al área de trabajo. Clic en **Ir a area de trabajo**
![](https://i.imgur.com/BkP34Ht.png)

17. Una vez le demos al botón, nos redirigirá al panel de configuración de todo el recurso.
![](https://i.imgur.com/6GhePvJ.png)
> En este curso se aprenderán a usar **Notebooks**, **ML Automatizado**, **Diseñador**, **Datos**, **Canalizaciones**, **Modelos**, **Puntos de Conexión** y **Procesos**.

### 〔Primer programa en Python〕

Para empezar, debo definir que es un **Notebook**, ya que eso trabajaremos en este tema.

**Notebook**
Es un entorno virtual que nos sirve para ejecutar codigo (normalmente Python), para que no tengamos que instalar Python en nuestras máquinas locales o cualquier entorno de desarrollo del mismo. Todo será creado y ejecutado directamente en la nube.

1. Empezamos dirigiendonos al apartado **Proceso**
2. Ahora en **Instancias de proceso** > **Nuevo**
![](https://i.imgur.com/jWj7KR8.png)

3. Asignamos un nombre. En mi caso, lo llamé **NotebookP1** (aunque debió ser P2 por la practica). Seguido de eso, dejamos CPU por defecto, y en el tamaño de la máquina virtual, elegimos el más barato (porque es una práctica sencilla y no requerimos tanta potencia).
![](https://i.imgur.com/v2ZaUvO.png)

4. Le damos en **Crear**, y esperamos a que termine el proceso.
![](https://i.imgur.com/gyTTvZe.png)
![](https://i.imgur.com/xXQUtNc.png)

5. Una vez creado, nos vamos al apartado **Notebooks**, elegimos la carpeta con nuestro nombre, y creamos un archivo nuevo.
![](https://i.imgur.com/vyLh0WI.png)

6. Le asignamos el **nombre** que queramos, y luego todo por defecto. Después en **Crear**.
![](https://i.imgur.com/0Oam42P.png)

7. Listo, ya tenemos nuestro entorno de desarrollo en la nube con Azure Machine Learning. Ahora solo resta el probarlo creando un programa, por ejemplo, en la imagen podemos ver la programación de un Print que nos muestre en pantalla la frase **Hola mundo**.
![](https://i.imgur.com/rPVFD0E.png)
> Nota: para el siguiente tema, es necesario hacer clic en el botón de **Autentificar** que se encuentra en el recuadro amarillo.


### 〔Enlace con Visual Code Studio〕
En este tema, explicaré como realizar una edición de código usando un entorno de desarrollo **local**, pero logrando modificar el código de **la nube** de forma sincronizada. Para ello usaremos **Visual Studio Code**

1. Primero, es necesario ya tener instalado el Visual Studio Code. Asumiendo que ya contamos con él, damos clic en el botón: **Editar con VS Code**. Y aceptamos la ventana emergente.
![](https://i.imgur.com/zazGuQ2.png)

2. Y **confirmamos** que lo abriremos con la aplicación de Visual Studio.
![](https://i.imgur.com/jAyefPH.png)

3. Una vez abierta, nos saldrán varios mensajes emergentes que nos indicarán que es necesario instalar algunos complementos para que funcione correctamente la conexión entre entornos local y nube.
![](https://i.imgur.com/TSxgI2d.png)
![](https://i.imgur.com/16oItGa.png)
> Aceptamos todo

4. Aquí se nos pedirá loguearnos de nueva cuenta con nuestra cuenta de Azure. Esto es porque VS Code necesita saber a donde hará la conexión, y para ello necesita las credenciales del entorno ML.
![](https://i.imgur.com/6wUMrum.png)
![](https://i.imgur.com/rrq19Ah.png)

5. Y aceptamos que confiamos en estos medios.
![](https://i.imgur.com/wwJP2fk.png)

6. Podemos observar que en VS tenemos exactamente el mismo código que creamos en la nube, pero ahora de forma local. Inclusive nos muestra el mismo resultado de la ejecución.
![](https://i.imgur.com/HeqkPgP.png)

7. Ahora, yo añadí una nueva linea de código; un print("¿como están?"), el cual quiero que se ejecute tanto aquí en el VSCode, como en Azure ML. Al darle a ejecutar, me manda directamente a la barra de busquedas, con una busqueda predeterminada, indicando que hace falta instalar un complemento extra a VSCode que nos permitirá habilitar la conexión con ML y poder mandar los cambios a la nube.
![](https://i.imgur.com/rZOzfGn.png)

8. Dicho complemento se llama Jupyter. Lo instalamos como se nos pide.
![](https://i.imgur.com/VTWEewM.png)

9. Podemos percatarnos que se nos habilitó un nuevo menú de opción arriba de las lineas de código, dichas opciones nos servirán para ejecutar el código tanto local como en la nube.
![](https://i.imgur.com/QTNBqyO.png)

10. Al darle en ejecutar todo, nos dice que podemos ejecutar Python 3.8 con un destino raro; dicho destino, no es sino que la nube propia, nuestro recurso de Azure ML que ya está configurado para empezar a recibir códigos de entornos fuera de si misma.
![](https://i.imgur.com/6JNeJn4.png)

11. y como se puede apreciar, aquí ya se ejecutó tanto la primera linea que se hizo en la nube, como la segunda linea que hice aquí en local.
![](https://i.imgur.com/EDecXsE.png)

12. Como bien mencioné antes, era necesario activar la Autentificación del Azure ML. por tanto, ya quedó listo para recibir código externo.
![](https://i.imgur.com/0YS4CTO.png)

13. Ahora solo es cuestión de cerrar el Notebook, y volverlo a abrir, y podemos ver que se ha actualizado nuestro código con los datos creados en el entorno local. Y posteriormente ejecutado en la nube de manera satisfactoria.
![](https://i.imgur.com/BgXp17m.png)


### 〔Programa de codificación Binaria hecho en Azure ML en la NUBE〕
Para finalizar con la práctica, explicaré este pequeño programa de Python que he implementado en la ML, usando el mismo Notebook.

Convertir un número decimal a binario es muy sencillo: basta con realizar divisiones sucesivas entre 2 y escribir los residuos obtenidos en cada división en orden inverso al que han sido obtenidos.

Por ejemplo el número decimal **23519**:

- 23519 / 2 = 11759 Residuo: **1**
- 11759 / 2 = 5879 Residuo: **1**
- 5879 / 2 = 2939 Residuo: **1**
- 2939 / 2 = 1469 Residuo: **1**
- 1469 / 2 = 734 Residuo: **1**
- 734 / 2 = 367 Residuo **0**
- 367 / 2 = 183 Residuo: **1**
- 183 / 2 = 91 Residuo: **1**
- 91 / 2 = 45 Residuo: **1**
- 45 / 2 = 22 Residuo: **1**
- 22/ 2 = 11  Residuo: **0**
- 11 / 2 = 5  Residuo: **1**
- 5 / 2 = 2 Residuo: **1**
- 2 / 2 = 1  Residuo: **0**
- 1 / 2 = 0  Residuo: **1**

Acomodando los residuos en orden inverso el número decimal **23519** sería el **101101111011111** binario.

Aplicando ese razonamiento.
1. Tenemos nuestra función llamada **Binario** con el atributo **decimal**
2. **binario** es igual a "", esto es porque queremos que dicha variable esté vacía hasta que el usuario sea capaz de ingresarle algún **valor/número** sobre el cual se le aplicará la **codificación** Binaria.
3. Seguido de eso, se crea un While que se ejecuta mientras que el residuo de **decimal** dividido entre 2 sea diferente de 0.
4. En la siguiente linea, se convierte a **String** la operación de **decimal** modulo de 2, y sumado al propio **binario**
5. Ahora decimal es igual a dividir decimal entre 2.
6. Se retorna de forma String a decimal y se le suma binario.
7. Para finalizar, se crea la variable numero que tiene un input el cual recibe el número de usuario. Después, se imprime el resultado de toda la operación.
![](https://i.imgur.com/7GyUSsD.png)
> Como podemos ver, es exactamente el mismo resultado que vimos arriba.

Ahora, procederé a dejar unos cuantos ejemplos más.

- Número **556**

![](https://i.imgur.com/mKz0zRv.png)
![](https://i.imgur.com/F8EpYW2.png)

- Número **37**

![](https://i.imgur.com/Qs8lOUb.png)
![](https://i.imgur.com/Mh4TPys.png)

- Número **1163**

![](https://i.imgur.com/1LMUrfT.png)
![](https://i.imgur.com/twsXBVs.png)

- Número **2606**

![](https://i.imgur.com/6DUEVXa.png)
![](https://i.imgur.com/hS1ZziO.png)