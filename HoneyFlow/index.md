[![](images/400px-Logo\_HoneyFlow.jpg)](/pti/index.php/File:Logo_HoneyFlow.jpg)

Logo HoneyFlow

## Contents

* [1 Introducción](#Introducci.C3.B3n)
  + [1.1 ¿Qué es un Honeypot?](#.C2.BFQu.C3.A9_es_un_Honeypot.3F)
  + [1.2 Objetivo del Proyecto](#Objetivo_del_Proyecto)
* [2 Funcionalidades Principales](#Funcionalidades_Principales)
* [3 Honeypots Utilizados](#Honeypots_Utilizados)
* [4 Implementación Técnica](#Implementaci.C3.B3n_T.C3.A9cnica)
* [5 Beneficios de HoneyFlow](#Beneficios_de_HoneyFlow)
* [6 Código del Proyecto](#C.C3.B3digo_del_Proyecto)

# Introducción[[edit](/pti/index.php?title=Categor%C3%ADa:HoneyFlow&veaction=edit&section=1 "Edit section: Introducción") | [edit source](/pti/index.php?title=Categor%C3%ADa:HoneyFlow&action=edit&section=1 "Edit section: Introducción")]

HoneyFlow es una innovadora plataforma de seguridad informática diseñada para simplificar la orquestación y gestión de honeypots con diversas características y objetivos.

## ¿Qué es un Honeypot?[[edit](/pti/index.php?title=Categor%C3%ADa:HoneyFlow&veaction=edit&section=2 "Edit section: ¿Qué es un Honeypot?") | [edit source](/pti/index.php?title=Categor%C3%ADa:HoneyFlow&action=edit&section=2 "Edit section: ¿Qué es un Honeypot?")]

Un honeypot es una herramienta de seguridad que actúa como señuelo, simulando ser un sistema vulnerable para atraer a atacantes y estudiar sus métodos. Esto permite identificar y analizar actividades maliciosas sin poner en riesgo los sistemas reales.

## Objetivo del Proyecto[[edit](/pti/index.php?title=Categor%C3%ADa:HoneyFlow&veaction=edit&section=3 "Edit section: Objetivo del Proyecto") | [edit source](/pti/index.php?title=Categor%C3%ADa:HoneyFlow&action=edit&section=3 "Edit section: Objetivo del Proyecto")]

El objetivo principal de HoneyFlow es facilitar la implementación y gestión de honeypots, permitiendo una supervisión constante y detallada de posibles ataques. La plataforma no solo despliega estos honeypots, sino que también integra un sistema de detección propio capaz de identificar diversos tipos de ataques en tiempo real.

[![](images/800px-Esquema\_HoneyFlow.jpg)](/pti/index.php/File:Esquema_HoneyFlow.jpg)

Esquema HoneyFlow

# Funcionalidades Principales[[edit](/pti/index.php?title=Categor%C3%ADa:HoneyFlow&veaction=edit&section=4 "Edit section: Funcionalidades Principales") | [edit source](/pti/index.php?title=Categor%C3%ADa:HoneyFlow&action=edit&section=4 "Edit section: Funcionalidades Principales")]

**Orquestación de Honeypots:** HoneyFlow permite la configuración y despliegue de honeypots de manera sencilla y efectiva. Estos honeypots están diseñados para atraer a posibles atacantes, registrando sus actividades para un análisis posterior.

**Detección de Ataques:** La plataforma incluye un sistema avanzado de detección que monitoriza el tráfico y las actividades en los honeypots, identificando patrones de ataques y clasificándolos según su tipo.

**Visualización de Datos:** Toda la información recopilada por los honeypots y el sistema de detección se presenta de manera clara y comprensible a través de tablas y gráficos. Esto facilita el análisis y la comprensión de los datos, ayudando a los administradores a tomar decisiones informadas.

[![](images/800px-Front-end-inicio\_HoneyFlow.jpg)](/pti/index.php/File:Front-end-inicio_HoneyFlow.jpg)

Inicio Front-End

# Honeypots Utilizados[[edit](/pti/index.php?title=Categor%C3%ADa:HoneyFlow&veaction=edit&section=5 "Edit section: Honeypots Utilizados") | [edit source](/pti/index.php?title=Categor%C3%ADa:HoneyFlow&action=edit&section=5 "Edit section: Honeypots Utilizados")]

**Cowrie:**
Cowrie es un honeypot de interacción media para SSH y Telnet que simula un servidor Debian 5.0 con un sistema de archivos falso. Permite a los atacantes crear, modificar y eliminar archivos, y guardar sesiones y archivos descargados para su análisis. Admite conexiones SSH, SFTP, SCP, y SMTP, además de guardar registros de actividad en formato JSON.

**Mailoney:**
Mailoney es un honeypot SMTP de baja interacción escrito en Python, con tres módulos: "open\_relay" para registrar correos enviados, "postfix\_creds" para registrar intentos de inicio de sesión, y "schizo\_open\_relay" para registrar toda la interacción. Exponemos el puerto 25 para capturar correos electrónicos.

**Heralding:**
Heralding es un honeypot de baja interacción que recopila credenciales emulando servicios de inicio de sesión como FTP, SSH, Telnet, SMTP, HTTP, y otros.

[![](images/800px-Front-end-configuracion\_HoneyFlow.jpg)](/pti/index.php/File:Front-end-configuracion_HoneyFlow.jpg)

Configuración Honeypots Front-End

# Implementación Técnica[[edit](/pti/index.php?title=Categor%C3%ADa:HoneyFlow&veaction=edit&section=6 "Edit section: Implementación Técnica") | [edit source](/pti/index.php?title=Categor%C3%ADa:HoneyFlow&action=edit&section=6 "Edit section: Implementación Técnica")]

Los honeypots de HoneyFlow están expuestos al exterior y se ejecutan en pods de Kubernetes dentro de una máquina virtual proporcionada por la FIB. Esto asegura que cualquier atacante potencial pueda interactuar con los honeypots en cualquier momento, proporcionando un flujo constante de datos para análisis.

[![](images/800px-Front-end-datos\_HoneyFlow.jpg)](/pti/index.php/File:Front-end-datos_HoneyFlow.jpg)

Muestra de datos honeypot Cowrie Front-End

# Beneficios de HoneyFlow[[edit](/pti/index.php?title=Categor%C3%ADa:HoneyFlow&veaction=edit&section=7 "Edit section: Beneficios de HoneyFlow") | [edit source](/pti/index.php?title=Categor%C3%ADa:HoneyFlow&action=edit&section=7 "Edit section: Beneficios de HoneyFlow")]

**Seguridad Mejorada:** Al atraer y estudiar a los atacantes, se pueden identificar y mitigar amenazas antes de que afecten a los sistemas reales.

**Análisis Detallado:** Los datos capturados se analizan y se presentan de forma accesible, permitiendo a los profesionales de seguridad comprender mejor las amenazas.

**Implementación Sencilla:** La plataforma está diseñada para ser fácil de usar, facilitando la creación y gestión de honeypots sin necesidad de conocimientos técnicos.

# Código del Proyecto[[edit](/pti/index.php?title=Categor%C3%ADa:HoneyFlow&veaction=edit&section=8 "Edit section: Código del Proyecto") | [edit source](/pti/index.php?title=Categor%C3%ADa:HoneyFlow&action=edit&section=8 "Edit section: Código del Proyecto")]

Podéis visualizar el código de HoneyFlow mediante el repositorio de GitHub. ¡Las contribuciones son bienvenidas! Si deseas mejorar HoneyFlow, haz un fork del repositorio, crea una rama con tus cambios y envía un pull request.

Link del repositorio: <https://github.com/marcelca02/Honeyflow/>