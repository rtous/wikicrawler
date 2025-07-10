[![](images/800px-Minethetag\_logo.jpg)](/pti/index.php/File:Minethetag_logo.jpg)

Logo del projecte

## Contents

* [1 Introducció](#Introducci.C3.B3)
  + [1.1 ¿Què és MineTheTag?](#.C2.BFQu.C3.A8_.C3.A9s_MineTheTag.3F)
* [2 Objectius tecnològics del projecte](#Objectius_tecnol.C3.B2gics_del_projecte)
* [3 El joc: Configuració i apartat tècnic](#El_joc:_Configuraci.C3.B3_i_apartat_t.C3.A8cnic)
  + [3.1 Captures de pantalla i jugabilitat](#Captures_de_pantalla_i_jugabilitat)
  + [3.2 Configuració del servidor amb Ansible](#Configuraci.C3.B3_del_servidor_amb_Ansible)
  + [3.3 Definició de la base de dades](#Definici.C3.B3_de_la_base_de_dades)
  + [3.4 Decisions preses respecte d’Android](#Decisions_preses_respecte_d.E2.80.99Android)
  + [3.5 Implementació de backend](#Implementaci.C3.B3_de_backend)
  + [3.6 Configuració de docker per al servidor i per al desenvolupament](#Configuraci.C3.B3_de_docker_per_al_servidor_i_per_al_desenvolupament)
* [4 Referències](#Refer.C3.A8ncies)
  + [4.1 GitHub del projecte](#GitHub_del_projecte)
  + [4.2 Referències externes](#Refer.C3.A8ncies_externes)

# Introducció[[edit](/pti/index.php?title=Categor%C3%ADa:MineTheTag&veaction=edit&section=1 "Edit section: Introducció") | [edit source](/pti/index.php?title=Categor%C3%ADa:MineTheTag&action=edit&section=1 "Edit section: Introducció")]

## ¿Què és MineTheTag?[[edit](/pti/index.php?title=Categor%C3%ADa:MineTheTag&veaction=edit&section=2 "Edit section: ¿Què és MineTheTag?") | [edit source](/pti/index.php?title=Categor%C3%ADa:MineTheTag&action=edit&section=2 "Edit section: ¿Què és MineTheTag?")]

El projecte que hem realitzat consisteix en un joc de geolocalització on cada jugador té la missió de defensar punts del mapa -tags NFC- el màxim temps possible, així com reflexa el seu nom MineTheTag (Mina l’etiqueta, en català). Cada jugador haurà de col·locar tags NFC físicament i aquests seran visibles per tothom. Posteriorment, el jugador defensarà aquest tag amb la col·locació de mines, que només ell podrà veure, sobre el mapa virtual. Paral·lelament, tot jugador tindrà la missió també de conquerir els tags d’altres jugadors sense que cap mina li exploti en intentar accedir-hi.

Les mines no existeixen físicament sinó que estan col·locades virtualment al mapa de l’aplicació i geolocalitzades amb GPS. Hi ha un cert nombre de mines que un jugador pot posar al voltant d’un tag i han de respectar una certa distància perquè sinó seria molt fàcil impedir l’accés a l’objectiu.

Quan un jugador trepitgi una mina perdrà la possibilitat de conquerir el tag durant un cert període de temps. Com a conseqüència tampoc li explotarà cap mina més per tal d’evitar desactivar tota la defensa del tag. La mina desapareix del joc però es pinta de color vermell com a succés que ha passat. Altrament, si un jugador aconsegueix accedir a un tag, farà check-in, es validarà al servidor i aquell tag passarà a formar part de la seva defensa.

Hi haurà tags registrats prèviament per a garantir una certa jugabilitat als usuaris, tot i que, si els usuaris ho desitgen, en poden posar més per on vulguin i registrar-los a través d’una opció de l’aplicació amb un nom propi.

# Objectius tecnològics del projecte[[edit](/pti/index.php?title=Categor%C3%ADa:MineTheTag&veaction=edit&section=3 "Edit section: Objectius tecnològics del projecte") | [edit source](/pti/index.php?title=Categor%C3%ADa:MineTheTag&action=edit&section=3 "Edit section: Objectius tecnològics del projecte")]

L’objectiu tecnològic del projecte ha estat aprendre a combinar diferents tecnologies, algunes vistes al laboratori de l’assignatura i aprofundir en altres que ja coneixiem. En aquest sentit, avaluem de forma molt correcte i gratificadora el fet d’haver pogut interaccionar amb noves tecnologies que fins a dia d’avui no havíem pogut tocar en cap altra assignatura. Tot i que en el següent apartat definim quines tecnologies hem utilitzat, cal dir que utilitzar docker per implementar algunes funcionalitats del servidor i també com a entorn de desenvolupament per anar implementant el backend ha estat una experiència molt enriquidora.

De la mateixa manera, hem tingut el primer contacte amb tecnologies com SQLAlchemy, un Object Relational Mapper i toolkit de Python que serveix com a capa d’abstracció per al desenvolupador a fi d’interactuar més còmodament amb la base de dades, també hem après com connectar la aplicacioó Android amb el servidor cosa que no vam poder fer en una assignatura anterior.
Tot i que no és l’objectiu d’aquest apartat definir les tecnologies utilitzades sí que com a grup donem per complit l’objectiu d’aprendre noves tecnologies i posar-les en pràctica de forma autònoma. Malgrat tot, considerem que la corba d’aprenentatge amb algunes d’elles ha estat alta i això ha fet que algunes tasques s’hagin vist endarrerides, tal i com descriurem en l’apartat oportú.

A més, per tal d’encarar el nostre projecte hem tingut en compte productes que ja estan al mercat i que ens han servit de referència a l’hora de pensar la jugabilitat de MineTheTag. En aquest sentit, alguns jocs que ja estan implementats i que parteixen de la mateixa base serien, per exemple, els de Niantic, com Ingress o Pokémon GO. Estan basats en geolocalització per interaccionar amb els punts virtuals en un mapa de realitat augmentada.
També en els jocs per smartphones, trobem Skylanders que usa tags NFC per llegir els personatges i poder entrar al joc.
En el camp d’OpenStreetMap, trobem un joc MapOftheDead, el qual, has d’ajudar a identificar llocs en un mapa d’OpenStreetMap per aportar recursos per sobreviure a l’apocalipsi zombie.

# El joc: Configuració i apartat tècnic[[edit](/pti/index.php?title=Categor%C3%ADa:MineTheTag&veaction=edit&section=4 "Edit section: El joc: Configuració i apartat tècnic") | [edit source](/pti/index.php?title=Categor%C3%ADa:MineTheTag&action=edit&section=4 "Edit section: El joc: Configuració i apartat tècnic")]

## Captures de pantalla i jugabilitat[[edit](/pti/index.php?title=Categor%C3%ADa:MineTheTag&veaction=edit&section=5 "Edit section: Captures de pantalla i jugabilitat") | [edit source](/pti/index.php?title=Categor%C3%ADa:MineTheTag&action=edit&section=5 "Edit section: Captures de pantalla i jugabilitat")]

[![](images/200px-Mttg\_cap\_1.jpg)](/pti/index.php/File:Mttg_cap_1.jpg)

Login

[![](images/200px-Mttg\_cap\_2.jpg)](/pti/index.php/File:Mttg_cap_2.jpg)

Registre

[![](images/200px-Mttg\_cap\_3.jpg)](/pti/index.php/File:Mttg_cap_3.jpg)

Mapa

[![](images/200px-Mttg\_cap\_4.jpg)](/pti/index.php/File:Mttg_cap_4.jpg)

Navigation drawer

## Configuració del servidor amb Ansible[[edit](/pti/index.php?title=Categor%C3%ADa:MineTheTag&veaction=edit&section=6 "Edit section: Configuració del servidor amb Ansible") | [edit source](/pti/index.php?title=Categor%C3%ADa:MineTheTag&action=edit&section=6 "Edit section: Configuració del servidor amb Ansible")]

Hem allotjat el nostre servidor amb el serveis de Cloud Computing de Amazon: Amazon EC2. Hem decidit triar aquest proveïdor doncs un dels integrants del grup disposava de crèdit gratuït aconseguit mitjançant una Hackathon. A més a més, ens interesa aprendre el servei de Cloud d’Amazon, doncs aquest té un important grau d’implantació en el mercat.

Per a sol·licitar el servidor, i realitzar la configuració del registre DNS, hem utilitzat Ansible, amb l’objectiu de poder disposar d’una solució que ens permeti disposar de màquines virtuals al núvol sense excessiva intervenció humana, això ens facilitaria la vida per a escalar de forma horitzontal (és a dir, disposar de més instàncies que suportin una càrrega de forma major, distribuint la feina).

Al codi que es mostra a continuació podem veure l’script d’Ansible que ens permet aixecar una única instància d’Amazon, i fer que el domini minethetag.cf apunti a la adreça IP assignada a aquesta (usant la API del nostre proveïdor de DNS: he.net)

```
 # This playbook needs the package python2-boto
 ---
 - hosts: localhost
 connection: local
 become: False
 gather_facts: False

 vars_files:
   - "vars.yml" ← Aquí tenim les claus d'accés a EC2 mitjançant API registrades. Juntament amb altres variables.

 environment:
   AWS_ACCESS_KEY: "Template:Aws access key"
   AWS_SECRET_KEY: "Template:Aws secret key"

 tasks:
   - name: Provision a instance
     ec2:
        key_name: "PTI_KeyPair"
        # group: test
        region: "Template:Region"
        instance_type: "t2.micro"
        image: "Template:Ami id"
        wait: true
        exact_count: 1
        count_tag:
           Name: MineTheTag
        instance_tags:
           Name: MineTheTag
     register: ec2

   - name: Add all instance public IPs to host group
     add_host: hostname=Template:Item.public ip groups=ec2hosts
     with_items: "Template:Ec2.instances"

   - name: Update dns record
     uri:
       url: https://dyn.dns.he.net/nic/update
       method: POST
       body: "hostname=Template:Domain&password=Template:He dns password&myip=Template:Item.public ip"
       body_format: raw
       return_content: yes

     with_items: "Template:Ec2.instances"




```

Pel que fa a Docker, l’hem instal·lat usant un script de Ansible Galaxy creat per l’usuari angstwad. Podeu trobar-lo a GitHub o el repositori de Ansible Galaxy

També hem usat Ansible per tal de pujar les noves versions de codi al servidor, i generar la imatge de Docker corresponent, així com aixecar els contenidors de Docker ( dividit en dues fases per a millor seguretat i flexibilitat en el cas de que tinguessim diverses màquines, i.e: pujem la nova versió del codi a tots els servidors, però no l’apliquem a tots fins que s’ha provat a un entorn de prova ).

Per la configuració de SSL amb Letsencrypt i Nginx hem optat per configuració manual, doncs es aplicar una configuració específica de Nginx, i usar l’eina de LetsEncrypt per a generar certificats, que ja s’encarrega d’actualitzar-los automàticament quan aquests estan a punt de caducar.

## Definició de la base de dades[[edit](/pti/index.php?title=Categor%C3%ADa:MineTheTag&veaction=edit&section=7 "Edit section: Definició de la base de dades") | [edit source](/pti/index.php?title=Categor%C3%ADa:MineTheTag&action=edit&section=7 "Edit section: Definició de la base de dades")]

Com hem dit, hem definit la base de dades dins el fitxer api.py juntament amb les funcions d’API per a la interacció amb el servidor. D’aquesta manera tenim tres taules: User, Mine i Tag.

```
   class User(db.Model):
       __tablename__ = 'users'
       id = db.Column(db.Integer, primary_key=True)
       name = db.Column(db.String(80),unique=True)
       password = db.Column(db.String(120))
       blocked = db.Column(db.DateTime, default=datetime.now())

```

```
   class Mine(db.Model):
       __tablename__ = 'mine'
       id = db.Column(db.Integer, primary_key=True)
       posX = db.Column(db.Float)
       posY = db.Column(db.Float)
       user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
       user = db.relationship('User', backref=db.backref('mines', lazy='dynamic'))

```

```
   class Tag(db.Model):
        __tablename__ = 'tag'
        id = db.Column(db.Integer, primary_key=True)
        tag_id = db.Column(db.BigInteger, unique=True, nullable=False)
        posX = db.Column(db.Float)
        posY = db.Column(db.Float)
        user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
        user = db.relationship('User', backref=db.backref('tags', lazy='dynamic'))

```

Aquestes classes representen les tres taules que es creen a la base de dades el primer cop que s’executa el fitxer de Python. Són només una part, ja que cada classe té internament altres funcions auxiliars. Com podem observar, doncs, hem simplificat molt el procés per als usuaris, ja que només s’identifiquen amb una id, un nom i un password. Podem veure que a més hi ha un atribut anomenat blocked de tipus DateTime, que ens serveix per bloquejar l’usuari fins a un temps determinat quan li explota una mina.

Una mina està definida per un id únic, unes coordenades i una foreign key que la relaciona amb un usuari. Això és així per identificar cada mina i poder fer que les mines que cada propi usuari posa al mapa no li exploten i no pugi veure les mines dels altres usuaris (a nivell de jugabilitat no tindria sentit). Finalment tenim el tag NFC, molt semblant en quant a definició a la mina, però en aquest cas tenim també un atribut tag\_id que és el que es rep des de l’aplicació Android quan llegeix un tag.

En l’apartat de backend explicarem una mica millor com s’ha implementat tot amb Flask, Python i l’autenticació.

## Decisions preses respecte d’Android[[edit](/pti/index.php?title=Categor%C3%ADa:MineTheTag&veaction=edit&section=8 "Edit section: Decisions preses respecte d’Android") | [edit source](/pti/index.php?title=Categor%C3%ADa:MineTheTag&action=edit&section=8 "Edit section: Decisions preses respecte d’Android")]

S’ha decidit fer una aplicació molt user-friendly ja que aporta molta facilitat d’ús per als jugadors que la faran servir majoritàriament en entorns oberts.

Degut a certes dificultats trobades per implementar algunes funcionalitats hem decidit utilitzar llibreries externes que ens han facilitat molt el treball.
Per agafar la localització actual de l’usuari hem utilitzat la llibreria SmartLocation en lloc de la solució oficial proveïda per Google (la qual per motius desconeguts no funcionava, segurament ha quedat antiquada).
Per connectar amb el servidor per fer crides a la API s’ha utilitzat Volley que és una llibreria d'HTTP que fa que el networking per a aplicacions Android sigui més fàcil i el més important, més ràpid.

També cal remarcar que molts tutorials a la web per ja no funcionen per que les noves versions d’Android ja no les suporten, cosa que ha portat una dificultat extra al projecte ja que hem tingut que fer moltes proves abans d’arribar a la solució implementada.

## Implementació de backend[[edit](/pti/index.php?title=Categor%C3%ADa:MineTheTag&veaction=edit&section=9 "Edit section: Implementació de backend") | [edit source](/pti/index.php?title=Categor%C3%ADa:MineTheTag&action=edit&section=9 "Edit section: Implementació de backend")]

Com s’ha dit en l’apartat anterior, el backend, és a dir, la implementació de totes les funcionalitats per a la interacció amb el servidor i la gestió de la base de dades ho hem dut a terme amb Flask, un microframework per a Python. Flask ens ha facilitat molt la feina. En aquest apartat, farem especial menció a l’autenticació dels usuaris i als token, a les contrasenyes hashejades amb salt i a les principals funcions implementades.

L’autentificació dels usuaris l’hem fet mitjançant la llibreria Httpauth de Flask. Amb aquesta llibreria hem hagut de sobreescriure alguns mètodes, com per exemple, verify\_password a través del qual implementem la comprovació del password de l’usuari.

Aquestes línies de codi ens serveixen per exemplificar com implementem l’autentificació d’usuari. En aquestes línies també hi veiem les crides a Serializer, SignatureExpired i BadSignature. Tot això forma part del paquet itsDangerous, usat per implementar els token. La gràcia d’aquesta llibreria és que un cop implementada només cal usar el decorador @auth.login\_required que implica que la funció que ve a continuació requereix autentificació per a poder-se cridar.

Així mateix, utilitzem la llibreria passlib per fer hash dels password, de manera que a la base de dades ja no hem de guardar en cap moment les claus en clar.

El hash es fa a partir d’una clau secreta. La mateixa llibreria li aplica un salt per tal d’evitar passar la llista de hash per diccionaris en cas de vulneració del servidor.

Gràcies a aquestes llibreries hem pogut implementar les principals funcionalitats de backend com per exemple la creació d’un nou usuari, la inserció de mines i tags, l’explosió de les mines, saber si un usuari està dins el rang d’explosió d’una mina, etc.

## Configuració de docker per al servidor i per al desenvolupament[[edit](/pti/index.php?title=Categor%C3%ADa:MineTheTag&veaction=edit&section=10 "Edit section: Configuració de docker per al servidor i per al desenvolupament") | [edit source](/pti/index.php?title=Categor%C3%ADa:MineTheTag&action=edit&section=10 "Edit section: Configuració de docker per al servidor i per al desenvolupament")]

Per a l’ús de Docker al nostre entorn, tant de desenvolupament, com de producció, hem utilitzat el programari Docker-Compose per a definir conjunts de contenidors, i com aquests estan enllaçats entre si.

Tenim dues configuracions de Docker-Compose, una de producció, on el codi de l’aplicació està contingut a la imatge, i l’altre de desenvolupament, on el codi es troba a un directori fora del contenidor, però enllaçat, el que permet realitzar canvis al codi de backend, i fer proves de forma ràpida. A l’entorn de desenvolupament tampoc tenim ngnix ni SSL, doncs no és estricament necessari.

Per a la imatge del contenidor de la base de dades PostgreSQL, hem creat una configuració basada en la imatge oficial: definim el català com a Locale de la imatge, i creem una base de dades i un usuari associat per a MineTheTag. La definició de la imatge la podeu trobar al GitHub del projecte

A continuació podem veure com la definició d’imatges de Docker pot ser molt senzilla en cas de que la comunitat darrera de la imatge en que ens basem ho hagi posat fàcil, per exemple mitjançant clàusules On Build als seus DockerFiles.

```
   FROM python:2-onbuild
   CMD [ "python", "api.py" ]


```

Amb aquestes dues línies, tenim definida la imatge de Docker del nostre codi de Backend, ens basem en una imatge de Python que copia el codi de la carpeta on estigui el DockerFile, instal·la amb PIP els mòduls de Python indicats al fitxer requirements.txt del mateix directori, i especifica que s’ha de córrer el fitxer de Python indicat a la segona línia.

Per a depuració en l’entorn Docker hem usat diferents mètodes:

Si volíem depurar l’aplicació Python de Backend, ens connectem directament al procés que corre el contenidor:

```
   $ docker container attach minethetag_web_1


```

Per a examinar els registres de la base de dades, executem un intèrpret de bash al contenidor de postgres, passem a superusuari de postgres i ens connectem a la base de dades de MineTheTag:

```
   $ docker exec -it minethetag_db_1 bash
   root@ec51dbaaa231:/# su postgres
   $ psql -d mttg
   psql (9.6.2)
   Type "help" for help.
   mttg=# select * from users where id=1;
    id | name | password|blocked           
   ----+------+-----------------------------------------+----------------------------
   1|test| $6$rounds=656000$ic10D72/fsbAxTGY$V8.7307YKr3oK/2Tgb6M.QMjmy/q2p3.ElbvnFOY0BxL4YxHCI2o7Z6A4brtZ/QxZdBX2q5NuKxPtFv/z7NpZ/ | 
   2017-05-21 11:54:36.884878
   (1 row)


```

Per a més detalls de la implementació, podeu consultar el codi.

# Referències[[edit](/pti/index.php?title=Categor%C3%ADa:MineTheTag&veaction=edit&section=11 "Edit section: Referències") | [edit source](/pti/index.php?title=Categor%C3%ADa:MineTheTag&action=edit&section=11 "Edit section: Referències")]

## GitHub del projecte[[edit](/pti/index.php?title=Categor%C3%ADa:MineTheTag&veaction=edit&section=12 "Edit section: GitHub del projecte") | [edit source](/pti/index.php?title=Categor%C3%ADa:MineTheTag&action=edit&section=12 "Edit section: GitHub del projecte")]

En el [GitHub de MineTheTag](https://github.com/MineTheTag) podreu trobar tot el codi que hem utilitzat

## Referències externes[[edit](/pti/index.php?title=Categor%C3%ADa:MineTheTag&veaction=edit&section=13 "Edit section: Referències externes") | [edit source](/pti/index.php?title=Categor%C3%ADa:MineTheTag&action=edit&section=13 "Edit section: Referències externes")]

* [Documentació d’Apache](http://httpd.apache.org/docs/)
* [Guia d’NGINX](https://www.nginx.com/resources/admin-guide/)
* [Docs d’Android](https://developer.android.com/index.html)
* [Open Containers](https://www.opencontainers.org/community)
* [NFC per Android](https://developer.android.com/guide/topics/connectivity/nfc/index.html)
* [API OpenStreetMap](https://wiki.openstreetmap.org/wiki/API)
* [Docker](https://docs.docker.com/)
* [SQLite amb Android](https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase.html)
* [Gantt](http://www.ganttproject.biz)
* [Flask](http://flask.pocoo.org/docs/0.12/)