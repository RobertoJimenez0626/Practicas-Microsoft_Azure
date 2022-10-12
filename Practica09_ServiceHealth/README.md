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

 - [Introducción a Azure Service Health](#introducción-a-azure-service-health)
    - [Estado de Azure](#estado-de-azure)
    - [Service Health](#service-health)
    - [Resource Health](#resource-health)
- [Practica 9](#practica-9-creación-de-alertas-de-service-health)
    - [Creación de regla de alertas](#creación-de-regla-de-alertas)
    - [Creación de grupo de acciones](#creación-de-grupo-de-acciones)
    - [Ejemplo de alerta](#ejemplo-de-alerta)
    - [Creación de regla de alertas: continuación](#creación-de-regla-de-alertas-continuación)
    - [Categorías de Service Health](#categorías-de-service-health)

-------

# 【Introducción a Azure Service Health】

![](https://symbols.getvecta.com/stencil_31/32_health-monitoring.95e5cd35cf.jpg)

Azure ofrece un conjunto de experiencias para mantenerle informado sobre el estado de los recursos en la nube. Esta información incluye los problemas actuales y futuros como eventos que afectan al servicio, el mantenimiento planeado y otros cambios que pueden afectar a la disponibilidad.

*Azure Service Health* es una combinación de tres servicios independientes más pequeños.

### 〔Estado de Azure〕

*Estado de Azure* informa de las interrupciones de servicio en Azure en la página de estado de Azure . La página es una vista global del estado de todos los servicios y regiones de Azure. La página de estado es una buena referencia para incidentes con un impacto masivo, pero se recomienda encarecidamente a los usuarios de Azure actuales que aprovechan Azure Service Health para mantenerse informados sobre los incidentes y el mantenimiento de Azure.

### 〔Service Health〕

*Service Health* proporciona una vista personalizada del estado de los servicios y regiones de Azure que usa. Es el mejor lugar para buscar comunicaciones que afecten a los servicios relativas a interrupciones, actividades de mantenimiento planeado y otros avisos de mantenimiento, ya que tras la autenticación, Service Health conoce los servicios y recursos que usa en la actualidad. La mejor forma de usar Service Health es configurar sus alertas para que le envíen notificaciones a través de sus canales de comunicación preferidos cuando los problemas del servicio, el mantenimiento planeado u otros cambios puedan afectar a los servicios y regiones de Azure que utilice.

### 〔Resource Health〕

*Resource Health* proporciona información sobre el estado de los recursos en la nube individuales, como una instancia de máquina virtual concreta. Mediante Azure Monitor también puede configurar alertas que le notifiquen los cambios de disponibilidad de los recursos en la nube. Resource Health, junto con las notificaciones de Azure Monitor, le ayudarán a estar mejor informado acerca de la disponibilidad de los recursos minuto a minuto y a evaluar rápidamente si un problema se le puede achacar a usted o está relacionado con un evento de plataforma de Azure.

Conjuntamente, estas experiencias proporcionan una vista completa del estado de Azure con el nivel de detalle relevante.

> ⚠ **Nota**
Este servicio admite Azure Lighthouse, que permite a los proveedores de servicios iniciar sesión en su propio inquilino para administrar las suscripciones y los grupos de recursos que los clientes hayan delegado.

--------------

# 【Practica 9: Creación de alertas de Service Health〕
Ahora, es momento de entrar a ver los servicios que permiten administrar otros servicios. Esto puede interpretarse como el monitoreo de un recurso o un sistema entero de una gran empresa.

Primero que todo, empezaremos por mostrar el servicio que es capaz de detectar aquellas fallas de manera global a los servicios de Azure. Service Health hace un monitoreo dentro del propio Azure para verificar que problemas ocurrieron y que problemas ocurrirán, para mantener un control efectivo de los incidentes.

Con este servicio, seremos capaz de preveer el momento en que un servicio estará en conflicto, para que no repercuta de forma significativa en las operaciones de nuestros demás recursos o sistemas. Para ello, aprenderemos a crear alertas de Service Health para determinados servicios, tanto en ciertas regiones como a nivel global.

1. En la barra de navegación, buscamos *Service Health*.

![](https://i.imgur.com/4hflfou.png)

2. En primer plano, podemos observar el apartado principal del Service Health, un mapamundi donde se nos mostrarían los posibles servicios en falla (de haber alguno). Vemos que está configurado por *Suscripción*, *todas las regiones*, y *todos los servicios*, y nos arroja que *no se encontró ningún problema de servicio*.

![](https://i.imgur.com/PAwnjVI.png)

3. Nosotros podemos modificar que regiones queremos analizar en especifico.

![](https://i.imgur.com/xPqREaX.png)

4. Al igual que especificar que servicios son los que nos interesan saber si están fallando o no.

![](https://i.imgur.com/4F6KkbQ.png)


### 〔Creación de regla de alertas〕
Con Service Health, tenemos la posibilidad de que automaticamente Azure nos notifique cuando un servicio ha fallado (con sus respectivos datos, region, tiempo, etc); con el fin de que nosotros no tengamos que estar pendientes al 100% de Service Health en caso de falla.

1. Para eso, vamos a dar clic en el botón *Añadir alerta de Service Health*.

![](https://i.imgur.com/gT3UsEF.png)

2. Necesitamos especificar *Suscripción*, *Servicios* que estemos interesados en estar alertas cuando estos fallen, *Regiones* en donde queremos saber si fallan y el *Tipo de evento*.

![](https://i.imgur.com/yRNXIig.png)

3. En servicios, puse Máquinas virtuales. Me interesa ser notificado cuando las máquinas virtuales entren en falla.

4. Aunado a lo anterior, quiero saber si fallan a nivel Global.

![](https://i.imgur.com/tSMi80I.png)

5. Y por ultimo, saber que tipo de evento/problema fue, en este caso, puse todos los eventos posibles: *problema de servicio*, *mantenimiento planeado*, *avisos de estado* y *aviso de seguridad*.

![](https://i.imgur.com/GuDLDjW.png)

### 〔Creación de grupo de acciones〕
Después, necesitamos crear un movimiento o "acción" que se ejecutará en caso de que ocurra dicho incidente. Esta acción sería como un Trigger (visto en Functions y Logic Apps).

1. Damos clic en *Seleccionar grupos de acciones*.

![](https://i.imgur.com/UCQNtbX.png)

2. Cuando le demos, aparecerá una pestaña emergente a la derecha. Clic en *Crear grupo de acciones*.

![](https://i.imgur.com/Rnc12QH.png)

3. Esto es muy similar a crear un recursos cualquiera de Azure. Nos pide una *suscripción*, *un grupo de recursos* (lo creamos), y *un nombre para el grupo de acciones* (el segundo nombre se pone automaticamente).

![](https://i.imgur.com/Yixd820.png)

4. Una vez rellenado eso, vamos a la pestaña *Notificaciones*, elegimos el tipo de notificación, en mi caso **Correo electrónico**. Colocamos un nombre para la notificación: **Notificación de Falla**, y seleccionamos *editar*, para ajustar los parámetros de Correo, SMS o Notificación de Azure Mobile App.

![](https://i.imgur.com/MAiYVyq.png)

5. Como ya mencioné, quiero que me llegue una notificación a mi correo electrónico, por ende, habilito el *Correo electrónico* y relleno el campo con mi dirección de correo electrónico. Después, clic en *Aceptar*.

![](https://i.imgur.com/dxZkkl4.png)

Quiero hacer énfasis en esta pestaña, llamada *Acciones*. Aquí podemos realizar Triggers especiales que tienen la capacidad de interactuar con recursos de Azure. Por ejemplo, supongamos que un día el servicio de VM deja de funcionar, pudimos haber creado una *Acción* de tipo *Aplicación lógica*, para que una logic app realice una función/operación en consecuencia de la caída del servicio o de las máquinas virtuales de un sistema.

![](https://i.imgur.com/31fi6tO.png)

6. Clic en *Revisar y crear*.

7. Luego, clic en *Crear*.

![](https://i.imgur.com/7T5I8Bz.png)

### 〔Ejemplo de alerta〕
¿Cómo sabemos que nuestra notificación está bien configurada y esté funcionando en un caso real?¿Tendremos que esperar a que suceda un incidente?
Este tipo de cuestiones ya están contempladas, y tenemos la posibilidad de hacer una prueba de nuestra notificación.

1. Para realizar la prueba, hacemos clic al nombre de nuestro grupo de acciones.

![](https://i.imgur.com/VZyHzHT.png)

2. Nos llevará a una ventana como la siguiente. Clic en *Grupo de acciones de prueba (versión preliminar)*.

![](https://i.imgur.com/F4a2emV.png)

3. Elegir el tipo de ejemplo. En este caso, se eligió la *Alerta de estado del servicio*.

![](https://i.imgur.com/2TnhALF.png)

4. Pulsamos el botón *Test*.

![](https://i.imgur.com/mJNBeG1.png)

5. Esperamos a que termine la ejecución.

![](https://i.imgur.com/VYuDe2x.png)
![](https://i.imgur.com/9qcclzk.png)

6. Ahora, verificamos que en nuestro correo electrónico llegó una email como el que se mira a continuación.

![](https://i.imgur.com/x5jYDd0.png)

Con esto, queda claro que nuestra notificación funciona correctamente.

### 〔Creación de regla de alertas: continuación〕
Procederemos a terminar de llenar los últimos parámetros necesarios para crear la regla de alertas.

1. Le ponemos un nombre a la regla, en mi caso, le puse **NotificacionesServMV**, con la descripción correspondiente. Seguido de ello, le decimos que pertenezca al grupo de recursos que nosotros queramos, yo le puse el mismo grupo de recursos que ésta práctica.

![](https://i.imgur.com/S34OFA6.png)

2. Damos clic al botón *Crear regla de alertas*.

3. Y esperamos a que se termine de crear la regla, tal como vemos en los recuadros emergentes.

![](https://i.imgur.com/ZqWebQQ.png)
![](https://i.imgur.com/W3Oxyv1.png)

### 〔Categorías de Service Health〕
A continuación, haremos un breve repaso a las funciones de las categorías pertinentes al servicio *Service Health*.

![](https://i.imgur.com/2bPPsET.png)

- **Problemas de servicio**: Monitoreo de anomalías en los servicios de Azure, tanto local como global.

- **Mantenimiento planeado**: Todo aquel recurso cuyo calendario de mantenimiento esté controlado por Azure. Se notificará cuando cierto servicio vaya a ser utilizado con fines de actualización, revisión o suspensión.

- **Avisos de estado**: Problemas de seguridad, intermitencias de servicios y toda aquella anomalia que se produzca cuando los servicios de Azure estén trabajando al momento.

- **Avisos de seguridad**: Alertas de posibles infecciones, vulnerabilidades o ataques externos a servicios que se estén operando, usualmente conectados a la red o internet pública.

En *Historial de estado* tenemos un monitoreo general de todos aquellos recursos que hayan fallado en determinado tiempo. Sirve para saber todas las fallas que vayan ocurriendo en Azure y que la propia empresa nos dice que ocurrió y porqué ocurrió. Sirve para hacer seguimiendo en caso de que haya afectado algo de importancia en tus recursos.

En *Alertas de estado* podemos ver nuestras alertas creadas y que estén funcionando en ese momento, incluyendo toda la información que contiene.