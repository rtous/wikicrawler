## 1. ¿En qué consiste el proeycto del Cloudy Media Center?[[edit](/pti/index.php?title=Categor%C3%ADa:CloudyMediaCenter&veaction=edit&section=1 "Edit section: 1. ¿En qué consiste el proeycto del Cloudy Media Center?") | [edit source](/pti/index.php?title=Categor%C3%ADa:CloudyMediaCenter&action=edit&section=1 "Edit section: 1. ¿En qué consiste el proeycto del Cloudy Media Center?")]

La tecnología ha entrado en las vidas de las personas y ha cambiado su manera de comunicarse, informarse o entretenerse. La sociedad está cada día más conectada, y en consecuencia, los hogares cada día tienen más dispositivos conectados a la red ofreciendo un sinfín de servicios. Por otro lado, cada vez es más la gente que se anima a montarse sus propios dispositivos, uniéndose a lo que se conoce como DIY (Do It Yourself) que es la práctica de la fabricación o preparación de alguna cosa por sí mismo.
Basándonos en estos hechos, la idea inicial del proyecto era crear un media center de software libre preparado para funcionar en un ordenador de placa reducida de bajo coste. Y así, dar la oportunidad a la gente de crearse su propio media center en casa, con solo una placa barata, nuestro software gratuito y un pequeño manual de instalación.

Pero la verdad es que ya existe mucho software libre de estas características, y tras conocer el proyecto Clommunity de Guifi.net, decidimos cambiar el objetivo de nuestro proyecto.
Uno de los objetivos principales del proyecto Clommunity es publicar una distribución GNU/Linux,llamada Cloudy, dirigida a los usuarios, para fomentar la transición y adopción del entorno Cloud en redes comunitarias. Intentando satisfacer requisitos como la distribución, para potenciar la distribución de servicios; la descentralización, para que los servicios no dependan del buen funcionamiento de una sola máquina y la facilidad de uso, para que el usuario pueda disfrutar de una buena experiencia.

Pensamos que a lo mejor podríamos aportar algo a este interesante proyecto y decidimos centrarnos en añadir a Cloudy un media center de software libre con el cual se pudiera reproducir contenido multimedia. Pero que también fomentara el entorno Cloud, pudiendo compartir contenido multimedia entre diferentes dispositivos.

Por lo tanto, el proyecto tiene como objetivo conseguir que los usuarios de redes comunitarias, como Guifi.net, puedan instalar en un ordenador de placa reducida de bajo coste la distribución Cloudy, y que uno de los servicios que esta ofrezca sea un media center que permita compartir contenido multimedia con los demás usuarios de la misma red comunitaria.

## 2. Escenario[[edit](/pti/index.php?title=Categor%C3%ADa:CloudyMediaCenter&veaction=edit&section=2 "Edit section: 2. Escenario") | [edit source](/pti/index.php?title=Categor%C3%ADa:CloudyMediaCenter&action=edit&section=2 "Edit section: 2. Escenario")]

El esquema de nuestro proyecto quedaría de la siguiente manera:

[File:Exemple.jpg](/pti/index.php?title=Special:Upload&wpDestFile=Exemple.jpg "File:Exemple.jpg")

La idea principal del proyecto es aprovechar la comunidad de guifi.net para compartir archivos de video ya sean películas o series y poder aprovechar todo ese contenido teniendo un media center en nuestra casa.

Para realizarlo, hemos usado un miniPC con el sistema operativo Cloudy y hemos instalado una base de datos MySQL para poder llevar un control de todo el contenido en nuestra red local. Este miniPC está conectado a la VPN de guifi.net mediante openVPN para poder coger el contenido que puedan estar compartiendo otros usuarios.

El miniPC también puede detectar los servicios que están siendo compartidos en la red de guifi.net por otros usuarios mediante Avahi. Por ejemplo, las carpetas compartidas de los otros usuarios que están en la red y así tener una librería extensa ya que podemos usar todo el contenido que los usuarios de guifi.net comparten. Además, también lleva instalado el media center Kodi para poder reproducir todo ese contenido en un televisor.

Para poder reproducir todo ese contenido, también usamos nuestro propio ordenador. El ordenador tiene Windows 8.1 y el media center Kodi instalado y lo conectamos a la VPN de guifi.net como hemos hecho con el miniPC mediante openVPN.

Para compartir las películas o series tenemos una placa olinuxino que esta fuera de nuestra red local conectada con openVPN a la VPN de guifi.net, como hemos hecho con los otros terminales, esa placa tiene instalado Samba para compartir las carpetas con el contenido multimedia y Avahi que es el encargado de anunciar el servicio de Samba para que otros usuarios de la VPN puedan encontrarlo.

