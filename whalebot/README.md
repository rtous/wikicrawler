## Contents

* [1 Introducció](#Introducci.C3.B3)
  + [1.1 Motivació](#Motivaci.C3.B3)
  + [1.2 ¿Què és Whalebot?](#.C2.BFQu.C3.A8_.C3.A9s_Whalebot.3F)
* [2 Infraestructura](#Infraestructura)
  + [2.1 Api Blockchain](#Api_Blockchain)
  + [2.2 Base de dades](#Base_de_dades)
  + [2.3 Machine Learning](#Machine_Learning)
  + [2.4 Server Deployment](#Server_Deployment)
  + [2.5 Interfície gràfica](#Interf.C3.ADcie_gr.C3.A0fica)
* [3 Resultats](#Resultats)
* [4 Futures implementacions](#Futures_implementacions)

# Introducció[[edit](/pti/index.php?title=Categor%C3%ADa:whalebot&veaction=edit&section=1 "Edit section: Introducció") | [edit source](/pti/index.php?title=Categor%C3%ADa:whalebot&action=edit&section=1 "Edit section: Introducció")]

## Motivació[[edit](/pti/index.php?title=Categor%C3%ADa:whalebot&veaction=edit&section=2 "Edit section: Motivació") | [edit source](/pti/index.php?title=Categor%C3%ADa:whalebot&action=edit&section=2 "Edit section: Motivació")]

Amb l'arribada de bitcoin i el seu creixement en popularitat, així com de moltes altres criptomonedes, molta gent veu una nova manera de generar riquesa de manera fàcil i ràpida. Sobretot la població més jove, a causa de la impulsivitat i inexperiència sovint comet errors d'inversió i acaben perdent considerables quantitats de diners. Això seria evitable amb un coneixement adequat en inversions i en el mercat de les criptomonedes en general, però no tothom té el temps o les ganes per posar-se a aprendre sobre un món tan ampli i complex com aquest. Però, i si hi hagués una manera de realitzar inversions fiables sense necessitar invertir tantes hores en recerca? D'aquí surt la idea del nostre projecte, "whalebot".

## ¿Què és Whalebot?[[edit](/pti/index.php?title=Categor%C3%ADa:whalebot&veaction=edit&section=3 "Edit section: ¿Què és Whalebot?") | [edit source](/pti/index.php?title=Categor%C3%ADa:whalebot&action=edit&section=3 "Edit section: ¿Què és Whalebot?")]

Whalebot és un sistema capaç de llegir i interpretar les transaccions de criptomonedes a la blockchain, en concret els moviments de les anomenades balenes (whales en anglès). Les balanes mouen quantitats molt elevades, i sovint causen un impacte directe al valor de les criptomonedes amb les que opera. L'objectiu de Whalebot és, mitjançant un model de Machine Learning, intentar predir els efectes que aquests moviments produiran en el mercat de criptomonedes. Aquesta predicció se li mostra a l'usuari de manera clara a través d'una interfície gràfica amigable i entendible per l'usuari.

# Infraestructura[[edit](/pti/index.php?title=Categor%C3%ADa:whalebot&veaction=edit&section=4 "Edit section: Infraestructura") | [edit source](/pti/index.php?title=Categor%C3%ADa:whalebot&action=edit&section=4 "Edit section: Infraestructura")]

## Api Blockchain[[edit](/pti/index.php?title=Categor%C3%ADa:whalebot&veaction=edit&section=5 "Edit section: Api Blockchain") | [edit source](/pti/index.php?title=Categor%C3%ADa:whalebot&action=edit&section=5 "Edit section: Api Blockchain")]

## Base de dades[[edit](/pti/index.php?title=Categor%C3%ADa:whalebot&veaction=edit&section=6 "Edit section: Base de dades") | [edit source](/pti/index.php?title=Categor%C3%ADa:whalebot&action=edit&section=6 "Edit section: Base de dades")]

Necessitàvem un gestor de base de dades per a emmagatzemar les dades, i poder fer modificacions i consultes de cara a realitzar prediccions i poder informar a l'usuari a través de la interfície gràfica que comentarem més endavant.

El gestor escollit és MongoDB per les següents raons:
Senzillesa: No necessitàvem una estructura molt complexa per emmagatzemar les dades, de manera que hem pensat que una BBDD no relacional seria més fàcil d'implementar i s'adaptaria més a les nostres necessitats.

Flexibilitat: Al moment de començar a recollir dades encara no teníem del tot clar si podríem necessitar més camps a posteriori, el fet de poder-ne afegir sense haver de modificar la resta d'elements era una característica clau.

Optimització: És ideal per a fer consultes de grans quantitats de dades, i consumeix pocs recursos. Per a entrenar el model de Machine Learning necessitàvem les dades de moltes transaccions, i les nostres màquines tenen recursos
limitats, de manera que en aquest sentit també s'adaptava molt al que necessitàvem.

Aprenentatge: Cap dels membres del grup havíem treballat amb MongoDB, la qual cosa ha estat un incentiu també per escollir-la i així aprendre com funciona.

La funció de la nostra base de dades és emmagatzemar les transaccions que són llegides per l'script de la API, i passen el filtre corresponent de quantitat i adreces explicat anteriorment. Una vegada les tenim emmagatzemades, aquestes s'utilitzen per a entrenar el model de Machine Learning que farà les prediccions que després es traspassaran a l'usuari final, així com per a mostrar a l'usuari les transaccions que es van donant en temps real.

## Machine Learning[[edit](/pti/index.php?title=Categor%C3%ADa:whalebot&veaction=edit&section=7 "Edit section: Machine Learning") | [edit source](/pti/index.php?title=Categor%C3%ADa:whalebot&action=edit&section=7 "Edit section: Machine Learning")]

## Server Deployment[[edit](/pti/index.php?title=Categor%C3%ADa:whalebot&veaction=edit&section=8 "Edit section: Server Deployment") | [edit source](/pti/index.php?title=Categor%C3%ADa:whalebot&action=edit&section=8 "Edit section: Server Deployment")]

## Interfície gràfica[[edit](/pti/index.php?title=Categor%C3%ADa:whalebot&veaction=edit&section=9 "Edit section: Interfície gràfica") | [edit source](/pti/index.php?title=Categor%C3%ADa:whalebot&action=edit&section=9 "Edit section: Interfície gràfica")]

La interfície gràfica s'ha creat mitjançant la llibreria tkinter de python. Aquesta et permet crear una finestra per la aplicació i insertar-li frames, labels, buttons, i altres funcions útils de cara a oferir una experiència satisfactòria i intuitiva.
Per la nostra aplicació necessitavem una interfície de caràcter informatiu més que interactiu. L'objectiu era que l'usuari identifiqués a primera vista la predicció en cada moment i les transaccions de les balenes que van succeint a temps real. Per fer-ho hem implementat un script que fa consultes periòdiques a la base de dades, i quan detecta que s'ha afegit un o més nous documents a la col·lecció de transaccions, els agafa per mostrar-los per la interfície i actualitza el valor de la predicció.

A la següent imatge es veu un exemple de la vista de la interfície:

[![](images/800px-Foto\_interficie\_grafica.png)](/pti/index.php/File:Foto_interficie_grafica.png)

Interfície gràfica

A la cantonada superior esquerra tenim un rellotge, que apart de la seva utilitat informativa, dóna a l'usuari una sensació de dinamisme de la aplicació, garantint que aquesta segueix en funcionament i verificant que la hora de les transaccions coincideix amb la del rellotge.

Al centre de la finestra a la part superior tenim la acció que ens recomana el sistema segons la predicció més recent que hagi realitzat el model de Machine Learning. Aquest oscil·la entre valors de "Hard Sell, Sell, Neutral, Buy, Hard Buy". Més abaix i ocupant la major part de la finestra, tenim els logs de les transaccions que es van recollint de la base de dades, disponibles perquè l'usuari fagi els seus propis anàlisis si així ho vol.

Per acabar, a la cantonad superior dreta hi ha un botó "Clear Results" que refresca la finestra per tal de que no s'acumulin infinits logs de transaccions en pantalla.

# Resultats[[edit](/pti/index.php?title=Categor%C3%ADa:whalebot&veaction=edit&section=10 "Edit section: Resultats") | [edit source](/pti/index.php?title=Categor%C3%ADa:whalebot&action=edit&section=10 "Edit section: Resultats")]

# Futures implementacions[[edit](/pti/index.php?title=Categor%C3%ADa:whalebot&veaction=edit&section=11 "Edit section: Futures implementacions") | [edit source](/pti/index.php?title=Categor%C3%ADa:whalebot&action=edit&section=11 "Edit section: Futures implementacions")]

La idea inicial del projecte era integrar-ho tot en un bot que operés directament a binance o qualsevol altre exchange, de manera que les transaccions fossin automatitzades en funció de les prediccions obtingudes i uns paràmetres a determinar.
A causa de la reducció de nombres del nostre grup (al final només hem quedat dos) vam haver de prescindir d'aquesta part del projecte i quedar-nos només amb la part de recol·lecció, predicció i frontend. Tot i això, de cara al futur seria interessant implementar-ho en un exchange i veure l'efectivitat de les prediccions en un entorn real i si realment genera benefici de manera regular.

Per altra banda, tot i que la interfície compleix el seu objectiu de cara a la funcionalitat, el disseny no s'adapta als estàndards d'una aplicació moderna i seria atractiu millorar-la en aquest sentit.

Per acabar, per falta d'informació no hem pogut calcular les prediccions tenint en compte les variacions de preu a una setmana posterior a la transacció (camp price\_1w), i tenint en compte que la precisió de les prediccions a un dia millora un 10% respecte a les prediccions a una hora, caldria veure quina variació té la predicció a una setmana respecte a les anteriors.