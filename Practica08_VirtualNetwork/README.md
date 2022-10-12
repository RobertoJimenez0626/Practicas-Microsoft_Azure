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

 - [Introducción a Azure Virtual Network](#introducción-a-azure-virtual-network)
    - [Razones para usar una red virtual de Azure](#razones-para-usar-una-red-virtual-de-azure)
        - [Comunicación con internet](#comunicación-con-internet)
        - [Comunicación entre recursos de Azure](#comunicación-entre-recursos-de-azure)
        - [Comunicación con recursos locales](#comunicación-con-recursos-locales)
        - [Filtrado del tráfico de red](#filtrado-del-tráfico-de-red)
        - [Enrutado del tráfico de red](#enrutado-del-tráfico-de-red)
        - [Integración de red virtual para los servicios de Azure](#integración-de-red-virtual-para-los-servicios-de-azure)
        - [Límites de Azure VNet](#límites-de-azure-vnet)
- [Practica 8](#practica-8-implementación-de-azure-virtual-network-y-conexión-de-dos-redes-virtuales)
    - [Creación de redes virtuales](#creación-de-redes-virtuales)
    - [Creación de máquinas virtuales](#creación-de-máquinas-virtuales)
    - [Uso de Azure Cloud Shell](#uso-de-azure-cloud-shell)
    - [Emparejando redes virtuales](#emparejando-redes-virtuales)
    - [Prueba de ping](#prueba-de-ping)

-------

# 【Introducción a Azure Virtual Network】

![](https://azure.microsoft.com/svghandler/virtual-network/?width=600&height=315)

*Azure Virtual Network* (VNet) es el bloque de creación fundamental de una red privada en Azure. VNet permite muchos tipos de recursos de Azure, como Azure Virtual Machines (máquinas virtuales), para comunicarse de forma segura entre usuarios, con Internet y con las redes locales. VNet es similar a una red tradicional que funcionaría en su propio centro de datos, pero aporta las ventajas adicionales de la infraestructura de Azure, como la escala, la disponibilidad y el aislamiento.

### 〔Razones para usar una red virtual de Azure〕
Una red virtual de Azure permite que los recursos de Azure se comuniquen de forma segura entre ellos, con Internet y con redes locales. Entre los escenarios clave que se pueden realizar con una red virtual se incluyen los siguientes: la comunicación de los recursos de Azure con Internet, la comunicación entre los recursos de Azure, la comunicación con los recursos locales, el filtrado del tráfico de red, el enrutamiento del tráfico de red y la integración con los servicios de Azure.

#### 〔Comunicación con internet〕
De manera predeterminada, todos los recursos de una red virtual tienen comunicación de salida hacia Internet. Para comunicarse con un recurso entrante, asígnele una dirección IP pública o un equilibrador de carga público. También puede usar la dirección IP pública o el equilibrador de carga público para administrar las conexiones salientes.

> ⚠ **Nota**
Cuando se usa solo una instancia interna de Standard Load Balancer, la conectividad de salida no está disponible hasta que define cómo desea que las conexiones salientes trabajen con una dirección IP pública o un equilibrador de carga público en el nivel de instancia.


#### 〔Comunicación entre recursos de Azure〕
Los recursos de Azure se comunican de manera segura entre sí de una de las maneras siguientes:

- Mediante una red virtual: tanto las máquinas virtuales como otros tipos de recursos de Azure se pueden implementar en una red virtual, como Azure App Service Environment, Azure Kubernetes Service (AKS) y Azure Virtual Machine Scale Sets.

- Mediante un punto de conexión de servicio de red virtual: extienda el espacio de direcciones privadas de la red virtual y la identidad de la red virtual a los recursos del servicio de Azure, como cuentas de Azure Storage y Azure SQL Database, mediante una conexión directa. Los puntos de conexión de los servicios permiten proteger los recursos críticos de los servicios de Azure únicamente en una red virtual.

- Mediante emparejamiento de VNet: Las redes virtuales se pueden conectar entre sí, lo que permite que los recursos de cualquiera de ellas se comuniquen entre sí mediante el emparejamiento de red virtual. Las redes virtuales que conecte pueden estar en la misma región de Azure o en regiones distintas.

#### 〔Comunicación con recursos locales〕
Puede conectar sus equipos y redes local a una red virtual mediante cualquier combinación de las siguientes opciones:

- Red privada virtual (VPN) de punto a sitio: se establece entre una red virtual y un equipo individual de la red. Cada equipo que desea establecer conectividad con una red virtual debe configurar su conexión. Este tipo de conexión es muy útil cuando se está comenzando con Azure, o para los desarrolladores, porque requiere poco o ningún cambio en la red existente. La comunicación entre el equipo y una red virtual se envía mediante un túnel cifrado a través de internet.

- VPN de sitio a sitio: se establece entre un dispositivo VPN local y una instancia de Azure VPN Gateway que está implementada en una red virtual. Este tipo de conexión permite que cualquier recurso local que autorice acceda a una red virtual. La comunicación entre un dispositivo VPN local y una puerta de enlace de VPN de Azure se envía mediante un túnel cifrado a través de internet.

- Azure ExpressRoute: se establece entre la red y Azure, mediante un asociado de ExpressRoute. Esta conexión es privada. El tráfico no pasa por Internet.

#### 〔Filtrado del tráfico de red〕
Puede filtrar el tráfico de red entre subredes mediante una o ambas de las siguientes opciones:

- Grupos de seguridad de red: los grupos de seguridad de red y los grupos de seguridad de aplicaciones pueden contener varias reglas de seguridad de entrada y salida que le permiten filtrar el tráfico que llega y sale de los recursos por dirección IP, puerto y protocolo de origen y destino.

- Aplicaciones virtuales de red: una aplicación de red virtual es una máquina virtual que ejecuta una función de red, como un firewall, la optimización de WAN u otra función de red.

#### 〔Enrutado del tráfico de red〕
De forma predeterminada Azure enruta el tráfico entre subredes, redes virtuales conectadas, redes locales e Internet. Puede implementar una o ambas de las siguientes opciones para reemplazar las rutas predeterminadas que crea Azure:

- Tablas de ruta: puede crear tablas de ruta personalizadas con las rutas que controlan a dónde se enruta el tráfico para cada subred.

- Rutas de Protocolo de puerta de enlace de borde (BGP) : si conecta la red virtual a su red local mediante una conexión de Azure VPN Gateway o ExpressRoute, puede propagar las rutas BGP locales a sus redes virtuales.

#### 〔Integración de red virtual para los servicios de Azure〕
La integración de servicios de Azure en una red virtual de Azure permite el acceso privado al servicio desde las máquinas virtuales o los recursos de proceso de la red virtual. Puede integrar los servicios de Azure en la red virtual con las siguientes opciones:

- Implementación de instancias dedicadas del servicio en una red virtual. Luego se puede acceder de forma privada a los servicios dentro de la red virtual y desde redes locales.

- Usando Private Link para acceder de forma privada a una instancia específica del servicio desde la red virtual y desde las redes locales.

- También puede acceder al servicio mediante puntos de conexión públicos si amplía una red virtual al servicio a través de los puntos de conexión de servicio. Los puntos de conexión de servicio permiten que los recursos de servicio se protejan en la red virtual.

#### 〔Límites de Azure VNet〕
Hay ciertos límites en torno al número de recursos de Azure que puede implementar. La mayoría de los límites de redes de Azure están en los valores máximos. Sin embargo, puede aumentar ciertos límites de red como se especifica en la [página de límites de red virtual](https://docs.microsoft.com/es-es/azure/azure-resource-manager/management/azure-subscription-service-limits#networking-limits).


--------------

# 【Practica 8: Implementación de Azure Virtual Network y conexión de dos Redes Virtuales〕
Empezamos de una forma diferente a como lo hemos hecho hasta ahora. Podemos crear nuestros grupos de recursos que utilizaremos para organizar los recursos, y luego, dichos recursos, asignarles el grupo al que pertenecerán.

1. Buscamos en el navegador, *Grupos de recursos*.

![](https://i.imgur.com/1feg44H.png)

2. Damos clic en *Crear*.

![](https://i.imgur.com/ls7Ri5p.png)

Los datos que requieren los grupos de recursos son más sencillos que los recursos en si, debido a que debemos entenderlos como "carpetas" u "organizadores", solo sirven para eso y no requieren algo tan especifico, a excepción de la *Región*.

3. Rellenamos la información *Suscripción*, *Grupo de recursos* (aunque suene redundante, pero este es el nombre que recibirá el grupo de recursos) y lo más importante, la *Región*.

![](https://i.imgur.com/gkPyK0U.png)

4. Después, clic en *Revisar y crear*.

5. Azure validará los parámetros, y seguido de ello, damos clic en *Crear*.

![](https://i.imgur.com/ZZXxBl6.png)

Ahora tenemos creado nuestro grupo de recursos llamado: **Practica8_Darki**. Este grupo será empleado en esta práctica.

![](https://i.imgur.com/PcYtFyK.png)

### 〔Creación de redes virtuales〕
Procedemos a crear unas redes virtuales, las cuales serán emparejadas para hacer un `ping` (por medio de Máquinas Virtuales) y verificar que ambas están en correcta comunicación.

1. Buscamos en el navegador *Redes Virtuales*.

![](https://i.imgur.com/eIoFeBH.png)

2. Damos clic en el botón *Crear*.

![](https://i.imgur.com/klLJSih.png)

3. En la pestaña de creación, como siempre, especificamos los datos correspondientes. En este caso, como vimos antes, ya tenemos creado un grupo de recursos especifico para ésta practica, llamado **Practica8_Darki**.

![](https://i.imgur.com/PFxYFvO.png)
> Algo importante a tener en cuenta. Cuando nosotros creamos nuestro grupo de recursos, usamos *UK South*; como nosotros asignamos este recurso a dicho grupo, automaticamente se le asignó la misma región utilizada en el grupo. Por ende, podemos decir que: *todos los elementos creados dentro del grupo de recursos, heredarán características propias del grupo*. (En este caso, la región)

4. Vamos a la pestaña *Direcciones IP*. Aquí encontraremos características relacionadas al espacio de direcciones de la red virtual. Pero aquí debemos crear una subred dentro de la red, esto usualmente se usa para organizar los elementos en pequeños espacios de red para cada cosa.

![](https://i.imgur.com/cEimLrt.png)

5. Seleccionamos la subred *default*, y le damos en *Quitar la subred*.

6. Ahora agregaremos una propia. Clic en *Agregar subred*, y rellenamos los parámetros que pide, en este caso, *Nombre de subred* y el *intervalo de direcciones*. Después en *Agregar*.

![](https://i.imgur.com/XLOzxP3.png)

7. Luego, *Revisar y crear*.

8. Esperamos la validación y luego en *Crear*.

![](https://i.imgur.com/3E3AdJ1.png)

9. Y para finalizar, esperamos que la implementación se termine.

![](https://i.imgur.com/RvoKddn.png)

Como usaremos dos máquinas virtuales, tenemos que crear dos redes virtuales. La creamos como la que acabamos de hacer, solo que con otro nombre, tanto *la Red* y *la Subred*.

![](https://i.imgur.com/m3YNYP6.png)
![](https://i.imgur.com/ulwxwQk.png)

### 〔Creación de máquinas virtuales〕
Como se mencionó antes, usaremos las redes virtuales para conectar dos máquinas virtuales y poder realizar el `ping` de ambas redes.
Entonces, procederemos a crear las máquinas virtuales, y en esta ocasión usaremos **Linux**.

1. Buscamos en el navegador, *Máquinas Virtuales*.

![](https://i.imgur.com/dsfBPrH.png)

2. Pulsamos en *Crear*, y seleccionamos *Máquina virtual de Azure*.

![](https://i.imgur.com/K7NQlfa.png)

3. Rellenamos los campos necesarios.

![](https://i.imgur.com/cLcKfSX.png)

> IMPORTANTE: Es necesario utilizar la misma *Región* que fue establecida en las redes virtuales para que podamos usarlas en nuestras máquinas virtuales, de lo contrario, no serán reconocidas por ellas.

4. En *Imagen*, elegiremos *Ubuntu*, ya que usaremos Linux, y en *tamaño* seleccionamos *el más barato*.

5. En *Cuenta de administrador*, para el *tipo de autenticación*, marcamos *Contraseña*. Seguido de ello, rellenamos *usuario* y *contraseña* que usaremos. (Esto nos servirá más adelante)

![](https://i.imgur.com/6qAsZgi.png)

6. Dejamos lo demás por defecto.

![](https://i.imgur.com/N5KNrF5.png)

7. En la pestaña *Redes*, vamos a configurar que red usará nuestra máquina virtual, y para ello, desplegamos la lista de redes disponibles. Automaticamente detectará aquellas redes que Azure tenga a su disposición (en caso de no existir, creará una propia). Evidentemente, seleccionaremos la red 1 que creamos, junto con la subred 1.

8. Dejamos todo lo demás por defecto, y hacemos clic en *Revisar y crear*.

![](https://i.imgur.com/kxrr9xK.png)

9. Esperamos a que se complete la validación, y luego damos en *Crear*.

![](https://i.imgur.com/XVlcEMx.png)

Aquí nos sale un mensaje emergente para *Generar un par de claves*. No usaremos nada de esto en la práctica, así que podemos omitirlo.

![](https://i.imgur.com/kxixlVM.png)

10. Y esperamos a que se termine de crear el recurso.

![](https://i.imgur.com/7k7Zqyl.png)

Una vez creada la primera máquina virtual, creamos la segunda de la misma forma, con la diferencia que usaremos *otro nombre* y en lugar de elegir la *red virtual 1*, elegiremos la *red virtual 2*.

![](https://i.imgur.com/NU5N7ZY.png)
![](https://i.imgur.com/RkyrUbO.png)
![](https://i.imgur.com/T0K8eAa.png)

### 〔Uso de Azure Cloud Shell〕
En este tema, usaremos una nueva herramienta que nos proporciona Azure. Si bien, vemos que es posible crear recursos/elementos de forma práctica y visual, también tenemos la posibilidad de crearlos usando código o programación.

Para dicho caso, se nos proporciona una herramienta llamanda *Azure Cloud Shell*, que en términos generales, es una ventana de linea de comandos, en la cual podemos dar órdenes a Azure para que ejecute lo que nosotros queramos. En prácticas posteriores veremos un ejemplo de cómo realizarlo.

Por el momento, nos interesa conectarnos a nuestras máquinas virtuales, pero, a diferencia de Windows que usamos un *Escritorio Remoto*, aquí usaremos unicamente lineas de comando.

1. Primero, nos vamos a una máquina virtual y damos clic en *Conectar* y seleccionamos *SSH*.

![](https://i.imgur.com/x5hdNK6.png)

2. Veremos una pestaña como ésta. Lo que nos interesa de aquí es lo señalado en color Azul, ya que son los datos de ingreso a nuestra máquina.

![](https://i.imgur.com/BJTpUKQ.png)

3. Ahora, posicionamos el puntero del ratón en el *primer ícono* a la *derecha* de la *barra de búsqueda de Azure*, el que parece una ventanita de comandos.

4. Una vez hecho, veremos que dentro de la propia ventana del navegador, se nos despliega una ventana extra; esto es Azure Cloud Shell.

![](https://i.imgur.com/V3R2KRQ.png)

> Podemos elegir si queremos usar Bash o Powershell, esto queda a elección del operador.

5. Lo primordial en Cloud Shell, es que debemos tener una cuenta de almacenamiento para que pueda empezar a funcionar. Si nosotros tenemos una creada, podemos elegirla, en caso contrario, podemos crearla directamente haciendo clic en el botón *Crear almacenamiento*, siempre eligiendo la suscripción que estamos usando.

![](https://i.imgur.com/ozapsF2.png)

6. Ahora, podemos observar que la ventana se convirtió en una consola de comandos. Con los conocimientos correctos, podemos realizar exactamente lo mismo que Azure Portal, pero mediante lineas de código.

![](https://i.imgur.com/NHfLOXx.png)

7. Ejecutamos el siguiente comando: `ssh` *seguido de lo que copiamos previamente* (tal como se muestra en la imagen).

8. Y nos pedirá validar la autenticación con nuestra contraseña que asignamos anteriormente.

![](https://i.imgur.com/dl1AsyS.png)

Sabremos que nos conectamos correctamente cuando no se nos muestre un mensaje de error de autenticación y el texto verde haya cambiado a ***usuario@nombreVM***.

![](https://i.imgur.com/bXDLrGq.png)

9. Hacemos un testeo rápido con el comando: `sudo apt-get moo`.

![](https://i.imgur.com/Enzqabn.png)

Si todo salió bien, debería salirnos una vaca como la que se muestra en la imagen.

### 〔Emparejando redes virtuales〕
Es importante darnos cuenta de una cosa, *no importa si las dos redes virtuales están en el mismo grupo de recursos, si nosotros no las emparejamos, ellas no interactúan entre si (como si se desconocieran)*.

Nuestro cometido en este tema, es conectarlas y que ambas puedan interactuar.

1. Abrimos cualquiera de nuestras redes virtuales, nos dirigimos al apartado de *Emparejamientos*, y damos clic en *Agregar*.

![](https://i.imgur.com/gA33Bv6.png)

2. Nos mostrará la siguiente ventana, y debemos rellenar los valores que nos solicita, en este caso, un *nombre para el vínculo de emparejamiento*. Para fines prácticos, podemos poner de nombre de esta forma: ***redTransmisora-redReceptora*** o como yo lo puse ***RedVirtual1-RedVirtual2***.

![](https://i.imgur.com/wLfSKeQ.png)

3. Dejamos lo demás por defecto.

4. Tal como la anterior, pero con la diferencia de que ahora configuramos la parte inversa, en lugar de actuar como **redTransmisora**, será una **redReceptora**. En otras palabras, podemos escribir el nombre pero al revés: ***RedVirtual2-RedVirtual1***.

![](https://i.imgur.com/sQWOUTw.png)

5. Especificamos que nuestra red remota es **RedVirtual2**.

6. Dejamos lo demás por defecto.

![](https://i.imgur.com/d83U8gE.png)

7. Damos clic en *Agregar* y esperamos a que haga el proceso de validación.

![](https://i.imgur.com/bRETQMQ.png)

Al final, en la pestaña de *Emparejamientos* debemos tener algo parecido a esto. Y debe indicar que está *Conectado*.

![](https://i.imgur.com/lsS7qy7.png)

### 〔Prueba de ping〕
Como vimos antes, trabajamos con el emparejamiento de la **Red Virtual 1** hacia la **Red Virtual 2**. Esto es importante para lo siguiente; significa que usaremos la red 1 para mandar señales a la red 2.

¿Como lo haremos?

1. Primero, iremos a las configuraciones de la *red virtual 2*, en *Dispositivos conectados*, y obtendremos el valor que hay en la columna *Dirección IP*. Copiamos ese valor.

![](https://i.imgur.com/leaI7IC.png)

2. Ahora, volvemos a abrir el Cloud Shell. Recordemos que nuestro CLI está conectado a nuestra VM1 que usa la *red virtual 1*, por ende, podemos decir que, usaremos esta máquina para mandarle un pingeo a la segunda máquina a través de las redes virtuales ya emperejadas (VM 1 -> VM2 / VNet1 -> VNet2).

3. Usamos el comando `ping`, pegamos la dirección IP que copiamos previamente, y pulsamos `Enter`.

![](https://i.imgur.com/jU0OsX7.png)

4. Si todo salió bien, debemos tener una pantalla como la que vemos en la imagen, dando a entender que los paquetes de información están siendo transmitidos de la *red 1* a la *red 2* correctamente. En caso contrario, el pingeo no mostraría ningún resultado, dando a entender que falló la conexión de dichas redes.

![](https://i.imgur.com/xDBMBC9.png)