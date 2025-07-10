## Contents

* [1 Introducción](#Introducci.C3.B3n)
  + [1.1 Objetivos](#Objetivos)
  + [1.2 Base teórica](#Base_te.C3.B3rica)
  + [1.3 Solución](#Soluci.C3.B3n)
  + [1.4 Resultados](#Resultados)
  + [1.5 Conclusiones](#Conclusiones)
  + [1.6 Referencias](#Referencias)

# Introducción[[edit](/pti/index.php?title=Categor%C3%ADa:Self-Sovereign-Identity&veaction=edit&section=1 "Edit section: Introducción") | [edit source](/pti/index.php?title=Categor%C3%ADa:Self-Sovereign-Identity&action=edit&section=1 "Edit section: Introducción")]

Muchos campos de la tecnología están vertiendo sus esfuerzos en ofrecer soluciones con algún grado de descentralización. En un aspecto tan crucial para la sociedad como es la identidad, no es de extrañar que muchas empresas hayan decidido invertir en la investigación de distintos modelos que podrían permitir que ésta fuese también descentralizada, alejándola de las grandes tecnológicas y poniéndola en las manos de las personas. Es gracias a este problema que aparece la solución de self-sovereign identity, un nuevo paradigma que se basa en tres principales figuras:
El issuer, o proveedor, que emite credenciales firmadas.
El holder, o poseedor, que recibe esas credenciales referentes a él de distintos proveedores y las usa.
El verifier, o verificador, que comprueba que esas credenciales son válidas y permite al usuario demostrar su identidad para acceder a un servicio o realizar otras acciones.
Esta tecnología permite a los usuarios autogestionar sus identidades digitales sin depender de proveedores externos para almacenar y administrar los datos de forma centralizada. Se basa en la misma idea de una cartera física donde guardar tu documentación, y busca trasladarla a la actualidad, en la cual, en la mayoría de los casos, los usuarios no tienen control sobre lo que sucede con sus datos y quién puede verlos. Se necesita un sistema fiable y confiable para que personas, empresas y máquinas puedan interactuar y conectarse en red de manera digital y segura.
El de la identidad descentralizada es un campo hoy en día muy verde, aún no hay sistemas de carácter oficial implementados ni entidades que ofrezcan esos servicios de una forma más allá de pequeños escenarios a modo de pruebas de concepto. Esto mismo es lo que nos hizo decantarnos en su momento por este tema para llevar a cabo el proyecto. En él, desarrollamos un ejemplo de pipeline que tiene como objetivo demostrar la utilidad de un sistema de este tipo, permitirnos explorar campos tecnológicos en su fase inicial que se encuentran en constante crecimiento y, sobre todo, aprender.

## Objetivos[[edit](/pti/index.php?title=Categor%C3%ADa:Self-Sovereign-Identity&veaction=edit&section=2 "Edit section: Objetivos") | [edit source](/pti/index.php?title=Categor%C3%ADa:Self-Sovereign-Identity&action=edit&section=2 "Edit section: Objetivos")]

Como hemos mencionado en la introducción, el objetivo principal de este proyecto es aprender sobre los beneficios respecto al sistema actual de identificaciones y cómo funciona un sistema self-sovereign identity (SSI), para así poder implementar un proof of concept y demostrar sus verdaderas ventajas y posibles aplicaciones. No solo vamos a investigar cómo funciona, sinó que también tendremos que aprender cómo se implementa, y esto lo vamos a hacer estudiando cómo lo han decidido implementar otros proyectos, como por ejemplo la solución del proyecto Alastria. A partir de aquí, tendremos que seguir investigando para poder decidir qué tecnologías se adecuan más a nuestra meta.
Para hacer el proof of concept tenemos distintos objetivos más técnicos:
Implementar un sistema con blockchain que funcione para registrar las credenciales de los usuarios y hacer que sean inmutables.
Diseñar una aplicación móvil Android que sirva de wallet del SSI, donde el usuario podrá ver sus credenciales y usarlas cuando las necesite.
Hacer una página web que te pida credenciales a través de SSI para poder acceder a sus servicios y así poder demostrar con un caso de uso la funcionalidad del sistema.
Crear un sistema que comunique la blockchain, la aplicación y la página web para que tenga el resultado esperado.

## Base teórica[[edit](/pti/index.php?title=Categor%C3%ADa:Self-Sovereign-Identity&veaction=edit&section=3 "Edit section: Base teórica") | [edit source](/pti/index.php?title=Categor%C3%ADa:Self-Sovereign-Identity&action=edit&section=3 "Edit section: Base teórica")]

Nuestro objetivo es desarrollar un sistema self-sovereign identity (SSI), el cual permite a las personas probar cosas sobre sí mismas utilizando credenciales descentralizadas y verificables tal como lo hacen en la vida real, sin conexión a Internet, como, por ejemplo, al presentar un documento de identidad válido para realizar un examen en la FIB.
La definición de un sistema soberano no es algo cerrado, pero la mejor opción que hemos encontrado es la propuesta por Quinten Stokkink y Johan Pouwelse, en la cual nos basaremos para algunos aspectos del proyecto. Según su trabajo, un sistema de identidad debe tener ciertas características clave que, por lo tanto, trataremos de cumplir:

1) Existencia. Los usuarios deben tener una existencia independiente.

2) Control. Los usuarios deben controlar sus identidades.

3) Acceso. Los usuarios deben tener acceso a sus propios datos.

4) Transparencia. Los sistemas y algoritmos deben ser transparentes.

5) Persistencia. Las identidades deben ser duraderas.

6) Portabilidad. La información y servicios sobre identidad tienen que ser portables.

7) Interoperabilidad. Las identidades deben ser lo más utilizables posible.

