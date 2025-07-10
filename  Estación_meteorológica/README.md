## Contents

* [1 Introducción](#Introducci.C3.B3n)
  + [1.1 ¿Qué es Weether?](#.C2.BFQu.C3.A9_es_Weether.3F)
* [2 Infraestructura](#Infraestructura)
* [3 Tecnologías](#Tecnolog.C3.ADas)

# Introducción[[edit](/pti/index.php?title=Categor%C3%ADa:_Estaci%C3%B3n_meteorol%C3%B3gica&veaction=edit&section=1 "Edit section: Introducción") | [edit source](/pti/index.php?title=Categor%C3%ADa:_Estaci%C3%B3n_meteorol%C3%B3gica&action=edit&section=1 "Edit section: Introducción")]

## ¿Qué es Weether?[[edit](/pti/index.php?title=Categor%C3%ADa:_Estaci%C3%B3n_meteorol%C3%B3gica&veaction=edit&section=2 "Edit section: ¿Qué es Weether?") | [edit source](/pti/index.php?title=Categor%C3%ADa:_Estaci%C3%B3n_meteorol%C3%B3gica&action=edit&section=2 "Edit section: ¿Qué es Weether?")]

Nuestro proyecto consiste en una estación meteorológica que provee a los usuarios de datos de interés sobre las condiciones climatológicas del día actual en tiempo real y un histórico de otras fechas entre las que se puede escoger o bien un día concreto o bien los datos de un mes entero. El usuario puede consultar dicha información mediante una página web habilitada para tal propósito.

# Infraestructura[[edit](/pti/index.php?title=Categor%C3%ADa:_Estaci%C3%B3n_meteorol%C3%B3gica&veaction=edit&section=3 "Edit section: Infraestructura") | [edit source](/pti/index.php?title=Categor%C3%ADa:_Estaci%C3%B3n_meteorol%C3%B3gica&action=edit&section=3 "Edit section: Infraestructura")]

Nuestro infraestructura consiste de distintos componentes:

* **Arduino Elegoo Uno R3**
En primer lugar tenemos un Arduino conectado a unos sensores de temperatura, humedad, presión y lluvia. Este a su vez, se conecta con una Raspberry Pi para enviarle los datos recogidos por los sensores.
Los sensores utilizados son los siguientes:

+ DHT22 que mide temperatura y humedad.
+ BMP180 que también mide temperatura para cálculos propios y presión.
+ Sensor HL-83 cuya función es determinar si llueve dependiendo de lo mojado que esté. (Mide la lluvia de forma binaria)

* **Raspberry PI 3B**
La Raspberry PI actuará como un middleware dentro de todo el stack de comunicaciones que hemos implementado, leyendo todo lo que pueda del input, utilizando una conexión serial con el Arduino, y enviándola al servidor central, utilizando un socket AMQP con el servidor RabbitMQ. Para añadir una
capa extra de tolerancia a falladas, el socket no está directamente conectado al servidor AMQP central, sino que está conectado a un servidor intermediario AMQP, que se ejecuta en la propia Raspberry PI y que está conectado al servidor central utilizando el plugin Shovel.* **Servidor Open Nebula**
El servidor web se encuentra localizado en una instancia de Open Nebula y tiene diversas funciones:

+ Servidor Web que se encargara de recibir las peticiones GET que se hagan en la Web. Tiene una API REST con un endpoint distinto para cada variable medida por los sensores.
+ Servidor Node.js que se ejecuta de forma independiente y concurrente respecto al servidor web y que se encarga de recoger los datos pendientes en la cola de RabbitMQ de Open Nebula para introducirlos en la base de datos de MongoDB.

# Tecnologías[[edit](/pti/index.php?title=Categor%C3%ADa:_Estaci%C3%B3n_meteorol%C3%B3gica&veaction=edit&section=4 "Edit section: Tecnologías") | [edit source](/pti/index.php?title=Categor%C3%ADa:_Estaci%C3%B3n_meteorol%C3%B3gica&action=edit&section=4 "Edit section: Tecnologías")]

Se han utilizado las siguientes tecnologías:

* **Arduino**
* **Raspberry PI**

+ Node.js: plataforma para ejecutar código en JavaScript.
+ Gulp: build-system basado en streams.
+ Babel: transpilador de JavaScript.
+ Docker: plataforma para la creación y ejecución de contenedores.
+ Docker Hub: servicio usado para distribuir contenedores.
+ RabbitMQ: bróker de mensajería.
+ AMQP: protocolo para la administración avanzada de las colas de RabbitMQ.
+ PiBakery: aplicación para configurar gráficamente la Raspberry PI.
+ Serialport: protocolo usado para obtener los datos de Arduino.
+ Travis CI: servicio de integración continua para hacer testing online.

* **Servidor Web en Open Nebula**

+ MongoDB: base de datos NoSQL líder en el mercado por su agilidad, flexibilidad y escalabilidad.
+ Mongoose: añade una capa sobre MongoDB que asiste a la hora de definir las estructuras de datos que se guardan en la base de datos.
+ AMQP: el protocolo utilizado para la comunicación con el servidor RabbitMQ central. La implementación nos la aporta la librería rabbit.js.
+ Express.js: framework utilizado para implementar el servidor HTTP.
+ AngularJS: framework utilizado para implementar el patrón de Model-View -Controller(MVC) de manera sencilla e intuitiva con el uso de bindings y diferentes componentes.
+ Node.js: la plataforma número uno en el mercado para ejecutar JavaScript en un servidor.
+ Material Design
+ Zingchart: ofrece una amplia variedad de herramientas de visualización en forma de gráficos.
+ HTML, CSS y JavaScript: las tres tecnologías básicas de una página web que permiten definir su estructura, estilo e interacción con el usuario.
+ Jade/Pug: librería de templating usada para generar las vistas, es decir, para crear la estructura de la página web (HTML).