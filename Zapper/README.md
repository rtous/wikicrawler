## Contents

* [1 Zapper: Connecta amb la gent!](#Zapper:_Connecta_amb_la_gent.21)
* [2 Arquitectura i tecnologies](#Arquitectura_i_tecnologies)
  + [2.1 Front-end](#Front-end)
  + [2.2 Back-end](#Back-end)
  + [2.3 WebApp](#WebApp)
  + [2.4 Infraestructura](#Infraestructura)
* [3 Aplicació mòbil](#Aplicaci.C3.B3_m.C3.B2bil)

# Zapper: Connecta amb la gent![[edit](/pti/index.php?title=Categor%C3%ADa:Zapper&veaction=edit&section=1 "Edit section: Zapper: Connecta amb la gent!") | [edit source](/pti/index.php?title=Categor%C3%ADa:Zapper&action=edit&section=1 "Edit section: Zapper: Connecta amb la gent!")]

***Zapper**, la nova aplicació per potenciar les relacions socials amb les persones que t'envolten.*

[![](images/250px-Zapper\_logo.png)](/pti/index.php/File:Zapper_logo.png)

Zapper logo.

Aquesta és la filosofia amb la qual hem pensat el nostre projecte, donada una necessitat que creiem que és d'actualitat a la nostra societat. Concretament, identifiquem que a les nostres vides les xarxes socials són un element de vital importància en les interaccions interpersonals. No obstant això, moltes vegades resulta vergonyós preguntar pels perfils després de conèixer algú, o bé resulta impossible arribar a tothom en un esdeveniment massiu.

En aquestes situacions és on entra **Zapper**, la nostra aplicació permetrà a cada usuari crear el seu propi perfil, on podrà compartir les xarxes socials que desitgi. Aquestes es compartiran amb els altres usuaris mitjançant geolocalització, és a dir, el perfil apareixerà a la interfície d'aquells que es trobin presencialment propers.
D'aquesta manera es crearà una xarxa en una determinada zona, on tots els implicats tindran accés a les xarxes compartides pels altres, donant solució al problema mencionat anteriorment.

**Zapper**, es basa en l'ús de la geolocalització. Mitjançant aquesta eina, l'usuari podrà veure en un mapa en temps real (o cada petits intervals de temps) quins altres usuaris apareixen en el seu radi de posició. Si l'aplicació mostra que un altre usuari es troba dins del radi, aquesta li oferirà a l'usuari la possibilitat de visualitzar el seu perfil.

# Arquitectura i tecnologies[[edit](/pti/index.php?title=Categor%C3%ADa:Zapper&veaction=edit&section=2 "Edit section: Arquitectura i tecnologies") | [edit source](/pti/index.php?title=Categor%C3%ADa:Zapper&action=edit&section=2 "Edit section: Arquitectura i tecnologies")]

L’arquitectura es divideix en tres seccions:

### Front-end[[edit](/pti/index.php?title=Categor%C3%ADa:Zapper&veaction=edit&section=3 "Edit section: Front-end") | [edit source](/pti/index.php?title=Categor%C3%ADa:Zapper&action=edit&section=3 "Edit section: Front-end")]

Aplicació multiplataforma, fa de client a l’arquitectura. És el component més important del model, ja que és la interfície amb l’usuari.
Desenvolupada en **React Native** pel seu suport a multiplataforma, gran comunitat, molta documentació disponible, facilitat alhora d’integrar APIs, etc…

### Back-end[[edit](/pti/index.php?title=Categor%C3%ADa:Zapper&veaction=edit&section=4 "Edit section: Back-end") | [edit source](/pti/index.php?title=Categor%C3%ADa:Zapper&action=edit&section=4 "Edit section: Back-end")]

Usarem contenidors **Docker** per executar les nostres aplicacions al back-end, administrades per **Kubernetes**. Son tres les aplicacions que hem desenvolupat:

* **API**: desenvolupada amb **ExpressJS** i **NodeJS**.
* **Base de dades**: usarem **MongoDB** per la seva fàcil integració amb l’API.

### WebApp[[edit](/pti/index.php?title=Categor%C3%ADa:Zapper&veaction=edit&section=5 "Edit section: WebApp") | [edit source](/pti/index.php?title=Categor%C3%ADa:Zapper&action=edit&section=5 "Edit section: WebApp")]

Es tracta d’una senzilla landing page. Pel que usarem **NextJS**, que permet fer projectes atractius visualment i lleugers de dependències.

### Infraestructura[[edit](/pti/index.php?title=Categor%C3%ADa:Zapper&veaction=edit&section=6 "Edit section: Infraestructura") | [edit source](/pti/index.php?title=Categor%C3%ADa:Zapper&action=edit&section=6 "Edit section: Infraestructura")]

La infraestructura sencera es gestionarà amb **Kubernetes**, concretament amb un cluster **K3S**.

[![](images/600px-Zapper\_arch.png)](/pti/index.php/File:Zapper_arch.png)

Arquitectura del projecte.

[![](images/600px-Zapper\_cluster.png)](/pti/index.php/File:Zapper_cluster.png)

Arquitectura de Kubernetes.

# Aplicació mòbil[[edit](/pti/index.php?title=Categor%C3%ADa:Zapper&veaction=edit&section=7 "Edit section: Aplicació mòbil") | [edit source](/pti/index.php?title=Categor%C3%ADa:Zapper&action=edit&section=7 "Edit section: Aplicació mòbil")]

Una app multiplataforma intuïtiva i amigable permet a l'usuari veure en tot moment la gent que l'envolta. Tu decideixes quan compartir la teva ubicació actual i veure qui està a prop teu. És a dir, quan es prem el botó de **ZAP**, l'aplicació envia la teva localització al back-end i aquest respon al front-end amb els usuaris propers.

Amb la funció de llista, pots veure els usuaris en qüestió i saltar ràpidament a les seves xarxes socials.

[![](images/400px-Zapper\_appgrid.png)](/pti/index.php/File:Zapper_appgrid.png)

Aplicació mòbil

Descobreix l'app mitjançant una web corporativa. Coneix **Zapper** i descarrega l'aplicació amb aquesta senzilla i minimalista landing page.

[![](images/300px-Zapper\_web.png)](/pti/index.php/File:Zapper_web.png)

Landing page.