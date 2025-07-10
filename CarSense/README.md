## Contents

* [1 Introduction](#Introduction)
  + [1.1 Why is CarSense needed?](#Why_is_CarSense_needed.3F)
  + [1.2 Technologies used](#Technologies_used)
* [2 Hardware device](#Hardware_device)
  + [2.1 Different possibilities and specs](#Different_possibilities_and_specs)
  + [2.2 Why the one chosen?](#Why_the_one_chosen.3F)
  + [2.3 Configuration](#Configuration)
* [3 Server](#Server)
  + [3.1 Providers](#Providers)

# Introduction[[edit](/pti/index.php?title=Categor%C3%ADa:CarSense&veaction=edit&section=1 "Edit section: Introduction") | [edit source](/pti/index.php?title=Categor%C3%ADa:CarSense&action=edit&section=1 "Edit section: Introduction")]

## Why is CarSense needed?[[edit](/pti/index.php?title=Categor%C3%ADa:CarSense&veaction=edit&section=2 "Edit section: Why is CarSense needed?") | [edit source](/pti/index.php?title=Categor%C3%ADa:CarSense&action=edit&section=2 "Edit section: Why is CarSense needed?")]

Nowadays, most of the new cars include mobile applications that allow users to control some of their vehicle’s parameters and other functionalities, such as geolocation services. Despite this, older cars or even newer ones with limited technology don’t provide these services.

Since this type of functionality can be very useful to people who share their cars or even to a unique user, CarSense aims to create an affordable and easy to use alternative.

There are more than 25 million cars in Spain [1], of which a big proportion of them don’t have a brand-included service that provides real-time information of the vehicle. Furthermore, most of them count with an OBD-II connector, a European standard that applies to petrol cars sold in Europe from 2001 and diesels from 2004 which allows getting real-time information and parameters from their central computer. If we also count on trucks and vans, the number increases a couple millions. This is why CarSense can help lots of people and enterprises manage their vehicles from a centralized application.

## Technologies used[[edit](/pti/index.php?title=Categor%C3%ADa:CarSense&veaction=edit&section=3 "Edit section: Technologies used") | [edit source](/pti/index.php?title=Categor%C3%ADa:CarSense&action=edit&section=3 "Edit section: Technologies used")]

* **Physical device**: the device that connects to the car and transmits the data to the servers uses an Arduino UNO board, which gets its power and information from the car using the OBD-II connector and a GSM/GPRS module allowing to get the geolocation of the device and forward information to the servers using the 2G infrastructure.

* **Application backend**: the core of the solution, the application that receives data from the cars and delivers information to the users. It uses the Spring Boot framework with a PostgreSQL database, due to the easy compatibility between these two technologies, to attend petitions and store the data. The PostgreSQL database runs on a docker container, which is deployed with docker-compose due to the ease of making the data persist.

* **CI/CD**: the point of having a CI/CD is to automate the integration of the code whenever a push to the main branch is made, and to deliver it to the server. The CI/CD can have different stages, such as ‘Checkout code from branch’, ‘build’, ‘test’, ‘deploy’ and ‘run on server’. In case of having all these stages, it ensures that the code deployed in the server has been tested, and will not fail to build/run, ensuring QoS. The Jenkins central server is also hosted in the CarSense server, being deployed in a docker container to isolate it from the rest of the components.

* **Application frontend**: the visual part of the project that allow users to access their vehicle's data. It uses Flutter to provide an application that could also be exported to an Android native version, but the web-based one is the main used, since Flutter allows developing applications for multiple devices with the same code. This application connects to the CarSense API in the backend to request and update data and provide a usable and intuitive interface to the end-user.

# Hardware device[[edit](/pti/index.php?title=Categor%C3%ADa:CarSense&veaction=edit&section=4 "Edit section: Hardware device") | [edit source](/pti/index.php?title=Categor%C3%ADa:CarSense&action=edit&section=4 "Edit section: Hardware device")]

## Different possibilities and specs[[edit](/pti/index.php?title=Categor%C3%ADa:CarSense&veaction=edit&section=5 "Edit section: Different possibilities and specs") | [edit source](/pti/index.php?title=Categor%C3%ADa:CarSense&action=edit&section=5 "Edit section: Different possibilities and specs")]

...

## Why the one chosen?[[edit](/pti/index.php?title=Categor%C3%ADa:CarSense&veaction=edit&section=6 "Edit section: Why the one chosen?") | [edit source](/pti/index.php?title=Categor%C3%ADa:CarSense&action=edit&section=6 "Edit section: Why the one chosen?")]

...

## Configuration[[edit](/pti/index.php?title=Categor%C3%ADa:CarSense&veaction=edit&section=7 "Edit section: Configuration") | [edit source](/pti/index.php?title=Categor%C3%ADa:CarSense&action=edit&section=7 "Edit section: Configuration")]

...

# Server[[edit](/pti/index.php?title=Categor%C3%ADa:CarSense&veaction=edit&section=8 "Edit section: Server") | [edit source](/pti/index.php?title=Categor%C3%ADa:CarSense&action=edit&section=8 "Edit section: Server")]

## Providers[[edit](/pti/index.php?title=Categor%C3%ADa:CarSense&veaction=edit&section=9 "Edit section: Providers") | [edit source](/pti/index.php?title=Categor%C3%ADa:CarSense&action=edit&section=9 "Edit section: Providers")]