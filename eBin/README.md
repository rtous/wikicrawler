[![](images/Meteoestructura.png)](/pti/index.php/File:Meteoestructura.png)

Estructura del proyecto.

## Contents

* [1 Introducción](#Introducci.C3.B3n)
* [2 Objectius](#Objectius)
* [3 Infraestructura](#Infraestructura)
  + [3.1 Rest API](#Rest_API)
  + [3.2 Persistència](#Persist.C3.A8ncia)
  + [3.3 MQTT](#MQTT)
  + [3.4 Clients MQTT](#Clients_MQTT)
    - [3.4.1 Processament](#Processament)
    - [3.4.2 Sensoring](#Sensoring)
* [4 Desenvolupament Practic](#Desenvolupament_Practic)
  + [4.1 Servidor](#Servidor)
  + [4.2 REST API](#REST_API_2)
  + [4.3 Broker MQTT](#Broker_MQTT)
* [5 Desenvolupament de l'algorisme](#Desenvolupament_de_l.27algorisme)
  + [5.1 Introdució](#Introduci.C3.B3)
  + [5.2 Plantejament inicial](#Plantejament_inicial)
  + [5.3 Primeres optimitzacions](#Primeres_optimitzacions)
  + [5.4 Interfície d’usuari](#Interf.C3.ADcie_d.E2.80.99usuari)
* [6 Entorn de desenvolupament](#Entorn_de_desenvolupament)
* [7 Millores](#Millores)
  + [7.1 Millores per part del front-end](#Millores_per_part_del_front-end)
  + [7.2 Millores en la part hardware](#Millores_en_la_part_hardware)
  + [7.3 Millores en l’algorisme](#Millores_en_l.E2.80.99algorisme)

# Introducción[[edit](/pti/index.php?title=Categor%C3%ADa:eBin&veaction=edit&section=1 "Edit section: Introducción") | [edit source](/pti/index.php?title=Categor%C3%ADa:eBin&action=edit&section=1 "Edit section: Introducción")]

eBin com a plataforma pretén aprofitar la innovació que representen les ciutats intel·ligents usant la tecnologia per reduir la contaminació a la ciutat, tan acústica com ambiental. Per dur a terme aquesta tasca, eBin fa una mesura del nivell de plenitud dels contenidors de la brossa i amb aquestes dades analitza i optimitza el recorregut que han de fer els camions encarregats de la seva recol·lecció, disminuint així els recorreguts (fins i tot podent arribar a eliminar els innecessaris) i contribuint així a la rebaixa dels alts nivells de contaminació que persisteixen avui dia a les ciutats.
Per fer-ho s'apliquen tecnologies de IoT (internet de les coses) orientades a la part hardware encarregada de recollir les dades i enviar-les a un servidor distribuït encarregat de processar-les i generar possibles solucions utilitzant un algorisme VRP (Vehicle Routing Problem). El resultat d'aquest algorisme permet als usuaris visualitzar un mapa amb les rutes òptimes a seguir complint l'objectiu principal.

# Objectius[[edit](/pti/index.php?title=Categor%C3%ADa:eBin&veaction=edit&section=2 "Edit section: Objectius") | [edit source](/pti/index.php?title=Categor%C3%ADa:eBin&action=edit&section=2 "Edit section: Objectius")]

El projecte que es planteja en aquest document, està emmarcat en el context del desenvolupament de sistemes digitals i automàtics a les ciutats. Aquest procés de digitalització de les ciutats les converteix en “smart cities”. El desenvolupament d’aquestes té com a objectiu crear entorns sostenibles que optimitzin l’ús que fan els usuaris i les administracions dels espais públics.

Tot i que a les ciutats existeixen centenars de processos que poden ser subjectes de la digitalització, ebin inclou alguns dels processos pertanyent a l’àmbit de la gestió de residus, oferint la capacitat de generació i posterior tractament de la informació a temps real de la plenitud dels contenidors desitjats.

Els objectius de ebin són en primer lloc, gràcies a la optimització de les rutes emprades per a la recollida de deixalles, reduir els nivells de contaminació acústica i pol·lució generada pels vehicles designats. En segon lloc, la reducció de costos en la recollida d'escombraries perquè una millor utilització d’aquests pot fer que es necessitin menys camions i conseqüentment menys consum de combustible i menys manteniment. De cara als ciutadans això es pot veure reflexat en una disminució dels impostos. A més, l'anàlisis de les noves dades generades pot permetre anàlisis estadistics que permetin crear patrons de comportament dels usuaris i dels districtes de les ciutats. Amb aquestes dades les administracions poden llençar noves estratègies per intentar promoure el reciclatge.

L’objectiu final, però no el menys important, ha sigut crear un sistema d’informació amb un mecanisme de comunicació per poder ser integrat amb altres plataformes de gestió. Així totes les dades que es generen poden ser utilitzades a través d’una API. Aquesta ofereix molta transparència i flexibilitat per al desenvolupament de sistemes de visualització programats per proveïdors externs a ebin.

# Infraestructura[[edit](/pti/index.php?title=Categor%C3%ADa:eBin&veaction=edit&section=3 "Edit section: Infraestructura") | [edit source](/pti/index.php?title=Categor%C3%ADa:eBin&action=edit&section=3 "Edit section: Infraestructura")]

En primer lloc, per entendre el rerefons tecnològic, s’especifica l'arquitectura de la plataforma.
Ebin és una aplicació que respon a un model tecnològic IoT. Per aquest motiu, la seva arquitectura correspon a un sistema d’informació dissenyat per recolectar informació de l’entorn per fer-la explotable per a les persones. Està conformat per 4 mòduls funcionals que utilitzen diferents tecnologies IT. Aquestes tecnologies s’integren mitjançant diferents procediments per aconseguir un entorn usable on l’usuari pugui accedir i gestionar les dades desde una única plataforma.
En segon lloc, des del punt de vista de comunicació entre les entitats que conformen el sistema, s’ha creat un model client-servidor. En aquest context, trobem dos tipus de dispositius diferents.
El primer el servidor. Aquest és el “back-bone” del sistema d’informació. És el punt en comú a través del qual tots els sistemes, tant recol·lectors com consumidors de dades, comparteixen informació. Tots aquests elements s’anomenen clients i conformen el segon grup de dispositius que hem esmentat anteriorment.

En últim lloc, segons la funcionalitat que els diferents blocs duen a terme es pot descriure una arquitectura de tres nivells. Aquests tres nivells corresponen a la presentació, al domini i a la persistència.

En els següents apartats es defineixen de forma més detallada cadascun dels elements utilitzant l’esquema de la següent imatge com a referència. Els elements inclosos dins del requadre blau són tots aquells que corren al servidor. Els elements que estan a fora del quadre són els clients.

## Rest API[[edit](/pti/index.php?title=Categor%C3%ADa:eBin&veaction=edit&section=4 "Edit section: Rest API") | [edit source](/pti/index.php?title=Categor%C3%ADa:eBin&action=edit&section=4 "Edit section: Rest API")]

Una API és una interfície de comunicació entre sistemes informàtics. La conforma un conjunt de definicions i protocols que s’utilitzen per integrar diverses aplicacions. Es pot entendre com un contracte d’intercanvi d’informació entre un proveïdor i un consumidor. El consumidor, també anomenat client fa sol·licituds d’informació i el proveïdor li respon amb la informació que ha sol·licitat. El concepte no és un protocol en si mateix sinó que recull un conjunt d’especificacions per desenvolupar la API de forma estàndard.
Ebin contempla la utilització de la rest api per fer accessible la informació als diferents clients. S’ha decidit escollir aquesta tecnologia perquè permet separar els programes del front end amb el backend, ofereix seguretat, control i escalabilitat. Una alternativa hauria sigut connectar els clients directament a la base de dades per aconseguir la informació. Això hauria complicat molt la lògica dels mateixos i qualsevol canvi a la base de dades obligaria als clients a ser actualitzats.
Per programar la api hem fet servir el framework NodeJS i una llibreria anomenada express. Existeixen moltes alternatives per programar REST APIS i publicar-les a un servidor. Per exemple s’hauria pogut fer servir Python i el framework Flask.

Node JS: node és un entorn que treballa en temps d’execució, de codi obert i multiplataforma que permet desenvolupar aplicacions en javascript per al servidor. Disposa d’un gestor de paquets que permet utilitzar milers de llibreries per afegir totes aquelles funcionalitats requerides al sistema.
Express: és el framework web més popular per NodeJS. Permet, per exemple, la creació de múltiples rutes utilitzant diverses funcions HTTP o la creació de middlewares per afegir funcionalitats a la “pipe” de processament abans de retornar la informació.
Autenticació per token: és un mecanisme que permet l’autenticació dels usuaris a la rest api sense que el backend hagi de guardar informació d’estat (stateless). L’usuari quan inicia sessió passa el seu identificador i la seva contrasenya i el servidor genera un token que l'identifica. Conseqüentment el client cada cop que fa una request ubica el token a la capçalera, el servidor la descodifica i li permet o no l’accés.

## Persistència[[edit](/pti/index.php?title=Categor%C3%ADa:eBin&veaction=edit&section=5 "Edit section: Persistència") | [edit source](/pti/index.php?title=Categor%C3%ADa:eBin&action=edit&section=5 "Edit section: Persistència")]

La capa de persistencia inclou totes aquelles tecnologies que permeten guardar les dades generades en un entorn persistent perquè puguin ser recuperades i no es quedin emmagatzemades únicament en memòria volàtil. A l’apartat desenvolupament del projecte s’explica de forma més detallada l’arquitectura de la capa de persistencia. En aquest apartat es descriuen les dues tecnologies utilitzades per implementar-la.
PostgreSQL: per guardar les dades relacionals s’utilitza postgreSQL. L’esquema de la base de dades que crea el model de dades s’explica de forma més detallada al següent apartat. Postgres és el sistema gestor de bases de dades més avançat. És multiplataforma i té una gran capacitat per treballar amb projectes grans el que augmenta la seva escalabilitat. Node disposa de varies llibreries que permeten interactuar amb la base de dades el que suposa un avantatge.
InfluxDB: per guardar les dades no relacionals, aquelles generades pels sensors, s’utilitza influxDB. És un servidor de bases de dades de series de temps (timeseries). És ideal per guardar de forma eficient dades generades per sensors en la línia temporal i que en ocasions poden arribar a representar un volum de dades molt gran.

## MQTT[[edit](/pti/index.php?title=Categor%C3%ADa:eBin&veaction=edit&section=6 "Edit section: MQTT") | [edit source](/pti/index.php?title=Categor%C3%ADa:eBin&action=edit&section=6 "Edit section: MQTT")]

Abans d'explicar el protocol que s'ha fet servir en l'aplicació, trobem adient fer una petita introducció dels tipus de comunicació que hi ha per IoT. Aquesta indústria que està en continua expansió, necessita protocols lleugers que requereixin poca capacitat de procés, ja que els dispositius on s'utilitzen tenen poca capacitat de càlcul. Una de les possibles solucions és externalitzar aquesta comunicació entre els dispositius, aquest servidor encarregat de rebre missatges i distribuir-los a altres dispositius s'anomena broker.
Per aquest projecte s'ha utilitzat el protocol MQTT. Un protocol que actua sobre TCP (permeten QoS) fent servir una metodologia PubSub amb un servei de missatgeria del tipus Message Queue, on el broker fa unes cues de missatges úniques per cada client que inicia una subscripció (via l'identificador del client). Els missatges romanen a la cua fins a ser entregats.
La metodologia PubSub és un procediment on intervenen dos agents, el subscriptor i el publicador. El primer se subscriu a un tema anomenat "topic" on té el port 1883 (per defecte en MQTT) escoltant permanentment i accepta tots els missatges que arribin amb aquest tòpic. Mentre que el publicador és l'encarregat de publicar aquests missatges amb un tòpic concret.
En el cas pràctic desenvolupat per a eBin només s'ha utilitzat un sensor (o el que seria equivalent a un publicador) amb la qual cosa la cua del broker és única. A més, no hi ha hagut la necessitat de configurar usuaris o seguretat extra, ja que el cas pràctic s'ha fet en una xarxa local, però existeix la possibilitat d'enviar els missatges a través de SSL. S'han instal·lat dos brokers, un que funciona com a pont i l'altre com a rebedor de les dades (el subscriptor). El seu funcionament i aplicació s'explica a la secció de "desenvolupament pràctic".

## Clients MQTT[[edit](/pti/index.php?title=Categor%C3%ADa:eBin&veaction=edit&section=7 "Edit section: Clients MQTT") | [edit source](/pti/index.php?title=Categor%C3%ADa:eBin&action=edit&section=7 "Edit section: Clients MQTT")]

En primera instància es va pensar fer la implementació amb nodes LoRa. Vam trobar adient aquesta opció, ja que s'adaptava molt bé a la nostra idea. Els sensors (nodes LoRa) es posarien dins dels contenidors i aquests enviarien la informació a un gateway mitjançant LoRaWAN, un protocol de xarxa que utilitza la tecnología LoRa per comunicar i administrar dispositius. Principalment es compon de dues parts:
Els gateways que són els encarregats de rebre i enviar informació als nodes i intercanviar dades amb un servidor.
Els nodes que són els dispositius finals que envien i reben la informació al gateway.
Tot i que aquest plantejament és l'idoni per desenvolupar el projecte de forma real, hem triat una altra combinació de dispositius i protocols per formular l'estudi teòric i una possible aplicació al món pràctic, més barata i simple però igual d'efectiva.

Aleshores aquest apartat es pot dividir en dos fases ben diferenciades però relacionades: el processament i el sensoring. La combinació d'aquests tres apartats ens donen una simulació del que faríem amb la tecnologia LoRa i també ens dóna una possible solució a l'objectiu que ens hem marcat.
Processament
Pel processament de les dades, la seva recepció, el seu processament i el seu enviament s'ha triat una placa Arduino, concretament l'Arduino Mega el model més potent de la marca. S'aprofita el microcontrolador reprogramable per rebre les dades del sensor i processar-les de manera que s'enviïn al servidor mitjançant el protocol MQTT. S'ajuda d'una placa ethernet per a la connexió a internet i una protoboard per fer més fàcil la connexió amb el sensor.

### Processament[[edit](/pti/index.php?title=Categor%C3%ADa:eBin&veaction=edit&section=8 "Edit section: Processament") | [edit source](/pti/index.php?title=Categor%C3%ADa:eBin&action=edit&section=8 "Edit section: Processament")]

Pel processament de les dades, la seva recepció, el seu processament i el seu enviament s'ha triat una placa Arduino, concretament l'Arduino Mega el model més potent de la marca. S'aprofita el microcontrolador reprogramable per rebre les dades del sensor i processar-les de manera que s'enviïn al servidor mitjançant el protocol MQTT. S'ajuda d'una placa ethernet per a la connexió a internet i una protoboard per fer més fàcil la connexió amb el sensor.

### Sensoring[[edit](/pti/index.php?title=Categor%C3%ADa:eBin&veaction=edit&section=9 "Edit section: Sensoring") | [edit source](/pti/index.php?title=Categor%C3%ADa:eBin&action=edit&section=9 "Edit section: Sensoring")]

Pel que fa als sensors hem volgut aprofitar al màxim la gran escalabilitat que el IoT ofereix i que la part sensorial d'aquest projecte pot ser fàcilment substituïble. Hem fet l'estudi teòric de dos sensors, un làser i l'altre d'ultrasons tot i que al final només s'ha implementat aquest segon perquè és el que disposàvem, en un cas real s'ha l'aplicació està pensada per tal d'utilitzar el sensor làser.
El model de sensor làser que hem emprat és el VL53L0x, un sensor de distància infraroig d'última generació perfecta per combinar-lo a un processador com Arduino. Aquest sensor mesura distàncies amb un llindar d'entre 50 mm i 2000 mm de forma molt precisa. Aquest tipus de sensor són els més adients per mesurar distàncies, ja que, a part de ser precisos, no es veuen alterats per les condicions ambientals com podrien ser els ecos o el reflex d'altres objectes i a més a més gràcies a la tecnologia que incorporen tenen major immunitat a la llum ambiental i més robustesa a l'hora de cobrir la difonía òptica del vidre. Com la majoria de sensors de distància, funciona emetent un raig de llum làser i mesurant el temps que tarda aquest a tornar novament al sensor. Aquests tipus de sensor s'anomenen ToF (Time of flight). Cal mencionar també que el làser és imperceptible per l'ull humà.

El sensor d'ultrasons que finalment hem posat en pràctica ha sigut el hc-sr04, un dels sensors més utilitzats donat el seu baix cost i la seva fàcil implementació. Tot i no ser tan precís com el sensor làser funciona de la mateixa manera, envia un pols d'alta freqüència no audible per l'ésser humà i mesura el temps que tarda a tornar al receptor, un micròfon. El llindar d'aquest sensor és de 20 mm a 5000 mm. Són uns sensors més sensibles a l'hora de mesurar, és a dir, és molt fàcil que la mesura sigui falsejada amb qualsevol objecte entremig a la superfície real a mesurar generada per un eco o simplement una falsa mesura. També són sensibles a les condicions ambientals (llum, temperatura i humitat).

# Desenvolupament Practic[[edit](/pti/index.php?title=Categor%C3%ADa:eBin&veaction=edit&section=10 "Edit section: Desenvolupament Practic") | [edit source](/pti/index.php?title=Categor%C3%ADa:eBin&action=edit&section=10 "Edit section: Desenvolupament Practic")]

## Servidor[[edit](/pti/index.php?title=Categor%C3%ADa:eBin&veaction=edit&section=11 "Edit section: Servidor") | [edit source](/pti/index.php?title=Categor%C3%ADa:eBin&action=edit&section=11 "Edit section: Servidor")]

A continuació es descriuen amb més detall tots els sistemes que s’han programat i s’han integrat per aconseguir les funcionalitats requerides.
Servidor
Com s’explica a l’apartat anterior el servidor és el node principal de l’aplicació i el que permet que la resta de mòduls disposin d’un entorn amb informació fiable i capacitat d’integració amb altres mòduls. Degut a la seva complexitat s’han dividit les seves funcionalitats tenint en compte la funcionalitat i la tecnologia feta servir per cadascuna d’elles.

A continuació es descriuen cadascun dels mòduls amb detall. Però primer s’explicarà l’arquitectura de la plataforma a nivell d’implementació. El servidor està instal·lat a una màquina virtual proporcionada per la FIB. El desplegament dels serveis s’ha fet utilitzant docker per introduir els programes en contenidors de software proporcionant una capa addicional d’abstracció i automatització de la virtualització. El servidor web està exposat al port 80, la REST API al port 9090 i el broker mqtt 1883.
Persistència
En primer lloc, la persistència inclou els components que tenen com a funcionalitat principal emmagatzemar les dades que genera el sistema i assegurar la seva disponibilitat i integritat. En la nostra aplicació existeixen dos tipus de dades diferents. En primer lloc, aquelles que tenen com a funcionalitat principal definir una lògica estructural i un conjunt d’actors. Aquestes s’anomenen dades relacionals per emmagatzemar-les s’utilitza un gestor de bases de dades relacional i orientat a objectes de codi lliure anomenat PostgreSQL.

La imatge insertada al final de l’apartat, mostra el disseny relacional que s’ha explicat al paràgraf anterior en forma de diagrama de classes. En primer lloc, la entitat principal es defineix com a Organització. Una organització es pot definir com un conjunt d’usuaris i de recursos. La classe usuari recull característiques sobre qualsevol dels usuaris que interactua amb el sistema d’informació. Com s’explica en més detall al següent apartat els usuaris tenen rols i poden accedir a les funcions dpenent d’aquests. Els recursos dels quals disposen els usuaris són els sensors, contenidors, les ubicacions i els camions. La gestió dels recursos sempre la fan usuaris administradors que fan possible la correcta utilització dels mateixos pels usuaris no administradors. L'assignació dels sensors que són els elements que recullen les dades del carrer, amb els propis contenidors es fa a través de la taula Assignació de sensors que ofereix un marc temporal perquè els sensors es puguin canviar de contenidor. La assignació de contenidors a les ubicacions es fa fent servir el mateix raonament a través de la taula Assignació d’ubicacions.

El segon tipus de dades que interactuen amb el sistema són les generades pels sensors col·locats als contenidors, que representen el percentatge d’ocupació dels mateixos. Aquest tipus d’informació ens presenta un marc molt diferent al explicat anteriorment. En aquest context, trobem un volum de dades molt gran que representen un valor en el temps però que defineixen una estructura per si soles. Per gestionar aquesta informació hem utilitzat un altre tipus de gestor de bases de dades, en aquest cas enfocat a la gestió dels timeseries, anomenat InfluxDB. Ofereix capacitats de processament de dades associades amb períodes temporals molt optimitzades per reduir l'espai d’emmagatzemament. La estructura que hem dissenyat per aquesta base de dades és una taula on es guarden els valors per a tots els sensors existents. Cada registre conte l’identificador de sensor, el percentatge d’ocupació i la data d’enregistrament.

## REST API[[edit](/pti/index.php?title=Categor%C3%ADa:eBin&veaction=edit&section=12 "Edit section: REST API") | [edit source](/pti/index.php?title=Categor%C3%ADa:eBin&action=edit&section=12 "Edit section: REST API")]

Per accedir a tota la informació descrita al paràgraf anterior el sistema disposa d’una REST API. Aquesta facilita un medi per extreure i introduir dades de forma molt àgil utilitzant consultes HTTP. El mecanisme ha estat desenvolupat utilitzant Node.js que és un entorn d’execució multiplataforma, de codi obert basat en el llenguatge de programació Javascript. S’ha utilitzat una llibreria anomenada Express que conté el gestor de paquets npm i que aporta totes les funcionalitats de creació i administració de rutes per a les consultes HTTP.

Com s’ha explicat anteriorment el sistema disposa de l’assignació de rols als usuaris. Aquesta funcionalitat la permet la API. En primer lloc l’autentificació dels usuaris es duu a terme mitjançant un mecanisme de tokens. Quan un usuari inicia sessió rep un token que l’identifica i que és el que introdueix al header de totes les seves consultes. Aquest token només és vàlid durant 15 dies. Després d'aquest temps caduca i l’usuari ha de sol·licitar un nou token. Un cop el servidor rep una consulta disposa d’unes funcions middlewares que descodifiquen el token, identifiquen l’usuari i comproven si existeix i té permisos per dur a terme la funció que solicita. Existeixen tres nivells de permisos. En primer lloc, l’usuari root és l'únic que pot crear organitzacions. Només n’hi ha un i es crea quan es crea la base de dades. En segon lloc, existeixen usuaris administradors. Aquests poden donar d’alta tant usuaris com recursos de la seva pròpia organització (tenen permís write). En tercer lloc tenim els usuaris que només tenen permisos de lectura sobre els recursos de la seva organització.

Per acabar, el programa que gestiona la API té una última funcionalitat. El fil d’execució principal només es dedica a la gestió de sol·licituds de la API. Tot i això, existeix un segon fil d’execució on el programa es subscriu al broker MQTT i que cada cop que rep informació d’un sensor l'emmagatzema a la base de dades influx. Així es construeix un model time series on cada valor està identificat pel sensor que l’ha generat i l’instant de temps en el qual s’ha creat.

## Broker MQTT[[edit](/pti/index.php?title=Categor%C3%ADa:eBin&veaction=edit&section=13 "Edit section: Broker MQTT") | [edit source](/pti/index.php?title=Categor%C3%ADa:eBin&action=edit&section=13 "Edit section: Broker MQTT")]

Si tornem a donar un cop d'ull a la figura 1, corresponent a la part hardware del projecte l'hem desenvolupat seguint la idea del que s'ha explicat en l'apartat anterior.
S'ha partit d'un problema com a base i és que la placa d'Arduino no té suport hardware per tolerar una connexió VPN, ja que aquesta és la manera de connectar-se amb el servidor, que es troba a la FIB. Per resoldre això s'ha fet servir el que s'anomena MQTT Bridge, formant un pont entre el sensor (l'Arduino) i el servidor passant per un gateway, en aquest cas hem fet servir un PC connectat a la mateixa xarxa que l'Arduino. Per desenvolupar aquest pont, s'ha modificat la configuració inicial del mosquitto al PC que fa de gateway, de la següent manera.

A la figura 6 podem veure el nom de la connexió (ha de ser únic per a cada connexió), en aquest cas "bridge01". Seguidament tenim l'adreça IP del broker que volem que faci de pont i després ve la configuració pròpiament dita. En primer lloc ve el tòpic pel qual aquest broker farà de pont (pot fer de pont per un o més tòpics), seguidament la direcció, que pot ser d'entrada, de sortida o en ambdós sentits com és el cas, també se li afegeix la QoS (0, 1, 2 depenent el nivell que vulguem de menys qualitat a més) i per últim tenim els prefixos locals i remots, que en aquest cas no estan especificats, però serveixen per reassignar tòpics d'una cadena de tòpics.

En la Figura 7 podem veure l’estructura final de la part hardware del projecte. Es veu com el PC fa de pont entre el sensor i el servidor ja que està configurat en ambdues direccions com publicador i subscriptor, per tant un missatge que tingui el seu origen al sensor, serà publicat al PC que està subscrit i aquest mateix ho publicarà al servidor que ja estava subscrit al mateix tòpic.
Un exemple de dades enviades i rebudes les podem veure en les següents imatges. Són captures fetes de les subscripcions al tòpic “Barcelona/Eixample/CValencia/204” del PC-Bridge i del Server a mode de prova. Són enviades en format JSON per tenir més facilitat a l’hora de tractar-les per part del servidor.

En aquest cas, la configuració del mosquitto s’ha posat localhost a l’opció de host però és igual de vàlid que posar la IP del servidor (figura 9) o no posar res, ja que pel mosquitto és implícit.

En la figura anterior podem veure una part del codi programat a l'Arduino corresponent a la construcció de la resposta enviada al servidor. A la línia 66 tenim una funció de la llibreria del sensor que ens retorna la distància en centímetres mesurada pel sensor. Seguidament apliquem una fórmula per convertir aquesta distància en percentatge de plenitud, contant que els contenidors tenen 170cm d'altura. Aleshores es guarda en un buffer les dades en format JSON amb l'identificador d'aquesta placa en concret (camp identity) i el valor de plenitud. Finalment el contingut d'aquest buffer és publicat al tòpic configurat prèviament.

# Desenvolupament de l'algorisme[[edit](/pti/index.php?title=Categor%C3%ADa:eBin&veaction=edit&section=14 "Edit section: Desenvolupament de l'algorisme") | [edit source](/pti/index.php?title=Categor%C3%ADa:eBin&action=edit&section=14 "Edit section: Desenvolupament de l'algorisme")]

### Introdució[[edit](/pti/index.php?title=Categor%C3%ADa:eBin&veaction=edit&section=15 "Edit section: Introdució") | [edit source](/pti/index.php?title=Categor%C3%ADa:eBin&action=edit&section=15 "Edit section: Introdució")]

L’algorisme proposat ha de resoldre el problema de la generació de rutes (les més òptimes possibles) passant per tots els punts d’un conjunt en un temps de computació raonable.

El problema és un VRP(Vehicle Routing Problem) on l’objectiu és trobar el conjunt de rutes a realitzar per un grup de vehicles per tal de minimitzar el recorregut total.
Aquest problema en sí és una generalització del problema TSP(Travelling salesman problem) del tipus NP-complet (poden ser resolts màquines determinístiques de Turing en un temps exponencial).

En el moment d’investigació prèvia no vam trobar aquesta informació i per aquest motiu la solució proposada no és la òptima, donant peu a la millora d’aquest en un futur. Això també justifica l’evolució del seu plantejament que difereix de les tècniques usades avui en dia per a tal de resoldre’l.

El plantejament de l’algorisme ha seguit aquest recorregut:

### Plantejament inicial[[edit](/pti/index.php?title=Categor%C3%ADa:eBin&veaction=edit&section=16 "Edit section: Plantejament inicial") | [edit source](/pti/index.php?title=Categor%C3%ADa:eBin&action=edit&section=16 "Edit section: Plantejament inicial")]

Inicialment es va plantejar fer servir únicament dijkstra. Abans de començar a implementar-ho ja ens vam adonar que no era viable ja que la filosofia que hi ha darrere és diferent i no funciona en escenaris determinats.
Concretament:
-No funciona en un graf estrella on les puntes presenten adjacències amb les veïnes amb un cost superior en una unitat a l’aresta del centre a la punta. (Veure figura 11).

Per tant vam decidir decantar-nos per una solució basada en backtracking (brute force searching) on inicialment explorem totes les opcions.
Hem de tenir en compte que tots els punts es troben sobre un mapa amb carrers pels quals es pot circular i on hi ha un sentit de direcció. Per trobar la ruta entre un punt i un altre fem servir l’algorisme de dijkstra proveït per la API de BNG maps. Figura 11 i 12.
Això ens permet convertir el mapa en un graf abstracte on cada vèrtex és el punt del mapa que volem referenciar i les arestes són el resultat d’aplicar dijkstra des d’un vertex al veí.

Sense tenir en compte el cost de computació inicial per crear el graf abstracte el cost de l’algorisme és de О(n\*n!). Aquesta solució no escala i amb valors de n superiors a 20 (sigui n el nombre de vèrtexs) ja no és viable.

### Primeres optimitzacions[[edit](/pti/index.php?title=Categor%C3%ADa:eBin&veaction=edit&section=17 "Edit section: Primeres optimitzacions") | [edit source](/pti/index.php?title=Categor%C3%ADa:eBin&action=edit&section=17 "Edit section: Primeres optimitzacions")]

En aquest moment vam decidir optimitzar l’algorisme per tal de reduir el nombre de solucions a explorar (branch cutoff)

Les diferents optimitzacions implementades van ésser:
No seguir explorant una solució si aquesta ja porta un recorregut superior a qualsevol solució trobada.
Tenint en compte que l’algorisme es farà servir per una agència de transport de residus podem assumir un punt d’origen dels vehicles (les cotxeres) i un punt destí (la deixalleria, per exemple). Això permet passar de la computació de totes les opcions possibles des de tots els punts a comptar totes les opcions des d’un únic punt (el més proper a l’origen). Això fa que el cost de l'algorisme passi a ser О(n!).
Definir veïns a cada vèrtex en funció de la seva posició per a tal de no visitar vèrtexs molt llunyans ja que no seran part de la solució. (Veure figura 13).

Aquestes optimitzacions permeten com ja s’ha mencionat reduir el cost del càlcul de О(n\*n!) a О(n!). (Recordem que no estem tenint en compte el temps de generació de les arestes amb l'algorisme de dijkstra.

Tot i aquestes optimitzacions a l’hora de fer tests ens vam trobar en que introduïnt valors de n superiors a 30 el temps de computació era superior a quinze minuts, per tant encara no era una solució viable a l’hora d’escalar.

```
=== Divisió per zones ===

```

Per tal de poder reduir de forma considerable el temps d’execució vàrem concloure que la millor optimització passava per aplicar l’estratègia de dividir i vèncer.
En el nostre escenari es tradueix en dividir recursivament el mapa fins que cada subdivisió tingui un valor màxim arbitrari de m contenidors (en la nostre solució m val 20). (Veure figura 14).

Un cop arribat a aquesta divisió es procedeix a fer la crida a l’algorisme de backtrack per a trobar la ruta òptima de cada una de les subzones i posteriorment aquestes s’encadenen en una única solució

Aquesta divisió recursiva ens permet passar d’un cost algorísmic de O (n!) = O (n^n)
a O(log (n!)) = O(n log n)
Interfície d’usuari
El desenvolupament de la part d’interfície gràfica per l’experiència dels usuaris s’ha centrat en el disseny d’una pàgina web amb les funcionalitats bàsiques per provar la interacció amb l’usuari. Aquesta ha integrat els llenguatges Html, CSS i javascript (aquest darrer per implementar el dinamisme dins la web).
Les peticions al servidor s’han implementat fent servir peticions http via XMLH proveït per javascript.
El mapa presentat a la plana web s’ha implementat fent servir les eines ofreses per mapbox.

## Interfície d’usuari[[edit](/pti/index.php?title=Categor%C3%ADa:eBin&veaction=edit&section=18 "Edit section: Interfície d’usuari") | [edit source](/pti/index.php?title=Categor%C3%ADa:eBin&action=edit&section=18 "Edit section: Interfície d’usuari")]

El desenvolupament de la part d’interfície gràfica per l’experiència dels usuaris s’ha centrat en el disseny d’una pàgina web amb les funcionalitats bàsiques per provar la interacció amb l’usuari. Aquesta ha integrat els llenguatges Html, CSS i javascript (aquest darrer per implementar el dinamisme dins la web).
Les peticions al servidor s’han implementat fent servir peticions http via XMLH proveït per javascript.
El mapa presentat a la plana web s’ha implementat fent servir les eines ofreses per mapbox.

# Entorn de desenvolupament[[edit](/pti/index.php?title=Categor%C3%ADa:eBin&veaction=edit&section=19 "Edit section: Entorn de desenvolupament") | [edit source](/pti/index.php?title=Categor%C3%ADa:eBin&action=edit&section=19 "Edit section: Entorn de desenvolupament")]

El desenvolupament del projecte s’ha fet sobre la màquina virtual que ha proporcionat la FIB. En aquesta s’han creat un conjunt de contenidors per contenir els diversos serveis descrits als apartats anteriors. Cal dir que aquesta màquina només és accessible a través de la VPN de la facultat el que afegeix una capa de seguretat molt important per evitar que la màquina pugui ser vulnerada per persones externes a la facultat. En un entorn real el servidor es podria instalar a la xarxa privada d’una organització.

A més per crear un entorn de prova de la REST API s’ha utilitzat un software anomenat Postman que facilita la creació de crides estàndard i d’entorns de test automatitzat. Finalment per gestionar correctament el codi s’ha fet servir el software de control de versions git i el servidor de git de la fib, el fibgit.
CONCLUSIONS

Per a tal de presentar les nostres conclusions primer recordarem el nostre objectiu.
Tenint en compte la tendència a nivell global de gentrificació de les metròpolis i abandonament de les zones rurals, sumat a evolució de les ciutats en l’era de la informació amb i la propensió d’aquestes al model de les smart cities vam creure oportú desenvolupar aquest treball marcant-nos com a objectiu la disminució de la pol·lució.
Respecte a aquest propòsit, tot i que considerem que per acabar el projecte ens mancaria un estudi de simulació, comparant el nostre treball amb altres ja existents i aplicats, ens trobem encaminats en la mateixa direcció.
Una altre meta que teníem era la investigació, el descobriment i l’aprenentatge de tecnologies desconegudes per als integrants del grup. Aconseguint així fer un projecte que les desenvolupés i les integrés en un conjunt que tingués una finalitat tangible.

Considerem que aquest objectiu s’ha complert, tot i que volem remarcar que la gran major part d’aquestes tecnologíes eren centrades al back-end, motiu pel qual la part relativa a la presentació i visualització, així com la interacció amb l’usuari final (el front-end) s’ha deixat pendent de millora.

# Millores[[edit](/pti/index.php?title=Categor%C3%ADa:eBin&veaction=edit&section=20 "Edit section: Millores") | [edit source](/pti/index.php?title=Categor%C3%ADa:eBin&action=edit&section=20 "Edit section: Millores")]

### Millores per part del front-end[[edit](/pti/index.php?title=Categor%C3%ADa:eBin&veaction=edit&section=21 "Edit section: Millores per part del front-end") | [edit source](/pti/index.php?title=Categor%C3%ADa:eBin&action=edit&section=21 "Edit section: Millores per part del front-end")]

Aquest projecte s’ha centrat en la part back-end, per tant s’ha deixat pendent la visualització i presentació dels resultats. Com a solució provisional s’ha fet una web bàsica on es poden trobar les funcionalitats bàsiques i funcionals, l’eix del projecte.
Tot i això, tot el que engloba a la part de back-end s’ha desenvolupat de tal manera que és totalment independent, l’arquitectura en 3 nivells diferenciades permeten una gran escalabilitat i versatilitat a l’hora de presentar les dades, ja sigui mitjançant una web convencional, una progressive web app o inclús una aplicació per a dispositius mòbils.
Donada aquesta arquitectura, la presentació està separada del domini per tant de manera molt àgil es pot variar la manera de visualitzar les dades, ja que tenim un back-end ben estructurat que facilita l’escalabilitat del front-end.

### Millores en la part hardware[[edit](/pti/index.php?title=Categor%C3%ADa:eBin&veaction=edit&section=22 "Edit section: Millores en la part hardware") | [edit source](/pti/index.php?title=Categor%C3%ADa:eBin&action=edit&section=22 "Edit section: Millores en la part hardware")]

En un cas real, el més adient com s’ha introduit anteriorment, és fer servir nodes LoRa. Aquesta tecnología és molt més potent que el sistema presentat en aquest informe tot i tenir un major cost.

### Millores en l’algorisme[[edit](/pti/index.php?title=Categor%C3%ADa:eBin&veaction=edit&section=23 "Edit section: Millores en l’algorisme") | [edit source](/pti/index.php?title=Categor%C3%ADa:eBin&action=edit&section=23 "Edit section: Millores en l’algorisme")]

Implementar la recollida dels contenidors no obligatoris pero si recomanats que coincideixin en la ruta traçada.
Fer la concatenació de les zones en funció del vèrtex més proper de la zona següent i de la anterior. Això implica cridar l’algorisme des del vèrtex de la zona actual més proper a l’últim visitat de la zona zona anterior i forçar el recorregut perquè acabi al vèrtex més proper a la zona següent.
Fer una generació de les rutes en el cas de >1 vehicle que obtingui la menor distància recorreguda total (la suma de les distàncies de les rutes de tots els vehicles) i no ho faci per a un vehicle i després divideixi per tants vehicles.