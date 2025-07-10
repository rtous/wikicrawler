[![](images/800px-Logo-blue.png)](/pti/index.php/File:Logo-blue.png)

Estructura del proyecto.

## Contents

* [1 Introducción](#Introducci.C3.B3n)
  + [1.1 ¿Qué es SmartID?](#.C2.BFQu.C3.A9_es_SmartID.3F)
* [2 Infraestructura](#Infraestructura)
  + [2.1 Blockchain](#Blockchain)
    - [2.1.1 Smart Contract](#Smart_Contract)
  + [2.2 Backend](#Backend)
    - [2.2.1 Ethereum](#Ethereum)
    - [2.2.2 IPFS](#IPFS)
    - [2.2.3 Infura](#Infura)
    - [2.2.4 Web3.js](#Web3.js)
  + [2.3 Frontend](#Frontend)
    - [2.3.1 React](#React)
    - [2.3.2 React Native](#React_Native)
    - [2.3.3 Metamask](#Metamask)
* [3 Entorno](#Entorno)
  + [3.1 Instalación](#Instalaci.C3.B3n)
    - [3.1.1 Metamask](#Metamask_2)
    - [3.1.2 React](#React_2)
    - [3.1.3 React Native](#React_Native_2)
    - [3.1.4 Remix](#Remix)
  + [3.2 Test](#Test)

# Introducción[[edit](/pti/index.php?title=Categor%C3%ADa:SmartID&veaction=edit&section=1 "Edit section: Introducción") | [edit source](/pti/index.php?title=Categor%C3%ADa:SmartID&action=edit&section=1 "Edit section: Introducción")]

## ¿Qué es SmartID?[[edit](/pti/index.php?title=Categor%C3%ADa:SmartID&veaction=edit&section=2 "Edit section: ¿Qué es SmartID?") | [edit source](/pti/index.php?title=Categor%C3%ADa:SmartID&action=edit&section=2 "Edit section: ¿Qué es SmartID?")]

Es prototipo de lo que tiene que ser el DNI del futuro el cual acabe con la burocracia, las colas en comisarías, seguridad social o ayuntamientos, que los datos de una persona estén seguros, y puedan ser accesibles en todo momento, desde cualquier parte del mundo, y para cualquier persona que lo necesite y esté autorizada.

# Infraestructura[[edit](/pti/index.php?title=Categor%C3%ADa:SmartID&veaction=edit&section=3 "Edit section: Infraestructura") | [edit source](/pti/index.php?title=Categor%C3%ADa:SmartID&action=edit&section=3 "Edit section: Infraestructura")]

La aplicación está compuesta por un frontend hecho en **React** para las páginas web y otro hecho en **React Native** para una APP para Smartphones, la cual hará llamadas a la red Blockchain Ethereum. La interface que autorizará las operaciones, proporcionará una API y mostrará la wallet del usuario será **Metamask**, una extensión del navegador. En el backend encontraremos la Blockchain **Ethereum** con su API, **IPFS** para almacenar los datos de mayor tamaño, **Infura** usada como puerta de enlace para todos los servicios distribuidos y **Web3.js**, un conjunto de librerías Javascript.

## Blockchain[[edit](/pti/index.php?title=Categor%C3%ADa:SmartID&veaction=edit&section=4 "Edit section: Blockchain") | [edit source](/pti/index.php?title=Categor%C3%ADa:SmartID&action=edit&section=4 "Edit section: Blockchain")]

Es una estructura de datos en que la información contenida se agrupa en conjuntos (bloques) a los que se les añade metainformaciones relativas a otro bloque de la cadena anterior en una línea temporal, de manera que gracias a técnicas criptográficas, la información contenida en un bloque solo puede ser repudiada o editada modificando todos los bloques posteriores.

### Smart Contract[[edit](/pti/index.php?title=Categor%C3%ADa:SmartID&veaction=edit&section=5 "Edit section: Smart Contract") | [edit source](/pti/index.php?title=Categor%C3%ADa:SmartID&action=edit&section=5 "Edit section: Smart Contract")]

Es un programa informático que facilita, asegura, hace cumplir y ejecuta acuerdos registrados entre dos o más partes.

Para realizar contratos inteligentes es necesario entrar en la página <https://remix.ethereum.org/>. Se programan con el lenguaje de alto nivel **Solidity** para realizar los contratos inteligentes

## Backend[[edit](/pti/index.php?title=Categor%C3%ADa:SmartID&veaction=edit&section=6 "Edit section: Backend") | [edit source](/pti/index.php?title=Categor%C3%ADa:SmartID&action=edit&section=6 "Edit section: Backend")]

### Ethereum[[edit](/pti/index.php?title=Categor%C3%ADa:SmartID&veaction=edit&section=7 "Edit section: Ethereum") | [edit source](/pti/index.php?title=Categor%C3%ADa:SmartID&action=edit&section=7 "Edit section: Ethereum")]

Es una plataforma de código abierto, descentralizada que permite la creación de acuerdos de contratos inteligentes entre pares, basada en el modelo blockchain.

### IPFS[[edit](/pti/index.php?title=Categor%C3%ADa:SmartID&veaction=edit&section=8 "Edit section: IPFS") | [edit source](/pti/index.php?title=Categor%C3%ADa:SmartID&action=edit&section=8 "Edit section: IPFS")]

Es un protocolo y una red diseñados para crear un método p2p direccionable por contenido para almacenar y compartir hipermedia en un sistema de archivos distribuidos.

### Infura[[edit](/pti/index.php?title=Categor%C3%ADa:SmartID&veaction=edit&section=9 "Edit section: Infura") | [edit source](/pti/index.php?title=Categor%C3%ADa:SmartID&action=edit&section=9 "Edit section: Infura")]

Es una API que sirve de puerta de enlace entre una APP con la red ethereum o con IPFS.

### Web3.js[[edit](/pti/index.php?title=Categor%C3%ADa:SmartID&veaction=edit&section=10 "Edit section: Web3.js") | [edit source](/pti/index.php?title=Categor%C3%ADa:SmartID&action=edit&section=10 "Edit section: Web3.js")]

Es una colección de bibliotecas que permiten interactuar con un nodo ethereum local o remoto, mediante una conexión HTTP o IPC.

## Frontend[[edit](/pti/index.php?title=Categor%C3%ADa:SmartID&veaction=edit&section=11 "Edit section: Frontend") | [edit source](/pti/index.php?title=Categor%C3%ADa:SmartID&action=edit&section=11 "Edit section: Frontend")]

### React[[edit](/pti/index.php?title=Categor%C3%ADa:SmartID&veaction=edit&section=12 "Edit section: React") | [edit source](/pti/index.php?title=Categor%C3%ADa:SmartID&action=edit&section=12 "Edit section: React")]

Es una biblioteca Javascript de código abierto diseñada para crear interfaces de usuario con el objetivo de facilitar el desarrollo de aplicaciones en una sola página.

### React Native[[edit](/pti/index.php?title=Categor%C3%ADa:SmartID&veaction=edit&section=13 "Edit section: React Native") | [edit source](/pti/index.php?title=Categor%C3%ADa:SmartID&action=edit&section=13 "Edit section: React Native")]

React Native es un framework quee permite construir aplicaciones móviles utilizando solamente JavaScript y React.

### Metamask[[edit](/pti/index.php?title=Categor%C3%ADa:SmartID&veaction=edit&section=14 "Edit section: Metamask") | [edit source](/pti/index.php?title=Categor%C3%ADa:SmartID&action=edit&section=14 "Edit section: Metamask")]

Es un plugin que hace de puente entre varias dapps y tu navegador sin comprometer tu seguridad, usando varias cuentas y sin necesidad de usar un nodo Ethereum completo.

# Entorno[[edit](/pti/index.php?title=Categor%C3%ADa:SmartID&veaction=edit&section=15 "Edit section: Entorno") | [edit source](/pti/index.php?title=Categor%C3%ADa:SmartID&action=edit&section=15 "Edit section: Entorno")]

## Instalación[[edit](/pti/index.php?title=Categor%C3%ADa:SmartID&veaction=edit&section=16 "Edit section: Instalación") | [edit source](/pti/index.php?title=Categor%C3%ADa:SmartID&action=edit&section=16 "Edit section: Instalación")]

### Metamask[[edit](/pti/index.php?title=Categor%C3%ADa:SmartID&veaction=edit&section=17 "Edit section: Metamask") | [edit source](/pti/index.php?title=Categor%C3%ADa:SmartID&action=edit&section=17 "Edit section: Metamask")]

Para instalar Metamask hay que ir a la página <https://metamask.io/> y descargarlo e instalarlo en tu navegador y crear una cuenta.

### React[[edit](/pti/index.php?title=Categor%C3%ADa:SmartID&veaction=edit&section=18 "Edit section: React") | [edit source](/pti/index.php?title=Categor%C3%ADa:SmartID&action=edit&section=18 "Edit section: React")]

Para instalar React hay que seguir los siguientes pasos (en Linux):

1. Para compilar e instalar complementos nativos desde npm, se necesita instalar herramientas de compilación:

```
    apt-get install -y build-essential

```

2. Descargar e instalar **Node.js**

```
    # En Ubuntu
    curl -sL https://deb.nodesource.com/setup_11.x | sudo -E bash -
    sudo apt-get install -y nodejs
    
    # En Debian, como root
    curl -sL https://deb.nodesource.com/setup_11.x | bash -
    apt-get install -y nodejs

```

3. Instalar **Create React App**

```
    npm install -g create-react-app

```

4. Crear una aplicación y lanzarla

```
    create-react-app nueva-app-react
    cd nueva-app-react
    npm start

```

### React Native[[edit](/pti/index.php?title=Categor%C3%ADa:SmartID&veaction=edit&section=19 "Edit section: React Native") | [edit source](/pti/index.php?title=Categor%C3%ADa:SmartID&action=edit&section=19 "Edit section: React Native")]

Para instalar React Native hay que seguir los siguientes pasos (en Linux):

1. Realizar los puntos (1) (2) de React (si no se han hecho antes).

2. Instalar **expo-cli**

```
    npm install -g expo-cli

```

3. Crear una aplicación y lanzarla

```
    expo init proyecto
    cd proyecto
    npm start

```

### Remix[[edit](/pti/index.php?title=Categor%C3%ADa:SmartID&veaction=edit&section=20 "Edit section: Remix") | [edit source](/pti/index.php?title=Categor%C3%ADa:SmartID&action=edit&section=20 "Edit section: Remix")]

1. Ir a Remix y cargar los archivos .sol en la carpeta de Smart Contract.

2. Seleccionar la versión del compilador: 0.4.22+commit.4cb486ee y haga clic en Start para compilar.

3. Vaya a la pestaña Ejecutar y asegúrese de tener la siguiente configuración:

```
    Environment: Injected Web3 (Ropsten)
    Account: Select your account address
    Gas limit: 3000000
    Value: 0

```

4. En el menú desplegable, asegúrese de que se haya seleccionado CitizensRecord (un ejemplo de nuestro smart Contract) y haga clic en deploy.

5. Haga clic en la dirección del nuevo contrato para copiarlo en el portapapeles.

## Test[[edit](/pti/index.php?title=Categor%C3%ADa:SmartID&veaction=edit&section=21 "Edit section: Test") | [edit source](/pti/index.php?title=Categor%C3%ADa:SmartID&action=edit&section=21 "Edit section: Test")]

Ir a <http://localhost:3000>