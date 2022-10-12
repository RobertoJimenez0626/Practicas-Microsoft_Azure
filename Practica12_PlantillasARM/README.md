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

 - [Introducción a plantillas de ARM](#introducción-a-plantillas-de-arm)
    - [¿Por qué elegir plantillas de Resource Manager?](#por-qué-elegir-plantillas-de-resource-manager)
    - [Archivo de plantilla](#archivo-de-plantilla)
    - [Proceso de implementación de plantillas](#proceso-de-implementación-de-plantillas)
    - [Diseño de plantilla](#diseño-de-plantilla)
- [Practica 12](#practica-12-creación-de-plantillas-de-arm)
    - [Creando un grupo de recursos](#creando-un-grupo-de-recursos)
    - [Instalando plugin de ARM Tools](#instalando-plugin-de-arm-tools)
    - [Creando una plantilla básica](#creando-una-plantilla-básica)
    - [Comprobando implementación](#comprobando-implementación)
    - [Implementando un recurso con nuestra plantilla](#implementando-un-recurso-con-nuestra-plantilla)

-------

# 【Introducción a plantillas de ARM】

![](https://blog.victorsilva.com.uy/assets/images/postsImages/AZ_ARM_templates_1.png)

Con el traslado a la nube, muchos equipos han adoptado métodos de desarrollo más ágiles. Estos equipos se iteran rápidamente. Necesitan implementar repetidamente sus soluciones en la nube y saber que su infraestructura se encuentra en un estado confiable. Dado que la infraestructura se ha convertido en parte del proceso iterativo, ha desaparecido la división entre las operaciones y el desarrollo. Por ello, los equipos necesitan administrar la infraestructura y el código de aplicación a través de un proceso unificado.

Para cumplir estos desafíos, puede automatizar las implementaciones y usar la práctica de infraestructura como código. En el código, debe definir la infraestructura que va a implementar. Así pues, el código de infraestructura se convierte en parte del proyecto. Al igual que el código de la aplicación, puede almacenar el código de infraestructura en un repositorio de origen y agregarle un número de versión. Cualquier miembro del equipo podrá ejecutar el código e implementar entornos similares.

Para implementar la infraestructura como código para las soluciones de Azure, use las *plantillas de Azure Resource Manager* (plantillas de ARM). La plantilla es un archivo de notación de objetos JavaScript (JSON) que contiene la infraestructura y la configuración del proyecto. La plantilla usa sintaxis declarativa, lo que permite establecer lo que pretende implementar sin tener que escribir la secuencia de comandos de programación para crearla. En la plantilla se especifican los recursos que se van a implementar y las propiedades de esos recursos.

> 💡 **Sugerencia**
Hemos presentado un nuevo lenguaje denominado **Bícep** que ofrece las mismas capacidades que las plantillas de ARM pero con una sintaxis más fácil de usar. Cada archivo de Bicep se convierte automáticamente en una plantilla de ARM durante la implementación. Si está pensando en usar infraestructura como opciones de código, le recomendamos que eche un vistazo a [**Bicep**](https://docs.microsoft.com/es-es/azure/azure-resource-manager/bicep/overview?tabs=bicep). 

### 〔¿Por qué elegir plantillas de Resource Manager?〕
Si intenta decidir entre usar plantillas de Resource Manager o una de las demás infraestructuras como servicios de código, tenga en cuenta las ventajas siguientes del uso de plantillas:

- **Sintaxis declarativa**: las plantillas de Resource Manager permiten crear e implementar una infraestructura de Azure completa de forma declarativa. Por ejemplo, puede implementar no solo máquinas virtuales, sino también la infraestructura de red, los sistemas de almacenamiento y cualquier otro recurso que pueda necesitar.

- **Resultados repetibles**: Implemente repetidamente la infraestructura a lo largo del ciclo de vida del desarrollo y tenga la seguridad de que los recursos se implementan de forma coherente. Las plantillas son idempotentes, lo que significa que puede implementar la misma plantilla varias veces y obtener los mismos tipos de recursos en el mismo estado. Puede desarrollar una plantilla que represente el estado deseado, en lugar de desarrollar muchas plantillas independientes para representar las actualizaciones.

- **Orquestación**: No tiene que preocuparse por la complejidad de las operaciones de ordenación. Resource Manager se encarga de gestionar la implementación de recursos interdependientes para que se creen en el orden correcto. Cuando es posible, Resource Manager implementa los recursos en paralelo para que las implementaciones finalicen más rápido que las implementaciones en serie. La plantilla se implementa mediante un comando, en lugar de hacerlo con varios comandos imperativos.

![](https://docs.microsoft.com/es-es/azure/azure-resource-manager/templates/media/overview/template-processing.png)

- **Archivos modulares**: Puede dividir las plantillas en componentes más pequeños y reutilizables y vincularlos en el momento de la implementación. También puede anidar una plantilla dentro de otra.

- **Cree cualquier recurso de Azure**: Puede usar inmediatamente los nuevos servicios y características de Azure en las plantillas. En cuanto un proveedor de recursos introduce nuevos recursos, puede implementarlos a través de plantillas. No tiene que esperar a que se actualicen las herramientas o los módulos antes de usar los nuevos servicios.

- **Extensibilidad**: con los scripts de implementación, puede agregar scripts de PowerShell o Bash a las plantillas. Los scripts de implementación amplían su capacidad para configurar recursos durante la implementación. Un script se puede incluir en la plantilla o almacenar en un origen externo y hacer referencia a él en la plantilla. Los scripts de implementación le ofrecen la posibilidad de completar la configuración del entorno integral en una sola plantilla de ARM.

- **Pruebas**: puede asegurarse de que la plantilla sigue las instrucciones recomendadas si la prueba con el kit de herramientas de la plantilla ARM (arm-ttk). Este kit de pruebas es un script de PowerShell que puede descargar de GitHub. El kit de herramientas facilita el desarrollo de conocimientos con el lenguaje de plantilla.

- **Vista previa de los cambios**: puede usar la operación hipotética para obtener una vista previa de los cambios antes de implementar la plantilla. Con la operación hipotética puede ver qué recursos se crearán, actualizarán o eliminarán, así como las propiedades de los recursos que se cambiarán. La operación hipotética comprueba el estado actual del entorno y elimina la necesidad de administrar el estado.

- **Validación integrada**: La plantilla solo se implementa después de pasar la validación. Resource Manager se encarga de comprobar la plantilla antes de iniciar la implementación para asegurarse de que esta se realizará correctamente. Es menos probable que la implementación se detenga a medio acabar.

- **Implementaciones con seguimiento**: En Azure Portal puede revisar el historial de implementación y obtener información sobre la implementación de la plantilla. También puede ver la plantilla que se implementó, los valores de parámetro agregados y los valores de salida. Recuerde que no se realiza el seguimiento de otras infraestructuras como servicios de código a través del portal.

![](https://docs.microsoft.com/es-es/azure/azure-resource-manager/templates/media/overview/deployment-history.png)

- **Directiva como código**: Azure Policy es un marco de directiva como código para automatizar la gobernanza. Si usa directivas de Azure, la corrección de la directiva se realiza en recursos no compatibles cuando se implementa mediante plantillas.

- **Planos técnicos de implementación**: Puede aprovechar las ventajas de los Planos técnicos proporcionados por Microsoft para cumplir los estándares de cumplimiento normativo. Estos planos técnicos incluyen plantillas precompiladas para distintas arquitecturas.

- **Integración de CI/CD**: Puede integrar plantillas en sus herramientas de integración e implementación continuas (CI/CD), que pueden automatizar las canalizaciones de versión para llevar a cabo actualizaciones de infraestructura y aplicaciones rápidas y confiables. Mediante la tarea de plantilla de Resource Manager y Azure DevOps puede usar Azure Pipelines para compilar e implementar proyectos de plantillas de Resource Manager de manera continua.

- **Código exportable**: Puede recuperar una plantilla de un grupo de recursos existente mediante la exportación del estado actual del grupo de recursos o la visualización de la plantilla de una implementación determinada. Una buena estrategia para aprender sobre la sintaxis de una plantilla es consultar la plantilla exportada.

- **Herramientas de creación**: Puede crear plantillas con Visual Studio Code y la extensión de la herramienta de plantillas. Podrá utilizar IntelliSense, el resaltado de sintaxis, la ayuda en línea y muchas otras funciones de lenguaje. Además de Visual Studio Code, también puede usar Visual Studio.


### 〔Archivo de plantilla〕
Dentro de la plantilla, puede escribir expresiones de plantilla que aumentan las capacidades de JSON. Estas expresiones hacen uso de las funciones que proporciona Resource Manager.

La plantilla contiene las secciones siguientes:

- Parámetros: proporcione valores durante la implementación que permitan usar la misma plantilla con entornos diferentes.

- Variables: defina los valores que se reutilizan en las plantillas. Se pueden crear a partir de valores de parámetro.

- Funciones definidas por el usuario: cree funciones personalizadas que simplifiquen la plantilla.

- Recursos: especifique los recursos que se van a implementar.

- Salidas: devuelva valores de los recursos implementados.

### 〔Proceso de implementación de plantillas〕
Cuando se implementa una plantilla, Resource Manager la convierte en operaciones de la API de REST. Por ejemplo, cuando Resource Manager recibe una plantilla con la siguiente definición de recursos:

```json
"resources": [
  {
    "type": "Microsoft.Storage/storageAccounts",
    "apiVersion": "2019-04-01",
    "name": "mystorageaccount",
    "location": "westus",
    "sku": {
      "name": "Standard_LRS"
    },
    "kind": "StorageV2",
    "properties": {}
  }
]
```

Convierte la definición en la siguiente operación de API de REST, que se envía al proveedor de recursos Microsoft.Storage:

```html
PUT
https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/mystorageaccount?api-version=2019-04-01
REQUEST BODY
{
  "location": "westus",
  "sku": {
    "name": "Standard_LRS"
  },
  "kind": "StorageV2",
  "properties": {}
}
```

Tenga en cuenta que el valor de apiVersion establecido en la plantilla para el recurso se usa como la versión de API para la operación REST. Puede implementar la plantilla varias veces y confiar en que seguirá funcionando. Al usar la misma versión de la API, no tiene que preocuparse de los cambios importantes que se pueden introducir en versiones posteriores.

Para implementar una plantilla, use cualquiera de las siguientes opciones:

- Azure Portal
- CLI de Azure
- PowerShell
- REST API
- Button del repositorio de GitHub
- Azure Cloud Shell

### 〔Diseño de plantilla〕
La definición de plantillas y grupos de recursos depende únicamente de usted, al igual que la administración de la solución. Por ejemplo, puede implementar su aplicación de tres niveles a través de una única plantilla en un único grupo de recursos.

![](https://docs.microsoft.com/es-es/azure/azure-resource-manager/templates/media/overview/3-tier-template.png)

No obstante, no es necesario que defina toda la infraestructura en una sola plantilla. A menudo, tiene sentido dividir los requisitos de implementación en un conjunto de plantillas seleccionadas, específicas para un propósito. Estas plantillas se pueden reutilizar fácilmente para distintas soluciones. Para implementar una solución concreta, cree una plantilla principal que vincule todas las plantillas necesarias. La imagen siguiente muestra cómo implementar una solución de tres niveles mediante una plantilla principal que incluye tres plantillas anidadas.

![](https://docs.microsoft.com/es-es/azure/azure-resource-manager/templates/media/overview/nested-tiers-template.png)

Si desea que sus niveles tengan ciclos de vida independientes, puede implementar los tres niveles en grupos de recursos independientes. Observe que todavía se pueden vincular los recursos a los recursos de otros grupos.

![](https://docs.microsoft.com/es-es/azure/azure-resource-manager/templates/media/overview/tier-templates.png)

--------------

# 【Practica 12: Creación de plantillas de ARM〕
Lo que haremos en esta practica será crear un recurso "de forma externa" al portal de Azure mediante lineas de código y programación. 

Para ello, usaré el entorno de desarrollo Visual Studio Code, el CLI de Azure, y el CMD. Iré explicando cada cosa escrita en el código para que se entienda bien.

### 〔Creando un grupo de recursos〕
Primero que nada, necesitamos crear un grupo de recursos en nuestro portal de Azure (más adelante veremos porqué). Es posible crearlo de igual forma como lo haremos en toda la práctica, pero por simplicidad lo crearé así.

1. Buscamos *Grupos de recursos*.

![](https://i.imgur.com/NEoarBJ.png)

2. Rellenamos los datos que nos solicitan, y luego clic en *Revisar y crear*.

![](https://i.imgur.com/7gNz6Qj.png)

3. Después, *Crear*.

![](https://i.imgur.com/ioKBujo.png)

### 〔Instalando plugin de ARM Tools〕
Como mencioné, usaré Visual Studio Code. En este entorno, tenemos acceso a un "Marketplace" (justo como Azure) donde existe a nuestra disposición una cantidad inmensa de complementos/plugins que nos habilita nuevas funciones que no vienen  por defecto en VSC.

1. Vamos al icono de los cuadrados (Marketplace).

![](https://i.imgur.com/t7vBu3x.png)

2. En la barra de búsqueda, escribimos *Azure Resource Manager*, y debemos encontrar el resultado que vemos en la imagen:

3. Damos clic en *Instalar*.

![](https://i.imgur.com/LW0uITF.png)

![](https://i.imgur.com/ps4CaEV.png)

![](https://i.imgur.com/tijT6E9.png)

### 〔Creando una plantilla básica〕
Ahora podemos empezar a "programar" la plantilla.

1. Creamos un nuevo archivo con terminación `.json`

![](https://i.imgur.com/TO7p3tX.png)

2. Primero que nada, abrimos **Llaves** `{ }` y dentro de ellos es donde va nuestro código.

- En la `línea 2` tenemos un schema. La sintaxis de un JSON Schema define los diferentes campos que una estructura concreta posee. En este caso, estamos agarrando de schema uno prefabricado por Azure para la implementación externa de componentes por código.

- En la `línea 4`, tenemos un valor numérico para la versión del schema que estamos creando.

- Por último, `línea 5`, tendremos los "resources" y unos **Corchetes**, en los cuales van a ir todos los recursos que queramos implementar. En este caso, lo dejaremos vacío.

![](https://i.imgur.com/PyPoiYT.png)

3. Ahora, guardamos el archivo.

4. En el Explorador, hacemos clic derecho sobre el archivo y seleccionamos *Mostrar en el Explorador de Archivos*.

![](https://i.imgur.com/JPeacvS.png)

5. En la barra de navegación del Explorer, borramos todo y escribimos **CMD**.

![](https://i.imgur.com/mtNkJXo.png)

6. Se nos abrirá el CMD con la ubicación exacta de nuestro archivo, listo para ser manipulado.

![](https://i.imgur.com/Xk3JFbX.png)

7. Ahora, toca explicar a detalle el siguiente código, el cual ingresaremos al CMD para implementar nuestra plantilla en Azure de forma remota.

Recordando que tenemos instalado en nuestra PC el CLI de Azure, los comandos correspondientes a Azure están funcionando correctamente, por ende, ya tenemos logeado nuestro CLI con nuestra cuenta de Azure.

- La `linea 1` es un comando de Azure que nos permite crear una implementación en un grupo de recursos.

- En la `linea 2` nosotros asignamos un nombre a la implementación.

- Para la `linea 3` asignamos a que grupo de recursos se hará nuestra implementación. Es por esto que previamente debimos crear un grupo de recursos con el cual iriamos a trabajar.

- Por último, en la `linea 4` le decimos a Azure cuál es el archivo de nuestra plantilla la cual queremos implementar para que sea utilizada en nuestro grupo de recursos.

![](https://i.imgur.com/NuiZih4.png)

8. Una vez esté bien escrito todo el código (y que sea en una sola línea), lo copiamos y pegamos en nuestro CMD previamente abierto.

9. Primero que nada, hacemos un `az login`, para verificar que nuestra cuenta está logeada con nuestro CLI o para logearnos en caso de no estarlo.

![](https://i.imgur.com/u1XqlUp.png)

10. Ahora si, después de eso, pegamos el código y presionamos *Enter*.

![](https://i.imgur.com/ShboAeJ.png)

Sabremos que nuestro código funcionó cuando entre todo el texto tenemos un mensaje como éste: `"provisioningState": "Succeeded"`

### 〔Comprobando implementación〕
Para verificar que nuestra implementación se hizo correctamente, vamos al portal.

1. Una vez en el portal de azure, buscamos nuestro *grupo de recursos*.

![](https://i.imgur.com/mVVgm1e.png)

2. Abrimos el que corresponde a la práctica.

![](https://i.imgur.com/xmtHbww.png)

3. Y ahora vemos en el apartado *Configuración*, y luego en *Implementaciones*.

![](https://i.imgur.com/EOkR0FP.png)

4. Podemos observar que aquí está la implementación hecha, hasta tiene el nombre que nosotros le asignamos **miPlantilla-P12**. Vemos que el estado es *Correcto*.

![](https://i.imgur.com/gQ7UvgI.png)

5. Si decidimos abrirlo, verá que nos dice *Se completó la implementación*.

![](https://i.imgur.com/ZfovfPP.png)

6. Y en el apartado *Plantillas*, podemos ver todo el código `Json` que se realizó e implementó.

![](https://i.imgur.com/exi1uay.png)

### 〔Implementando un recurso con nuestra plantilla〕
Hagamos algo más complejo, ahora si implementaremos un recurso de verdad de forma local.

Hay muchas formas de schemas para los diferentes recursos, solo basta con consultarlos en la documentación de Microsoft.

Por ahora, usaremos el schema que vemos para la creación de *Una cuenta de almacenamiento*.

1. Volviendo al código, trabajaremos dentro los Corchetes `[ ]`. Abrimos *llaves* `{ }`

- La `linea 6` se nos pide especificar que tipo de recurso estamos creando, el cual será un **Storage Account** de *Microsoft Storage*.

- Seguido de eso, en la `linea 7` elegiremos la versión de la API de las cuentas de almacenamiento (elegiremos la más reciente. Estos valores vienen por parte de Azure, no debemos preocuparnos por ellos).

- Después, `linea 8` asignamos un nombre a nuestra cuenta de almacenamiento.

- Luego, `linea 9`, la localización donde queremos que esté asentado nuestro recurso.

- Ahora, en `linea 10`, el *sku* es el *plan de uso* de nuestro recurso, o sea, si será básico o de pago.

- Y por último, `linea 13`, elegimos el tipo de almacenamiento, en este caso **StorageV2**.

- La siguiente linea es opcional, pero lo puse porque así viene en la práctica. Asignamos *propiedades* al recurso, y que tenga un protocolo de *Solo soportar tráfico HTTPS*.

![](https://i.imgur.com/HHo7mA8.png)

2. Guardamos el archivo.

3. Vamos al CMD y volvemos a escribir la misma línea de código que teniamos copiada previamente. Lo que hará el CLI será interpretar los cambios realizados en la plantilla para poder actualizarla en la nube, creando o eliminando los recursos si así lo requiere.

![](https://i.imgur.com/i8GsadW.png)
![](https://i.imgur.com/mlNb5vL.png)

De nueva cuenta, debemos esperar un `"provisioningState": "Succeeded"` para asegurarnos de que todo salió bien.

4. Refrescamos la página de nuestro *grupo de recursos*. Y podemos observar que ahora ya tenemos un recurso creado, la cuenta de almacenamiento (inclusive con el nombre asignado).

![](https://i.imgur.com/59r7ImK.png)

5. Revisamos el mismo apartado de Plantilla de nuestra implementación y podremos notar los cambios realizados por nosotros, que fueron hechos de forma local y ahora están en la nube.

![](https://i.imgur.com/tbUYRTa.png)

6. Para finalizar, podemos abrir el recurso en cuestión y verificar cada uno de los parámetros que fueron asignados, para comprobar que efectivamente es el mismo recurso que programamos en Visual Studio Code.

![](https://i.imgur.com/6mWilN3.png)