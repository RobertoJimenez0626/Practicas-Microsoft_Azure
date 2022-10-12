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

 - [Introducción a App Service](#introducción-a-app-service)
    - [¿Por qué usar App Service?](#por-que-usar-app-service)
    - [Limitaciones](#limitaciones)
- [Practica 5](#practica-5-implementación-de-pagina-web-con-app-service)
    - [Descargar ejemplo de Github](#descargar-ejemplo-de-github)
    - [Subir proyecto a repositorio personal](#subir-proyecto-a-repositorio-personal)
    - [Creando recurso App Service](#creando-recurso-app-service)
    - [Implementación en App Service](#implementación-en-app-service)
    - [Resultado final](#resultado-final)

-------

# 【Introducción a App Service】

![](https://icon-library.com/images/azure-icon/azure-icon-28.jpg)

*Azure App Service* es un servicio basado en HTTP para hospedar aplicaciones web, API REST y back-ends para dispositivos móviles. Puede desarrollarlo en su lenguaje preferido, ya sea. NET, .NET Core, Java, Ruby, Node.js, PHP o Python. Las aplicaciones se ejecutan y escalan fácilmente en los entornos basados tanto en Windows como en Linux.

App Service no solo agrega a la aplicación la funcionalidad de Microsoft Azure, como la seguridad, el equilibrio de carga, el escalado automático y la administración automatizada. También puede sacar partido de sus funcionalidades de DevOps, por ejemplo, la implementación continua desde Azure DevOps, GitHub, Docker Hub y otros orígenes, la administración de paquetes, entornos de ensayo, dominio personalizado y certificados TLS/SSL.

Con App Service, se paga por los recursos de proceso de Azure que se utilizan. Los recursos de proceso que usa se determinan mediante el plan de App Service en el que ejecuta las aplicaciones.

### 〔¿Por que usar App Service?〕
Azure App Service es una oferta de plataforma como servicio (PaaS) completamente administrada para desarrolladores. Estas son algunas características clave de App Service:

- Varios lenguajes y plataformas: App Service tiene compatibilidad de primera clase con ASP.NET, ASP.NET Core, Java, Ruby, Node.js, PHP o Python. También puede ejecutar PowerShell y otros scripts o ejecutables como servicios en segundo plano.
- Entorno de producción administrado: App Service parchea y mantiene los marcos del sistema operativo y del lenguaje de forma automática. Invierta su tiempo en escribir aplicaciones magníficas y deje que Azure se preocupe por la plataforma.
- Contenedores y Docker: aplique Docker a la aplicación y hospede un contenedor de Windows o Linux personalizado en App Service. Ejecute las aplicaciones de varios contenedores con Docker Compose. Migre sus habilidades de Docker directamente a App Service.
- Optimización con DevOps: configure la integración y la implementación continuas con Azure DevOps, GitHub, BitBucket, Docker Hub o Azure Container Registry. Promueva actualizaciones a través de entornos de ensayo y prueba. Administre las aplicaciones de App Service mediante Azure PowerShell o la interfaz de la línea de comandos (CLI) multiplataforma.
- Escala global con alta disponibilidad: escale verticalmente u horizontalmente de forma manual o automática. Hospede las aplicaciones en cualquier parte de la infraestructura del centro de datos global de Microsoft y el Acuerdo de Nivel de Servicio de App Service promete una alta disponibilidad.
- Conexiones a plataformas SaaS y a datos locales: elija entre más de 50 conectores para sistemas empresariales (como SAP), servicios SaaS (como Salesforce) y servicios de Internet (como Facebook). Acceda a los datos locales mediante Conexiones híbridas y Azure Virtual Networks.
- Seguridad y cumplimiento: App Service cumple con ISO, SOC y PCI. Autentique a los usuarios con Azure Active Directory, Google, Facebook, Twitter o una cuenta Microsoft. Cree restricciones de direcciones IP y administre las identidades de servicio.
- Plantillas de aplicación: elija entre una amplia lista de plantillas de aplicación en Azure Marketplace, como WordPress, Joomla y Drupal.
- Integración con Visual Studio y Visual Studio Code : existen herramientas dedicadas en Visual Studio y Visual Studio Code que permiten optimizar las tareas de creación, implementación y depuración.
- API y características para móviles: App Service proporciona compatibilidad CORS llave en mano para escenarios de la API RESTful y simplifica los escenarios de aplicaciones móviles al permitir la autenticación, la sincronización de datos sin conexión, las notificaciones push, y mucho más.
- Código sin servidor: ejecute un fragmento de código o script a petición sin tener que proporcionar explícitamente ni administrar la infraestructura, y pague solo por el tiempo de proceso que el código utiliza realmente (vea Azure Functions).

### 〔Limitaciones〕
> ⚠ **Nota**
*Los planes de App Service para Windows y Linux ahora pueden compartir grupos de recursos. Esta limitación ya no se aplica desde la plataforma y los grupos de recursos existentes se han actualizado para admitir este hecho.*

- App Service en Linux no se admite en el plan de tarifa Compartido.
- Azure Portal solo muestra las características que funcionan actualmente para las aplicaciones Linux. A medida que se habiliten las características, se activarán en el portal.
- Cuando se implementen en imágenes integradas, el código y el contenido se asignarán a un volumen de almacenamiento para el contenido web, respaldado por Azure Storage. La latencia de disco de este volumen es mayor y más variable que la del sistema de archivos del contenedor. Las aplicaciones que requieran muchos accesos de solo lectura a archivos de contenido pueden beneficiarse de la implementación de contenedores personalizados, que permite colocar los archivos en el sistema de archivos de contenedor en lugar de en el volumen de contenido.

--------------

# 【Practica 5: Implementación de Pagina Web con App Service】
### 〔Descargar ejemplo de Github〕

Aquí explicaré todo lo que realicé para crear el repositorio local y descargar el ejemplo de GitHub.

1. Primero que nada, usando Git Bash, navegué por los directorios *Desktop* > *Practicas Azure*. Dentro de esa carpeta, usé el comando `mkdir` para crear un nuevo directorio llamado **Practica5_Darki**

![](https://i.imgur.com/wMu3psA.png)

2. Una vez dentro de la nueva carpeta creada, procedí a inicializar el repositorio con `git init`.

3. Seguido de ello, fui a la direccion Web de GitHub donde se encontraba el ejemplo que usé en Azure. Di clic en *Code* > *Download ZIP*

![](https://i.imgur.com/l84Zbs8.png)

4. Veremos que hay varios archivos, pero son otros ejemplos de paginas web con otras arquitecturas, las que usaré es la que está señalada, llamada **pagina web**.

![](https://i.imgur.com/V3h5FSX.png)

5. Y procedí a colocar el contenido de dicha carpeta dentro del directorio del repositorio creado previamente, tal como se ve en la imagen:

![](https://i.imgur.com/Kvk3B7A.png)


### 〔Subir proyecto a repositorio personal〕
Aquí explico como subí todo el contenido de la pagina web a un repositorio propio de mi cuenta de GitHub. 

Dicha cuenta se enlazará a Azure y de ahí extraeremos este repositorio.

1. Primero, creé un nuevo repositorio en GitHub con el nombre marcado en rojo.

![](https://i.imgur.com/Amhecvl.png)

2. Usé los comandos de Bash `git remote` para enlazar el repositorio local con el de nube.

3. Luego hice un `git push` para subir todo a GitHub.

![](https://i.imgur.com/4Td6n0z.png)



### 〔Creando recurso App Service〕
Explicaré como crear un recurso App Service en Azure, los parametros que me solicita y como se implementaré la página una vez creado.

1. En Azure Portal buscamos *App Service*, después nos encontraremos una interfaz como la siguiente, y le damos en *Crear*:

![](https://i.imgur.com/9HRqv6I.png)

2. Nos llevará a esta ventana de configuración, y como cualquier recurso de Azure nos solicitará *Suscripción*, *grupo de recursos*, *Nombre* y *Region*. (**Practica5**, **ASPágina-P5**, **Central US**, respectivamente)

![](https://i.imgur.com/btPE9RZ.png)

3. Como ya dijimos, en App Service no debemos preocuparnos por configurar un entorno de desarrollo (VM y todo lo que conlleva administrar una); aquí solo elegiremos el lenguaje que usaremos para trabajar o programar. En este caso se eligió PHP 8.0, aunque realmente no programaremos, es lo que necesita nuestra página para funcionar.

4. Ahora, la siguiente opción *SKU y tamaño*, hace referencia a la capacidad que tendrá nuestra aplicación en su ejecución, por defecto nos pone el plan de paga (verde), pero nosotros lo bajaremos al plan gratuito, el que nos ofrece 1GB. 

![](https://i.imgur.com/EL9wbeB.png)

5. Ahora en *Revisar y crear* > *Crear*

![](https://i.imgur.com/FAB0MRM.png)
![](https://i.imgur.com/Sy6x7xA.png)

6. Y esperamos a que la implementación se termine de realizar.

![](https://i.imgur.com/Nb5QeLr.png)


### 〔Implementación en App Service〕
Ahora, haremos la *implementación* del proyecto con el recurso *App Service* que creamos.

1. Tras crear el *App Service*, ingresamos al recurso, en la pestaña de la izquierda, vamos al apartado *Implementación* > *Centro de implementación*

![](https://i.imgur.com/F59uR46.png)

2. En *origen*, seleccionamos uno de los servicios que disponemos para implementar un proyecto/repositorio, en este caso, GitHub; tras seleccionarlo, nos pedirá asociarlo a Azure ingresando nuestras credenciales de login.

3. Después de eso, nos pedirá seleccionar "categorias" en las cuales nosotros podemos encontrar nuestros repositorios.

4. En mi caso, organización sería mi nombre de usuario **RobertoJimenez0626**, en repositorio, elegiré el que creé para la práctica **Practica5_Darki**, y la rama, la cual es **Master**

![](https://i.imgur.com/nMdEYWX.png)

5. Después, clic en *Guardar*

6. Si volvemos al repositorio en GitHub, y vamos a la sección de *Actions*, podemos ve que se nos creó por parte de Azure un *Flujo de trabajo*, esto es la forma en la que la nube empieza a trabajar con nuestros archivos para ser implementados.

![](https://i.imgur.com/VZNvIHp.png)
> GitHub ya reconoce que App Service es el que está solicitando esta operación.

7. Podemos ver que se *Construye* y luego se *Desplega*. (Build and Deploy)

![](https://i.imgur.com/1zFEOZU.png)
![](https://i.imgur.com/yogEocM.png)

8. Ahora, una vez todo terminado, nuestro proyecto está subido a Azure App Service, y podemos acceder a él mediante la URL proporcionada por dicho servicio.

### 〔Resultado final〕
Para finalizar, aquí se encuentra un pequeño video del resultado de nuestra página web implementada.

[![](https://yt-embed.herokuapp.com/embed?v=RvJVTmvraJo)](https://www.youtube.com/watch?v=RvJVTmvraJo "Practica5 - Darki - AppService")