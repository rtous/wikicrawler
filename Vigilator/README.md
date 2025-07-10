[![](images/Meteoestructura.png)](/pti/index.php/File:Meteoestructura.png)

Estructura del proyecto.

# Introducción[[edit](/pti/index.php?title=Categor%C3%ADa:Vigilator&veaction=edit&section=1 "Edit section: Introducción") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vigilator&action=edit&section=1 "Edit section: Introducción")]

## ¿Qué es MeteoFib?[[edit](/pti/index.php?title=Categor%C3%ADa:Vigilator&veaction=edit&section=2 "Edit section: ¿Qué es MeteoFib?") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vigilator&action=edit&section=2 "Edit section: ¿Qué es MeteoFib?")]

Nuestro proyecto consiste en una estación meteorológica que provee a los usuarios de datos de interés sobre las condiciones climatológicas del día actual y un histórico de los días recientes. El usuario puede consultar dicha información mediante una aplicación de Android o bien mediante una página web habilitada para tal propósito.

# Infraestructura[[edit](/pti/index.php?title=Categor%C3%ADa:Vigilator&veaction=edit&section=3 "Edit section: Infraestructura") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vigilator&action=edit&section=3 "Edit section: Infraestructura")]

Nuestro infraestructura consiste de distintos componentes. En primer lugar tenemos un Arduino conectado a unos sensores de temperatura, humedad y presión. Este a su vez, se conecta con una Raspberry Pi para enviarle los datos recogidos por los sensores.

La Raspberry nos servirá para dos fines: almacenar estos datos meteorológicos en una base de datos SQL y para crear un servicio web que será el encargado de recibir las peticiones GET de la página web y la aplicación Android y responder a estas peticiones con los datos pedidos en formato JSon. Tanto la Base de datos como el servicio web se encuentran en dos contenedores independientes que se gestionan mediante Docker.

Para poder visualizar estos datos, al usuario se le ofrecen dos posibilidades, acceder a ellos mediante una página web y una aplicación Android.