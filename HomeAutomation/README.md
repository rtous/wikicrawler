[![](images/200px-HomeAutomation.png)](/pti/index.php/File:HomeAutomation.png)

HomeAutomation.

## Contents

* [1 Introducció](#Introducci.C3.B3)
  + [1.1 En què consisteix?](#En_qu.C3.A8_consisteix.3F)
  + [1.2 Objectius](#Objectius)
* [2 Components](#Components)
  + [2.1 Workflow del projecte](#Workflow_del_projecte)
  + [2.2 Hardware](#Hardware)
    - [2.2.1 Raspberry Pi](#Raspberry_Pi)
    - [2.2.2 Aparell de recepció de senyals](#Aparell_de_recepci.C3.B3_de_senyals)
    - [2.2.3 Aparell d'emssió de senyals](#Aparell_d.27emssi.C3.B3_de_senyals)
    - [2.2.4 Assistents de veu](#Assistents_de_veu)
  + [2.3 Software](#Software)
    - [2.3.1 IFTTT](#IFTTT)
    - [2.3.2 Dweet.io](#Dweet.io)
    - [2.3.3 Analisi de les senyals](#Analisi_de_les_senyals)
    - [2.3.4 Audacity](#Audacity)
* [3 El codi](#El_codi)
  + [3.1 Perquè Python?](#Perqu.C3.A8_Python.3F)
  + [3.2 Llibreries utilitzades](#Llibreries_utilitzades)
    - [3.2.1 rpi-rf](#rpi-rf)
    - [3.2.2 Dweepy](#Dweepy)
  + [3.3 Fragments de codi importants i breu explicació](#Fragments_de_codi_importants_i_breu_explicaci.C3.B3)
    - [3.3.1 Subscripció a accións: Tractament](#Subscripci.C3.B3_a_acci.C3.B3ns:_Tractament)
    - [3.3.2 Subscripció a accións: Retry](#Subscripci.C3.B3_a_acci.C3.B3ns:_Retry)
* [4 Problemes afrontats i solucións](#Problemes_afrontats_i_soluci.C3.B3ns)
  + [4.1 Lectura de les senyals](#Lectura_de_les_senyals)
  + [4.2 Emissió de les senyals](#Emissi.C3.B3_de_les_senyals)
    - [4.2.1 Mod Llibreria: Protocol Genèric](#Mod_Llibreria:_Protocol_Gen.C3.A8ric)
    - [4.2.2 Mod Llibreria: Millora de la precisió](#Mod_Llibreria:_Millora_de_la_precisi.C3.B3)
  + [4.3 Subscripció a accións](#Subscripci.C3.B3_a_acci.C3.B3ns)
  + [4.4 Servidor web](#Servidor_web)

# Introducció[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=1 "Edit section: Introducció") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=1 "Edit section: Introducció")]

## En què consisteix?[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=2 "Edit section: En què consisteix?") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=2 "Edit section: En què consisteix?")]

El nostre projecte es basa en un cas real d'una persona de mobilitat reduïda, la qual, actualment, no pot moure les extremitats. Fa uns anys va fer una gran inversió per tal d'automatitzar la seva casa amb portes i persianes controlats per RF, però actualment només pot utilitzar la veu. Com és comprensible, no vol fer una nova inversió i canviar de nou tota la tecnologia de la casa seva, i aquí es on neix la nostra idea.

El hem fet es adaptar el nostre sistema a la casa, en comptes del procés tipic d'adaptar la casa a la tecnologia. Per això, hem integrat els assistents de veu amb tot el sistema de RF del que disposa aquesta persona per tal que pugui controlar les portes i persianes de la seva casa a través de comandes de veu. A més a més, el producte final permetria controlar també el televisor o l'aire acondicionat, tot i que s'haurien de fer petites modificacions.

## Objectius[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=3 "Edit section: Objectius") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=3 "Edit section: Objectius")]

* Comunicar un assistent de veu amb una Raspberry.
* Utilitzar comandes de veu concretes per accions específiques (no integrades amb les AV).
* Tenir una tecnologia pràcticament "Plug and Play" on la persona no necessiti configurar res.
* Que sigui escalable a més portes, persianes i cases i usuaris.
* Conseguir que la Raspberry emeti RF concrets per a obrir i tancar cada porta i persiana diferent.
* Que sigui fiable i que els usuaris piguin dependre de la nostra solució amb garanties.

# Components[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=4 "Edit section: Components") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=4 "Edit section: Components")]

## Workflow del projecte[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=5 "Edit section: Workflow del projecte") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=5 "Edit section: Workflow del projecte")]

En la imatge es mostra un diagrama amb les diferents tecnologies emprades en el projecte i com es connecten entre elles, des de l'usuari fins l'objectiu d'obrir la porta.

[![](images/300px-HomeAutomation\_1.png)](/pti/index.php/File:HomeAutomation_1.png)

Flow del projecte

## Hardware[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=6 "Edit section: Hardware") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=6 "Edit section: Hardware")]

El hardware es la part més important del nostre projecte. Hem necessitat una Raspberry Pi que ha estat el cervell del nostre sistema, també un dispositiu amb assistent de veu per tal de poder donar-li les comandes. A més a més, hem hagut de comprar un accessori especial per a la Raspberry per a fer la emissió de les senyals i una antena externa amb USB per poder llegir-les.

### Raspberry Pi[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=7 "Edit section: Raspberry Pi") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=7 "Edit section: Raspberry Pi")]

La elecció estava entre la RPI o un Arduino. El principal problema de l'Arduino era el fet de no tenir un sistema operatiu i stack TCP/IP i la desventatja de programar en C (ja que teniem poc temps per a fer el projecte).

Utilitzant una Raspberry teníem una llibertat molt més gran a l'hora d'escollir les diverses tecnologies que voliem utilitzar, com ara Python i les seves llibreries, que ens han facilitat moltes coses, deixant-nos centrar en altres problemes més importants del projecte.

El model utilitzat ha estat el 3B+. Un model assequible per a qualsevol butxaca, i que funciona perfectament amb el nostra sistema. De totes formes, qualsevol model de Raspberry o altres copies hauria de ser compatible amb el nostre projecte

### Aparell de recepció de senyals[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=8 "Edit section: Aparell de recepció de senyals") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=8 "Edit section: Aparell de recepció de senyals")]

Tot i que un dels objectius és la no intervenció física de l'usuari per a configurar el dispositiu, hem determinat que afegir senyals de manera dinamica afegeix massa complexitat al projecte. Per aixó hem decidit analitzar manualment les senyals dels mandos a copiar i incorporar-les manualment en el nostre codi. Per tant, un dels dispositius més necessàris era el que ens permetria capturar les senyals. Si no podiem llegir les senyals no podriem fer el projecte que teniem en ment. La recerca per a trobar una antena assequible i que poguessim utilitzar amb comoditat va ser extensa, ja que existeixen molts tipus d'antena. La nostra havia de ser compatible amb la banda de 433MHz, que és la que s'utilitza normalment en els comandaments que tenim a casa.

Finalment vam trobar el model **Nooelec NESDR Mini 2** que ens permetia capturar gran part de l'espectre radioelèctric. El vam comprar a través d'Amazon i ens va arribar relativament ràpid. Això ho vam poder fer abans del confinament, per sort.

### Aparell d'emssió de senyals[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=9 "Edit section: Aparell d'emssió de senyals") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=9 "Edit section: Aparell d'emssió de senyals")]

En aquest apartat tenim moltes opcions disponibles, des de microncontroladors amb conexions I2C o algun protocol similar que s'han de configurar amb les especificacions del seu datasheet abans d'emtre qualsevol cosa fins a plaques amb un sol pin d'entrada de dades que emeten l'estat (Up o Down) del pin en qüestió.

Un altre fet important és que vam detectat que tots els comandaments que voliem adaptar modulaven la seva senyal amb **ASK** (Amplitude Shift Keying), pel que vam centrar la nostre cerca en dispositius que permetessin aquesta modulació. Un avantatge és que és molt fàcil i barat d'implementar electrònicament, pel que la oferta és amplia

Per simplicitat hem acabat escollint un dels aparells més senzills que hem trobat. Aquest modula únicament en ASK i només té un pin de dades que conectem a la RaspBerry directament

### Assistents de veu[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=10 "Edit section: Assistents de veu") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=10 "Edit section: Assistents de veu")]

Amb la decisió d'utilitzar IFTTT vam tenir la llibertat de poder escollir qualsevol dispositiu amb un assistent de veu. En el nostre cas el propi smartphone.

## Software[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=11 "Edit section: Software") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=11 "Edit section: Software")]

Dividim el software en dos subgrups. El software utilitzar per a **comunicar els elements de Hardware entre ells** i el software utilitzar per al **processament i visualització de les senyals**.

### IFTTT[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=12 "Edit section: IFTTT") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=12 "Edit section: IFTTT")]

IFTTT es l'acrònim per a "If This Then That". Bàsicament es un servei que permet la integració d'assistents virtuals per a executar comandes de veu personalitzades amb accions personalitzades.

Hem escollit IFTTT per la compatibilitat amb les diferents assistents de veu del mercat i la senzillesa de la seva interfaç d'usuari. IFTTT es comunica a través d'un webhook a un servei de subscripció a accións per a que aquest sigui consultat per la Raspberry Pi.

És a dir, IFTTT fa un canvi en una variable en el servei de subscripció a accións que farà de trigger per a que la Raspberry envii la senyal RF a la porta / persiana que toca.

**Alternativa self-hosted**: Si es volgués obtenir els resultats que ens brinda IFTTT sense haver de dependre d'un tercer es podria utilitzar un software com **[Node-RED](https://nodered.org/)** amb [el "node"](https://flows.nodered.org/node/node-red-contrib-google-action) per integrar-lo amb Google assistant.

### Dweet.io[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=13 "Edit section: Dweet.io") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=13 "Edit section: Dweet.io")]

Dweet.io es un servei de subscripció a accións gratuït amb accés a través d'una API i que té una còmode llibreria Python. Vam estar contemplant altres alternatives com Pubnub o Jet, però Dweet era la més senzilla i la més còmode per al nostre projecte.

Podem veure Dweet com un Twitter per coses. Les coses publiquen Dweets que poden ser llegits posteriorment per altres dispositius. És a dir, l'assistent de veu a través de IFTTT publica un Dweet per la cosa "Porta 1" i la Raspberry, que *segueix* aquesta cosa (Porta 1) quan veu la publicació pot actuar.

**Alternativa self-hosted**: Si es volgués obtenir els resultats que ens brinda Dweet.io sense dependre d'un tercer es podria utilitzar una alternativa com [Gotify](https://gotify.net/). Gotify es exactament el mateix que Dweet però és Open Source i es pot hostejar en un servidor propi. A més està escrit en Go i és força eficient.

### Analisi de les senyals[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=14 "Edit section: Analisi de les senyals") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=14 "Edit section: Analisi de les senyals")]

El dispositiu que hem fet servir és el que s'anomena Software Defined Radio (SDR). Per tant, es pot utlitzar qualsevol programa per a interpetar les dades que aquest ens dona. Primer vam fer servir **SDR#** per Windows i més tard **gqrx** per GNU. Dos programes molt semblants que ens permetien veure l'espectre radioelectric de manera visual així com capturar part d'aquest espectre que més tard vam passar per l'Audacity per a tractar-lo com una senyal d'audio normal, i així poder apreciar visualment els codis que els comandaments emetien

Amb aquest programa hem pogut visualitzar a temps real l'emisió de la senyal del comandament, però no era suficientment ampliada com per a poder interpretar els bits d'aquesta. Amb aquest programa podiem grabar la senyal com si fos so i així poder-la obrira amb Audacity.

### Audacity[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=15 "Edit section: Audacity") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=15 "Edit section: Audacity")]

Com que vam considerar que afegir les senyals de manera dninamica afegia molta complexitat al projecte, vam decidir analitzar les senyals de forma manual. Per aixo les vam tracat com a senyals d'audio normals ,després de haver-les capturat amb SDR# o gqrx, amb el programa Audacity. Un cop importats els arxius es pot fer zoom in per a apreciar molt bé els bits transmesos, i hem importat aquest valor en el nostre codi perque la llibreria **rpi-rf** ho emeti

# El codi[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=16 "Edit section: El codi") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=16 "Edit section: El codi")]

El codi es força breu. Només hem hagut de tractar la subscripció a accións a través d'una connexió HTTP oberta amb Dweet.io gràcies amb l'endpoint anomenat **/listen/for/dweets/from/{thing}**, on

Per altra banda, la part més complicada ha estat que hem necessitat editar les diferentes llibreries de Python per tal que l'emissió de les senyals fos correcta, ja que ens trobavem amb petits retards i altres problemes explicats en l'apartat []

## Perquè Python?[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=17 "Edit section: Perquè Python?") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=17 "Edit section: Perquè Python?")]

Sabiem que teniem poc temps per a fer el projecte, erem dues persones la qual cosa significava una major càrrega de treball per a cada un. Els dos coneixiem Python, creiem que es un llenguatge modern i molt utilitzat actualment i a més compta amb un gran nombre de llibreries útils. Per aquests motius vam escollir Python.

Per el tema d'eficiència i perquè vam fer un laboratori a PTI vam considerar decantar-nos per Go, però finalment com que cap dels dos havia treballat amb Go i ens podia complicar més les coses el vam descartar.

## Llibreries utilitzades[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=18 "Edit section: Llibreries utilitzades") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=18 "Edit section: Llibreries utilitzades")]

### rpi-rf[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=19 "Edit section: rpi-rf") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=19 "Edit section: rpi-rf")]

[rpi-rf](https://github.com/milaq/rpi-rf) és una llibreria pensada per sistemes que corren en una Raspberry que permet rebre i emetre senyals radioelèctriques sempre que disposem del dispositiu adeqüat conectat en un dels pins GPIO de la propia raspberry. Malauradament, més tard hem descobert que aquesta llibreria tenia forçes limitacions pel que hem hagut de fer [algunes modificacions](https://github.com/sergimn/rpi-rf/commits/acb11c968f7d406b19da6a0992e10bed4c2b07ae) per a tenir una solució funcional.

### Dweepy[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=20 "Edit section: Dweepy") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=20 "Edit section: Dweepy")]

Buscant per Github, vam trobar que existia una llibreria creada per un individual per interactuar amb Dweet.io a través de Python d'una manera molt senzilla.

Té crides tant senzilles com:

```
dweepy.dweet_for('Cosa X', {'clau': 'valor'})

```

Amb aquesta crida tant senzilla podem crear un nou dweet per la cosa **"Cosa X"**. També ens donava molta facilitat per a la subscripció a les accións amb un codi més net i breu, com per exemple:

```
for dweet in dweepy.listen_for_dweets_from('Cosa X'):

```

Amb aquesta sola línia podríem escoltar tots els Dweets d'una sola cosa. Bàsicament és el que ens interessa.

## Fragments de codi importants i breu explicació[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=21 "Edit section: Fragments de codi importants i breu explicació") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=21 "Edit section: Fragments de codi importants i breu explicació")]

#### Subscripció a accións: Tractament[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=22 "Edit section: Subscripció a accións: Tractament") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=22 "Edit section: Subscripció a accións: Tractament")]

```
 for dweet in dweepy.listen_for_dweets_from(id):
        cnt = dweet['content']
        if "keepalive" in cnt:
            logger.debug("Keepalive Dweet")
        if cnt.setdefault(porta_fora):
            logger.info("Obrint la porta de fora")
            rf.tx_code(679159...06659, 7, 320, len("11100...010"))
```

Aquest es un fragment de codi, que hem retallat per l'exemple, on es mostra com estem *escoltant* per nous Dweets. Quan un nou dweet arriba, la funció entra i busquem el contingut d'aquest Dweet. Si, per exemple, el Dweet coincideix amb el codi de **porta de fora** s'executa lacció i obrim la porta de fora a través de l'última acció que podem veure.

Com es pot observar, la primera comprovació es de si el contingut es un *keepalive*. Aquest es un dels primers problemes que ens vam trobar en el projecte i el qual vam haver de pensar una manera eficient per a solucionar-lo.

Resulta que Dweet, en la versió gratuïta, només et deixa tenir sessions TCP de fins a 59s obertes des de l'últim *dweet* rebut. Això vol dir que, si la persona obra la porta al matí i el següent cop és a la tarda ens trobariem que Dweet.io ha tancat la connexió TCP i ja no estem escoltant pels nous *dweets*. La solució a aquest problema s'explica en l'apartat 5.3 *Problemes amb la subscripció a accións*.

#### Subscripció a accións: Retry[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=23 "Edit section: Subscripció a accións: Retry") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=23 "Edit section: Subscripció a accións: Retry")]

```
 def retry(function, on_exceptions=None, attempts=2, every_s=0.5):
    def _try_operation(retries_left=attempts):
        try:
            result = function()
        except (on_exceptions or Exception) as e:
            if retries_left > 0:
                time.sleep(every_s)
                result = _try_operation(retries_left - 1)
            else:
                raise e

        return result

    return _try_operation()
```

# Problemes afrontats i solucións[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=24 "Edit section: Problemes afrontats i solucións") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=24 "Edit section: Problemes afrontats i solucións")]

## Lectura de les senyals[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=25 "Edit section: Lectura de les senyals") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=25 "Edit section: Lectura de les senyals")]

La llibreria que hem decidit fer servir ofereix suport per a llegir senyals radioelèctriques. Tot i així, com hem comentat abans, aquesta no és una llibreria gaire flexible i no hi hauria manera de debugar problemes en la lectura de senyals. A més a més, vam creure que la càrrega dinàmica de noves senyals afegiria una complexitat que faria difícil la viabilitat del projecte. Al final, hem optat per a analitzar les senyals de forma visual nosaltres mateixos, sabent que aixó trenca l'objectiu de obtenir una solució PnP, pero entenem que és un sacrifici comprensible i que podria ser solucionat en un futur.

## Emissió de les senyals[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=26 "Edit section: Emissió de les senyals") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=26 "Edit section: Emissió de les senyals")]

Aquesta és la part més crítica del projecte, ja que si no aconseguim obrir les portes o aixecar les persianes, no estarem aconseguint l'objectiu primordial, que funcioni. Per aixó els requisits de l'emissió són força estrictes i és que si no aconseguim emetre una senyal molt semblant (de fet, necessitem que sigui gairebé igual) els dispositius no reaccionaran. Per aquest motiu vam haver de fer dues modificacions en la llibreria que haviem escollit.

### Mod Llibreria: Protocol Genèric[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=27 "Edit section: Mod Llibreria: Protocol Genèric") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=27 "Edit section: Mod Llibreria: Protocol Genèric")]

rpi-rf no està específicament dissenyada per a interactuar amb qualsevol dispositiu. Més aviat es va crear pensant en dispositius concrets de marques conegudes pel que a priori no podiem interactuar amb cap dispositiu que no fos aquells inicialment pensats.
Aquest problema es deu a que la llibreria intenta facilitar la feina al desenvolupador abstraient la codificació de les senyals a través del que anomena *Protocols*. Els Protocols, dins de l'argot de la llibreria, no són més que perfils de codificació, o sigui maneres en la que els '1' i els '0' són representats en al senyal emesa (per exemple, el símbol 0 podria consistir en les senyals 10, mentre que el simbol 1 consistiria en la senyal 11).
Per aquest motiu vam crear el que anomenem un protocol genèric, en el que el símbol 0 és representat per la senyal 0 i el símbol 1 per la senyal 1, d'aquesta manera, podriem emetre qualsevol senyal.

### Mod Llibreria: Millora de la precisió[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=28 "Edit section: Mod Llibreria: Millora de la precisió") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=28 "Edit section: Mod Llibreria: Millora de la precisió")]

Després d'aconseguir la senyal que haviem d'emetre per a activar els dispositius de la casa ens vam trobar amb un problema força curiós i és que la senyal que emeteiem semblava ser la que desitjavem, en realitat només ho semblava. El que es podia apreciar és que, evidentment, el missatge era correcte, pero no hi havia manera de aconseguir una llargada de bit constant o deterministica, pel que la llargada dels missatges no era constant i cap receptor entenia el missatge degut a que el mostreig de la senyal és fix.
La sospita principal era que el procés que s'encarregava de establir el pin de la raspberry a Up i a Down feia un context switch en el moment que havia de fer el canvi i aquest passava instants després, quan ja era massa tard i l'error es propagava infinitament, ja que la llibreria no està preparada per detectar aquests errors. De totes formes, és difícil aclarir si aquest és realment el problema i encara més solucionar-lo en un Sistema Operatiu d'ús general i en un llenguatge d'alt nivell com Python. Per sort, analitzant la llibreria vam detectar que l'espera de una transició de bit a la següent es feia a través de un **sleep**, que posa el procés en la cua de *Sleeping*, pel que un procés de la cua de *Ready* entra en aquella CPU i tot i que el nostre procés es desperta gairebé immediatament, en un sistema com aquest, ja s'ha perdut el deadline de cambi de de bit. La solució que hem fet servir ha estat fer una espera activa, fent un sleep just després de un canvi d'estat, per evitar que el SO ens el forçi en el moment menys adeqüat, igual que abans.

## Subscripció a accións[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=29 "Edit section: Subscripció a accións") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=29 "Edit section: Subscripció a accións")]

Com bé hem comentat anteriorment, en la subscripció a accións el principal problema que vam trobar va ser el fet que Dweet.io només deixa tenir connexions TCP de fins a 59s des de l'últim Dweet en la seva versió gratuïta.

Aquest problema feia que el projecte deixés de ser viable, ja que el sistema no podia estar més de 59s en estat **"idle"**, és a dir, la persona no podia estar més de 59s sense utilitzar el sistema o es tancaria la connexió. A més a més, la llibreria que utilitzem llança una excepció en aquest cas, pel que si no fem res al respecte, el programa acabaria la seva execució de forma anormal.

Evidentment, això no es una opció ja que no tindria cap mena d'usabilitat ni comoditat. Per aquest motiu, va ser necessari pensar una manera senzilla però eficient de mantenir les connexións TCP obertes. La manera més senzilla i clara de solventar aquest problema va ser utilitzant el clàssic concepte de *keepalive*. Petits missatges sense informació cada x segons (x<59) que ens mantenen la connexió viva.

El fragment de codi que aconsegueix això es el següent:

```
 def keepalive(id):
    logger.debug("Running keepaliver")
    while True:
        time.sleep(45)
        logger.debug("Sending keepalive")
        utils.retry(
            function=lambda: dweepy.dweet_for(thing_name=id,payload={"keepalive": 1}),
            on_exceptions=dweepy.api.DweepyError,
            attempts=10000,
            every_s=3
        )
```

Com veiem, la funció conté un **while True** el qual s'estarà executant en bucle. S'esperarà 45 segons abans d'enviar el *keepalive*. A més a més també fem servir la funció **retry** que evita un corner case en el que s'envien múltiples peticions als servidors de dweet.io i aquest decideix bloquejar la IP origen durant uns segons. Aquest no és un cas que esperem que passi sovint, pero com que no podem preveure l'entorn en el que el nostre dispositiu s'acabarà desplegant, per exemple en uncas de internet a traves de CG-NAT, hem intentat solucionar aquest problema.

## Servidor web[[edit](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&veaction=edit&section=30 "Edit section: Servidor web") | [edit source](/pti/index.php?title=Categor%C3%ADa:HomeAutomation&action=edit&section=30 "Edit section: Servidor web")]

Disposar de tots els components de la nostra solucó en un sol dispositiu, la Raspberry, en aquest cas, hagués estat una situació ideal. Per aixó necessitariem alguna mena de servei en la Raspberry que escoltes conexions entrants en forma de missatges com "Obra la porta". El problema, però, és que necessitem alguna manera de comunicar l'assistent de veu, que no té perqué estar a la mateixa xarxa que la Raspberry. En aquest cas, l'utilització comuna de NAT en les conexions domestiques ens obligaria a configurar el router per a fer *Port Forwarding* i a obtenir sempre la mateixa IP dins de la xarxa, cosa que implicaria la necessitat de configuració per l'usuari final, una acció que volem evitar. També podriem fer servir UPnP, pero aquest és un servei que no està sempre disponible i per tant hauriem de recòrrer al cas anterior.
Degut a les complicacions mencionades hem acabat decidint que externalitzariem aquestes funcions i que seria dweet.io el que faria push de les actualitzacions amb una conexió previament oberta per nosaltres, de una manera semblant a les notificacions dels smartphones.