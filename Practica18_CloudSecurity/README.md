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

- [Introducción a Microsoft Defender for Cloud](#introducción-a-microsoft-defender-for-cloud)
    - [Protección de los recursos y seguimiento del progreso de la seguridad](#protección-de-los-recursos-y-seguimiento-del-progreso-de-la-seguridad)
    - [CSPM: Corrección de problemas de seguridad y mejora de la posición de seguridad](#cspm-corrección-de-problemas-de-seguridad-y-mejora-de-la-posición-de-seguridad)
    - [CWP: identificación de los requisitos propios de seguridad de las cargas de trabajo](#cwp-identificación-de-los-requisitos-propios-de-seguridad-de-las-cargas-de-trabajo)
    - [Defensa de los recursos nativos de Azure](#defensa-de-los-recursos-nativos-de-azure)
    - [Defensa de los recursos locales](#defensa-de-los-recursos-locales)
    - [Defensa de los recursos que se ejecutan en otras nubes](#defensa-de-los-recursos-que-se-ejecutan-en-otras-nubes)
- [Introducción a Azure Sentinel](#introducción-a-azure-sentinel)
    - [Conexión a todos sus datos](#conexión-a-todos-sus-datos)
    - [Workbooks](#workbooks)
    - [Análisis](#análisis)
    - [Automatización y orquestación de la seguridad](#automatización-y-orquestación-de-la-seguridad)
    - [Investigación](#investigación)
    - [Búsqueda](#búsqueda)
    - [Cuaderno](#cuaderno)
    - [Comunidad](#comunidad)
- [Introducción a Azure Key Vault](#introducción-a-azure-key-vault)
    - [Authentication](#authentication)
    - [Cifrado de datos en tránsito](#cifrado-de-datos-en-tránsito)
    - [Roles de Key Vault](#roles-de-key-vault)
- [Practica 18](#practica-18-seguridad-en-azure)
    - [Microsoft Defender for Cloud](#microsoft-defender-for-cloud)
    - [Azure Sentinel](#azure-sentinel)
    - [Azure Key Vault](#azure-key-vault)

-------

# 【Introducción a Microsoft Defender for Cloud】

![](https://repository-images.githubusercontent.com/184655500/0c3a9480-c615-11ea-9290-28f0d7792688)

*Microsoft Defender for Cloud* es un recurso de administración de la posición de seguridad en la nube (CSPM) y la plataforma de protección de cargas de trabajo en la nube (CWPP) para todos los recursos de Azure, locales y multinube (Amazon AWS y Google GCP). Defender for Cloud cubre tres necesidades vitales a medida que administra la seguridad de los recursos y las cargas de trabajo en la nube y en el entorno local:

![](https://docs.microsoft.com/es-es/azure/defender-for-cloud/media/defender-for-cloud-introduction/defender-for-cloud-synopsis.png)

- **Puntuación de seguridad de Defender for Cloud**: ***evalúa*** continuamente su posición de seguridad para que pueda hacer un seguimiento de las nuevas oportunidades de seguridad e informar precisamente sobre el progreso de los esfuerzos de seguridad.
- **Recomendaciones de Defender for Cloud**: ***protege*** las cargas de trabajo con acciones paso a paso que protegen las cargas de trabajo frente a riesgos de seguridad conocidos.
- **Alertas de Defender for Cloud**: ***defiende*** las cargas de trabajo en tiempo real para que pueda reaccionar de inmediato e impedir que tengan lugar eventos de seguridad.

### 〔Protección de los recursos y seguimiento del progreso de la seguridad〕
Las características de Microsoft Defender for Cloud cubren los dos grandes pilares de la seguridad en la nube: la plataforma de protección de cargas de trabajo en la nube (CWPP) y la administración de la posición de seguridad en la nube (CSPM).

### 〔CSPM: Corrección de problemas de seguridad y mejora de la posición de seguridad〕
En Defender for Cloud, las características de administración de posturas proporcionan:

- **Guía de protección**: para ayudarle a mejorar la seguridad de forma eficaz.
- **Visibilidad**: para ayudarle a entender su situación de seguridad actual.
Defender for Cloud evalúa continuamente los recursos, las suscripciones y la organización en busca de problemas de seguridad, y muestra la posición de seguridad en la **puntuación de seguridad**, una puntuación agregada de los resultados de seguridad que le indica, de un vistazo, la situación actual de seguridad: cuanto mayor sea la puntuación, menor será el nivel de riesgo identificado.

Tan pronto como abre Defender for Cloud por primera vez, Defender for Cloud:

- **Genera una puntuación de seguridad** para sus suscripciones en función de la evaluación de sus recursos conectados en comparación con la guía de Azure Security Benchmark. Use la puntuación para comprender su posición de seguridad y el panel de cumplimiento para revisar el cumplimiento con la prueba comparativa integrada. Cuando haya habilitado las características de seguridad mejoradas, puede personalizar los estándares que se usan para evaluar el cumplimiento y agregar otras regulaciones (como NIST y Azure CIS) o requisitos de seguridad específicos de la organización. También puede aplicar recomendaciones y puntuar en función de los estándares de procedimientos recomendados de seguridad fundamentales de AWS.

- **Proporciona recomendaciones de protección** en función de los errores de configuración y los puntos débiles de seguridad identificados. Use estas recomendaciones de seguridad para reforzar la posición de seguridad de los recursos de Azure, híbridos y multinube de su organización.

### 〔CWP: identificación de los requisitos propios de seguridad de las cargas de trabajo〕
Defender for Cloud ofrece alertas de seguridad con tecnología de Inteligencia sobre amenazas de Microsoft. También incluye una gama de protecciones avanzadas e inteligentes para las cargas de trabajo. Las protecciones de cargas de trabajo se proporcionan a través de planes de Microsoft Defender específicos de los tipos de recursos de las suscripciones. Por ejemplo, puede habilitar **Microsoft Defender para Storage** y recibir alertas sobre actividades sospechosas relacionadas con los recursos de almacenamiento.

### 〔Defensa de los recursos nativos de Azure〕
Defender for Cloud le permite detectar amenazas en:

- **Servicios de PaaS de Azure**: puede detectar amenazas dirigidas a servicios de Azure como Azure App Service, Azure SQL, la cuenta de Azure Storage y otros servicios de datos. También puede realizar la detección de anomalías en los registros de actividad de Azure mediante la integración nativa con Microsoft Defender para aplicaciones en la nube (anteriormente conocido como Microsoft Cloud App Security).

- **Servicios de datos de Azure**: Defender for Cloud incluye funcionalidades que le ayudarán a clasificar automáticamente los datos en Azure SQL. También puede obtener evaluaciones de las posibles vulnerabilidades en los servicios de Azure SQL y Azure Storage, además de recomendaciones sobre cómo mitigarlas.

- **Redes**: Defender for Cloud le permite limitar la exposición a los ataques por fuerza bruta. Si reduce el acceso a los puertos de las máquinas virtuales mediante el acceso de máquina virtual Just-In-Time, puede proteger la red al prevenir el acceso innecesario. Puede establecer directivas de acceso seguro en los puertos seleccionados, solo para usuarios autorizados, direcciones IP o intervalos de direcciones IP de origen permitidos y durante un período limitado.

### 〔Defensa de los recursos locales〕
Además de defender el entorno de Azure, puede agregar funcionalidades de Defender for Cloud a su entorno de nube híbrida para proteger los servidores que no sean de Azure. Para que pueda centrarse en lo que más le importa, obtenga inteligencia personalizada sobre las amenazas y alertas prioritarias según su entorno específico.

Para ampliar la protección a las máquinas locales, implemente Azure Arc y habilite las características de seguridad mejoradas de Defender for Cloud.

### 〔Defensa de los recursos que se ejecutan en otras nubes〕
Defender for Cloud puede proteger los recursos de otras nubes (como AWS y GCP).

Por ejemplo, si ha conectado una cuenta de Amazon Web Services (AWS) a una suscripción de Azure, puede habilitar cualquiera de estas protecciones:

- **Las características de CSPM de Defender para la nube** se extienden a los recursos de AWS. Este plan sin agente evalúa los recursos de AWS según las recomendaciones de seguridad específicas de AWS, que se incluyen en la puntuación de seguridad. También se evaluará el cumplimiento de los recursos de los estándares integrados específicos de AWS (AWS CIS, AWS PCI DSS y Procedimientos recomendados de seguridad fundamentales de AWS). La página de inventario de recursos de Defender for Cloud es una característica habilitada para varias nubes, que permite administrar los recursos de AWS junto con los de Azure.
- **Microsoft Defender para Kubernetes** amplía la detección de amenazas de contenedores y defensas avanzadas a los **clústeres Linux de Amazon EKS**.
- **Microsoft Defender para servidores** proporciona la detección de amenazas y defensas avanzadas a las instancias de EC2 con Windows y Linux. Este plan incluye la licencia integrada de Microsoft Defender para punto de conexión, líneas base de seguridad y evaluaciones de nivel de sistema operativo, análisis de evaluación de vulnerabilidades, controles de aplicaciones adaptables (AAC), supervisión de la integridad de los archivos (FIM) y mucho más.

-------

# 【Introducción a Azure Sentinel】

![](https://www.cloudsma.com/wp-content/uploads/2020/05/azure-sentinel-twitter.png)

> ⚠️ **Nota**
Azure Sentinel ahora se denomina Microsoft Sentinel y se actualizarán estas páginas en las próximas semanas.

*Microsoft Sentinel* es una solución de **administración de eventos e información de seguridad (SIEM)** y **respuesta automatizada de orquestación de seguridad (SOAR)** escalable y nativa de la nube. Microsoft Sentinel ofrece análisis de seguridad inteligente e inteligencia frente a amenazas en toda la empresa, de forma que proporciona una única solución para la detección de ataques, la visibilidad de amenazas, la búsqueda proactiva y la respuesta a amenazas.

Microsoft Sentinel permite obtener una vista general de toda la empresa, lo que suaviza la tensión de ataques cada vez más sofisticados, volúmenes de alertas cada vez mayores y plazos de resolución largos.

- **Recopile datos a escala de nube** de todos los usuarios, dispositivos, aplicaciones y de toda la infraestructura, tanto en el entorno local como en diversas nubes.

- **Detecte amenazas que antes no se detectaban** y minimice los falsos positivos mediante el análisis y la inteligencia sobre amenazas sin precedentes de Microsoft.

- **Investigue amenazas con inteligencia artificial** y busque actividades sospechosas a escala, aprovechando el trabajo de ciberseguridad que ha llevado a cabo Microsoft durante décadas.

- **Responda a los incidentes con rapidez** con la orquestación y la automatización de tareas comunes integradas.

![](https://docs.microsoft.com/es-es/azure/sentinel/media/overview/core-capabilities.png)

Creado sobre la gama completa de servicios de Azure existentes, Microsoft Azure Sentinel incorpora de forma nativa bases contrastadas, como Log Analytics y Logic Apps. Microsoft Azure Sentinel enriquece la investigación y la detección con AI al proporcionar el flujo de inteligencia de amenazas de Microsoft y permitirle aportar su propia inteligencia de amenazas.

### 〔Conexión a todos sus datos〕
Para incorporar Microsoft Azure Sentinel, primero debe conectarse a sus orígenes de seguridad.

Microsoft Azure Sentinel incluye varios conectores para soluciones de Microsoft, que están disponibles inmediatamente y proporcionan integración en tiempo real, entre las que se incluyen las soluciones de Microsoft 365 Defender (anteriormente, Protección contra amenazas de Microsoft) y orígenes de Microsoft 365, incluido Office 365, Azure AD, Microsoft Defender for Identity (anteriormente, Azure ATP) y Microsoft Defender for Cloud Apps, entre otros. Además, hay conectores integrados al amplio ecosistema de seguridad para soluciones que no son de Microsoft. También puede usar el formato de evento común, Syslog o las API de REST para conectar los orígenes de datos con Microsoft Azure Sentinel.

![](https://docs.microsoft.com/es-es/azure/sentinel/media/collect-data/collect-data-page.png)

### 〔Workbooks〕
Después de que haya conectado los orígenes de datos a Microsoft Azure Sentinel, puede supervisar los datos mediante la integración de Microsoft Azure Sentinel con los libros de Azure Monitor, lo que proporciona versatilidad al crear libros personalizados.

Aunque los libros se muestran de manera diferente en Microsoft Azure Sentinel, puede que le resulte útil ver cómo crear informes interactivos con los libros de Azure Monitor. Microsoft Azure Sentinel permite crear libros personalizados en los datos y también incluye plantillas de libro integradas que permiten obtener información rápidamente en los datos en cuanto se conecta con un origen de datos.

![](https://docs.microsoft.com/es-es/azure/sentinel/media/tutorial-monitor-data/access-workbooks.png)

- Los libros están diseñados para que los ingenieros y analistas de SOC de todos los niveles visualicen los datos.

- Aunque los libros son más adecuados para vistas generales de los datos de Microsoft Azure Sentinel y no requieren ningún conocimiento de codificación, no se pueden integrar libros con datos externos.

### 〔Análisis〕
Para reducir el ruido y minimizar el número de alertas que tiene que revisar e investigar, Microsoft Azure Sentinel usa análisis para correlacionar las alertas con los incidentes. Los **incidentes** son grupos de alertas relacionadas que, juntas, crean una posible amenaza procesable que se puede investigar y resolver. Use las reglas de correlación integrada tal cual, o úselas como punto de partida para crear las suyas propias. Microsoft Azure Sentinel también proporciona reglas de aprendizaje automático para asignar el comportamiento de red y buscar luego anomalías en los recursos. Estos análisis conectan los puntos, al combinar alertas de baja fidelidad sobre distintas entidades en posibles incidentes de seguridad de alta fidelidad.

![](https://docs.microsoft.com/es-es/azure/sentinel/media/investigate-cases/incident-severity.png#lightbox)

### 〔Automatización y orquestación de la seguridad〕
Automatice las tareas comunes y simplifique la orquestación de la seguridad con cuadernos de estrategias que se integran con los servicios de Azure y las herramientas existentes.

Construida sobre la base de Azure Logic Apps, la solución de automatización y orquestación de Microsoft Azure Sentinel proporciona una arquitectura muy extensible que permite una automatización escalable a medida que emergen nuevas tecnologías y amenazas. Para crear cuadernos de estrategias con Azure Logic Apps, puede elegir de una galería creciente de cuadernos de estrategias integrados. Estos incluyen más de 200 conectores para servicios, como Azure Functions. Los conectores permiten aplicar cualquier lógica personalizada en el código, ServiceNow, Jira, Zendesk, solicitudes HTTP, Microsoft Teams, Slack, Windows Defender ATP y Defender for Cloud Apps.

Por ejemplo, si usa el sistema de vales de ServiceNow, puede usar las herramientas proporcionadas para usar Azure Logic Apps para automatizar los flujos de trabajo y abrir un vale en ServiceNow cada vez que se detecta un evento determinado.

![](https://docs.microsoft.com/es-es/azure/sentinel/media/tutorial-respond-threats-playbook/logic-app.png)

- Los cuadernos de procedimientos están diseñados para ingenieros y analistas de SOC de todos los niveles, con el fin de automatizar y simplificar las tareas, incluida la ingesta de datos, el enriquecimiento, la investigación y la corrección.

- Los cuadernos de estrategias son más adecuados para tareas únicas y repetibles, y no requieren ningún conocimiento de codificación. Los cuadernos de reproducción no son adecuados para cadenas de tareas ad hoc o complejas, ni para documentar y compartir evidencias.

### 〔Investigación〕
Las herramientas de investigación profunda de Microsoft Azure Sentinel están actualmente en versión preliminar y le ayudan a conocer el ámbito y a encontrar la causa principal de una posible amenaza de seguridad. Puede elegir una entidad en el gráfico interactivo para hacer preguntas interesantes sobre ella y explorar en profundidad esa entidad y sus conexiones para llegar a la causa principal de la amenaza.

![](https://docs.microsoft.com/es-es/azure/sentinel/media/investigate-cases/map-timeline.png)

### 〔Búsqueda〕
Use las eficaces herramientas de búsqueda y consulta de Microsoft Azure Sentinel, basadas en el marco MITRE, que le permiten buscar de forma proactiva amenazas de seguridad en todos los orígenes de datos de la organización, antes de que se desencadene una alerta. Una vez que ha descubierto qué consulta de búsqueda proporciona las conclusiones más valiosas sobre posibles ataques, también puede crear reglas de detección personalizadas basadas en la consulta y exponer esas conclusiones como alertas para los respondedores a los incidentes de seguridad. Durante la búsqueda puede crear marcadores de los eventos interesantes, para así poder volver a ellos más tarde, compartirlos con otros usuarios y agruparlos con otros eventos correlacionados para crear un incidente de investigación convincente.

![](https://docs.microsoft.com/es-es/azure/sentinel/media/overview/hunting.png)

### 〔Cuaderno〕
Microsoft Azure Sentinel admite cuadernos de Jupyter en áreas de trabajo de Azure Machine Learning, incluidas las bibliotecas completa para el aprendizaje automático, la visualización y el análisis de datos.

Use cuadernos en Microsoft Azure Sentinel para ampliar el ámbito de lo que puede hacer con los datos de Microsoft Azure Sentinel. Por ejemplo, realizar análisis que no están integrados en Microsoft Azure Sentinel, como algunas características de aprendizaje automático de Python, crear visualizaciones de datos que no están integradas en Microsoft Azure Sentinel, como escalas de tiempo personalizadas y árboles de proceso, o integrar orígenes de datos fuera de Microsoft Azure Sentinel, como un conjunto de datos local.

![](https://docs.microsoft.com/es-es/azure/sentinel/media/notebooks/sentinel-notebooks-on-machine-learning.png)

- Los cuadernos de Microsoft Azure Sentinel están destinados a buscadores de amenazas o analistas de nivel 2 y 3, investigadores de incidentes, científicos de datos e investigadores de seguridad.

- Los cuadernos proporcionan consultas tanto a datos de Microsoft Azure Sentinel como externos, características para el enriquecimiento de datos, la investigación, la visualización, la búsqueda, el aprendizaje automático y el análisis de macrodatos.

- Los cuadernos son adecuados para cadenas más complejas de tareas repetibles, controles de procedimientos ad hoc, aprendizaje automático y análisis personalizado, admiten bibliotecas de Python enriquecidas para manipular y visualizar datos, y son útiles para documentar y compartir evidencias de análisis.

- Los cuadernos requieren una curva de aprendizaje más alta y conocimientos de codificación, y tienen compatibilidad limitada con la automatización.

### 〔Comunidad〕
La comunidad Microsoft Azure Sentinel es un recurso muy eficaz para la detección y la automatización de amenazas. Nuestros analistas de seguridad de Microsoft crean y agregan constantemente nuevos libros, cuadernos de estrategias, consultas de búsqueda, etc. y los publican en la comunidad para que los pueda usar en su entorno. Puede descargar contenido de ejemplo del repositorio de GitHub privado de la comunidad para crear libros personalizados, consultas de búsqueda, cuadernos y cuadernos de estrategias Microsoft Azure Sentinel.

![](https://docs.microsoft.com/es-es/azure/sentinel/media/overview/community.png)

-------

# 【Introducción a Azure Key Vault】

![](https://azure.microsoft.com/svghandler/key-vault/?width=600&height=315)

*Azure Key Vault* es un servicio en la nube para el almacenamiento de los secretos y el acceso a estos de forma segura. Un secreto es todo aquello cuyo acceso desea controlar de forma estricta, como las claves API, las contraseñas, los certificados o las claves criptográficas. El servicio Key Vault admite dos tipos de contenedores: almacenes y grupos de módulos de seguridad de hardware administrados (HSM). Los almacenes permiten almacenar software y claves, secretos y certificados respaldados por HSM. Los grupos HSM administrados solo admiten claves respaldadas por HSM.

Estos son otros términos importantes:

- **Tenant**: un inquilino es la organización que posee y administra una instancia específica de los servicios en la nube de Microsoft. Se usa más a menudo para hacer referencia al conjunto de servicios de Azure y Microsoft 365 de una organización.

- **Propietario del almacén**: un propietario del almacén puede crear un almacén de claves y obtener acceso completo y control sobre él. El propietario del almacén también puede configurar una auditoría para registrar quién accede a los secretos y claves. Los administradores pueden controlar el ciclo de vida de la clave. Pueden revertir a una nueva versión de la clave, realizar copias de seguridad de ella y efectuar otras tareas relacionadas.

- **Consumidor del almacén**: un consumidor del almacén puede realizar acciones en los recursos del almacén de claves si el propietario del almacén le concede acceso de consumidor. Las acciones disponibles dependen de los permisos concedidos.

- **Administradores de HSM administrado**: los usuarios que tienen asignado el rol de administrador tienen un control total sobre los grupos HSM administrados. Pueden crear más asignaciones de roles para delegar el acceso controlado a otros usuarios.

- **Usuario o responsable de criptografía de HSM administrado**: los roles integrados que normalmente se asignan a usuarios o entidades de servicio que realizarán operaciones criptográficas mediante claves en HSM administrado. El usuario criptográfico puede crear claves, pero no puede eliminarlas.

- **Usuario de cifrado del servicio de criptografía de HSM administrado**: rol integrado que normalmente se asigna a una identidad de servicio administrada por las cuentas de servicio (por ejemplo, la cuenta de almacenamiento) para el cifrado de datos en reposo con la clave administrada por el cliente.

- **Recursos**: un recurso es un elemento administrable que está disponible a través de Azure. Ejemplos comunes son una máquina virtual, una cuenta de almacenamiento, una aplicación web, una base de datos y una red virtual. Hay muchos más.

- **Grupo de recursos**: Un grupo de recursos es un contenedor que almacena los recursos relacionados con una solución de Azure. El grupo de recursos puede incluir todos los recursos de la solución o solo aquellos que se desean administrar como grupo. Para decidir cómo asignar los recursos a los grupos de recursos, tenga en cuenta lo que más conviene a su organización.

- **Entidad de seguridad**: una entidad de seguridad de Azure es una identidad de seguridad que usan las aplicaciones, los servicios y las herramientas de automatización que ha creado el usuario para acceder a recursos específicos de Azure. Se puede considerar una "identidad de usuario" (nombre de usuario y contraseña o certificado) con un rol específico y permisos estrechamente controlados. A diferencia de una identidad de usuario general, una entidad de seguridad solo necesita poder realizar acciones específicas. Mejora la seguridad si le concede el nivel de permiso mínimo necesario para realizar sus tareas de administración. Una entidad de seguridad que se usa con una aplicación o un servicio se denomina específicamente entidad de servicio.

- **Azure Active Directory (Azure AD)**: Azure AD es el servicio de Active Directory para un inquilino. Cada directorio tiene uno o varios dominios. Un directorio puede tener varias suscripciones asociadas, pero solo un inquilino.

- **Identificador de inquilino de Azure**: un identificador de inquilino es una manera única para identificar una instancia de Azure Active Directory dentro de una suscripción de Azure.

- **Identidades administradas**: Azure Key Vault proporciona una manera de almacenar de forma segura las credenciales y otras claves y secretos, pero el código tiene que autenticarse en Key Vault para recuperarlos. El uso de una identidad administrada permite solucionar este problema más fácilmente, al proporcionar a los servicios de Azure una identidad administrada automáticamente en Azure AD. Puede usar esta identidad para autenticarse Key Vault o en cualquier servicio que admita la autenticación de Azure AD, sin necesidad de tener credenciales en el código.

### 〔Authentication〕
Para realizar cualquier operación con Key Vault, deberá autenticarse en la solución primero. Hay tres formas de autenticarse en Key Vault:

- **Identidades administradas de recursos de Azure**: cuando implementa una aplicación en una máquina virtual en Azure, puede asignar una identidad a la máquina virtual que tiene acceso a Key Vault. También puede asignar identidades a otros recursos de Azure . La ventaja de este enfoque es que la aplicación o el servicio no administran la rotación del primer secreto. Azure alterna automáticamente la identidad. Este enfoque es un procedimiento recomendado.
- **Entidad de servicio y certificado**: puede usar una entidad de servicio y un certificado asociado que tenga acceso a Key Vault. No se recomienda este enfoque porque el propietario o el desarrollador de la aplicación debe girar el certificado.
- **Entidad de servicio y secreto**: aunque puede usar una entidad de servicio y un secreto para autenticarse en Key Vault, no se recomienda que lo haga. Es difícil girar automáticamente el secreto de arranque que se utiliza para autenticarse en Key Vault.

### 〔Cifrado de datos en tránsito〕
Azure Key Vault aplica el protocolo Seguridad de la capa de transporte (TLS) para proteger los datos cuando viajan entre Azure Key Vault y los clientes. Los clientes negocian una conexión TLS con Azure Key Vault. TLS proporciona una autenticación sólida, privacidad de mensajes e integridad (lo que permite la detección de la manipulación, interceptación y falsificación de mensajes), interoperabilidad, flexibilidad de algoritmo, y facilidad de implementación y uso.

Confidencialidad directa total (PFS) protege las conexiones entre los sistemas cliente de los clientes y los servicios en la nube de Microsoft mediante claves únicas. Las conexiones también usan longitudes de clave de cifrado RSA de 2048 bits. Esta combinación hace difícil para un usuario interceptar y acceder a datos que están en tránsito.

### 〔Roles de Key Vault〕
Utilice la tabla siguiente para comprender mejor cómo Key Vault puede ayudar a satisfacer las necesidades de los programadores y de los administradores de seguridad.

|Rol|Declaración del problema|Resuelto por Azure Key Vault|
|:----|:----|:----|
|Desarrollador para una aplicación de Azure|Quiero escribir una aplicación para Azure que use claves para el cifrado y la firma. Pero quiero que estas claves sean externas a mi aplicación, de forma que la solución sea adecuada para aplicaciones distribuidas geográficamente. Quiero que tanto las claves como los secretos estén protegidos sin tener que escribir el código. Por último, quiero poder usar fácilmente las claves y los secretos desde mis aplicaciones, y que el rendimiento sea óptimo".|√ Las claves se almacenan en un almacén y las invoca un identificador URI cuando se necesitan. √ Las claves se protegen mediante Azure, para lo que se usan algoritmos estándar del sector, longitudes de clave y módulos de seguridad de hardware. √ Las claves se procesan en los HSM que residen en los mismos centros de datos de Azure que la aplicaciones. Este método proporciona mayor confiabilidad y menor latencia que las claves que se encuentran en una ubicación independiente, como por ejemplo si son locales.
Desarrollador para software como servicio (SaaS)|"No quiero asumir la responsabilidad, ni tampoco la posible responsabilidad, de las claves y los secretos de inquilino de mis clientes. Quiero que los clientes posean sus claves y las administren, de modo que yo pueda concentrarme en mi trabajo, que es proporcionar las características de software principales".|√ Los clientes pueden importar sus propias claves a Azure y administrarlas. Cuando una aplicación SaaS necesita realizar operaciones criptográficas mediante las claves de los clientes, Key Vault las realiza en nombre de la aplicación. La aplicación no ve las claves de los clientes.
Responsable principal de la seguridad (CSO)|"Quiero saber que nuestras aplicaciones cumplen con los HSM de FIPS 140-2 nivel 2 o FIPS 140-2 nivel 3 para la administración de claves segura. Deseo asegurarme de que mi organización tiene el control del ciclo de vida de las claves y puedo supervisar el uso de estas. Y aunque usamos varios servicios y recursos de Azure, quiero administrar las claves desde una ubicación única en Azure".|√ Elija **almacenes** para los HSM validados por FIPS 140-2 nivel 2.√ Elija **grupos HSM administrados** para los HSM validados por FIPS 140-2 nivel 3.√ Key Vault está diseñado de modo que Microsoft no pueda ver ni extraer sus claves.El uso de la clave √ se registra en tiempo casi real.√ El almacén proporciona una sola interfaz, independientemente del número de almacenes que tenga en Azure, las regiones que admitan y las aplicaciones que los usen.|

Cualquiera con una suscripción a Azure puede crear y usar instancias de Key Vault. Aunque Key Vault beneficia a los desarrolladores y los administradores de seguridad, el administrador de una organización que administra otros servicios de Azure puede implementarlo y administrarlo. Por ejemplo, este administrador puede iniciar sesión con una suscripción de Azure, crear un almacén para la organización en el que almacenar las claves y, después, asumir la responsabilidad de las tareas operativas, como:

- Crear o importar una clave o un secreto
- Revocar o eliminar una clave o un secreto
- Autorizar usuarios o aplicaciones para acceder al almacén de claves para que puedan administrar o usar sus claves y secretos
- Configurar el uso de claves (por ejemplo, para firmar o cifrar)
- Supervisar el uso de claves

A continuación, este administrador proporciona a los desarrolladores los URI para llamar desde sus aplicaciones. Este administrador también ofrece información de registro del uso de claves al administrador de seguridad.

![](https://docs.microsoft.com/es-es/azure/key-vault/media/key-vault-whatis/azurekeyvault_overview.png)

Los desarrolladores también pueden administrar las claves directamente mediante API.

--------------

# 【Practica 18: Seguridad en Azure〕
Para esta práctica no haremos tantas cosas complejas como crear recursos o manipular algo, esto es debido a que la mayor parte de seguridad de Azure es "automática", siempre a la vanguardia usando Inteligencia Artificial.

Por ende, solo mostraré como lucen dichos recursos en Azure y explicaré algunos aspectos básicos de ellos.

### 〔Microsoft Defender for Cloud〕
El *Defender for Cloud* es como nuestro "antivirus" de la nube. Si recuerdan bien como funcionan los antivirus, se quedan en segundo plano, analizando en tiempo real (la mayoría de las veces) cada acción que usted realice en la computadora. Al detectar algo malicioso o perjudicial, nos alertará de que algo está sucediendo, y dependiendo de la amenaza, el antivirus realizará medidas correctivas que nosotros le ajustemos.

Ahora, en Azure tenemos exactamente lo mismo, solo que éste servicio es solamente para recomendaciones de seguridad, por ejemplo, si tenemos una vulnerabilidad en algún recurso, nos dirá nuestras *medidas correctivas*.

1. En la barra de navegación, buscamos *Microsoft Defender for Cloud.

![](https://i.imgur.com/XMWJCJA.png)

2. Tendremos una interfaz como ésta. Debido a que éste servicio se encuentra en **Plan Standard** con algunas funciones limitadas. Se nos muestra a la derecha una tabla de precios por protección de cada recurso que nosotros podamos llegar a utilizar, y ese será el costo que nos cobrarán por protegerlo en el **Plan Premium**.

![](https://i.imgur.com/EEXYTmK.png)

3. Por ahora, haremos clic en *Omitir*.

4. Ahora, en el panel de información general, tenemos muchas cosas interesantes, tales como la cantidad de suscripciones que tengo, los recursos que hay creados (por categoría), y lo más importante, la **posición de seguridad**. La "posición de seguridad" es un valor estadístico que se toma en base de cuán seguro esta nuestra nube; esto se logra acatando las recomendaciones de seguridad, solucionando vulnerabilidades, y resolviendo los desperfectos de nuestros recursos.

![](https://i.imgur.com/buaxsBC.png)

5. El siguiente apartado es *Recomendaciones*, y como su nombre lo indica, son aquellas recomendaciones hechas por Azure para mejorar la seguridad de los recursos de nuestra nube (en caso de tenerlos creados).

![](https://i.imgur.com/RcF1vkO.png)

6. Al igual que en prácticas anteriores, tenemos *Alertas*, y estas son *Alertas de seguridad*. Podemos programar alertas para que nosotros estemos al tanto de lo que sucede en nuestra nube, si es vulnerada o algo no se encuentra bien.

![](https://i.imgur.com/KMXCYUr.png)

7. La sección se *Inventario*, es para aquellos recursos de otras nubes que no pertenecen a Azure. Se almacenan aquí y son manipuladas con la máxima protección que ofrece Azure.

![](https://i.imgur.com/UPYkWen.png)

8. Los *libros* se pueden interpretar como conjuntos de intrucciones usando inteligencia artificial y entrenadas con base de datos de vulnerabilidades, que puedan ser utilizados de forma automática en caso de un problema en la nube.

![](https://i.imgur.com/1XgIJx4.png)

9. La *comunidad* es una sección donde tenemos acceso a miles de repositorios creados para ayudarse entre si los numerosos programadores de la internet, con el fin de apoyarse a todos entre si siempre que sea necesario.

![](https://i.imgur.com/ffH3Kbi.png)

10. En la sección "Seguridad en la nube, tenemos el apartado *Cumplimiento normativo*. Esta herramienta sirve para verificar si nuestros sistemas cumplen con las normativas impuestas por los gobiernos de los paises del mundo. (En próximas prácticas profundizaremos en este tema)

![](https://i.imgur.com/93eHNpe.png)

11. Finalmente, tenemos el *Firewall Manager*, muy similar a Azure Firewall, pero éste se enfoca en la defensa de amenazas hacia los recursos y AF en la seguridad de red.

![](https://i.imgur.com/HQslwjA.png)

### 〔Azure Sentinel〕
Microsoft Azure Sentinel es un recurso muy eficaz para la detección y la automatización de amenazas. Es una solución nativa en la nube de gestión de eventos de información de seguridad (SIEM) y respuesta automatizada de orquestación de seguridad (SOAR) proporcionada por Microsoft para ayudarte mediante una visión de conjunto de un determinado proyecto.

1. Para crearlo, vamos a buscar *Sentinel* y clic en el primer resultado.

![](https://i.imgur.com/6anUyMb.png)

2. Clic en *Crear*.

![](https://i.imgur.com/TjYoexy.png)

3. Ahora, damos clic en *Crear un área de trabajo*.

![](https://i.imgur.com/2zLBCMi.png)

Para esta parte, necesitamos un servicio de **Log Analytics**, el cual será el encargado de recopilar toda la información de cada recurso creado o acción realizada en nuestra nube, para su posterior análisis.

4. Rellenamos los parámetros solicitados. Luego hacemos clic en *Revisar y crear*.

![](https://i.imgur.com/M1Mp65N.png)

5. Después, clic en *Crear*.

![](https://i.imgur.com/LgrtxVH.png)

6. Seleccionamos el área de trabajo, y luego damos al botón *Agregar*.

![](https://i.imgur.com/2mOXt97.png)

7. Una vez dentro del recurso, se nos habrá activado la versión Trial (de prueba) del Sentinel. Muy parecido al servicio anterior, podemos contratar la versión Premium.

![](https://i.imgur.com/ay2ZZAW.png)

8. En esta primera pestaña vemos un poco de información acerca de Sentinel.

![](https://i.imgur.com/N37J4im.png)

9. En el apartado de *Incidentes* se hace un conteo de los problemas que se han detectado mientras la nube estaba trabajando.

![](https://i.imgur.com/qmt0dz9.png)

10. Como ya se mencionó antes, los *libros* son conjuntos de intrucciones usando inteligencia artificial y entrenadas con base de datos de vulnerabilidades para resolver problemas.

![](https://i.imgur.com/557PHgg.png)

11. Use cuadernos en Sentinel para ampliar el ámbito de lo que puede hacer con los datos, por ejemplo, realizar análisis que no están integrados en Microsoft Azure Sentinel, como algunas características de aprendizaje automático de Python, crear visualizaciones de datos que no están integradas en Azure Sentinel, como escalas de tiempo personalizadas y árboles de proceso, o integrar orígenes de datos fuera de Azure Sentinel, como un conjunto de datos local.

![](https://i.imgur.com/KyMu6Ql.png)

12. En el apartado *MITRE ATT&CK*, tenemos un listado muy extenso de todos los posibles ataques que puede recibir nuestra nube. Esto ha sido validado por la empresa MITRE dedicada a la ciberseguridad.

![](https://i.imgur.com/LQc19Ob.png)

13. Podemos hacer clic en cualquiera y nos sale una pequeña descripción del problema. Pero igual podemos hacer clic en el hipervínculo y nos redirigirá a la página oficial de Mitre y su respectivo artículo sobre el problema que estamos investigando.

![](https://i.imgur.com/24IBYNx.png)
![](https://i.imgur.com/rI5JVcc.png)

14. También encontraremos Ejemplos y métodos de Mitigación.

![](https://i.imgur.com/elp5GVV.png)

### 〔Azure Key Vault〕
Por último, tenemos un servicio que nos sirve para almacenar claves, contraseñas y certificados, protegidos ante amenazas y que podemos usar en diferentes recursos de Azure.

1. Buscamos *Key Vault*, y hacemos clic en el primer resultado.

![](https://i.imgur.com/8NdhopH.png)

2. Hacemos clic en *Crear*.

![](https://i.imgur.com/9KBrQ7u.png)

3. Llenamos los datos solicitados, luego vamos a la pestaña *Directiva de acceso*.

![](https://i.imgur.com/YK8iunH.png)

4. Marcamos las tres opciones y dejamos lo demás por defecto.

![](https://i.imgur.com/gVstj1g.png)
![](https://i.imgur.com/x1M8ALt.png)

5. Hacemos clic en *Revisar y crear*.

![](https://i.imgur.com/ZuhTb9r.png)

6. Y nuevamente *Revisar y crear*.

![](https://i.imgur.com/xK7kehX.png)

7. Esperamos a que termine de implementarse. Damos clic en *Ir al recurso*

![](https://i.imgur.com/xEYaPFn.png)

Tenemos una interfaz como ésta donde nos aparece información general del recurso.

![](https://i.imgur.com/KFh5ex1.png)

8. Vamos a la sección *Configuración*, luego al apartado *Claves*. Hacemos clic en *Generar o importar*.

![](https://i.imgur.com/9Mb9U2r.png)

9. Le damos un nombre y lo configuramos como queramos. Después, damos clic en *Crear*.

![](https://i.imgur.com/R8ss0kH.png)

10. Hacemos clic en la *Clave*.

![](https://i.imgur.com/X1cQDmR.png)

11. Luego en el nombre largo con muchos carácteres.

![](https://i.imgur.com/ZkPrCZI.png)

12. Y aquí tenemos información detallada de nuestra clave y lo que contiene. Inclusive tenemos una URL para enlazarlo a otros recursos. (si así lo quisieramos)

![](https://i.imgur.com/WrAETqC.png)

13. De igual forma podemos crear *Secretos*, los cuales se podrían decir son nuestras "contraseñas".

14. Clic en *Generar o importar*.

![](https://i.imgur.com/wLIDO9G.png)

15. Y escribimos *nombre*, y el *valor* (que es nuestra contraseña).

![](https://i.imgur.com/A8K1t0B.png)

16. También podemos consultarlo cuando queramos.

![](https://i.imgur.com/ufg61O3.png)

![](https://i.imgur.com/WDFgoss.png)

![](https://i.imgur.com/0LGfAoK.png)

17. Por último, podemos crear certificados, que son claves más seguras y encriptadas, implementadas en nuestras aplicaciones. Estos los abarcaremos en otra práctica.

![](https://i.imgur.com/Qt3wYIT.png)