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

 - [Introducción a Virtual Machines](#introducción-a-virtual-machines)
    - [¿Cuándo usar máquinas virtuales?](#¿cuándo-usar-máquinas-virtuales)
    - [¿Qué son los conjuntos de escalado de máquinas virtuales?](#¿qué-son-los-conjuntos-de-escalado-de-máquinas-virtuales)
    - [¿Qué es Azure Batch?](#¿qué-es-azure-batch)
- [Introducción a Virtual Network](#introducción-a-virtual-network)
    - [Aislamiento y segmentación](#aislamiento-y-segmentación)
    - [Comunicación con Internet](#comunicación-con-internet)
    - [Comunicación entre los recursos de Azure](#comunicación-entre-los-recursos-de-azure)
    - [Comunicación con recursos locales](#comunicación-con-recursos-locales)
    - [Conexión de redes virtuales](#conexión-de-redes-virtuales)
- [Practica 4](#practica-4-conexión-de-dos-vm-por-medio-de-redes-virtuales-y-subnets)
    - [Creación de las máquinas virtuales](#creación-de-las-máquinas-virtuales)
    - [Acceder a una VM](#acceder-a-una-vm)
    - [Verificación de conexión](#verificación-de-conexión)

-------

# 【Introducción a Virtual Machines】

![](https://connectoricons-prod.azureedge.net/releases/v1.0.1555/1.0.1555.2715/azurevm/icon.png)

Gracias a Azure Virtual Machines, puede crear y utilizar máquinas virtuales en la nube. Estas máquinas virtuales proporcionan una infraestructura como servicio (IaaS) en forma de un servidor virtualizado y se pueden usar de muchas formas. Al igual que sucede en un equipo físico, se puede personalizar todo el software que se ejecuta en la máquina virtual. Las máquinas virtuales son una opción ideal cuando se necesita lo siguiente:

- Control total sobre el sistema operativo (SO).
- Capacidad de ejecutar software personalizado.
- Usar configuraciones de hospedaje personalizadas.

Una máquina virtual de Azure le ofrece la flexibilidad de la virtualización sin necesidad de adquirir y mantener el hardware físico que ejecuta la máquina virtual. Todavía se necesita configurar, actualizar y mantener el software que se ejecuta en la máquina virtual.

Al seleccionar una imagen de máquina virtual preconfigurada, podrá crear y aprovisionar una máquina virtual en cuestión de minutos. La selección de una imagen es una de las decisiones más importantes que tomará cuando cree una máquina virtual. Estas plantillas ya incluyen un sistema operativo y, a menudo, otro software, como herramientas de desarrollo o entornos de hospedaje web.

Azure proporciona más de cien servicios que permiten hacer todo tipo de cosas: desde ejecutar las aplicaciones existentes en máquinas virtuales hasta explorar nuevos paradigmas de software, como bots inteligentes y realidad mixta.

Muchos equipos comienzan a explorar la nube mediante la migración de sus aplicaciones existentes a máquinas virtuales que se ejecutan en Azure. Si bien este es un buen comienzo, la nube es mucho más que "un lugar diferente donde ejecutar las máquinas virtuales".

Por ejemplo, Azure proporciona servicios de inteligencia artificial y aprendizaje automático que pueden comunicarse naturalmente con los usuarios mediante la vista, el oído y la voz. También facilita soluciones de almacenamiento que crecen dinámicamente para dar cabida a grandes cantidades de datos. Los servicios de Azure permiten soluciones que no son factibles sin la potencia de la nube.

## 〔¿Cuándo usar máquinas virtuales?〕
- **Durante las pruebas y el desarrollo.**
Las máquinas virtuales proporcionan una manera rápida y sencilla de crear distintas configuraciones de sistema operativo y de aplicación.
- **Al ejecutar aplicaciones en la nube.**
La capacidad de ejecutar determinadas aplicaciones en la nube pública, en lugar de crear una infraestructura tradicional para ejecutarlas, puede proporcionar importantes beneficios económicos. Por ejemplo, es posible que una aplicación necesite controlar las fluctuaciones en la demanda. 
- **A la hora de extender el centro de recursos a la nube.**
Una organización puede extender las capacidades de su propia red local mediante la creación de una red virtual en Azure y al agregar máquinas virtuales a esa red virtual. Las aplicaciones como SharePoint se pueden ejecutar en una máquina virtual de Azure en lugar de hacerlo de forma local.
- **Durante la recuperación ante desastres.**
Igual que con la ejecución de ciertos tipos de aplicaciones en la nube y con la ampliación de una red local a la nube, se puede obtener un ahorro considerable en costos mediante el uso de un enfoque basado en IaaS para la recuperación ante desastres. Si se produce un error en un centro de datos principal, puede crear máquinas virtuales que se ejecuten en Azure para ejecutar las aplicaciones críticas y, después, puede apagarlas cuando el centro de datos principal vuelva a estar operativo.

## 〔¿Qué son los conjuntos de escalado de máquinas virtuales?〕

![](https://www.kindpng.com/picc/m/27-271985_azure-virtual-machine-png-transparent-png.png)

Los conjuntos de escalado de máquinas virtuales permiten crear y administrar un grupo de máquinas virtuales idénticas, de carga equilibrada. Imagine que está ejecutando un sitio web que permite a los científicos cargar imágenes de astronomía que deben procesarse. Si ha duplicado la máquina virtual, normalmente necesitará configurar un servicio adicional para enrutar las solicitudes entre varias instancias del sitio web. Los conjuntos de escalado de máquinas virtuales pueden encargarse de ello.

Los conjuntos de escalado le permiten administrar, configurar y actualizar de forma centralizada un gran número de máquinas virtuales en cuestión de minutos para proporcionar aplicaciones altamente disponibles. El número de instancias de máquina virtual puede aumentar o disminuir automáticamente según la demanda, o de acuerdo con una programación definida. Con los conjuntos de escalado de máquinas virtuales, puede crear servicios a gran escala para áreas como proceso, macrodatos y cargas de trabajo de contenedor.

## 〔¿Qué es Azure Batch?〕

![](data:image/png;base64,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)

Azure Batch permite trabajo por lotes paralelos a gran escala y de informática de alto rendimiento (HPC) con la capacidad de escalar a decenas, cientos o miles de máquinas virtuales.

Cuando esté listo para ejecutar un trabajo, Batch:

- Iniciará un grupo de máquinas virtuales de proceso - de forma automática.
- Instalará aplicaciones y datos de almacenamiento provisional.
- Ejecutará trabajos con tantas tareas como tenga.
- Identificará errores.
- Reordenará la cola de trabajo.
- Reducirá verticalmente el grupo a medida que se complete el trabajo.

# 【Introducción a Virtual Network】

![](https://symbols.getvecta.com/stencil_27/99_virtual-network.e43fa52244.png)

Las redes virtuales de Azure permiten a los recursos de Azure, como las máquinas virtuales, las aplicaciones web y las bases de datos, comunicarse entre sí, con los usuarios de Internet y con los equipos cliente en el entorno local. Una red de Azure se puede considerar una extensión de la red local con recursos que vincula otros recursos de Azure.

Las redes virtuales de Azure proporcionan las importantes funcionalidades de red siguientes:

- Aislamiento y segmentación
- Comunicación con Internet
- Comunicación entre recursos de Azure
- Comunicación con los recursos locales
- Enrutamiento del tráfico de red
- Filtrado del tráfico de red
- Conexión de redes virtuales

## 〔Aislamiento y segmentación〕
La red virtual de Azure permite crear varias redes virtuales aisladas. Al configurar una red virtual, se define un espacio de direcciones IP privadas con intervalos de direcciones IP públicas o privadas. El intervalo IP público solo existe dentro de la red virtual y no es enrutable en Internet. Después, puede dividir ese espacio de direcciones IP en subredes y asignar parte del espacio de direcciones definido a cada subred con nombre.

En la resolución de nombres, puede usar el servicio de resolución de nombres integrado en Azure. También puede configurar la red virtual para que use un servidor DNS interno o externo.

## 〔Comunicación con Internet〕
Una máquina virtual en Azure se puede conectar a Internet de forma predeterminada. Puede habilitar las conexiones entrantes desde Internet mediante la asignación de una dirección IP pública a la máquina virtual o colocando la máquina virtual detrás de un equilibrador de carga público. Para la administración de la máquina virtual, puede conectarse a través de la CLI de Azure, el Protocolo de escritorio remoto o Secure Shell.

## 〔Comunicación entre los recursos de Azure〕
Le interesará habilitar los recursos de Azure para que se comuniquen entre sí de forma segura. Puede hacerlo de dos maneras:

- **Redes virtuales:** Las redes virtuales no solo pueden conectar máquinas virtuales, sino también otros recursos de Azure, como App Service Environment para Power Apps, Azure Kubernetes Service y conjuntos de escalado de máquinas virtuales de Azure.
- **Puntos de conexión de servicio:** Puede usar los puntos de conexión de servicio para conectarse a otros tipos de recursos de Azure, como cuentas de almacenamiento y bases de datos SQL de Azure. Este enfoque permite vincular varios recursos de Azure con las redes virtuales para mejorar la seguridad y proporcionar un enrutamiento óptimo entre los recursos.

## 〔Comunicación con recursos locales〕
Las redes virtuales de Azure permiten vincular entre sí los recursos del entorno local y dentro de la suscripción de Azure. De hecho, puede crear una red que abarque tanto el entorno local como el entorno en la nube. Existen tres mecanismos para lograr esta conectividad:

- **Redes privadas virtuales de punto a sitio:** El enfoque habitual para una conexión de red privada virtual (VPN) consiste en establecer la conexión con la red corporativa desde un equipo ajeno a la organización. En este caso, el equipo cliente inicia una conexión VPN cifrada para conectar ese equipo a la red virtual de Azure.
- **Redes virtuales privadas de sitio a sitio:** Una VPN de sitio a sitio vincula un dispositivo o puerta de enlace de VPN local con la puerta de enlace de VPN de Azure en una red virtual. De hecho, puede parecer que los dispositivos de Azure están en la red local. La conexión se cifra y funciona a través de Internet.
- **Azure ExpressRoute:** Para los entornos donde se necesita más ancho de banda e incluso mayores niveles de seguridad, Azure ExpressRoute es el mejor sistema. ExpressRoute proporciona una conectividad privada dedicada a Azure que no viaja por Internet. 

## 〔Conexión de redes virtuales〕
Puede vincular redes virtuales entre sí mediante el emparejamiento de red virtual. El emparejamiento permite que los recursos de cada red virtual se comuniquen entre sí. Estas redes virtuales pueden estar en regiones distintas, lo que permite crear una red global interconectada con Azure.

Las rutas definidas por el usuario (UDR) son una actualización significativa de las redes virtuales de Azure que permiten un mayor control sobre el flujo de tráfico de red. Este método permite a los administradores de red controlar las tablas de enrutamiento entre subredes dentro de una red virtual, así como entre redes virtuales.

![](https://docs.microsoft.com/es-mx/learn/azure-fundamentals/azure-networking-fundamentals/media/local-or-remote-gateway-in-peered-virual-network-21106a38.png)

--------------

# 【Practica 4: Conexión de dos VM por medio de Redes Virtuales y SubNets】
### 〔Creación de las máquinas virtuales〕
1. Dentro de nuestro Azure Portal, buscamos en la barra de navegación **Máquinas Virtuales** (o Virtual Machines), y seleccionamos la que se muestra en la imagen.

![](https://i.imgur.com/ehb8glv.png)

2. Nos redireccionará a la pestaña de recursos de Máquinas virtuales. Damos clic en **Crear**, y luego **Máquina virtual de Azure**

![](https://i.imgur.com/yQJMSdL.png)

3. Se nos presentarán las opciones de configuración de nuestra VM. (Es **importante** resaltar el mensaje en azul que nos dice que debido a nuestra suscripción, ciertas regiones no estarán disponibles para nuestro uso)

![](https://i.imgur.com/PxjzhSZ.png)

4. Ahora, empezamos a configurar.

5. Empezamos con lo básico que nos solicita un recurso. (Suscripción, grupo de recursos, nombre del recurso y región)

![](https://i.imgur.com/63YWGW0.png)

6. En mi caso, al grupo de recursos lo puse como **Practica4**. A la máquina virtual le asigné como **VM1-P4** (hay que tomar en cuanto que serán 2). Y debido a las limitaciones de región, tuve que optar por elegir **Australia Central**

7. Ahora, se nos pide opciones de disponibilidad y tipo de seguridad. Aquí lo dejamos por defecto.

8. En imagen, es muy importante elegir que vamos utilizar, si **Linux** o **Windows**. En mi caso elegí **Windows 10 Pro**.

9. Ligado a lo anterior, en el siguiente apartado llamado **Tamaño**, es necesario elegir el "plan" que usará nuestra VM. Dicho de otro modo, elegiremos que tanta potencia/recursos empleará la VM. Mientras más potencia, mayor será el costo.

![](https://i.imgur.com/PBoqiIV.png)

10. En **Cuenta de administrador**, nosotros asignaremos unos datos de identificación para poder acceder a la VM. Uno **nombre de usuario** y una **contraseña** son más que suficientes.

11. En **Puertos de entrada públicos** elegiremos **Permitir los puertos seleccionados**. Posterior a ello, seleccionamos el **RDP (3389)**; este es un protocolo de escritorio remoto, el cual nos permitirá conectarnos desde nuestra propia computadora a la VM.

12. En el final de la configuración de **Datos Básicos**, marcamos la siguiente opción, para confirmar el uso de la licencia de nuestro S.O. elegido.

![](https://i.imgur.com/PoG7f28.png)

13. Ahora, en el apartado **Redes**, verificamos la siguiente información. Dejando por defecto todo, excepto la sección *Grupo de seguridad de red de NIC*, el cual seleccionaremos **Ninguno**.

![](https://i.imgur.com/U5ktf3b.png)

14. Clic en **Revisar y Crear**. Una vez superada la validación, **Crear**

![](https://i.imgur.com/bvSXWt5.png)

15. Una vez termine de implementarse correctamente, procederemos a crear la segunda máquina virtual, tal como vimos en todos los pasos anteriores.

16. Una vez creados, vamos a nuestro grupo de recursos. Aquí debemos darnos cuenta de algo. Además de los diferentes elementos que se crearon para las VM, se nos creó dentro del grupo, un elemento llamado **Practica4_Darki-vnet** de tipo Red Virtual. Al crearse una máquina virtual, se nos creará por si mismo una red virtual de esa máquina virtual asignado al grupo de recursos correspondiente.

![](https://i.imgur.com/pgrSk3Z.png)

17. Como nosotros especificamos que nuestra VM2 fuese creada en el mismo grupo de recursos, Azure automaticamente le asignó la misma red virtual a ella. Con esto, no hizo falta crear una segunda red virtual para la VM2, y ambas estarían funcionando con la misma red virtual.

### 〔Acceder a una VM〕
1. De la imagen anterior. Vamos a entrar al recurso **VM1-P4**.

2. Después clic en **Conectar** > **RDP**.

![](https://i.imgur.com/5tRJizm.png)

3. Y damos clic en **Descargar archivo RDP**. (Será como un ejecutable que nos permitirá acceder a la VM)

![](https://i.imgur.com/eDLF2iW.png)

4. Una vez abierto, nos apareceran una serie de ventanas emergentes.

5. Clic en **Conectar**.

![](https://i.imgur.com/gDkN7XL.png)

6. Aquí nos solicitará las credenciales que asignamos al momento de crear la Máquina Virtual. Colocaremos esas mismas, y en **Aceptar**.

![](https://i.imgur.com/6LBsiL7.png)

7. Esta será una alerta de un error de certificado, pero no pasa nada, damos clic en **Si**.

![](https://i.imgur.com/IDsCtnn.png)

8. Como podemos apreciar, se nos abrió una "aplicación" en la que se nos muestra un nuevo Windows iniciando. A esto le podemos llamar **Escritorio Remoto**.

![](https://i.imgur.com/r9Ls4zF.png)

9. Una vez iniciado, nos pedirá establecer unas configuraciones. Dichas configuraciones se realizan cuando el Windows es instalado por primera vez y después de ajustarlas, no nos volverá a pedirlas nuevamente.

![](https://i.imgur.com/EXhbAtV.png)

10. Ahora si, disponemos de nuestra VM (o PC en la nube), para su utilización a gusto del consumidor.

![](https://i.imgur.com/DWISu6h.png)

> Esto lo realizaremos con la VM2 de igual forma.

### 〔Verificación de conexión〕
Para finalizar, queremos comprobar que ambas VM están conectadas a una misma red. Lo correcto sería usar el comando `ping` con la dirección IP de la máquina a la que quiere "pinguear" o "llamar".

Aquí podemos ver la lista de direcciones IP asignadas a las VM en nuestra Red Virtual.

![](https://i.imgur.com/NibzPd2.png)

Entonces, si estamos en la **máquina virtual 1**, y queremos llamar a la **VM2**, entonces deberíamos usar `10.0.0.5`; por el contrario, si estamos en **VM2**, y queremos llamar a **VM1**, usaremos `10.0.0.4`.

Pero tenemos un problema, y es que ambos firewall de las máquinas, nos impide que entren datos externos inclusive si estan en la misma Red virtual. Por ende, usaremos lo siguiente:

1. Dentro de las máquinas virtuales, abrimos **PowerShell** como *administrador*

2. Debemos crear una nueva regla a nuestro Firewall. Dicha regla queda de esta forma: 
`New-NetFirewallRule -DisplayName "Allow ICMPv4-In" -Protocol ICMPv4`

> El Protocolo de control de mensajes de Internet (ICMP) es un protocolo en la capa de red que utilizan los dispositivos de red para diagnosticar problemas de comunicación en la red. El ICMP se utiliza principalmente para determinar si los datos llegan o no a su destino a su debido tiempo.

![](https://i.imgur.com/1KcGSPu.png)
> Recuerda, se tiene que realizar en ambas VM.

3. Ahora, le estamos asignando a nuestra VM, que el firewall admitirá el protocolo de mensajes ICMPv4, exactamente el mismo que se usa durante el comando `ping`.

4. Finalmente, podemos realizar el ping en ambas VM tal como expliqué anteriormente. En esta captura podemos apreciar el proceso para la nueva regla de firewall.

![](https://i.imgur.com/ArheDZg.png)

5. Seguido de la regla, hacemos los respectivos pingueos, la VM1 a la VM2, y viceversa.

6. Podemos ver que se están recibiendo datos tanto de uno como de otro, y en ambos casos hubo un 0% de perdida de paquetes. 

Resumiendo, ambas VM están conectadas correctamente dentro de nuestra Red Virtual.