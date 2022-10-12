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

- [Introducción a Grupos de Seguridad de Red](#introducción-a-grupos-de-seguridad-de-red)
    - [Reglas de seguridad](#reglas-de-seguridad)
    - [Reglas de seguridad predeterminadas](#reglas-de-seguridad-predeterminadas)
        - [Entrada](#entrada)
        - [Salida](#salida)
    - [Reglas de seguridad aumentada](#reglas-de-seguridad-aumentada)
    - [Etiquetas de servicio](#etiquetas-de-servicio)
    - [Grupos de seguridad de aplicaciones](#grupos-de-seguridad-de-aplicaciones)
- [Practica 19](#practica-19-uso-de-los-grupos-de-seguridad-de-red)
    - [Creando una máquina virtual](#creando-una-máquina-virtual)
    - [Creando y configurando el grupo de seguridad de red](#creando-y-configurando-el-grupo-de-seguridad-de-red)
    - [Añadiendo reglas de entrada](#añadiendo-reglas-de-entrada)
    - [Añadiendo reglas de salida](#añadiendo-reglas-de-salida)

-------

# 【Introducción a Grupos de Seguridad de Red】

![](https://songer812039438.files.wordpress.com/2019/09/network-security-group_color.png?w=300)

Puede usar el *grupo de seguridad de red* de Azure para filtrar el tráfico de red hacia y desde los recursos de Azure de una red virtual de Azure. Un grupo de seguridad de red contiene reglas de seguridad que permiten o deniegan el tráfico de red entrante o el tráfico de red saliente de varios tipos de recursos de Azure. Para cada regla, puede especificar un origen y destino, un puerto y un protocolo.

### 〔Reglas de seguridad〕
Un grupo de seguridad de red puede contener cero reglas, o tantas reglas como desee, siempre que esté dentro de los límites de la suscripción de Azure. Cada regla especifica las siguientes propiedades:

| Propiedad | Explicación |
| - | - |
| Nombre | Un nombre único dentro del grupo de seguridad de red. |
| Priority | Un número entre 100 y 4096. Las reglas se procesan en orden de prioridad. Se procesan primero las reglas con los números más bajos ya que estos tienen más prioridad. Si el tráfico coincide con una regla, se detiene el procesamiento. Como resultado, las reglas con menor prioridad (números más altos) que tengan los mismos atributos que las reglas con una prioridad mayor no se procesarán. |
| Origen o destino | Cualquiera, una dirección IP individual, un bloque CIDR de enrutamiento entre dominios sin clases (10.0.0.0/24, por ejemplo), una etiqueta de servicio o un grupo de seguridad de aplicaciones. Si especifica una dirección para un recurso de Azure, especifique la dirección IP privada asignada al recurso. Las grupos de seguridad de red se procesan después de que Azure traduzca una dirección IP pública a una dirección IP privada para el tráfico de entrada y antes de que Azure traduzca una dirección IP privada a una dirección IP pública para el tráfico de salida. Se necesitan menos reglas de seguridad cuando se especifica un intervalo, una etiqueta de servicio o un grupo de seguridad de aplicaciones. La posibilidad de especificar varias direcciones IP individuales e intervalos (no puede especificar varias etiquetas de servicio ni grupos de aplicaciones) en una regla se conoce como reglas de seguridad aumentada. Las reglas de seguridad aumentada solo se pueden generar en los grupos de seguridad de red creados mediante el modelo de implementación de Resource Manager. No puede especificar varias direcciones IP ni intervalos de ellas en grupos de seguridad de red creados mediante el modelo de implementación clásica. |
| Protocolo | TCP, UDP, ICMP, ESP, AH o cualquiera. |
| Dirección | Si la regla se aplica al tráfico entrante o al saliente. |
| Intervalo de puertos | Puede especificar un puerto individual o un intervalo de puertos. Por ejemplo, puede especificar 80 o 10000-10005. La especificación de intervalos le permite crear menos reglas de seguridad. Las reglas de seguridad aumentada solo se pueden generar en los grupos de seguridad de red creados mediante el modelo de implementación de Resource Manager. No puede especificar varios puertos ni intervalos de ellos en la misma regla de seguridad de los grupos de seguridad de red creados mediante el modelo de implementación clásica. |
| Acción | Permitir o denegar. |

Las reglas de seguridad se evalúan y aplican en función de la información de cinco tuplas (origen, puerto de origen, destino, puerto de destino y protocolo). No puede crear dos reglas de seguridad con la misma prioridad y dirección. Se crea un registro de flujo para las conexiones existentes. Se permite o deniega la comunicación en función del estado de conexión del registro de flujo. El registro de flujo permite que un grupo de seguridad de red sea con estado. Por ejemplo, si especifica una regla de seguridad de salida para cualquier dirección a través del puerto 80, no será necesario especificar una regla de seguridad de entrada para la respuesta al tráfico saliente. Solo debe especificar una regla de seguridad de entrada si la comunicación se inicia de forma externa. Lo contrario también es cierto. Si se permite el tráfico entrante a través de un puerto, no es necesario especificar una regla de seguridad de salida para responder al tráfico a través del puerto.

No es posible interrumpir las conexiones existentes cuando se elimina una regla de seguridad que habilitó el flujo. Los flujos de tráfico se interrumpen cuando se detienen las conexiones y no fluye ningún tráfico en ambas direcciones durante al menos unos minutos.

Hay límites en el número de reglas de seguridad que puede crear en un grupo de seguridad de red.

### 〔Reglas de seguridad predeterminadas〕
Azure crea las siguientes reglas predeterminadas en cada grupo de seguridad de red que cree:

#### 〔Entrada〕

**AllowVNetInBound**

| Priority | Source | Puertos de origen	| Destination | Puertos de destino | Protocolo | Acceso |
| - | - | - | - | - | - | - |
| 65000 | VirtualNetwork | 0-65535 | VirtualNetwork | 0-65535 | Any | Allow |

**AllowAzureLoadBalancerInBound**

| Priority | Source | Puertos de origen	| Destination | Puertos de destino | Protocolo | Acceso |
| - | - | - | - | - | - | - |
| 65001 | AzureLoadBalancer | 0-65535 | 0.0.0.0/0 | 0-65535 | Any | Allow |

**DenyAllInbound**

| Priority | Source | Puertos de origen	| Destination | Puertos de destino | Protocolo | Acceso |
| - | - | - | - | - | - | - |
| 65500 | 0.0.0.0/0 | 0-65535 | 0.0.0.0/0 | 0-65535 | Any | Denegar |

#### 〔Salida〕

**AllowVnetOutBound**

| Priority | Source | Puertos de origen	| Destination | Puertos de destino | Protocolo | Acceso |
| - | - | - | - | - | - | - |
| 65000 | VirtualNetwork | 0-65535 | VirtualNetwork | 0-65535 | Any | Allow |

**AllowInternetOutBound**

| Priority | Source | Puertos de origen	| Destination | Puertos de destino | Protocolo | Acceso |
| - | - | - | - | - | - | - |
| 65001 | 0.0.0.0/0 | 0-65535 | Internet | 0-65535 | Any | Allow |

**DenyAllOutBound**

| Priority | Source | Puertos de origen	| Destination | Puertos de destino | Protocolo | Acceso |
| - | - | - | - | - | - | - |
| 65500 | 0.0.0.0/0 | 0-65535 | 0.0.0.0/0 | 0-65535 | Any | Denegar |

En las columnas **Origen** y **Destino**, *VirtualNetwork*, *AzureLoadBalancer* e *Internet* son etiquetas de servicios, en lugar de direcciones IP. En la columna de protocolos, **Cualquiera** abarca TCP, UDP e ICMP. Al crear una regla, puede especificar TCP, UDP, ICMP o Cualquiera. *0.0.0.0/0* en las columnas **Origen** y **Destino** representa todas las direcciones. Los clientes, como Azure Portal, la CLI de Azure o PowerShell, pueden usar * o any en esta expresión.

Las reglas predeterminadas no se pueden quitar, pero puede reemplazarlas con reglas de prioridad más alta.

### 〔Reglas de seguridad aumentada〕
Las reglas de seguridad aumentada permiten simplificar la definición de seguridad para las redes virtuales, lo que le permitirá definir directivas de seguridad de red más grandes y complejas, con menos reglas. Puede combinar varios puertos y varias direcciones IP explícitas e intervalos en una única regla de seguridad de fácil comprensión. Use reglas aumentadas en los campos de origen, destino y puerto de una regla. Para simplificar el mantenimiento de la definición de la regla de seguridad, combine las reglas de seguridad aumentada con etiquetas de servicio o grupos de seguridad de aplicaciones. Hay límites en el número de direcciones, intervalos y puertos que se pueden especificar en una regla.

### 〔Etiquetas de servicio〕
Una etiqueta de servicio representa un grupo de prefijos de direcciones IP de un servicio de Azure determinado. Ayuda a minimizar la complejidad de las actualizaciones frecuentes de las reglas de seguridad de red.

### 〔Grupos de seguridad de aplicaciones〕
Los grupos de seguridad de aplicaciones le permiten configurar la seguridad de red como una extensión natural de la estructura de una aplicación, lo que le permite agrupar máquinas virtuales y directivas de seguridad de red basadas en esos grupos. Puede reutilizar la directiva de seguridad a escala sin mantenimiento manual de direcciones IP explícitas.

--------------

# 【Practica 19: Uso de los Grupos de seguridad de red〕
En esta práctica vamos a interactuar con las opciones de los grupos de seguridad de red, creando una máquina virtual y permitiendo la conexión a escritorio remoto y negando el acceso a internet.

### 〔Creando una máquina virtual〕
Empezaremos creando la máquina virtual.

1. Vamos a buscar *Máquinas virtuales*. 

![](https://i.imgur.com/fkvKk2w.png)

2. Damos clic en *Crear* y seleccionamos *Máquina virtual de Azure*.

![](https://i.imgur.com/VUAnTlv.png)

3. Llenamos los datos que nos pide: *suscripción*, *grupo de recursos*, *nombre* y *región*. En este caso no usaremos redundancia de zona y la seguridad será de tipo *Standard*.

![](https://i.imgur.com/alxtasO.png)

4. En imagen, usaré *Windows 10 Pro*, en el tamaño más pequeño. Ponemos un usuario y una contraseña.

![](https://i.imgur.com/9TA4pNh.png)

5. Después, en *puertos de entrada públicos*, seleccionamos *Ninguno*. Seguido de eso, seleccionamos el acuerdo de licencia.

![](https://i.imgur.com/ZRn4pe2.png)

6. En el apartado de *Redes*, vamos a dejar todo por defecto, excepto *Grupo de seguridad de red de NIC*, seleccionaremos *Ninguno*. (Por defecto, los recursos que se conecten a una red virtual vienen con un GSR predeterminado)

![](https://i.imgur.com/12gxLrK.png)

7. En *Administración*, *Supervisión*, vamos a seleccionar *Deshabilitar*.

![](https://i.imgur.com/a3utieh.png)

8. Después, clic en *Revisar y crear*.

![](https://i.imgur.com/0iQf66N.png)

9. Luego en *Crear*.

![](https://i.imgur.com/Tp417NJ.png)

10. Esperamos a que termine de implementarse, y luego damos clic al botón *Ir al recurso*.

![](https://i.imgur.com/FT38nYN.png)

### 〔Creando y configurando el grupo de seguridad de red〕
Como vimos anteriormente, nosotros especificamos que nuestra VM no tuviese un grupo de seguridad de red. Esto se ve reflejado en que al momento de que intentos conectarnos a nuestra máquina, no podremos establecer conexión, debido a que no existen los puertos de conexión válidos para que podamos usarla.

![](https://i.imgur.com/s3enNIq.png)

1. Una vez dentro, vamos a *Redes*. Podemos ver que nos dice que no existen Reglas de puerto de entrada. (Esto es lo que necesitamos para poder establecer conexión, y como no hay, no podamos conectarnos)

![](https://i.imgur.com/feutWkP.png)

2. En el buscador, escribimos *grupos de seguridad de red*, y abrimos el que no dice "clasico".

![](https://i.imgur.com/L0YNwvS.png)

3. Damos clic en *Crear*.

![](https://i.imgur.com/I1JCc3k.png)

4. Acompletamos los campos necesarios.

![](https://i.imgur.com/UVRUGOD.png)

5. Clic en *Revisar y crear*. Y por último en *Crear*.

![](https://i.imgur.com/mGPtLHw.png)

6. Clic en *Ir al recurso*.

![](https://i.imgur.com/gZeJdLt.png)

Esta es la interfaz del Grupo de seguridad de red. Si desplazamos el scroll, podemos ver una lista de reglas predefinidas que podemos empezar a usar.

![](https://i.imgur.com/IsoZp3H.png)
![](https://i.imgur.com/R6koRPS.png)

7. Vamos al apartado *Interfaces de red*. Hacemos clic en *Asociar*.

![](https://i.imgur.com/rc6gf1u.png)

8. Se nos mostrará una pestaña a la derecha. Debemos seleccionar nuestra Interfaz de Red de nuestra Máquina virtual.

![](https://i.imgur.com/i15rDqi.png)

9. Damos clic en *Aceptar*.

![](https://i.imgur.com/XgvAi9Y.png)
![](https://i.imgur.com/b4skqSz.png)

Ahora, intentemos conectarnos a nuestra máquina virtual con el *escritorio remoto*.

10. Vamos a *Conectar*. Y descargamos el RDP.

![](https://i.imgur.com/O0FoTRM.png)

11. Lo ejecutamos y damos clic al botón *Conectar*.

![](https://i.imgur.com/y8yUIjo.png)

12. Esperamos a que cargue.

![](https://i.imgur.com/N7AYwM4.png)

13. Nos marca un error de conexión. Esto se debe a que, aunque hayamos asociar el GSR a nuestra Interfaz de Red, no hemos habilitado los puertos para establecer una conexión.

![](https://i.imgur.com/scOh8XX.png)

### 〔Añadiendo reglas de entrada〕
Vamos a hacer que podamos conectarnos, y para eso, habilitaremos el puerto de conexión del RDP. (Puerto 3389)

1. Volviendo al recurso GSR, vamos al apartado *Configuración* y en *Reglas de seguridad de entrada*.

![](https://i.imgur.com/Cvn4jtH.png)

2. Clic al botón *Agregar*.

![](https://i.imgur.com/pgtrLcZ.png)

3. Se nos desplegará un menú a la derecha, el cual debemos configurar con las opciones necesarias.

4. *Origen*, *Intervalos de puertos de origen* y *Destino* los dejaremos por defecto. *Servicio* debe ser del tipo *Custom* y en *Intervalos de puertos de destino* pondremos el puerto que queremos habilitar (3389).

![](https://i.imgur.com/fKqB0fb.png)

5. Para el *Protocolo*, seleccionaremos *TCP*. En *Acción* usaremos *Permitir*. Ajustaremos una *Prioridad* de 300 (la prioridad es más mientras menor sea el número comenzando en 100). Por último, le ponemos el nombre que queramos.

![](https://i.imgur.com/SqFHawo.png)

6. Hacemos clic en *Agregar*, y esperamos a que nos aparezca un mensaje como el siguiente:

![](https://i.imgur.com/ahrJBQb.png)

7. Intentamos volver a abrir el RDP.

![](https://i.imgur.com/H0nRzIV.png)

8. Ahora si se nos permite logearnos con nuestro usuario y contraseña.

![](https://i.imgur.com/TX7PUFc.png)
![](https://i.imgur.com/sz2KMzj.png)

9. Clic en *Aceptar*.

10. Después, hacemos clic en *Si*.

![](https://i.imgur.com/4PLq0Rw.png)

11. Ahora si estamos ingresando en la máquina virtual.

![](https://i.imgur.com/RofeTVL.png)

12. Aceptamos.

![](https://i.imgur.com/eTlK0h5.png)

13. Clic en *Yes*.

![](https://i.imgur.com/YAep8YS.png)

14. Podemos abrir el navegador de preferencia y realizar una búsqueda cualquiera.

![](https://i.imgur.com/EuVa0BL.png)

### 〔Añadiendo reglas de salida〕
Por último, una vez enseñado que tenemos internet en nuestra máquina virtual, vamos a limitarla para que no tenga el acceso a dicho elemento con el GSR.

1. Volvemos al recurso del Grupo de seguridad de red en Azure.

2. Vamos a *Reglas de seguridad de salida*. Y clic en *Agregar*.

![](https://i.imgur.com/EPHF1Ao.png)

3. Como en el tema anterior, rellenamos los valores que necesitamos. En *Destino* cambiará la configuración, porque ahora seleccionaremos *Service Tag*, para elegir que tipo de servicio estamos permitiendo o negando. Seleccionamos *Internet*, dejamos el *Servicio* en *Custom*, y para el intervalo ponemos un *.

![](https://i.imgur.com/sB55oei.png)

4. Para el protocolo ponemos *TCP*. Como estamos "impidiendo" a nuestro recurso conectarse a Internet, en *Acción* seleccionaremos *Denegar*. La prioridad puede ser la que queramos empezando desde el 100. Por último, ponemos un nombre.

![](https://i.imgur.com/w6O3fAd.png)

5. Hacemos clic en *Agregar*.

![](https://i.imgur.com/0fToHHm.png)

6. Volviendo a la Máquina Virtual, si entramos a cualquier página de internet, no será posible establecer una conexión con ella, puesto que ahora los puertos están denegados.

![](https://i.imgur.com/NnMIeDP.png)

7. Aunque igual hay algunas excepciones, como los búscadores, tales como *google.com*.

![](https://i.imgur.com/c4e5Ypc.png)
![](https://i.imgur.com/CeWSB6H.png)

8. Pero páginas más específicas como *fast.com*, no será posible su acceso.

![](https://i.imgur.com/CYuYmOS.png)
![](https://i.imgur.com/Si40Nni.png)