## Contents

* [1 Introducción](#Introducci.C3.B3n)
  + [1.1 ¿Qué es GrooveLink?](#.C2.BFQu.C3.A9_es_GrooveLink.3F)
* [2 Tecnologias y arquitectura](#Tecnologias_y_arquitectura)
  + [2.1 Frontend](#Frontend)
  + [2.2 Backend](#Backend)
* [3 Infraestructura](#Infraestructura)

# Introducción[[edit](/pti/index.php?title=Categor%C3%ADa:GrooveLink&veaction=edit&section=1 "Edit section: Introducción") | [edit source](/pti/index.php?title=Categor%C3%ADa:GrooveLink&action=edit&section=1 "Edit section: Introducción")]

## ¿Qué es GrooveLink?[[edit](/pti/index.php?title=Categor%C3%ADa:GrooveLink&veaction=edit&section=2 "Edit section: ¿Qué es GrooveLink?") | [edit source](/pti/index.php?title=Categor%C3%ADa:GrooveLink&action=edit&section=2 "Edit section: ¿Qué es GrooveLink?")]

[![](images/300px-Groove\_Link\_Logo.png)](/pti/index.php/File:Groove_Link_Logo.png)

Logo de GrooveLink.

**GrooveLink** es una aplicación móvil innovadora diseñada para conectar a los usuarios a través de la música, promoviendo experiencias compartidas más allá de barreras físicas y culturales. Funciona mediante **notificaciones diarias** que invitan a los usuarios a compartir canciones con su grupo, las cuales son valoradas de forma anónima, generando un ranking diario y uno global dentro del grupo.   
 Motivados por la pasión por la música y la tecnología, el equipo creó esta plataforma para unir a los amantes de la música, con una interfaz intuitiva y funcionalidades avanzadas.

# Tecnologias y arquitectura[[edit](/pti/index.php?title=Categor%C3%ADa:GrooveLink&veaction=edit&section=3 "Edit section: Tecnologias y arquitectura") | [edit source](/pti/index.php?title=Categor%C3%ADa:GrooveLink&action=edit&section=3 "Edit section: Tecnologias y arquitectura")]

## Frontend[[edit](/pti/index.php?title=Categor%C3%ADa:GrooveLink&veaction=edit&section=4 "Edit section: Frontend") | [edit source](/pti/index.php?title=Categor%C3%ADa:GrooveLink&action=edit&section=4 "Edit section: Frontend")]

El frontend se centra en brindar una interfaz intuitiva y visualmente atractiva para los usuarios. Usamos:  
- **React Native con Expo**: Permite desarrollar una única base de código para múltiples plataformas, acelerando el desarrollo y pruebas mediante Expo Go, que facilita la visualización en dispositivos físicos o simuladores sin necesidad de compilación.  
- **React Navigation**: Biblioteca utilizada para gestionar la navegación de la aplicación. Incluye:

```
   -Stack Navigator: Navegación basada en pilas, adecuada para pantallas con flujo jerárquico.
   -Bottom Tab Navigator: Barra de pestañas en la parte inferior, que proporciona acceso rápido a secciones como Home, Grupos y Perfil del Usuario.

```

**Gestión de datos locales:**

-**AsyncStorage**: Herramienta utilizada para almacenar datos localmente, como tokens de sesión o configuraciones personalizadas del usuario, asegurando persistencia de datos incluso si la aplicación se cierra.

## Backend[[edit](/pti/index.php?title=Categor%C3%ADa:GrooveLink&veaction=edit&section=5 "Edit section: Backend") | [edit source](/pti/index.php?title=Categor%C3%ADa:GrooveLink&action=edit&section=5 "Edit section: Backend")]

El backend de GrooveLink garantiza un procesamiento eficiente, seguro y escalable, conectando todos los servicios necesarios.

**Tecnologías principales utilizadas:**

**Node.js con Express**: Framework minimalista para construir la API RESTful, manejando solicitudes de usuarios, lógica de negocio y conexión con la base de datos.
**MongoDB Atlas**: Base de datos NoSQL alojada en la nube, seleccionada por su flexibilidad y capacidad de escalar. Utiliza Mongoose como ODM para estructurar datos y definir esquemas validados.
**JWT (JSON Web Tokens)**: Proporciona autenticación segura con tokens de acceso (de corta duración) y refresh tokens (de larga duración).  
**Funciones principales implementadas:**

1.**Gestión de usuarios**:

-Registro y autenticación mediante bcrypt para el hashing de contraseñas.  
-Guardado de tokens de sesión y configuraciones personalizadas.  
2.**Gestión de grupos**:

-Creación de grupos únicos identificados por un groupCode generado con UUID.  
-Relación dinámica entre grupos y usuarios, incluyendo rankings diarios y globales.  
3.**Gestión de canciones**:

-Soporte para compartir canciones desde Spotify.  
-Almacenamiento de información como artista, álbum, URL de preview y votos asociados.  
-Actualización en tiempo real de rankings según los votos recibidos.  
4.**Integración con Spotify**:

-Proxy seguro para la comunicación con la API de Spotify.  
-Funciones de búsqueda y escucha de canciones.

[![](images/400px-Estructura\_arquitectura.png)](/pti/index.php/File:Estructura_arquitectura.png)

Estructura de la arquitectura con Spotify.

5.**Notificaciones diarias**:

-Implementadas con Firebase Cloud Messaging para enviar notificaciones.  
-Automatización de horarios aleatorios para compartir y votar canciones, gestionada con cron.  
6.**Seguridad**:

-Middleware para validar tokens de usuario en cada solicitud.  
-Protección contra ataques como CORS y exposición de datos sensibles.

# Infraestructura[[edit](/pti/index.php?title=Categor%C3%ADa:GrooveLink&veaction=edit&section=6 "Edit section: Infraestructura") | [edit source](/pti/index.php?title=Categor%C3%ADa:GrooveLink&action=edit&section=6 "Edit section: Infraestructura")]

Se optó por una infraestructura basada en **contenedores** y **clústeres**:

-**Docker**: Encapsulación de frontend y backend en contenedores individuales.  
-**Kubernetes**: Clúster con 3 nodos (1 maestro y 2 esclavos) para gestionar cargas y escalar.  
-**MetalLB**: Asignación de IPs públicas para exponer los servicios del clúster.  
División de servicios:

Backend y frontend desplegados en pods separados.
Base de datos en la nube mediante MongoDB Atlas.
Balanceo de carga gestionado por LoadBalancer y NodePort.