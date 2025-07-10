## Contents

* [1 Projecte AskOut](#Projecte_AskOut)
  + [1.1 1. Resum de la proposta](#1._Resum_de_la_proposta)
  + [1.2 2. Tecnologies emprades](#2._Tecnologies_emprades)
    - [1.2.1 Aplicació](#Aplicaci.C3.B3)
    - [1.2.2 Servidor](#Servidor)
    - [1.2.3 Llenguatges i Frameworks](#Llenguatges_i_Frameworks)
  + [1.3 3. Screenshots](#3._Screenshots)
    - [1.3.1 WEB](#WEB)

# Projecte AskOut[[edit](/pti/index.php?title=Categor%C3%ADa:AskOut&veaction=edit&section=1 "Edit section: Projecte AskOut") | [edit source](/pti/index.php?title=Categor%C3%ADa:AskOut&action=edit&section=1 "Edit section: Projecte AskOut")]

[![Askout logo.png](images/Askout\_logo.png)](/pti/index.php/File:Askout_logo.png)

AskOut és una aplicació que permet a qualsevol que la tingui disposar d'un calendari de tots els esdeveniments públics a la ciutat de Barcelona.

AskOut permet a més veure el calendari d'esdeveniments i compartir les teves experiències a Facebook!

## 1. Resum de la proposta[[edit](/pti/index.php?title=Categor%C3%ADa:AskOut&veaction=edit&section=2 "Edit section: 1. Resum de la proposta") | [edit source](/pti/index.php?title=Categor%C3%ADa:AskOut&action=edit&section=2 "Edit section: 1. Resum de la proposta")]

AskOut és una aplicació que mostra els esdeveniments extrets directament de l’Ajuntament de Barcelona, mitjançant la web d’Open Data, d’una manera àgil i còmoda per tal que l’usuari estigui en tot moment informat i pugui gaudir de les activitats d’aquesta meravellosa ciutat.

A més, els esdeveniments que es mostren estan classificats per categoria tenint en compte les preferències de l’usuari. Això permet personalitzar la visualització d’esdeveniments, donat que cada día n’hi ha més de 600 a la ciutat.

L’aplicació també inclou altres funcionalitats com la de desar les activitats a les quals assistirà l’usuari per a que les tingui sempre vigilades, posar recordatoris per tal de que no s’oblidi de cap, i compartir­les al Facebook poguent així avisar als seus amics i coneguts. Aquesta funcionalitat només està disponible per aquells usuaris que prèviament s’hagin identificat a l’aplicació mitjançant aquesta xarxa social.

El projecte s’ha elaborat per a dispositius Android i connecta amb un servidor propi. També s’ha creat una senzilla pàgina web per promocionar-lo, explicar­lo i facilitar la descàrrega de l’aplicació i la compartició dels esdeveniments.

## 2. Tecnologies emprades[[edit](/pti/index.php?title=Categor%C3%ADa:AskOut&veaction=edit&section=3 "Edit section: 2. Tecnologies emprades") | [edit source](/pti/index.php?title=Categor%C3%ADa:AskOut&action=edit&section=3 "Edit section: 2. Tecnologies emprades")]

### Aplicació[[edit](/pti/index.php?title=Categor%C3%ADa:AskOut&veaction=edit&section=4 "Edit section: Aplicació") | [edit source](/pti/index.php?title=Categor%C3%ADa:AskOut&action=edit&section=4 "Edit section: Aplicació")]

Per realitzar l’aplicació Android s’ha utilitzat el llenguatge de programació Java i s’ha desenvolupat per la API Level 16 (Android 4.1 ­ Jellybean). A més s’han utilitzat diverses llibreries per poder afegir elements de manera més fàcil, com el calendari o per facilitar la connexió HTTP i la obtenció de dades en format JSON del servidor web.
Per poder treballar amb aquestes eines s’ha utilitzat l’entorn de desenvolupament Android Studio i s’ha realitzat un control de versions del programa amb Git, utilitzant un repositori privat a Github.

### Servidor[[edit](/pti/index.php?title=Categor%C3%ADa:AskOut&veaction=edit&section=5 "Edit section: Servidor") | [edit source](/pti/index.php?title=Categor%C3%ADa:AskOut&action=edit&section=5 "Edit section: Servidor")]

Amb la finalitat de provar tecnologies noves i aprendre a configurar un entorn estèril, s’ha utilitzat un Nettop PC propietat de l’associació JEDI Junior Empresa, on dos dels membres del grup estan participant.

Aquest ordinador té unes prestacions baixes: Intel Atom (2 cores) 1,60 GHz, 2GB RAM, 320GB SATA Hard Drive 5400 RPM,... Tot i això, com no cal gaire volum de càlcul en aquest projecte, per la fase inicial i de la proves funciona sense cap problema.

El sistema operatiu instal∙lat a l’ordinador és un Debian 7.5 Wheezy. Això facilita part del treball d’instal∙lació i manteniment dels programes utilitzats gràcies al gestor de paquets que incorpora Debian.

### Llenguatges i Frameworks[[edit](/pti/index.php?title=Categor%C3%ADa:AskOut&veaction=edit&section=6 "Edit section: Llenguatges i Frameworks") | [edit source](/pti/index.php?title=Categor%C3%ADa:AskOut&action=edit&section=6 "Edit section: Llenguatges i Frameworks")]

**­Npm:​** gestor de descàrregues dels paquets de NodeJS.

­
**NodeJS:** ​plataforma que utilitza Javascript per crear pàgines webs ràpides i escalables, mitjançant funcions asíncrones (non­blocking I/O model) per tal de permetre la creació de webs més eficients i lleugeres, entre d’altres.

**MongoDB:** ​base de dades no relacional (NoSQL) de codi obert, la qual emmagatzema documents JSON amb la finalitat de poder desar informació de forma molt escalable i poder extreure­la àgilment.

­**ExpressJS:** ​framework de NodeJS que facilita l’enrutament, la recepció i l’enviament de dades, la comunicació amb el framework de MongoDB, Mongoose, per tal d’obtenir dades de la base de dades, etc.

­**AngularJS:** ​front­end framework per NodeJS que permet generar pàgines dinàmicament. És possible extreure i mostrar dades de la base de dades utilitzant les apis creades prèviament amb ExpressJS i creant serveis amb AngularJS.

**CrontabJS:​** e​ina que permet l’execució d’scripts programats amb NodeJS,amb una periodicitat definida pel programador.

­**PM2:** ​e​ina que gestiona els processos del servidor. És l’encarregat de que sempre estigui corrent la pàgina web i de reiniciar­la si hi ha errors. També la manté vigilada per si hi ha algun canvi en el codi, per tal de que s’apliqui immediatament.​

­**Git i Github:** ​e​ines de control de versions i emmagatzematge del codi.

## 3. Screenshots[[edit](/pti/index.php?title=Categor%C3%ADa:AskOut&veaction=edit&section=7 "Edit section: 3. Screenshots") | [edit source](/pti/index.php?title=Categor%C3%ADa:AskOut&action=edit&section=7 "Edit section: 3. Screenshots")]

[![Askout portada.png](images/Askout\_portada.png)](/pti/index.php/File:Askout_portada.png) [![Askout home.png](images/Askout\_home.png)](/pti/index.php/File:Askout_home.png) [![Askout pic2.png](images/Askout\_pic2.png)](/pti/index.php/File:Askout_pic2.png) [![Askout pic3.png](images/Askout\_pic3.png)](/pti/index.php/File:Askout_pic3.png) [![Askout list.png](images/Askout\_list.png)](/pti/index.php/File:Askout_list.png) [![Askout pic1.png](images/Askout\_pic1.png)](/pti/index.php/File:Askout_pic1.png)

### WEB[[edit](/pti/index.php?title=Categor%C3%ADa:AskOut&veaction=edit&section=8 "Edit section: WEB") | [edit source](/pti/index.php?title=Categor%C3%ADa:AskOut&action=edit&section=8 "Edit section: WEB")]

Link: <http://jediantic.upc.es/>