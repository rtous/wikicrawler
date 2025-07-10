[![](images/400px-Logo.PNG)](/pti/index.php/File:Logo.PNG)

Proyecto de PTI - Q1 2017-2018.

# ¿Qué es Sit&Order?[[edit](/pti/index.php?title=Categor%C3%ADa:Sit%26Order&veaction=edit&section=1 "Edit section: ¿Qué es Sit&Order?") | [edit source](/pti/index.php?title=Categor%C3%ADa:Sit%26Order&action=edit&section=1 "Edit section: ¿Qué es Sit&Order?")]

Los restaurantes que solemos visitar hoy en día funcionan casi todos de forma similar, el cliente llega y espera a que le asignen mesa, luego espera a que le traigan la carta, luego espera a que le recojan el pedido, luego espera que le traigan la comida,… muchas esperas que a veces crean una mala reputación para el restaurante si encima son largas.

La solución que proponemos a este problema consiste en una aplicación móvil multiplataforma con dos tipos de perfiles de usuario: clientes y restaurantes. La app permite a los clientes identificarse cuando llegan a un restaurante, descargarse la carta o menú, hacer el pedido a la cocina, añadir comentarios al pedido y avisar al restaurante de que se quiere pagar la cuenta. La misma aplicación permite a los restaurantes modificar su carta o menú diario y recibir los pedidos de los clientes.

# Objetivo del proyecto[[edit](/pti/index.php?title=Categor%C3%ADa:Sit%26Order&veaction=edit&section=2 "Edit section: Objetivo del proyecto") | [edit source](/pti/index.php?title=Categor%C3%ADa:Sit%26Order&action=edit&section=2 "Edit section: Objetivo del proyecto")]

Nuestro objetivo durante este proyecto ha sido el de crear un entorno más automatizado y unificado en un restaurante, es decir, que tanto los clientes como el restaurante pudieran tener información de lo que sucedía en todo momento y para ello, nos marcamos unos objetivos básicos.

Tanto el cliente como el restaurante usarían una misma aplicación donde podrían registrarse con distintos perfiles (cada uno verá cosas diferentes en su aplicación). En el caso de los clientes lo más importante era poder ver el menú, seleccionar los distintos platos que quisiera pedir e enviarlos a la cocina, además poder añadir comentarios con cada plato pedido.

Para el restaurante las funcionalidades que consideramos más importantes fueron el hecho de poder crear y modificar un menú y el control de los pedidos: poder ver todos los pedidos realizados en tu restaurante identificados por el número de mesa y poder cambiar su estado (por ejemplo si pasamos a cocinar el pedido o está a punto de ser entregado o ya lo tiene el cliente), este cambio de estado también sería visible por el cliente en todo momento.

# Infraestructura[[edit](/pti/index.php?title=Categor%C3%ADa:Sit%26Order&veaction=edit&section=3 "Edit section: Infraestructura") | [edit source](/pti/index.php?title=Categor%C3%ADa:Sit%26Order&action=edit&section=3 "Edit section: Infraestructura")]

Para implementar esta solución se han escogido una serie de tecnologías que facilitan su desarrollo y puesta en marcha. El proyecto está dividido en dos grandes bloques, la aplicación móvil por un lado, y el servidor que gestiona y sirve la información a la aplicación a través de servicios web.
Para el desarrollo de la aplicación móvil se ha usado el framework Ionic que permite compilar el mismo código para iOS, Android y WindowsPhone.

Cuando los clientes llegan al restaurante deben utilizar la tecnología NFC para leer un tag que está situado en las mesas de los restaurante, de esta manera, la app identifica el restaurante y se descarga el menú. El mismo tag también contiene el numero de mesa para enviarlo al restaurante cuando se hace un pedido.

El intercambio de información entre la app y el backend se realiza a través de servicios REST y en formato JSON.

Finalmente, el backend consiste en una aplicación Java creada con el framework Spring Boot que hace consultas a una base de datos MySQL. El backend está montado sobre dos contenedores Docker, uno con la aplicación y otro con el servidor de bases de datos.