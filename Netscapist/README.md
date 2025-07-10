## Contents

* [1 Projecte Netscapist](#Projecte_Netscapist)
  + [1.1 1. Introducció](#1._Introducci.C3.B3)
    - [1.1.1 Objectius projecte](#Objectius_projecte)
  + [1.2 2. Esquema general del sistema](#2._Esquema_general_del_sistema)
  + [1.3 3. Disseny del sistema](#3._Disseny_del_sistema)
    - [1.3.1 Libnetscapist](#Libnetscapist)
  + [1.4 4. Referència](#4._Refer.C3.A8ncia)

# Projecte Netscapist[[edit](/pti/index.php?title=Categor%C3%ADa:Netscapist&veaction=edit&section=1 "Edit section: Projecte Netscapist") | [edit source](/pti/index.php?title=Categor%C3%ADa:Netscapist&action=edit&section=1 "Edit section: Projecte Netscapist")]

## 1. Introducció[[edit](/pti/index.php?title=Categor%C3%ADa:Netscapist&veaction=edit&section=2 "Edit section: 1. Introducció") | [edit source](/pti/index.php?title=Categor%C3%ADa:Netscapist&action=edit&section=2 "Edit section: 1. Introducció")]

La idea principal del projecte en breus paraules és aconseguir una connexió entre un client (host) i un servidor a través de missatges ICMPv4 (el tipus de paquets que utilitza el “ping” en xarxes IPv4). Aquesta comunicació s’utilitzarà per poder-se connectar a internet, és a dir, el client rep una petició http (per exemple) aquest li envia al server a través de missatges ICMP, el server tracta la petició i retorna el resultat amb totes les dades cap al client.

### Objectius projecte[[edit](/pti/index.php?title=Categor%C3%ADa:Netscapist&veaction=edit&section=3 "Edit section: Objectius projecte") | [edit source](/pti/index.php?title=Categor%C3%ADa:Netscapist&action=edit&section=3 "Edit section: Objectius projecte")]

1. Aconseguir connexió via ICMP paquets entre client - servidor
2. Re-dirigir tot el tràfic del navegador a un proxy dins el client
3. Algoritme de encapsular i desencapsular paquets ICMP i separar la informació.
4. Acceptar protocols HTTP (GET i POST) i HTTPS
5. Muntar tot el sistema com un Framework, de tal forma que sigui fàcil aprofitar les classes perquè la gent pugui continuar el projecte.
6. Aconseguir que funcioni en una situació real.
7. Permetre configuracions amb múltiples clients

## 2. Esquema general del sistema[[edit](/pti/index.php?title=Categor%C3%ADa:Netscapist&veaction=edit&section=4 "Edit section: 2. Esquema general del sistema") | [edit source](/pti/index.php?title=Categor%C3%ADa:Netscapist&action=edit&section=4 "Edit section: 2. Esquema general del sistema")]

[![Esquema\_netscapist](images/Esquema\_netscapist.PNG)](/pti/index.php/File:Esquema_netscapist.PNG "Esquema_netscapist")

## 3. Disseny del sistema[[edit](/pti/index.php?title=Categor%C3%ADa:Netscapist&veaction=edit&section=5 "Edit section: 3. Disseny del sistema") | [edit source](/pti/index.php?title=Categor%C3%ADa:Netscapist&action=edit&section=5 "Edit section: 3. Disseny del sistema")]

### Libnetscapist[[edit](/pti/index.php?title=Categor%C3%ADa:Netscapist&veaction=edit&section=6 "Edit section: Libnetscapist") | [edit source](/pti/index.php?title=Categor%C3%ADa:Netscapist&action=edit&section=6 "Edit section: Libnetscapist")]

Contingut:

● IP class: conté l’estructura i les funcions per gestionar els paquets IP

● ICMP class: conté l’estructura i les funcions per gestionar els paquets ICMP

● PingServer class: conté l’estructura del server i les funcions necessàries perquè funcioni el sistema. Escolta i respon les peticions del client.

● Proxy class: conté la estructura del client i les funcions necessàries perquè funcioni el sistema. Crea el proxy per rebre les peticions del navegador, envia i rep peticions al server.

● TunnelEndPoint class: superclasse que conté funcions comunes del proxy i el server, comunica també amb el Networknode.

● Networknode class: classe que conté la estructura de la xarxa i les funcions per enviar paquets ICMP.

## 4. Referència[[edit](/pti/index.php?title=Categor%C3%ADa:Netscapist&veaction=edit&section=7 "Edit section: 4. Referència") | [edit source](/pti/index.php?title=Categor%C3%ADa:Netscapist&action=edit&section=7 "Edit section: 4. Referència")]

[Memòria projecte Netscapist](/pti/images/b/b1/PTI-_Netscapist.pdf "PTI- Netscapist.pdf")