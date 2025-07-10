## Contents

* [1 ¿Què és MasterChef?](#.C2.BFQu.C3.A8_.C3.A9s_MasterChef.3F)
* [2 Tecnologia utilitzada](#Tecnologia_utilitzada)
  + [2.1 Chef](#Chef)
  + [2.2 Terraform](#Terraform)
  + [2.3 API](#API)
* [3 Com funciona el nostre servei de desplegament d'infraestructura i software?](#Com_funciona_el_nostre_servei_de_desplegament_d.27infraestructura_i_software.3F)

## ¿Què és MasterChef?[[edit](/pti/index.php?title=Categor%C3%ADa:Masterchef&veaction=edit&section=1 "Edit section: ¿Què és MasterChef?") | [edit source](/pti/index.php?title=Categor%C3%ADa:Masterchef&action=edit&section=1 "Edit section: ¿Què és MasterChef?")]

MasterChef és una empresa que s'encarrega de l'administració dels sistemes i que dins dels serveis que ofereix té el de desplegament d'infraestructures i software en un temps mínim i el manteniment constant d'aquest amb les versions més noves de programari sense la necessitat de preocupar-se. Això proporciona un nivell de seguretat molt alt que pot cobrir els buits de seguretat que hi ha als sistemes desactualitzats.
Gràcies a l'utilització del programari Terraform i Chef i de les seves eines podem oferir als nostres clients el millor servei possible.

## Tecnologia utilitzada[[edit](/pti/index.php?title=Categor%C3%ADa:Masterchef&veaction=edit&section=2 "Edit section: Tecnologia utilitzada") | [edit source](/pti/index.php?title=Categor%C3%ADa:Masterchef&action=edit&section=2 "Edit section: Tecnologia utilitzada")]

La tecnologia utilitzada en el nostre projecte es basa en:

* Chef: s'utilitza pel desplegament de programari en les diferents infraestructures creades.

* Terraform: aplicació que serveix per desplegar les màquines de forma fàcil i automatitzada. Té l'avantatge de ser compatible amb els principals cloud servers(AWS, Google Cloud, Azure).

* Google Cloud: plataforma cloud que utilitza MasterChef, es basa principalment en l'ús de Compute Engine per realitzar el deploy de les màquines. Es connecta amb Terraform per poder automatitzar el deploy.

* API: una API utilitzada per al processament de les dades rebudes per les execucions de Chef.

### Chef[[edit](/pti/index.php?title=Categor%C3%ADa:Masterchef&veaction=edit&section=3 "Edit section: Chef") | [edit source](/pti/index.php?title=Categor%C3%ADa:Masterchef&action=edit&section=3 "Edit section: Chef")]

Chef és una tecnologia de gestió de la configuració que s'utilitza per automatitzar l'aprovisionament d'infraestructura. Està desenvolupat sobre llenguatge Ruby DSL, un llenguatge declaratiu. S'utilitza per agilitzar la tasca de configuració i gestió dels servidors de les empreses. Té la capacitat d'integrar-se amb qualsevol tecnologia al núvol (AWS, Azure, Google Cloud).

### Terraform[[edit](/pti/index.php?title=Categor%C3%ADa:Masterchef&veaction=edit&section=4 "Edit section: Terraform") | [edit source](/pti/index.php?title=Categor%C3%ADa:Masterchef&action=edit&section=4 "Edit section: Terraform")]

Programari de HashiCorp utilitzat per poder realitzar el deploy de les màquines. Per al nostre projecte ens hem unit amb el proveïdor de cloud de Google. D'aquesta manera ens assegurem tenir màquines amb molta o poca potència depenent de les necessitats dels nostres clients.
Gràcies a la potència de Terraform podem configurar la màquina de infinitats de formes, podent modificar coses tan simples com el tipus de màquina (memòria ram i processadors que utilitzarà) fins modificar regles de firewall, crear noves xarxes dins de Google Cloud o fins i tot crear el nostre propi firewall.

### API[[edit](/pti/index.php?title=Categor%C3%ADa:Masterchef&veaction=edit&section=5 "Edit section: API") | [edit source](/pti/index.php?title=Categor%C3%ADa:Masterchef&action=edit&section=5 "Edit section: API")]

La funció de l'API és recopilar els logs de les execucions de Chef, emmagatzemar-los i poder-los processar adequadament. Poder emmagatzemar i processar els outputs dels processos de forma automàtica ens permet obtenir un valor afegit adicional i ens proporciona vàries funcionalitats extres, com el control d’errors, la filtració d’informació rellevant, un històric de processos executats, etc.

## Com funciona el nostre servei de desplegament d'infraestructura i software?[[edit](/pti/index.php?title=Categor%C3%ADa:Masterchef&veaction=edit&section=6 "Edit section: Com funciona el nostre servei de desplegament d'infraestructura i software?") | [edit source](/pti/index.php?title=Categor%C3%ADa:Masterchef&action=edit&section=6 "Edit section: Com funciona el nostre servei de desplegament d'infraestructura i software?")]

Donarem servei de la següent manera:

Un client ens demana un servei necessari que es pot replicar fàcilment com pot, per exemple, ser dos servidor web de Nginx, dos servidors davant d'ambdós Nginx corrent Varnish i finalment dos balançejadors de càrrega com Haproxys que distribueixin la carrega entre els dos Varnish. En definitiva, un web en Nginx que tingui alta disponibilitat (HA).

Primer de tot, mitjançant un script de Terraform, creariem les sis màquines objectiu amb els recursos mínims per poder mantenir les necessitats de l'usuari i aquestes es crearàn en la nostra plataforma de Google Cloud. Amb això ja tindirem la part d'infraestructura creada, el que ens portaria més de 1 hora el desplegar i configurar cada servidor manualment nosaltres ho faiem en menys de 15 minuts.

Seguidament, des de la màquina workstation de Chef haurem d'instal·lar els cookbooks amb les configuracions pertinents en les màquines clients perquè puguin tenir tant Nginx, com Varnish, com Haproxy actualitzats en tot moment. El software s'instal·laria en els servidors corresponents i només acabar l'execució de totes les comandes, en menys de 10 minuts, tindriem tot el programari instal·lat i funcionant.

D'aquesta manera tenim totes les máquines amb el programari constantment actualitzat sense necessitat que l'usuari final hagi d'intervenir. Amb això reduïm temps i cost de mà d'obra per a les empreses perquè es tracta d'un procés molt automatitzat i lliure d'errors humans.
A més a més el desplegament de tot el programari en condicions normals i sense fer servir un sistema d'automatització ens portaria més de 4 hores sense problema, ja que sempre s'ha de passar un QA per tal de veure que tot funciona correctament. En canvi, utilitzant el software mencionat ho podem fer en menys de 30 minuts i amb la certesa de que tot estarà funcionant correctament ja que són idempotents.

També podriem veure els outputs de l'execució en la nostre API de manera que podriem veure si totes les característiques de les màquines objectiu són les desitjades.