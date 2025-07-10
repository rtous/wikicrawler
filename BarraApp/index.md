[![](images/800px-LogoBarraApp.png)](/pti/index.php/File:LogoBarraApp.png)

Logotip de l'aplicació.

## Contents

* [1 Introducció](#Introducci.C3.B3)
* [2 Motivació](#Motivaci.C3.B3)
* [3 Repositori de Codi](#Repositori_de_Codi)
* [4 Infraestructura](#Infraestructura)
  + [4.1 Servidors](#Servidors)
  + [4.2 Escalabilitat](#Escalabilitat)
  + [4.3 Seguretat](#Seguretat)
* [5 Funcionament general de l’aplicació](#Funcionament_general_de_l.E2.80.99aplicaci.C3.B3)
* [6 Backend](#Backend)
  + [6.1 Tecnologies escollides](#Tecnologies_escollides)
  + [6.2 Seguretat](#Seguretat_2)
  + [6.3 Backend dels pagaments](#Backend_dels_pagaments)
* [7 Frontend](#Frontend)
  + [7.1 Tecnologies escollides](#Tecnologies_escollides_2)
  + [7.2 Estructura de l’aplicació](#Estructura_de_l.E2.80.99aplicaci.C3.B3)
    - [7.2.1 Login i registre d’usuaris](#Login_i_registre_d.E2.80.99usuaris)
    - [7.2.2 Administrador](#Administrador)
    - [7.2.3 Clients](#Clients)
    - [7.2.4 Personal de barra](#Personal_de_barra)
    - [7.2.5 Connexions a la API](#Connexions_a_la_API)
* [8 Base de Dades](#Base_de_Dades)
  + [8.1 Estructura de la base de dades](#Estructura_de_la_base_de_dades)
* [9 Docker](#Docker)
  + [9.1 Base de dades](#Base_de_dades_2)
  + [9.2 Backend](#Backend_2)
  + [9.3 Frontend](#Frontend_2)
  + [9.4 Composició dels Dockers](#Composici.C3.B3_dels_Dockers)
  + [9.5 Desplegament](#Desplegament)
* [10 Aplicació Android](#Aplicaci.C3.B3_Android)
* [11 Possibles millores](#Possibles_millores)
  + [11.1 Millores al Backend](#Millores_al_Backend)
  + [11.2 Millores al frontend](#Millores_al_frontend)
  + [11.3 Millores a la Base de Dades](#Millores_a_la_Base_de_Dades)

# Introducció[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=1 "Edit section: Introducció") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=1 "Edit section: Introducció")]

BarraApp emergeix com una solució innovadora per abordar la ineficiència notòria en les festes populars, especialment aquelles amb una afluència de 1000 a 2000 persones. Amb l'objectiu de millorar l'experiència dels assistents, la plataforma proposa eliminar la necessitat de fer cues per comprar tiquets, permetent als usuaris realitzar les seves comandes directament a través de la nostra aplicació web. Així, la transició a BarraApp busca transformar el procés tradicional de compra de consumicions, optimitzant-ne l'eficiència i facilitant una interacció més àgil amb la barra.

# Motivació[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=2 "Edit section: Motivació") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=2 "Edit section: Motivació")]

L'origen de BarraApp es fonamenta en la identificació d'una problemàtica evident en les festes universitàries i de barri: les tedioses cues per a la compra de tiquets i consumicions. Amb l'objectiu de proporcionar una solució pràctica i millorar l'experiència dels assistents, el nostre equip va decidir encarar aquest projecte. Mitjançant una aplicació web de codi obert, busquem simplificar aquest procés, permetent als usuaris realitzar comandes amb antelació i oferint als organitzadors eines per gestionar preus, estadístiques i transaccions en temps real. Aquesta visió apunta a eliminar la dualitat de cues, millorant l'eficiència del servei de barra i proporcionant una experiència global més satisfactòria per als assistents. La nostra motivació recau en la creença que a través d'aquesta solució, les festes poden evolucionar cap a esdeveniments més eficients i adaptats a les demandes actuals, desbloquejant el potencial de les tecnologies per millorar la gestió i l'experiència de tots els involucrats.

# Repositori de Codi[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=3 "Edit section: Repositori de Codi") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=3 "Edit section: Repositori de Codi")]

Al següent enllaç podreu trobar tot el codi del projecte i instruccions per fer-lo córrer mitjançant docker.
[Repositori Github](https://github.com/MCrumo/BarraApp/tree/main)

# Infraestructura[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=4 "Edit section: Infraestructura") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=4 "Edit section: Infraestructura")]

## Servidors[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=5 "Edit section: Servidors") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=5 "Edit section: Servidors")]

Per fer anar l’aplicació necessitarem:

* Un servidor web que serveixi l’aplicació web del frontend.
* Un servidor que serveixi el backend.
* Un servidor de base de dades
* Un servidor per cada un dels backend específics de plataforma de pagament.

Tots aquests servidors es podrien estar executant a la mateixa màquina o en màquines diferents segons les necessitats.
En el nostre cas, per fer les proves, hem posat tots els serveis al mateix servidor virtual.

## Escalabilitat[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=6 "Edit section: Escalabilitat") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=6 "Edit section: Escalabilitat")]

Els escenaris en què està previst que s’utilitzi l’aplicació serien esdeveniments de com a màxim 1000 o 2000 assistents dels quan un màxim del 10% podrien estar fent ús de l’aplicació. La major part del temps d’utilització de l’aplicació és al dispositiu del client. Per tant, la càrrega que han de suportar els servidors és realment molt baixa. En aquest escenari, no s’ha tingut en compte explícitament una necessitat d’escalabilitat.
Malgrat tot el fet que tots els backend siguin stateless fa que es puguin desplegar diverses instàncies sense problema. Només cal tenir en compte que tots han de compartir la mateixa base de dades que és on podria estar el coll d’ampolla.
En el nostre cas, per fer les proves, hem posat tots els serveis al mateix servidor virtual

## Seguretat[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=7 "Edit section: Seguretat") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=7 "Edit section: Seguretat")]

A nivell de seguretat d’infraestructura. Els únics pots exposats a internet són el 80 i el 443 del servidor web del frontend. El port 80 només està publicat a nivell de compatibilitat legacy, però redirecciona automàticament al port SSL. El port 443 està securitzat amb un certificat SSL.
El backend de l’aplicació es publica mitjançant un reverse proxy com una carpeta del frontend. Per tant, es beneficia de l'encriptació i el certificat SSL del frontend.
Els backend corresponents a la comunicació amb les plataformes de pagament no són, en cap moment, accessibles des d'internet directament. Només es poden fer crides a aquests backends des del backend principal de l’aplicació.

# Funcionament general de l’aplicació[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=8 "Edit section: Funcionament general de l’aplicació") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=8 "Edit section: Funcionament general de l’aplicació")]

El procés de venda ha de permetre al client triar els productes, pagar-los i recollir-los.
Pel pagament utilitzarem plataformes de pagament i mirarem de preparar l’aplicació per poder admetre més plataformes de pagament si es desitja.
Per recollir els productes, l’aplicació generarà un codi QR al client per les comandes ja pagades. Per tant, necessitarem generar codis QR.
El personal de barra haurà de llegir aquest codi QR per comprovar que la comanda està pagada i poder veure el contingut de la comanda. Així doncs, caldrà poder llegir codis QR.

# Backend[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=9 "Edit section: Backend") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=9 "Edit section: Backend")]

## Tecnologies escollides[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=10 "Edit section: Tecnologies escollides") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=10 "Edit section: Tecnologies escollides")]

La tecnologia escollida sobre la qual hem programat el backend ha estat nodejs. És una tecnologia molt popular en l’actualitat i que respon de manera molt adequada amb altres tecnologies actuals. Com que tants programadors l’utilitzen, existeixen un munt de mòduls (així s’anomenen les llibreries de nodejs) programats pels mateixos usuaris que afegeixen funcionalitat i facilitat d’ús a la base de node.
Hem fet també ús de diversos mòduls de nodejs per facilitar la programació. Seguidament, els nomenem i expliquem per a què han estat importants:

* Axios [1.6.2]: Per tal de crear comodament tots els endpoints de tipus GET i POST.
* Express [4.18.2], express-validator [7.0.1] i express-fileupload [1.4.3]: Han estat la base de construcció de la nostra aplicació web, també els hem usat per validar les dades que arriben als endpoints i per permetre la pujada d’arxius de manera còmoda i senzilla des del punt de vista de programació.
* Bcrypt [5.1.1]: Ens ha permès fer un tracte de contrasenyes adequat als requisits del nostre projecte. Permet encriptar les contrasenyes amb SHA256 i afegir un “salt” i un temps mínim de cost de hashing per tal d’augmentar la privacitat a l’hora d’emmagatzemar les contrasenyes. A més permet la comparacio de dos hashes per verificar fàcilment que la contrasenya introduïda és correcte.
* Cors [2.8.5]: Permet definir l’accés des de l’exterior als diferents recursos disponibles al backend.
* Json Web Tokens [9.0.2]: Per a un control robust de sessions, persistència i autenticació dels usuaris.
* nodemailer [6.9.7]: Ens ha facilitat la gestió d’enviament de correus electrònics per funcionalitats com la de verificar el compte creat recentment d’un usuari.
* uuid [9.0.1] i uuid-validate [0.0.3]: Per crear i verificar strings aleatòris, únics i generats de manera segura per tal de poder assignar tokens complexos i únics a elements de la base de dades que necessiten un identificador d’aquest estil per seguretat.
* mysql2 [3.6.1]: Per tal de fer les crides a la base de dades de manera senzilla, segura i còmoda.

## Seguretat[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=11 "Edit section: Seguretat") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=11 "Edit section: Seguretat")]

Des dels primers compassos de la concepció de BarraApp, la nostra visió ha estat clara: oferir una aplicació de codi obert accessible per a tothom. En aquest sentit, garantir la seguretat de l'aplicació ha estat una prioritat inquebrantable. A continuació, detallarem les diverses mesures implementades al backend per assolir aquest objectiu.

La comunicació entre el client i el servidor backend es realitza mitjançant HTTPS, assegurant que la informació confidencial, com ara contrasenyes en text pla, es mantingui encriptada d'extrem a extrem. Això ofereix una capa addicional de protecció, assegurant que la informació sensible romangui inaccessiblement encriptada.

Mitjançant l'ús d'un proxy invers, el backend de l'aplicació es publica com una carpeta del frontend, beneficiant-se així de l'encriptació i el certificat SSL del frontend. Aquesta integració proporciona una capa addicional de seguretat i protecció contra possibles amenaces.

Per garantir la persistència de sessions i l'autenticació dels usuaris, hem implementat l'ús de Jason Web Tokens (JWT). Aquests tokens, signats amb un secret conegut només pel backend, verifiquen les peticions dels usuaris i asseguren que disposin dels permisos necessaris. La inclusió d'informació de l'usuari, com l'identificador i el rol, dins del JWT permet una verificació exhaustiva en temps real, prevenint manipulacions no autoritzades i mantenint la integritat del sistema.

La verificació dels comptes constitueix un punt crucial en la nostra estratègia de seguretat. Imposant la creació d'usuaris amb adreces de correu electrònic pròpies, el procés de verificació s'assegura que cada usuari validi el seu compte mitjançant un enllaç enviat per correu electrònic. Aquest enllaç codifica la seva adreça de correu electrònic i una clau única, garantint una autenticació fiable i minimitzant les possibilitats d'ús fraudulents.

Dins del backend, el sanejament de dades és prioritàri. Per prevenir vulnerabilitats com buffer overflow, SQL injection i altres manipulacions, totes les dades rebudes passen per un exhaustiu procés de validació mitjançant la llibreria express-validator. Aquesta abordatge minuciosa assegura que tota dada sigui verificada pel seu tipus, longitud màxima, camp obligatori i altres criteris, garantint així la integritat del sistema davant possibles amenaces.

En conjunt, aquest conjunt de mesures està dissenyat no només per complir amb els estàndards de seguretat, sinó també per proporcionar una experiència d'usuari robusta i fiable en tot moment.

## Backend dels pagaments[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=12 "Edit section: Backend dels pagaments") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=12 "Edit section: Backend dels pagaments")]

Des d’un principi, el que s’ha intentat és aïllar el màxim possible l'aplicació del funcionament específic de les plataformes de pagament. De tal manera que es poguessin anar incorporant plataformes de pagament sense haver de modificar la manera de funcionar de la nostra aplicació.
La solució que vam adoptar va ser definir una interface comuna a la nostra aplicació i implementar un backend diferent per cada plataforma. La lògica específica de cada plataforma estaria dins el backend específic.
Després de veure com funcionaven dues de les plataformes més utilitzades al nostre entorn (Paypal i Redsys) vam preveure que tots els backend de les plataformes havien de disposar de dos endpoints:
**POST /pay:** Admet un body amb una variable orderId. El Id de la comanda que es pretén pagar. Amb aquest ID recollirà de la base de dades les dades necessàries per poder generar el link de redirecció a la plataforma de pagament.
També registrarà a la base de dades les dades necessàries per poder fer el seguiment del pagament quan la plataforma de pagament retorni el control a la nostra app.
Retornarà al frontend una estructura que permeti redireccionar al client a la plataforma de pagament seleccionada. El retorn es un objecte JSON amb les següents propietats:

* payment: Identificador del pagament a la plataforma de pagament.
* link: URL on redireccionar al client.
* method: POST/GET.
* formData: Un objecte amb els parells key/value dels camps a enviar en cas d’un mètode POST.

**POST /payment-check:** Al body hi haurà els paràmetres enviats per la plataforma de pagament quan retorna el control a la nostra aplicació. L'aplicació es limita a recollir aquests paràmetres i enviar-los al backend específic sense interpretar-los de cap manera.
L’endpoint recollirà aquests paràmetres i els validarà fent les crides necessàries a l’API de la plataforma de pagament corresponent.
Si la validació és correcta registrarà a la base de dades el pagament de la comanda i informarà l’aplicació. En cas que es produeixi algun error també s'informarà l’aplicació que la validació ha fallat.

# Frontend[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=13 "Edit section: Frontend") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=13 "Edit section: Frontend")]

## Tecnologies escollides[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=14 "Edit section: Tecnologies escollides") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=14 "Edit section: Tecnologies escollides")]

Hem decidit triar Angular per programar el nostre frontend perquè era un framework que no havíem fet servir abans, a més oferia molta compatibilitat amb les altres tecnologies que utilitzavem i la corba d'aprenentatge des de zero era realment bona.
Cal destacar els mòduls més importants utilitzats, a banda dels proporcionats per angular:

* ngBootstrap [15.1.1] : És un mòdul de bootstrap especialitzat per ser utilitzat en angular amb el que dóna noves oportunitats de personalització, ha sigut una gran avantatge utilitzar-ho ja que automàticament et fa el spacing per els dispositius mòbils, el que va fer molt més senzill la programació de la interfície visual sense tindre gaire en compte la compatibilitat entre dispositius.
* Angularx-qrcode [16.1.0] : És un módul que vam utilitzar per generar els codis qr a la part del client, quan demana una comanda

## Estructura de l’aplicació[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=15 "Edit section: Estructura de l’aplicació") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=15 "Edit section: Estructura de l’aplicació")]

### Login i registre d’usuaris[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=16 "Edit section: Login i registre d’usuaris") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=16 "Edit section: Login i registre d’usuaris")]

En el login es demana l’email, i la contrasenya d’un usuari ja creat, es crea un formulari i s’envia al backend el qual s’encarrega de validar les dades amb la base de dades. Un cop validades si el login és satisfactori es retorna una clase user, entre les quals conté el rol al qual pertany, aleshores es dirigeix a la pàgina d’inici del rol, mostrant també un missatge de login correcte. Si el login és incorrecte es mostra un missatge d’error indicant que les credencials son correctes.
Pel registre d’usuaris es demanen diversos paràmetres, el email, contrasenya, nom i cognoms i la data de naixement, aquests es comproven que no falta cap i els envia cap al backend, que aquest ho recollirà, i ho inserirà a la base de dades marcat com a no validat i enviarà un email de verificació a l’usuari nou. Quan aquest usuari retorni a la url de verificació ho farà amb dos paràmetres a la URL, el email verificat i una key generada pel backend i l'únic que es fa és enviarlos al backend perquè validi l’adreça. Un cop validada es mostrarà un missatge i es podrà loguejar normal i corrent.

### Administrador[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=17 "Edit section: Administrador") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=17 "Edit section: Administrador")]

Al entrar a cada pàgina de l’entorn d’administrador es mirarà el rol de l’usuari que està loguejat, en cas de que no tingui el rol d’admin se’l reconduirà al login amb un missatge d’error.
Al home d’usuari es mostrarà la llista de família de productes on podrem crear de noves, modificar-les i deshabilitar-les, a més de un botó on ens enviarà a la llista de productes d’aquella família. Hi haurà un checkbox que la podem marcar si volem veure els productes deshabilitats. Això es fa ja que les comandes que es fan s’enregistra el producte i la família de productes, aixi que es deshabiliten per evitar inconsistencies a la base de dades. Quan cliquem a ver productos ens dirigirà al home de la familia de productes, on podem gestionar els productes igual que com ho podíem fer amb les famílies.
També a dalt a la dreta hi ha un menú desplegable on ens podrà reconduïr a les pàgines d’usuaris, on es podran gestionar els diferents usuaris registrats a l’aplicació com canviar el rol per exemple, i la pàgina de configuració, on es podrà configurar els paràmetres del event on pertany com el nom, les diferents plataformes de pagament disponibles i les dies on es celebra l’esdeveniment.

### Clients[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=18 "Edit section: Clients") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=18 "Edit section: Clients")]

L'àrea de client no farà la verificació de rol cada cop que entri ja que és el rol bàsic que se t’assigna un cop et registres.
Només entrar ens sortirà un botó per escollir una comanda, demanant productes dins de les famílies de productes i la quantitat. Un cop escollit la comanda et sortirà el botó per pagar-la i si li cliques et demana la plataforma amb la que vols pagar, la qual et redirigirà cap a la pàgina del servei de pagament escollit. Un cop pagada et mostrarà un botó de mostrar comanda, la qual mostrarà el qr corresponent a aquesta comanda.

### Personal de barra[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=19 "Edit section: Personal de barra") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=19 "Edit section: Personal de barra")]

El personal de barra o bartender només loguejar-se li demanarà els permisos de la càmera i automàticament sortirà la imatge perquè pugui escanejar el codi que mostrarà el dispositiu del client. Un cop escanejat sortirà la comanda i a mesura que els productes estiguin llestos podrà anar marcant-los. No podrà finalitzar i tornar a escanejar comandes noves fins que no hagi seleccionat i servit tots els productes demanats.

### Connexions a la API[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=20 "Edit section: Connexions a la API") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=20 "Edit section: Connexions a la API")]

Les connexions a la API han sigut mitjançant HTTP personalitzant les capçaleres per una major seguretat. Per les peticions GET es feia un tractament de les dades retornades pel backend en forma de JSON, i les peticions POST s’envien les dades en forma de JSON també en el ordre i amb els id’s acordats en el backend per una correcte implementació. Si alguna de les crides el backend retorna un JSON amb un codi d’error diferent i un missatge.

# Base de Dades[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=21 "Edit section: Base de Dades") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=21 "Edit section: Base de Dades")]

Per la base de dades, hem decidit utilitzar el nostre projecte, MySQL. Com que aquesta base de dades està desplegada a un servidor web d’acord amb la nostra manera de treballar, el programari que hem utilitzat per tal de poder editar de forma senzilla la base de dades, exportar-la, crear procediments, taules i coses complexes, ha sigut l’eina phpMyAdmin.

## Estructura de la base de dades[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=22 "Edit section: Estructura de la base de dades") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=22 "Edit section: Estructura de la base de dades")]

[![](images/DatabaseBarraApp.png)](/pti/index.php/File:DatabaseBarraApp.png)

Esquema de la Base de Dades de l'aplicació.

# Docker[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=23 "Edit section: Docker") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=23 "Edit section: Docker")]

Per tal de complir un dels objectius de la nostra pràctica, que era que aquesta aplicació pogués de desplegar de forma ràpida, eficient i senzilla per qualsevol persona que volgués utilitzar el nostre software sense la necessitat de tindre coneixements previs, teníem clar que havíem de dockeritzar la nostra aplicació.
Per tat de poder dur a terme una dockerització, primer hem d’identificar els serveis que tenim funcionant a la nostra web app. Aquest son, com es mostra a la imatge de sota, essecialment 3: la persistencia (base de dades) que utilitzem MySQL, el backend, que utilitzem NodeJs i el frontend que utilitzem Angular i nginx per servir-lo.

## Base de dades[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=24 "Edit section: Base de dades") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=24 "Edit section: Base de dades")]

Com hem dit la base de dades corre sobre MySQL, per tant, versió de la imatge del container de docker que correrà la base de dades, serà la de mysql:8.0.35, que és la que hem anat utilitzant al llarg de la pràctica i la que sabem que funciona.
Per tal de persistir les dades entre del container de base de dades, hem creat un volum que linka una carpeta local del nostre servidor a la carpeta SQL del continer. Això ho fem, ja que cada cop el container pel que sigui es para i s’ha de tornar a aixecar, aquest perdria tota la informació de la base de dades.

Per últim, editem les variables d’entorn amb el nom de la base de dades, usuaris i contrasenyes per tal que el backend es pugui connectar a la base de dades amb les credencials i noms utilitzats i obrim el port 3306 del container per tal de poder fer la comunicació entre aquests.

## Backend[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=25 "Edit section: Backend") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=25 "Edit section: Backend")]

Pel backend hem creat un dockerfile amb la imatge de node:18:17:1, que és amb la que em treballat i sabem que funciona. Per la configuració intenra, hem obert el port 8082 del contenidor perquè el frontend es pugui connectar a ell i hem configurat també totes les variables d’entorn de la base de dades de forma coherent.

## Frontend[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=26 "Edit section: Frontend") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=26 "Edit section: Frontend")]

El frontend té una configuració complexa pel que fa al dockerfile. Hem dividit el stages de la creació de la imatge en tres.
Al primer stage, agafem també la imatge de node:18:17:1 i copiem tots els paquets necessaris pel funcionament de l’apliació.
Al segon stage, agafem la imatge de nginx:stable per tal de poder servir el frontend i copiem les configuracions de nginx necessàries al mateix temps que obrim els ports 80 i 443 de contenidor.
Per últim, a l’stage final, agafem la imatge d’ubuntu:18.04 per tal de poder instal·lar entre d’altres, el repositori de cerbot. Ja que cerbot el que ens proporciona és un certificat SSL de forma gratuïta, per tant podem fer que el contenidor del frontend tingui un certificat SSL i, per tant, podem accedir des de HTTPS.

## Composició dels Dockers[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=27 "Edit section: Composició dels Dockers") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=27 "Edit section: Composició dels Dockers")]

Un cop tenim la configuració d’aquests tres contenidors, arriba el moment d’agrupar-los perquè treballin de forma conjunta amb un docker-compose.
El primer que hem fet és utilitzar una internalnetwork perquè els 3 containers es poguessin veure entre si. Després ens hem assegurat d’obrir els ports corresponents per tal de dur a terme la connexió i hem creat les dependències entre sí, fent que el backend depengués de la base de dades i el frontend depengués del backend. També es pot linkar amb un volum, un fitxar d’inicialització a la base de dades perquè tingui el context que nosaltres vulguem. Per últim, hem creat algun altre volum al frontend pels sites-enabled de nginx i pel /var/www/html per fer-ho persistent.

## Desplegament[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=28 "Edit section: Desplegament") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=28 "Edit section: Desplegament")]

Pel desplegament del Docker, ha sigut tant senzill com executar la comanda del docker-compose per aixecar i connectar tots els containers amb els paràmetres que hem anat configurant. Aquesta precisament era la gràcia de fer-ho amb docker, que simplement amb una instrucció tinguéssim l’aplicació web corrent a un servidor.
Per tant, el funcionament final de la nostra aplicació dockeritzada és el que es mostra a la següent figura:
El client fa una petició al servidor al port 80 o 443 segons sigui HTTP o HTTPS.
El server té corrent els containers, el qual el del frontend està escoltant les peticions del port 80 i 443 de la màquina local tal com ho hem configurat, per tant el container és el que rep les peticions.
Després es comunica segons necessiti amb el backend i aquest eventualment amb la base de dades.
Per tant, en tindre el servidor i amb els tres containers corrent, no cal fer cap configuració especial per tindre corrent la web app.

# Aplicació Android[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=29 "Edit section: Aplicació Android") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=29 "Edit section: Aplicació Android")]

Malgrat que inicialment no estava previst al projecte, vam veure la possibilitat de migrar l’aplicació web a una aplicació mòbil nativa. Fer-ho ens requeria poc temps i facilitava la utilització per als usuaris. A més a més permet més fàcilment disposar d’una tauleta a la barra per llegir codis QR.
Per fer-ho hem utilitzat un framework opensource que es diu capacitor (<https://capacitorjs.com>). Aquest framework, a partir d’una aplicació web genera el codi necessari perquè es pugui compilar una aplicació Android i una aplicació iOS. L’aplicació iOS no l'hem pogut compilar perquè no disposàvem de cap ordinador MAC.
La conversió és força automàtica. Només vam haver de fer 3 petites modificacions a l’aplicació web que van swer la modificació del local storage per tal de guardar ara el JWT a la memòria del telèfon, canviar la configuració de l'escàner de QRs que ara utilitza una llibreria pròpia d'android i el deep linking, per tal que els enllaços i redireccions siguin capturades per l'aplicació i no et porti a la versió web per error.

# Possibles millores[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=30 "Edit section: Possibles millores") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=30 "Edit section: Possibles millores")]

## Millores al Backend[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=31 "Edit section: Millores al Backend") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=31 "Edit section: Millores al Backend")]

El backend és força complet, però hi ha alguns punts on es podria millorar. Per exemple no hi ha una implementació de recuperació de les contrasenyes i és un punt força important per tal de donar per acabada una aplicació que gestiona usuaris de manera complexa i completa.
Seria molt interessant i important d’implementar un sistema d’invalidació de tokens a la banda del backend. Si un usuari tanca la sessió, el token no queda inservible i es pot continuar fent servir mentre no expiri la seva validesa. Com que la comunicació entre client i servidor és segura, no hi ha manera que algú robi el token durant la comunicació entre els dos, però si l’atacant té accés a la màquina de l’usuari aleshores sí que seria capaç d’agafar el token de l’usuari i utilitzar-lo per fer-se passar per ell.
Una altra qüestió de seguretat és que el secret per signar els tokens JWT està en un fitxer de configuració i és estàtic. Hauríem de generar-lo en cada reinici del servidor i guardar-lo en una variable d’entorn. De la mateixa manera, el password del compte de correu que s’utilitza per a l’enviament de correus electrònics de verificació, també es guarda en un fitxer de configuració que es puja als repositoris. Seria molt necessari migrar el guardat d’aquesta dada a la base de dades per exemple i que en iniciar l’aplicació es posés en una variable d’entorn.

## Millores al frontend[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=32 "Edit section: Millores al frontend") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=32 "Edit section: Millores al frontend")]

Al frontend es podria millorar tot el tracte d’errors. Aprofitant que el backend retorna codis específics i clar sobre el tipus d’error que ha succeït, seria interessant que el frontend fos capaç d’interpretar-los i oferís a l’usuari el tracte més oportú segons l’error que ha succeït.
Per altra banda, durant el registre d’un usuari no hi ha cap camp on hagi d’introduir la contrasenya per tal de verificar que no s’ha equivocat ni tampoc hi ha cap requisit sobre la robustesa de les contrasenyes. Seria molt interessant afegir aquesta millora per incrementar la robustesa i la resiliència davant d’atacs de l’aplicació.
Es podrien afegir funcionalitats com estadístiques sobre les compres, un llistat de totes les comandes fetes, de tots els pagaments fets, opcions per l’usuari per buscar famílies o productes mitjançant un buscador, que l’administrador pugui fer cerques d’usuaris com moltes altres funcionalitats que millorarien l’experiència d’ús de l’usuari.

## Millores a la Base de Dades[[edit](/pti/index.php?title=Categor%C3%ADa:BarraApp&veaction=edit&section=33 "Edit section: Millores a la Base de Dades") | [edit source](/pti/index.php?title=Categor%C3%ADa:BarraApp&action=edit&section=33 "Edit section: Millores a la Base de Dades")]

Moltes de les comprovacions de correctesa i de dades que fa el backend les podria fer la base de dades. Seria interessant migrar-les i incorporar-les a la DB per tal que el codi sigui més eficient i les respostes al client més ràpides.