8) Consentimiento. Los usuarios deben aceptar el uso de su identidad.

9) Minimización. Las afirmaciones deben revelar la mínima información necesaria.

10) Protección. Los derechos de usuario deben estar protegidos.

11) Demostrabilidad. Las afirmaciones no serán válidas si no se puede demostrar que son verdaderas.

Gracias a la estructura de blockchain, la mayoría de estas características se cumplen:
Un usuario podrá crear su existencia con una blockchain personalizada sin permisos externos (1).
Cada usuario tendrá su propia blockchain, por lo tanto el usuario tendrá control absoluto de su identidad (2).
El usuario crea y mantiene su blockchain, por lo tanto tiene acceso a la información de su identidad (3).
Al tener un algoritmo de consenso público, podemos afirmar que obtenemos la transparencia que buscábamos (4).
Por la naturaleza de solo adición de blockchain también proporciona persistencia en los atributos publicados (5).
Para compartir tus datos personales tienes que dar tu consentimiento (8).
Las demás propiedades que hay que cumplir vienen dadas por los atributos que guardaremos en la blockchain.

Nombre: El nombre del atributo.

Timestamp: El momento de creación de la afirmación.

Validez: El tiempo tras el cuál la afirmación ya no es válida.

Formato de la prueba: El tipo de prueba de la afirmación.

Enlace de la prueba: Esto debe garantizar que la afirmación es verdadera.

## Solución[[edit](/pti/index.php?title=Categor%C3%ADa:Self-Sovereign-Identity&veaction=edit&section=4 "Edit section: Solución") | [edit source](/pti/index.php?title=Categor%C3%ADa:Self-Sovereign-Identity&action=edit&section=4 "Edit section: Solución")]

Dado que la intención principal de nuestro proyecto era mostrar la utilidad y el funcionamiento de un sistema self-sovereign identity, decidimos que lo más representativo sería recrear un pipeline simple en el que un usuario demuestre la mayoría de edad a una página web que lo requiera, en nuestro caso, una casa de apuestas.
Sobre el papel, para ello necesitaríamos una página web que nos pidiese ser mayor de edad, una aplicación wallet que pudiese hacer claims y una blockchain donde registrarlos. Llevándolo a la implementación, tuvimos que añadir un cliente para que se pudiese comunicar con la blockchain, ya que directamente desde la aplicación móvil no era posible la integración.

[![](images/800px-A.PNG)](/pti/index.php/File:A.PNG)

Figura 1. Diagrama de la arquitectura de nuestra solución.

La arquitectura resultante fue la siguiente:

- Una instancia de Ganache, una blockchain de Ethereum personal para simular en local un entorno en el que desplegar smart contracts y realizar transacciones.

- Un cliente de web3 que se comunique con Ganache y que, usando Metamask, haga transacciones para modificar la blockchain (realizar un claim) y llamadas para ver su estado (comprobar si un usuario ha hecho un claim).

- Una aplicación wallet para Android que permitiese al usuario recibir peticiones, realizar claims y gestionar sus datos.

- Una página web alojada en Netlify que representase una entidad que necesita un dato concreto del usuario, en nuestro caso, si éste es mayor de edad.

Con estos elementos implementados y partiendo de un estado en el que un issuer le ha proporcionado sus datos al usuario, podemos recrear el siguiente pipeline:

1. El usuario trata de acceder a la página web.

2. La página web le bloquea el acceso y le pide que demuestre que es mayor de edad para continuar. Para ello, le proporciona un código QR.

3. El usuario escanea el QR con su aplicación wallet.

