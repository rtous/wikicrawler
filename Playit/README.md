## Contents

* [1 PlayIt](#PlayIt)
  + [1.1 Resum](#Resum)
  + [1.2 Parts del projecte](#Parts_del_projecte)
    - [1.2.1 Base de dades](#Base_de_dades)
    - [1.2.2 Web](#Web)
    - [1.2.3 Aplicació](#Aplicaci.C3.B3)
  + [1.3 Valoració econòmica](#Valoraci.C3.B3_econ.C3.B2mica)
    - [1.3.1 Costos d'implementació](#Costos_d.27implementaci.C3.B3)
    - [1.3.2 Costos d'implantació](#Costos_d.27implantaci.C3.B3)
  + [1.4 Desenvolupament futur](#Desenvolupament_futur)

# PlayIt[[edit](/pti/index.php?title=Categor%C3%ADa:Playit&veaction=edit&section=1 "Edit section: PlayIt") | [edit source](/pti/index.php?title=Categor%C3%ADa:Playit&action=edit&section=1 "Edit section: PlayIt")]

[![Logo playit.png](images/200px-Logo\_playit.png)](/pti/index.php/File:Logo_playit.png)

## Resum[[edit](/pti/index.php?title=Categor%C3%ADa:Playit&veaction=edit&section=2 "Edit section: Resum") | [edit source](/pti/index.php?title=Categor%C3%ADa:Playit&action=edit&section=2 "Edit section: Resum")]

La idea d’aquest projecte sorgeix de la dificultat a l’hora de demanar una cançó al DJ en una discoteca, i conseqüentment la poca incidència que té l’opinió del públic en la decisió de la música que sona. El que volem aconseguir, és que les discoteques que decideixin utilitzar el nostre producte, crein una relació més directa entre el DJ i el públic de la sala, millorant així l’experiència dels usuaris.

Això ho volem aconseguir oferint al públic la possibilitat de votar per les cançons que desitgen escoltar, des del seu mòbil. La llista de cançons per les que es poden votar la confecciona el DJ, donant la possibilitat als usuaris de decidir sobre un conjunt de cançons, seleccionat prèviament a criteri del DJ.

Doncs, hem implementat una aplicació Android des de la qual els usuaris es validen a la discoteca mitjançant la tecnologia NFC, i posteriorment poden contribuir a l’elecció de cançons.

Com a suport per al DJ i monitoratge de vots, hem creat una web des d’on el DJ pot veure la sessió activa i els vots per les cançons en temps real. És a la web també, on el DJ defineix la llista de cançons que oferirà en una sessió determinada.

Per a la gestió i administració del sistema també s’utilitza la web, oferint tres perfils diferents: usuari, DJ i administrador. Aquest últim és el responsable de crear les sessions. Els administradors poden proposar als DJs, realitzar sessions en una sala i data determinats. El DJ pot rebutjar, o acceptar la sessió definint una llista.

## Parts del projecte[[edit](/pti/index.php?title=Categor%C3%ADa:Playit&veaction=edit&section=3 "Edit section: Parts del projecte") | [edit source](/pti/index.php?title=Categor%C3%ADa:Playit&action=edit&section=3 "Edit section: Parts del projecte")]

### Base de dades[[edit](/pti/index.php?title=Categor%C3%ADa:Playit&veaction=edit&section=4 "Edit section: Base de dades") | [edit source](/pti/index.php?title=Categor%C3%ADa:Playit&action=edit&section=4 "Edit section: Base de dades")]

La base de dades que utilitzem és MySQL, ja que és el sistema gestor que hem utilitzat normalment. Doncs, és amb el quin ens sentim més còmodes treballant i satisfà les necessitats que requereixen la web i l’aplicació creades.

Cal dir que les consultes realitzades des de la web no han estat directament programades amb SQL, ja que Laravel ofereix una nomenclatura pròpia i més simple per a realitzar consultes sobre elements d’una base de dades.

Per a poder proporcionar els serveis necessaris, la base de dades conté les taules especificades en el següent diagrama, amb les seves respectives relacions.

[![Untitled (3).png](images/500px-Untitled\_%283%29.png)](/pti/index.php/File:Untitled_(3).png)

Els serveis que ofereix la base de dades són els següents:

* Registre d’usuaris.
* Registre de sales.
* Registre de llistes.
* Registre de cançons.
* Registre de sessions.
* Registre de vots per sessió.
* Registre de tags NFC.
* Registre de cançons per sessió.

### Web[[edit](/pti/index.php?title=Categor%C3%ADa:Playit&veaction=edit&section=5 "Edit section: Web") | [edit source](/pti/index.php?title=Categor%C3%ADa:Playit&action=edit&section=5 "Edit section: Web")]

El servidor ofereix connexió HTTP i HTTPS. Actualment utilitza HTTPS amb un certificat propi, no validat. La configuració i gestió d’aquestes connexions l’hem dut a terme mitjançant Nginx. Primerament vam configurar HTTP, però posteriorment també HTTPS.

Per a la implementació de la web, hem utilitzat una tecnologia innovadora anomenada Laravel 5. Es basa en el llenguatge php i en l'encapsulació de codi mitjançant paquets de funcionalitats.

L’IDE que hem fet servir per programar els codis dels fitxers és PhpStorm, en el qual és fàcil d’integrar el repositori de GitHub, on hem establert el control de versions del projecte referent a la pàgina web.

Un exemple de la vista de la web d’un DJ és la que podem veure a continuació.

[![Captura de pantalla 2015-05-27 a la(s) 21.47.46.png](images/600px-Captura\_de\_pantalla\_2015-05-27\_a\_la%28s%29\_21.47.46.png)](/pti/index.php/File:Captura_de_pantalla_2015-05-27_a_la(s)_21.47.46.png)

### Aplicació[[edit](/pti/index.php?title=Categor%C3%ADa:Playit&veaction=edit&section=6 "Edit section: Aplicació") | [edit source](/pti/index.php?title=Categor%C3%ADa:Playit&action=edit&section=6 "Edit section: Aplicació")]

Per fer l’aplicació hem utilitzat “Android Studio” que es un software dissenyat expressament per fer aplicacions Android i que conté un munt de llibreries que ens han ajudat en la implementació de les diferents funcions que necessitem. També facilita treballar amb els SDK d’Android.

El codi utilitzat per a programar les funcionalitats de l’aplicació ha estat Java. Els fitxers de configuració i d’estil en aquest cas són XML. La combinació d’aquest dos és el que s’utilitza per a la creació d’aplicacions d’aquest estil.

Tot seguit, podem veure un exemple de les diferents interfícies que trobem a l’aplicació. Són simples, agradables a la vista i intuïtives.

[![Captura de pantalla 2015-06-15 a la(s) 00.50.42.png](images/600px-Captura\_de\_pantalla\_2015-06-15\_a\_la%28s%29\_00.50.42.png)](/pti/index.php/File:Captura_de_pantalla_2015-06-15_a_la(s)_00.50.42.png)

## Valoració econòmica[[edit](/pti/index.php?title=Categor%C3%ADa:Playit&veaction=edit&section=7 "Edit section: Valoració econòmica") | [edit source](/pti/index.php?title=Categor%C3%ADa:Playit&action=edit&section=7 "Edit section: Valoració econòmica")]

### Costos d'implementació[[edit](/pti/index.php?title=Categor%C3%ADa:Playit&veaction=edit&section=8 "Edit section: Costos d'implementació") | [edit source](/pti/index.php?title=Categor%C3%ADa:Playit&action=edit&section=8 "Edit section: Costos d'implementació")]

Els costos d’implementació han estat mínims, si no nuls. Totes les eines que hem utilitzat són gratuites.

Únicament podem destacar el cost de registre a www.laracasts.com, web que ofereix tutorials de Laravel en format video, que ens ha servit molt per a aprendre sobre Laravel i les seves possibilitats.

### Costos d'implantació[[edit](/pti/index.php?title=Categor%C3%ADa:Playit&veaction=edit&section=9 "Edit section: Costos d'implantació") | [edit source](/pti/index.php?title=Categor%C3%ADa:Playit&action=edit&section=9 "Edit section: Costos d'implantació")]

Fins el moment, l’únic cost d’implantació és el dels tags NFC per a poder fer les proves per a comprovar que el sistema funciona correctament.

En quant al hosting del servidor i la base de dades, DigitalOcean ens ho ofereix de franc.

Doncs, en una futura implantació en un cas real, l’únic cost derivat seria l’adquisició dels tags NFC necessaris per a la validació en la discoteca en qüestió.

## Desenvolupament futur[[edit](/pti/index.php?title=Categor%C3%ADa:Playit&veaction=edit&section=10 "Edit section: Desenvolupament futur") | [edit source](/pti/index.php?title=Categor%C3%ADa:Playit&action=edit&section=10 "Edit section: Desenvolupament futur")]

El desenvolupament futur seria la continuació d’aquest projecte per a poder-lo implantar en un cas real.

Doncs, ja tenim bastantes idees de novetats que podem introduir:

* Crear una xarxa social: primerament establint un cercador de perfils entre usuaris. Això facilitarà, entre d’altres, a promoure els events que utilitzin el nostre sistema.
* Establir assoliments: els usuaris tindran la possibilitat de ser premiats amb privilegis dins de l’aplicació. S’aconseguiran mostrant fidelitat a l’aplicació, a sales concretes o a DJs.
* Crear l’aplicació per a iOS: una part important de la població utilitza dispositius mòbils Apple, per tant l’èxit de l’aplicació ve condicionat per aquest factor.
* Traduir a altres llengües: d’aquesta manera incrementarem el nombre d’usuaris possibles i la promoció de l’aplicació. Anglès, espanyol i alemany són els primers idiomes als que traduirem web i aplicació.
* Comprar domini: abans de llançar la web caldrà comprar un domini. De moment els que ens semblaven adequats no estan disponibles.
* Possibilitar sessions domèstiques: oferir als usuaris crear sessions per a festes particulars, sense la necessitat de validar els votants amb NFC. Seria establir una contrassenya per a l’event, proporcionada als individus in situ.