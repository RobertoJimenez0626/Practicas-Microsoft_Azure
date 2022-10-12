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

 - [Introducción a Azure Machine Learning](#introducción-a-azure-machine-learning)
    - [¿Para quién es Azure Machine Learning?](#para-quién-es-azure-machine-learning)
        - [Herramientas para desarrolladores](#herramientas-para-desarrolladores)
        - [Interfaz de usuario del Estudio](#interfaz-de-usuario-del-estudio)
    - [Flujo de trabajo del proyecto de aprendizaje automático](#flujo-de-trabajo-del-proyecto-de-aprendizaje-automático)
        - [Ciclo de vida del proyecto](#ciclo-de-vida-del-proyecto)
    - [Entrenamiento de modelos](#entrenamiento-de-modelos)
        - [Abierto e interoperable](#abierto-e-interoperable)
    - [MLOps: DevOps para aprendizaje automático](#mlops-devops-para-aprendizaje-automático)
        - [Ciclo de vida del modelo de ML](#ciclo-de-vida-del-modelo-de-ml)
        - [Integraciones que habilitan MLOP](#integraciones-que-habilitan-mlop)
- [Introducción a Azure Machine Learning Studio](#introducción-a-azure-machine-learning-studio)
    - [Creación de proyectos de aprendizaje automático](#creación-de-proyectos-de-aprendizaje-automático)
    - [Administración de activos y recursos](#administración-de-activos-y-recursos)
- [Practica 13](#practica-13-experimento-predictivo-con-ml-studio)
    - [Creando un Workspace](#creando-un-workspace)
    - [Ingreso de Datos](#ingreso-de-datos)
    - [Entrenamiento ML](#entrenamiento-ml)
    - [Métricas y gráficas](#métricas-y-gráficas)
    - [Implementando a servicio web y testeo](#implementando-a-servicio-web-y-testeo)

-------

# 【Introducción a Azure Machine Learning】

![](https://adatis.co.uk/wp-content/uploads/maxresdefault-e1569599198910.jpg)

*Azure Machine Learning* es un servicio en la nube que permite acelerar y administrar el ciclo de vida de los proyectos de aprendizaje automático. Los profesionales de aprendizaje automático, científicos de datos e ingenieros pueden usarlo en sus flujos de trabajo diarios: entrenamiento e implementación de modelos y administración de MLOps.

Puede crear un modelo en Azure Machine Learning o usar un modelo creado a partir de una plataforma de código abierto, como Pytorch, TensorFlow o Scikit-learn. Las herramientas de MLOps le ayudan a supervisar, volver a entrenar y volver a implementar modelos.

### 〔¿Para quién es Azure Machine Learning?〕
Azure Machine Learning es para individuos y equipos que implementan MLOps dentro de su organización para que los modelos de aprendizaje automático entren en producción en un entorno de producción seguro y auditable.

Los científicos de datos y los ingenieros de ML encontrarán herramientas para acelerar y automatizar sus flujos de trabajo diarios. Los desarrolladores de aplicaciones encontrarán herramientas para integrar modelos en aplicaciones o servicios. Los desarrolladores de plataformas encontrarán un sólido conjunto de herramientas, respaldado con API duraderas de Azure Resource Manager, para crear herramientas de ML avanzadas.

Las empresas que trabajan en la nube de Microsoft Azure encontrarán una seguridad conocida y el control de acceso basado en rol (RBAC) para la infraestructura. Puede configurar un proyecto para denegar el acceso a los datos protegidos y seleccionar operaciones.

#### 〔Herramientas para desarrolladores〕
Los desarrolladores encuentran interfaces conocidas en Azure Machine Learning, como las siguientes:

- SDK de Python
- API REST de Azure Resource Manager
- CLI v2

#### 〔Interfaz de usuario del Estudio〕
*Estudio de Azure Machine Learning* es una interfaz gráfica de usuario para un área de trabajo del proyecto. En el Estudio, puede hacer lo siguiente:

- Ver ejecuciones, métricas, registros, salidas, etc.
- Crear y editar cuadernos y archivos.
- Administrar recursos comunes, como:
    - Credenciales de datos
    - Proceso
    - Entornos
- Visualizar las métricas de ejecución, los resultados y los informes.
- Visualice las canalizaciones creadas a través de interfaces de desarrollador.
- Crear trabajos de AutoML.

Además, el diseñador tiene una interfaz de arrastrar y colocar en la que puede entrenar e implementar modelos.

### 〔Flujo de trabajo del proyecto de aprendizaje automático〕
Normalmente, los modelos se desarrollan como parte de un proyecto con varios objetivos. Los proyectos suelen implicar a más de una persona. Al experimentar con datos, algoritmos y modelos, el desarrollo es iterativo.

#### 〔Ciclo de vida del proyecto〕
Aunque el ciclo de vida del proyecto puede variar según el proyecto, a menudo tendrá el aspecto siguiente:

![](https://docs.microsoft.com/es-es/azure/machine-learning/media/overview-what-is-azure-machine-learning/overview-ml-development-lifecycle.png)

Un área de trabajo organiza un proyecto y permite la colaboración para muchos usuarios que trabajan con un objetivo común. Los usuarios de un área de trabajo pueden compartir fácilmente los resultados de sus ejecuciones de experimentación en la interfaz de usuario del Estudio o usar recursos con versiones para trabajos como entornos y referencias de almacenamiento.

Cuando un proyecto está listo para ponerse en marcha, el trabajo de los usuarios se puede automatizar en una canalización de aprendizaje automático y desencadenarse según una programación o una solicitud HTTPS.

Los modelos pueden implementarse en la solución de inferencia administrada, tanto en tiempo real como por lotes, lo que simplifica la administración de la infraestructura que suele ser necesaria para implementar los modelos.

### 〔Entrenamiento de modelos〕
En Azure Machine Learning, puede ejecutar el script de entrenamiento en la nube o crear un modelo desde cero. A menudo, los clientes incorporan modelos que han creado y entrenado en marcos de código abierto, a fin de ponerlos en marcha en la nube.

#### 〔Abierto e interoperable〕
Los científicos de datos pueden usar modelos en Azure Machine Learning que han creado en marcos comunes de Python, como:

- PyTorch
- TensorFlow
- scikit-learn
- XGBoost
- LightGBM

También se admiten otros lenguajes y marcos, como:

- R
- .NET

### 〔MLOps: DevOps para aprendizaje automático〕
DevOps para modelos de aprendizaje automático, a menudo denominados MLOps, es un proceso para desarrollar modelos para la fase de producción. El ciclo de vida de un modelo desde el entrenamiento hasta la implementación debe ser auditable si no se puede reproducir.

#### 〔Ciclo de vida del modelo de ML〕

![](https://docs.microsoft.com/es-es/azure/machine-learning/media/overview-what-is-azure-machine-learning/model-lifecycle.png)

#### 〔Integraciones que habilitan MLOP〕
Azure Machine Learning se ha creado teniendo en cuenta el ciclo de vida de los modelos. Incluso puede auditar una confirmación y un entorno específicos del ciclo de vida de los modelos.

Algunas características clave que habilitan MLOps incluyen:

- Integración de `git`
- Integración de MLflow
- Programación de la canalización de aprendizaje automático
- Integración de Azure Event Grid para desencadenadores personalizados
- Facilidad de uso con herramientas CI/CD, como Acciones de GitHub o Azure DevOps

Además, Azure Machine Learning incluye características para la supervisión y auditoría:

- Artefactos de trabajo, como instantáneas de código, registros y otras salidas
- Linaje entre trabajos y recursos, como contenedores, datos y recursos de proceso

--------------

# 【Introducción a Azure Machine Learning Studio】

![](https://i.imgur.com/65XKi1V.png)

### 〔Creación de proyectos de aprendizaje automático〕
Studio ofrece varias experiencias de creación en función del tipo de proyecto y el nivel de experiencia del usuario.

- **Blocs de notas**
Escriba y ejecute su propio código en servidores de Jupyter Notebook administrados que estén integrados directamente en Studio.

![](https://docs.microsoft.com/es-es/azure/machine-learning/media/overview-what-is-azure-ml-studio/notebooks.gif)

- **Diseñador de Azure Machine Learning**
Use el diseñador para entrenar e implementar modelos de Machine Learning sin necesidad de escribir código. Arrastre y coloque conjuntos de datos y componentes para crear canalizaciones de Machine Learning.

![](https://docs.microsoft.com/es-es/azure/machine-learning/media/concept-designer/designer-drag-and-drop.gif)

- **Interfaz de usuario de Automated Machine Learning**
Aprenda a crear experimentos de aprendizaje automático automatizado con una interfaz fácil de usar.

![](https://docs.microsoft.com/es-es/azure/machine-learning/media/overview-what-is-azure-ml-studio/azure-machine-learning-automated-ml-ui.jpg)

- **Etiquetado de datos**
Use el etiquetado de datos de Azure Machine Learning para coordinar eficazmente los proyectos de etiquetado de imágenes y de etiquetado de texto.

### 〔Administración de activos y recursos〕
Administre los recursos de aprendizaje automático directamente en el explorador. Los recursos se comparten en la misma área de trabajo entre el SDK y Studio para ofrecer una experiencia sin problemas. Use Studio para administrar:

- Modelos
- Conjuntos de datos
- Almacenes de datos
- Recursos de proceso
- Cuaderno
- Experimentos
- Registros de ejecución
- Procesos
- Puntos de conexión de canalización

Studio puede simplificar el modo en que se administran los recursos del área de trabajo incluso para desarrolladores experimentados.

--------------

# 【Practica 13: Experimento predictivo con ML Studio〕
En esta práctica vamos a trabajar con ML Studio, que, como ya se habló en la parte teórica, es un entorno donde podemos desarrollar y trabajar con aprendizaje automático.

Lo que haremos será crear un experimento el cual hará una predicción sobre el número de bicicletas que serán rentadas en determinado día, editando sus características y usando como "datos" un ejemplo de Microsoft en formato CSV de uso libre.

### 〔Creando un Workspace〕
Antes de nada, debemos ingresar a la página donde trabajaremos, la cual es diferente al portal de Azure. Nos dirigiremos al siguiente link de **[MLStudio](https://ml.azure.com/)**.

1. En primer lugar, seremos recibidos con varios mensajes de Azure, los cuales cerramos. Y para empezar debemos crear un Workspace (espacio de trabajo).

Podemos definir un *Workspace* como un pequeño grupo (como si fuese un grupo de recursos) en el cual haremos nuestra manipulación de inteligencia artificial.

![](https://i.imgur.com/tkweqGO.png)

2. Para crearlo, nos pedirá llenar ciertos parámetros. Un *nombre*, *suscripción*, *grupo de recursos* y *región*. Muy idéntico a crear un recurso/grupo de recursos.

![](https://i.imgur.com/09cQyHr.png)

Se empieza a procesar el Workspace.

![](https://i.imgur.com/mifbHEI.png)

3. Una vez terminado, hacemos clic al Workspace, y veremos una interfaz así.

![](https://i.imgur.com/GbeaQMo.png)

4. Hacemos clic en *Compute* y luego en *New*.

![](https://i.imgur.com/PyTuH0j.png)

5. Para que podamos empezar a hacer trabajos de IA, debemos crear una instancia o una "computadora" la cual hará todos los cálculos y acciones del entrenamiento de IA. Para eso, estamos creando esta *instancia* (que también podríamos decir que es una *Virtual Machine*).

6. Acompletamos los datos que necesita. *Nombre*, *localización* (aunque por defecto usa la del propio Workspace), nos hace decidir si usaremos *CPU o GPU* (depende de la potencia que requieras para el entrenamiento de IA), y por último, seleccionar el *tamaño* de nuestra máquina virtual.

![](https://i.imgur.com/tDuug13.png)
![](https://i.imgur.com/HP24lUA.png)

7. Clic en *Crear*.

![](https://i.imgur.com/hV7YRdw.png)

8. Esperamos a que el estado (state) pase de *Creating* a *Completed*

![](https://i.imgur.com/8QY1w1K.png)

### 〔Ingreso de Datos〕
Para entrenar el aprendizaje automático, debemos proporcionarle datos de "base" para que empiece a calcular y de ahí aprenda a predecir un posible resultado futuro.

1. Vamos al apartado de *Assets* y luego en *Data* (datos).

![](https://i.imgur.com/bSyFwW3.png)

2. Hacemos clic en *Create*. Luego se nos desplegará unas opciones para elegir de donde tomaremos los datos, en nuestro caso, será mediante *Web files*.

![](https://i.imgur.com/1HAfvUN.png)

3. Aquí podemos ver el archivo que usaremos. Tiene muchos datos clasificados en columnas, tales como dia, mes, año, estación, temperatura inicial, temperatura final, velocidad del viento, y rentas (el valor más importante, luego trabajaremos con él).

![](https://i.imgur.com/dg3un56.png)

4. El archivo que vimos antes está alojado en una página web de Microsoft, cuyo *link* es el que vemos en la siguiente imagen, de ahí extraeremos la información. Seguido, asignamos un *nombre*, el *tipo de datos* y una *descripción*.

![](https://i.imgur.com/8JayQfH.png)

5. Después de llenar los datos, clic en *Next*.

6. Ahora, debemos decirle el formato que tiene nuestro documento, el cual es CSV, que se caracteriza por tener sus datos separados por **Comas**. En cabecera de columnas, elegiremos *Solo el primer archivo tiene cabeceras*. Después, clic en *Next*.

![](https://i.imgur.com/USOGfok.png)

7. Aquí podemos ver un Esquima de todas las columnas que se determinaron a partir de nuestro documento. Podemos *activar* o *desactivar* a nuestra conveniencia, en mi caso, todo estará activo.

![](https://i.imgur.com/DUiHcs2.png)

8. Clic en *Next*.

9. Finalmente podemos ver una pantalla con los datos que proporcionamos para verificar que no hay ningún error y estamos conformes.

![](https://i.imgur.com/1MrLD6P.png)

10. Clic en el botón *Create*.

![](https://i.imgur.com/nVBCCdC.png)

### 〔Entrenamiento ML〕
Ahora empezaremos el entrenamiento del aprendizaje automático (Automated ML job).

1. Vamos a la sección *Author* y luego en *Automated ML*. Clic en *New Automated ML job*.

![](https://i.imgur.com/lFWu6Wa.png)

2. De primeras, nos pedirá elegir los datos que usaremos para el entrenamiento, por eso es que hicimos el tema anterior, para crear los *Assets de datos* y que puedan ser utilizados en este apartado. Elegiremos nuestro Asset **RentaBicis-P13**.

![](https://i.imgur.com/J4MXokP.png)

3. Clic en *Next*.

4. Ahora, crearemos un experimento. Un experimento es un conjunto de pruebas y cálculos que se realizan, y como el ML aprende de ellas.

5. Colocamos un *nombre*, y seleccionaremos la *columna objetivo* la cual será "Rentals", con esto le decimos a la IA que aprenda a sacar los valores **Rentas** usando los valores de la fila donde correspondan al valor a predecir.

![](https://i.imgur.com/fU5sb4s.png)

6. Después, elegiremos una *instancia Clúster*. Como no tenemos ninguna, crearemos una con el botón *New*.

7. De la misma forma a la anterior, elegimos los valores que nos convengan para la tarea que realizaremos. En mi caso elegí el tamaño más pequeño ya que no será un trabajo muy demandante.

![](https://i.imgur.com/oeyZWP4.png)

Usualmente aquí se nos permitirá modificar más los datos, pero por ser una VM de muy pocos recursos, no nos deja, así que ponemos todo por defecto.

![](https://i.imgur.com/Fa21QKg.png)

8. Clic en *Create*.

![](https://i.imgur.com/95DQZaf.png)

9. Una vez seleccionado el Clúster, clic en *Next*.

![](https://i.imgur.com/5GatbJs.png)

10. Aquí debemos decidir que tipo de experimento será el que se entrene. Para esta práctica, estamos haciendo una predicción de secuencia de números, y la que va más acorde a ella es *Regression*. Clic en *Next*.

![](https://i.imgur.com/o4qxmeF.png)

11. Dejamos por defecto, y clic en *Finish*.

![](https://i.imgur.com/WQApWZz.png)

12. Y esperamos a que termine de crear el recurso.

![](https://i.imgur.com/NKZjo2W.png)

### 〔Métricas y gráficas〕
Una vez terminado, ML empezará a trabajar por si solo, hará el experimento y sus pruebas hasta que pueda generar un *modelo* listo para ser empleado en lo que nosotros queramos.

Estado: **Inactivo**
![](https://i.imgur.com/WVAytZC.png)

Estado: **En ejecución**
![](https://i.imgur.com/ObINTHF.png)

Estado: **Completado**
![](https://i.imgur.com/8gCEvs8.png)

> ¡Este proceso podría durar desde **15 minutos** hasta **1 hora**!

1. Una vez terminado, nos dirigimos al recuadro de *Best model summary*, y clic en *VotingEnsamble* para ver el algoritmo que se creó en base al experimento.

![](https://i.imgur.com/pSLgGb1.png)

2. Aquí podemos apreciar una amplia gama de opciones, en las cuales nos importan las métricas, los cuales son algunos resultados tras el experimento, como *Varianza*, *Media*, *Mediana*, *Error*, *Predicción* y *Puntaje*, entre otras. La mayoría de estos resultados satisfacen a los científicos de datos, ya que ellos saben a profundidad como operar dichos valores.

![](https://i.imgur.com/dSYYDpI.png)

3. También podemos apreciar visualmente como fueron los resultados con gráficas a detalle del proceso y sus valores.

![](https://i.imgur.com/vskmrDk.png)
![](https://i.imgur.com/3MBUjgt.png)

### 〔Implementando a servicio web y testeo〕
Nos dirigimos al apartado de *Model*. Aquí nosotros podemos generar un modelo apartir de los resultados. Recordemos que un modelo, es la secuencia de operaciones o acciones que el ML realizó y aprendió. De lo aprendido se puede generar código de programación para que pueda ser replicado en donde nosotros queramos.

1. Una vez en *model*, hacemos clic en *Deploy* (implementar), y luego seleccionamos la que necesitemos, en mi caso será *Implementar a servicio Web*.

![](https://i.imgur.com/K3ONUBU.png)

2. Asignamos un *nombre*, *descripción*, habilitamos la *autenticación*. Luego, hacemos clic en *Deploy*.

![](https://i.imgur.com/qizSB7N.png)
![](https://i.imgur.com/gti6EiM.png)

> Esta operación de implementación y generación de código también **tardará un rato**.

![](https://i.imgur.com/vvucTUd.png)

3. Una vez terminada, nos dirigimos a *Test*. Ahora si tenemos nuestro código, el cual ya podemos manipular.

![](https://i.imgur.com/3BkB5im.png)

4. Para hacer la prueba, debemos **modificar** los valores por defecto que viene en el código con los valores que nosotros queramos. Damos clic en *Test*.

Si no nos indica ningún error, el proceso se realizó con éxito.

![](https://i.imgur.com/w0a9zUW.png)

5. Y aquí tenemos nuestro resultado. De todo lo aprendido, el ML predice que el día de **hoy 8 de agosto del 2022** se rentarán un total de **414 bicicletas**

![](https://i.imgur.com/nI76j8q.png)

En el apartado de *Consume*, tenemos una interfaz muy parecida, con la diferencia que podremos elegir a qué lenguaje queremos exportar nuestro código, entre ellos tenemos *Python*, *C#* y *R*.