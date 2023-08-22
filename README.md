# UVG_Redes_Proyecto1_V3
Universidad del Valle de Guatemala <br>
Facultad de Ingeniería <br>
Departamento de Ciencias de la Computación <br>
CC3067 Redes <br>
Maria Isabel Solano (20504) 

## Table of contents
- [What is XMPP](#What-is-XMPP)
- [Requirements](#Requirements)
- [How to use](#How-to-use)
- [Functions](#Functions)
- [Difficulties](#Difficulties)
- [Lessons Learnt](#Lessons-Learnt)

## What is XMPP
> [The XMPP Protocol] It is an XML-driven protocol utilized typically in open standard communication. To say it concisely, it is a chat protocol that permits the seamless to and fro sending of essential XML components such as data. Besides making IM and real-time ‘talks’ possible, XMPP also finds its applications in contact list maintenance and presence details. [...] <br>The entire processing of XMPP relies upon the client-server architecture that interests message transmission to the server first and then to the clients.<br> To find out which client should receive the message, the XMPP server utilizes the unique ID of the receiver. The unique ID or Jabber ID is very much comparable to an email address with negligible changes. <br> user@domain.com/resource is the format for the Jabber ID. <br> Here, the user directs to the username, domain.com is the domain particulars of the sender, and resource is the device type of message receiver

([Wallman](https://www.wallarm.com/what/extensible-messaging-presence-protocol), s.f.)

## Requirements
The necessary libraries for the project are the following. 
- `pip install pyfiglet==0.7`
- `pip install asyncio`
- `pip install slixmpp`
- `pip install tk`
- `pip install prettytable`

## How to use
Para utilizar es necesario tener todos los requerimientos anteriormente mencionados instalados en el dispositivo. Para ejecutar el programa solo es neceario correr el siguiente commando:
- `py main.py` (puede variar dependiendo de la configuración de python)

## Functions
1. Log in to accounts
2. Sing-up accounts
3. Check contacts
4. Add contacts
5. Send and receive messages
6. Check info about a specific contact
7. Change presence
8. Receive notifications
9. Delete account

## Difficulties
Personally speaking, starting the project was the most difficult part. First, it was because I felt overwhelmed by it that I didn't even know where to start. When I finally got the time to work on it, settings its foundations was such a headache. Initially, I wanted to develop the project using Java, but the versions of the libraries I was intending to use were all clashing with each other and giving me a lot of error messages. After that, I decided to start all over using Python with slixmpp, and it also gave me its fair share of issues at first, but when I finally got to solve them, I was able to advance with the rest of the project. Sadly, at that point I didn't have much time left, but I did what I could. 

## Lessons Learnt
- The implementation of a XMPP Protocol can be a powerful tool and relatively easy to use. Sadly, most of the libraries that support them are deprecated. 
- When something doesn't work, sometimes it's better to start all over instead of trying to fix it (I've had similar experiences and other projects where I've applied this knowledge, but this one just adds to the lesson)
- Never underestimate a one-month project. 
