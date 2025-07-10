[![](images/Meteoestructura.png)](/pti/index.php/File:Meteoestructura.png)

Estructura del proyecto.

## Contents

* [1 Introducción](#Introducci.C3.B3n)
  + [1.1 ¿Qué es TweetWeather?](#.C2.BFQu.C3.A9_es_TweetWeather.3F)
  + [1.2 Objetivos](#Objetivos)
* [2 Infraestructura](#Infraestructura)
  + [2.1 Tecnologías usadas](#Tecnolog.C3.ADas_usadas)

# Introducción[[edit](/pti/index.php?title=Categor%C3%ADa:Tweet-Weather&veaction=edit&section=1 "Edit section: Introducción") | [edit source](/pti/index.php?title=Categor%C3%ADa:Tweet-Weather&action=edit&section=1 "Edit section: Introducción")]

## ¿Qué es TweetWeather?[[edit](/pti/index.php?title=Categor%C3%ADa:Tweet-Weather&veaction=edit&section=2 "Edit section: ¿Qué es TweetWeather?") | [edit source](/pti/index.php?title=Categor%C3%ADa:Tweet-Weather&action=edit&section=2 "Edit section: ¿Qué es TweetWeather?")]

Nuestro proyecto consiste en una estación meteorológica portátil que registra los valores de diferentes condiciones climatológicas del entorno en el que se encuentra. El usuario puede consultar la información registrada mediante una aplicación Android, donde ve el último valor registrado y gráficos que muestran la evolución de los diferentes aspectos. Con la app también puede publicar estos datos en twitter, gracias a la integración que la aplicación tiene con la red social.

La frecuencia con la que los datos se actualizan se puede ajustar en la Raspberry. Por defecto, estos se envían a la base de datos cada hora, lo que permite mostrar una evolución de las condiciones climatológicas que pueda resultar útil al usuario.

## Objetivos[[edit](/pti/index.php?title=Categor%C3%ADa:Tweet-Weather&veaction=edit&section=3 "Edit section: Objetivos") | [edit source](/pti/index.php?title=Categor%C3%ADa:Tweet-Weather&action=edit&section=3 "Edit section: Objetivos")]

# Infraestructura[[edit](/pti/index.php?title=Categor%C3%ADa:Tweet-Weather&veaction=edit&section=4 "Edit section: Infraestructura") | [edit source](/pti/index.php?title=Categor%C3%ADa:Tweet-Weather&action=edit&section=4 "Edit section: Infraestructura")]

Nuestro infraestructura consiste de distintos componentes. En primer lugar tenemos un Arduino conectado a unos sensores de temperatura, humedad y presión. Este a su vez, se conecta con una Raspberry Pi para enviarle los datos recogidos por los sensores.

La Raspberry nos servirá para dos fines: almacenar estos datos meteorológicos en una base de datos SQL y para crear un servicio web que será el encargado de recibir las peticiones GET de la página web y la aplicación Android y responder a estas peticiones con los datos pedidos en formato JSon. Tanto la Base de datos como el servicio web se encuentran en dos contenedores independientes que se gestionan mediante Docker.

Para poder visualizar estos datos, al usuario se le ofrecen dos posibilidades, acceder a ellos mediante una página web y una aplicación Android.

## Tecnologías usadas[[edit](/pti/index.php?title=Categor%C3%ADa:Tweet-Weather&veaction=edit&section=5 "Edit section: Tecnologías usadas") | [edit source](/pti/index.php?title=Categor%C3%ADa:Tweet-Weather&action=edit&section=5 "Edit section: Tecnologías usadas")]

**Hardware:**

```
 - Sensores 
     Lluvia - HL83 
     Humedad, temperatura, índice de calor - DHT11
     Luz - LM393
 - Arduino Uno R3
 - Raspberry Pi con sistema operativo Raspbian

```

**Software:**

```
 - Servidor Amazon EC2 con LAMP (Linux, Apache, MySQL, PHP)
 - Base de datos MySQL
 - Android Studio (Java)
 - Twitter API
 - Webservice PHP + JSON
 - Librerías de sensores: DHT, Adafruit

```