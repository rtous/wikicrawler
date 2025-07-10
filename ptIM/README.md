## Contents

* [1 Projecte ptIM](#Projecte_ptIM)
  + [1.1 1. Resum del projecte](#1._Resum_del_projecte)
  + [1.2 2. Tecnologies](#2._Tecnologies)
    - [1.2.1 Hardware Servidor](#Hardware_Servidor)
    - [1.2.2 Software Servidor](#Software_Servidor)
    - [1.2.3 Client Android](#Client_Android)
  + [1.3 Fotografies d'exemple](#Fotografies_d.27exemple)
    - [1.3.1 Exemple del llistat dels contactes](#Exemple_del_llistat_dels_contactes)
    - [1.3.2 Exemple de conversa entre dos contactes](#Exemple_de_conversa_entre_dos_contactes)

# Projecte ptIM[[edit](/pti/index.php?title=Categor%C3%ADa:ptIM&veaction=edit&section=1 "Edit section: Projecte ptIM") | [edit source](/pti/index.php?title=Categor%C3%ADa:ptIM&action=edit&section=1 "Edit section: Projecte ptIM")]

[![PtIM Logo.png](images/PtIM\_Logo.png)](/pti/index.php/File:PtIM_Logo.png)

**PTIM és un client de missatgeria instantània que busca proporcionar seguretat i privacitat als usuaris que cada cop estan més conscienciats del perill del núvol.**

## 1. Resum del projecte[[edit](/pti/index.php?title=Categor%C3%ADa:ptIM&veaction=edit&section=2 "Edit section: 1. Resum del projecte") | [edit source](/pti/index.php?title=Categor%C3%ADa:ptIM&action=edit&section=2 "Edit section: 1. Resum del projecte")]

Com a principal objectiu d’aquest projecte s’ha tingut la màxima de proporcionar seguretat davant de qualsevol altre funcionalitat o característica de l’aplicació. Això fa que es tingui un sistema sòlid i escalable, tant a nivell d’usuaris com de desenvolupament, podent deixar com a secundari, però mai oblidat, la interfície gràfica o funcionalitats no crítiques. Com a extrapolació, hi ha l’exemple dels smartphones, la capacitat de la bateria i el tamany de la pantalla i grossor. Durant els últims 2 anys els fabricants han decidit que el que demandaven els usuaris era telèfons més prims i llargs i que en cap cas importava la bateria. Avui, amb smartphones de fins a 8” (Phablets) encara es funciona amb bateries amb tecnologia de fa més de 5 anys i autonomies d’un dia a tot estirar per un ús corrent.

Es podria arribar a concloure que aquesta premissa, més seguretat enfront comoditat, no és correcta vist l’èxit d’aplicacions com Whatsapp [0], la qual ha estat incontables vegades demostrada com a insegura[1]. També es pot copsar que el sistema de pagament ha mermat molt fortament les dades de whatsapp a favor d’altres solucions gratuïtes tals com LINE. És per això que s’ha optat per seguir una línia de treball enfocada a maximitzar la seguretat i confort. L’usuari pot no percebre-ho, ja que tota la feina es fa internament i transparent a aquest, però que farà que l’aplicació obtingui realment un afegit i garantia de qualitat enfront els rivals.

A partir d’això es pot concloure que tota aplicació té el seu públic o sector al qual està dirigit. PTIM està enfocat a aquell públic exigent que requereix uns mínims de seguretat, privacitat i professionalitat a l’hora de triar qui tractarà informació tant preuada i valuosa per aquest, com són les converses privades. Això, no obstant, no vol dir que vagi dirigit a un públic concret o limitat, ja que PTIM està desenvolupada per a ser agradable i agraïda d’usar, amb un sistema molt senzill de configuració i un sistema de seguretat en nivells molt senzill d’entendre, fent de PTIM una solució òptima per a tots els públics.

PTIM farà servir bases de dades no relacionals (Cassandra) per augmentar la seva escalabilitat de manera més ràpida, sacrificant la consistència en les seves instàncies de bases de dades.

## 2. Tecnologies[[edit](/pti/index.php?title=Categor%C3%ADa:ptIM&veaction=edit&section=3 "Edit section: 2. Tecnologies") | [edit source](/pti/index.php?title=Categor%C3%ADa:ptIM&action=edit&section=3 "Edit section: 2. Tecnologies")]

[![PtIM Estructura.png](images/PtIM\_Estructura.png)](/pti/index.php/File:PtIM_Estructura.png)

### Hardware Servidor[[edit](/pti/index.php?title=Categor%C3%ADa:ptIM&veaction=edit&section=4 "Edit section: Hardware Servidor") | [edit source](/pti/index.php?title=Categor%C3%ADa:ptIM&action=edit&section=4 "Edit section: Hardware Servidor")]

* Amazon Web Services EC2 - Free
* Ubuntu 12.04 LTS Version
* ~1GHz de CPU
* 613 MB RAM (~100MB disponibles)
* SWAP no possible

### Software Servidor[[edit](/pti/index.php?title=Categor%C3%ADa:ptIM&veaction=edit&section=5 "Edit section: Software Servidor") | [edit source](/pti/index.php?title=Categor%C3%ADa:ptIM&action=edit&section=5 "Edit section: Software Servidor")]

* Apache Tomcat
* Servlets Java Multithreading
* REST
* JSON
* HTTPS
* RSA Keys Syncronization
* Javax-Mail
* Apache Cassandra No-SQL
* API interna Cassandra

### Client Android[[edit](/pti/index.php?title=Categor%C3%ADa:ptIM&veaction=edit&section=6 "Edit section: Client Android") | [edit source](/pti/index.php?title=Categor%C3%ADa:ptIM&action=edit&section=6 "Edit section: Client Android")]

* API 10 (A partir d'Android 2.3.3)
* MultiThreading
* REST
* HTTPS
* JSON
* Encriptació RSA
* SQLite com a gestor d'informació local
* Converses ".ptIM"

## Fotografies d'exemple[[edit](/pti/index.php?title=Categor%C3%ADa:ptIM&veaction=edit&section=7 "Edit section: Fotografies d'exemple") | [edit source](/pti/index.php?title=Categor%C3%ADa:ptIM&action=edit&section=7 "Edit section: Fotografies d'exemple")]

### Exemple del llistat dels contactes[[edit](/pti/index.php?title=Categor%C3%ADa:ptIM&veaction=edit&section=8 "Edit section: Exemple del llistat dels contactes") | [edit source](/pti/index.php?title=Categor%C3%ADa:ptIM&action=edit&section=8 "Edit section: Exemple del llistat dels contactes")]

[![Contactes ptim.png](images/Contactes\_ptim.png)](/pti/index.php/File:Contactes_ptim.png)

### Exemple de conversa entre dos contactes[[edit](/pti/index.php?title=Categor%C3%ADa:ptIM&veaction=edit&section=9 "Edit section: Exemple de conversa entre dos contactes") | [edit source](/pti/index.php?title=Categor%C3%ADa:ptIM&action=edit&section=9 "Edit section: Exemple de conversa entre dos contactes")]

[![Conversa ptIM.PNG](images/Conversa\_ptIM.PNG)](/pti/index.php/File:Conversa_ptIM.PNG)