[![几千ㄒᎶㄖ.gif](images/%E5%87%A0%E5%8D%83%E3%84%92%E1%8E%B6%E3%84%96.gif)](/pti/index.php/File:%E5%87%A0%E5%8D%83%E3%84%92%E1%8E%B6%E3%84%96.gif)

## Contents

* [1 Introducción](#Introducci.C3.B3n)
  + [1.1 Contexto y justificación del proyecto](#Contexto_y_justificaci.C3.B3n_del_proyecto)
  + [1.2 Objetivos y alcances](#Objetivos_y_alcances)
* [2 Marco Teórico](#Marco_Te.C3.B3rico)
  + [2.1 Blockchain y descentralización](#Blockchain_y_descentralizaci.C3.B3n)
  + [2.2 Tokens No Fungibles (NFTs)](#Tokens_No_Fungibles_.28NFTs.29)
  + [2.3 Caso de estudio en CS:GO](#Caso_de_estudio_en_CS:GO)
* [3 Diseño del Sistema](#Dise.C3.B1o_del_Sistema)
  + [3.1 Arquitectura y tecnologías utilizadas](#Arquitectura_y_tecnolog.C3.ADas_utilizadas)
  + [3.2 Elección de blockchain y estándar de NFT](#Elecci.C3.B3n_de_blockchain_y_est.C3.A1ndar_de_NFT)
* [4 Casos de Uso](#Casos_de_Uso)
  + [4.1 Gestión de NFT, ofertas, compras y usuarios](#Gesti.C3.B3n_de_NFT.2C_ofertas.2C_compras_y_usuarios)
* [5 Desarrollo](#Desarrollo)
  + [5.1 Implementación de Smart Contracts](#Implementaci.C3.B3n_de_Smart_Contracts)
  + [5.2 Desarrollo de interfaz y su integración](#Desarrollo_de_interfaz_y_su_integraci.C3.B3n)
* [6 Potencial de Desarrollo](#Potencial_de_Desarrollo)
  + [6.1 Expansión de funcionalidades y seguridad](#Expansi.C3.B3n_de_funcionalidades_y_seguridad)
  + [6.2 Integración con Metamask y nuevas oportunidades](#Integraci.C3.B3n_con_Metamask_y_nuevas_oportunidades)
* [7 Repositorio (código fuente)](#Repositorio_.28c.C3.B3digo_fuente.29)

# Introducción[[edit](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&veaction=edit&section=1 "Edit section: Introducción") | [edit source](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&action=edit&section=1 "Edit section: Introducción")]

## Contexto y justificación del proyecto[[edit](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&veaction=edit&section=2 "Edit section: Contexto y justificación del proyecto") | [edit source](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&action=edit&section=2 "Edit section: Contexto y justificación del proyecto")]

Este proyecto busca desarrollar una plataforma de comercio electrónico basada en blockchain y NFT, inspirada en el juego CS:GO. Se enfoca en la transferencia de "skins" de armas del juego como activos digitales seguros y transparentes.

## Objetivos y alcances[[edit](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&veaction=edit&section=3 "Edit section: Objetivos y alcances") | [edit source](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&action=edit&section=3 "Edit section: Objetivos y alcances")]

Los objetivos incluyen la creación de un servicio web para la transferencia de skins de CS:GO mediante blockchain, la integración de tecnologías como truffle, Ethereum y Web3 para asegurar la seguridad en las transacciones, y la implementación de un frontend y backend robustos y amigables para los usuarios.

El alcance del proyecto abarca desde el desarrollo de Smart Contracts hasta la interfaz de usuario, permitiendo a los usuarios gestionar sus NFTs en el mercado, modificar precios y destinatarios, con seguimiento continuo del progreso mediante GitLab y asegurando la portabilidad del servicio mediante Docker.

# Marco Teórico[[edit](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&veaction=edit&section=4 "Edit section: Marco Teórico") | [edit source](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&action=edit&section=4 "Edit section: Marco Teórico")]

## Blockchain y descentralización[[edit](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&veaction=edit&section=5 "Edit section: Blockchain y descentralización") | [edit source](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&action=edit&section=5 "Edit section: Blockchain y descentralización")]

El proyecto se apoya en la tecnología Blockchain para crear una plataforma descentralizada de comercio de activos digitales únicos, como las skins de CS:GO. La Blockchain asegura la seguridad y descentralización al almacenar información en nodos independientes, garantizando la inmutabilidad de las transacciones y su visibilidad para todos los usuarios.

## Tokens No Fungibles (NFTs)[[edit](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&veaction=edit&section=6 "Edit section: Tokens No Fungibles (NFTs)") | [edit source](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&action=edit&section=6 "Edit section: Tokens No Fungibles (NFTs)")]

Los Tokens No Fungibles (NFTs) son activos digitales únicos e irremplazables encriptados en la blockchain, como las skins en CS:GO. Aunque los NFTs no pueden fraccionarse ni intercambiarse, representan activos digitales valiosos en mercados como "OpenSea", donde se negocian obras de arte y activos de videojuegos, generando transacciones de gran valor.

## Caso de estudio en CS:GO[[edit](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&veaction=edit&section=7 "Edit section: Caso de estudio en CS:GO") | [edit source](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&action=edit&section=7 "Edit section: Caso de estudio en CS:GO")]

En CS:GO, las skins son elementos estéticos de armas con valor en el mercado, adquiridas a través de intercambios o partidas. La implementación de blockchain, NFT y smart contracts asegura la propiedad de estas skins, permitiendo transacciones seguras de compra y venta al asociar un token único a cada skin, evitando la duplicación y garantizando la autenticidad de las transacciones en el mercado de CS:GO.

# Diseño del Sistema[[edit](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&veaction=edit&section=8 "Edit section: Diseño del Sistema") | [edit source](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&action=edit&section=8 "Edit section: Diseño del Sistema")]

## Arquitectura y tecnologías utilizadas[[edit](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&veaction=edit&section=9 "Edit section: Arquitectura y tecnologías utilizadas") | [edit source](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&action=edit&section=9 "Edit section: Arquitectura y tecnologías utilizadas")]

El diseño del sistema se basa en una arquitectura tecnológica sólida para respaldar la plataforma:

[![](images/800px-Arquitectura\_y\_tecnolog%C3%ADas\_utilizadas.png)](/pti/index.php/File:Arquitectura_y_tecnolog%C3%ADas_utilizadas.png)

Esquema de la arquitectura

* Ganache: facilita el desarrollo local de contratos inteligentes en Ethereum, ofreciendo una blockchain local para pruebas y gestión de transacciones.
* Web3.js: permite la interacción con la blockchain Ethereum y los contratos inteligentes, facilitando llamadas a funciones y la gestión de cuentas.
* Node.js: utilizado para ejecutar JavaScript en el servidor, con Express para manejar rutas, Path para gestionar archivos y otras librerías para aspectos como análisis de solicitudes HTTP, autenticación y conexión con Ethereum.
* MongoDB: base de datos NoSQL aprovechada por su capacidad de almacenamiento, escalabilidad y consultas intuitivas, gestionadas con Mongoose como driver.
* React: biblioteca para construir interfaces de usuario reutilizables, complementada con librerías para diseño, renderizado y navegación entre pantallas (Bootstrap, React-Bootstrap, React-dom, React-router-dom y React-scripts).
* Docker: encapsula el servidor, la base de datos y sus dependencias en contenedores autónomos, orquestados con Docker Compose para entornos consistentes y reproducibles.

## Elección de blockchain y estándar de NFT[[edit](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&veaction=edit&section=10 "Edit section: Elección de blockchain y estándar de NFT") | [edit source](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&action=edit&section=10 "Edit section: Elección de blockchain y estándar de NFT")]

Se seleccionó la Blockchain Ethereum con Ganache para desarrollo local, aprovechando su capacidad de iniciar una blockchain sin necesidad de utilizar la red pública.

Se optó por el estándar ERC-721 para NFT debido a su uso común en transfermarkets y su capacidad para asignar un identificador único a cada token, asegurando la singularidad de los activos digitales.
Este enfoque tecnológico asegura un desarrollo ágil, pruebas realistas en entornos controlados y la implementación de estándares sólidos para garantizar la singularidad y autenticidad de los activos digitales en la plataforma.

# Casos de Uso[[edit](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&veaction=edit&section=11 "Edit section: Casos de Uso") | [edit source](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&action=edit&section=11 "Edit section: Casos de Uso")]

## Gestión de NFT, ofertas, compras y usuarios[[edit](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&veaction=edit&section=12 "Edit section: Gestión de NFT, ofertas, compras y usuarios") | [edit source](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&action=edit&section=12 "Edit section: Gestión de NFT, ofertas, compras y usuarios")]

Esta sección del proyecto se enfoca en las funcionalidades clave de la aplicación, divididas en cuatro áreas principales: Gestión de NFT (que presenta acciones tanto para clientes como administradores), Ofertas, Compras y Usuarios. Destacando la Gestión de NFT, que presenta acciones tanto para clientes como administradores, con énfasis en las funciones exclusivas del administrador.

* Gestión de NFT:
  + GetNFT: recopila información de NFT asociada a un usuario, retornando sus NFT.
  + SetParamNFT: permite modificar parámetros de un NFT, como su visibilidad/vendibilidad y precio.
  + CreateNFT: permite al administrador crear un nuevo NFT con la información requerida.

* Gestión de Ofertas:
  + GetOffers: consulta y devuelve las ofertas abiertas asociadas a un usuario.
  + Accept Offer: Verifica y acepta una oferta, actualizando el estado y propiedad del NFT.
  + Reject Offer: rechaza una oferta, actualizando su estado.

* Gestión de Compras:
  + GetSellingNFT: recopila los NFT disponibles para la venta.
  + ComprarNFT: permite al usuario comprar un NFT, creando una oferta al vendedor.

* Gestión de Usuarios:
  + Login: verificación de credenciales y redirección al perfil en caso de validez.
  + Register: registro de usuario (nombre, contraseña y dirección).
  + Change Password: modificación de la contraseña y retorno al perfil.
  + Logout: token anulado y redirección a la página de inicio.

La REST API proporciona una serie de funciones que incluyen cambio de contraseña, autenticación, registro de usuario, gestión de NFTs, obtención de saldo en la red blockchain, información del usuario, manejo de ofertas y transacciones de compra, entre otras.

# Desarrollo[[edit](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&veaction=edit&section=13 "Edit section: Desarrollo") | [edit source](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&action=edit&section=13 "Edit section: Desarrollo")]

El desarrollo del proyecto se dividió en dos partes clave: la implementación de los Smart Contracts y el desarrollo de la interfaz de usuario.

## Implementación de Smart Contracts[[edit](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&veaction=edit&section=14 "Edit section: Implementación de Smart Contracts") | [edit source](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&action=edit&section=14 "Edit section: Implementación de Smart Contracts")]

Como no teníamos experiencia previa en aplicaciones Blockchain y Contratos Inteligentes, comenzamos con guías introductorias de Truffle, explorando ejemplos como "Pet-Shop" y "How to Build a NFT Marketplace DApp on Ethereum or Optimism." Posteriormente, descargamos un repositorio vacío proporcionado por Truffle, eliminamos las partes relacionadas con Optimism y añadimos las dependencias de OpenZeppelin para estandarizar los contratos.

Dos contratos fundamentales fueron desarrollados:

* csgoNFT.sol: este contrato se centró en la creación de NFTs, utilizando la librería ERC-721 para definir la estructura y la asignación de identificadores únicos a cada token.
* NFTMarketplace.sol: éste gestionó el mercado de transferencia, incluyendo la estructura de datos y funciones para listar, comprar, modificar precios y gestionar los NFTs.

Tras la implementación de los contratos inteligentes, procedimos a la migración de los mismos. Ganache se integró para las pruebas y se usaron scripts en JavaScript para verificar la funcionalidad en este entorno.

## Desarrollo de interfaz y su integración[[edit](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&veaction=edit&section=15 "Edit section: Desarrollo de interfaz y su integración") | [edit source](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&action=edit&section=15 "Edit section: Desarrollo de interfaz y su integración")]

La interfaz de usuario se ha enfocado en la unificación del aspecto visual y la inclusión de funcionalidades que optimizaran la experiencia del usuario. Se han usado tecnologías como React, Bootstrap, React-Bootstrap, React-dom y React-router-dom para construir las distintas pantallas, cada una con objetivos específicos:

* Login: permite a los usuarios iniciar sesión con verificaciones de autenticación.

[![](images/500px-%E5%87%A0%E5%8D%83%E3%84%92-\_%E1%8E%B6%E3%84%96\_-\_Login.png)](/pti/index.php/File:%E5%87%A0%E5%8D%83%E3%84%92-_%E1%8E%B6%E3%84%96_-_Login.png)

Pantalla de inicio de sesión

* Register: facilita el registro de nuevos usuarios.

[![](images/500px-%E5%87%A0%E5%8D%83%E3%84%92%E1%8E%B6%E3%84%96\_-\_Register.png)](/pti/index.php/File:%E5%87%A0%E5%8D%83%E3%84%92%E1%8E%B6%E3%84%96_-_Register.png)

Pantalla de registro

* CreateNFT: permite la creación de nuevos NFTs, incluyendo carga de imágenes y gestión de información.

[![](images/500px-%E5%87%A0%E5%8D%83%E3%84%92%E1%8E%B6%E3%84%96\_-\_CreateNFT.png)](/pti/index.php/File:%E5%87%A0%E5%8D%83%E3%84%92%E1%8E%B6%E3%84%96_-_CreateNFT.png)

Pantalla de crear NFT

* BuyNFT: muestra detalles de NFTs disponibles para compra y hace posible la adquisición de los mismos.

[![](images/500px-%E5%87%A0%E5%8D%83%E3%84%92%E1%8E%B6%E3%84%96\_-\_BuyNFT.png)](/pti/index.php/File:%E5%87%A0%E5%8D%83%E3%84%92%E1%8E%B6%E3%84%96_-_BuyNFT.png)

Pantalla de comprar NFT

* ListNFT: muestra la lista del marketplace de NFTs y permite realizar ofertas y compras.

[![](images/500px-%E5%87%A0%E5%8D%83%E3%84%92%E1%8E%B6%E3%84%96\_-\_ListNFT.png)](/pti/index.php/File:%E5%87%A0%E5%8D%83%E3%84%92%E1%8E%B6%E3%84%96_-_ListNFT.png)

Pantalla de lista de NFT's

* MyProfile: proporciona un espacio personal para que los usuarios interactuen con sus propios NFTs, cambien precios o gestionen ofertas, entre otros.

[![](images/500px-%E5%87%A0%E5%8D%83%E3%84%92%E1%8E%B6%E3%84%96\_-\_MyProfile.png)](/pti/index.php/File:%E5%87%A0%E5%8D%83%E3%84%92%E1%8E%B6%E3%84%96_-_MyProfile.png)

Pantalla de mi perfil

* MyOffers: ofrece a los usuarios una vista de sus ofertas y las opciones para aceptar o rechazarlas.

[![](images/500px-%E5%87%A0%E5%8D%83%E3%84%92%E1%8E%B6%E3%84%96\_-\_MyOffers.png)](/pti/index.php/File:%E5%87%A0%E5%8D%83%E3%84%92%E1%8E%B6%E3%84%96_-_MyOffers.png)

Pantalla de mis ofertas

* ChangePassword: permite a los usuarios cambiar su contraseña de acceso a la plataforma.

[![](images/500px-%E5%87%A0%E5%8D%83%E3%84%92%E1%8E%B6%E3%84%96\_-\_ChangePassword.png)](/pti/index.php/File:%E5%87%A0%E5%8D%83%E3%84%92%E1%8E%B6%E3%84%96_-_ChangePassword.png)

Pantalla de cambiar contraseña

# Potencial de Desarrollo[[edit](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&veaction=edit&section=16 "Edit section: Potencial de Desarrollo") | [edit source](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&action=edit&section=16 "Edit section: Potencial de Desarrollo")]

El proyecto contempla un amplio potencial de desarrollo, centrado en tres áreas clave: expansión de funcionalidades, actualizaciones de seguridad e integración con MetaMask, además de explorar nuevas oportunidades.

## Expansión de funcionalidades y seguridad[[edit](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&veaction=edit&section=17 "Edit section: Expansión de funcionalidades y seguridad") | [edit source](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&action=edit&section=17 "Edit section: Expansión de funcionalidades y seguridad")]

* Inteligencia Artificial y Filtrado de Contenidos para mejorar la búsqueda y personalizar recomendaciones.
* Integración con otras redes blockchain como Binance Smart Chain, Polygon y Solana para transacciones más rápidas y tarifas reducidas.
* Creación de una criptomoneda propia para recaudar fondos y ofrecer financiamiento colectivo.
* Investigación de soluciones de interoperabilidad entre criptomonedas para facilitar la transferencia de activos entre diversas blockchains.
* Ampliación para tokenizar activos del mundo real, como obras de arte físicas.

* Actualizaciones de Seguridad:
  + Implementación de HTTPS para una comunicación segura entre el navegador y el backend.
  + Uso de Cookies para mantener sesiones de usuarios y personalizar contenido, con precaución por las preocupaciones de privacidad.

## Integración con Metamask y nuevas oportunidades[[edit](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&veaction=edit&section=18 "Edit section: Integración con Metamask y nuevas oportunidades") | [edit source](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&action=edit&section=18 "Edit section: Integración con Metamask y nuevas oportunidades")]

Estas propuestas se enfocan en mejorar la aplicación, fortalecer la seguridad, ampliar la funcionalidad y ofrecer una experiencia más rica y segura para los usuarios.

* Accesibilidad simplificada mediante su extensión en el navegador.
* Almacenamiento local de claves privadas para seguridad y recuperación.
* Facilitación de la participación en el mercado de NFTs y compatibilidad con diversas blockchains.

* Exploración de Nuevas Oportunidades:
  + Escalabilidad con Kubernetes para orquestar contenedores y optimizar recursos según la demanda.
  + Uso de IPFS para descentralizar la aplicación y mejorar la resistencia a fallos y la eficiencia.
  + Herramientas de análisis para comprender el comportamiento y sentimiento de los usuarios, y para automatizar mensajes y recopilar feedback.

# Repositorio (código fuente)[[edit](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&veaction=edit&section=19 "Edit section: Repositorio (código fuente)") | [edit source](/pti/index.php?title=Categor%C3%ADa:%E5%87%A0%E5%8D%83%E3%84%92:_%E1%8E%B6%E3%84%96&action=edit&section=19 "Edit section: Repositorio (código fuente)")]

<https://repo.fib.upc.es/jordi.baranda/csgo-marketplace>