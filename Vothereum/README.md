[![](images/400px-LogoVothereum.png)](/pti/index.php/File:LogoVothereum.png)

Logo.

## Contents

* [1 Introducció](#Introducci.C3.B3)
* [2 Objectius del projecte](#Objectius_del_projecte)
* [3 Punt de partida i orientació](#Punt_de_partida_i_orientaci.C3.B3)
* [4 Treballs relacionats](#Treballs_relacionats)
* [5 Estructura del Projecte](#Estructura_del_Projecte)
  + [5.1 Esquema de l’arquitectura](#Esquema_de_l.E2.80.99arquitectura)
  + [5.2 Smart Contract](#Smart_Contract)
  + [5.3 Pàgina Web](#P.C3.A0gina_Web)
    - [5.3.1 Introducció](#Introducci.C3.B3_2)
    - [5.3.2 Disseny web](#Disseny_web)
    - [5.3.3 Web3 i JS](#Web3_i_JS)
  + [5.4 Integració](#Integraci.C3.B3)
* [6 Tests i simulació](#Tests_i_simulaci.C3.B3)
  + [6.1 Proves de funcionament](#Proves_de_funcionament)
  + [6.2 Limitacions](#Limitacions)
  + [6.3 Casos d’ús](#Casos_d.E2.80.99.C3.BAs)
  + [6.4 Simulació Blockchain](#Simulaci.C3.B3_Blockchain)
  + [6.5 Dockerització](#Dockeritzaci.C3.B3)
    - [6.5.1 Python i Flask](#Python_i_Flask)
* [7 Millores futures](#Millores_futures)
  + [7.1 En general](#En_general)
  + [7.2 zk-SNARKs](#zk-SNARKs)
* [8 Anàlisi econòmic](#An.C3.A0lisi_econ.C3.B2mic)
* [9 Conclusions](#Conclusions)
  + [9.1 Problemes](#Problemes)
  + [9.2 Reptes aconseguits](#Reptes_aconseguits)
* [10 Bibliografia](#Bibliografia)

# Introducció[[edit](/pti/index.php?title=Categor%C3%ADa:Vothereum&veaction=edit&section=1 "Edit section: Introducció") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vothereum&action=edit&section=1 "Edit section: Introducció")]

Amb totes les votacions en les que hem de participar aquest any (i els conflictes que estan succeint en països amb governs corruptes), hem intentat trobar una solució per poder votar telemàticament i que la votació sigui anonima. Per implementar aquest sistema hem utilitzat la Blockchain de Ethereum per assegurar-nos que els vots emesos no es puguin modificar o esborrar, d’aquesta manera posem remei a un problema real on es corrompeix la votació. Un altre aspecte que soluciona la nostra aplicació es el problema que tenen els habitants de petites urbanitzacions o pobles ja que s’han de desplaçar a un altre municipi per exercir el seu vot, amb aquest sistema no els caldria desplaçar-se i podrien votar des de casa seva.

El nostre sistema de votació permet que un usuari crei una votació amb una data d’inici i una data final i afegir un cens, és a dir, les persones que poden votar en aquella votació, posteriorment només podran votar en aquella votació els usuaris que hagin sigut autoritzats pel creador de la votació i només ho podrán fer una vegada. Com hem comentat abans, l’hem construït al voltant de la Blockchain d’Ethereum utilitzant el llenguatge Solidity per escriure el Smart Contract que es l’encarregat de definir les transaccions que podrem fer a la blockchain. Per construir la pàgina web hem utilitzat HTML, CSS, Bootstrap i JavaScript per la comunicació amb la blockchain. Per fer la simulació de la blockchain hem utilitzat Truffle, Ganache que posa en funcionament una blockchain monitorizable a partir d’una interfície gràfica i Node.js per aixecar la pàgina web, també hem utilitzat Docker per dockeritzar la pàgina web.

# Objectius del projecte[[edit](/pti/index.php?title=Categor%C3%ADa:Vothereum&veaction=edit&section=2 "Edit section: Objectius del projecte") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vothereum&action=edit&section=2 "Edit section: Objectius del projecte")]

L’objectiu principal del nostre projecte és dissenyar un sistema de votació telemàtica on no hi pugui haver cap tipus de corrupció de les dades, no poder falsejar el resultat de la votació i que la votació sigui anònima. D'altra banda com a grup ens enfrontem a una tecnología en la qual cap membre del grup hi havia treballat abans i per aquest motiu ens semblava molt interessant poder dissenyar aquest sistema utilitzant la blockchain d’Ethereum.

Per tal d’assolir el nostre objectiu, hem hagut de fer un treball previ d’investigació sobre com funciona la blockchain d’Ethereum, com interactuar amb aquesta i com escriure el nostre SmartContract.

# Punt de partida i orientació[[edit](/pti/index.php?title=Categor%C3%ADa:Vothereum&veaction=edit&section=3 "Edit section: Punt de partida i orientació") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vothereum&action=edit&section=3 "Edit section: Punt de partida i orientació")]

Quan emergeix una nova tecnologia sol haver un interès associat per a la seva proliferació. Conseqüentment, els mateixos desenvolupadors s’encarreguen de generar documentació oficial per a facilitar la feina als desenvolupadors d’aplicacions i procurar-ne així la seva difusió. A la vegada, també és comú que n’apareguin tutorials per animar a aquells desenvolupadors menys experimentats a dur a terme les seves apps amb la nova tecnologia. Per al cas de les dapps (apps descentralitzades) és freqüent trobar tutorials que facin servir com a exemple un procés electoral ja que combina la simplicitat convenient per un tutorial i un cas d’ús adequat per una aplicació descentralitzada.

Tant és així que nosaltres hem partit del tutorial d’aquest link i n’hem estès la funcionalitat. Els primers passos del tutorial ens han servit per preparar l’entorn on desenvoluparíem la dapp. A partir d’allà, i pel mor d’introduir les noves funcionalitats, ens hem vist obligats a entendre les tecnologies web com jQuery i Bootstrap per qüestions de la interfície, com JS i web3 pel control lògic de l’aplicació i la interacció amb la blockchain. També, com era d’esperar, l’smart-contract en Solidity i l’ús de Truffle i Ganache en la simulació.

El punt de partida és una dapp on cada proposal només pot acceptar tres tipus de vots (a favor, en contra i abstenció). Les votacions les podia exercir qualsevol usuari en poder d’una account (per tant no tenia definit un cens), la interacció amb la blockchain es fa a partir de Metamask, sense dates d’inici i fi de les votacions i amb un únic frame com a interfície gràfica de la web. A partir d’aquí hem anat incorporant totes les funcionalitats esmentades.

# Treballs relacionats[[edit](/pti/index.php?title=Categor%C3%ADa:Vothereum&veaction=edit&section=4 "Edit section: Treballs relacionats") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vothereum&action=edit&section=4 "Edit section: Treballs relacionats")]

Existeixen diversos projectes d’aplicacions descentralitzades per implementar un sistema de votació electrònic i segur com SecureVote, Polys, Voatz i Vocdoni entre d’altres. El nostre projecte referent ha sigut Vocdoni, una aplicació opensource que implementa la tecnologia zk-SNARKS i LRS (Linkable Ring Signatures) per aconseguir que el vot sigui anònim. En Vocdoni es van plantejar la idea de poder votar des d’un dispositiu electronic de manera electronica i evitant la censura. Van decidir resoldre aquest problema utilitzant la blockchain d’Ethereum i les característiques principals d’aquest projecte son:

- Utilitza la xarxa d’Ethereum i minimitza les transaccions a la blockchain.

- Els votants no escriuen a la blockchain, només llegeixen d’aquesta.

- Els votants poden participar des de una pàgina web o una aplicació Android o iOS.

- Aconsegueixen un vot segur i anònim utilitzant zk-SNARKS i Linkable Ring Signatures.

- La disponibilitat de les dades es troba en un sistema d’emmagatzematge descentralitzat (IPFS, SWARM).

- L’usuari pot comprovar la correctesa dels resultats i que s’hagi comptabilitzat correctament el seu vot.

- Tot el procés es verificable per qualsevol observador extern.

Vocdoni no depèn ni de DNS, IPs específiques ni de cap companyia específica o cap infraestructura en el cloud, això permet que tothom pugui votar evitant qualsevol tipus de censura.
Cal destacar que la característica més important és a més de totes les mesures de seguretat que aplica aquest projecte, la implementació del vot anònim, podent així respectar la privacitat de l’usuari que utilitza aquesta aplicació.

# Estructura del Projecte[[edit](/pti/index.php?title=Categor%C3%ADa:Vothereum&veaction=edit&section=5 "Edit section: Estructura del Projecte") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vothereum&action=edit&section=5 "Edit section: Estructura del Projecte")]

## Esquema de l’arquitectura[[edit](/pti/index.php?title=Categor%C3%ADa:Vothereum&veaction=edit&section=6 "Edit section: Esquema de l’arquitectura") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vothereum&action=edit&section=6 "Edit section: Esquema de l’arquitectura")]

[![](images/800px-Estructura\_tecnologies\_vothereum.png)](/pti/index.php/File:Estructura_tecnologies_vothereum.png)

Esquema de les tecnologies.

Per tenir una visió global de les tecnologies que s’han utilitzat, aquest esquema ens il·lustra de com es relacionen les diferents tecnologies i quina funció fan.

## Smart Contract[[edit](/pti/index.php?title=Categor%C3%ADa:Vothereum&veaction=edit&section=7 "Edit section: Smart Contract") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vothereum&action=edit&section=7 "Edit section: Smart Contract")]

El Smart Contract ens serveix per definir les regles de la blockchain. Bàsicament és la part de programació de la blockchain, on es programen els mètodes amb els que crearem les votacions, mètodes per fer les diferents comprovacions…

S’ha fet servir un smart-contract senzill. S’estructura com si fos una classe, amb els seus atributs i mètodes, de manera que en fer-ne el deploy s’en crea una instància a la Blockchain. Per començar cal posar un indicador per avisar al compilador de la versió mínima de solidity a utilitzar. El nostre contracte (o “classe”) es diu Voting i farà servir un struct per cada proposal amb el títol, dates d’inici i fi, un únic string de candidats codificats en JSON, un array d’int amb tantes posicions com candidats, per anar-hi sumant els vots, i un mapping que no és més que una taula de hash que per a cada address donada (cada votant tindrà la seva) té associat un struct amb les dades del votant. Per això caldrà estar registered (que vol dir estar censat), voted en cas que s’hagi votat i value on indica el vot. Malgrat pugui semblar que sense aquest últim es pot ocultar el vot, el cert es que el vot només pot ser rastrejable pel creador de la votació i, amb aquest paràmetre o sense, a través de les transaccions. També es disposa d’un array amb totes les proposals, i d’ uns events que permeten disparar avisos al JS de quan una transacció s’ha realitzat.

També trobem un bloc amb funcions. Primer trobem la que ens serveix per obtenir les proposals realitzades. Cal notar que com que aquestes funcions no modifiquen l’estat de la Blockchain (per entendre’ns, només són de lectura) fan servir les paraules clau public view. Per al cas de public és per fer-la accessible des de fora de la Blockchain i des d’altres smart-contract, mentre que view fa referència a que és únicament de lectura. Com que solidity, si més no en les versions estables, intercanviar molta informació a la vegada, és més pràctic primer fer una crida per saber quantes proposals hi ha i després anar-le cridant una a una per obtenir-ne la informació. L’intercanvi d’informació es fa amb tipus bàsics uint=integer, bool, string memory=string unidimensional, address=un string especial de mida definida en format ‘0x58Af4…’ i que permet transmetre en arrays (address[ ]). El fet que no es puguin transmetre arrays d’strings (per transmetre una llista de candidats, per exemple) es degut a que no tolera array multidimensionals, ja que un string ja és un array en sí.

A la funció per afegir proposals es pot veure que és de tipus public, però no és view. Per tant aquesta funció altera la blockchain i tindrà un cost associat. De fet a la mateixa crida de la funció cal afegir paràmetres addicionals per costejar-ne el cost. En aquesta funció es pot veure també l’ús convencional de bucles for, funcions com push per afegir elements a un array, i referenciació amb el punt ‘.’ per referir a atributs d’un struct. També cal notar l’ús de la comanda storage per indicar que un bloc de memoria serà modificat.

Molt similar és el funcionament de la funció per votar, encara que en aquesta podem destacar l’ús dels condicionals de la mateixa manera que es fa servir en tants d’altres llenguatges, en aquest cas per fer les comprovacions oportunes a saber si el vot és duplicat, o d’una I’address no censada o si es vota fora de temps, fent ús de la variable interna now.

Per a la compilació i migració d’un contracte, ens hem servit de l’entorn de simulació Truffle. Per compilar n’hi ha prou amb executar:

$ truffle compile

I per migrar el contracte, havent “aixecat” Ganache prèviament cal executar:

$ truffle migrate --reset

D’aquesta manera el contracte es desplega dins la Blockchain, i a partir d’allà qualsevol que vulgui pot interactuar amb ella.

## Pàgina Web[[edit](/pti/index.php?title=Categor%C3%ADa:Vothereum&veaction=edit&section=8 "Edit section: Pàgina Web") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vothereum&action=edit&section=8 "Edit section: Pàgina Web")]

### Introducció[[edit](/pti/index.php?title=Categor%C3%ADa:Vothereum&veaction=edit&section=9 "Edit section: Introducció") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vothereum&action=edit&section=9 "Edit section: Introducció")]

S’ha creat una pàgina web per que la gent tingui la facilitat de votar o de crear les seves votacions. Desde la pàgina web es poden crear votacions amb una data d’inici i una data final, afegir els candidats i penjar un llistat en el qual hi ha la gent autoritzada a votar. Automàticament es crearan les comptes a la blockchain i aquesta s’enviara per mail al votant amb certa informació sobre la votació.
Per fer la votació desde la pàgina web s’haurà d'introduir el compte enviat al mail i simplement fer click al candidat escollit. La pàgina web és una gran eïna que facilita al votant o al creador de la votació a fer la seves gestions fàcilment, ràpidament i sobretot còmodament.
Tecnologies associades al disseny web
Per desenvolupar la web s’han utilitzat plantilles que involucren CSS, JavaScript, Bootstrap y jQuery. Tots aquests són complements per fer d’un codi Html un codi versàtil, maleable i de fàcil tractament de cara al programador. CSS ofereix la capacitat d’aplicar un format visual que dóna certa uniformitat, per exemple que el tipus de lletra dels paràgrafs sigui igual tot l’entorn. Podem pensar que CSS és una capa per sobre d’Html, ja que amb un sol canvi al CSS afecta a tot el document Html. Així mateix també podem concebre Bootstrap, que no és més que una capa que està per sobre de CSS i a la vegada per sobre de Html. Bootstrap permet gestionar tant l’aparença dels objectes que es mostren com la seva distribució i funcionalitat. Pel que fa a l’aparença crea objectes com a plantilles, per exemple el nostre seleccionador d’hora i dia.

Bootstrap fa servir jQuery que és un complement de JavaScript (a partir d’ara JS). És un sistema d’accés als elements d’un Html per tal de modificar-ne propietats, atributs o valors. En la nostra web hem emprat jQuery tant de manera implícita (en l’ús de Bootstrap) com de manera explícita, per variar el comportament dels elements Html, o bé per recollir dades dels formularis i processar-los en el JS.

### Disseny web[[edit](/pti/index.php?title=Categor%C3%ADa:Vothereum&veaction=edit&section=10 "Edit section: Disseny web") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vothereum&action=edit&section=10 "Edit section: Disseny web")]

Principalment la web l’hem compost d’un html i d’un JS associat, que és el que li dóna tota la funcionalitat. La web està pensada per no fer cap mena d’interacció amb el servidor, tant és així que un cop servida fa la gestió i interacció amb la blockchain de manera íntegra, així com amb el servidor de correu. La web es compon de tres pestanyes, una que és el home i que serveix per “autenticar” introduint-hi l’account que l’usuari té d’Ethereum i el password.

En aquest pas el JS comprova que és una account i password vàlids i permet accedir a les altres dues pestanyes. Cal notar, que els codis Html i JS són modificables un cop estan carregats en el nostre navegador, i que és molt convenient no recolzar la seguretat en el seu comportament. Dit això, convé assenyalar que encara que es modifiqués el JS, la seguretat del nostre sistema no rau en la web sinó en la blockchain, de manera que encara que s’accedís a les altres pestanyes sense haver-se autenticat amb una account, l’operativitat seria supèrflua.

La pestanya Proposals mostra les votacions disponibles per a l’Account amb que s’hagi fet login. Les proposals són visibles per a tots els participants del cens d’aquella votació i pel creador, encara que en aquest últim cas, si no està al cens no podrà votar. En els casos en que no es pot votar s’inhabiliten els botons, ja sigui perquè s’és creador no censat o perquè ja s’hagi votat. Com ja s’ha fet menció abans, el que restringeix votar no és el JS, si no la Blockchain, de manera que si s’alterés el JS per habilitar els botons, es tramitaria la votació tot i que la Blockchain la rebutjaria.

D’altra banda, la pestanya New proposal permet crear noves votacions. Aquesta pestanya conté tots els camps necessaris per crear una votació nova, com ara el nom de la votació (p.ex: Presidencials), dos camps per introduir les dates i hores d’inici i de fi, en els que es pot votar. Per a aquest complement ha calgut afegir una llibreria bootstrap bootstrap-datetimepicker.min.js i el seu corresponent css bootstrap-datetimepicker.css. També un panell per introduir-hi les candidatures, on es van afegint candidats amb el botó Add i es poden sostreure fent-hi clic sobre la llista si és necessari. També es disposa d’un input per a fitxers des d’on es llegirà el fitxer del cens, un fitxer de text que cal que estigui ben formatejat, com per exemple (votant1; e-mail1; password1; votant2…). I finalment uns camps per al correu i password des d’on es vol enviar els correus informatius de la votació.

### Web3 i JS[[edit](/pti/index.php?title=Categor%C3%ADa:Vothereum&veaction=edit&section=11 "Edit section: Web3 i JS") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vothereum&action=edit&section=11 "Edit section: Web3 i JS")]

Web3 és la llibreria que permet a la web, en definitiva al JS, obtenir una interfície per comunicar-se amb la Blockchain. Per això cal crear una instància de web3 per executar totes les comandes relacionades amb la Blockchain. La comunicació amb la Blockchain es fa mitjançant RPC (Remote Procedure Call) i web3 s’encarrega de “convertir” les funcions que usem en format RPC. Tanmateix existeixen diverses versions de web3, de fet ens hem vist forçats a usar la versió 0.2.0 quan la versió beta 1.0.0 ens hauria facilitat moltes tasques com la creació de nous comptes i altres crides útils.

Després cal instanciar el contracte. Per fer-ho és necessari un fitxer creat durant la compilació del contracte, Voting.json, on hi ha la informació relativa a les crides possibles al contracte en un format que es diu ABI. Aquí també es fa servir una llibreria de truffle, que és la que ens ha fet la guitza per usar versions més actuals de web3, ja que fa de capa intermediària entre el JS i web3.

Un aspecte molt important de les funcions de web3, és que són asíncrones. I no és pas d’estranyar, doncs aquestes crides han d’anar fins al node de Blockchain per ser processades. Això comporta que el codi es segueix executant tot i haver fet la crida a aquesta funció. Tanmateix, l’ús de Promises i de Callbacks en faciliten una mica la gestió. A la imatge següent es pot observar l’ús del callback amb l’apèndix .then(function...) que el que fa és executar la funció function només després d’haver acabat la seva pròpia execució. Cal recordar que controlar estrictament aquestes esperes és essencial per a què no hi hagi data race, que no és més que usar dades que encara no s’han actualitzat.

## Integració[[edit](/pti/index.php?title=Categor%C3%ADa:Vothereum&veaction=edit&section=12 "Edit section: Integració") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vothereum&action=edit&section=12 "Edit section: Integració")]

Per a l’smart-contract s’ha fet servir el llenguatge Solidity. Aquest codi es compila i es migra a la blockchain gràcies a Truffle fent servir les comandes de consola abans esmentades. El codi generat migra a la blockchain que simula Ganache a través d’una ip i un port que per defecte està configurat en localhost:7545. Per interactuar amb la blockchain fem servir una web, que la servim o bé amb un servidor que ens aixeca Nodejs o bé amb un servidor Python-Flask en un contenidor Docker, del qual més endavant en donarem més detalls. La web interactua amb la blockchain fent ús de JavaScript, concretament amb la llibreria web3. Ho fa, o bé directament amb crides RPC o bé usant Metamask com a supervisor de les transaccions, que al seu torn es comunica amb la blockchain també amb RPC.

# Tests i simulació[[edit](/pti/index.php?title=Categor%C3%ADa:Vothereum&veaction=edit&section=13 "Edit section: Tests i simulació") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vothereum&action=edit&section=13 "Edit section: Tests i simulació")]

## Proves de funcionament[[edit](/pti/index.php?title=Categor%C3%ADa:Vothereum&veaction=edit&section=14 "Edit section: Proves de funcionament") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vothereum&action=edit&section=14 "Edit section: Proves de funcionament")]

Per poder prova l’aplicació hem aplicat les diferents proves:

Generar diferents tipus de votacions amb diferent número de candidats.
Cambiar el número de votants en el arxiu que s’ha de pujar.
Intentar votar amb comptes que no estan autoritzades.
Intentar accedir a comptes amb passwords erronis.
Intentar votar per segon cop.
Intentar accedir amb comptes inexistents.
Intentar votar fora de termini.
intentar votar abans de termini.

## Limitacions[[edit](/pti/index.php?title=Categor%C3%ADa:Vothereum&veaction=edit&section=15 "Edit section: Limitacions") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vothereum&action=edit&section=15 "Edit section: Limitacions")]

En el nostre projecte existeixen certes limitacions que no hem pogut solucionar. Per començar el nostre sistema només utilitza el servidor de correu de Google per enviar els correus amb la clau privada que l’usuari utilitza per votar, per tant, els usuaris que creen una proposta nova, han de disposar d’un correu de Gmail o crear-se un de nou.També com que Gmail no permet enviar més de 100 emails per dia, podriem dir que això seria una limitació a l’hora de voler fer una votació per milers de persones. Ja que ara per ara no es podria.

Un altre limitació, seria que el qui fa la proposal, podria arribar a saber que ha votat cadascú, ja que com és qui envia els mails pot restrejar a quin votant pertany cada compte. També al tenir totes les comptes(pel mails que ha enviat), abans del que el propi votant votés, podria agafar els comptes i votar en nom d’un altre votant, ja que com hem dit, al enviar ell els mails, té totes les credencials per poder-ho fer.

## Casos d’ús[[edit](/pti/index.php?title=Categor%C3%ADa:Vothereum&veaction=edit&section=16 "Edit section: Casos d’ús") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vothereum&action=edit&section=16 "Edit section: Casos d’ús")]

La nostre aplicació podria servir per fer qualsevol tipus de votació, exceptuan les limitacions anteriors. Per qualsevol votació amb menys de 100 persones es podria fer servir perfectament. També hauríem de tenir present que el qui ha creat la proposal pot arribar a saber què ha votat cadascú, potser això fa que la aplicació no serveixi per un sistema que hagi de ser totalment anònim. Exemples en que l’aplicació pot ser molt útil seria com triar el degà d'una universitat, el president d'una comunitat de veïns, algun acte participatiu d'una entitat municipal, etc...

Un altre exemple que s’ens va passar pel cap, seria per poder demostrar que ha votat cadascú, ja que com hem dit, el qui fa la proposal pot arribar a saber que ha votat cada votant. Per exemple en un sopar de nadal, on normalment s’ha d‘escollir plat uns dies abans, es podria crear una votació amb els plats disponibles pel sopar, on cada convidat podria votar el plat que vol. D’aquesta manera cada votant se li relacionaria un plat, i el dia del sopar, no podria haver equivocació ni dir que ell no havia demanat aquell plat.
Com podem veure els casos d’ús poden ser diversos, i no ens hem de tancar a només que es faci servir l’aplicació per votar persones, ja que com hem exposat pot servir per altres casos.

## Simulació Blockchain[[edit](/pti/index.php?title=Categor%C3%ADa:Vothereum&veaction=edit&section=17 "Edit section: Simulació Blockchain") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vothereum&action=edit&section=17 "Edit section: Simulació Blockchain")]

Per simular la blockchain hem utilitzat la eina truffle i ganache. La diferència és que ganache directament ens “aixeca” una blockchain ja preparada i amb 10 comptes per defecte ja creadas. Truffle això no ens ho facilitava, peró ens ha servit per provar mètodes i fer diferents depuracions de codi.
Ganache és una aplicació amb una interfície gràfica fàcil d’entendre, desde la cual podem comprovar l’estat de les comptes, les transferències fetes, la quantitat de eth(moneda de la blockchain) i fer alguna configuració amb el servidor.
Truffle en canvi no te interfície gràfica i s’ha de fer tot per consola. Al tenir-ho que fer tot per consola potser dificulta més la feina, però tenim moltes més utilitats que en el Ganache, ja que podem, per exemple, crear comptes, probar mètodes, entre d’altres que desde Ganache no es pot fer.

## Dockerització[[edit](/pti/index.php?title=Categor%C3%ADa:Vothereum&veaction=edit&section=18 "Edit section: Dockerització") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vothereum&action=edit&section=18 "Edit section: Dockerització")]

La pàgina web a estat dockeritzada, de tal manera que en un container docker s'aixeca ja automàticament un servidor amb la pàgina web ja funcionan. És una manera molt pràctica de poder probar la pàgina web en qualsevol equip sense tenir que dependre de tenir un servidor aixeca’t i de que la nostra versió php, java… sigui l’adequada.
El nostre container ha estat publicat en el repositori de docker (docker hub) de tal manera que amb les comandes de docker és molt fàcil descargar-lo i muntar la imatge. En qüestió de minuts es pot tenir la web funcionant.

### Python i Flask[[edit](/pti/index.php?title=Categor%C3%ADa:Vothereum&veaction=edit&section=19 "Edit section: Python i Flask") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vothereum&action=edit&section=19 "Edit section: Python i Flask")]

Per simplificar la tasca de Dockerització s’ha partit de la base d’un projecte fet amb python i Flask. Doncs, només ha calgut aplegar tots els fitxers necessaris del lloc web, aquests són tots el fitxers JS, els CSS, les fonts (imatges…), els ABI dels contractes compilats (en realitat es fan servir dos contractes, un és el contracte en sí mateix i l’altre que s’encarrega que no es migri un mateix contracte), el fitxer index.html, i el fitxer python que amb la llibreria Flask s’encarregarà de servir els fitxers. Addicionalment caldrà afegir els fitxers que usarà Docker per generar el contenidor: Per una banda requirements.txt conté els imports que l’accessori pip necessitaria per obtenir la llibreria Flask, i per últim el fitxer Dockerfile que es l’autèntic generador:

Executant la següent comanda des de dins el directori es crea el contenidor:

docker build -t vothereum:latest .

Executant la següent comanda es posa en marxa el contenidor:

docker run -d -p 80:5000 vothereum

# Millores futures[[edit](/pti/index.php?title=Categor%C3%ADa:Vothereum&veaction=edit&section=20 "Edit section: Millores futures") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vothereum&action=edit&section=20 "Edit section: Millores futures")]

## En general[[edit](/pti/index.php?title=Categor%C3%ADa:Vothereum&veaction=edit&section=21 "Edit section: En general") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vothereum&action=edit&section=21 "Edit section: En general")]

Malgrat la cerca exhaustiva que hem fet, no hem pogut trobar la manera de perdre el rastre de les comptes. Que vol dir això? Que l’administrador que crei la votació (proposal), podria saber quin compte correspon a cada votant, i per tant, saber que hauria votat.
Vam trobar informació sobre com perdre el rastre en un exemple publicat a vocdoni, però malgrat la nostre insistencia i el curt termini no hem sapigut aplicar-ho el nostre projecte. Per tant veiem que una de les possibles i grans millores que es poden fer en el projecte seria perdre el rastre total aplicant els coneixements que ens donen a la web de Vocdoni.

Quan es creen els comptes a la blockchain, és necessari fer-lis una transferencia de eth perquè aquestes comptes puguin fer la votació. Ja que fer la votació suposa un cost de eth igual que la transferència.
Hi ha una problema i és que per cada compte que es crea s’ha de fer una transferència i això en suposa un increment de cost. Per tant creiem que un altre de les millores (no sabem si és possible) seria que cridant només una vegada el mètode de la transferencia, pogués fer la transferencia de x eth a totes les comptes creades. Per tant ens supondria un estalvi molt important de eth.

Un altre de les millores seria millorar el sistema d’enviament de la clau per correu, ja que actualment cada usuari que volgués crear una nova proposta s’ha de crear un compte de Gmail, o utilitzar-ne un ja existent, ja que la pàgina web utilitza el servidor de correu de Google com emissor.

Com hem dit anteriorment a les limitacions, només podem fer votacions fins a 100 persones ja que Gmail no permet enviar més mails per dia. Una millora possible seria canviar el codi per posar un servidor de correu que permeti l’enviament de correu massiu per així poder fer votacions més extenses.

## zk-SNARKs[[edit](/pti/index.php?title=Categor%C3%ADa:Vothereum&veaction=edit&section=22 "Edit section: zk-SNARKs") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vothereum&action=edit&section=22 "Edit section: zk-SNARKs")]

Un problema del nostre projecte generat per les característiques d’una blockchain es com simular el procés d’introduir la papereta en la urna i així aconseguir que el vot sigui anònim. Tot i que no ho hem sapigut implementar en el nostre projecte, hem fet una petita cerca sobre una solució que se'ns va proposar. En el 2018, es va introduir el protocol de privacitat zk-SNARKs, acrònim de Zero-Knowledge Succint Non-Interactive Argument of Knowledge, es una forma de criptografía que permet a un usuari validar que es el propietari d’un conjunt de dades sense revelar quines son les dades.
La generació de proves zero-knowledge es basa en un conjunt de paràmetres públics que permeten als usuaris construir i verificar transaccions privades. Aquests paràmetres es construeixen utilitzant numeros aleatoris coneguts com ‘toxic waste’, el problema es que si algú és capaç de descobrir l’aleatorietat que s’utilitza per generar els paràmetres, podria generar falses proves que a l’ull del verificador serien acceptables. Existeixen eines per prevenir aquestes falsificacions, per exemple, Zcash utilitza reunions “multi-party computation” on es permet a diferents parts independents construir de manera conjunta els paràmetres públics , això vol dir que per tal que un usuari infringeixi els paràmetres públics, tots els participants de la reunió han d’estar d’acord.

# Anàlisi econòmic[[edit](/pti/index.php?title=Categor%C3%ADa:Vothereum&veaction=edit&section=23 "Edit section: Anàlisi econòmic") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vothereum&action=edit&section=23 "Edit section: Anàlisi econòmic")]

Parlant desde el punt de vista de com està actualment el valor de les diferents criptomonedes (que seran necessàries per poder crear comptes, transferir i votar), podem dir que per fer votacions generals podria arribar a sortir a comte. Però per fer votacions en empreses o en petits comitès creiem que no.
En votacions generals si suposem que tothom vota per internet, el cost de no imprimir paperetes, personal, transport, gasolina, correus... pensem que podria ser molt més elevat que el que ens supondría compra criptomones i transferir-les.
Obviament no contem el cost de tenir accés a la xarxa (ISP), ja que avui en dia casi tothom té accés tant desde casa com desde el movil. Creiem que no tindria que se cap problema el tema de poder accedir a la xarxa, ja que en un futur imminent tothom tindrà accés a internet.

# Conclusions[[edit](/pti/index.php?title=Categor%C3%ADa:Vothereum&veaction=edit&section=24 "Edit section: Conclusions") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vothereum&action=edit&section=24 "Edit section: Conclusions")]

Una de les primeres conclusions que hem tret d’aquest projecte, és que si en futur poguessim solucionar les millores que hem proposat, podria ser una alternativa molt bona per fer les votacions. No veiem cap disbarat que en un futur tothom pugui votar desde internet, ja que facilitaria molta feina, i creiem que utilitzant la blockchain és una de les millors tecnologies que avui en dia existeixen que no permet ni la modificació ni la pèrdua de dades, ja que és una sistema descentralitzat.
Hi han països que ja han utilitzat aquest sistema i les critiques han estat bones, per això pensem que el nostre projecte pot tenir un bon futur.

Gràcies aquest projecte, hem après bastant sobre blockchain i eines derivades. Això ens ha motivat molt a l’hora de crear el nostre sistema de votacions, ja que tots teniem ganes d’aprendre i saber com funciona realment la blockchain.

## Problemes[[edit](/pti/index.php?title=Categor%C3%ADa:Vothereum&veaction=edit&section=25 "Edit section: Problemes") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vothereum&action=edit&section=25 "Edit section: Problemes")]

A l’hora d’utilitzar noves tecnologies ens ha portat molt de temps la part d'aprendisatge, ja que de moment hi ha poca informació i sobretot molts errors. Però creiem que ens n'hem ensortit prou bé i en el projecte es poden veure els resultats.

Un dels grans problemes que ens hem trobat, és que el mètode de la llibreria web3 que ens permet crear comptes no funcionava. Això va suposar una gran pèrdua de temps, però ens vam ensortir fent servir un altre funció, que per el que voliem fer ja ens servia.
Molts dels mètodes de la llibreria web3 no funcionaven i això ens causava tenir que buscar informació de com poder arreglar aquests problemes.
Com hem tingut que utilitzar eines que no teniem instal·lades ( npm, truffle, ganache…), vam tenir problemes de compatibilitat a l’hora de fer la instal·lació, sobretot amb el npm.

## Reptes aconseguits[[edit](/pti/index.php?title=Categor%C3%ADa:Vothereum&veaction=edit&section=26 "Edit section: Reptes aconseguits") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vothereum&action=edit&section=26 "Edit section: Reptes aconseguits")]

Creiem que hem de fer saber, que un dels majors reptes que ens hem proposat en aquest projecte ha estat treure la utilització del Metamask.
El Metamask és una eina que en principi s’havia d'instal·lar tot votant en el navegador per poder-se autentificar a la blockchain. Era una de les coses que ens tirava enrere per fer les votacions via web, ja que el votant l'últim que vol, és tenir que instalar mes programes i apart aprendre'ls a utilitzar-los.
Entre d’altres reptes aconseguits, creiem adequat puntualitzar el Metamask, ja que al llarg de tot el projecte és una eina més a la que ens hem tingut que adaptat, aprendre com funciona i que ens ha portat bastants mal de caps, però al final hem aconseguit prescindir d’ella, d’aquí que la volguem puntualitzar.
Apart d’això, el Metamask només funcionava correctament amb Firefox, de tal manera, que estavem obligats a fer servir la nostre web desde aquest navegador. Al evitar l'ús d’aquesta eina (Metamask) també hem facilitat que es pugui votar desde qualsevol navegador.

# Bibliografia[[edit](/pti/index.php?title=Categor%C3%ADa:Vothereum&veaction=edit&section=27 "Edit section: Bibliografia") | [edit source](/pti/index.php?title=Categor%C3%ADa:Vothereum&action=edit&section=27 "Edit section: Bibliografia")]

Instal·lació node
<https://github.com/nodesource/distributions/blob/master/README.md#debinstall>

Tutorial
<https://aprendeblockchain.wordpress.com/desarrollo-en-ethereum/desarrollo-con-truffle-i/>

Treball de fi de grau de La Laguna
<https://riull.ull.es/xmlui/bitstream/handle/915/9462/Sistema%20de%20votacion%20electronica%20basado%20en%20blockchain.pdf?sequence=1&isAllowed=y>

Normativa EU
<http://www.eods.eu/library/CoE_Recommentaion%20on%20Legal,%20Operational%20and%20Technical%20Standards%20for%20E-voting_2004_EN.pdf>

Sistema de votació amb truffle (tutorial)
<https://medium.com/agorachain-mag/desarrollo-de-una-dapp-sobre-ethereum-8aee3aa0f3d7>
Informacio sobre Solidity
<https://solidity-es.readthedocs.io/es/latest/>

Afegir comptes a la blockchain
<https://web3js.readthedocs.io/en/1.0/web3-eth-accounts.html>

Dockerització (tutorial de com crear imatges Docker)
<https://docs.docker.com/get-started/>

Possible informació de com perdre el rastre de les votacions
<http://vocdoni.io/>

Informació sobre zk-SNARKS
<https://es.coinnewstelegraph.com/zk-snarks-explained-introduction-to-privacy-protocol/>
<https://z.cash/blog/snark-explain>

Projectes de sistemes de votació utilitzant blockchain
Polys
<https://polys.me>

Voatz
<https://voatz.com/faq.html>

SecureVote
<https://secure.vote>

Vocdoni
<http://vocdoni.io/docs/#/architecture/general>