El funcionamiento es el siguiente. La placa olinuxino tiene una serie de rutas con películas y series, que comparte en la red de guifi.net mediante Samba y anuncia con Avahi. El miniPC, que también está conectado a la VPN, puede ver esos archivos que comparte la placa una vez ha encontrado el servicio de Samba que la placa ha anunciado. Entonces explora el contenido de los directorios compartidos y lo registra en la base de datos, que se encarga de gestionar el contenido que más tarde Kodi se encargará de reproducir. El servidor MySQL registra también el estado de reproducción del contenido multimedia de la librería, indicando que contenido hemos visto y el instante que hemos dejado de ver una película para poder continuar su reproducción más tarde incluso desde otro dispositivo. Además, también nos muestra toda la información sobre la película: sinopsis, trailer, duración, actores, director, etc. El ordenador solo se encarga de reproducir el contenido registrado en la base de datos, para hacerlo se conecta al minPC mediante la red local y accede a la base de datos para coger el path de la película que queremos reproducir, entonces va a buscar el archivo allá donde este para reproducirlo, en el caso de que este esté en la placa, accederá a él mediante la VPN.

## 3. Conclusiones[[edit](/pti/index.php?title=Categor%C3%ADa:CloudyMediaCenter&veaction=edit&section=3 "Edit section: 3. Conclusiones") | [edit source](/pti/index.php?title=Categor%C3%ADa:CloudyMediaCenter&action=edit&section=3 "Edit section: 3. Conclusiones")]

Durante toda la realización del proyecto nos hemos encontrado con diferentes contratiempos, más de los que imaginábamos, que nos han llevado a modificar el objetivo inicial del proyecto para poder adaptarlo a las condiciones que han ido apareciendo.

Desde el principio sabíamos que trabajar sobre una placa como la A20-OLinuXino no sería nada fácil, ya que no es muy conocida y tiene una arquitectura ARM. Además sabíamos que teníamos que instalarle software que no estaba preparado para ella. La instalación del Cloudy sobre la placa ya llevo sus problemas, teniendo al final que instalar primero una distribución Debian y luego añadirle los paquetes de Cloudy.

Más tarde nos encontramos con el problema de que la placa no era capaz de utilizar Kodi de una forma fluida y agradable. Así que decidimos cambiar un poco la organización del proyecto, destinando la placa exclusivamente a la compartición de contenido multimedia y dejando las funciones de reproducción a los miniPc’s y Pc’s de la red.

Decidimos que la placa compartiese el contenido multimedia a través de Samba y también que alojara una base de datos que contenía información sobre los contenidos que compartía la placa. Pero finalmente decidimos adaptar nuestro escenario a uno más realista, y creímos que tenía mucho más sentido alojar la base de datos en la red local, como puede ser en casa, que en una comunidad de usuarios tan grande. Así que pusimos la base de datos en el miniPc.

También el hecho de trabajar en la red comunitaria de Guifi y de utilizar VPN’s nos han traído algún problema, como por ejemplo la imposibilidad de utilizar el móvil para gestionar Kodi. Ya que conectar el móvil a la red de Guifi, es una tarea complicada y poco práctica.

En cada paso que hemos dado nos hemos encontrado con diferentes obstáculos que hemos tenido que asumir y superar de la mejor forma posible. Pero al final el proyecto ha resultado ser muy provechoso, ya que hemos estado en contacto con numerosas tecnologías de las cuales muchas de ellas ni conocíamos.

Gracias a este proyecto nos hemos familiarizado con tecnologías de lo más interesantes y nos hemos dado cuento que a veces es más difícil hacer que diferentes tecnologías converjan que no crear una.

El resultado final ha sido satisfactorio ya que el objetivo de compartir recursos multimedia a través de una red comunitaria se ha cumplido.

Además, vemos muy positivo que nuestro proyecto tiene logros reales. Aportamos nuevos conocimientos al proyecto de Coudy, como por ejemplo, el manual de cómo instalar Cloudy en la placa computadora A20-OLinuXino-MICRO-4Gb, el cual se publicará. Fue muy interesante y enriquecedor colaborar con las personas de Guifi y Cloudy. El mundo de redes comunitarias, software libre y placas computadoras nos parece una combinación muy interesante ya que aunque a veces tecnológicamente difícil nos parece un mundo muy accesible por el código abierto, el bajo coste económico, y la comunidad colaborativa. Esperamos que un futuro podemos aportar más.