[![](images/200px-Ap%C3%BAntalo.png)](/pti/index.php/File:Ap%C3%BAntalo.png)

Apúntalo.

Apúntalo és una webapp per crear i compartir documents relacionats amb la universitat de forma col·laborativa i en temps real. La web consisteix en un seguit de categories on els usuaris podran crear posts en la categoria de l'assignatura que estudien d'una carrera i universitat concreta. El mateix usuari que crea els posts pot decidir qui pot editar el document i pot posar a la venda el document perquè qualsevol pugui comprar i descarregar el document.

## Contents

* [1 Perquè Apuntalo?](#Perqu.C3.A8_Apuntalo.3F)
* [2 Arquitectura](#Arquitectura)
  + [2.1 Etherpad](#Etherpad)
  + [2.2 Backend](#Backend)
  + [2.3 Frontend](#Frontend)
  + [2.4 Blockchain](#Blockchain)
* [3 Desplegament](#Desplegament)
  + [3.1 Blockchain](#Blockchain_2)
  + [3.2 Etherpad](#Etherpad_2)
  + [3.3 Backend](#Backend_2)
  + [3.4 NGINX](#NGINX)
* [4 Possibles Millores](#Possibles_Millores)
  + [4.1 Etherpad](#Etherpad_3)
  + [4.2 Backend](#Backend_3)
  + [4.3 Frontend](#Frontend_2)
  + [4.4 Blockchain](#Blockchain_3)

# Perquè Apuntalo?[[edit](/pti/index.php?title=Categor%C3%ADa:Apuntalo&veaction=edit&section=1 "Edit section: Perquè Apuntalo?") | [edit source](/pti/index.php?title=Categor%C3%ADa:Apuntalo&action=edit&section=1 "Edit section: Perquè Apuntalo?")]

La idea d'aquest projecte va sorgir al ser estudiants i trobar-nos amb la necessitat de poder compartir apunts entre nosaltres. També havíem vist que en algunes ocasions eines com Google Docs ens han set molt útils per poder fer treballs en grup i ens ha donat idees per com podem fer nosaltres una web amb un funcionament similar però que estigui enfocat en l'estudiantat universitari.

D’altra banda, també teníem ganes de poder aprendre una mica de Blockchain. En aquest sentit, la nostra idea de tenir transaccions de pagaments era compatible amb l'ús d'una Blockchain.

# Arquitectura[[edit](/pti/index.php?title=Categor%C3%ADa:Apuntalo&veaction=edit&section=2 "Edit section: Arquitectura") | [edit source](/pti/index.php?title=Categor%C3%ADa:Apuntalo&action=edit&section=2 "Edit section: Arquitectura")]

El nostre projecte está dividit en 3 parts ben diferenciades: backend, frontend i blockchain. A més, utilitzem Etherpad per afegir funcionalitats d’edició de documents en temps real.

## Etherpad[[edit](/pti/index.php?title=Categor%C3%ADa:Apuntalo&veaction=edit&section=3 "Edit section: Etherpad") | [edit source](/pti/index.php?title=Categor%C3%ADa:Apuntalo&action=edit&section=3 "Edit section: Etherpad")]

Etherpad ens ofereix tant una part de backend com de frontend per poder fer ús de l’aplicació pràcticament sense configuració. Requereix tenir nodeJS al ordinador per poder fer funcionar. La configuració per defecte guarda els pads en una dirtyDB. DirtyDB és una base de dades que guarda els continguts en JSON. Tot i que d’aquesta manera es pot crear pads sense problemes, es recomana utilitzar una altra base de dades per guardar els pads.

El disseny d’Etherpad està fet per ser fàcilment incrustable en qualsevol pàgina, i ofereix una API per poder gestionar els pads. A nosaltres ens interessa el endpoint per crear pads: createPad. Aquests serà cridats per part del backend.

```
createPad {apikey, padID}  <- El padID ens el podem inventar.

```

L’apikey es genera quan executem per primera vegada Etherpad, es necessitarà utilitzar aquesta Apikey per poder fer la implementació en el Backend.

Per incrustar un pad en una pàgina html qualsevol simplement es fa de la següent forma:

```
<iframe src='http:/<domini>/p/<id del pad>' width=400 height=400>

```

[![](images/800px-ApuntaloEtherpad.JPG)](/pti/index.php/File:ApuntaloEtherpad.JPG)

Interfície Etherpad

## Backend[[edit](/pti/index.php?title=Categor%C3%ADa:Apuntalo&veaction=edit&section=4 "Edit section: Backend") | [edit source](/pti/index.php?title=Categor%C3%ADa:Apuntalo&action=edit&section=4 "Edit section: Backend")]

Pel que fa al backend, s’ha desenvolupat totalment amb nodeJS. Com hem dit prèviament, node és un entorn d’execució que permet executar javascript fora d’un navegador. Javascript és un llenguatge que ha evolucionat molt en els últims temps, arribant a tenir fins a 9 versions diferents.

D’altra banda, s’han anat afegint mòduls npm. NPM és acrònim de Node Package Manager i serveix per afegir llibreries externes al teu projecte node. D’aquesta forma, podem utilitzar llibreries molt conegudes sense haver de reescriure tot el codi de nou. Cal dir que npm permet instal·lar paquets a nivell global, convertint-los en un programa més del nostre sistema; o fer-ho de forma local, fent que el paquet només estigui disponible dins del projecte. D’altra banda, alguns paquets estan enfocats a ser usats per terminal (com mongoose), i altres son simples llibreries que un pot importar al seu projecte i cridar les seves funcions.

Algunes de les llibreries que hem fet servir compleixen propòsits molt específics, mentre que altres son pilars fonamentals de la api.

## Frontend[[edit](/pti/index.php?title=Categor%C3%ADa:Apuntalo&veaction=edit&section=5 "Edit section: Frontend") | [edit source](/pti/index.php?title=Categor%C3%ADa:Apuntalo&action=edit&section=5 "Edit section: Frontend")]

Angular permet crear webs d’una sola pàgina. Consisteix bàsicament en la construcció de components. Hi ha un component inicial que és on inserim la resta de components i nosaltres podem fer que segons donat un endpoint es puguin mostrar uns components o uns altres.

La carpeta d’un component contè 4 fitxers, dos fitxers TypeScript, un descriu la classe (aquest no fa falta editar) i un altre conté la classe del component on podem definir mètodes per definir el comportament del component. Llavors tenim un fitxer html on definim l’estructura del component i podem fer que executi funcions de la classe que hem implementat. Finalment tenim un fitxer CSS per poder afegir disseny a l’aspecte. Els components queden guardats a la carpeta src/app/ del projecte.

La idea inicial de la pàgina era tenir una barra vertical amb el menú de navegació i utilitzar la resta d’espai en poder navegar per les universitats, carreres, assignatures i poder veure els documents.

[![](images/ApuntaloFrontend.JPG)](/pti/index.php/File:ApuntaloFrontend.JPG)

Homepage Apuntalo

## Blockchain[[edit](/pti/index.php?title=Categor%C3%ADa:Apuntalo&veaction=edit&section=6 "Edit section: Blockchain") | [edit source](/pti/index.php?title=Categor%C3%ADa:Apuntalo&action=edit&section=6 "Edit section: Blockchain")]

Per desenvolupar la blockchain utilitzarem dos components de Trufflesuite: Truffle i Ganache, a més d’utilizar la API Web3 per la connexió backend-blockchain. Per començar el projecte primer s’ha d'instal·lar truffle amb *npm install -g truffle* , seguidament Ganache amb *npm install -g ethereumjs-testrpc*. Un cop tenim instal·lats aquests dos components principals cal instal·lar web3 a la carpeta on tindrem la blockchain amb *npm install web3* , conjuntament amb nodejs per implementar el web3.

Amb tots els components principals ja es pot començar a programar. El projecte de la blockchain l’hem dividit en tres parts: implementació de l’Smart Contract (Truffle), implementació del server blockchain (Ganache) i connexió entre backend i blockchain (Web3).

A l’hora de programar aquestes parts, hem fet Truffle i Ganache conjuntament (ja que un depèn de l’altre i viceversa) i un cop hem testejat de manera local que tot funciona correctament hem implementat Web3.

# Desplegament[[edit](/pti/index.php?title=Categor%C3%ADa:Apuntalo&veaction=edit&section=7 "Edit section: Desplegament") | [edit source](/pti/index.php?title=Categor%C3%ADa:Apuntalo&action=edit&section=7 "Edit section: Desplegament")]

## Blockchain[[edit](/pti/index.php?title=Categor%C3%ADa:Apuntalo&veaction=edit&section=8 "Edit section: Blockchain") | [edit source](/pti/index.php?title=Categor%C3%ADa:Apuntalo&action=edit&section=8 "Edit section: Blockchain")]

En primer lloc, i com ja s'ha comentat anteriorment, la blockchain que hem fet servir és de desenvolupament i no té un desplegament real a internet. Per tant, hem decidit mantenir aquesta blockchain i deixar la futura implementació global per les possibles millores. Així doncs, la blockchain acaba sent un simple procés que corre al mateix servidor de la FIB i que només s'hi pot accedir des de la API amb les crides de web3.

```
#!/bin/bash
testrpc -a 100 &
truffle migrate

```

## Etherpad[[edit](/pti/index.php?title=Categor%C3%ADa:Apuntalo&veaction=edit&section=9 "Edit section: Etherpad") | [edit source](/pti/index.php?title=Categor%C3%ADa:Apuntalo&action=edit&section=9 "Edit section: Etherpad")]

Per desplegar etherpad, el primer que vam fer va ser Dockeritzar el projecte. Això va ser bastant senzill, ja que el pròpi repositòri d'Etherpad-lite ja té un Dockerfile. Abans, vam haver de crear un settings.json a partir del template, tot i que la configuració es pot editar posteriorment des de el frontend del servidor etherpad.

```
docker build -t nilquera/etherpad-lite:1.1 .
docker push nilquera/etherpad-lite:1.1

```

Desde el Hub de Docker vam associar la imatge al nostre fork de github. D’aquesta forma, cada commit al repositori fa un build automàtic de la imatge i no hem de repetir les comandes anteriors cada vegada. Un cop fet això, podem crear una imatge del servei.

```
sudo docker run -d -e ADMIN_PASSWORD="*******" -p 9001:9001 nilquera/etherpad-lite:latest

```

Com hem vist abans, el servei d'Etherpad es publica al port 9001. Donat que escolta a la interfície ethernet externa, podem accedir a l'etherpad des de fora (amb la vpn) sense problemes. Tot i això, volíem donar-li una capa de seguretat als paquets, ja que no sabíem fins a quin punt Etherpad s'ocupava d'això. Per fer-ho, vam posar l'etherpad darrere d'un reverse proxy amb nginx. Redirigim totes les peticions al port 9002 al port 9001 de l'adreça loopback. El més important, li vam afegir un certificat ssl perquè les connexions anessin xifrades.

## Backend[[edit](/pti/index.php?title=Categor%C3%ADa:Apuntalo&veaction=edit&section=10 "Edit section: Backend") | [edit source](/pti/index.php?title=Categor%C3%ADa:Apuntalo&action=edit&section=10 "Edit section: Backend")]

Pel que fa al backend, hem fet servir PM2, un process manager, per donar-li persistència, flexibilitat i monitoreig. Executar un projecte de node amb pm2 és molt senzill. El pas més important és pm2 startup que s’ocupa de modificar l’init system i fer que el backend es torni a executar si es reinicia la màquina.

## NGINX[[edit](/pti/index.php?title=Categor%C3%ADa:Apuntalo&veaction=edit&section=11 "Edit section: NGINX") | [edit source](/pti/index.php?title=Categor%C3%ADa:Apuntalo&action=edit&section=11 "Edit section: NGINX")]

Hem fet servir NGINX com a reverse proxy dels diferents serveis. La idea principal era la de posar tots els serveis darrere d’un sol port de l’nginx, però Etherpad crea túnels tcp per fer l’edició col·laborativa de documents, i les adreces que fa servir son imprevisibles. Per tant, vam haver de separar els serveis en dos ports: el 443 pel frontend i la api, i el 9002 per l’etherpad.

# Possibles Millores[[edit](/pti/index.php?title=Categor%C3%ADa:Apuntalo&veaction=edit&section=12 "Edit section: Possibles Millores") | [edit source](/pti/index.php?title=Categor%C3%ADa:Apuntalo&action=edit&section=12 "Edit section: Possibles Millores")]

## Etherpad[[edit](/pti/index.php?title=Categor%C3%ADa:Apuntalo&veaction=edit&section=13 "Edit section: Etherpad") | [edit source](/pti/index.php?title=Categor%C3%ADa:Apuntalo&action=edit&section=13 "Edit section: Etherpad")]

Com s'havia comentat anteriorment, seria interessant poder aconseguir que un usuari no pugui accedir a l'Etherpad a no ser que ho faci accedint a un document del frontend. No sabem si és possible fer això, ja que per utilitzar Etherpad s'obre un socket i es necessiten fer crides de l'usuari cap a Etherpad utilitzant el port d'aquest. Així doncs el que s'hauria de fer és crear una associació entre usuaris del frontend i autors de pads. No hem tingut temps de mirar-nos aquesta part però es podria arribar a fer amb crides de l'API.

També ens queda amb Etherpad, guardar tots els pads en una base de dades que no sigui dirtyDB. Tal com planejàvem nosaltres, volíem utilitzar mongoDB, ja que havíem vist en documentació que era possible i com que pel backend ja utilitzem mongo, doncs ens hagués anat bé.

## Backend[[edit](/pti/index.php?title=Categor%C3%ADa:Apuntalo&veaction=edit&section=14 "Edit section: Backend") | [edit source](/pti/index.php?title=Categor%C3%ADa:Apuntalo&action=edit&section=14 "Edit section: Backend")]

En primer lloc, caldria depurar una mica el codi de l'api. El fet és que el codi ha anat creixent en complexitat a mesura que afegíem funcionalitats. A més, les promeses de l'ECMAScript 6 que Express fa servir generen un codi molt identat i difícil de llegir. També hauríem de fer una millor gestió dels errors, fent els try-catchs només quan calgui o utilitzant el catch en cadena de les promeses.

En segon lloc, creiem que MongoDB ha sigut molt bona base de dades per la facilitat d'instal·lació, però el model de classes que vam acabar desenvolupant exigia una base de dades relacional. No és que Mongo no ens permetés fer relacions, però la llibreria que vam fer servir des de el backend no estava preparada per certes coses que necessitàvem fer. La complexitat del codi creixia molt ràpidament per fer coses molt senzilles.

Finalment, caldria afegir moltes funcionalitats a l'aplicació en global (ja que només hem implementat les més importants). Això s'hauria de fer a tots els nivells, tant a frontend com a backend. A l'api s'haurien de crear els mètodes necessaris per gestionar aquestes noves funcionalitats.

## Frontend[[edit](/pti/index.php?title=Categor%C3%ADa:Apuntalo&veaction=edit&section=15 "Edit section: Frontend") | [edit source](/pti/index.php?title=Categor%C3%ADa:Apuntalo&action=edit&section=15 "Edit section: Frontend")]

El frontend té diverses possibles millores per poder implementar. La primera de totes seria poder mantenir les sessions guardades en cookies i no amb emmagatzematge local tal com es fa ara. No seria un canvi difícil de fer, ja que el comportament seria similar, però com que ja des del principi s'ha utilitzat emmagatzematge s'ha decidit seguir utilitzant-lo per evitar problemes.

Per altra banda, seria necessari programar per part de les crides a l'API, accions en cas de tenir errors en la resposta. El codi actual en cas d'error no fa res, com a molt envia un missatge a la consola deixant constància del que hi ha hagut un error o fa un log amb algunes de les variables que s'utilitzen a l'API. Així doncs, s'haurien d'eliminar aquests avisos que serveixen d'informació per programar però no son necessaris que puguin ser vistos per un usuari. Llavors s'haurien de posar avisos a la pàgina per donar feedback del que passa (per exemple si ha introduit incorrectament les credencials).

Una cosa que no hem pogut implementar tampoc, ja sigui per backend i frontend és poder afegir documents com a preferits. És una funcionalitat que ja teniem pensada però que no hem pogut acabar fent perquè ens hem centrat amb altres que hem considerat més importants. També faria falta afegir una secció a la pàgina de l'usuari on es pugui veure els documents on pots participar.

Per últim, estaria bé també mantenir a la navegació de documents, un rastre de les categories que ha anat seleccionant, per si vol poder anar enrere així ho pot fer de forma pràctica i no haver d'utilitzar els botons d'enrere del navegador.

## Blockchain[[edit](/pti/index.php?title=Categor%C3%ADa:Apuntalo&veaction=edit&section=16 "Edit section: Blockchain") | [edit source](/pti/index.php?title=Categor%C3%ADa:Apuntalo&action=edit&section=16 "Edit section: Blockchain")]

Finalment hem decidit simular la blockchain de manera local, ja que per l'ús de l'aplicació (en development) no és necessari tenir-la a una blockchain real. Per tant, una de les millores que es poden fer és passar de una blockchain privada a una global. La dificultat no seria molta.

Un altre millora que es podria fer és implementar una serie de funcions entre backend i blockchain per assegurar una consistència de dades en cas que el servidor blockchain caigui. Com el tenim en local amb testrpc, en cas de caure es perdria tota la informació (historial de transaccions i adreces/balanç dels usuaris). No obstant aquesta informació si que es guarda en el backend, per tant es podria implementar una funció que, en cas de caure la blockchain s'activés i passés totes les dades que teníem al backend a les noves adreces de la blockchain. Aquest cas es podria resoldre si en comptes de fer-la local la tenim en una blockchain existent a internet.