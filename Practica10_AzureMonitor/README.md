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

 - [Introducción a Azure Monitor](#introducción-a-azure-monitor)
    - [Información general](#información-general)
    - [Plataforma de datos de Monitor](#plataforma-de-datos-de-monitor)
    - [¿Qué datos recopila Azure Monitor?](#qué-datos-recopila-azure-monitor)
    - [Alertas](#alertas)
    - [Escalado automático](#escalado-automático)
    - [Workbooks](#workbooks)
- [Practica 10](#practica-10-uso-de-azure-monitor)
    - [Creando un recurso](#creando-un-recurso)
    - [Azure Monitor y la creación de alertas](#azure-monitor-y-la-creación-de-alertas)
    - [Estresando la Máquina Virtual](#estresando-la-máquina-virtual)
    - [Datos, métricas y correo electrónico](#datos-métricas-y-correo-electrónico)

-------

# 【Introducción a Azure Monitor】

![](https://azure.microsoft.com/svghandler/monitor?width=600&height=315)

*Azure Monitor* ayuda a maximizar la disponibilidad y el rendimiento de las aplicaciones y los servicios. Ofrece una solución completa para recopilar, analizar y actuar en la telemetría desde los entornos local y en la nube. Esta información le ayudará a conocer el rendimiento de las aplicaciones y a identificar de manera proactiva los problemas que les afectan y los recursos de los que dependen.

Entre los ejemplos de lo que puede hacer con Azure Monitor se incluyen:

- Detección y diagnóstico de problemas en aplicaciones y dependencias con Application Insights.
- Correlación de problemas de infraestructura con VM Insigths y Container Insights.
- Profundización en sus datos de supervisión con Log Analytics para la solución de problemas y diagnósticos profundos.
- Compatibilidad con operaciones a gran escala con acciones automatizadas.
- Creación de visualizaciones con paneles y libros de Azure.
- Recopile datos de los recursos supervisados mediante métricas en Azure Monitor.
- Investigue los datos modificados para supervisar las rutinas o para evaluar los incidentes mediante el Change Analysis.

> ⚠ **Nota**
Este servicio admite **Azure Lighthouse**, que permite a los proveedores de servicios iniciar sesión en su propio inquilino para administrar las suscripciones y los grupos de recursos que los clientes hayan delegado.

### 〔Información general〕
El siguiente diagrama proporciona una visión general de Azure Monitor. En el centro del diagrama están los almacenes de datos de las métricas y los registros, que son los dos tipos fundamentales de datos que se utilizan en Azure Monitor. En la parte izquierda están los orígenes de datos de supervisión que rellenan estos almacenes de datos. En la derecha puede ver las diferentes funciones que realiza Azure Monitor con los datos recopilados. Estas acciones incluyen el análisis, las alertas y el streaming a sistemas externos.

![](https://docs.microsoft.com/es-es/azure/azure-monitor/media/overview/azure-monitor-overview-optm.svg)

### 〔Plataforma de datos de Monitor〕
Todos los datos recopilados por Azure Monitor pueden clasificarse como uno de los dos tipos fundamentales: métricas y registros. Las métricas son valores numéricos que describen algún aspecto de un sistema en un momento dado. Son ligeras y capaces de admitir escenarios de tiempo casi real. Los registros contienen distintos tipos de datos organizados en grupos de registros, donde cada tipo tiene diferentes conjuntos de propiedades. Los datos de telemetría, como los eventos y los seguimientos, se almacenan como registros junto con los datos de rendimiento para poder analizarlos de forma combinada.

En muchos recursos de Azure, los datos recopilados por Azure Monitor aparecen directamente en la página de información general de Azure Portal. Eche un vistazo a cualquier máquina virtual (VM), por ejemplo, y verá varios gráficos en los que aparecen métricas de rendimiento. Seleccione cualquiera de los gráficos para abrir los datos en el Explorador de métricas de Azure Portal. Con el Explorador de métricas puede representar gráficamente los valores de varias métricas a lo largo del tiempo. Puede ver los gráficos de forma interactiva o anclarlos a un panel para verlos con otras visualizaciones.

![](https://docs.microsoft.com/es-es/azure/azure-monitor/media/overview/metrics.png)

Los datos de registro recopilados por Azure Monitor se pueden analizar con consultas que recuperan, consolidan y analizan rápidamente los datos recopilados. Puede crear y probar consultas con Log Analytics en Azure Portal. Puede analizar los datos directamente con distintas herramientas o guardar las consultas para usarlas con visualizaciones o reglas de alertas.

Azure Monitor utiliza una versión del lenguaje de consulta de Kusto adecuado para realizar búsquedas de registros simples, pero también dispone de funciones avanzadas, como agregaciones, combinaciones y análisis inteligentes. Puede aprender rápidamente el lenguaje de consulta con diversas lecciones. Se proporciona orientación concreta a los usuarios que ya están familiarizados con SQL y Splunk.

![](https://docs.microsoft.com/es-es/azure/azure-monitor/media/overview/logs.png)

Change Analysis no solo le avisa de problemas, interrupciones, errores de componentes u otros datos modificados en el sitio en directo. También proporciona información sobre esos cambios en la aplicación, aumenta la observabilidad y reduce el tiempo medio para repararlos (MTTR). Para registrar automáticamente el proveedor de recursos `Microsoft.ChangeAnalysis` en una suscripción de Azure Resource Manager, vaya a Change Analysis desde Azure Portal. Para los cambios en la aplicación web de los invitados puede habilitar Change Analysis mediante la herramienta para diagnosticar y resolver problemas.

Change Analysis se basa en Azure Resource Graph para proporcionar un registro histórico de cómo han cambiado los recursos de Azure con el tiempo. También detecta identidades administradas, actualizaciones del sistema operativo de la plataforma y cambios en el nombre de host. Change Analysis consulta de forma segura las reglas de configuración de IP, la configuración de TLS y versiones de extensión para proporcionar datos más detallados de los cambios.

### 〔¿Qué datos recopila Azure Monitor?〕

Azure Monitor puede recopilar datos de orígenes que van desde la aplicación a cualquier sistema operativo y servicios en los que se basa, hasta la propia plataforma. Azure Monitor recopila datos de cada uno de los siguientes niveles:

- Datos de supervisión de aplicaciones: datos sobre el rendimiento y la funcionalidad del código que se ha escrito, independientemente de la plataforma.
- Datos de supervisión del sistema operativo invitado: datos sobre el sistema operativo en el que se ejecuta la aplicación. Este sistema se puede ejecutar en Azure, en otra nube o en el entorno local.
- Datos de supervisión de recursos de Azure: datos acerca del funcionamiento de un recurso de Azure. Para obtener una lista completa de los recursos que tienen métricas o registros, consulte What can you monitor with Azure Monitor? (¿Qué se puede supervisar con Azure Monitor?).
- Datos de supervisión de suscripciones de Azure: datos sobre el funcionamiento y la administración de una suscripción de Azure, así como sobre el mantenimiento y el funcionamiento propios de Azure.
- Datos de supervisión del inquilino de Azure: datos sobre el funcionamiento de los servicios de Azure en el nivel del inquilino, como Azure Active Directory.
- Datos de los cambios en los recursos de Azure: datos sobre los cambios en los recursos de Azure y cómo abordar y evaluar incidentes y problemas.

En cuanto se crea una suscripción a Azure y se empiezan a agregar recursos, como VM y aplicaciones web, Azure Monitor comienza a recopilar datos. Los registros de actividad registran la creación y modificación de recursos. Las métricas indican cómo está funcionando un recurso y los recursos que consume.

### 〔Alertas〕
Las alertas de Azure Monitor informan de forma proactiva de los estados críticos e intentan aplicar acciones correctivas. Las reglas de alertas basadas en métricas proporcionan alertas casi en tiempo real con valores numéricos. Las reglas basadas en los registros permiten una lógica compleja con datos de varios orígenes.

Las reglas de alertas de Azure Monitor utilizan grupos de acciones, que contienen diferentes conjuntos de destinatarios y acciones que pueden compartirse entre varias reglas. En función de los requisitos, los grupos de acciones pueden realizar diferentes acciones, como utilizar webhooks para que las alertas inicien acciones externas o se integren con las herramientas de administración de herramientas de administración de servicios de TI.

![](https://docs.microsoft.com/es-es/azure/azure-monitor/media/overview/alerts.png)


### 〔Escalado automático〕
Gracias al escalado automático, puede ejecutar la cantidad correcta de recursos para administrar la carga de la aplicación. Cree reglas que usen las métricas recopiladas por Azure Monitor para determinar cuándo se deben agregar automáticamente recursos al aumentar la carga. Elimine los recursos inactivos para ahorrar dinero. Tiene que especificar un número mínimo y máximo de instancias y la lógica para decidir cuándo deben aumentar o disminuir los recursos.

![](https://docs.microsoft.com/es-es/azure/azure-monitor/media/overview/autoscale.png)

### 〔Workbooks〕
Los libros proporcionan un lienzo flexible para el análisis de datos y la creación de informes visuales completos en Azure Portal. Puede usar estas opciones para acceder a varios orígenes de datos desde Azure y combinarlos en experiencias interactivas unificadas. Use los libros proporcionados en Insights o cree los suyos propios a partir de plantillas predefinidas.

![](https://docs.microsoft.com/es-es/azure/azure-monitor/media/overview/workbooks.png)

--------------

# 【Practica 10: Uso de Azure Monitor〕
El objetivo de esta practica será crear un recurso de Azure, monitorear su uso, crear alertas y solicitar que nos manden un correo electrónico en caso de que dicho recurso esté siendo afectado o su uso sea inapropiado.

El ejemplo más sencillo es crear una máquina virtual, y con la telemetría, podemos definir que haga un monitoreo de como está rindiendo el CPU, o sea, que porcentaje de CPU está siendo utilizado al momento de usar nuestra máquina en un lapso de tiempo. Nosotros forzaremos la máquina para que se estrese y use mucha potencia de CPU a proposito.

### 〔Creando un recurso〕
Bien, para ello, empezaremos creando nuestra VM.

1. Vamos a la barra de navegación, y buscamos *Máquinas Virtuales*.

![](https://i.imgur.com/0iP5gEM.png)

2. Damos clic en *Crear*, y seleccionamos *Máquina virtual de Azure*.

![](https://i.imgur.com/pyiydTi.png)

3. Rellenamos los datos solicitados.

![](https://i.imgur.com/LwSYDKq.png)

4. En este caso, usaremos *Windows 10* del tamaño más básico/barato, luego asignamos *usuario* y *contraseña*.

![](https://i.imgur.com/wFWuSaz.png)

5. En puertos de entrada, elegiremos *RDP*. Para finalizar, *confirmamos* el uso de la licencia.

![](https://i.imgur.com/Xnzd5NN.png)

6. Hacemos clic en *Revisar y crear*.

7. Y luego en *Crear*.

![](https://i.imgur.com/yoxmlIA.png)
![](https://i.imgur.com/c3DUi41.png)

8. Seguidamente, vamos al recurso. Clic en *Conectar* y seleccionamos *RDP*.

![](https://i.imgur.com/VuxYd3y.png)

9. Nos redirigirá a esta pestaña. Clic en *Descargar archivo RDP*.

![](https://i.imgur.com/G2VBgLb.png)

Se nos descargará este archivo que funciona con la aplicación *Escritorio remoto* de Windows.

![](https://i.imgur.com/ZKQjtPn.png)

10. Ahora, abrimos el archivo, y hacemos clic en el botón *Conectar*.

![](https://i.imgur.com/EVOi8v2.png)

11. Nos solicitará un usuario y una contraseña, usaremos las que previamente asignamos en la creación del recurso.

![](https://i.imgur.com/gTbUKDV.png)

12. Y por último, *aceptamos* el certificado.

![](https://i.imgur.com/W8h7PZm.png)

Debería mostrarse una ventana parecida a ésta.

![](https://i.imgur.com/7k4qyCg.png)

### 〔Azure Monitor y la creación de alertas〕
Una vez creado el recurso, ahora toca utilizar el servicio que nos permite el monitoreo de dicho recurso y aprenderemos a usar sus funciones básicas.

1. En la barra de búsqueda, escribimos *Monitor*.

![](https://i.imgur.com/HSYVpYd.png)

Aquí podemos ver un poco de las funcionalidades básicas de *Azure Monitor*.

![](https://i.imgur.com/VJzTvHB.png)

2. En la pestaña de *Métricas*, podemos elegir de toda la suscripción uno o varios recursos que pueden ser medidos. Para este ejemplo, elegimos de *ámbito* a nuestra máquina virtual.

![](https://i.imgur.com/zXXThSm.png)

3. En métrica, seleccionamos la que nosotros queramos, para fines prácticos, elegí *Percentage CPU*. Lo que hará es un monitoreo de como va el funcionamiento del CPU en Porcentaje.

![](https://i.imgur.com/Y7LMnxB.png)

Ahora vamos a lo más importante, las *alertas*.

4. Vamos a la pestaña *Alertas*, damos clic en *Crear* y seleccionamos *Regla de alertas*.

![](https://i.imgur.com/IBhyj5v.png)

5. Seleccionamos el ámbito, mejor dicho, el recurso al que queremos enfocarnos. En este caso, nuestra máquina virtual.

![](https://i.imgur.com/Azrm4rK.png)

6. En condición, agregaremos una *señal*. La señal es "el trigger" por asi decirlo, es aquella información que será medida por el Monitor. Entonces, elegimos el *Percentage CPU*.

![](https://i.imgur.com/7l1Focr.png)

Aquí vamos a editar los valores por defecto.

![](https://i.imgur.com/gvl8ydk.png)

7. En *Lógica de alerta*, vamos a cambiar el *Valor del umbral*, que por defecto viene en 60%, pero por ahora lo cambiamos a 40%. Significa que cuando nuestro CPU llegue a 40% o lo sobrepase, se activará el trigger, indicando que hubo una sobrecarga de CPU.

![](https://i.imgur.com/o73SBFJ.png)

8. Y haremos que la verificación sea cada minuto.

Recordando la práctica anterior, aquí también podemos hacer que se ejecuten acciones tras activarse los triggers de las métricas (o de los ámbitos).

9. Vamos a crear un gurpo de acciones, y rellenamos los datos correspondientes.

![](https://i.imgur.com/kK7a84P.png)

10. Ahora, en la pestaña de notificaciones, elegiremos el tipo de notificación que recibiremos, en este caso, correo electrónico. Ponemos un *nombre* y anexamos nuestro *correo electrónico*.

![](https://i.imgur.com/htelnih.png)

11. *Revisar y crear*, y luego en *Crear*.

![](https://i.imgur.com/8NM8tZ0.png)

Esto hará que cada vez que nuestro ámbito (CPU) sobrepase el 40%, recibiremos una alerta y además una notificación a nuestro correo electrónico.

![](https://i.imgur.com/JUj7RGg.png)

12. Terminamos de configurar los datos correspondientes.

![](https://i.imgur.com/GE40YYq.png)

13. *Revisar y crear*. Para finalizar, clic en *Crear*.

![](https://i.imgur.com/DBfswiI.png)
![](https://i.imgur.com/LsDNVxt.png)

### 〔Estresando la Máquina Virtual〕
Ahora toca trabajar con la máquina virtual.

1. Aceptamos las configuraciones de privacidad.

![](https://i.imgur.com/djMqm68.png)

2. Ahora estamos dentro de Windows 10.

![](https://i.imgur.com/SkZdccU.png)

3. La manera más fácil de estresar una computadora es abriendo el *Task manager* o *Administrador de tareas*.

![](https://i.imgur.com/89q4OkX.png)

4. Como podemos ver, la Máquina Virtual ya está estresada bastante y sin hacer nada. Con esto ya sería suficiente, pero aún así quise probar abriendo el navegador Edge.

![](https://i.imgur.com/PkVxBes.png)
![](https://i.imgur.com/E9uJiat.png)

Con esto sería suficiente, el Monitor ya habrá detectado todos casos en que el CPU subió a más del 40%.

### 〔Datos, métricas y correo electrónico〕
Volviendo a los paneles de métricas y alertas, podemos darnos cuenta de que se generó una alerta, indicando que se *desencadenó*. Nos dice la *gravedad de la alerta*, *condición* y la *fecha/hora de activación*.

![](https://i.imgur.com/qkZ8jrv.png)

Si abrimos la alerta, podemos ver una gráfica donde podemos ver los picos de uso de la CPU en su respectiva hora de suceso.

![](https://i.imgur.com/0Dekkz9.png)
![](https://i.imgur.com/T1ELG4q.png)

Además, pudimos recibir un correo que nos alerta de que algo ocurrió con nuestra Máquina virtual. especificando que nuestro *Percentage CPU* subió a más del umbral de 40%

![](https://i.imgur.com/0BjFspj.png)
![](https://i.imgur.com/H5YKcqh.png)