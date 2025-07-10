## Contents

* [1 Introducción](#Introducci.C3.B3n)
* [2 Objetivos del proyecto](#Objetivos_del_proyecto)
* [3 Enfoque y método seguido](#Enfoque_y_m.C3.A9todo_seguido)
* [4 Arquitectura del proyecto](#Arquitectura_del_proyecto)
  + [4.1 Asistente virtual](#Asistente_virtual)
  + [4.2 Back-end](#Back-end)
  + [4.3 Front-end](#Front-end)
  + [4.4 Demo](#Demo)

# Introducción[[edit](/pti/index.php?title=Categor%C3%ADa:Elira&veaction=edit&section=1 "Edit section: Introducción") | [edit source](/pti/index.php?title=Categor%C3%ADa:Elira&action=edit&section=1 "Edit section: Introducción")]

El propósito de nuestro proyecto de PTI es crear un dispositivo con funcionalidades análogas a las ofrecidas por Alexa de Amazon o Google Home. Para esto, emplearemos tecnologías de código abierto. Específicamente, usaremos LlaMa 2, el modelo de lenguaje de código abierto de Facebook, que se ocupará de procesar y responder a comandos de voz. El dispositivo se construirá utilizando una Raspberry Pi como base.
Inspirándose en productos existentes, nuestro proyecto también incluirá una aplicación móvil, que permitirá configurar y acceder al historial del dispositivo basado en Raspberry Pi.

# Objetivos del proyecto[[edit](/pti/index.php?title=Categor%C3%ADa:Elira&veaction=edit&section=2 "Edit section: Objetivos del proyecto") | [edit source](/pti/index.php?title=Categor%C3%ADa:Elira&action=edit&section=2 "Edit section: Objetivos del proyecto")]

El proyecto tiene varios objetivos tecnológicos, incluyendo:

● Integrar distintos modelos de lenguaje natural (como LlaMa 2), tecnologías de detección de palabras clave, y sistemas de conversión de voz a texto y de texto a voz, en una aplicación práctica.

● Autoalojar un modelo de lenguaje natural (LLM, LlaMa 2 en nuestro caso).

● Desarrollar software basado en la arquitectura cliente-servidor.

● Crear una aplicación para smartphones.

● Desarrollar software específico para dispositivos de IoT, como Raspberry Pi.

● Emplear bases de datos NoSQL, específicamente Cassandra DB, para tener un entorno que esté preparado para un despliegue real.

Este proyecto se inspira en asistentes virtuales conocidos como Alexa, Siri y Google Assistant, así como en otros proyectos menos conocidos que utilizan la Raspberry Pi, como Mycroft o Rhasspy.

# Enfoque y método seguido[[edit](/pti/index.php?title=Categor%C3%ADa:Elira&veaction=edit&section=3 "Edit section: Enfoque y método seguido") | [edit source](/pti/index.php?title=Categor%C3%ADa:Elira&action=edit&section=3 "Edit section: Enfoque y método seguido")]

Como son tres componentes independientes unos de los otros hicimos el desarrollo en paralelo, y no hubo contacto entre ellos hasta que se hizo la integración. El asistente virtual no necesita de un back-end para poder funcionar, ya que siempre se puede usar un mock-up server para testearlo. Para el front-end podemos aplicar la lógica anterior. Para testear el back-end lo dividimos en dos partes: las llamadas a base de datos, las cuales se implementaron al inicio de todo y se testearon todas con Postman, y posteriormente el endpoint de LlaMa que se testeó por partes durante la integración. La integración se testeó usando una VPN de WireGuard donde todos los componentes estaban conectados como si
fuera una red privada.

# Arquitectura del proyecto[[edit](/pti/index.php?title=Categor%C3%ADa:Elira&veaction=edit&section=4 "Edit section: Arquitectura del proyecto") | [edit source](/pti/index.php?title=Categor%C3%ADa:Elira&action=edit&section=4 "Edit section: Arquitectura del proyecto")]

[![Firefox gOLxLRsUfj.png](images/Firefox\_gOLxLRsUfj.png)](/pti/index.php/File:Firefox_gOLxLRsUfj.png)

## Asistente virtual[[edit](/pti/index.php?title=Categor%C3%ADa:Elira&veaction=edit&section=5 "Edit section: Asistente virtual") | [edit source](/pti/index.php?title=Categor%C3%ADa:Elira&action=edit&section=5 "Edit section: Asistente virtual")]

Este asistente está diseñado para operar idealmente en una Raspberry Pi, aunque es lo suficientemente versátil como para funcionar en cualquier dispositivo que soporte Python, es decir, prácticamente todos los sistemas operativos.
Escrito en Python, el asistente se encargará de diversas tareas relacionadas con el procesamiento de voz y la interacción con el back-end del servidor mediante HTTP.

## Back-end[[edit](/pti/index.php?title=Categor%C3%ADa:Elira&veaction=edit&section=6 "Edit section: Back-end") | [edit source](/pti/index.php?title=Categor%C3%ADa:Elira&action=edit&section=6 "Edit section: Back-end")]

Se desarrollará utilizando Node.js. Interactúa con la base de datos Cassandra DB,
seleccionada por su alta escalabilidad, gran resistencia a fallos y otras características
avanzadas. Dicho back-end realizará:

• La gestión de usuarios y credenciales.

• CRUD al historial de preguntas.

• La transformación de la voz del usuario a texto usando un modelo de ASR (STT).

• La integración de un modelo de LLM (Large Language Model) y una inteligencia artificial open source para procesar consultas, en este caso se trata del modelo LlaMa 2 de Meta.

• La transformación de texto a voz para ser reproducido en el asistente virtual mediante el uso de un modelo de TTS.

Este sistema proporcionará funcionalidades de conversión de voz a texto y de texto a voz, interactuando con varias librerías de uso gratuito.

## Front-end[[edit](/pti/index.php?title=Categor%C3%ADa:Elira&veaction=edit&section=7 "Edit section: Front-end") | [edit source](/pti/index.php?title=Categor%C3%ADa:Elira&action=edit&section=7 "Edit section: Front-end")]

Su diseño se realizará utilizando Figma, una herramienta que permite crear interfaces de usuario de manera intuitiva. Una vez diseñado, se exportará a Flutter, un framework de código abierto que soporta Android, iOS y web. Esto permitirá la implementación de funcionalidades diversas, incluyendo la capacidad de hacer peticiones HTTPS, lo que hace adaptable el uso de las funcionalidades del back-end para su uso en diversos lenguajes de programación.
Es importante destacar que, aunque en la propuesta del proyecto se menciona la posibilidad de integrar funcionalidades de Bluetooth para la autenticación del asistente virtual, esta característica queda pendiente de ser implementada fuera del marco de esta PoC.

## Demo[[edit](/pti/index.php?title=Categor%C3%ADa:Elira&veaction=edit&section=8 "Edit section: Demo") | [edit source](/pti/index.php?title=Categor%C3%ADa:Elira&action=edit&section=8 "Edit section: Demo")]

youtu.be/FV1PtHJJXpE

[![](images/Frame.png)](/pti/index.php/File:Frame.png)

Link to the demo video