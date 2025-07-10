## Contents

* [1 Introducción](#Introducci.C3.B3n)
  + [1.1 ¿Qué es IoT Harvest?](#.C2.BFQu.C3.A9_es_IoT_Harvest.3F)
* [2 Infraestructura](#Infraestructura)
  + [2.1 **🌱** Sistema integrado en el huerto:](#.F0.9F.8C.B1_Sistema_integrado_en_el_huerto:)
  + [2.2 🖥️ Backend (Servidor Web con Node.js)](#.F0.9F.96.A5.EF.B8.8F_Backend_.28Servidor_Web_con_Node.js.29)
  + [2.3 🧠 Modelo de Machine Learning (Keras)](#.F0.9F.A7.A0_Modelo_de_Machine_Learning_.28Keras.29)
  + [2.4 🌐 Frontend (Interfaz de Usuario)](#.F0.9F.8C.90_Frontend_.28Interfaz_de_Usuario.29)
  + [2.5 🐳 Docker Compose](#.F0.9F.90.B3_Docker_Compose)
  + [2.6 Repositorio GitHub](#Repositorio_GitHub)

# Introducción[[edit](/pti/index.php?title=Categor%C3%ADa:IoTHarvest&veaction=edit&section=1 "Edit section: Introducción") | [edit source](/pti/index.php?title=Categor%C3%ADa:IoTHarvest&action=edit&section=1 "Edit section: Introducción")]

La agricultura de precisión surge como una respuesta innovadora a los desafíos actuales del sector agrícola, como el cambio climático, la escasez de agua y la necesidad de optimizar la producción de alimentos de manera sostenible. A través de la integración de tecnologías avanzadas, esta disciplina permite una gestión más eficiente de los cultivos, basada en la recopilación y análisis de datos en tiempo real. En este contexto, IoT Harvest es un proyecto que busca desarrollar un sistema de monitorización inteligente para huertos y cultivos, combinando sensores IoT, comunicación inalámbrica y herramientas de análisis de datos para mejorar la toma de decisiones agrícolas.

Gracias a su enfoque innovador, IoT Harvest ofrece una solución integral para el monitoreo y gestión inteligente de cultivos, proporcionando a los agricultores una visión completa y detallada del estado de sus tierras. Con acceso a información precisa y en tiempo real, los usuarios pueden tomar decisiones fundamentadas que optimicen el uso del agua, reduzcan desperdicios y maximicen el rendimiento de las cosechas. Esta capacidad de anticiparse a problemas potenciales, como el estrés hídrico o la aparición de plagas, convierte a IoT Harvest en una herramienta clave para una agricultura más eficiente y sostenible.

Además de la supervisión en tiempo real, IoT Harvest transforma los datos recopilados en información valiosa a través de gráficos interactivos y reportes detallados. La plataforma no solo ofrece métricas ambientales clave, sino que también incorpora un sistema de imágenes automatizado que permite evaluar visualmente la evolución de los cultivos. Gracias a esto, los agricultores pueden analizar tendencias, identificar patrones y recibir alertas inteligentes que faciliten la gestión de su producción sin necesidad de estar físicamente en el terreno.

En un mundo donde la digitalización está redefiniendo sectores clave, IoT Harvest representa el futuro de la agricultura conectada. Su diseño modular y escalable permite que cualquier agricultor, desde pequeños productores hasta grandes explotaciones, pueda beneficiarse de esta tecnología sin necesidad de conocimientos técnicos avanzados. Con una plataforma intuitiva y un enfoque basado en la automatización, IoT Harvest simplifica la toma de decisiones y empodera a los agricultores con herramientas de última generación para optimizar su trabajo y garantizar cultivos más sanos y productivos.

Este proyecto no solo responde a las necesidades actuales del sector agrícola, sino que también abre la puerta a un modelo de producción más eficiente y respetuoso con el medio ambiente. Al integrar tecnología de punta en el corazón de la agricultura, IoT Harvest demuestra que la innovación y la sostenibilidad pueden ir de la mano, asegurando un futuro más inteligente y resiliente para la producción de alimentos.

## ¿Qué es IoT Harvest?[[edit](/pti/index.php?title=Categor%C3%ADa:IoTHarvest&veaction=edit&section=2 "Edit section: ¿Qué es IoT Harvest?") | [edit source](/pti/index.php?title=Categor%C3%ADa:IoTHarvest&action=edit&section=2 "Edit section: ¿Qué es IoT Harvest?")]

IoT Harvest es una herramienta diseñada para acercar la agricultura inteligente a cualquier tipo de cultivo, desde una simple maceta hasta grandes extensiones de terreno. Ofrece a los usuarios una interfaz compacta y minimalista que permite monitorizar, de un solo vistazo, los parámetros clave de su cultivo.

La plataforma muestra la evolución de la temperatura del aire, la temperatura del suelo y la humedad ambiental durante las últimas 24 horas. También proporciona lecturas en tiempo real de estos mismos valores, una imagen actual del cultivo acompañada de un diagnóstico automatizado sobre su estado de salud, y una predicción meteorológica precisa basada en su ubicación.

Con IoT Harvest, la tecnología se pone al servicio del campo para facilitar decisiones informadas, optimizar recursos y promover cultivos más saludables y sostenibles. Porque creemos que el futuro de la agricultura empieza con datos inteligentes y herramientas accesibles para todos.

[![Interfaz Usuario IoT Harvest.jpg](images/776px-Interfaz\_Usuario\_IoT\_Harvest.jpg)](/pti/index.php/File:Interfaz_Usuario_IoT_Harvest.jpg)

# Infraestructura[[edit](/pti/index.php?title=Categor%C3%ADa:IoTHarvest&veaction=edit&section=3 "Edit section: Infraestructura") | [edit source](/pti/index.php?title=Categor%C3%ADa:IoTHarvest&action=edit&section=3 "Edit section: Infraestructura")]

### **🌱** Sistema integrado en el huerto:[[edit](/pti/index.php?title=Categor%C3%ADa:IoTHarvest&veaction=edit&section=4 "Edit section: 🌱 Sistema integrado en el huerto:") | [edit source](/pti/index.php?title=Categor%C3%ADa:IoTHarvest&action=edit&section=4 "Edit section: 🌱 Sistema integrado en el huerto:")]

* Módulo ESP32-CAM que toma fotos de las plantas y las envía al Servidor Web mediante HTTP.

* Sistema LoRa formado por:
  + Un ESP32 (Sender) que toma lecturas de los sensores y las envía al Gateway a través de LoRa.
  + Un ESP32 (Gateway) que recibe estos datos y los envía por HTTP.

### 🖥️ Backend (Servidor Web con Node.js)[[edit](/pti/index.php?title=Categor%C3%ADa:IoTHarvest&veaction=edit&section=5 "Edit section: 🖥️ Backend (Servidor Web con Node.js)") | [edit source](/pti/index.php?title=Categor%C3%ADa:IoTHarvest&action=edit&section=5 "Edit section: 🖥️ Backend (Servidor Web con Node.js)")]

* Recibe tanto imágenes como datos de sensores.
* Procesa la información y:
  + Guarda imágenes y datos en MongoDB optimizada para sistemas IoT (time series).
  + Sube imágenes a Cloudinary para almacenamiento en la nube.
  + Usa un modelo en Keras (machine learning) para clasificar la salud de las plantas

### 🧠 Modelo de Machine Learning (Keras)[[edit](/pti/index.php?title=Categor%C3%ADa:IoTHarvest&veaction=edit&section=6 "Edit section: 🧠 Modelo de Machine Learning (Keras)") | [edit source](/pti/index.php?title=Categor%C3%ADa:IoTHarvest&action=edit&section=6 "Edit section: 🧠 Modelo de Machine Learning (Keras)")]

* Entrenado para analizar imágenes de plantas.
* Categoriza el estado de salud de cada planta con base en las imágenes recibidas.

### 🌐 Frontend (Interfaz de Usuario)[[edit](/pti/index.php?title=Categor%C3%ADa:IoTHarvest&veaction=edit&section=7 "Edit section: 🌐 Frontend (Interfaz de Usuario)") | [edit source](/pti/index.php?title=Categor%C3%ADa:IoTHarvest&action=edit&section=7 "Edit section: 🌐 Frontend (Interfaz de Usuario)")]

* Aplicación hecha con Vite + React.
* Se comunica con el backend para mostrar:
  + Datos de sensores.
  + Imágenes y resultados del modelo.
  + Gráficas generadas con MongoDB Charts para visualizar la información.

### 🐳 Docker Compose[[edit](/pti/index.php?title=Categor%C3%ADa:IoTHarvest&veaction=edit&section=8 "Edit section: 🐳 Docker Compose") | [edit source](/pti/index.php?title=Categor%C3%ADa:IoTHarvest&action=edit&section=8 "Edit section: 🐳 Docker Compose")]

* Infraestructura contenida en 3 contenedores para facilitar el despliegue: Frontend, Backend y Modelo.

[![](images/715px-Esquema\_tecnologias\_del\_Proyecto.png)](/pti/index.php/File:Esquema_tecnologias_del_Proyecto.png)

Esquema de tecnologías utilizadas para la implementación de IoT Harvest.

## Repositorio GitHub[[edit](/pti/index.php?title=Categor%C3%ADa:IoTHarvest&veaction=edit&section=9 "Edit section: Repositorio GitHub") | [edit source](/pti/index.php?title=Categor%C3%ADa:IoTHarvest&action=edit&section=9 "Edit section: Repositorio GitHub")]

El código completo del proyecto está disponible en el siguiente repositorio de GitHub: <https://github.com/ermias-vm/IoTHarvest>.

El repositorio está organizado en cinco carpetas principales: frontend, backend, scripts, model y hardware. Cada una incluye un archivo README.md donde se explica su contenido y funcionamiento.

Además, en la raíz del repositorio se encuentra una guía paso a paso para instalar las dependencias necesarias y poner en marcha la aplicación.