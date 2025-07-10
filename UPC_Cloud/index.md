[![Upccloud name](images/755px-Upccloud\_name.png)](/pti/index.php/File:Upccloud_name.png "Upccloud name")

## Contents

* [1 Introducción](#Introducci.C3.B3n)
* [2 Objetivos](#Objetivos)
* [3 Arquitectura](#Arquitectura)
* [4 Tecnologías utilizadas](#Tecnolog.C3.ADas_utilizadas)
  + [4.1 Nginx](#Nginx)
  + [4.2 React.js](#React.js)
  + [4.3 Node.js](#Node.js)
  + [4.4 MongoDB](#MongoDB)
  + [4.5 IPFS](#IPFS)
  + [4.6 Kubernetes](#Kubernetes)
  + [4.7 Blockchain](#Blockchain)
* [5 Interacción con el usuario](#Interacci.C3.B3n_con_el_usuario)
  + [5.1 Página de inicio](#P.C3.A1gina_de_inicio)
  + [5.2 Inicio de sesión y Registro de usuario](#Inicio_de_sesi.C3.B3n_y_Registro_de_usuario)
  + [5.3 Página gestora de ficheros](#P.C3.A1gina_gestora_de_ficheros)
    - [5.3.1 Vista inicial](#Vista_inicial)
    - [5.3.2 Gráficos](#Gr.C3.A1ficos)
* [6 Enlaces de interés](#Enlaces_de_inter.C3.A9s)

# Introducción[[edit](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&veaction=edit&section=1 "Edit section: Introducción") | [edit source](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&action=edit&section=1 "Edit section: Introducción")]

[![](images/159px-Upccloud\_logo.png)](/pti/index.php/File:Upccloud_logo.png)

Logo de UPC Cloud.

UPC Cloud es un sistema de almacenamiento de datos revolucionario y altamente eficiente. En contraposición a las plataformas convencionales como Google Drive, este sistema se fundamenta en una arquitectura descentralizada, utilizando un cluster privado de IPFS para administrar nodos de almacenamiento distribuido. Esta elección tecnológica no solo asegurará la disponibilidad de los datos en todo momento, sino que también proporcionará redundancia y escalabilidad, características esenciales para un servicio de almacenamiento confiable en el mundo digital actual.

# Objetivos[[edit](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&veaction=edit&section=2 "Edit section: Objetivos") | [edit source](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&action=edit&section=2 "Edit section: Objetivos")]

Este proyecto tiene como objetivo crear un sistema de disco, con acceso simple, protegiendo la integridad y la confidencialidad de la información, tanto en el almacenamiento como en el acceso, con un sistema distribuido de almacenamiento de disco, escalable para permitir añadir espacio de almacenamiento de forma simple y sin tener que interrumpir el sistema, a prueba de fallos de caídas de máquinas, usando replicaciones de datos.

Al plantear el problema se vió que IPFS era un candidato a realizar esas características.Además, IPFS es un sistema que tiene una implementación que viene dockerizada, y que sobre el papel es fácil de administrar a través de contenedores. Con ello, falta un sistema de orquestación de contenedores para que IPFS sea realmente escalable de forma automática, así que usamos Kubernetes para encargarse de la orquestación de las instancias de IPFS, creándose y eliminando bajo demanda, e distribuyendo las instancias entre diversas máquinas. En este caso, la replicación de datos se hace a nivel de bloques entre nodos.

Para poder acceder a estos datos, tenemos que crear una página web, con una interfaz moderna y fácil de usar, escrita en React. Para distribuir esta página web usaremos un servidor Nginx en la máquina.

El frontend, para obtener los atributos de los usuarios y los archivos se comunica con un backend robusto (escrito en JavaScript usando la librería express) que se encarga de la autenticación de los usuarios, del almacenamiento de los atributos de los archivos y de implementar características extras de las que se consideraban al inicio del proyecto (el backend se encarga de dar las características de compartición de archivos y también hace de gateway con el frontend para dar los datos de blockchain. Este backend se apoya en una base de datos noSQL (mongoDB) para almacenar quien comparte los archivos a quién y ciertos atributos simples de los archivos.

Para almacenar los índices de popularidad de un archivo (en nuestro caso cuantas veces se ha compartido y descargado) tenemos planteado externalizar esto a un sistema blockchain, que nos permite hacer que estos datos sean provenientes de la blockchain. Para ello, tendremos que implementar un Smart Contract que nos permita hacer deploy y que en blockchain se almacenen esos atributos de todos los archivos.

# Arquitectura[[edit](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&veaction=edit&section=3 "Edit section: Arquitectura") | [edit source](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&action=edit&section=3 "Edit section: Arquitectura")]

[![](images/418px-Estructura\_final.png)](/pti/index.php/File:Estructura_final.png)

Esquema de la arquitectura final del sistema.

En la imagen de la arquitectura nos encontramos con cinco recuadros grises. Estos representan las cinco máquinas virtuales utilizadas.

Si analizamos el esquema, y por tanto la estructura final del proyecto, tenemos el usuario que hace peticiones a una web. Este contenido es mostrado y gestionado por Nginx, que, de cara al frontend, está actuando como servidor web.

Si el usuario, o el propio sistema, necesitan consultar información sobre el usuario, desde el mismo frontend se realizarán peticiones al backend que, gracias a que utilizamos un Nginx a modo de reverse proxy en la máquina virtual que contiene el backend, podemos ofrecer al usuario una conexión totalmente segura y encriptada con ssl.

Si el sistema necesita hacer algún cambio sobre los ficheros del usuario, ya sea subir un fichero nuevo, descargar uno existente, eliminar o cambiarle el nombre, el backend se comunicará con uno de los nodos de IPFS responsable de la gestión del almacenamiento.

Este nodo de IPFS, en caso de poder realizar la operación requerida, operará como sea necesario. En caso de no poder, por ejemplo porque sea una petición de descarga de un fichero que no está localizado en ese nodo, será el propio nodo el que se encargue de comunicarse con el resto de nodos para poder obtener los datos y operar como sea necesario.

Adicionalmente disponemos de un kubernetes sobre los nodos de IPFS que son capaces de realizar un balanceo de carga y escalar el sistema.

Como se puede observar, el sistema blockchain no se muestra en ninguna máquina, esto es debido a que se consiguieron hacer pruebas en local pero debido a los problemas que encontramos a la hora de hacer la migración a las máquinas virtuales, decidimos descartar la tecnología.

# Tecnologías utilizadas[[edit](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&veaction=edit&section=4 "Edit section: Tecnologías utilizadas") | [edit source](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&action=edit&section=4 "Edit section: Tecnologías utilizadas")]

Para la correcta realización del proyecto decidimos utilizar las siguientes tecnologías.

## Nginx[[edit](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&veaction=edit&section=5 "Edit section: Nginx") | [edit source](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&action=edit&section=5 "Edit section: Nginx")]

[![Nginx logo.png](images/72px-Nginx\_logo.png)](/pti/index.php/File:Nginx_logo.png)

La utilización de Nginx fue una parte fundamental de nuestro proyecto ya que, como hemos podido comprobar hasta ahora, toda nuestra infraestructura se basa en un solo punto de acceso a través de un navegador web desde donde el usuario puede interactuar con nuestro sistema.
Desde un punto de vista más técnico, grácias a la versatilidad de esta tecnología pudimos realizar un servicio web y un reverse proxy para poder separar la carga de cada máquina y disponer de una comunicación entre ellas totalmente segura y encriptada y, debido al poco consumo de recursos que presenta esta tecnología, era la opción más acertada.

## React.js[[edit](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&veaction=edit&section=6 "Edit section: React.js") | [edit source](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&action=edit&section=6 "Edit section: React.js")]

[![React logo](images/React\_logo.png)](/pti/index.php/File:React_logo.png "React logo")

La implementación con React.js es, debido al mecanismo de funcionamiento de nuestro sistema, de las partes más importantes implementadas.

Grácias a la gran versatilidad y posibilidades que ofrece este framework, hemos podido crear una interfaz para el usuario atractiva e intuitiva, que exprime al máximo las posibilidades que ofrecen las capas subyacentes a lo que es el frontend.

## Node.js[[edit](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&veaction=edit&section=7 "Edit section: Node.js") | [edit source](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&action=edit&section=7 "Edit section: Node.js")]

[![Nodejs logo](images/100px-Nodejs\_logo.png)](/pti/index.php/File:Nodejs_logo.png "Nodejs logo")

Utilizado en el backend, Node.js permite ejecutar nuestro sistema de manera eficiente, optimizando el manejo de las solicitudes de API gracias a su modelo de eventos no bloqueante. Esta característica es fundamental para procesar un alto volumen de transacciones simultáneamente, lo que genera respuestas rápidas del servidor y una mejor experiencia de usuario. Su integración fluida con tecnologías como MongoDB y su vasto ecosistema de módulos npm amplían aún más su funcionalidad, haciendo que Node.js sea perfecto para la escalabilidad y el rendimiento.

## MongoDB[[edit](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&veaction=edit&section=8 "Edit section: MongoDB") | [edit source](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&action=edit&section=8 "Edit section: MongoDB")]

[![Mongodb logo](images/65px-Mongodb\_logo.png)](/pti/index.php/File:Mongodb_logo.png "Mongodb logo")

Como base de datos NoSQL, MongoDB juega un papel crucial en el manejo de grandes volúmenes de datos con alta disponibilidad y elasticidad.

Su capacidad para escalar horizontalmente y manejar eficientemente datos estructurados y no estructurados es vital para sistemas descentralizados, facilitando la gestión y el acceso rápido a los datos, y apoyando las demandas dinámicas del sistema al garantizar que los datos estén siempre disponibles y sean fácilmente accesibles.

## IPFS[[edit](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&veaction=edit&section=9 "Edit section: IPFS") | [edit source](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&action=edit&section=9 "Edit section: IPFS")]

[![Ipfs logo](images/52px-Ipfs\_logo.png)](/pti/index.php/File:Ipfs_logo.png "Ipfs logo")

La integración de IPFS fue fundamental para descentralizar el almacenamiento de archivos, superando así las limitaciones de los sistemas centralizados tradicionales. IPFS nos permite que los archivos no residan en un solo punto, sino que están distribuidos a través de una red, mejorando así la redundancia y la disponibilidad.

## Kubernetes[[edit](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&veaction=edit&section=10 "Edit section: Kubernetes") | [edit source](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&action=edit&section=10 "Edit section: Kubernetes")]

[![Kube logo](images/65px-Kube\_logo.png)](/pti/index.php/File:Kube_logo.png "Kube logo")

La automatización y la gestión de cargas de trabajo utilizando Kubernetes y Docker ha sido crucial para optimizar la gestión de nuestros microservicios, facilitando la alta disponibilidad de datos, la tolerancia a fallos y la escalabilidad. A medida que se buscan mejoras futuras, la implementación de funcionalidades de escalabilidad automática a través de Kubernetes se destaca como una mejora significativa en el sistema. Actualmente, el sistema no dispone de autoescalado, pero se reconoce la importancia crítica de esta funcionalidad para adaptarse dinámicamente a las variaciones en la carga y la demanda. Se planea integrar el Horizontal Pod Autoscaler (HPA) y el Cluster Autoscaler en nuestro sistema para mejorar la escalabilidad. El HPA ajustará automáticamente la cantidad de pods basándose en el uso de CPU y memoria, mientras que el Cluster Autoscaler modificará la cantidad de nodos en función de las necesidades, integrándose con la infraestructura de nube. Estas mejoras facilitarán la adaptación dinámica a las demandas del sistema, mejorando la gestión de la carga, la eficiencia y la resiliencia, y garantizando un rendimiento óptimo y la satisfacción del cliente.

## Blockchain[[edit](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&veaction=edit&section=11 "Edit section: Blockchain") | [edit source](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&action=edit&section=11 "Edit section: Blockchain")]

[![Block logo](images/72px-Block\_logo.png)](/pti/index.php/File:Block_logo.png "Block logo")

La implementación de la blockchain prometía mejoras en la trazabilidad y la seguridad de las transacciones para el contador de popularidad de archivos. Sin embargo, durante la implantación se presentaron obstáculos significativos que impidieron su efectiva integración en el sistema. Estos desafíos han permitido identificar áreas críticas para mejora, y destacan la necesidad de un desarrollo continuo y adaptación de estrategias para superar las dificultades iniciales. El aspecto más crucial para abordar es la mejora del contrato inteligente para asegurar una funcionalidad completa y eficiente.

# Interacción con el usuario[[edit](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&veaction=edit&section=12 "Edit section: Interacción con el usuario") | [edit source](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&action=edit&section=12 "Edit section: Interacción con el usuario")]

## Página de inicio[[edit](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&veaction=edit&section=13 "Edit section: Página de inicio") | [edit source](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&action=edit&section=13 "Edit section: Página de inicio")]

[![](images/840px-Landing\_Page.png)](/pti/index.php/File:Landing_Page.png)[![](images/841px-Landing\_dark.png)](/pti/index.php/File:Landing_dark.png)

## Inicio de sesión y Registro de usuario[[edit](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&veaction=edit&section=14 "Edit section: Inicio de sesión y Registro de usuario") | [edit source](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&action=edit&section=14 "Edit section: Inicio de sesión y Registro de usuario")]

[![](images/840px-Login\_upccloud.png)](/pti/index.php/File:Login_upccloud.png)[![](images/840px-Registro\_upccloud.png)](/pti/index.php/File:Registro_upccloud.png)

## Página gestora de ficheros[[edit](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&veaction=edit&section=15 "Edit section: Página gestora de ficheros") | [edit source](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&action=edit&section=15 "Edit section: Página gestora de ficheros")]

### Vista inicial[[edit](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&veaction=edit&section=16 "Edit section: Vista inicial") | [edit source](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&action=edit&section=16 "Edit section: Vista inicial")]

[![](images/840px-Storage\_light\_upccloud.png)](/pti/index.php/File:Storage_light_upccloud.png)[![](images/840px-Storage\_dark\_upccloud.png)](/pti/index.php/File:Storage_dark_upccloud.png)

### Gráficos[[edit](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&veaction=edit&section=17 "Edit section: Gráficos") | [edit source](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&action=edit&section=17 "Edit section: Gráficos")]

[![](images/840px-Gr%C3%A1ficos\_light\_upccloud.png)](/pti/index.php/File:Gr%C3%A1ficos_light_upccloud.png)[![](images/840px-Graficos\_dark\_upccloud.png)](/pti/index.php/File:Graficos_dark_upccloud.png)

# Enlaces de interés[[edit](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&veaction=edit&section=18 "Edit section: Enlaces de interés") | [edit source](/pti/index.php?title=Categor%C3%ADa:UPC_Cloud&action=edit&section=18 "Edit section: Enlaces de interés")]

* [Código fuente del proyecto](https://github.com/JavierArmaza/PTI-project-UPCCloud)