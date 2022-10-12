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
- [Practica 14](#practica-14-reconocimiento-facial-con-face-api)
    - [Creando un Notebook](#creando-un-notebook)
        - [Creando una Instancia de Computo](#creando-una-instancia-de-computo)
    - [Código de reconocimiento facial](#código-de-reconocimiento-facial)
    - [Implementación de Face API](#implementación-de-face-api)
    - [Resultado final](#resultado-final)

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

# 【Practica 14: Reconocimiento facial con Face API〕
Para esta práctica vamos a volver a usar el portal de *Machine Learning Studio*. Debemos crear un Workspace (como vimos en la práctica anterior), pero ahora con un nombre diferente, en este caso yo le puse **miWorkspace-P14**. El grupo de recursos **Practica14_Darki** y localizado en *Australia East*.

![](https://i.imgur.com/3OhoJ4R.png)

Damos clic en el botón *Create* y esperamos a que se termine de procesar.

![](https://i.imgur.com/zrH9S5A.png)

### 〔Creando un Notebook〕
Ahora, usaremos una nueva herramienta integrada en ML Studio, los *Notebooks*. 

Podemos describirlos como *entornos de desarrollo en la nube* sin necesidad de programas externos. Con ellos, somos capaces de programar en diferentes lenguajes, tales como *Python*, *R*, *C#*, etc.

1. Vamos al apartado *Author* y luego seleccionamos *Notebooks*.

![](https://i.imgur.com/9uj7YOK.png)

2. Para crear uno, damos clic en el botón `+`. Luego, seleccionamos *Crear un nuevo archivo*.

![](https://i.imgur.com/vTb5Wpv.png)

3. Lo que necesitamos para crear un notebook es un *nombre* y el *tipo* de archivo que será. Le puse **miNotebook-P14** y lo dejé con el tipo de archivo por defecto.

![](https://i.imgur.com/iTXLYvn.png)

4. Luego, clic en *Create*.

![](https://i.imgur.com/fWxNELc.png)

5. Una vez abierto, podremos ver que ya tenemos un espacio para implementar código como si fuese un entorno de desarrollo cualquiera.

![](https://i.imgur.com/a8mpNme.png)

#### 〔Creando una Instancia de Computo〕
Pero para empezar a ejecutar código, el notebook nos manda una alerta de que no tenemos algo que ejecute dicho código, no tenemos una computadora por decirlo así. Por ende, se nos solicita crear una *Instancia de Computo* (o bien, una Máquina Virtual), para que podamos ejecutar nuestro archivo.

1. Para hacerlo, hacemos clic en los *tres puntitos*, y luego  clic en *Create Azure ML compute instance*.

![](https://i.imgur.com/SZzfuWx.png)

2. Se nos mostrará una pantalla de creación como la de la práctica anterior. Rellenamos los campos necesarios, *nombre*, *localización (por defecto)*, *CPU* y *tamaño*.

![](https://i.imgur.com/YcLcU86.png)

3. Luego, hacemos clic en *Create*.

![](https://i.imgur.com/XP2yftt.png)

### 〔Código de reconocimiento facial〕
Vamos a extraer de un repositorio en GitHub el código Python del reconocimiento facial, el cual implementaremos a nuestro Notebook. (El notebook interpreta Python)

1. Nos dirigiremos a la **[página](https://github.com/josejesusguzman/face-api-consumption-python)** que vemos en la barra de navegación. Y hacemos clic en el hipervinculo **[Código de Python explicado](https://github.com/josejesusguzman/face-api-consumption-python/blob/main/face-consumption.py)**.

![](https://i.imgur.com/GnTtxJt.png)

2. Una vez estando aquí, veremos el código de programación que hará todas las funciones que necesitamos para que, cuando nosotros ingresamos una imagen, nos identifique la *edad*, *genero*, *si lleva lentes* y la *emoción*.

![](https://i.imgur.com/4EZrfZQ.png)

3. Hacemos clic en *Raw*.

4. Nos dejará en una ventana como ésta.

![](https://i.imgur.com/SqSqTSz.png)

5. Ahora, solo resta seleccionar todo, y copiarlo. (Luego lo usaremos)

![](https://i.imgur.com/PkZeUTx.png)

### 〔Implementación de Face API〕
Pero, para que el código Python pueda ser usado, necesitamos de lo siguiente:

```python
# Obtener el API KEY de la aplicación
subscription_key = "AQUÍ_PONES_TU_CLAVE_DEL_RECURSO_DE_AZURE"

# Obtener el endpoint de la aplicación
face_api_url = "AQUÍ_PONES_TU_URL_DESTINO_DEL_RECURSO_DE_AZURE" + '/face/v1.0/detect'

image_url = 'AQUÍ_PONES_TU_IMAGEN'
# Imagen de prueba: https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg
```

Estos son parámetros que nosotros debemos proporcionarle a la programación para que entienda que ésta usando como lector facial. Entonces, el *API Key* es la **contraseña** del recurso de reconocimiento facial, la *API URL* es el **punto de conexión** al cual se ajustará el programa para usar el recurso, y por último el *Image URL* es la **dirección url de la imagen** que se usará para analizar.

Es necesario crear el recurso Face API para obtener los valores que utilizaremos.

1. En la barra de navegación, escribimos *Face API* o *API de Face*, y hacemos clic en el resultado.

![](https://i.imgur.com/zSrUnUT.png)

2. Clic en el botón *Crear*.

![](https://i.imgur.com/R5ZcYCd.png)

3. Y rellenamos los datos necesarios, procurando usar el plan *Free F0* (que es el plan gratuito)

![](https://i.imgur.com/Czv1mIS.png)

4. Clic en *Revisar y crear*.

5. Y luego clic en *Crear*.

![](https://i.imgur.com/sNngH8L.png)

6. Esperamos a que se implemente correctamente.

7. Hacemos clic en *Ir al recurso*.

![](https://i.imgur.com/5pL55x8.png)

8. Nos dirigimos al apartado *Administración de recursos*, y luego en *Claves y punto de conexión*.

Aquí tenemos los valores que necesitamos copiar y reemplazar en las partes del código que ya hemos visto.

![](https://i.imgur.com/BsP2hKC.png)

![](https://i.imgur.com/gHEwPr6.png)

### 〔Resultado final〕
Y como resultado tendremos algo parecido a esto, ya con los valores de las *claves* y el *punto de conexión* ajustados correctamente.

Podemos darnos cuenta que ya está usando nuestra *Instancia* previamente creada y en estado *Running*. Empleamos *Python 3.8* de *Azure ML*.

Ahora, solo damos clic al botón de la izquierda del recuadro *Play*.

![](https://i.imgur.com/AQ9mqdI.png)

El resultado resultó satisfactorio. La imagen fue capturada y analizada. Además, se nos desplegaron los parámetros interpretados por la IA: *la edad, el genero, inclusive la emoción que tiene la persona*.

![](https://i.imgur.com/GasGVx5.jpg)