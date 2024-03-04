# RPC_Assg2
Distributed system using Remote Procedure Calls
In this assignment,  a distributed system using Remote Procedure Calls (RPC) will be created. On Java, RPC is handled commonly through Java remote method invocation (RMI). For web applications, Representational state transfer (REST) is the most commonly linked term. In essence, RPC allows for a client to make a request for the server to run some functionalities based on given requirements. In this task, an RPC client-server system is created. It's first made to function between N clients and a single server. For 8-10 points on the assignment, the amount of servers linked has to be increased.

For this task, you have to create a client and a server that communicate through Remote Procedure Calls. The system's main functionality is to serve as a notebook. Communication between the server and the client can be done with the tool-set that fits you the best. Python is especially recommended for this, as XML-RPC provides simple client-server communication.
The client should be able to:

Ask the user for input & send it to server
        Topic, Text, and timestamp for the note
        If the topic exists on the XML, the data will be appended to the structure
        If not, a new XML entry will be made
Get the contents of the XML database based on given topic
The server should be able to:

Process the client's input
Save data on a local database mock (XML)
Handle multiple client requests at once
