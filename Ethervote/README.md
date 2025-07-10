## Contents

* [1 ¿Qué es Ethervote?](#.C2.BFQu.C3.A9_es_Ethervote.3F)
* [2 Infraestructura](#Infraestructura)
* [3 Blockchain](#Blockchain)
  + [3.1 Smart-Contract](#Smart-Contract)
* [4 Backend](#Backend)
* [5 Frontend](#Frontend)
* [6 Infraestructura](#Infraestructura_2)
* [7 Tests](#Tests)
  + [7.1 Truffle](#Truffle)
  + [7.2 Programació dels tests](#Programaci.C3.B3_dels_tests)
  + [7.3 Exmples](#Exmples)
  + [7.4 Altres considerecions sobre truffle](#Altres_considerecions_sobre_truffle)

## ¿Qué es Ethervote?[[edit](/pti/index.php?title=Categor%C3%ADa:Ethervote&veaction=edit&section=1 "Edit section: ¿Qué es Ethervote?") | [edit source](/pti/index.php?title=Categor%C3%ADa:Ethervote&action=edit&section=1 "Edit section: ¿Qué es Ethervote?")]

Ethervote és un projecte que té com a objectiu posar a disposició de la comunitat una plataforma de votació fàcilment accessible i que a la vegada sigui segura, utilitzant la tecnologia blockchain per aconseguir-ho.

# Infraestructura[[edit](/pti/index.php?title=Categor%C3%ADa:Ethervote&veaction=edit&section=2 "Edit section: Infraestructura") | [edit source](/pti/index.php?title=Categor%C3%ADa:Ethervote&action=edit&section=2 "Edit section: Infraestructura")]

L'aplicació estarà composta per un frontend escrit en React, el qual farà les crides cap a la Blockchain d'Ethereum. L'interfície que autoritzarà les operacions, proporcionarà una API i mostrarà la wallet del usuari serà Metamask, una extensió del navegador. Al backend trobarem la Blockchain d'Ethereum amb la seva API i un petit servidor Express de NodeJS per emmagatzemar alguna informació persistent. Tot això estarà empaquetat en un contenidor docker que podrà ser executat en plataformes com Kubernetes.

# Blockchain[[edit](/pti/index.php?title=Categor%C3%ADa:Ethervote&veaction=edit&section=3 "Edit section: Blockchain") | [edit source](/pti/index.php?title=Categor%C3%ADa:Ethervote&action=edit&section=3 "Edit section: Blockchain")]

Podem definir Blockchain com una base de dades distribuïda que permet registrar i compartir informació dins d’una comunitat. Per a això crea un llibre de comptabilitat de les transaccions digitals compartit dins d'una xarxa distribuïda d'ordinadors.
Nosaltres fem servir Etherum i Solidity per l'smart-contract..

## Smart-Contract[[edit](/pti/index.php?title=Categor%C3%ADa:Ethervote&veaction=edit&section=4 "Edit section: Smart-Contract") | [edit source](/pti/index.php?title=Categor%C3%ADa:Ethervote&action=edit&section=4 "Edit section: Smart-Contract")]

El nostre smart-contract serà la lògica que processarà les diferents votacions. afegir nous usuaris, etc.

Hem definit una sèrie d'estructures de dades per emmagatzemar: el cens, les propostes a votar, els vots, i totes les seves metadades. A través de funcions com: Vote, addVoter, getNumProposals, entre d'altres i una llibreria com Web3 podrem interactuar amb el contracte desde qualsevol lloc.

# Backend[[edit](/pti/index.php?title=Categor%C3%ADa:Ethervote&veaction=edit&section=5 "Edit section: Backend") | [edit source](/pti/index.php?title=Categor%C3%ADa:Ethervote&action=edit&section=5 "Edit section: Backend")]

El backend de l’aplicació està programat amb NodeJS. Node és un entorn de servidor per a JavaScript que permet fer operacions d’entrada i sortida de manera asíncrona que treballa amb mòduls (equivalents a llibreries de JavaScript).

# Frontend[[edit](/pti/index.php?title=Categor%C3%ADa:Ethervote&veaction=edit&section=6 "Edit section: Frontend") | [edit source](/pti/index.php?title=Categor%C3%ADa:Ethervote&action=edit&section=6 "Edit section: Frontend")]

Teníem la necessitat de proporcionar l'usuari una plataforma d'interacció amb l'aplicació on es produís una abstracció completa de les funcions pròpies de smart-contract.
Vam escollir la llibreria React per realitzar-lo.

# Infraestructura[[edit](/pti/index.php?title=Categor%C3%ADa:Ethervote&veaction=edit&section=7 "Edit section: Infraestructura") | [edit source](/pti/index.php?title=Categor%C3%ADa:Ethervote&action=edit&section=7 "Edit section: Infraestructura")]

A la part d'infraestructura hem utilitzat Kubernetes,tot i no ser un component essencial de l'aplicació ethervote, des d'un primer moment ens va semblar una tecnologia amb unes característiques molt interessants i per això és part del projecte.

# Tests[[edit](/pti/index.php?title=Categor%C3%ADa:Ethervote&veaction=edit&section=8 "Edit section: Tests") | [edit source](/pti/index.php?title=Categor%C3%ADa:Ethervote&action=edit&section=8 "Edit section: Tests")]

Aquesta part està centralitzada, no en probar el funcionament correcte de tota l'aplicació, sinó de probar el que és purament blockchain, el Smart Contract. Això es va decidir per varies raons, la fonamental és perqué al ser una tecnòlogia nova, que té bugs i que no haviem utilitzat mai, ens haviem d'assegurar que funcionava correctament per tal de no programar a cegues la resta del projecte.

## Truffle[[edit](/pti/index.php?title=Categor%C3%ADa:Ethervote&veaction=edit&section=9 "Edit section: Truffle") | [edit source](/pti/index.php?title=Categor%C3%ADa:Ethervote&action=edit&section=9 "Edit section: Truffle")]

Truffle suite és una eina molt potent que ens permet fer probes a un o més smart contract a la vegada, sent el punt de comunicació amb la blockchain.

Truffle conté una carpeta amb els smart contracts que volem probar i un adicional anomentat *Migrations.sol* el qual serveix com a controlador de versions dels *scripts* utilitzats quan executem el nostre test. Les *migracions* són aquests petits \textit{scripts} que ajuden a afegir els nous canvis fets al smart contract a la blockchain. A més hi ha la carpeta *test* que com el seu nom indica, conté els tests.

## Programació dels tests[[edit](/pti/index.php?title=Categor%C3%ADa:Ethervote&veaction=edit&section=10 "Edit section: Programació dels tests") | [edit source](/pti/index.php?title=Categor%C3%ADa:Ethervote&action=edit&section=10 "Edit section: Programació dels tests")]

Per poder fer els tests necessitem importar el nostre contracte utilitzant la funció *require* de la següent manera al principi del nostre File:

```
    const Ethervote = artifacts.require('./ethervote.sol')

```

Seguidament instanciarem el contracte on pasarem com a paràmetre el contracte importat i una funció que contindrà tots els tests que volguem que passi aquell contracte:

```
    contract('Ethervote', function(accounts) {  })

```

El paràmetre *accounts* és un array que es passa a la funció que conté 10 comptes de la blockchain especials per fer tests carregats amb *ether*, que és el que es consumeix quan s'executen funcions o transaccions a la xarxa. Aquesta xarxa per fer tests juntament amb les comptes s'aconsegueix amb l'eina *ganache-cli* comentada anteriorment.

Per programar els diferents tests necessitem que per a cadascún, el contracte estigui inicialitzat de nou per evitar arrosegar errors entre tests i així aconseguir un certa independència d'uns dels altres. Això s'aconsegueix amb:

```
    beforeEach('setup contract for each test', async function () {
         ethervote = await Ethervote.new("organitzacio test", 300)
        })}

```

Per programar tenim la funció *it* on se li passen dos paràmetres, el primer és el nom que li volem donar al test, normalment és posarà algun nom que fagi referència al que estem provant, i el segón es una funció que dins tindrà les crides al contracte i càlculs.

## Exmples[[edit](/pti/index.php?title=Categor%C3%ADa:Ethervote&veaction=edit&section=11 "Edit section: Exmples") | [edit source](/pti/index.php?title=Categor%C3%ADa:Ethervote&action=edit&section=11 "Edit section: Exmples")]

**Exemple funcionament:**

```
    it('has an owner', async function() {
       assert.equal(await ethervote.owner(), owner_address)
    })

```

Aquest petits exmple mostra un petit test on es comprova que la crida cap a la blockchain per saber qui és el propietari es igual al propietari definit com a *owner\_address* (*accounts[0]*);

**Exmple més avançat:**

```
   it('create proposal', async function() {
       var name = "proposal_test_1"
       var description = "First proposal test description"
       await ethervote.addVoter(voter_1, 2, {from: owner_address})
       await ethervote.newProposal(name, description, {from: voter_1})
       var res = await ethervote.getNumberOfProposals()
       assert.equal(res, 1)
       var name_p = await ethervote.getProposalName(1)
       assert.equal(name, name_p)
       var description_p = await ethervote.getProposalDescription(1)
       assert.equal(description, description_p)
   })

```

En aquest exemple primer de tot el propietari de l'enquesta afegirà un votant, el qual té el privilegi per poder crear una nova enquesta. Després de crearla, mirem si el número de enquestes ha aungmentat (*getNumberOfProposals()*) i mirem si s'ha creat correctament amb el nom i la descripció indicada en la seva creació.

## Altres considerecions sobre truffle[[edit](/pti/index.php?title=Categor%C3%ADa:Ethervote&veaction=edit&section=12 "Edit section: Altres considerecions sobre truffle") | [edit source](/pti/index.php?title=Categor%C3%ADa:Ethervote&action=edit&section=12 "Edit section: Altres considerecions sobre truffle")]

Actualment, al ser tot això en general, una tecnologia bastant nova hi han molts errors. En truffle no és diferent, hi han opcions que estan bug, com per exmple el debugger. A més, molts errors que retorna a l'hora de compilar no són prou descriptives cosa que fa que es perdi bastant temps en buscar informació i exemples per webs externes a la oficial de truffle.