4. Si el usuario es mayor de edad, le aparece una ventana emergente en la aplicación que le permite realizar o no el claim.

5. Si el usuario acepta:

- Se envía esa petición al cliente de web3

- Metamask la detecta

- El smart contract verifica los campos del claim

- Se realiza la transacción

6. La aplicación wallet recibe que la transacción se ha realizado correctamente y envía la prueba a la página web.

7. La página web verifica los datos y deja acceder al usuario.

## Resultados[[edit](/pti/index.php?title=Categor%C3%ADa:Self-Sovereign-Identity&veaction=edit&section=5 "Edit section: Resultados") | [edit source](/pti/index.php?title=Categor%C3%ADa:Self-Sovereign-Identity&action=edit&section=5 "Edit section: Resultados")]

Al finalizar la realización de este proyecto, podemos valorar el cumplimiento de nuestros objetivos:
Aprender. Hemos profundizado bastante sobre los conceptos de SSI y hemos podido entender mejor distintas herramientas para implementar soluciones de este estilo, como los smart contracts o las funciones criptográficas.
Para empezar, hemos implementado un sistema con blockchain que registra las credenciales de una persona.
En segundo lugar, hemos diseñado una aplicación móvil desde la que se pueden ver las credenciales del usuario y usarlas en caso de que se requieran.
En tercer lugar, hemos diseñado una página web que te pide tus credenciales para poder acceder a sus servicios para simular un caso de uso de este sistema.
Por último, hemos comunicado la blockchain, la aplicación y la página web para que tenga el resultado esperado.

Como podemos comprobar, hemos cumplido exactamente nuestros objetivos principales en este proyecto. Aún así, debemos de tener en cuenta que este proyecto ha sido pensado para realizar una prueba de concepto de un sistema totalmente desconocido para los integrantes de este grupo y que en ningún momento este diseño podría salir al mundo real, además de que le faltan muchos aspectos por concretar y pulir para poder salir a producción, la arquitectura es muy simple y no ofrece una buena escalabilidad.

## Conclusiones[[edit](/pti/index.php?title=Categor%C3%ADa:Self-Sovereign-Identity&veaction=edit&section=6 "Edit section: Conclusiones") | [edit source](/pti/index.php?title=Categor%C3%ADa:Self-Sovereign-Identity&action=edit&section=6 "Edit section: Conclusiones")]

Nuestro proyecto de self-sovereign identity ha sido implementado en un escenario muy básico y para un caso de uso muy concreto. De este proyecto podemos extraer varias conclusiones sobre esta nueva forma de entender la identidad:
En primer lugar, este sistema tiene muchos aspectos positivos a valorar, pero su implementación a gran escala requiere una implementación más compleja y tener en cuenta muchos aspectos que no se han tenido para la realización de nuestro sistema.
En segundo lugar queríamos añadir que este sistema bien implementado puede amenazar a la grandes empresas que usan libremente datos de los usuarios aprovechándose de la poca transparencia que hay en internet, cosa que podría producir una dificultad añadida para generalizar el uso de este sistema.
Por último, creemos que para que este sistema salga a la luz como una opción real para los usuarios tiene que haber un “empujón” por parte del Gobierno tanto otorgando ayudas para el correcto desarrollo y mantenimiento de la aplicación como en el ámbito legal haciendo que estos sistemas justos y transparentes puedan competir contra los actuales.
En cuanto a la realización del proyecto en sí, estamos satisfechos con el resultado y creemos que nos ha sido una experiencia útil a corto y largo plazo.

## Referencias[[edit](/pti/index.php?title=Categor%C3%ADa:Self-Sovereign-Identity&veaction=edit&section=7 "Edit section: Referencias") | [edit source](/pti/index.php?title=Categor%C3%ADa:Self-Sovereign-Identity&action=edit&section=7 "Edit section: Referencias")]

Código del proyecto, <https://github.com/abernalmac/SSI/>

Definición self-sovereign identities, <https://www.bosch.com/stories/self-sovereign-identities/>

Truffle Suite tutorial, <http://trufflesuite.com/tutorial/>

Creating a RESTful API With Go, <https://tutorialedge.net/golang/creating-restful-api-with-golang/>

Repositorio AlastriaID, <https://github.com/alastria/alastria-identity/wiki/>

Funcionamiento AlastriaID, <https://alastria.io/wp-content/uploads/Alastria_Id_Privacy_Rational.pdf>

Documentación Netlify, <https://docs.netlify.com/>

Documentación Android Studio, <https://developer.android.com/docs?hl=es>

Kotlin, <https://developer.android.com/kotlin?hl=es>

Base del QR scanner, <https://github.com/foxandroid/QR_CODE_SCANNER>