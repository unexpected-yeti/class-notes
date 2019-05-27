# Message Passing

## Lernziele

### Sie wissen was Persistenz und Synchronität in der Kommunikation bedeutet und können daraus die möglichen Kommunikationsformen ableiten

### Sie wissen was eine Nachricht ist und kennen die Prinzipien der Nachrichtenverarbeiten

### Sie können Nachrichten für fixe und adaptive Protokolle mit Hilfe des Basic- und Adaptive-Message Typs implementieren

### Sie kennen die Entwurfsmuster Fabrikmethode und Prototyp

## Definitionen

### Message Passing
Message passing is the paradigm of communication where messages are sent from a sender to one or more recipients.
Forms of messages include (remote) method invocation, signals, and data packets.

Siehe auch [MPI Standard](http://www.mpi-forum.org).

### Fixe Protokolle
Bei fixen Protokollen sind für jede Art von Nachricht die Menge der möglichen Kennungen (IDs) und die möglichen Argumente vor der Kommunikaation bekannt.
Es gibt keine Änderungen während der Kommunikation.
Wird oft mit dem Entwurfsmuster Fabrikmethode umgesetzt.

### Adaptive Protokolle
Nachrichten Protokolle können während der Laufzeit ändern, z.B. können:
- Nachrichtentypen ändern
- Argumenttypen ändern
- die Länge der Argumentliste ändern 

Ein anpassbarer Message Handler bewältigt die Änderungen des Nachrichten Protokolls während der Laufzeit.
In der Praxis kommen Message Passing Systeme mit adaptiven Protokollen häufiger vor als diejenigen mit fixen Protokollen.
Wird oft mit dem Entwurfsmster Prototyp umgesetzt.

### Nachrichtenorientierte Kommunikationsformen
Es wird zwischen folgenden Kommunikationsformen unterschieden:
- **Persistente Kommunikation**: Nachricht wird solange gespeichert bis der Empfänger bereit ist 
- **Transiente Kommunikation**: Nachricht wird nur so lange gespeichert, solange sendende und empfangende Applikation ausgeführtt wird
- **Asynchrone Kommunikation**: Sender wird fortgesetzt unmittelbar nach dem er seine Nachricht zur Übertragung weiter gegeben hat
- **Synchrone Kommunikation**: Der Sender wird blockiert bis die Nachricht an den Empfänger übermittelt wurde

#### Persistente Kommunikation
Es wird unterschieden zwischen:
- Persistenter synchroner Kommunikation (siehe oben)
- Persistenter asynchroner Kommunikation, vgl. Message Oriented Middleware wie z.B. Java Message Service (JMS)

#### Transiente Kommunikation
Es wird unterschieden zwischen:
- Empfangsbasierte transienter synchroner Kommunikation, vgl. TCP Socket Verbindungsaufbau
- Transiente asynchrone Kommunikation, vgl. UDP Socket
- Auslieferungsbasierte transiente synchrone Kommunikation, vgl. Asynchroner RCP
- Antwortbasierte transiente synchrone Kommunikation, vgl. RPC oder RMI

## Entwurfsmuster Fabrikmethode

Siehe [https://de.wikipedia.org/wiki/Fabrikmethode#UML-Diagramm](https://de.wikipedia.org/wiki/Fabrikmethode#UML-Diagramm)

## Entwurfsmuster Prototyp

Siehe [https://de.wikipedia.org/wiki/Prototyp_(Entwurfsmuster)#UML-Diagramm](https://de.wikipedia.org/wiki/Prototyp_(Entwurfsmuster)#UML-Diagramm)
