[![](images/400px-Noogle\_logo.png)](/pti/index.php/File:Noogle_logo.png)

Noogle Logo

## Contents

* [1 Project Overview](#Project_Overview)
* [2 Com instalar](#Com_instalar)
  + [2.1 Utilitzant el Generador d'Instal·ladors públic a la Web](#Utilitzant_el_Generador_d.27Instal.C2.B7ladors_p.C3.BAblic_a_la_Web)
  + [2.2 Auto-Hostatjant el Generador d'Instal·ladors de Noogle](#Auto-Hostatjant_el_Generador_d.27Instal.C2.B7ladors_de_Noogle)
* [3 References](#References)

# Project Overview[[edit](/pti/index.php?title=Categor%C3%ADa:Noogle&veaction=edit&section=1 "Edit section: Project Overview") | [edit source](/pti/index.php?title=Categor%C3%ADa:Noogle&action=edit&section=1 "Edit section: Project Overview")]

La utilització de serveis proporcionats per empreses com Google i altres gegants tecnològics s'ha convertit en una pràctica habitual. Aquests serveis ofereixen comoditat i eficiencia, permetent als usuaris accedir a una àmplia gamma de funcionalitats.Pero aquesta conveniència no està lliure de conseqüències.

Malgrat la popularitat d'aquests serveis, les empreses que els proporcionen han estat objecte de múltiples desastres relacionats amb el tractament de les dades i l'incompliment de Reglament General de Protecció de Dades (GRPD). El preu que paguem per les avantatges d'aquests serveis és l'accés a les nostres dades personals.

Noogle neix amb la intenció de desafiar el paradigma actual on la privadesa queda en segon pla i l'únic que sembla important es la eficacia i eficiència dels serveis oferts.

Mitjançant la migració de serveis com Gmail, Google Drive, Youtube, Passwords, Calendar y mes cap a alternatives autogestionades, Noogle busca eliminar les preocupacions relacionades amb la privadesa, la dependència de dades i les limitacions funcionals imposades per les grans corporacions tecnològiques sense deixar de posar-ho fàcil per a l’usuari.

# Com instalar[[edit](/pti/index.php?title=Categor%C3%ADa:Noogle&veaction=edit&section=2 "Edit section: Com instalar") | [edit source](/pti/index.php?title=Categor%C3%ADa:Noogle&action=edit&section=2 "Edit section: Com instalar")]

Pots instal·lar Noogle de dues maneres, depenent de les teves preferències i necessitats.

## Utilitzant el Generador d'Instal·ladors públic a la Web[[edit](/pti/index.php?title=Categor%C3%ADa:Noogle&veaction=edit&section=3 "Edit section: Utilitzant el Generador d'Instal·ladors públic a la Web") | [edit source](/pti/index.php?title=Categor%C3%ADa:Noogle&action=edit&section=3 "Edit section: Utilitzant el Generador d'Instal·ladors públic a la Web")]

* Accedeix a la pàgina web oficial de Noogle <https://generator.noogle.site> .
* Utilitza l'eina d'instal·lador a la web per seleccionar els serveis que desitges instal·lar i personalitzar-ne la configuració.
* Una vegada hagis fet les seleccions, prem sobre el botó de descàrrega per obtenir l'instal·lador personalitzat.
* Descomprimeix el fitxer descarregat: tar -xvzf file.tar.gz
* Executa l’instalador: sudo chmod +x setup.sh && ./setup.sh

Després de la instal·lació, podràs accedir als serveis Noogle mitjançant l'adreça URL del teu servidor.

## Auto-Hostatjant el Generador d'Instal·ladors de Noogle[[edit](/pti/index.php?title=Categor%C3%ADa:Noogle&veaction=edit&section=4 "Edit section: Auto-Hostatjant el Generador d'Instal·ladors de Noogle") | [edit source](/pti/index.php?title=Categor%C3%ADa:Noogle&action=edit&section=4 "Edit section: Auto-Hostatjant el Generador d'Instal·ladors de Noogle")]

* Clona o descarrega el repositori de Noogle des del nostre repositori a GitHub: git clone <https://github.com/PolGs/noogle.git>
* Accedeix al directori del generador d'instal·ladors: cd noogle
* Executa el servidor web (es necessari tenir flask i jinja instal·lat): python3 main.py
* Accedeix a l'interfície web del generador a través de l'adreça del teu servidor i selecciona les opcions desitjades.
* Descarrega l'instal·lador generat.
* Descomprimeix el fiitxer decarregat: tar -xvzf file.tar.gz
* Executa l’instalador: sudo chmod +x setup.sh && ./setup.sh

# References[[edit](/pti/index.php?title=Categor%C3%ADa:Noogle&veaction=edit&section=5 "Edit section: References") | [edit source](/pti/index.php?title=Categor%C3%ADa:Noogle&action=edit&section=5 "Edit section: References")]

<https://github.com/polgs/noogle>