[![Logo FileSec.png](images/800px-Logo\_FileSec.png)](/pti/index.php/File:Logo_FileSec.png)

## Contents

* [1 Introducción](#Introducci.C3.B3n)
  + [1.1 ¿Qué es FileSec?](#.C2.BFQu.C3.A9_es_FileSec.3F)
* [2 Arquitectura](#Arquitectura)
  + [2.1 Tecnologías utilizadas](#Tecnolog.C3.ADas_utilizadas)
    - [2.1.1 IPFS](#IPFS)
    - [2.1.2 React](#React)
    - [2.1.3 Blockchain](#Blockchain)
    - [2.1.4 Node.js](#Node.js)
    - [2.1.5 Express.js y JWT](#Express.js_y_JWT)
    - [2.1.6 MySQL](#MySQL)
    - [2.1.7 Truffle](#Truffle)
    - [2.1.8 Ganache](#Ganache)
* [3 Desarollo](#Desarollo)
* [4 Conclusiones](#Conclusiones)

# Introducción[[edit](/pti/index.php?title=Categor%C3%ADa:Filesec&veaction=edit&section=1 "Edit section: Introducción") | [edit source](/pti/index.php?title=Categor%C3%ADa:Filesec&action=edit&section=1 "Edit section: Introducción")]

## ¿Qué es FileSec?[[edit](/pti/index.php?title=Categor%C3%ADa:Filesec&veaction=edit&section=2 "Edit section: ¿Qué es FileSec?") | [edit source](/pti/index.php?title=Categor%C3%ADa:Filesec&action=edit&section=2 "Edit section: ¿Qué es FileSec?")]

FileSec es una aplicación web donde cada persona puede crear su propia cuenta para subir sus ficheros de forma segura y poder listar los que ha subido en esa misma sesión.
Nuestro proyecto nace de la intención del grupo por crear un sistema de ficheros que fuese descentralizado, seguro y persistente en el tiempo, utilizando siempre que fuese posible Blockchain, ya que era una tecnología la cual teníamos muchas ganas de verla en acción después de haber leído, cada vez con más frecuencia, información sobre ella.

# Arquitectura[[edit](/pti/index.php?title=Categor%C3%ADa:Filesec&veaction=edit&section=3 "Edit section: Arquitectura") | [edit source](/pti/index.php?title=Categor%C3%ADa:Filesec&action=edit&section=3 "Edit section: Arquitectura")]

Para comenzar este apartado, adjuntamos la siguiente figura, a modo de esquema, donde se puede encontrar la arquitectura del proyecto y cómo están relacionadas entre sí las diferentes tecnologías que hemos utilizado.

[![](images/800px-Arquitectura\_FileSec.png)](/pti/index.php/File:Arquitectura_FileSec.png)

Arquitectura del proyecto.

## Tecnologías utilizadas[[edit](/pti/index.php?title=Categor%C3%ADa:Filesec&veaction=edit&section=4 "Edit section: Tecnologías utilizadas") | [edit source](/pti/index.php?title=Categor%C3%ADa:Filesec&action=edit&section=4 "Edit section: Tecnologías utilizadas")]

### IPFS[[edit](/pti/index.php?title=Categor%C3%ADa:Filesec&veaction=edit&section=5 "Edit section: IPFS") | [edit source](/pti/index.php?title=Categor%C3%ADa:Filesec&action=edit&section=5 "Edit section: IPFS")]

Como su nombre indica, IPFS (InterPlanetary File System) es un sistema de ficheros global que se basa en una red de nodos peer-to-peer los cuales comparten ficheros. Al subir un fichero a la red de IPFS, éste obtiene un hash único que lo identifica. Gracias a este hash, esta tecnología es capaz de ofrecer inmutabilidad e integridad a los ficheros. A diferencia de Blockchain, IPFS no ofrece la misma persistencia. Para nuestro proyecto hemos utilizado la librería de IPFS de Node.js que nos permite crear una API que gestiona la subida de ficheros a la red de IPFS.

### React[[edit](/pti/index.php?title=Categor%C3%ADa:Filesec&veaction=edit&section=6 "Edit section: React") | [edit source](/pti/index.php?title=Categor%C3%ADa:Filesec&action=edit&section=6 "Edit section: React")]

React es una librería de JavaScript especialmente enfocada en el desarrollo de interfaces de usuario. No obstante, es una herramienta excelente para todo tipo de aplicaciones. A diferencia de otras librerías más sencillas, elegimos React ya que aporta una serie de posibilidades muy importantes, como el hecho de que no necesitamos escribir el código necesario para manipular la página cuando los datos cambian.

### Blockchain[[edit](/pti/index.php?title=Categor%C3%ADa:Filesec&veaction=edit&section=7 "Edit section: Blockchain") | [edit source](/pti/index.php?title=Categor%C3%ADa:Filesec&action=edit&section=7 "Edit section: Blockchain")]

Esencialmente, Blockchain es una base datos descentralizada que puede contener información variada, incluso archivos, pero lo más común es que actúe como un libro de contabilidad público. Esto último es debido a que solo se puede interactuar con la cadena de bloques a través de transacciones y que normalmente su uso está relacionado con criptomonedas. En nuestro caso, hemos utilizado una Blockchain propia y privada para almacenar los hashes que identifican los ficheros subidos a IPFS y la fecha de su subida.

### Node.js[[edit](/pti/index.php?title=Categor%C3%ADa:Filesec&veaction=edit&section=8 "Edit section: Node.js") | [edit source](/pti/index.php?title=Categor%C3%ADa:Filesec&action=edit&section=8 "Edit section: Node.js")]

La tecnología Node.js destaca en la construcción rápida y escalable de aplicaciones de red, debido a que es capaz de manejar un gran número de conexiones simultáneas con alto rendimiento, equivalente a una alta escalabilidad.

### Express.js y JWT[[edit](/pti/index.php?title=Categor%C3%ADa:Filesec&veaction=edit&section=9 "Edit section: Express.js y JWT") | [edit source](/pti/index.php?title=Categor%C3%ADa:Filesec&action=edit&section=9 "Edit section: Express.js y JWT")]

Express.js es el framework web más popular de Node.js, ya que es rápido, flexible y consta de un buen diseño. Con la unión de este framework y JWT (JSON Web Token) hemos implementado el sistema de sesiones en nuestra aplicación web, en combinación con el React que estará en la parte del Front-end. El acceso a la página web lo verificamos mediante el JWT Authentification, que permite que un usuario nuevo que accede se pueda crear una nueva cuenta propia o hacer el login en el caso de que ya tenga una cuenta creada con anterioridad, tratando todo esto mediante peticiones dentro del framework de Express.js.

### MySQL[[edit](/pti/index.php?title=Categor%C3%ADa:Filesec&veaction=edit&section=10 "Edit section: MySQL") | [edit source](/pti/index.php?title=Categor%C3%ADa:Filesec&action=edit&section=10 "Edit section: MySQL")]

En nuestro caso, decidimos que necesitábamos una base de datos para almacenar únicamente los usuarios que registraba nuestra aplicación, ya que los archivos en sí los guardaríamos en IPFS. De esta forma, buscábamos un gestor de bases de datos sencillo y útil que almacenará estos datos y de ahí que finalmente nos decantasemos por MySQL.

### Truffle[[edit](/pti/index.php?title=Categor%C3%ADa:Filesec&veaction=edit&section=11 "Edit section: Truffle") | [edit source](/pti/index.php?title=Categor%C3%ADa:Filesec&action=edit&section=11 "Edit section: Truffle")]

Truffle es un conjunto de herramientas que permite trabajar con una Blockchain, la cual funciona encima de la tecnología Ethereum. Además, Truffle aprovecha la EVM (Ethereum Virtual Machine), que ofrece un entorno para poder desarrollar contratos inteligentes. Para nuestro proyecto, hemos utilizado Truffle para compilar el contrato inteligente y hacer el deploy de éste en una Blockchain local simulada por Ganache, dejando Drizzle a un lado ya que no vimos ninguna característica diferencial que nos motivase a incorporarlo al proyecto.

### Ganache[[edit](/pti/index.php?title=Categor%C3%ADa:Filesec&veaction=edit&section=12 "Edit section: Ganache") | [edit source](/pti/index.php?title=Categor%C3%ADa:Filesec&action=edit&section=12 "Edit section: Ganache")]

Ganache forma parte de las herramientas que nos ofrece Truffle para el desarrollo de aplicaciones que funcionan sobre Ethereum. Esencialmente, simula una Blockchain de Ethereum de forma local, y con la cual podemos interactuar. Además, comentar que para nuestro proyecto ha sido muy importante el tener a nuestro alcance una herramienta como Ganache, ya que nos ha permitido trabajar de una forma muy cómoda y sencilla. Por último, tenemos que hacer mención a la librería de Web3 de js, que nos ha permitido interactuar con nuestra Blockchain de Ganache desde Node.js.

# Desarollo[[edit](/pti/index.php?title=Categor%C3%ADa:Filesec&veaction=edit&section=13 "Edit section: Desarollo") | [edit source](/pti/index.php?title=Categor%C3%ADa:Filesec&action=edit&section=13 "Edit section: Desarollo")]

FileSec está construida sobre una base de tres funcionalidades ofrecidas al usuario, que son las siguientes:

**Subir archivos:** Esta es la función principal de nuestro proyecto. Nos permite arrastrar dentro de la zona los archivos que deseemos subir a la red IPFS o clickar en la propia zona y elegirlo desde el pop-up que aparece con todos los archivos del disco local, y una vez hecho eso nos devuelve un hash identificador del fichero. Como hemos comentado al principio, el “Subir archivos” la podríamos considerar como la función básica y principal de nuestro proyecto, ya que sin poder subir archivos a la red IPFS no existirían ni la opción de buscarlos ni de listarlos.

**Buscar archivos:** En esta parte de la aplicación, nos encontramos un campo donde el usuario deberá introducir el hash del fichero que se le proporcionó cuando subió ese mismo fichero. Una vez lo introduzca, podrá observar como se despliega un conjunto de información obtenido desde la Blockchain (siendo el hash el identificador del bloque), como por ejemplo el link para acceder al contenido de dicho archivo, que está guardado en la red IPFS.

**Listar archivos:** Esta opción permite al usuario ver los hashes de los archivos que ha subido exclusivamente en esa sesión. A medida que vaya subiendo ficheros podrá observar una lista que va aumentando, siendo el último hash el hash del fichero subido más recientemente. El poder listar los archivos subidos es imprescindible en la aplicación, ya que permite al usuario ver los hashes que identifican a cada uno de los ficheros para que pueda proceder a buscarlos en la pestaña de Buscar y de esta forma acceder al contenido de los mismos. Nuestra aplicación tiene como uno de sus principales objetivos la seguridad de los ficheros, y para ello pensamos que un factor extra en este ámbito podría ser que la aplicación web no guardase de ninguna manera estos hashes. De esta manera, se nos ocurrió una muy buena idea, que sería listar solo los hashes de los archivos que el usuario haya subido en esa misma sesión, y que una vez hiciera el logout, no quedase rastro de esos hashes en ningún lado.

# Conclusiones[[edit](/pti/index.php?title=Categor%C3%ADa:Filesec&veaction=edit&section=14 "Edit section: Conclusiones") | [edit source](/pti/index.php?title=Categor%C3%ADa:Filesec&action=edit&section=14 "Edit section: Conclusiones")]

Podemos decir que estamos muy satisfechos con el proyecto, ya que está formado por diversas tecnologías, que una vez unidas nos ha dado lugar a un sistema de ficheros nada convencional como es FileSec. La creación de esta compleja aplicación ha hecho que hayamos tenido que cambiar muchas decisiones del proyecto que teníamos como claras, pero una vez explorado ese camino nos dimos cuenta de que no era el idóneo y por lo tanto nos tocó girar el rumbo, como nos pasó al principio con la idea de solo utilizar la Blockchain. Esto consideramos que ha sido parte del aprendizaje que hemos obtenido tras haber realizado este proyecto, y por lo tanto estamos satisfechos de que así haya sido, ya que además nos ha permitido aprender sobre como superar los problemas que hemos ido encontrando a lo largo de estos meses.