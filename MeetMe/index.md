## Contents

* [1 Proyecto MEETME](#Proyecto_MEETME)
  + [1.1 1. Resumen de la propuesta](#1._Resumen_de_la_propuesta)
  + [1.2 2. Tecnologias utilizadas](#2._Tecnologias_utilizadas)
    - [1.2.1 Servidor](#Servidor)
    - [1.2.2 Web](#Web)
    - [1.2.3 Android](#Android)
    - [1.2.4 Diseños y edición de imagen](#Dise.C3.B1os_y_edici.C3.B3n_de_imagen)
  + [1.3 3. Video](#3._Video)

# Proyecto MEETME[[edit](/pti/index.php?title=Category:MeetMe&veaction=edit&section=1 "Edit section: Proyecto MEETME") | [edit source](/pti/index.php?title=Category:MeetMe&action=edit&section=1 "Edit section: Proyecto MEETME")]

[![Logo MeetMe.png](images/Logo\_MeetMe.png)](/pti/index.php/File:Logo_MeetMe.png)

Red social para Smart Phones enfocada en el uso de la Geo Localización.

Aplicación Android + Página Web

Motivación: Facilitar la gestión de la vida social de las personas.

## 1. Resumen de la propuesta[[edit](/pti/index.php?title=Category:MeetMe&veaction=edit&section=2 "Edit section: 1. Resumen de la propuesta") | [edit source](/pti/index.php?title=Category:MeetMe&action=edit&section=2 "Edit section: 1. Resumen de la propuesta")]

Nuestro objetivo principal, teniendo en cuenta la necesidad anteriormente mencionada, es proporcionar una herramienta para que un grupo de amigos pueda gestionar sus eventos y mantener toda la información sobre dicho evento en una única aplicación.
Por ello, entre las funcionalidades que incluiremos, destacamos:

* Geolocalización y servicios GPS para ver donde se situa el evento y donde están tus contactos situadosrespecto al evento. Trabajos similares en este ámbito podrían ser Latitude o Navigator.
* Gestión de mapas, utilizando la API de Google Maps, para situar el punto del evento. Obviamente, Google Maps no es que sea un trabajo similar, directamente es la base de este apartado.

## 2. Tecnologias utilizadas[[edit](/pti/index.php?title=Category:MeetMe&veaction=edit&section=3 "Edit section: 2. Tecnologias utilizadas") | [edit source](/pti/index.php?title=Category:MeetMe&action=edit&section=3 "Edit section: 2. Tecnologias utilizadas")]

### Servidor[[edit](/pti/index.php?title=Category:MeetMe&veaction=edit&section=4 "Edit section: Servidor") | [edit source](/pti/index.php?title=Category:MeetMe&action=edit&section=4 "Edit section: Servidor")]

* Sistema Operativo Ubuntu 10.04
* Apache 2.2.0 con módulo PHP 5.3.6
* Scripts internos de gestión del servidor escritos en Bash.
* Ubicado en un ordenador de sobremesa Pentium 4, 1GB de RAM, 80 GB de disco, y dedicado al 100%. Posibilidad de portar a mejores servidores en el futuro.
* Base de datos MySQL 5.1.62 gestionada con un phpMyAdmin versión 2.1.0

### Web[[edit](/pti/index.php?title=Category:MeetMe&veaction=edit&section=5 "Edit section: Web") | [edit source](/pti/index.php?title=Category:MeetMe&action=edit&section=5 "Edit section: Web")]

* Programación web en HTML.
* Maquetación del diseño utilizando CSS3.
* Uso de Librería JQuery realizada en JavaScript para el slider y el menú dinámico.
* Scripts PHP para la gestión de peticiones/modificaciones a la base de datos.
* PHP SESSION para gestionar i mantener el login de los usuarios.
* Subversión para la sincronización de ficheros.

### Android[[edit](/pti/index.php?title=Category:MeetMe&veaction=edit&section=6 "Edit section: Android") | [edit source](/pti/index.php?title=Category:MeetMe&action=edit&section=6 "Edit section: Android")]

* Desarrollo de la aplicación en Java usando las librerías Android.
* Uso de la API de Google Maps para gestión de mapas.
* Uso de clase ya creada y ajena a la API de Google para crear y gestionar calendarios.
* Uso y gestión de resultados de Web Services (PHP).
* Entorno de desarrollo Eclipse con SDK de Android.
* Subversión para la sincronización de ficheros.

### Diseños y edición de imagen[[edit](/pti/index.php?title=Category:MeetMe&veaction=edit&section=7 "Edit section: Diseños y edición de imagen") | [edit source](/pti/index.php?title=Category:MeetMe&action=edit&section=7 "Edit section: Diseños y edición de imagen")]

* Adobe Photoshop CS5.
* Adobe IIlustrator.

## 3. Video[[edit](/pti/index.php?title=Category:MeetMe&veaction=edit&section=8 "Edit section: 3. Video") | [edit source](/pti/index.php?title=Category:MeetMe&action=edit&section=8 "Edit section: 3. Video")]

[Video MeetMe](https://www.youtube.com/watch?v=3APBSej8Y-8&feature=youtu.be)