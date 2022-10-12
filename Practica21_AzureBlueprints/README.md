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

- [Introducción a Azure Blueprint](#introducción-a-azure-blueprint)
  - [¿En qué se diferencia de las plantillas de Resource Manager?](#en-qué-se-diferencia-de-las-plantillas-de-resource-manager)
  - [¿En qué difiere de Azure Policy?](#en-qué-difiere-de-azure-policy)
  - [Definición del plano técnico](#definición-del-plano-técnico)
  - [Ubicaciones de definición de plano técnico](#ubicaciones-de-definición-de-plano-técnico)
  - [Parámetros de plano técnico](#parámetros-de-plano-técnico)
  - [Asignación de plano técnico](#asignación-de-plano-técnico)
  - [Permisos de Azure Blueprint](#permisos-de-azure-blueprint)
- [Practica 21](#practica-21-uso-de-azure-blueprints)
  - [Creando un Plano Técnico](#creando-un-plano-técnico)
  - [Prueba de directiva en Plano Técnico](#prueba-de-directiva-en-plano-técnico)

---

# 【Introducción a Azure Blueprint】

![](https://docs.microsoft.com/answers/topics/25501/icon.html?t=282208)

Del mismo modo que un plano técnico permite a un ingeniero o a un arquitecto bosquejar los parámetros de diseño de un proyecto, _Azure Blueprint_ permite a los grupos de arquitectos de la nube y de TI central definir un conjunto repetible de recursos de Azure que implementa y cumple los estándares de la organización, sus requisitos y sus patrones. Azure Blueprints permite a los equipos de desarrollo compilar e iniciar rápidamente nuevos entornos sabiendo que se compilan cumpliendo los estándares organizativos y que contienen un conjunto de componentes integrados, como las redes, para acelerar el desarrollo y la entrega.

Los planos técnicos son una manera declarativa de organizar la implementación de varias plantillas de recursos y de otros artefactos, como son:

- Asignaciones de roles
- Asignaciones de directiva
- Plantillas de Azure Resource Manager (plantillas de ARM)
- Grupos de recursos

El servicio Azure Blueprints está respaldado por la distribución global Azure Cosmos DB. Los objetos de plano técnico se replican en varias regiones de Azure. Esta replicación proporciona baja latencia, alta disponibilidad y acceso coherente a los objetos de plano técnico, con independencia de la región en la que Azure Blueprints implemente el recurso.

### 〔¿En qué se diferencia de las plantillas de Resource Manager?〕

El servicio está diseñado para ayudar con la configuración del entorno. A menudo, esta configuración consta de un conjunto de grupos de recursos, directivas, asignaciones de roles e implementaciones de plantillas de Resource Manager. Un plano técnico es un paquete para reunir todos estos tipos de artefacto y permite componer y crear la versión del paquete, incluso mediante una canalización de integración continua y entrega continua (CI/CD). En última instancia, cada uno se asigna a una suscripción en una única operación que se puede auditar y seguir.

Casi todo lo que desee incluir para la implementación en Azure Blueprints se puede conseguir con una plantilla de Resource Manager. Sin embargo, una plantilla de Resource Manager es un documento que no existe de forma nativa en Azure, cada una se almacena localmente, en el control de código fuente o en Plantillas (versión preliminar). La plantilla se usa para las implementaciones de uno o varios recursos de Azure pero, una vez implementados los recursos, no hay conexión activa ni relación con la plantilla.

Con Azure Blueprints, la relación entre la definición del plano técnico (lo que debe ser implementado) y su asignación (lo que se ha implementado) permanece. Esta conexión permite un seguimiento mejorado y la auditoría de las implementaciones. Azure Blueprints también puede actualizar varias suscripciones a la vez que se rigen por el mismo plano técnico.

No es preciso elegir entre una plantilla de Resource Manager y un plano técnico. Cada plano técnico puede tener cero o más artefactos de una plantilla de Resource Manager. Esta compatibilidad significa que se pueden reutilizar los trabajos anteriores para desarrollar y mantener una biblioteca de plantillas de Resource Manager en Azure Blueprints.

### 〔¿En qué difiere de Azure Policy?〕

Un plano técnico es un paquete o contenedor para crear conjuntos muy específicos de estándares, patrones y requisitos relacionados con la implementación de los servicios en la nube de Azure, la seguridad y el diseño que se pueden reutilizar para garantizar la coherencia y el cumplimiento normativo.

Una directiva es un sistema de denegación explícita y permisos predeterminados que se centra en las propiedades de recursos durante su implementación y para los recursos ya existentes. Admite la gobernanza de la nube al validar que los recursos de una suscripción cumplen los requisitos y estándares.

La inclusión de una directiva en un plano técnico permite crear el patrón o diseño adecuado durante la asignación del plano. La inclusión de la directiva garantiza que solo se pueden realizar en el entorno cambios aprobados o esperados para proteger el cumplimiento continuo en el ámbito del plano técnico.

Se puede incluir una directiva como uno de muchos artefactos en una definición de plano técnico. Los planos técnicos también permiten usar parámetros con las directivas y las iniciativas.

### 〔Definición del plano técnico〕

Un plano técnico se compone de artefactos. Azure Blueprints admite actualmente los siguientes recursos como artefactos:

| Resource                | Opciones de la jerarquía       | Descripción                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Grupos de recursos      | Suscripción                    | Cree un nuevo grupo de recursos para que lo usen otros artefactos incluidos en el plano técnico. Estos grupos de recursos de marcador de posición permiten organizar los recursos exactamente como desee que se estructuren y proporciona un limitador de ámbito para los artefactos de asignación de roles y directivas, así como plantillas de Resource Manager. |
| Plantilla ARM           | Suscripción, grupo de recursos | Las plantillas, incluidas las plantillas anidadas y vinculadas, se usan para crear entornos complejos. Ejemplo de entornos: una granja de servidores SharePoint, Azure Automation State Configuration o un área de trabajo de Log Analytics.                                                                                                                       |
| Asignación de directiva | Suscripción, grupo de recursos | Permite la asignación de una directiva o iniciativa a la suscripción a la que está asignado el plano técnico. La directiva o iniciativa debe estar dentro del ámbito de la ubicación de la definición del plano técnico. Si la directiva o iniciativa tiene parámetros, estos se asignan en la creación del plano técnico o durante su asignación.                 |
| Asignación de roles     | Suscripción, grupo de recursos | Agregue un grupo o usuario existente a un rol integrado para asegurarse de que las personas adecuadas siempre tienen derechos de acceso a los recursos. Las asignaciones de roles se pueden definir para toda la suscripción o anidarse para un grupo de recursos específico incluido en el plano técnico.                                                         |

> ⚠️ **Nota**
> Cada artefacto debe tener 2 MB o menos. Si el artefacto supera este valor, se producirá un error HTTP 500 (error interno del servidor).

### 〔Ubicaciones de definición de plano técnico〕

Al crear una definición de plano técnico, definirá dónde se guarda. Los planos técnicos se pueden guardar en un grupo de administración o suscripción a los que tenga acceso de colaborador. Si la ubicación es un grupo de administración, el plano técnico está disponible para asignarlo a cualquier suscripción secundaria de ese grupo de administración.

### 〔Parámetros de plano técnico〕

Los planos técnicos pueden pasar parámetros a una iniciativa o directiva, o bien a una plantilla de Resource Manager. Cuando algún artefacto se agrega a un plano técnico, el autor es capaz de decidir si proporcionar un valor definido para cada asignación de plano técnico o permitir que cada asignación del plano técnico proporcione un valor en el momento de la asignación. Esta flexibilidad permite definir un valor predeterminado para todos los usos del plano técnico o que esa decisión se tome en el momento de la asignación.

> ⚠️ **Nota**
> Un plano técnico puede tener sus propios parámetros, pero actualmente solo se pueden crear si el plano técnico se genera desde la API REST en lugar de mediante el Portal.

### 〔Asignación de plano técnico〕

Cada **versión publicada** de un plano técnico (con una longitud máxima del nombre de 90 caracteres) se puede asignar a un grupo de administración o una suscripción existentes. En el portal, el plano técnico tiene de forma predeterminada la **versión publicada** más recientemente. Si hay parámetros de artefacto o parámetros de plano técnico, se definirán durante el proceso de asignación.

> ⚠️ **Nota**
> Asignar una definición de plano técnico a un grupo de administración significa que el objeto de asignación existe en el grupo de administración. La implementación de artefactos sigue teniendo como destino una suscripción. Para realizar una asignación de grupo de administración, se debe usar la **API REST para crear o actualizar** y el cuerpo de la solicitud debe incluir un valor para `properties.scope` para definir la suscripción de destino.

### 〔Permisos de Azure Blueprint〕

Para poder utilizar planos técnicos, se le deben conceder permisos mediante el control de acceso basado en rol de Azure (Azure RBAC). Para leer o ver un plano técnico en Azure Portal, la cuenta debe tener acceso de lectura al ámbito en que se encuentra la definición del mismo.

Para crear planos técnicos, su cuenta necesita los siguientes permisos:

- `Microsoft.Blueprint/blueprints/write`: para crear una definición de plano técnico
- `Microsoft.Blueprint/blueprints/artifacts/write`: para crear artefactos en una definición de plano técnico
- `Microsoft.Blueprint/blueprints/versions/write`: para publicar un plano técnico

Para eliminar planos técnicos, su cuenta necesita los siguientes permisos:

- `Microsoft.Blueprint/blueprints/delete`
- `Microsoft.Blueprint/blueprints/artifacts/delete`
- `Microsoft.Blueprint/blueprints/versions/delete`

> ⚠️ **Nota**
> Los permisos de definición de plano técnico deben ser concedidos o heredados en el ámbito de la suscripción o grupo de administración donde se guarda.

Para asignar o cancelar la asignación de un plano técnico, la cuenta necesita los siguientes permisos:

- `Microsoft.Blueprint/blueprintAssignments/write`: para asignar un plano técnico
- `Microsoft.Blueprint/blueprintAssignments/delete`: para cancelar la asignación de un plano técnico

> ⚠️ **Nota**
> Como las asignaciones de planos técnicos se crean en una suscripción, los permisos de asignación y de cancelación de la asignación deben concederse o heredarse en el ámbito de una suscripción.

Están disponibles los siguientes roles integrados:

| Rol de Azure                 | Descripción                                                                                                                                                                                 |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Propietario                  | Además de otros permisos, incluye todos los permisos relacionados con Azure Blueprints.                                                                                                     |
| Colaborador                  | Además de otros permisos, puede crear y eliminar definiciones de planos técnicos, pero no tiene permisos para asignarlos.                                                                   |
| Colaborador de plano técnico | Puede administrar las definiciones del plano técnico, pero no asignarlas.                                                                                                                   |
| Operador del plano técnico   | Puede asignar los planos técnicos publicados existentes, pero no puede crear nuevos. Las asignaciones solo funcionan si se realizan con una identidad administrada asignada por el usuario. |

Si estos roles integrados no satisfacen sus necesidades de seguridad, considere la posibilidad de crear un rol personalizado.

> ⚠️ **Nota**
> Si usa una identidad administrada asignada por el sistema, la entidad de servicio para Azure Blueprints requiere el rol **Propietario** en la suscripción asignada con el fin de habilitar la implementación. Si usa el portal, este rol se le concede automáticamente y se revoca para la implementación. Si usa la API REST, este rol se debe conceder manualmente, pero se sigue revocando de forma automática una vez finalizada la implementación. Si usa una identidad administrada asignada por el usuario, solo el usuario que crea la asignación de planos necesita el permiso `Microsoft.Blueprint/blueprintAssignments/write`, que se incluye en los roles integrados **Propietario** y **Operador de planos**.

---

# 【Practica 21: Uso de Azure Blueprints〕

### 〔Creando un Plano Técnico〕

Muy similar a las _Plantillas ARM_, aquí tenemos que crear poco a poco una "plantilla" de iniciativas y directivas las cuales serán implementadas en un ámbito (el cual será nuestra suscripción).

Por lo tanto, toda la suscripción heredará ese conjunto de reglas, y, por ende, todos los recursos deberán cumplirlas para su creación.

1. Buscamos _Planos técnicos_. Y seleccionamos el primer resultado que nos aparezca.

![](https://i.imgur.com/XyRzNlr.png)

2. Aquí tenemos la interfaz de Planos técnicos, lo primero que hay que hacer es crear uno. Vamos a hacer clic en _Definiciones de planos técnicos_.

![](https://i.imgur.com/DLF44Gi.png)

3. Clic en _Crear plano técnico_.

![](https://i.imgur.com/2rF5iqx.png)

4. Azure ya tiene planos prefabricados para diferentes tipos de situaciones que lo requiera una solución de nube. Hay desde cumplimiento de normas ISO hasta cumplimiento de normas gubernamentales.

5. Yo elegí usar un plano para la Norma ISO 27001.

![](https://i.imgur.com/NKlPUvf.png)

6. Ponemos un _nombre_, y elegimos la _ubicación_ a donde se aplicará el plano (nuestra suscripción).

![](https://i.imgur.com/yDioJks.png)

7. Vamos al apartado _Artefactos_.

![](https://i.imgur.com/SyQUMze.png)

8. Aquí podemos ver el conjunto de directivas que se asignarán al implementar este plano técnico a toda nuestra suscripción (en otras palabras, todas estas reglas se aplicarán a nuestra suscripción).

![](https://i.imgur.com/ASQAT8L.png)

9. Clic en _Guardar borrador_.

10. Hacemos clic en el nombre del plano.

![](https://i.imgur.com/L1bKS1B.png)

11. Una vez dentro, hacemos clic en _Publicar plano técnico_.

![](https://i.imgur.com/M61XVIu.png)

12. Ajustamos el número de versión (en mi caso, 1.0), seguido de unas notas sobre este plano.

![](https://i.imgur.com/UtrTu0P.png)

13. Clic en _Publicar_. Y esperamos a que se publique correctamente.

![](https://i.imgur.com/n1lgqHd.png)

14. Hacemos clic en _Asignar plano técnico_.

![](https://i.imgur.com/Gu86wyT.png)

15. Le ponemos _nombre_, _región_ y _número de versión_.

![](https://i.imgur.com/Z4ev9bt.png)

16. Dejamos lo demás por defecto.

![](https://i.imgur.com/em9IMhY.png)

17. Y aquí tenemos un panorama amplio de todos aquellos parámetros que podemos definir en la creación del plano, por ejemplo, número de máquinas virtuales permitidas, regiones accesibles, etc.

![](https://i.imgur.com/puOSYxA.png)

18. Damos clic en _Asignar_.

![](https://i.imgur.com/IJtBMwU.png)

Nosotros también podemos crear nuestro propio plano técnico desde 0. Haremos uno que cumpla la misma función que la práctica pasada, nuestros recursos solo pueden ser creados dentro de USA.

1. Vamos a _Definiciones del plano técnico_ y luego hacemos clic en el botón _Crear plano técnico_.

![](https://i.imgur.com/pqYPbQL.png)

2. Damos clic en _Empezar con un plano técnico en blanco_.

![](https://i.imgur.com/SgmwnnU.png)

3. Asignamos un _nombre_ y la _ubicación_ de definición.

![](https://i.imgur.com/l670D4T.png)

4. Nos vamos al apartado _Artefactos_. Hacemos clic en _Agregar artefacto_, aquí tenemos que especificar que tipo de artefacto será, en este caso, una _Asignación de directiva_.

![](https://i.imgur.com/pyzHDFc.png)

5. Vamos a buscar la directiva _ubicaciones permitidas_ (la misma que hemos estado usando en las últimas prácticas). Clic en _Agregar_.

![](https://i.imgur.com/IkLmH4S.png)

6. Luego de agregarlo, clic en _Guardar borrador_.

![](https://i.imgur.com/KfP4Xe0.png)

7. Nos regresamos a _Definiciones del plano técnico_ e ingresamos a nuestro borrador creado.

![](https://i.imgur.com/Uqf0a36.png)

8. Una vez dentro, hacemos clic en el botón _Publicar plano técnico_.

![](https://i.imgur.com/ovkJOIJ.png)

9. Especificamos la _versión_ y unas _notas_ con información (opcional). Después, hacemos clic en _Publicar_.

![](https://i.imgur.com/rlYKSof.png)

10. Cuando termine de publicarse, vamos a darle al botón _Asignar plano técnico_.

![](https://i.imgur.com/AegE3lR.png)

11. Aquí vamos a asignar este plano a nuestra suscripción y después se empezarán a aplicar todas las directivas que hayamos especificado dentro del plano.

![](https://i.imgur.com/LVqiwoq.png)

12. Bajando el scroll, tenemos que configurar los parámetros de los artefactos. Como nosotros elegimos _Ubicaciones permitidas_, debemos especificar en que ubicaciones se podrán crear nuestros recursos (y las que no estén seleccionadas, estarán prohibidas).

![](https://i.imgur.com/Bd5aEgw.png)

13. Finalmente, clic en _Asignar_.

![](https://i.imgur.com/eUbsPCm.png)
![](https://i.imgur.com/IO2RbYi.png)

14. Podemos comprobar que se asignó correctamente si nos dirigimos al apartado _Planos técnicos asignados_.

![](https://i.imgur.com/hRqRy5i.png)
![](https://i.imgur.com/DlQXK2V.png)

### 〔Prueba de directiva en Plano Técnico〕

Ahora, probaremos nuestro plano creando un recurso que vaya en contra de la directiva, para ver si es capaz de crearse o nos arroja un error.

1. En mi caso, crearé un _App Service_. Buscamos eso en nuestra barra de navegación.

![](https://i.imgur.com/odvWbeO.png)

2. Clic al botón _Crear_.

![](https://i.imgur.com/KomNKlM.png)

3. Rellenamos los parámetros solicitados. Recordemos que nuestra directiva no admite recursos creados en regiones fuera de USA, y nosotros estamos especificando que queremos nuestro App Service en _Japan East_.

![](https://i.imgur.com/qEJdlVY.png)

4. Seleccionamos el plan que queramos. Clic en _Revisar y crear_.

![](https://i.imgur.com/zzDyy0j.png)

5. Después, clic en _Crear_.

![](https://i.imgur.com/zkzBaMD.png)

Aquí podemos apreciar que nos arrojó un texto super largo y muy extraño. Pero, para ser más claros, vamos a hacerle clic.

![](https://i.imgur.com/lKU97cg.png)

Los detalles del error fueron causados por la _Directiva: Ubicaciones permitidas_. Por eso se nos impidió crear el App Service en Japón, porque es una región fuera de USA.

![](https://i.imgur.com/4GUohry.png)

Y si vamos al apartado de _Directiva_ y en _Cumplimiento_, podemos ver las incompatibilidades que hubieron (en este caso, la que ocurrió hace poco es la segunda que aparece en la lista).

![](https://i.imgur.com/Sqg9nfr.png)
