[![](images/Screenshot\_from\_2024-12-23\_13-50-21.png)](/pti/index.php/File:Screenshot_from_2024-12-23_13-50-21.png)

Logo FIBerBot

## Contents

* [1 Introducción](#Introducci.C3.B3n)
  + [1.1 ¿Qué es FIBerBot?](#.C2.BFQu.C3.A9_es_FIBerBot.3F)
* [2 Arquitectura y Tecnologías utilizadas](#Arquitectura_y_Tecnolog.C3.ADas_utilizadas)
  + [2.1 Frontend](#Frontend)
    - [2.1.1 Tailwind CSS](#Tailwind_CSS)
    - [2.1.2 JavaScript](#JavaScript)
  + [2.2 Backend](#Backend)
    - [2.2.1 Flask](#Flask)
    - [2.2.2 Ollama](#Ollama)
    - [2.2.3 Langchain](#Langchain)
    - [2.2.4 SQLite](#SQLite)
    - [2.2.5 ChromaDB](#ChromaDB)
    - [2.2.6 Groq Cloud](#Groq_Cloud)
    - [2.2.7 DOCKER](#DOCKER)

# Introducción[[edit](/pti/index.php?title=Categor%C3%ADa:FIBerBot&veaction=edit&section=1 "Edit section: Introducción") | [edit source](/pti/index.php?title=Categor%C3%ADa:FIBerBot&action=edit&section=1 "Edit section: Introducción")]

Estos últimos años los LLMs (Large Language Models) han demostrado ser una herramienta muy útil para dar asistencia a las consultas del día a día de sus usuarios, causando un gran impacto en la forma que accedemos a la información. Los LLMs han impulsado el desarrollo de herramientas capaces de generar respuestas en lenguaje natural, dando paso a aplicaciones conversacionales.

El objectivo de este proyecto es desarrollar un asistente conversacional especializado en la FIB. Aprovechando técnicas recientes, como NLP (Natural Language Processing), RAG (Retrieval-Augmented Generation), bases de datos vectoriales, embeddings, AI Agent y Tool/function Calling, se busca no solo mejorar la calidad de las respuestas, sino también dar información más personalizada y exacta a los usuarios.

## ¿Qué es FIBerBot?[[edit](/pti/index.php?title=Categor%C3%ADa:FIBerBot&veaction=edit&section=2 "Edit section: ¿Qué es FIBerBot?") | [edit source](/pti/index.php?title=Categor%C3%ADa:FIBerBot&action=edit&section=2 "Edit section: ¿Qué es FIBerBot?")]

FIBerbot es un asistente conversacional capaz de comprender y responder a estas cuestiones concretas presenta un gran valor tanto para estudiantes como para el personal de la facultad, facilitando así el acceso ágil a información específica.

# Arquitectura y Tecnologías utilizadas[[edit](/pti/index.php?title=Categor%C3%ADa:FIBerBot&veaction=edit&section=3 "Edit section: Arquitectura y Tecnologías utilizadas") | [edit source](/pti/index.php?title=Categor%C3%ADa:FIBerBot&action=edit&section=3 "Edit section: Arquitectura y Tecnologías utilizadas")]

[![](images/592px-Screenshot\_from\_2024-12-23\_13-44-23.png)](/pti/index.php/File:Screenshot_from_2024-12-23_13-44-23.png)

Diagrama de tecnologías y funcionamiento del proceso de RAG

## Frontend[[edit](/pti/index.php?title=Categor%C3%ADa:FIBerBot&veaction=edit&section=4 "Edit section: Frontend") | [edit source](/pti/index.php?title=Categor%C3%ADa:FIBerBot&action=edit&section=4 "Edit section: Frontend")]

### Tailwind CSS[[edit](/pti/index.php?title=Categor%C3%ADa:FIBerBot&veaction=edit&section=5 "Edit section: Tailwind CSS") | [edit source](/pti/index.php?title=Categor%C3%ADa:FIBerBot&action=edit&section=5 "Edit section: Tailwind CSS")]

Framework sencillo que genera a partir de todos las clases y ficheros HTML

### JavaScript[[edit](/pti/index.php?title=Categor%C3%ADa:FIBerBot&veaction=edit&section=6 "Edit section: JavaScript") | [edit source](/pti/index.php?title=Categor%C3%ADa:FIBerBot&action=edit&section=6 "Edit section: JavaScript")]

Se utiliza para generar la interface con html.

## Backend[[edit](/pti/index.php?title=Categor%C3%ADa:FIBerBot&veaction=edit&section=7 "Edit section: Backend") | [edit source](/pti/index.php?title=Categor%C3%ADa:FIBerBot&action=edit&section=7 "Edit section: Backend")]

### Flask[[edit](/pti/index.php?title=Categor%C3%ADa:FIBerBot&veaction=edit&section=8 "Edit section: Flask") | [edit source](/pti/index.php?title=Categor%C3%ADa:FIBerBot&action=edit&section=8 "Edit section: Flask")]

Framework para desarrollo web en Python. Gracias a su escalabilidad y su facilidad de uso ideal para crear la aplicación principal.

### Ollama[[edit](/pti/index.php?title=Categor%C3%ADa:FIBerBot&veaction=edit&section=9 "Edit section: Ollama") | [edit source](/pti/index.php?title=Categor%C3%ADa:FIBerBot&action=edit&section=9 "Edit section: Ollama")]

Plataforma que permite interactuar con LLMs de manera rapida. Gracias a su API permite generar texto, procesar en lenguaje natural y generar respuestas con información adicional del contenido enviado.

### Langchain[[edit](/pti/index.php?title=Categor%C3%ADa:FIBerBot&veaction=edit&section=10 "Edit section: Langchain") | [edit source](/pti/index.php?title=Categor%C3%ADa:FIBerBot&action=edit&section=10 "Edit section: Langchain")]

Framework que se encarga de conectar los diferentes componentes tales como la API de flask, los modelos y la base de datos vectorial para generar texto con IA.

### SQLite[[edit](/pti/index.php?title=Categor%C3%ADa:FIBerBot&veaction=edit&section=11 "Edit section: SQLite") | [edit source](/pti/index.php?title=Categor%C3%ADa:FIBerBot&action=edit&section=11 "Edit section: SQLite")]

Sirve para guardar la persistencia de los mensajes y chats en una base de datos para mostrarlos en el frontend y la capacidad del chatbot para recordar el contexto de la conversación mediante checkpoints (la IA utilitza los mensajes anteriores para generar un contexto).

### ChromaDB[[edit](/pti/index.php?title=Categor%C3%ADa:FIBerBot&veaction=edit&section=12 "Edit section: ChromaDB") | [edit source](/pti/index.php?title=Categor%C3%ADa:FIBerBot&action=edit&section=12 "Edit section: ChromaDB")]

Base de datos especializada en almacenar y gestionar datos de objectos complejos respresentados de forma vectorial. Cada vector representa una frase / un documento / una imagen para facilitar la búsqueda por similitud.

### Groq Cloud[[edit](/pti/index.php?title=Categor%C3%ADa:FIBerBot&veaction=edit&section=13 "Edit section: Groq Cloud") | [edit source](/pti/index.php?title=Categor%C3%ADa:FIBerBot&action=edit&section=13 "Edit section: Groq Cloud")]

Plataforma integrada en el cloud que ens permet executar els models LLM de gran tamaño en tiempo real de manera eficiente y rápida sin la necesidad de manejar hardware físico. Es ideal para tareas que requieren gran poder de cálculo como es el caso.

### DOCKER[[edit](/pti/index.php?title=Categor%C3%ADa:FIBerBot&veaction=edit&section=14 "Edit section: DOCKER") | [edit source](/pti/index.php?title=Categor%C3%ADa:FIBerBot&action=edit&section=14 "Edit section: DOCKER")]

Lo usamos para desplegar de forma rápida todo el sistema para que cualquier persona pueda utilizar el software sin la necesidad de tener conocimientos previos, dando una ejecución rápida y sencilla.