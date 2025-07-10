## Contents

* [1 Introducción](#Introducci.C3.B3n)
  + [1.1 ¿Qué es Safe marks?](#.C2.BFQu.C3.A9_es_Safe_marks.3F)
  + [1.2 Objetivos del proyecto](#Objetivos_del_proyecto)
* [2 Tecnologias](#Tecnologias)
  + [2.1 Hyperledger](#Hyperledger)
  + [2.2 Node.js](#Node.js)
  + [2.3 ReadTheDocs](#ReadTheDocs)
* [3 Guía de uso](#Gu.C3.ADa_de_uso)
  + [3.1 Universal](#Universal)
  + [3.2 Estudiante](#Estudiante)
  + [3.3 Profesor](#Profesor)

# Introducción[[edit](/pti/index.php?title=Categor%C3%ADa:SafeMarks&veaction=edit&section=1 "Edit section: Introducción") | [edit source](/pti/index.php?title=Categor%C3%ADa:SafeMarks&action=edit&section=1 "Edit section: Introducción")]

## ¿Qué es Safe marks?[[edit](/pti/index.php?title=Categor%C3%ADa:SafeMarks&veaction=edit&section=2 "Edit section: ¿Qué es Safe marks?") | [edit source](/pti/index.php?title=Categor%C3%ADa:SafeMarks&action=edit&section=2 "Edit section: ¿Qué es Safe marks?")]

SafeMarks es una aplicación web basada en la tecnología Hyperledger con el objetivo de proporcionar tanto a profesores como estudiantes una alternativa robusta y segura de modificar y consultar información, específicamente notas de asignaturas, gracias al uso que le da Hyperledger a la Blockchain.

## Objetivos del proyecto[[edit](/pti/index.php?title=Categor%C3%ADa:SafeMarks&veaction=edit&section=3 "Edit section: Objetivos del proyecto") | [edit source](/pti/index.php?title=Categor%C3%ADa:SafeMarks&action=edit&section=3 "Edit section: Objetivos del proyecto")]

* Aprender los entresijos tanto de Docker como de la Blockchain, así como comprender qué proyectos están impulsando su uso.
* Realizar una prueba de concepto sobre Hyperledger Fabric, dado que en proyectos anteriores se anotó su potencial, pese a encontrarse en una etapa de desarrollo muy temprana.
* Entre las diversas posibilidades que nos ofrece Docker, utilizar una base de cadena de bloques privada y segura permitiendo un acceso con nuestras propias normas en el sistema.
* Aplicar buena praxis de trabajo a través de la documentación progresiva del proyecto, y aplicarlo en el resultado final.

# Tecnologias[[edit](/pti/index.php?title=Categor%C3%ADa:SafeMarks&veaction=edit&section=4 "Edit section: Tecnologias") | [edit source](/pti/index.php?title=Categor%C3%ADa:SafeMarks&action=edit&section=4 "Edit section: Tecnologias")]

## Hyperledger[[edit](/pti/index.php?title=Categor%C3%ADa:SafeMarks&veaction=edit&section=5 "Edit section: Hyperledger") | [edit source](/pti/index.php?title=Categor%C3%ADa:SafeMarks&action=edit&section=5 "Edit section: Hyperledger")]

Hyperledger Fabric es una plataforma de código abierto de nivel empresarial con tecnología de ledger, diseñada para su uso en contextos empresariales, que ofrece algunas capacidades clave de diferenciación sobre otras plataformas populares de ledger o de blockchain.

El modelo de una red de Hyperledger es el siguiente: la red está formada por los pares que tienen almacenada la información del leger y los smart contracts. Los smart contracts son las transacciones que se pueden ejecutar entre los clientes y los ledger que incluyen el registro de todas las transacciones efectuadas entre los clientes del canal. Otra característica de HyperLedger Fabric es la existencia de canales, que es una capa de abstracción que limita el acceso de usuarios a diferentes pares de la red con diferentes ledgers y smarts contracts. Los accesos a los canales se efectúan utilizando unos certificados emitidos por las autoridades de certificación de las organizaciones que participan el la red.

## Node.js[[edit](/pti/index.php?title=Categor%C3%ADa:SafeMarks&veaction=edit&section=6 "Edit section: Node.js") | [edit source](/pti/index.php?title=Categor%C3%ADa:SafeMarks&action=edit&section=6 "Edit section: Node.js")]

Node.js es un entorno de trabajo multiplataforma, que usa como lenguaje de programación Javascript. La idea principal tras la utilitzación de Node.js en esta aplicación ha sido la posibilidad de usar módulos predeterminados muy eficientes. Los módulos principales que han sido usados para el desarrollo han sido:

* **Express:** Permite que podamos tener un entorno para desarrollo web muy cómodo, facilitando la utilización de métodos post, get y de renderización en la web.
* **Fs:** Permite crear archivos y consultarlos. Estas operaciones son necesarias para los certificados que se usan en las autoridades de certificación de HyperLedger.
* **Módulos propios:** Estos módulos son propios de HyperLedger Fabric, permitiendo usar muchos de los objetos que necesitamos. Algunos ejemplos de estos módulos son: FileSystemWallet, Gateway y X509WalletMixin.

## ReadTheDocs[[edit](/pti/index.php?title=Categor%C3%ADa:SafeMarks&veaction=edit&section=7 "Edit section: ReadTheDocs") | [edit source](/pti/index.php?title=Categor%C3%ADa:SafeMarks&action=edit&section=7 "Edit section: ReadTheDocs")]

ReadTheDocs es un software OpenSource que simplifica la documentación de un software al automatizar la construcción del mismo. Utilizando un generador de documentación como base (en nuestro caso ese generador es Sphinx, que a su vez está basado en reStructuredText), ReadTheDocs se encarga de compilar la documentación, convertirla al formato deseado (HTML en nuestro caso) e indexarla. Tiene muchas otras funcionalidades, pero en este proyecto hemos dado a las mencionadas anteriormente.

Hemos utilizado ReadTheDocs no sólo para proporcionar a los usuarios un acceso cómodo a la información relevante del proyecto, sino porque nos facilitaba añadir y compartir la información de las diversas features que se han ido implementando en el desarrollo del proyecto. No solo eso, si la aplicación se actualiza en producción, ReadTheDocs nos permitiría ampliar la documentación en paralelo a los commits añadidos, facilitando el qué pertenece a qué.

# Guía de uso[[edit](/pti/index.php?title=Categor%C3%ADa:SafeMarks&veaction=edit&section=8 "Edit section: Guía de uso") | [edit source](/pti/index.php?title=Categor%C3%ADa:SafeMarks&action=edit&section=8 "Edit section: Guía de uso")]

## Universal[[edit](/pti/index.php?title=Categor%C3%ADa:SafeMarks&veaction=edit&section=9 "Edit section: Universal") | [edit source](/pti/index.php?title=Categor%C3%ADa:SafeMarks&action=edit&section=9 "Edit section: Universal")]

En la pantalla de inicio saldrán dos funcionalidades: una para registrar usuario y otra para iniciar sesión (en caso de tener ya un usuario).

* Registrar usuario: En esta funcionalidad, pediremos primero que inicie sesión el administrador (es el único que puede añadir a la network, al tratar con transacciones privadas, que son las notas). Una vez iniciada, se solicitarán los datos del usuario a registrar. Estos datos serán Nombre de Usuario, Contraseña y Categoría (Alumno o Profesor). En caso que el registro se efectúe correctamente, el usuario será devuelto a la página de inicio.
* Iniciar sesión: Requerirá los credenciales de un usuario ya creado y, en función del rol de la cuenta (en caso de iniciar sesión correctamente), nos llevará a la página de inicio correspondiente.

## Estudiante[[edit](/pti/index.php?title=Categor%C3%ADa:SafeMarks&veaction=edit&section=10 "Edit section: Estudiante") | [edit source](/pti/index.php?title=Categor%C3%ADa:SafeMarks&action=edit&section=10 "Edit section: Estudiante")]

Con este rol, la página de inicio solo tendrá una funcionalidad:

* Consultar tu nota: en esta página se solicitará tu nombre de usuario y la asignatura de donde consultar tu nota. Si los parámetros envian son correctos y coinciden con los alojados en la base de datos, se realizará una query a la blockchain para poder acceder a tus datos y, una vez procesados, se te transmitirán.

## Profesor[[edit](/pti/index.php?title=Categor%C3%ADa:SafeMarks&veaction=edit&section=11 "Edit section: Profesor") | [edit source](/pti/index.php?title=Categor%C3%ADa:SafeMarks&action=edit&section=11 "Edit section: Profesor")]

Con este rol, la página de inicio tendrá varias funcionalidades:

* Añadir nota: en esta página se solicitará la materia a evaluar, nombre del profesor que evalúa, la nota que ha conseguido el alumno y el alumno en cuestión. Si los parámetros enviados son válidos, se crea una query a la blockchain y se reenvía el profesor al inicio.
* Consultar nota: en esta página se solicitará el nombre del alumno y la materia evaluada. Si los parámetros enviados son correctos y coinciden con los alojados en la base de datos, se realizará una query a la blockchain para poder acceder a tus datos y, una vez procesados, se te transmitirán.
* Consultar todas: en esta página se solicitará la materia evaluada. Si el parámetro enviado es correcto, se creará la query a la blockchain y, una vez procesado, devolverá todas las notas (junto con laos alumnos que la han adquirido) de la asignatura solicitada.