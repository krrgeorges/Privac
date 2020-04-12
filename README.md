## Project Description

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/) [![Version](https://badge.fury.io/gh/tterb%2FHyde.svg)](https://badge.fury.io/gh/tterb%2FHyde)


### Privac

Privac is a demonstration of how people communicating through the internet can have control of their chat data without relying on external third party servers. This allows for more control, flexibility and higher security bandwidth for communication infrastructures.

### Why should I use this?

Most of the communication apps rely on the client-server model where the server and data lies within the control of the control party and clients rely on the infrastructures on the side of the control party. This has brought up the issue of lack of security, data control and backdoors that can't be avoided in terms of legal precedence.

The architecture proposed and implemented can help with the issues mentioned above. You would have complete control over your chat data, and implementation of backdoors can be completely avoided since you are hosting your own server. Please read below to know more.

### Features

* Complete control of chat interfaces
* Complete control of security aspects
* No middle man, client1 can communicate with client2 with client1 acting as server
* GIFs, emotes, file sharing
* AES encryption
* Read Receipts(controllable)
* Export Chats
* End to End Encryption

### Requirements

* Android -v > 6 && -v < 10
* Python with Flash API
* A local tunneling application. eg:ngrok or localtunnel
* PostgreSQL

### Architecture

A client can host their own server with a local tunneling app for port 80. This would allow global access for communication purposes. Using this port and the IP associated with it. This server is primariy aimed for data storage and interaction endpoints. The deployer can authenticate the client for access, and the access can be revoked if necessary at any time. The client app would communicate with this server and use the data and presentation interfaces for communication. Multiple clients can connect to this server and clients can communicate with each other irrespective of whether he or she is the server depolyer or not.

The server deployer cannot see the messages and files sent by users since it is AES encrypted, allowing for end to end encryption of chats. This provides an additional layer of security in the infrastructure.

**Group Chat is not implemented**

### Installation and Deployment

#### Server Deployment

The database and its table has to be inculcated first in PostgreSQL. Use the `privac.sql` file with database name as 'privac' to deploy the database.

The `ChatServer.py` acts as the server for the communcation architecture. Run the python file to deploy the server.

Till this step, the server would allow local communcation but not global. In order to do this without going into the DNS specifications,
Use a local tunneling app like ngrok or localtunnel to allow communcation from global clients to your port 80. These apps would provide an IP through which the client can use the server.

To authenticate a client, add a record for the user in the users table with user id(uid) and user name(user_name). Share the user id and the IP obtained throught the deployment of local tunnel with the user in order for them to connect and use the server for communcation purposes.

#### Android App 

Install ``app-debug.apk`` to install the client. Would require storage and other permissions.

When logging in, use the user id and the IP provided by the server deployer to access the communication infrastructure. Initiate chats by looking at the list of users available.
