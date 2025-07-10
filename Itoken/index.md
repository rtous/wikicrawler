## Contents

* [1 Introducció](#Introducci.C3.B3)
  + [1.1 ¿Què és IToken?](#.C2.BFQu.C3.A8_.C3.A9s_IToken.3F)
* [2 Infraestructura](#Infraestructura)
  + [2.1 Blockchain](#Blockchain)
  + [2.2 Python](#Python)
  + [2.3 MongoDB](#MongoDB)
  + [2.4 Flutter](#Flutter)
* [3 Funcionament](#Funcionament)
* [4 Conclusions](#Conclusions)
  + [4.1 Objectius assolits](#Objectius_assolits)
  + [4.2 Problemes](#Problemes)

# Introducció[[edit](/pti/index.php?title=Categor%C3%ADa:Itoken&veaction=edit&section=1 "Edit section: Introducció") | [edit source](/pti/index.php?title=Categor%C3%ADa:Itoken&action=edit&section=1 "Edit section: Introducció")]

## ¿Què és IToken?[[edit](/pti/index.php?title=Categor%C3%ADa:Itoken&veaction=edit&section=2 "Edit section: ¿Què és IToken?") | [edit source](/pti/index.php?title=Categor%C3%ADa:Itoken&action=edit&section=2 "Edit section: ¿Què és IToken?")]

La idea de IToken va néixer de la idea de fer una plataforma de trading de criptomonedes que afegís un camp de seguretat al utilitzar la tecnologia Blockchain. En un futur tampoc molt llunyà els mètodes de pagament estan destinats a canviar i formes de monedes com els diners en metàl·lic desapareixeran. En aquest futur formes de pagament com pot ser utilitzant criptomonedes augmentaran i serà necessari tenir aplicacions per poder fer les transaccions pertinents.

IToken permet fer transaccions entre els usuaris de l'aplicació de manera segura. L'aplicació es basa en la creació d'ofertes públiques que crea un usuari i els altres poden acceptar si els hi agrada.

# Infraestructura[[edit](/pti/index.php?title=Categor%C3%ADa:Itoken&veaction=edit&section=3 "Edit section: Infraestructura") | [edit source](/pti/index.php?title=Categor%C3%ADa:Itoken&action=edit&section=3 "Edit section: Infraestructura")]

[![](images/800px-Diagrama\_Tecnologies.png)](/pti/index.php/File:Diagrama_Tecnologies.png)

Esquema de les tecnologies.

El nostre projecte està compòs bàsicament per tres parts i una quarta que és el Docker que ho engloba tot i és el què el permet que tota l'estructura es posi en moviment.

### Blockchain[[edit](/pti/index.php?title=Categor%C3%ADa:Itoken&veaction=edit&section=4 "Edit section: Blockchain") | [edit source](/pti/index.php?title=Categor%C3%ADa:Itoken&action=edit&section=4 "Edit section: Blockchain")]

Utilitzarem la blockchain Ethereum. Per tal de poder-la fer servir definirem els smart contracts. Aquests contractes, escrits en el llenguatge Solidity, són els que ens defineixen les diferents funcions que la blockchain podrà fer. En el nostre cas els farem servir per definir quatre tokens diferents y les seves funcions per tal de que els podem enviar i rebre i saber-ne el seu total d’una cartera d’un usuari. Utilitzarem el simulador d’una blockchain anomenat Ganache que és a on migren els nostres contractes. Ganache és una eina molt útil per tal de provar els nostres smart contracts. Ens dona per defecte 10 comptes amb el seu identificador i les seves claus privades per tal de poder-les linkar amb l’aplicació. Per escriure els nostres contractes farem servir el framework Truffle. Truffle té varies comandes que et permet crear un projecte de forma ràpida i fàcil. També té comandes per poder compilar els contractes i fer-ne el deploy al nostre blockchain Ganache.

Per la part del backend farem servir Python amb mongoDB.

### Python[[edit](/pti/index.php?title=Categor%C3%ADa:Itoken&veaction=edit&section=5 "Edit section: Python") | [edit source](/pti/index.php?title=Categor%C3%ADa:Itoken&action=edit&section=5 "Edit section: Python")]

Hem creat un servidor web principalment amb el mòdul flask que bàsicament el què ens permet és servir fitxers. D’aquesta manera creem una API que conté varis endpoints. Aquests endpoints contenen rutes per on es passen les nostres funcions. D’aquesta manera quan el front-end vol per exemple crear un usuari crida aquest endpoint amb uns paràmetres i el crea.

Les funcionalitats principals dels nostres endpoints són:
Registrar usuaris.
Logejar usuaris.
Borrar usuaris.
Ficar cokies per poder iniciar la sessió.
Crear ofertes.
Esborrar ofertes.
Bloquejar ofertes.
Desbloquejar ofertes.
Filtrar el contingut de les ofertes.
Filtrar el contingut de les ofertes filtrades.

Apart hem creat un altre servidor per temes d’espai on està hostejat el front-end de la web app que rep les peticions del fitxer HTML i Javascript i serveix els abis dels tokens. El front end fa una petició AJAX al servidor, després treballa amb els contractes dels tokens de manera local i així pots operar amb ells. Apart també fa com de “pasarela” per temes de logistica entre el front-end i el primer servidor.

### MongoDB[[edit](/pti/index.php?title=Categor%C3%ADa:Itoken&veaction=edit&section=6 "Edit section: MongoDB") | [edit source](/pti/index.php?title=Categor%C3%ADa:Itoken&action=edit&section=6 "Edit section: MongoDB")]

És la base de dades no relacional que hem fet servir. Es guarden les dades en documents de format JSON. Nosaltres hi tenim 3 bases de dades:
- Wallets: On es guarda el compte i la private key.
- Usuaris: Té el nom d’usuari, la seva contrasenya, quina account té assignada i la seva api key.
- I una d’ofertes públiques: On hi tenim el nom de qui ha creat l’oferta, quin token ven, quina és la quantitat, quin token compra, quina n’és la quantitat i un camp que ens indica i l’oferta està bloquejada.

### Flutter[[edit](/pti/index.php?title=Categor%C3%ADa:Itoken&veaction=edit&section=7 "Edit section: Flutter") | [edit source](/pti/index.php?title=Categor%C3%ADa:Itoken&action=edit&section=7 "Edit section: Flutter")]

La hem fet amb el framework Flutter. Flutter utilitza el llenguatge Dart per programar les seves aplicacions. Pot programar mobile apps tan per iOS com per Android.

Per connectar-se amb la blockchain ha fet servir la llibreria Web3Dart.

# Funcionament[[edit](/pti/index.php?title=Categor%C3%ADa:Itoken&veaction=edit&section=8 "Edit section: Funcionament") | [edit source](/pti/index.php?title=Categor%C3%ADa:Itoken&action=edit&section=8 "Edit section: Funcionament")]

[![](images/800px-Diagrama\_Funcionament\_Operaci%C3%B3\_Compraventa.png)](/pti/index.php/File:Diagrama_Funcionament_Operaci%C3%B3_Compraventa.png)

Esquema de les tecnologies.

# Conclusions[[edit](/pti/index.php?title=Categor%C3%ADa:Itoken&veaction=edit&section=9 "Edit section: Conclusions") | [edit source](/pti/index.php?title=Categor%C3%ADa:Itoken&action=edit&section=9 "Edit section: Conclusions")]

### Objectius assolits[[edit](/pti/index.php?title=Categor%C3%ADa:Itoken&veaction=edit&section=10 "Edit section: Objectius assolits") | [edit source](/pti/index.php?title=Categor%C3%ADa:Itoken&action=edit&section=10 "Edit section: Objectius assolits")]

Després de fer tot el projecte creiem que, tot i les millores que podem fer i dificultats que hem tingut , hem assolit els objectius que ens havíem proposat al començament del treball.

Un dels objectius dels que estem més orgullosos és haber entès com funcionen les tecnologies que hem usat pel nostre projecte. Quan vam començar tots vam tenir de fer un gran esforç per entendre les tecnologies i ara podem dir que sabem com funcionen i que la nostra aplicació ho demostra.

Un altre objectiu assolit ha sigut saber quan canviar d’idea i agafar un altre camí que fos més viable. Això ens va passar quan després de veure com funcionava la blockchain ens em vam adonar de que tal com havíem plantejat el projecte al començament era inviable i que havíem de fer un canvi. Vam trobar una solució i vam decidir tirar per aquell camí i ens ha acabat funcionant. En algunes ocasions si que no hem pogut variar l’opció com hem explicat anteriorment amb el Web3.Dart i no hi ha hagut més remei de fer el millor que hem pogut amb el que teniem.

Segurament un dels objectius més importants és tenir una aplicació funcional que es pugui fer servir. Tot i que la nostra mobile app feta en Flutter ens pot millorar la web app feta en Javascript funciona perfectament i té diferents funcionalitats implementades. A part creiem que té un disseny bastant ben acabat i és molt fàcil de fer servir. Tot i la seva sencilleza té un grau de complexitat en diferents apartats més tècnics com quan es crea un usuari nou que s’envia un correu amb la private key del seu compte del Ganache per poder-la ficar en el Metamask. Creiem que compleixen els objectius que ens haviem proposat. Una, la app mobile, per què demostra que hem assolit un coneixement de Flutter bastant elevat, suficient per poder fer una app que tingui diferents funcionalitats i per una altra banda, la web app, que demostra com seria un disseny final de la nostra aplicació si mai la volguéssim portar a mercat.

### Problemes[[edit](/pti/index.php?title=Categor%C3%ADa:Itoken&veaction=edit&section=11 "Edit section: Problemes") | [edit source](/pti/index.php?title=Categor%C3%ADa:Itoken&action=edit&section=11 "Edit section: Problemes")]

Al llarg d’aquest camí ens hem anat trobant diversos obstacles, alguns més difícils i d’altres no tant, que ens han ajudat a aprendre sobre aquestes noves tecnologies que hem utilitzat.

Un dels primers obstacles que ens vam trobar va ser entendre la tecnología Blockchain. En el nostre projecte utilitzem la blockchain Ethereum per poder fer les transaccions de manera segura. El problema va ser que cap dels quatre integrants del grup havía utilitzat mai aquesta tecnologia i per tant vam tenir de invertir una bona part del temps de les primeres setmanes del projecte a buscar informació sobre què era exactament una blockchain i com funcionava. La documentació sobre la blockchain no és molt clara i has de buscar en diferents fonts per trobar la informació que nosaltres necessitàvem. Ens va ajudar bastant veure les tecnologies que havien fet servir projectes anteriors perquè d’aquesta manera vam poder veure quines utilitzariem nosaltres per connectar tots els diferents components del nostre projecte.

Connectar tots els components va ser una altre dels grans problemes que vam tenir al començament. No enteniem ben bé quin rol jugava la blockchain en la nostra aplicació i no sabíem ben bé com s’havia de comunicar. Com ja he dit això es va resoldre després de fer les recerques corresponents però tot i així ens va prendre una bona part del temps de les primeres setmanes.

Un altre problema important que ens vam trobar és amb el Flutter. Aquest framework és molt nou i només porta un any en producció i per tant hi ha funcionalitats que necessitàvem que encara no estaven disponibles o no funcionaven del tot bé. En concret sobretot la llibreria que utilitzavem per connectar-nos amb la blockchain que era la Web3.Dart. Aquesta llibreria va ser bastant difícil d’entendre i ens va donar molt problemes que ens va fer pedre molt de temps quan la vam voler fer servir. A més era completament necessària si voliem comunicar el front end amb la blockchain.

La part interna de la blockchain també ens va donar dificultats a l’hora de fer la transacció en sí. Com hem explicat abans hi havia un problema a l’hora de fer la transacció i vam tenir de dissenyar aquest intermediari anomenat Escrow per solucionar-ho. Vam tenir de pensar bastant en aquest disseny però la solució demostra que després de totes les hores dedicades a entendre com funciona una blockchain ens han servir per poder saber què havíem de dissenyar per poder resoldre aquest problema.

Hi ja com a última dificultat està el fet de la situació actual amb la pandèmia mundial. El fet de no poder-nos reunir com ens hauria agradat ha fet més complicada la comunicació interna del grup ja que creiem que la comunicació és molt més fluida si es poden fer les reunions cara a cara.