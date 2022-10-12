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

 - [Introducción a Azure Advisor](#introducción-a-azure-advisor)
    - [¿Cómo se accede a Advisor?](#cómo-se-accede-a-advisor)
    - [¿Qué permisos son necesarios para acceder a Advisor?](#qué-permisos-son-necesarios-para-acceder-a-advisor)
    - [¿Para qué recursos Advisor ofrece recomendaciones?](#para-qué-recursos-advisor-ofrece-recomendaciones)
    - [¿Se puede posponer o descartar una recomendación?](#se-puede-posponer-o-descartar-una-recomendación)
- [Practica 11](#practica-11-uso-de-azure-advisor)
    - [Creando un grupo de recursos](#creando-un-grupo-de-recursos)
    - [Azure Advisor y su interfaz](#azure-advisor-y-su-interfaz)
    - [Creando alertas de Advisor](#creando-alertas-de-advisor)

-------

# 【Introducción a Azure Advisor】

![](https://adinermie.com/wp-content/uploads/2018/05/Azure-Advisor-Logo.png)

*Azure Advisor* es un consultor personalizado en la nube que lo ayuda a seguir procedimientos recomendados para optimizar las implementaciones de Azure. Analiza la configuración de recursos y la telemetría de uso, y recomienda soluciones que pueden ayudar a mejorar la rentabilidad, el rendimiento, la confiabilidad (antes conocida como alta disponibilidad) y la seguridad de los recursos de Azure.

Con Advisor, puede:

- Obtener sugerencias de procedimientos recomendados proactivas, prácticas y personalizadas,
- Mejorar el rendimiento, la seguridad y la confiabilidad de los recursos, al mismo tiempo que identifica oportunidades para reducir el gasto general de Azure, y
- Obtener recomendaciones con acciones propuestas en línea.

El panel de Advisor muestra recomendaciones personalizadas para todas las suscripciones. Puede aplicar filtros para mostrar las recomendaciones para determinadas suscripciones y tipos de recursos. Las recomendaciones se dividen en cinco categorías:

- Confiabilidad (anteriormente denominada alta disponibilidad) : para garantizar y mejorar la continuidad de las aplicaciones empresariales críticas. Para obtener más información, consulte las recomendaciones de confiabilidad de Advisor.

- Seguridad: ayuda a detectar amenazas y vulnerabilidades que podrían dar lugar a infracciones de seguridad. Para obtener más información, consulte las recomendaciones sobre seguridad de Advisor.

- Rendimiento: ayuda a mejorar la velocidad de las aplicaciones. Para obtener más información, consulte las recomendaciones sobre rendimiento de Advisor.

- Costo: ayuda a optimizar y reducir el gasto general de Azure. Para obtener más información, consulte las recomendaciones sobre el costo de Advisor.

- Excelencia operativa: ayuda a conseguir procedimientos recomendados de eficiencia en procesos y flujos de trabajo, manejabilidad de los recursos e implementación. Para más información, consulte Recomendaciones de excelencia operativa de Advisor.

![](https://docs.microsoft.com/es-es/azure/advisor/media/advisor-overview/advisor-dashboard.png)

Puede hacer clic en una categoría para ver la lista de recomendaciones dentro de esa categoría y seleccionar una recomendación para obtener más información sobre ella. También puede aprender más sobre las acciones que puede llevar a cabo para aprovechar las ventajas de una oportunidad o resolver un problema.

![](https://docs.microsoft.com/es-es/azure/advisor/media/advisor-overview/advisor-ha-category-example.png)

Seleccione la acción recomendada para implementar la recomendación. Se abrirá una interfaz sencilla que le permitirá implementar la recomendación o consultar la documentación que le ayudará con la implementación. Una vez que implemente una recomendación, Advisor puede tardar un día en reconocerla.

Si no desea realizar de inmediato una acción basada en una recomendación, puede posponerla durante un período de tiempo o descartarla. SI no desea recibir recomendaciones para un grupo de recursos o una suscripción específicos, puede configurar Advisor para generar solo recomendaciones para grupos de recursos y suscripciones específicos.

### 〔¿Cómo se accede a Advisor?〕
Puede acceder a Advisor mediante Azure Portal. Inicie sesión en el portal, busque Asesor en el menú de navegación o búsquelo en el menú Todos los servicios.

También puede ver las recomendaciones de Advisor a través de la interfaz de recursos de la máquina virtual. Seleccione una máquina virtual y después desplácese a las recomendaciones de Advisor en el menú.

### 〔¿Qué permisos son necesarios para acceder a Advisor?〕
Puede acceder a las recomendaciones de Advisor como Propietario, Colaborador o Lector de una suscripción, grupo de recursos o recurso.

### 〔¿Para qué recursos Advisor ofrece recomendaciones?〕
Advisor proporciona recomendaciones sobre Application Gateway, App Services, conjuntos de disponibilidad, Azure Cache, Azure Data Factory, Azure Database for MySQL, Azure Database for PostgreSQL, Azure Database for MariaDB, Azure ExpressRoute, Azure Cosmos DB, direcciones IP públicas de Azure, Azure Synapse Analytics, servidores SQL Server, cuentas de almacenamiento, perfiles de Traffic Manager y máquinas virtuales.

Azure Advisor también incluye recomendaciones procedentes de Microsoft Defender para la nube, que pueden abarcar recomendaciones de tipos de recursos adicionales.

### 〔¿Se puede posponer o descartar una recomendación?〕
Para posponer o descartar una recomendación, haga clic en el vínculo Postpone (Posponer). Puede especificar un tiempo de posposición o seleccionar Never (Nunca) para descartar la recomendación.

--------------

# 【Practica 11: Uso de Azure Advisor〕
Este recurso será el más sencillo de todos, y consiste en que podemos ver recomendaciones sobre nuestros recursos. Esto quiere decir que si algo anda mal con nuestros recursos o algo puede ser mejorado/implementado, se nos notificará y podemos realizar la acción tanto manual como automaticamente.

Por el momento, crearemos las alertas correspondientes para que cuando un recurso sea monitoreado, nos de las recomendaciones necesarias sobre que podemos mejorar.

### 〔Creando un grupo de recursos〕
Primero que nada, necesitamos crear un grupo de recursos, más adelante veremos porqué.

1. Buscamos en la barra de navegación *Grupos de recursos*.

2. Creamos el recurso, acompletamos los campos solicitados y luego hacemos clic en *Revisar y crear*.

![](https://i.imgur.com/LNpDa74.png)

3. Una vez superada la validación, clic en *Crear*.

![](https://i.imgur.com/gwuVysT.png)

### 〔Azure Advisor y su interfaz〕
Ahora, exploraremos Azure Advisor. Veremos ciertos apartados interesantes en su interfaz, tales como *Recomendaciones*, donde tendremos acceso a todo aquello de nuestros sistemas/recursos que puede tener alguna recomendación para su rendimiento y/o funcionamiento.

1. Buscamos en la navegación *Advisor* o "Asesor".

![](https://i.imgur.com/skQauE6.png)

2. Como mencioné antes, en la interfaz tenemos algunos apartados categorizados en que tipo de recomendaciones nos brindan, por ejemplo, si queremos saber una recomendación sobre la **seguridad** de nuestro sistema o tal vez saber si podemos reducir los **costos** de algo.

![](https://i.imgur.com/jyAsByc.png)

Por el momento no tengo ningún recurso creado, pero si hubiese alguno, automaticamente me diría sus recomendaciones y la puntuación de Advisor cambiaría hasta que yo resuelva el aviso.

### 〔Creando alertas de Advisor〕
Ahora, vamos a crear las alertas. Son muy similares a las que vimos en la práctica pasada.

1. Vamos al apartado *Supervisión* y en *Alertas*. Clic en el botón *Nueva alerta*.

![](https://i.imgur.com/BPubpbG.png)

2. Rellenamos los primeros campos como siempre, *Suscripción* y *Grupo de recursos*. Ahora, en condición, seleccionamos la que más convenga, en este caso seleccioné *Categoría y nivel de impacto*.

3. Después, seleccioné la categoría en la cual quiero la alerta, en este caso *Costo* y de impacto *Bajo*.

![](https://i.imgur.com/02RGmEx.png)

Esto quiere decir que tendremos una alerta cuando el costo sea menor o bajo a lo estipulado al momento de hacer nuestra contabilidad, signo de que algo "no está funcionando correctamente" (Máquinas virtuales) o "no hay mucho tráfico entrante" (Functions/Logic Apps).

![](https://i.imgur.com/PVAQIYm.png)

4. De igual forma, como vimos en la práctica 9, podemos elegir un grupo de acciones, la cual esté configurada para que podamos recibir un email a nuestro correo electrónico indicandonos de algo en nuestro sistema anda mal y necesite ser mejorado.

![](https://i.imgur.com/1uUjvxx.png)

5. Finalizamos colocando un nombre a nuestra regla de alertas, y lo demás por defecto.

6. Clic en *Crear regla*.

![](https://i.imgur.com/OyVCFSL.png)

La regla ya fue creada, pero tarda un poco en ser reflejada en el portal de Azure y que entre en vigor para que seamos notificados cuando el Asesor detecte alguna incidencia.