## Contents

* [1 Introducción](#Introducci.C3.B3n)
  + [1.1 ¿Qué es SensaReal?](#.C2.BFQu.C3.A9_es_SensaReal.3F)
* [2 Infraestructura](#Infraestructura)
  + [2.1 Sensores y comunicación](#Sensores_y_comunicaci.C3.B3n)
  + [2.2 Backend y procesamiento de datos](#Backend_y_procesamiento_de_datos)
  + [2.3 Frontend e interfaz de usuario](#Frontend_e_interfaz_de_usuario)
  + [2.4 Despliegue y orquestación](#Despliegue_y_orquestaci.C3.B3n)
* [3 Conclusión](#Conclusi.C3.B3n)

# Introducción[[edit](/pti/index.php?title=Categor%C3%ADa:Sensorial&veaction=edit&section=1 "Edit section: Introducción") | [edit source](/pti/index.php?title=Categor%C3%ADa:Sensorial&action=edit&section=1 "Edit section: Introducción")]

## ¿Qué es SensaReal?[[edit](/pti/index.php?title=Categor%C3%ADa:Sensorial&veaction=edit&section=2 "Edit section: ¿Qué es SensaReal?") | [edit source](/pti/index.php?title=Categor%C3%ADa:Sensorial&action=edit&section=2 "Edit section: ¿Qué es SensaReal?")]

SensaReal es una plataforma de monitoreo ambiental que permite a los usuarios visualizar en tiempo real las condiciones de temperatura y humedad en distintos entornos físicos. La solución fue diseñada para ser accesible, precisa y escalable, permitiendo su uso tanto en contextos domésticos como en laboratorios, invernaderos, almacenes, entre otros.

La idea central surge de la necesidad de contar con una herramienta confiable que permita registrar, analizar y alertar sobre condiciones ambientales fuera de lo esperado. Para ello, se construyó un sistema que integra sensores físicos, protocolos de comunicación eficientes para IoT, una base de datos relacional y una interfaz web moderna.

# Infraestructura[[edit](/pti/index.php?title=Categor%C3%ADa:Sensorial&veaction=edit&section=3 "Edit section: Infraestructura") | [edit source](/pti/index.php?title=Categor%C3%ADa:Sensorial&action=edit&section=3 "Edit section: Infraestructura")]

La arquitectura de SensaReal se basa en una estructura modular y distribuida, dividida en tres capas principales: la capa de datos (sensores y microcontroladores), la capa de lógica (backend y base de datos) y la capa de presentación (frontend web).

## Sensores y comunicación[[edit](/pti/index.php?title=Categor%C3%ADa:Sensorial&veaction=edit&section=4 "Edit section: Sensores y comunicación") | [edit source](/pti/index.php?title=Categor%C3%ADa:Sensorial&action=edit&section=4 "Edit section: Sensores y comunicación")]

En la base del sistema se encuentran sensores digitales \*\*DHT22\*\*, encargados de medir temperatura y humedad relativa con buena precisión y bajo consumo energético. Estos sensores están conectados a microcontroladores \*\*ESP32\*\*, dispositivos que combinan capacidad de procesamiento con conectividad WiFi.

El ESP32 toma lecturas del sensor cada pocos segundos y transmite la información utilizando el protocolo \*\*MQTT\*\*, un estándar liviano ideal para entornos IoT. Para ello, cada ESP32 se conecta a una red WiFi local y publica los datos en un \*\*broker Mosquitto\*\*, en tópicos identificados por cada sensor. Esta comunicación de tipo \*publisher/subscriber\* permite una transmisión eficiente, tolerante a desconexiones, y sin necesidad de solicitudes constantes desde el servidor.

## Backend y procesamiento de datos[[edit](/pti/index.php?title=Categor%C3%ADa:Sensorial&veaction=edit&section=5 "Edit section: Backend y procesamiento de datos") | [edit source](/pti/index.php?title=Categor%C3%ADa:Sensorial&action=edit&section=5 "Edit section: Backend y procesamiento de datos")]

El backend del sistema, desarrollado con \*\*Node.js\*\* y el framework \*\*Express\*\*, se encarga de recibir las mediciones desde el broker MQTT. Se encuentra suscripto a los tópicos correspondientes, y cada mensaje recibido se valida, se procesa y se guarda en una base de datos \*\*MySQL\*\*, junto con su respectivo timestamp.

Además de manejar los datos de los sensores, el backend ofrece una \*\*API RESTful\*\* que permite a los usuarios interactuar con el sistema: registrarse, iniciar sesión, registrar sensores, configurar umbrales de alerta y visualizar los datos históricos. Cada solicitud está protegida con \*\*tokens JWT\*\*, lo que garantiza sesiones seguras y sin estado.

El backend también implementa mecanismos de alerta: si una medición excede los límites configurados por el usuario, se genera automáticamente una alerta asociada, que puede luego ser visualizada en la interfaz o gestionada para futuras notificaciones.

## Frontend e interfaz de usuario[[edit](/pti/index.php?title=Categor%C3%ADa:Sensorial&veaction=edit&section=6 "Edit section: Frontend e interfaz de usuario") | [edit source](/pti/index.php?title=Categor%C3%ADa:Sensorial&action=edit&section=6 "Edit section: Frontend e interfaz de usuario")]

La capa de presentación fue desarrollada utilizando \*\*Vue 3\*\*, responsiva y centrada en la experiencia del usuario. La interfaz permite:

- Visualizar los sensores registrados y sus mediciones más recientes en gráficos actualizados en tiempo real.
- Configurar los sensores (nombre, ubicación, límites de temperatura y humedad).
- Gestionar alertas y estados.
- Acceder a datos históricos.

Para la gestión del estado se utilizó \*\*Pinia\*\*, lo que facilita mantener sincronizada la información del usuario, sensores y alertas. La comunicación con el backend se realiza exclusivamente mediante la API REST, utilizando tokens JWT para cada solicitud.

## Despliegue y orquestación[[edit](/pti/index.php?title=Categor%C3%ADa:Sensorial&veaction=edit&section=7 "Edit section: Despliegue y orquestación") | [edit source](/pti/index.php?title=Categor%C3%ADa:Sensorial&action=edit&section=7 "Edit section: Despliegue y orquestación")]

Todos los servicios de SensaReal (frontend, backend, base de datos y broker MQTT) están contenidos en \*\*Docker\*\* y desplegados utilizando \*\*Kubernetes\*\*. El despliegue se realizó sobre una infraestructura de \*\*máquinas virtuales\*\*, gestionadas a través de \*\*OpenNebula\*\*, siguiendo una arquitectura con un nodo maestro y dos worker nodes.

Se utilizaron archivos de configuración generados mediante \*\*kompose\*\* para traducir la estructura definida en `docker-compose.yaml` al formato necesario para Kubernetes. Los servicios públicos son expuestos mediante un proxy inverso \*\*nginx\*\*, que enruta el tráfico hacia los pods correspondientes, utilizando distintos puertos externos para acceder a frontend, backend y MQTT.

La base de datos es accedida únicamente a través de túneles SSH para garantizar la seguridad, y se aplicaron mecanismos como `imagePullPolicy: IfNotPresent`, almacenamiento local persistente, y monitoreo del estado de los pods mediante `kubectl`.

# Conclusión[[edit](/pti/index.php?title=Categor%C3%ADa:Sensorial&veaction=edit&section=8 "Edit section: Conclusión") | [edit source](/pti/index.php?title=Categor%C3%ADa:Sensorial&action=edit&section=8 "Edit section: Conclusión")]

SensaReal integra de manera eficiente hardware de bajo costo con software moderno y tecnologías de contenedorización, resultando en una solución práctica y escalable para el monitoreo ambiental.

Gracias al uso de tecnologías como \*\*ESP32\*\*, \*\*MQTT\*\*, \*\*Node.js\*\*, \*\*Vue 3\*\*, \*\*MySQL\*\*, \*\*Docker\*\* y \*\*Kubernetes\*\*, el proyecto ofrece una arquitectura robusta, extensible y alineada con buenas prácticas tanto en el desarrollo web como en entornos IoT.

El sistema no solo permite visualizar datos en tiempo real, sino también gestionar sensores y alertas de forma intuitiva, lo cual lo convierte en una herramienta útil para diversas aplicaciones donde el control ambiental es crítico.