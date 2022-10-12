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

- [Introducción a Azure Policy](#introducción-a-azure-policy)
    - [Información general](#información-general)
    - [Descripción de los resultados de evaluación](#descripción-de-los-resultados-de-evaluación)
    - [Control de la respuesta a una evaluación](#control-de-la-respuesta-a-una-evaluación)
    - [Corrección de recursos no compatibles](#corrección-de-recursos-no-compatibles)
    - [Azure Policy y Azure RBAC](#azure-policy-y-azure-rbac)
    - [Permisos de Azure RBAC en Azure Policy](#permisos-de-azure-rbac-en-azure-policy)
    - [Objetos de Azure Policy](#objetos-de-azure-policy)
        - [Definición de directiva](#definición-de-directiva)
        - [Definición de iniciativa](#definición-de-iniciativa)
        - [Assignments](#assignments)
- [Practica 20](#practica-20-uso-de-azure-policy)
    - [Creando un recurso](#creando-un-recurso)
    - [Interfaz de Policy](#interfaz-de-policy)
    - [Creando una directiva](#creando-una-directiva)
    - [Asignando una directiva](#asignando-una-directiva)
    - [Prueba](#prueba)

-------

# 【Introducción a Azure Policy】

![](https://www.starwindsoftware.com/blog/wp-content/uploads/2020/12/gestion-de-la-conformite-et-du-cloud-azure-policy.png)

*Azure Policy* ayuda a aplicar los estándares de la organización y a evaluar el cumplimiento a escala. Mediante su panel de cumplimiento, proporciona una vista agregada para evaluar el estado general del entorno, con la posibilidad de explorar en profundidad hasta el nivel de recurso y directiva. También ayuda al cumplimiento de los recursos gracias a la corrección masiva de los recursos existentes y la corrección automática de nuevos recursos.

Entre los casos de uso comunes de Azure Policy se incluye la implementación de la gobernanza para la coherencia de los recursos, el cumplimiento normativo, la seguridad, el costo y la administración. Las definiciones de directiva de estos casos de uso comunes ya están disponibles en el entorno de Azure como complementos para ayudarle a comenzar.

Todos los datos y objetos de Azure Policy se cifran en reposo.

### 〔Información general〕
Para evaluar los recursos de Azure, Azure Policy compara las propiedades de esos recursos con las reglas de negocio. Estas reglas de negocios, descritas en formato JSON, se conocen como definiciones de directiva. Para simplificar la administración, se pueden agrupar varias reglas de negocio para formar una iniciativa de directiva (a veces conocida como policySet). Una vez formadas las reglas de negocio, se asigna la definición o la iniciativa de directiva a cualquier ámbito de recursos que admita Azure, como grupos de administración, suscripciones, grupos de recursos o recursos individuales. La asignación se aplica a todos los recursos dentro del ámbito de Resource Manager de esa asignación. Si es necesario, se pueden excluir los subámbitos.

Azure Policy usa un formato JSON para formar la lógica que la evaluación emplea para determinar si un recurso es compatible o no. Las definiciones incluyen metadatos y la regla de directiva. La regla definida puede usar funciones, parámetros, operadores lógicos, condiciones y alias de propiedad para coincidir exactamente con el escenario deseado. La regla de directiva determina qué recursos del ámbito de la asignación se evalúan.

### 〔Descripción de los resultados de evaluación〕
Los recursos se evalúan en momentos concretos durante el ciclo de vida de los recursos, el ciclo de vida de la asignación de directivas y la evaluación de cumplimiento periódica continua. Estos son los acontecimientos o eventos que hacen que se evalúe un recurso:

- Un recurso se crea o actualiza en un ámbito con una asignación de directiva.
- Una directiva o iniciativa se asigna recientemente a un ámbito.
- Una directiva o iniciativa que ya está asignada a un ámbito se actualiza.
- Durante el ciclo de evaluación de cumplimiento estándar, que se produce una vez cada 24 horas.

### 〔Control de la respuesta a una evaluación〕
Las reglas de negocio para administrar recursos no compatibles varían considerablemente según la organización. Entre los ejemplos de la forma en que una organización desea que la plataforma responda a un recurso no compatible se incluyen:

- Denegar el cambio de recursos
- Registrar el cambio en el recurso
- Modificar el recurso antes del cambio
- Modificar el recurso después del cambio
- Implementar recursos compatibles relacionados

Azure Policy hace posible cada una de estas respuestas empresariales mediante la aplicación de efectos. Los efectos se establecen en la parte de la **definición de directiva** de la regla de directiva.

### 〔Corrección de recursos no compatibles〕
Aunque estos efectos influyen principalmente sobre un recurso cuando este se crea o actualiza, Azure Policy también admite el tratamiento de recursos no compatibles existentes sin necesidad de modificar ese recurso.

### 〔Azure Policy y Azure RBAC〕
Hay algunas diferencias importantes entre Azure Policy y el control de acceso basado en rol de Azure (Azure RBAC). Para evaluar el estado, Azure Policy examina las propiedades de los recursos que se representan en Resource Manager y las propiedades de algunos proveedores de recursos. Azure Policy no restringe las acciones (también denominadas operaciones). Azure Policy garantiza que el estado de los recursos sea compatible con las reglas de negocio sin importar quién hizo el cambio o quién tiene permisos para hacerlo. Algunos recursos de Azure Policy, como las definiciones de directivas, las definiciones de iniciativas y las asignaciones, son visibles para todos los usuarios. Este diseño permite la transparencia a todos los usuarios y servicios para saber qué reglas de directiva se establecen en su entorno.

Azure RBAC se centra en la administración de acciones del usuario en ámbitos diferentes. Si es necesario controlar alguna acción, Azure RBAC es la herramienta idónea. Incluso si un individuo tiene acceso para realizar una acción, si el resultado es un recurso no compatible, Azure Policy sigue bloqueando la creación o la actualización.

La combinación de Azure RBAC y Azure Policy proporciona un control completo del ámbito en Azure.

### 〔Permisos de Azure RBAC en Azure Policy〕

Azure Policy dispone de varios permisos, conocidos como operaciones, en dos proveedores de recursos:

- Microsoft.Authorization
- Microsoft.PolicyInsights

Muchos roles integrados conceden permiso a recursos de Azure Policy. El rol **Colaborador de directiva de recursos** incluye la mayoría de las operaciones de Azure Policy. El rol **Propietario** tiene derechos completos. Tanto el rol **Colaborador** como el rol **Lector** tienen acceso a todas las operaciones de *lectura* de Azure Policy.

**Colaborador** puede desencadenar la corrección de recursos, pero no puede *crear* ni *actualizar* definiciones y asignaciones. **Administrador de acceso de usuario** es necesario para conceder la identidad administrada en los permisos necesarios de las asignaciones **deployIfNotExists** o **modify**.

> ⚠️ Nota
Todos los objetos de la directiva, como las definiciones, iniciativas y asignaciones, se pueden leer mediante todos los roles de su ámbito. Por ejemplo, una asignación de directiva con alcance a una suscripción de Azure podrá leerse por todos los titulares de roles en el alcance de la suscripción y en niveles inferiores.

Si ninguno de los roles integrados tiene los permisos necesarios, cree un rol personalizado.

Las operaciones de Azure Policy pueden tener un importante impacto en el entorno de Azure. Solo se debe asignar el conjunto mínimo de permisos necesarios para realizar una tarea y estos permisos no se deben conceder a los usuarios que no los necesiten.

> ⚠️ Nota
La identidad administrada de una asignación de directiva deployIfNotExists or modify necesita permisos suficientes para crear o actualizar los recursos de destino.

### 〔Objetos de Azure Policy〕

#### 〔Definición de directiva〕
El proceso de creación e implementación de una directiva en Azure Policy comienza con la creación de una definición de directiva. Cada definición de directiva tiene condiciones que regulan su aplicación. Además, tiene un efecto definido que se produce cuando se cumplen las condiciones.

En Azure Policy, se ofrecen varias directivas integradas que están disponibles de manera predeterminada. Por ejemplo:

- **Allowed Storage Account SKUs** (SKU permitidas de cuentas de almacenamiento) (denegar): determina si una cuenta de almacenamiento que se va a implementar se engloba dentro de un conjunto de tamaños de SKU. Su efecto es denegar todas las cuentas de almacenamiento que no cumplen el conjunto de tamaños de SKU definidos.
- **Allowed Resource Type** (Tipo de recurso permitido) (denegar): define los tipos de recursos que se pueden implementar. Su efecto es denegar todos los recursos que no forman parte de esta lista definida.
- **Ubicaciones permitidas** (denegar): restringe las ubicaciones disponibles para los nuevos recursos. Su efecto se utiliza para exigir los requisitos de cumplimiento de replicación geográfica.
- **Allowed Virtual Machine SKUs** (SKU de máquina virtual permitidas) (denegar): especifica un conjunto de SKU de máquina virtual que se pueden implementar.
- **Add a tag to resources** (Agregar una etiqueta a los recursos) (modificar): aplica una etiqueta obligatoria y su valor predeterminado si la solicitud de implementación no la especifica.
- **Not allowed resource types** (Tipos de recursos no permitidos) (denegar): impide la implementación de una lista de tipos de recursos.

Para implementar estas definiciones de directiva (tanto las definiciones integradas como las personalizadas), será preciso asignarlas. Puede asignar cualquiera de estas directivas a través de Azure Portal, PowerShell o la CLI de Azure.

La evaluación de la directiva se realiza con distintas acciones, como la asignación de directivas o las actualizaciones de directiva.

#### 〔Definición de iniciativa〕
Una definición de iniciativa es una colección de definiciones de directiva personalizadas para alcanzar un único objetivo general. Las definiciones de iniciativa simplifican la administración y asignación de las definiciones de directiva. Tal simplificación se realiza mediante la agrupación de un conjunto de directivas como un solo elemento. Por ejemplo, podría crear una iniciativa titulada **Habilitación de la supervisión en Microsoft Defender for Cloud**, con el objetivo de supervisar todas las recomendaciones de seguridad disponibles en la instancia de Microsoft Defender for Cloud.

> ⚠️ Nota
El SDK, como CLI de Azure y Azure PowerShell, usa propiedades y parámetros denominados PolicySet para hacer referencia a las iniciativas.

En esta iniciativa, tendría definiciones de directiva como las siguientes:

- **Supervisar SQL Database sin cifrar en Microsoft Defender for Cloud**, para supervisar servidores y bases de datos SQL sin cifrar.
- **Supervisar las vulnerabilidades del SO en Microsoft Defender for Cloud**, para supervisar los servidores que no cumplen con la base de referencia configurada.
- **Supervisar Endpoint Protection omitido en Microsoft Defender for Cloud**, para supervisar los servidores que no tienen instalado un agente de protección de los puntos de conexión.

Al igual que los parámetros de directiva, los parámetros de iniciativa permiten simplificar la administración de iniciativas mediante la reducción de la redundancia. Los parámetros de iniciativa son aquellos que las definiciones de directiva usan dentro de la iniciativa.

Por ejemplo, imagine un escenario en el que tiene la definición de una iniciativa (**initiativeC**), con las definiciones de directiva **policyA** y **policyB**, y que cada una de ellas espera un tipo diferente de parámetro:

| Directiva | Nombre del parámetro | tipo del parámetro | Nota: |
| - | - | - | - |
| policyA | allowedLocations | array | Este parámetro espera una lista de cadenas para un valor, porque el tipo de parámetro está definido como una matriz |
| policyB | allowedSingleLocation | string | Este parámetro espera una palabra para un valor, porque el tipo de parámetro se definió como una cadena |

En este escenario, tiene tres opciones en el momento de definir los parámetros de iniciativa para **initiativeC**:

- Use los parámetros de las definiciones de directiva dentro de esta iniciativa: en este ejemplo, *allowedLocations* y *allowedSingleLocation* se convierten en parámetros de iniciativa para **initiativeC**.
- Proporcione valores a los parámetros de las definiciones de directiva dentro de esta definición de iniciativa. En este ejemplo, puede proporcionar una lista de ubicaciones al parámetro de **policyA**, **allowedLocations**, y al parámetro de **policyB**, **allowedSingleLocation**. También puede proporcionar valores cuando asigne esta iniciativa.
- Proporcione una lista de las opciones de *value* que se puede usar cuando se asigna esta iniciativa. Cuando asigna esta iniciativa, los parámetros inherentes de las definiciones de directiva dentro de la iniciativa solo pueden tener valores provenientes de esta lista.

Al crear las opciones de valor en una definición de iniciativa, no se puede proporcionar un valor diferente durante la asignación de la iniciativa, porque no forma parte de la lista.

#### 〔Assignments〕
Una asignación es una definición o una iniciativa de directiva que se ha asignado a un ámbito concreto. Este ámbito puede ir desde un grupo de administración a un recurso individual. El término ámbito hace referencia a todos los recursos, grupos de recursos, suscripciones o grupos de administración a los que se asigna la definición. Todos los recursos secundarios heredan las asignaciones. Este diseño conlleva que una definición aplicada a un grupo de recursos también se aplique a los recursos de dicho grupo. Sin embargo, puede excluir un subámbito de la asignación.

Por ejemplo, en el ámbito de la suscripción, puede asignar una definición que impida la creación de recursos de red. También podría excluir un grupo de recursos en la suscripción que está diseñado para la infraestructura de red. De esta forma, concede acceso a este grupo de recursos de red a los usuarios de confianza con la creación de recursos de red.

En otro ejemplo, podría asignar una definición de lista de tipos de recursos permitidos en el nivel de grupo de administración. Luego, puede asignar una directiva más permisiva (que permita más tipos de recursos) en un grupo de administración secundario o incluso directamente en las suscripciones. Sin embargo, este ejemplo podría no funcionar porque Azure Policy es un sistema de denegación explícito. En su lugar, debe excluir el grupo de administración secundario o la suscripción de la asignación de nivel de grupo de administración. Después, puede asignar la definición más permisiva en el grupo de administración secundario o en el nivel de suscripción. Si alguna asignación tiene como resultado la denegación de un recurso, la única manera de permitir el recurso es modificar la directiva de denegación.

Las asignaciones de directivas siempre usan el estado más reciente de su definición o iniciativa asignadas al evaluar los recursos. Si se cambia una definición de directiva que ya está asignada, todas las asignaciones existentes de esa definición usarán la lógica actualizada al realizar la evaluación.

--------------

# 【Practica 20: Uso de Azure Policy〕
Para esta práctica, nos enfocaremos en crear una directiva sencilla, la cual limite la ubicación en la cual nuestros recursos pueden ser creados.

### 〔Creando un recurso〕
Vamos a crear el recurso más sencillo de todos, que propiamente un *grupo de recursos*. (Si, cuentan como recursos)

1. Buscamos *Grupos de recursos*.

![](https://i.imgur.com/EHRSNit.png)

2. Hacemos clic en *Crear*.

![](https://i.imgur.com/FzKb6zC.png)

3. Seleccionamos nuestra *suscripción*, asignamos un *nombre* y elegimos la *región*. (Para esta práctica, obligatoriamente pondré la región en US)

![](https://i.imgur.com/euI914m.png)

4. Clic en *Revisar y crear*. Luego en *Crear*.

![](https://i.imgur.com/NIo50UM.png)

### 〔Interfaz de Policy〕

1. Para buscar al Azure Policy, escribimos *Directiva*. Clic en el primer resultado.

![](https://i.imgur.com/5YdaFhs.png)

2. Podemos apreciar la interfaz que tiene Directiva de tal forma que podemos ver un gráfico de pastel, cuyas divisiones son la compatibilidad de los recursos. Por el momento, solo tenemos un recurso (el que creamos) y aún sin haberle hecho nada, ya tiene incompatibilidades.

![](https://i.imgur.com/Ra8sRH5.png)

3. Aquí podemos ver las *directivas* e *iniciativas* que tiene nuestra nube, y una gráfica de todo lo que hemos realizado en los últimos 7 días (de recursos creados con anterioridad).

![](https://i.imgur.com/CKCWhTd.png)

4. Si hacemos clic en la *iniciativa*, podemos ver sus características, y todo aquello que esté bien al margen del cumplimiento. Alcanzamos a ver que tiene 24 directivas no compatibles, esto significa que tiene algunos parámetros no válidos.

![](https://i.imgur.com/5ZiLas4.png)

Como bien dije, apenas hemos creado el recurso y no hemos realizado nada, ¿Cómo es posible que tenga tantos errores?

Esto no quiere representar que estémos haciendo algo mal o que el recurso se creó erróneamente, esto representa que debido a la naturaleza de la nube, vienen con cosas limitadas, ya sea por el recurso en si o *la suscripción*. Recordemos que ésta es una suscripción de estudiante, muy diferente a una suscripción profesional o empresarial. 

Por ende, muchas cosas estarán *deshabilitadas* en dicha suscripción; sin embargo, aunque tengamos tantos errores de incompatibilidad, la suscripción ya está medida para que estos problemas no lleguen a repercutir gravemente en el uso de Azure, por tal motivo es que casi no notamos estos desperfectos al momento de trabajar.

5. Aquí podemos ver la lista completa de las *directivas* en conflicto.

![](https://i.imgur.com/4CPAbo9.png)

6. Si clickeamos en cualquiera, podemos verla a detalle y saber la manera de corregirla.

![](https://i.imgur.com/MXhCa53.png)
![](https://i.imgur.com/LlkdZ8o.png)

7. También tenemos el apartado de *Cumplimiento*. Es lo mismo que vimos en *Información general*.

![](https://i.imgur.com/KMT51nX.png)

8. El apartado de *Corrección* es para aquellas directivas o iniciativas que tenian conflicto y fueron corregidas (terminan en este apartado).

![](https://i.imgur.com/XXfHZDc.png)

9. Y por último, el apartado *Eventos* es para cuando en medio del desarrollo o uso de la nube, se encuentran nuevos problemas de incompatibilidad, Azure las almacena aquí para su posterior análisis en segundo plano.

![](https://i.imgur.com/yzAJQUO.png)

### 〔Creando una directiva〕
Ahora, crearemos una directiva anexada a nuestro grupo de recursos, y ésta contendrá la orden de que no se pueden crear recursos fuera de USA.

1. Vamos al apartado *Definiciones* y hacemos clic en *Definición de directiva*.

![](https://i.imgur.com/teAsK3F.png)

2. Hacemos clic al botón Azul, y nos pedirá elegir la ubicación de definición, en otras palabras, a donde aplicaremos la directiva.

3. Una vez desplegada la ventana de la derecha, elegiremos nuestra *suscripción*.

![](https://i.imgur.com/lnwEg4w.png)

4. Clic en *Seleccionar*.

![](https://i.imgur.com/CrdOk6s.png)

5. Rellenaremos los campos correspondientes.

![](https://i.imgur.com/Q45mwYM.png)

6. En la parte de abajo, podemos ver un código JSON, el cual, como vimos en prácticas anteriores (Plantillas ARM), podemos manipular para ser utilizado como plantilla e implementarse varias veces si así lo requerimos.

![](https://i.imgur.com/IHxYIWc.png)

7. Clic en *Guardar*.

![](https://i.imgur.com/FpG34a6.png)
![](https://i.imgur.com/wvngDg6.png)

### 〔Asignando una directiva〕

1. Vamos al apartado *Asignaciones*, y clic en *Asignar directiva*.

![](https://i.imgur.com/WMplngk.png)

2. Hacemos clic al botón Azul, y nos pedirá elegir el ámbito, en otras palabras, el recurso/grupo de recursos a donde vamos a aplicar la directiva. La seleccionamos y clic en *Seleccionar*.

![](https://i.imgur.com/RPnFaGF.png)
![](https://i.imgur.com/uJ7W05r.png)

3. Podemos crear una exclusión, por si queremos evitar que a un recurso en concreto se le aplique la directiva.

![](https://i.imgur.com/Il9dL1P.png)

4. Vamos a darle clic al botón Azul de *Definición de directiva*. Podemos ver nuestra directiva creada, pero en este caso no la usaremos debido a que no contiene nada de las funciones que haría la directiva real de *Ubicaciones permitidas*.

![](https://i.imgur.com/IdT0eOq.png)

5. Buscamos *Ubicaciones* en el navegador, y tenemos que localizar una directiva llamada *Ubicaciones permitidas*. La seleccionamos

![](https://i.imgur.com/2j3EbNE.png)

6. Le ponemos un *nombre*.

![](https://i.imgur.com/5OjqL8f.png)

7. Vamos a la pestaña *Parámetros*.

![](https://i.imgur.com/nET3Pqa.png)

Tenemos una lista desplegable de diferentes ubicaciones dentro de Azure. Como bien mencionamos antes, queremos que nuestro grupo de recursos solo esté limitado a que se puedan crear recursos dentro de USA. Por ende, vamos a seleccionar todas las ubicaciones dentro de USA, y las demás las dejamos sin marcar. (En mi caso, solo puse 2 marcadas)

8. En la pestaña *Mensajes de no cumplimiento*, nosotros podemos escribir un mensaje de alerta, la cual aparecerá cuando dicha directiva se incumpla. El mensaje mostrará lo que nosotros pusimos al momento de dar error nuestra implementación.

![](https://i.imgur.com/Hv66Huy.png)

9. Clic en *Revisar y crear*, y luego *Crear*.

![](https://i.imgur.com/uh7HYrB.png)
![](https://i.imgur.com/9neKWaN.png)

### 〔Prueba〕
Para saber si funcionó, vamos a crear un recurso intentando forzar un error de implementación.

1. Crearé un recurso Functions. Buscamos *Aplicación de funciones*.

![](https://i.imgur.com/PinRbhQ.png)

2. Clic en *Crear*.

![](https://i.imgur.com/zjhZpPs.png)

3. Rapidamente llenamos los campos necesarios.

![](https://i.imgur.com/yrEZfoD.png)

4. AQUÍ LO MÁS IMPORTANTE. El grupo de recurso asignado fue *Practica20*, pero ahora mismo pondré que mi recurso tenga una ubicación en el **Sur de Brasil**. 

![](https://i.imgur.com/fok8prV.png)

5. Clic en *Revisar y crear*. En este punto, Azure empieza a tener complicaciones para verificar que todo esté bien. Sin embargo, somos capaces de pasar la primera linea de verificación.

![](https://i.imgur.com/I3v331F.png)

6. Damos clic en *Crear*.

![](https://i.imgur.com/GLQRHsR.png)
![](https://i.imgur.com/3urehKP.png)

7. Aquí ya nos arrojó un error. Nos impidió la creación del recurso, apesar de que todo esté bien, solo nos falló una cosa. En el mensaje en rojo, damos clic en *Please see details for more information ➡*.

![](https://i.imgur.com/RcAS5g0.png)

8. Podemos apreciar el motivo de nuestro error, el cual es el mensaje que nosotros mismos colocamos en caso de haber un incumplimiento de la directiva.

![](https://i.imgur.com/HyirNuA.png)

En simples palabras, el error ocurrió porque nuestro grupo de recursos tiene una regla que dice: *Todos los recursos que estén dentro de mi, no pueden estar en otras regiones que no sean USA*.

Y nosotros colocamos nuestro Functions en una ubicación de Brasil. Por eso el retén nos detuvo de crear el recurso, porque el Policy fue notificado de que hay una incongruencia en la creación de ese recurso en ese grupo de recursos.

9. Si volvemos al apartado de *Detalles*, y ahora ajustamos otra región (dentro de USA). Damos clic en *Revisar y crear*.

![](https://i.imgur.com/CiMNLUR.png)

10. Y ahora clic en *Crear*.

![](https://i.imgur.com/IHWVJUi.png)

11. Ahora si fuimos capaces de crear un recurso dentro de nuestro grupo de recursos, el cual ahora si cumplió con la directiva establecida, y no hubieron más errores.

![](https://i.imgur.com/OcU1nbv.png)