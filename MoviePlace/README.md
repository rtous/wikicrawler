[![](images/440px-Captura\_de\_pantalla\_de\_2021-12-21\_19-40-22.png)](/pti/index.php/File:Captura_de_pantalla_de_2021-12-21_19-40-22.png)

Logo del proyecto.

## Contents

* [1 Introducción](#Introducci.C3.B3n)
  + [1.1 ¿Qué es Movie Place?](#.C2.BFQu.C3.A9_es_Movie_Place.3F)
* [2 Infraestructura](#Infraestructura)
  + [2.1 Tecnologías utilizadas](#Tecnolog.C3.ADas_utilizadas)

# Introducción[[edit](/pti/index.php?title=Categor%C3%ADa:MoviePlace&veaction=edit&section=1 "Edit section: Introducción") | [edit source](/pti/index.php?title=Categor%C3%ADa:MoviePlace&action=edit&section=1 "Edit section: Introducción")]

En esta Wiki queremos introducir nuestro proyecto desarrollado, así como los puntos clave de su desarrollo y arquitectura.

## ¿Qué es Movie Place?[[edit](/pti/index.php?title=Categor%C3%ADa:MoviePlace&veaction=edit&section=2 "Edit section: ¿Qué es Movie Place?") | [edit source](/pti/index.php?title=Categor%C3%ADa:MoviePlace&action=edit&section=2 "Edit section: ¿Qué es Movie Place?")]

[![](images/Captura\_de\_pantalla\_de\_2021-12-21\_20-01-52.png)](/pti/index.php/File:Captura_de_pantalla_de_2021-12-21_20-01-52.png)

Vista del Home de Movie Place.

Movie Place es una aplicación pensada para que los usuarios puedan sentirse por un momento, los protagonistas de sus películas favoritas. Ya que nuestra aplicación, mediante la recogida de datos de diferentes géneros de películas y el almacenamiento de los mismos en una base de datos, recomendará diferentes películas, según la ubicación del usuario y según la cualificación que tengan las películas. Lo primero, es posible gracias a la integración a nuestra aplicación de la API de Google Maps.

Una vez que el usuario haya elegido la película que quiere visitar, se le mostrarán las diferentes escenas que se han grabado y tienen un sitio real en el que se grabó. También se escuchará la banda sonora, para hacer una integración más real con la película, para hacer eso se ha utilizado la API de Spotify.

Con este proyecto se ha intentado conseguir que nuestros usuarios puedan conseguir una sensación de que forman parte de algunas de las escenas de sus películas favoritas. Además, pensamos que es una alternativa a la hora de visitar una ciudad o pueblo, de forma totalmente diferente a la tradicional, si estás de turismo.

# Infraestructura[[edit](/pti/index.php?title=Categor%C3%ADa:MoviePlace&veaction=edit&section=3 "Edit section: Infraestructura") | [edit source](/pti/index.php?title=Categor%C3%ADa:MoviePlace&action=edit&section=3 "Edit section: Infraestructura")]

Nuestra infraestructura consiste en alguns elementos que juntamente forman el *frontend* y el backend. Frontend: Hemos desenvolupado una aplicación Android usando Android Studio, Kotlin y XML. Backend: Sobre una màquina virtual de la FIB hemos hecho un servidor con Node.js y Express, para poner una base de datos con MongoDB.

[![](images/701px-Captura\_de\_pantalla\_de\_2021-12-21\_19-54-24.png)](/pti/index.php/File:Captura_de_pantalla_de_2021-12-21_19-54-24.png)

Arquitectura del proyecto.

## Tecnologías utilizadas[[edit](/pti/index.php?title=Categor%C3%ADa:MoviePlace&veaction=edit&section=4 "Edit section: Tecnologías utilizadas") | [edit source](/pti/index.php?title=Categor%C3%ADa:MoviePlace&action=edit&section=4 "Edit section: Tecnologías utilizadas")]

La lista de las tecnologías que se han utilizado son las siguientes:
-Android Studio: IDE para el desarrollo nativo de aplicaciones Android, hemos decidido utilizar el lenguaje Kotlin para el desarrollo y XML para los layouts principalmente.
-Spotify API: API para poder construir una reproducción musical de las bandas sonoras, integrada con nuestra aplicación.
-Google Maps API: es la API utilizada para poder coger la ubicación del usuario y poder visualizar y recomendar películas según su ubicación, entre otras cosas.
-MongoDB: sistema de base de datos NoSQL orientada a objetos, que nos permite guardar toda la información de nuestra aplicación.
-Node.js y Express.js: entorno de tiempo de ejecución de JavaScript que ayuda a tener entre otras cosas un manejo simultáneo de diferentes peticiones.