[![Youtv black.png](images/200px-Youtv\_black.png)](/pti/index.php/File:Youtv_black.png)

[Enlace a YouTV](http://youtv.aleixmurtra.com)

## 1. ¿Qué es YouTV?[[edit](/pti/index.php?title=Categor%C3%ADa:YouTV&veaction=edit&section=1 "Edit section: 1. ¿Qué es YouTV?") | [edit source](/pti/index.php?title=Categor%C3%ADa:YouTV&action=edit&section=1 "Edit section: 1. ¿Qué es YouTV?")]

Youtv es una plataforma de televisión por Internet con contenido de Youtube y está compuesto por diferentes canales agrupados por temáticas.
Tenemos canales de música, humor, conocimiento y entretenimiento. Todos estos canales funcionan a tiempo real. Es decir, si dos personas miran un mismo canal veran el mismo contenido y, en el caso ideal, estarán sincronizados al segundo.
Creemos que tenemos dos componentes muy importantes para poder crecer en un futuro: el contenido es a tiempo real, y le damos la posibilidad a los usuarios a que puedan compartir lo que ven con sus amigos; el segundo componente es el hecho de tener canales temáticos. Los usuarios que no sepan qué visualizar en la televisión o en internet pueden escoger un canal o hacer zapping. Una vez encuentren el canal que mas les guste no tienen que preocuparse por los videos que vienen a continuación, todos están relacionados con la misma temática central.

## 2. Tecnologías[[edit](/pti/index.php?title=Categor%C3%ADa:YouTV&veaction=edit&section=2 "Edit section: 2. Tecnologías") | [edit source](/pti/index.php?title=Categor%C3%ADa:YouTV&action=edit&section=2 "Edit section: 2. Tecnologías")]

**Servidor**
Hemos instalado Apache 2 para el servidor web y lo hemos configurado con los módulos rewrite y sslengine para que pueda ser llamado mediante HTTP y HTTPS.
Junto al servidor Apache tenemos PHP5.5, que se usará para correr código PHP en el servidor, tanto proveniente de la página web, puesto que es uno de los lenguajes con los que está programada en PHP, como del propio servidor.
Node.JS
Es un entorno de programación asíncrono que se ejecuta al lado del servidor. Está programado en JavaScript y carga diferentes módulos para poder dar el servicio deseado. En la práctica hemos usado los siguientes módulos:
- Socket.io: Éste módulo nos permite comunicar dos dispositivos y transmitir datos en JSON. Para realizar la comunicación se usan esencialmente dos métodos llamados socket.emit(nombre, función) y socket.on(nombre, función). El emit lo emite el que quiere interactuar con el otro y el on el que recibe la llamada. Reaccionan si el nombre es el mismo ejecutando así la función definida.
- Node-MySQL: Éste módulo permite hacer conexiones a un servidor MySQL.
- Temboo: Permite enviar tweets usando la API de una página web llamada Temboo.

**Web**
Hemos decidido crear una interfaz web sencilla e intuitiva. Para el diseño hemos usado HTML5 y CSS3, compatibles con versiones de internet Explorer 10 o superior y últimas versiones de Firefox, Chrome,Opera y Safari.
- JavaScript: Permite crear funciones que se ejecutarán en el navegador del cliente.
- Ajax: Permite llamadas al servidor a través de JavaScript con las que podemos actualizar una parte del código (una parte específica de la web). En muchos casos mejoramos la eficiencia al no enviar información redundante (enviamos al servidor solo aquellos datos que sean necesarios y pedimos solo lo que nos interesa). También mejora la usabilidad de la aplicación haciéndola más cómoda y rápida para el usuario.

**Android**
Hemos desarrollado una aplicación Android para controlar algunos aspectos del funcionamiento de la página web remotamente, como si de un mando a distancia se tratara. Ésta está programada usando las herramientas básicas que ofrece el sistema Android (ofreciendo compatibilidad hasta la versión 4.1.2) y otra herramienta para la conexión:
- Socket.io: Para la comunicación en red hemos usado una implementación abierta del cliente Socket.io que encontramos en GitHub.[1] El funcionamiento es el mismo que el de la implementación para el servidor, usando las funciones emit para llamar a funciones remotas y on para atender las peticiones entrantes.

[![Youtv screen.png](images/800px-Youtv\_screen.png)](/pti/index.php/File:Youtv_screen.png)