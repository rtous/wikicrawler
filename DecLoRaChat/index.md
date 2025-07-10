# Introducción[[edit](/pti/index.php?title=Categor%C3%ADa:DecLoRaChat&veaction=edit&section=1 "Edit section: Introducción") | [edit source](/pti/index.php?title=Categor%C3%ADa:DecLoRaChat&action=edit&section=1 "Edit section: Introducción")]

El projecte Xat amb pagaments de criptodivises mitjançant LoRa és el treball en grup realitzat per a l'assignatura de Projecte de tecnologies de la informació.
L'objectiu d'aquest projecte és proporcionar un xat que funcioni mitjançant la tecnologia LoRa, i que alhora tingui la capacitat de fer pagaments amb criptodivises als contactes de l'usuari.
Els usuaris fan servir el xat a través d'una aplicació Android que es comunica per Bluetooth amb els dispositius LoRa, i els pagaments que realitzen els usuaris es propaguen per la xarxa de la criptodivisa Bitcoin Cash (BCH) a través d'un node que actua de gateway.

[![](images/800px-Lorachat\_esquema.PNG)](/pti/index.php/File:Lorachat_esquema.PNG)

Google.

## Plantejament de LoRaChat[[edit](/pti/index.php?title=Categor%C3%ADa:DecLoRaChat&veaction=edit&section=2 "Edit section: Plantejament de LoRaChat") | [edit source](/pti/index.php?title=Categor%C3%ADa:DecLoRaChat&action=edit&section=2 "Edit section: Plantejament de LoRaChat")]

-Xat descentralitzat. Enviar missatges per nodes sense haver d’estar coordinats per un servidor centralitzat, i sense la necessitat que el receptor dels missatges estigui connectat.

-Comunicació de llarg abast. Utilitzar la tecnología sense fils LoRa per a comunicar els nodes propers en absència de connectivitat a Internet.

-Xarxa mesh. Implementar una xarxa mesh amb els nodes propers.

## Infraestructura[[edit](/pti/index.php?title=Categor%C3%ADa:DecLoRaChat&veaction=edit&section=3 "Edit section: Infraestructura") | [edit source](/pti/index.php?title=Categor%C3%ADa:DecLoRaChat&action=edit&section=3 "Edit section: Infraestructura")]

El nostre projecte té els següents components:

-Dispositius ESP32 amb connectivitat LoRa, Bluetooth i WiFi.

-Dispositious Android amb connectivitat Bluetooth.

-Ordinador Linux amb connectivitat WiFi i accés a Internet.

Els components interactuen de la següent manera:

-L'usuari escriu els missatges als contactes que té propers en un dispositiu Android, el qual els envia als ESP32 per Bluetooth.

-Els ESP32 es comuniquen entre ells emprant la llibreria LoRaMesher i l'aplicació LoRaChat per a enviar-se missatges per LoRa.

-Un d'aquests dispositius ESP32 és el gateway, que es comunica amb un ordinador per WiFi i li passa les transaccions de Bitcoin Cash que realitzen els usuaris.

-L'ordinador rep les transaccions i les propaga a la xarxa de Bitcoin Cash utilitzant un node BCHD que es comunica amb Internet.