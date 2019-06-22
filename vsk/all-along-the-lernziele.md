# Kommunikation in Systemen

[TOC]

### Sie kennen die wichtigsten Begriffe aus den Netzwerk Konzepten kennen, die man für die Java Netzwerkprogrammierung benötigt. 

Sie sind mit folgenden grundlegenden Begriffen vertraut:

- Host
- IP-Adresse
- IP(v4/v6)
- DNS
- ISO/OSI-Layer
- Ports 
- Sockets
- Protokolle (TCP, UDP)
- Client/Server Prinzip

### Sie wissen, welche Aktionen nötig sind, um Daten verbindungsorientiert senden zu können. 

Um Daten verbindungsorientiert zu versenden, sind folgende Aktionen nötig:

- Socket erzeugen
- Socket an einen lokalen      Port binden (Verbindung herstellen) 
- Daten über Socket      lesen/schreiben
- Socket schliessen

### Sie kennen den Lebenszyklus eines TCP Servers und können die einzelnen Elemente mit einem Java Programm in Beziehung stellen. 

Ein Server wird durch die Klasse ServerSocket repräsentiert. Der Lebenszyklus eines TCP Servers sieht wie folgt aus:

1. ServerSocket      mit Port erzeugen
2. Mit accept auf eine Verbindung warten
3. In- und Outputstreaam mit      dem Socket verknüpfen
4. Daten lesen und schreiben,      entsprechend dem vereinbarten Protokoll
5. Connection schliessen
6. Beim Schritt 2.      weitermachen oder ServerSocket schliessen

Der Dienst und die Kommunikation mit dem Client sollte nebenläufig ausgeführt werden.

Beispiel:![1561204684273](./assets/1561204684273.png)

## Sie wissen was ein Netzwerk Interface ist und wie dieses in Java repräsentiert wird. 

Ein Netzwerk Interface ist ein Netzwerk Adapter NIC (network interface card). Ein Netzwerk Adapter kann auch eine Software sein, z.B. ein Loopback Interface (127.0.0.1 für IPv4 und :::1 für IPv6).

Heutige Rechner besitzen mehr als ein Netzwerk Adapter. Beim Erstellen des Server Sockets oder Datagramm Sockets kann (muss) der Netzwerk Adapter angegeben werden.

Die Klasse NetworkInterface repräsentiert eine Netzwerkschnittstelle. Die Netzwerk-Adapter können mit der Methode getNetworkInterfaces() ausgelesen werden.  Auf dem NetworkInterface können InetAdress des Interfaces mit getInetAddresses() ausgelesen werden.

Um einen Server Socket einem bestimmten Netzwerk Adapter zuzuordnen, stehen überladene Konstruktoren zur Verfügung. Zudem muss dem Server Socket noch die Grösse der Warteschlange (Parameter backlog) für anstehende Clients mitgegeben werden. Die Signatur des Konstruktors sieht wie folgt aus: 

```
ServerSocket (final int port, final int backlog, final InetAddress bindAddr) throws IOException
```

### Sie können sowohl Java Client-Programme sowie Java Server-Programme analysieren und implementieren. 

![1561204782620](./assets/1561204782620.png)

### Sie wissen was Persistenz von Objekten bedeutet. 

Die Persistenz von Objekten muss folgende Anforderungen erfüllen:

- **Transparenz**: Persistenz erfordert keine      Sonderbehandlung bei der Programmierung (Benutzer arbeiten in gleicher      Weise mit transienten sowie mit persistenten Objekten)
- **Interoperabilität**: Laufzeitumgebung und      persistenter Speicher sind austauschbar. Persistente Objekte können in      anderen Umgebungen verwendet werden.
- **Skalierbare      Wiederauffindbarkeit**: Das Auffinden von persistenten Objekten erfolgt transparent,      ohne spezifisches Durchsuchen von Objektpools.

Unter Java lassen sich Objekte über verschiedene Ansätze automatisch persistieren:

- **Standardserialisierung**: Binär via Java Object      Serialization (JOS)
- **XML-Serialisierung      über JavaBeans Persistence (JBP)**: Via XML, wird in der Praxis kaum mehr verwendet.
- **XML-Abbildung      über JAXB**: Via      XML. Teil der Standardbibliothek seit Java Version 6.

## Sie kennen den Standardmechanismus zur Serialisierung von Java-Objekten. 

**Ablauf**

Ablauf des Standardmechanismus zur Serialisierung eines Java- Objekts:

1. Metadaten, wie Klassenname      und Versionsnummer, in den Byte-Strom schreiben
2. alle nichtstatischen      Attribute (private, protected, public) serialisieren
3. die entstehenden Byte-Ströme      in einem bestimmten Format zu einem zusammenfassen

Bei der Deserialisierung wird dann der Datenstrom gelesen und ein Java Objekt mit dem gespeicherten Zustand erzeugt

**Standard-Serialisierung**

Es stehen zwei Klassen und ihre (De-)Serialisierungs-Methode zur Verfügung:

- **ObjectOutputStream**: Mit der Methode      writeObject() können Objekte in einen Ausgabestrom geschrieben werden.      Während der Serialisierung geht der ObjectOutputStream die Zustände und      Objektverweise rekursiv ab und schreibt die Zustände Schritt für Schritt      in einen Ausgabestrom
- **ObjectInputStream**: Mit der Methode      readObject() können serialisierte Objekte in ein Objekt der Laufzeit      umgewandelt werden.

 

Beispiel:

```java
final FileOutputStream outputStream = new FileOutputStream("datei"); 
final ObjectOutput output = new ObjectOutputStream(outputStream);

output.writeObject(new Integer(3));
output.flush();

final FileInputStream inputStream = new FileInputStream("datei"); final ObjectInputStream input = new ObjectInputStream(inputStream); 

final Integer integer = (Integer)input.readObject();
```

### Sie kennen das Prinzip der Java Object Serialization. 

Wenn eine beliebige Klasse das Interface java.io.Serializable implementiert, kann Java deren Instanzen serialisieren. Das Interface java.io.Serializable ist ein Marker-Interface, besitzt also keine Methoden. Ist dieses Interface implementiert, kann die Serialisierung entsprechend mit den Klassen `ObjectInputStream` und `ObjectInputStream` zu serialisieren.

Folgende Informationen und Daten zu einem Objekt werden serialisiert:

- Der vollständig qualifizierte Name der Klasse.
- Die Signatur der Klasse.
- Alle nicht-statischen, nicht-transienten Attribute.
- Weitere Objekte, auf welche die Objekt Attribute verweisen.
- Alle aus den Oberklassen geerbten Attribute.

#### Transiente Attribute

Ein transientes Attribut ist ein berechnetes Attribut. Oft \(aber nicht immer\) müssen transiente Attribute beim Deserialisieren initialisiert werden. Dazu gibt es die Methode `readResolve()`. Sie wird, wenn vorhanden, vom `ObjectInputStream` aufgerufen und kann eine Initialisierung vornehmen. Als Beispiel:

```java
 //... weitere Methoden der Klasse Customer
 public Object readResolve() {
 return new Customer(firstName, lastName);
 }
}
```

Das Java-Keyword `transient` kann eine Variable markieren, sodass diese nicht serialisiert wird.

```java
public class Customer implements Serializable {
 private final String firstName;
 private final String lastName;
 // name wird im Konstruktor zusammengesetzt und muss nicht serialisiert werden
 private transient final String name;
 public Customer(final String firstName, final String lastName) {
 	this.firstName = firstName;
 	this.lastName = lastName;
 	this.name = firstName + " " + lastName;
 }
}
```

### Sie wissen wie eine beliebige Klasse zu serialisieren und deserialisieren ist.

 TODO

 

### Sie kennen die Möglichkeiten der Serialisierung bei Vererbung. 

Ist eine Oberklasse einer serialisierbaren Klasse nicht serialisierbar, so werden ihre privaten Felder nicht serialisert. Beim Deserialisieren wird der Konstruktor ohne Argumente der ersten nichtserialisierbaren Oberklasse aufgerufen. In der Oberklasse muss ein Konstruktor ohne Argumente existieren! Alle Unterklassen einer serialisierbaren Klasse sind ebenfalls serialisierbar. Dabei muss die Unterklasse nicht extra mit dem Interface `Serializable` markiert werden.

 

### Sie wissen warum die Versionierung bei der Serialisierung wichtig ist und können Versionsnummern entsprechend einsetzen. 

Alle benötigten Klassen müssen beim Serialisieren und Deserialisieren im Classpath liegen. Serialisierung und Deserialisierung von Objekten können in unterschiedlichen JVMs erfolgen, die potenziell auf unterschiedlichen Plattformen laufen. Es kann sein, dass beliebig viel Zeit zwischen dem Schreiben und Lesen von Dateien liegt.

Serialisierte Objekte haben eine Versionsnummer. Objekte mit falscher Versionsnummer können nicht deserialisiert werden. Die Versionsnummer wird als statisches Attribut definiert. Beispiel:

```java
public static long serialVersionUID = 8365728189244278312L;
```



Ist keine Nummer angegeben, so benutzt Java einen Hashwert, der sich u.a. aus den Namen der Klassenattribute errechnet. Änderungen an der Klasse \(z.B. Hinzufügen einer Methode\) machen serialisierte Daten inkompatibel. Dies verhindert versehentliches Einlesen inkompatibler Daten. Durch Angabe einer serialVersionUID kann man Kompatibilität steuern, eventuell mit eigener readObject-Methode.

 

### Sie können die Code-Beispiele nachvollziehen und modifizieren. 

 TODO

 

### Sie wissen was Persistenz und Synchronität in der Kommunikation bedeutet. 

#### Nachrichtenorientierte Kommunikation

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

### Sie wissen was eine Nachricht ist und kennen die Prinzipien der Nachrichtenverarbeitung. 

**Eine Nachricht**:

* wird über einen Kommunikationskanal gesendet
* enthält eine Anzahl Elemente von bestimmten Datentypen:
  * ID: identifiziert die Nachricht (z.B. GET, POST, … bei HTTP); wird nicht immer benötigt. Bei strikten Interaktionen zwischen Kommunikationspartnern ist die ID unnötig. (z.B. Schach)
  * Argumente: können einfache Datentypen (Integer, Strings, Floating-point) sein
    * Vorteil: Argumente können direkt über DataInputStream und DataOutputStream gelesen und geschrieben werden.
    * Können zusätzliche Informationen enthalten, basierend auf der Art
      der Nachricht, z.B. eine Aktion oder Anfrage (Wandle X in Y und gibt
      Resultat zurück oder Berechne X mit Hilfe von A,B,C)

**Weshalb Nachrichten anstatt SOAP, CORBA, RMI?** 

Weil:

* die Kommunikation relativ simpel ist.
* der Transaktionsdurchsatz kritisch ist (realtime Anwendungen).
* die Entwicklungsresourcen limitiert sind (schnelle Systementwicklung steht über der Flexibilität).
* spezielle Netzwerkprotokolle benötigt werden.
* Remote Objektprotokolle nicht verfügbar sind (z.B. Applet-Browser unterstützt nicht RMI, CORBA, o.ä.).

#### Prinizipien

![1561205442086](./assets/1561205442086.png)

 

### Sie können Nachrichten für fixe oder adaptive Protokolle mit Hilfe des Basic- oder Adaptive-Message Typs nachvollziehen. 

### Fixe Protokolle

Bei fixen Protokollen sind für jede Art von Nachricht die Menge der möglichen Kennungen (IDs) und die möglichen Argumente vor der Kommunikaation bekannt. Es gibt keine Änderungen während der Kommunikation. Wird oft mit dem Entwurfsmuster Fabrikmethode umgesetzt.

### Adaptive Protokolle

Nachrichten Protokolle können während der Laufzeit ändern, z.B. können:

- Nachrichtentypen ändern
- Argumenttypen ändern
- die Länge der Argumentliste ändern 

Ein anpassbarer Message Handler bewältigt die Änderungen des Nachrichten Protokolls während der Laufzeit.
In der Praxis kommen Message Passing Systeme mit adaptiven Protokollen häufiger vor als diejenigen mit fixen Protokollen. Wird oft mit dem Entwurfsmster Prototyp umgesetzt.

### Sie kennen die Entwurfsmuster «Fabrikmethode» und «Prototyp».

#### Factory

> Der Begriff **Fabrikmethode** ([englisch](https://de.wikipedia.org/wiki/Englische_Sprache) **factory method**) bezeichnet ein [Entwurfsmuster](https://de.wikipedia.org/wiki/Entwurfsmuster) aus dem Bereich der [Softwareentwicklung](https://de.wikipedia.org/wiki/Softwareentwicklung). Das Muster beschreibt, wie ein [Objekt](https://de.wikipedia.org/wiki/Objekt_(Programmierung)) durch Aufruf einer [Methode](https://de.wikipedia.org/wiki/Methode_(Softwaretechnik)) anstatt durch direkten Aufruf eines [Konstruktors](https://de.wikipedia.org/wiki/Konstruktor) erzeugt wird. Es gehört somit zur Kategorie der [Erzeugungsmuster](https://de.wikipedia.org/wiki/Erzeugungsmuster) (engl. *creational patterns*).

[![Klassendiagramm der am Muster beteiligten Rollen.](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Fabrikmethode.svg/438px-Fabrikmethode.svg.png)](https://de.wikipedia.org/wiki/Datei:Fabrikmethode.svg)

#### Prototyp

> Ein **Prototyp** ([engl.](https://de.wikipedia.org/wiki/Englische_Sprache) *prototype*) ist ein [Entwurfsmuster](https://de.wikipedia.org/wiki/Entwurfsmuster) (*design pattern*) aus dem Bereich der [Softwareentwicklung](https://de.wikipedia.org/wiki/Softwareentwicklung) und gehört zur Kategorie der [Erzeugungsmuster](https://de.wikipedia.org/wiki/Erzeugungsmuster) (engl. *creational patterns*). Neue [Instanzen](https://de.wikipedia.org/wiki/Objekt_(Programmierung)) werden auf Grundlage von prototypischen Instanzen („Vorlagen“) erzeugt. Dabei wird die Vorlage kopiert 

[![Klassendiagramm, das die am Entwurfsmuster beteiligten Rollen zeigt.](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Prototyp.svg/511px-Prototyp.svg.png)](https://de.wikipedia.org/wiki/Datei:Prototyp.svg)



# Verteilte Systeme (R. Diehl)

### Sie kennen zwei verschiedene Algorithmen zur Synchronisation von physischen Uhren.

### Algorithmus von Cristian

Cristians Algorithmus dient der Zeitsynchronisation von clientseitigen Prozessen mit einem Timeserver. Der Algorithmus funktioniert gut in Netzwerken mit tiefer  Latenz, in welchen die Round-Trip-Zeit kurz ist. Für verteilte Systeme oder Applikationen mit hoher Redundanz ist der Algorithmus nicht geeignet.

> Die _Round-Trip-Zeit_ (RTT) bezeichnet hier die Zeit zwischen Start einer Abfrage (Request) und dem Ende der zugehörigen Anwtort (Response).

#### Zeitserver (time server)

Der Zeitserver ist eine Maschine mit Zeitzeichen-Empfänger. 
Mit diesem Server werden alle anderen Maschinen synchronisiert.
Zu Beginn jeder UTC-Sekunde sendet der Zeitzeichensender einen kurzen Impuls.

> "_UTC_" steht für _Universal Coordinated Time_, die Zeitmessung in Beziehung zum Sonnenstand mit Schaltsekunden.

#### Implementation

- Client _P_ erfragt die Zeit vom Zeitserver _S_ zum Zeitpunkt _t0_
- Die Anfrage wird von _S_ verarbeitet - dies benötigt eine Zeitspanne _I_
- Die Antwort _C(t1)_ (UTC) wird ovn P zum Zeitpunkt _t1_ empfangen.
- _P_ wird auf die Zeit _C(t1)_ + RTT/2 gesetzt, d.h. die vom Server gemeldete Zeit plus die Rücklaufzeit des Pakets
  - Berechnung RTT = _t1_ - _t0_ 
  - ist die Zeitspanne _I_ bekannt, kann die Berechnung verbessert werden: RTT = _t1_ - _t0_ - _I_
- Eine häufigere Messung der Laufzeit wird durchgeführt, um genauere Werte zu erreichen.
- Messungen auserhalb eines Bereiches werden verworfen.
- Von den verbleibenden Werten wird das Mittel verwendet.

#### Probleme

##### Zeit in Vergangenheit

Die Zeit vom Zeitserver liegt in der Vergangenheit der lokalen Zeit. Die Uhr kann nicht einfach zurückgedreht werden, da inkonsistente Zustände im System entstehen könnten.
Hierbei handelt es sich um ein _grosses Problem_.

### **Lösung:** Die lokale Zeit wird verlangsamt, bis die Zeitdifferenz ausgeglichen ist.

##### Rücklaufzeit

Das kleinere der beiden Probleme des Algorithmus von Cristian ist die Zeit (_I_), welche vom Server benötigt wird, bis er eine Antwort sendet.
Diese Laufzeit kann nicht genau bestimmt werden, denn sie ist abhängig von der Netzwerklast.

**Lösung:** Die Zeit _I_ wird durch mehrfache Messung der Dauer der Anfrage kompensiert. 
Der vom Zeitserver gelieferte Wert kann so adaptiert werden.

#### Berkeley-Algorithmus

Anders als beim Algorithmus von Cristian hat beim _Berkley_-Algorithmus keine Maschine einen Zeitzeichen-Empfänger.
Der Zeitserver (Zeit-Daemon) fragt periodisch alle Maschinen nach ihrer Zeit.
Basierend auf den Antworten dieser berechnet der Zeitserver die Durchschnittszeit.
Anschliessend weist er alle Maschinen an, ihre Uhren an diese neue Zeit anzupassen.

#### Network Time Protocol (NTP)

Das seit 1982 entwickelte Protokoll (aktuelle Version NTP v4 seit 1994) dient der Synchronisierung von Rechneruhren im Internet.
Auf fast allen Rechnerplattformen (von PCs bis Crays, Unix, Windows, VMs, embedded systems) sind NTP-Dämone verfügbar.
Durch die Verwendung des Protokolls und des Dämons kann in einem WAN (world access network, Internet) eine Genauigkeit von ca. 0.01s erreicht werden.
In LANs ist gar eine Genauigkeit kleiner als 1ms möglich.

### Struktur

- **Stratum 1:** primärer Zeitgeber, über Funk oder Standleitungen an amtliche Zeitstandards angebunden
- **Stratum >1:**  synchronisiert mit Zeitgeber des Stratums _i-1_

> Das Stratum kann dynamisch wechseln, z.B. bei Unterhalt oder Ausfall der Verbindung

![Diagramm Struktur NTP](assets/structure_ntp.png)



## Sie wissen was eine logische Uhr ist.

Im Jahr 1978 zeigte Leslie Lamport, dass eine Einigkeit bzw. Übereinstimmung der Zeit aller Maschinen innerhalb eines bestimmten Systems ausreicht.
Eine Übereinstimmung mit der Zeit ausserhalb des Systems bzw. eine "echte" UTC ist nicht notwendig.
Logische Uhren finden ihre Anwendung vor allem in Breichen mit hohem Anspruch an Kausalität und Verlässlichkeit. Die Verfahren zur Synchronisation von logischen Uhren in grossen Systemen ist im Allgemeinen jedoch ineffizient.

## Sie kennen die Happened-Before-Relation.

Lamport stellte auch die _Happened-Before-Relation_ auf. Der Ausdruck $a \rightarrow b$  wird gelesen als "_a_ passiert vor _b_". 
Dies bedeutet, dass sich **alle Prozese einig sind**, dass **zuerst das Ereignis _a_** und **dann das Ereignis _b_** stattfindet. Es gilt ebenfalls die Transitivität falls $a \rightarrow b$ und $b \rightarrow c$, dann gilt $a \rightarrow c$

## Sie kennen den Algorithmus des Lamport-Zeitstempels zur Synchronisation von logischen Uhren.

#### Ausgangslage

Jede Maschine hat eine eigene Uhr mit konstanten aber unterschiedlichen Geschwindigkeiten.

Beim Lamport-Zeitstempel sendet ein Prozess eine Nachricht mit der eigenen Uhrzeit an einen anderen Prozess.
Einem Ereignis _a_ wird ein zeitwert _C(a)_ zugeordnet. Alle Prozesse sind sich über den Zeitwert einig.
Wenn _a_ vor _b_ gilt, gilt auch _C(a)_ < _C(b)_.
Ein Prozess sendet eine Nachricht mit eigener Uhrzeit _a_ an einen anderen Prozess, welcher die Nachricht zur eigenen Zeit _b_ empfängt. Dann müssen _C(a)_ und _C(b)_ so zugewiesen werden, dass _C(a)_ < _C(b)_ ist.

Die Uhrzeit C muss **immer vorwärts laufen**.
Korrekturen können durch **Addition von positiven Werten** vorgenommen werden.

#### Lösung

Zwischen zwei Ereignissen muss die lokale Uhr mindestens einmal ticken - _empfangene Zeit_ + 1.

![Übersicht Lösung](assets/lamportexlpanation1.png)

> Es gibt nie zwei EReignsise, die zu genau der selben (logischen) Zeit auftreten.

Die Lösung liegt darin, die **Prozessnummer dem Zeitstempel hinzuzufügen**.

Damit kann allen Ereignissen in einem verteilten System eine Zeit zugewisen werden, die folgenden Bedingungen genügt:

1. wenn _a_ im selben Prozess vor _b_ auftritt, gilt _C(a)_ < _C(b)_.
2. wenn _a_ und _b_ das Senden und Empfangen einer Nachricht darstellen, gilt _C(a)_ < _C(b)_.
3. für allen anderen Ereignisse _a_ und _b_ gilt _C(a)_ != _C(b)_.

### Lamports Uhren

See also: https://www.youtube.com/watch?v=CMBjvCzDVkY

### Eigenschaften

Lamports Uhren erfüllen die Uhrenbedingung! 
Die logischen Lamport-Zeitstempel _L(e)_ definieren daher eine parteille Ordnung auf der Menge der Ereignisse,
die den kausalen Zusammenhang zwischen Ereignissen erhält.
Eine Ergänzung zu einer totalen Ordnung ist wieder möglich.

### Problem: Anahnd der Zeitstempel lässt sich nicht immer sicher sagen, ob zwei Ereignisse kausal voneinander abhängen.

Hierfür müsste auch die Umkehrung der Uhrenbedingung gelten, es gilt aber lediglich _C(a)_ < _C(b)_ --> a vor b V a || b.

## Sie kennen den Algorithmus des Vektor-Zeitstempels zur Synchronisation von logischen Uhren.

See also: <https://www.youtube.com/watch?v=jD4ECsieFbE>

Ein Vektor-Zeitstempel _VT(a)_, der einem Ereignis _a_ zugewiesen wurde, hat die Egenschaft, dass Ereignis _a_
 dem Ereignis b kausal vorausgeht, wenn _VT(a)_ < _VT(b)_ für ein Ereignis _b_ gilt.

 Jeder Prozess _Pi_ besitzt einen Vektor _Vi_, der für jedenProzess im System die Anzahl der Ereignisse enthält 
 mit den Eigenschaften: 

1. _Vi_[i] ist die Anzahl der Ereignisse, die bisher in _Pi_ aufgetreten sind
2. _Vi_[j] = k, erkennt _Pi_, dass in _Pj_ k Ereignisse aufgetreten sind
3. Der Vektor _Vi_ wird den gesendeten Nachrichten mitgegeben.

Jeder Prozess hat einen Vektor an Uhren (Integer Clock). Angenommen es gibt `N` Prozesse (in einer Gruppe von Prozessen `1..N`). Jeder Vektor hat `N` Elemente. Der Prozess `i` hat einen Vektor $V_i[1..N]$.

Das j-the Element im Vektor vom Prozess i (also $V_i[j]$) ist die Zeit (aus Perspektive Prozess i) vom letzten Event des Prozesses j.

Zu Beginn ist der Vektor der Nullvektor.

### Vektor-Zeit inkrementieren

Bei einer Instruktion oder einem gesendeten Event bei Prozess i, der Prozess inkrementiert nur sein i-tes Element des Vektors. Jede Nachricht trägt den Vektor-Zeitstempel des sendenden Prozesses mit.

Erhält Prozess $$i$$ von Prozess $$j$$ eine Nachricht passiert:

- $$V_i[i] = V_i[i] + 1$$
- $$V_i[j] = max(V_\text{message}[j], V_i[j]) \text{for}  j \neq i$$

Also: Der Prozess inkrementiert seinen Vektor an i-ter Stelle und aktualisiert den Zeitstempel an der j-ten Stelle um den höheren Wert zwischen dem gespeicherten und dem mit gesendeten Wert.

### Kausalität

- Zwei Vektor-Zeitstempel sind gleich ($$VT_1 = VT_2$$) falls $$VT_1[i] = VT_2[i]$$ für alle $$i = 1, ..., N$$
- Ein Vektor-Zeitstempel ist kleiner oder gleich ein anderer Vektor ($$VT_1 \le VT_2$$) falls $$VT_1[i] \le VT_2[i]$$ für alle $$i = 1, ..., N$$
- Zwei Events sind **kausal**, z.B. $$VT_1$$ erfolgt vor $$VT_2$$ ($$VT_1 < VT_2$$) falls:
  - $$VT_1 \le VT_2$$ und
  - Es existiert ein $$j$$ sodass $$1 \le j \le N$$ und $$VT_1[j] < VT_2[

## Sie können die Algorithmen zur Synchronisation von logischen Uhren in einem Programm nachvollziehen

TODO



## Sie können den Begriff Middleware erklären und wissen in welche Middleware Kategorien RMI einzuordnen ist

### Middleware

Middleware (englisch für Dienste-Schicht oder Zwischenanwendung) oder Vermittlungssoftware bezeichnet in der Informatik anwendungsneutrale Programme, die so zwischen Anwendungen vermitteln, dass die Komplexität dieser Applikationen und ihre Infrastruktur verborgen werden.

Sie sind transparent in Bezug auf [verschiedene Aspekte](#transparenz).

#### Kategorien

Middlewares werden in die folgenden Kategorien unterteilt:

- **Kommunikationsorientiert**: Der Schwerpunkt liegt in der Abstraktion der Netzwerkprogrammierung (RPC, **RMI**, Web-Service)
- **Nachrichtenorientiert**: Arbeitet über Austausch von Nachrichten mithilfe von Warteschlangen (JMS, SOAP)
- **Anwendungsorientiert**: Im Mittelpunkt steht neben Kommunikation v.a. die Unterstützung verteilter Anwendungen (Hazelcast, JEE, Microsoft .NET und WCF, CORBA)



## Sie wissen was mit Transparenz gemeint ist und kennen die drei gängigsten Transparenzen.

- **Ortstransparenz:** Benutzer kennt Lokation einer Ressource oder eines Dienstes nicht
- **Zugriffstransparent:** Zugriff auf Ressource erfolgt immer identisch, egal ob sich diese lokal oder entfernt im Netz befindet.
- **Nebenläufigkeitstransparenz:** Mehrbenutzerbetrieb wird von Diensten und Ressourcen unterstützt. Das System ermöglicht exklusive Zugriffe und Datensynchronisation und -replikation.
- **Fehler- und Ausfalltransparenz:** Typische durch Verteilung entstehende Fehler (Übertragungsfehler, Komponentenausfall etc.) bleiben der Anwendung weitgehend verborgen.
- **Sprachtransparenz:** Die Kommunikation zwischen den Komponenten ist unabhängig von der jeweils verwendeten Programmiersprache.
- **Replikationstransparenz:** Aus Performancegründen kann es mehrere Kopien derselben Ressource geben. Das System sorgt für die transparente Änderung der darin vorgenommenen Änderungen.

## Sie kennen zwei Architekturmodelle von verteilten Systemen und können erklären was eine Multi-Tier Architektur ist.

### Client-Server / Peer-to-Peer

- Client-Server: langlebender Server, kurzlebende Client-Prozesse
- Peer-to-Peer: Gleichberechtigte Prozesse laufen lokal und tauschen nur bei Bedarf untereinander Informationen aus, es wird kein zentraler Prozess benötigt.

### Fat-Client und Thin-Client

- Fat-Client: Verarbeitung der Daten i.d.R. vor Ort vollzogen, oftmals stellt es auch ein GUI zur Verfügung
- Thin-Client: Stark auf die Hilfe anderer Computer oder Server angewiesen ist um seine Computeraufgaben zu erfüllen

### Multi-Tier Architektur (2-Tier, 3-Tier und n-Tier)

- 2-Tier: Präsentation, Anwendungslogik und Datenhaltung auf zwei Anwendungen verteilt
- 3-Tier: Die Anwendungslogik erhält einen eigenen Tier
- n-Tier: Verteilung der Anwendungslogik und Datenhaltung auf mehrere Tiers

## Sie kennen das RMI Prinzip und wissen wozu die notwendigen Komponenten dienen.

- Bereitstellung von einer oder mehrere Methoden in einem Remote-Interface. Diese Methoden sollen als Dienste zur Verfügung stehen.
- Server-Klasse implementiert Interface
  - Instanzen davon heissen Remote-Objekte
  - Remote-Objekte werden bei Namens-Service registriert
  - Clients können Dienst dort anfordern
- Clients fordern mithilfe des Namensservices die Remote-Referenz der benötigten Objekte und können dann die entsprechenden Methoden darauf aufrufen
- Übertragung der Parameter und des Rückgabewertes sind für Server sowie Client transparent.

### Technische Realisierung

![Diagramm RMI Realisierung](./assets/rmi_implementation.png)

- **Client-Stub**: Stellvertreterobjekt, identische Schnittstelle wie Remote-Objekt; befindet sich auf selbem Rechner wie Client 
- **Server-Stub**: befindet sich auf Server, nimmt Aufrufe von Client-Stub entgegen
- **Remote Method Procotol**: regelt Kommunikation auf Basis von TCP/IP Verbindungen
- **RMI-Transportschicht**: Hier kommunizieren die beiden Stubs miteinander. Der Server-Stub kennt das tatsächliche Remote-Objekt, leitet die Anfragen des CLient-Stubs entsprechend weiter und gibt den Rückgabewert an den Client zurück

## Sie wissen in den Grundzügen wie RMI auf Client- und Serverseite mit Hilfe von Stellvertreterobjekten funktionieren.

siehe oben.

## Sie kennen die Voraussetzungen, welche für Parameter und Rückgabewerte bei RMI gelten.

- Elementare Datentypen: können wie gewöhnlich *by value* übergeben werden.
- Lokale Objekte: können nur übergeben werden (oder als Rückgabewerte), wenn sie serialisierbar sind (Implementation des `Serializable` Interfaces); werden als Kopie übergeben (also auch *by value*)
- Verweise auf Remote-Objekte: werden z.B. vom Namensservice zurückgegeben und werden als Objektreferenzen (*by reference*) behandelt.

## Sie können in Java die Schnittstelle für Remote Objekte definieren, die Remote Objekte anhand der Schnittstelle implementieren und bei einem Namens-Service registrieren

##### 1. Remote-Interface definieren

- Jedes Remote-Objekt muss Interface `Remote` implementieren
    - beschreibt die Funktioenn, die auf Server zur Verfügung stehen
    - auch Parameter/Rückgabewerte eines Interfacetypes
- Jede angebotene Methode kann eine `RemoteException` auslösen
- Parameter/Rückgabewerte: müssen serializable sein, Laden von Byte-Code automatisch möglich

```java
public interface RemoteFibonacci extends Remote {
    public BigInteger calc(int value) throws RemoteException;
}
```

##### 2. Remote-Interface implementieren

- Um eingehende externe Methodenaufrufe zu behandeln muss jedes Remote-Objekt in die RMI Infrastruktur exportiert werden. Möglichkeiten:
    1. Ableitung der Klasse `UnicastRemoteObject` und Implementation des RMI-Interfaces
    2. Remote-Objekt implementiert RMI-Interface und wird mithilfe der Klassen-Methode `UnicastRemoteObject.exportObject(...)` exportiert.
- Infrastruktur generiert dann die zugehörige URL für Remote Method Protocol

```java
public class FibonacciImpl extends UnicastRemoteObject
implements RemoteFibonacci {
 public FibonacciImpl() throws RemoteException {
 super();
 }
 @Override
 public BigInteger calc(int value) throws RemoteException {
 BigInteger fibonacci;
 fibonacci = FibonacciCalculator.getFibonacci(
 new BigInteger(Integer.toString(value)));
 return fibonacci;
 }
}
```

##### 3. RMI-Repository starten

- Infrastruktur für das Binding ist der RMI Namensdienst
    - rmiregistry.exe: Repository erreichbar über RMI-URL
    - ansprechbar über Methoden des Pakets `java.rmi.registry`
- Reskriktion: RMI-Server kann nur Referenzen von Remote-Objekten in Registry registrieren, die  auf demselben Host laufen
    - Sicherheitsrisiko: Ansonsten könnte RMI-Client Registryeinträge entfernen oder verändern
- RMI-Registry ist Abbildung ovn Namen auf Remote-Objekte
    - Hierarchische Namensräume, dynamische Objektsuche, Lastverteilung oder ähnliche Eigenschaften fehlen
    - Alternative: Java Naming and Directory Interface (JNDI)

##### 4. Remote-Objekte erzeugen

 - Factory-Methode `LocateRegistry.createRegistry(int portNumber)`
 - Standard-Port 1099
 - Programm `RegistrySetup` darf nicht beenden

 ```java
public final class RegistrySetup {
 public static void main(final String[] args) throws RemoteException, InterruptedException {
    final Registry reg = LocateRegistry.createRegistry(Registry.REGISTRY_PORT);
    LOG.info("o.k.");
    synchronized (reg) {
        reg.wait();
    }
 }
}
 ```

##### 5. Remote-Objekte registrieren

- Klasse Naming stellt Funktionen zur Registrierung von  Remote-Objekten zur Verfügung:

```java
public static void bind(String name, Remote obj)
 throws AlreadyBoundException, MalformedURLException,
 RemoteException;
public static void rebind(String name, Remote obj)
 throws RemoteException, MalformedURLException
public static void unbind(String name)
 throws RemoteException, MalformedURLException, NotBoundException
public static Remote lookup(String name)
 throws NotBoundException, MalformedURLException, RemoteException
public static String[] list(String name)
 throws RemoteException, MalformedURLException
```

####### Vorgang

1. Remote-Objekt erzeugen
2. Nach Start des RMI-Namensdiensts kann Remote-Objekt registriert werden

```java
public class FibonacciServer {
    public static void main(String[] args)
        throws RemoteException, AlreadyBoundException, MalformedURLException {
        final FibonacciImpl fibo = new FibonacciImpl();
        final String url = "rmi://localhost:1099/fibo";
        Naming.bind(url, fibo);
    }
}
```

> Werden Bytecode-Klassen dynamisch per RMI geladen, so wird eine Installation des SecurityManagers notwendig.

##### 6. Client implementieren

- Client sucht Referenz zum Remote-Objekt mittels `Naming.lookup(String url)`

```java
public class FibonacciClient {
    public static void main(String[] args) {
        try {
            final int value = 123;
            final String url = "rmi://localhost:1099/fibo";
            final var fibo = (RemoteFibonacci) Naming.lookup(url);
            BigInteger reslult = fibo.calc(value);
            // do something with result
        }
        catch (NotBoundException | MalformedURLException |RemoteException e) {
            LOG.fatal(e.getMessage());
        }
    }
}
```



## Sie können RMI Clients auf die Remote Objekte zugreifen lassen.

Siehe oben (Schritt 6 öppe ungefähr)

## Sie kennen das Push Prinzip für RMI und können es an Code Beispielen nachvollziehen.

### RMI Push Prinzip

- Das Remote-Interface bietet eine Registrierungsmethode als Dienst zur Verfügung
- Der Server (hier Logger Server) implementiert dieses Interface und erzeugt eine Remote-Instanz, diese Instanz wird bei der Registry registriert
- Der Viewer erzeugt ein Remote Push Receiver und exportiert diesen in die RMI Runtime (implizit oder explizit möglich)
- Der Viewer holt sich die Remote-Referenz zum Server und registriert sich (übergibt den Receiver für den Remote Push)
- Der Server ruft den Receiver bei Bedarf auf, um Nachrichten an den Client zu senden

#### Callback Beispiel (Fibonacci)

- Der Server stellt einen Dienst zur Berechnung einer Fibonacci Zahl zur Verfügung (kann bei grossen Zahlen eine längere Zeit dauern). Dazu ruft der Server intern die Methode `calc` auf.
- Wenn der Client die Methode des Server aufruft gibt er eine Referenz zu sich mit
- Der Fibonacci rechnet die Zahl asynchron und benachrichtigt den Client nach Abschluss der Berechnung. Dies macht er über ein Callback des Clients. Der Client stellt also eine Methode zur Verfügung (z.B. `handle`), die der Server aufrufen kann

Aufbau:

- Remote Schnittstellen:
  - `RemoteFibonacci` für die Berechnung der Fibonacci Zahl
  - `RemoteCallbackHandler` für den Callback
- RMI Server
  - `FibonacciImpl` implementiert den Server-Dienst zur Berechnung
  - `Request`, hier wird die eigentliche Berechnung durchgeführt
  - `FibonacciServer` erstellt die RMI Registry, erzeugt das Remote Objekt (`FibonacciImpl`)
- RMI Client
  - `FibonacciTask` implementiert den Callback und den Aufruf der Remote Methode `calc`
  - `FibonacciClient` erzeugt einen `FibonacciTask` und lässt diesen asynchron / nebenläufig ausführen

## Sie wissen welche Komponenten notwendig sind, um eine RMI Applikation zu verteilen.

#### Verwendung der RMI Registry vom Server

- Server holt sich über die Methode `getRegistry` der Klasse `LocateRegistry` eine Referenz zur lokalen Registry. Aus Sicherheitsgründen kann ein RMI Server Referenzen von Remote Objekten nur in einer lokalen Registry registrieren
- `getRegistry` ermöglicht eine Referenz zur Registry auf dem lokalen Host auf einem Default Port (1099) oder einem spezifizierten Port.

#### Verwendung der RMI Registry vom Client

- Der RMI Client holt sich mit Hilfe der Klasse LocateRegistry und der Methode getRegistry eine Referenz zur Registry.
- Die getRegistry Methode ermöglicht eine Referenz zur Registry
  - auf dem lokalen Host am Default Port (1099) oder
  - auf dem lokalen Host an einem spezifizierten Port oder
  - auf einen entfernten Host am Default Port oder
  - auf einen entfernten Host an einem spezifizierten Port.

## Sie können eine Codebase definieren und wissen welche Komponente den Code bereitstellen muss.

Bei Ausführung von RMI Applikationen wird immer Byte-Code geladen. Der Byte-Code wird nach folgendem Muster gesucht:

- In den lokalen Verzeichnissen (lokale Code Basis)
- In den entfernten Verzeichnissen (definierte Code Basis)

RMI Anwendungen haben die Wahl zwischen zwei Mechanismen, um Referenzen auf Remote-Objekte zu erhalten:

- Eine Anwendung kann ihre Remote-Objekte mit RMI Naming
  Methoden bei der RMI-Registry registrieren.
- Eine Anwendung kann ihre Remote-Objekte mit Hilfe der
  Klassen-Methode UnicastRemoteObject.exportObject
  exportieren.

Die Kommunikation mit Remote-Objekten wird durch die RMIMiddleware gehandhabt. Die Kommunikation ist transparent.

Wird Klassen-Bytecode für Objekte, die als Parameter oder Rückgabewerte übergeben werden, benötigt, stellt  RMI die erforderlichen Mechanismen zum Laden des Codes eines Objekts sowie zum Übertragen seiner Daten bereit.

#### Beispiel am Fibonacci Calculator

![1560420176718](assets/1560420176718.png)

Codebase einrichten:

- Das Property `java.rmi.server.codebase` gibt die Codebase an, für Klassen welche die JVM benötigt. Das Property wird via `System.setProperty(...)` gesetzt, z.B. `System.setProperty("java.rmi.server.codebase", "http://localhost:8080/")`
- Sobald Code von Remote geladen wird ist ein Security Manager notwendig

Codebase zur Verfügung stellen:

- Am einfachsten: Die Klassen-Bytecode via HTTP-Server zur Verfügung stellen
- Wichtig: Der HTTP-Server benötigt Zugriff auf die .class-Dateien (und keine Java Archives (jar)!)
- JDK hat selbst einen HTTP-Server (in den neuen Versionen nicht mehr dabei), oder via Nginx/Apache oder ähnliches (z.B. mit Python `python -m http.server 8080`)



## Sie wissen, wie ein Security Manager in den Grundzügen funktioniert und können einen Security Manager für Ihr verteiltes RMI System konfigurieren und aktivieren

Java unterscheidet zwischen lokalem und remote Code bezüglich der Sicherheitsanforderungen:

- Lokaler Code hat Zugriff auf alle verfügbaren Ressourcen
- Remote Code hat eingeschränkten Zugriff, er kann z.B. nicht:
  - auf Dateien auf dem lokalen Computer zugreifen
  - Netzwerkverbindungen öffnen, die auf einen anderen Host als von dem der Code geladen wurde verbinden
  - Netzwerkverbindungen auf privilegierten Ports (< 1024) akzeptieren
  - Lesen von benutzerbezogenen System-Properties ("user.name", "user.home" etc)
  - Ausführen von externen Programmen
  - Laden von System-Libraries

#### Security Manager aktivieren

- `java.lang.SecurityManager` (seit JDK1.2) bietet eine Default-Implementierung an, die folgende Möglichkeiten hat:
  - Aktivieren über die Kommandozeile via `-Djava.security.manager`
  - Instanziieren des SecurityManagers via `System.setSecurityManager(new SecurityManager())`
  - `System.getSecurityManager()` prüft ob ein Security Manager aktiviert ist
- Man kann eine eigene Security Policy definieren. Dies wirdin einer Text-Datei (sog. policy file) statt im Code definiert.

##### Beispiel Policy File

Ein Policy File besteht aus `grant` Anweisungen um Rechte (`permission`) zu vergeben:

```java
grant {
    permission java.security.AllPermission
}
```

Achtung: Das ist ein schlechtes Beispiel, da es alle Rechte vergibt!

Die geltende Policy muss VOR Aktivierung des Security Managers angegeben werden.

- Definition der Policy-Datei über die Kommandozeile mittels -Djava.security.policy=rules.policy
- Definition der Policy-Datei im Code mittels Property System.setProperty("java.security.policy", "rules.policy");

Mit der Angabe der Policy-Datei, kann auch ein Verzeichnis definiert werden. Wird kein Pfad angegeben sucht der Security Managers die Policy im root-Verzeichnis.

Ebenfalls kann im Policy File angegeben werden:

- Codebase: Vergibt Rechte für Klassen, die von einem bestimmten Ort kommen.
- Signierung: Es wird nur das Recht eingeräumt, wenn Programmcode signiert ist.
- Principal: Gewährt bestimmte Rechte für authentifizierte Benutzer. 

#### Beispiel Policy für Fibonacci Calculator

- Die RMI-Registry muss Rechte besitzen, um
  - am Registry Port 1099 hören können
  - Verbindung zu Codebase Port 8080 machen können
  - Verbindungen mit lokalen Prozess Ports akzeptieren können
  - Verbindungen mit Client Prozess Ports akzeptieren können
- Der RMI-Server muss Rechte besitzen, um
  - Verbindung zu Registry Port 1099 machen können
  - Verbindung zu Codebase Port 8080 machen können
  - Verbindungen mit lokalen Prozess Ports akzeptieren können
  - Verbindungen mit Client Prozess Ports akzeptieren können

Im Policy File(s) sieht das so aus:

Registry-Setup:

```
grant {
 permission java.net.SocketPermission "localhost:1099", "listen";
 permission java.net.SocketPermission "localhost:8080", "connect,resolve";
 permission java.net.SocketPermission "localhost:1024-", "accept,resolve";
 permission java.net.SocketPermission "*:1024-", "connect,resolve";
 permission java.net.SocketPermission "*:1024-", "accept,resolve";
};
```

Fibonacci-Server:

```
grant {
 permission java.net.SocketPermission "localhost:1099", "connect,resolve";
 permission java.net.SocketPermission "localhost:8080", "connect,resolve";
 permission java.net.SocketPermission "localhost:1024-", "accept,resolve";
 permission java.net.SocketPermission "*:1024-", "connect,resolve";
 permission java.net.SocketPermission "*:1024-", "accept,resolve";
};
```

# Komponentenentwurf und Entwicklungsprozess (M. Jud)

## Sie verstehen das Konzept der Software-Komponenten und kennen die Kriterien zur Modularisierung.

Folgende Kriterien gelten für den modularen Entwurf von Systemen:

- **Zerlegbarkeit**: Teilprobleme sind unabhängig voneinander entwerfbar.
- **Kombinierbarkeit**: Module sind unabhängig voneinander \(wieder-\)verwendbar.
- **Verständlichkeit**: Module sind unabhängig voneinander zu verstehen.
- **Stetigkeit**: kleine Änderungen der Spezifikation führen nur zu kleinen Änderungen im Code.

### Zerlegbarkeit \(modular decomposability\)

Zerlege ein Softwareproblem in eine Anzahl weniger komplexe Teilprobleme und verknüpfe diese so, dass die Teile möglichst unabhängig voneinander bearbeitet werden können. Die Zerlegung wird häufig rekursiv angewendet: Teilprobleme können so komplex sein, dass sich eine weitere Zerlegung aufdrängt.

### Kombinierbarkeit \(modular composability\)

Strebe möglichst frei kombinierbare Software-Elemente an, die sich auch in einem andern Umfeld wieder einsetzen lassen. Kombinierbarkeit und Zerlegbarkeit sind voneinander unabhängige Eigenschaften.

### Verständlichkeit \(modular understandabilty\)

Der SourceCode eines Moduls soll auch verstehbar sein ohne dass man die anderen Module des Systems kennt. Software-Unterhalt setzt voraus, dass die Teile eines Systems unabhängig von einander zu verstehen und zu warten sind.

### Stetigkeit \(modular continuity\)

Von einer kleinen Änderung der Anforderungen soll auch nur ein kleiner Teil der Module betroffen sein.

## Sie kennen die Kriterien für gute Schnittstellen im Software-Entwurf und können solche Schnittstellen entwerfen.

- Schnittstellen sollen minimal sein
- Schnittstellen sollen einfach zu verstehen sein
- Schnittstellen sollen gut dokumentiert sein

## Sie können verschiedene Arten von Schnittstellen angemessen dokumentieren.

### Operational Interfaces

A component offers a range of services, which are accessed by calling interface operations.

Operational Interfaces group operations belonging together. If a client uses one operation, it is quite likely that it will use some of the other operations too. Sets of such operations belong together and have related effects on the state of the component object.

From the interface providers view the following needs to be specified:

- The name
- The input parameters: specifying the information passed to the component
- The output parameters: specifying the information provided or returned by the component
- Any resulting change of state 
- Specification how the inputs, outputs and component states are related

### Signal Interfaces

A set of signals that can be sent or received by a component.

From the interface providers view the following needs to be specified:

- The name
- Outgoing signals
- Ingoing signals

### Stream Interfaces

Collections of data-streams, that can be consumed or produced by a component.

From the interface providers view the following needs to be specified:

- The name
- The produced streams \(outgoing\)
- The consumed streams \(ingoing\)
- The quality of services \(e.g. max dataflow\)



## Sie können Komponenten entwerfen, dokumentieren, in Java realisieren, testen und deployen.

?

## Sie kennen die Zusammenhänge zwischen Analyse/ Design und Test/Abnahme von Softwarekomponenten.

Mit dem V-Modell lässt sich der Zusammenhang zwischen den verschiedenen Disziplinen (Requirement Engineering, Design, Implementierung) und deren Verifikation mittels Tests aufzeigen.

![V-Modell](assets/v-modell.png)

Beim Testen ist es wichtig Tests zu dokumentieren oder zu automatisieren, um so Regressionstests zu erreichen. 
Mit keiner Testart und mit keinem Review findet man alle Fehler. 
Nur im Zusammenwirken der unterschiedlichen Techniken findet man ein Maximum an Fehlern. 

## Sie können geeignete Systemtests definieren, diese dokumentieren und die Durchführung protokollieren.

Systemtests prüfen die gesamte Wirkungskette im Softwareprodukt, Aspekte, die mit Unit-Tests und Integrationstests nicht abgedeckt werden.

Testfälle sollen in einer Testumgebung ablaufen, welche der späteren Einsatzumgebung möglichst nahe kommt.  Sobald mehrere Komponenten zusammen funktionieren müssen, gibt viele mögliche Konfigurationen, die entsprechend der Vorgaben des Konfigurationsmanagements zu testen sind.

Systemtestfälle können grundsätzlich den im Backlog formulierten Anforderungen und Akzeptanzkriterien abgeleitet werden.

### Systemtestfälle

// TODO

Systemtestfälle können grundsätzlich abgeleitet werden aus:

- den im Backlog formulierten Anforderungen
  - den im Backlog formulierten Abnahmekriterien
  - zugehörigen, detaillierteren UseCase-Beschreibungen.
  - der «Definition of Done»
- Nicht funktionale Anforderungen werden oft wenig explizit festgehalten, entsprechend kommen auch nicht funktionale Tests zu kurz: Last- / Performance- / Stress- / Security- / Robustness- Tests sind ebenfalls wichtige Systemtests.
- Wie beim Test-first-Ansatz auf Unittest-Ebene fördert auch das Formulieren der Systemtests das Verständnis der Anforderungen im Backlog und bringt Unklarheiten und Inkonsistenzen frühzeitig zu Tage.

## Sie wissen welche Informationen über die zu entwickelnde Software wann, wie und wo dokumentiert werden sollen.

hahahhahahahha.



## Sie kennen Arten, Zweck und Bedeutung von Reviews und können ein Review durchführen und protokollieren.

![Folie](assets/review-overview1.png)
![Folie](assets/review-overview2.png)
![Folie](assets/review-overview3.png)
![Folie](assets/review-overview4.png)
![Folie](assets/review-overview5.png)

### Durchführung von Reviews

Review-Sitzungen sollten **nicht länger als zwei Stunden dauern**.
Überprüfe bei jeder Sitzung nur ein Objekt / Artefakt eines Autors (oder mehrere kleine verwandte Objekte / Artefakte).
Die Teilnehmer erhalten die Objekte / Artefakte einige Tage vor der Review-Sitzung.
Es ist wichtig, dass sich alle Mitglieder des Review-Teams darauf vorbereiten, d.h. die Unterlagen ernsthaft studieren.
Der Leiter der Review geht die Objekte / Artefakte Seite für Seite durch und frägt die Teilnehmer, ob sie Kommentare zu einem bestimmten Abschnitt oder einer bestimmten Seite haben.
Entdeckte Fehler und aufgeworfenen Probleme werden in einem standard Reviewprotokoll festgehalten.
Beim klassischen Projektvorgehen sind Reviews eng an den Projektlebenszyklus gekoppelt. Sie müssen deshalb dann angesetzt werden, wenn die zu überprüfenden Objekte / Artefakte vorliegen sollten.
Reviews bringen das beste Aufwand/Ertragsverhältnis, wenn übergeordnete Objekte / Artefakte überprüft werden (besser Anforderungen & Konzepte reviewen statt Detail-Design & Code)

Die Art und Weise, wie eine Review organisiert wird, ist wichtig. 
Der erste Zug muss so aussehen, als käme er vom Autor und nicht vom Gutachter. 
Der Autor muss sich mit der Idee der Review wohlfühlen.
Reviews sind im zuerst eine zwischenmenschliche Angelegenheit, der Erfolg hängt von der persönlichen Dynamik zwischen Autor und Reviewer ab. 
Es ist wichtig flexibel zu sein, wer wessen Arbeit reviewed, d.h. kompatible Paare sich gegenseitig suchen lassen.
Ein guter Reviewer ist nicht wertend und erkennt, dass der primäre Nutzen einer Review darin besteht, dass man gemeinsam über ein Werk spricht.
Mögliche oder tatsächliche Fehler, die in einem Review gefunden werden, soll man nicht an die grosse Glocke hängen, sondern möglichst lokal lösen.

## Sie kennen Bedeutung, Begrifflichkeit und Methoden des Konfigurationsmanagements.

Im Konfigurationsmanagement geht es um das Identifizieren der Konfiguration eines Systems zu verschiedenen, definierten Zeitpunkten um über den gesamten System-Lebenszyklus Änderungen an der Konfiguration kontrolliert durchzuführen und die Integrität und Rückverfolgbarkeit sicherzustellen.

SCM ist eine technische und organisatorische Führungsaufgabe:

- identifizieren und dokumentieren der Eigenschaften für jedes Configuration Item 
- steuern nötiger Änderungen dieser Eigenschaften
- den Stand der Umsetzung von Änderungen erfasssen 
- die Einhaltung festgelegter Anforderungen überprüfen

### Software Configuration Item

A software configuration item (SCI) is an aggregation of software that is designated for configuration management and is treated as a single entity in the SCM process.

Items tht are controlled in addition to the code itself include:

- plans
- specifications
- code libraries
- data and data dictionaries
- documentation for installation, maintenance, operations etc.

### Version

Eine Version ist ein spezifisches, identifizierbares Artefakt auf einem bestimmten Entwicklungsstand.

### Revision

Eine Revision ist eine neue Version eines Artefaktes mit dem Zweck eine ältere abzulösen.

### Baseline

Eine Baseline ist ein Satz von Revisionen, d.h. ein Snapshot der Konfiguration.

### Release

Ein Release ist eine getestete und freigegebene Baseline.

## Sie können für ein kleines Entwicklungsprojekt Rahmen- und Sprint-Planung gemäss SoDa machen.

looooooooooooooooooooool.

## Sie können Sprintbacklogs für ein kleines Team formulieren, schätzen und geeignete Abnahmekriterien festlegen.

phahahaha ja genau

## Sie können ein Controlling auf Projekt- und Sprintebene  für kleine Entwicklungsprojekte gemäss SoDa führen.

ech weiss au ned was ich da dezue söll säge

## Sie wissen welche Informationen aus dem Entwicklungsprozess gemäss SoDa wann, wie und wo dokumentiert werden sollen.

Bullshit.

# Entwicklung, Entwurfsmuster, Testing, Clean Code und QS (R. Gisler)
## Sie kennen die Aufgaben eines Versionskontrollsystems (VCS) und können es nutzen.

Check

## Sie kennen die verschiedenen Konzepte und Arten von Versionskontrollsystemen.

Check

##  Sie können mit verschiedenen VCS-(Client-)Werkzeugen alleine und im Team arbeiten.

Check

## Sie kennen die Vorteile eines automatisierten Buildprozesses.

Check

## Sie können Beispiele von Buildwerkzeugen benennen.

Check

## Sie beherrschen die Anwendung eines ausgewählten Buildwerkzeuges (Apache Maven).

Check

## Sie sind mit den wesentlichen Konzepten von Apache Maven vertraut.

Check

## Sie haben ein grundsätzliches Verständnis von Dependency Management.

Jap

## Sie wissen am Beispiel von Java und Apache Maven wie das Dependency Management funktioniert.

Jap

## Sie sind mit den Begriffen «dependency scopes» und «transitiv dependencies» vertraut und können diese  erklären

Im Beispiel oben fällt das Element `<scope>compile</scope>`auf, das optional pro Abhängigkeit definiert werden kann.

* Damit wird der Zweck und Geltungsbereich (-> Scope) der Dependency qualifiziert, **was unbedingt empfohlen wird!**

Maven kennt verschiedene Scopes (hier nur die wichtigsten drei):
* compile – Dependency wird für die Kompilation und zur Laufzeit des Programmes benötigt (Default).
* test – Dependency ausschliesslich für die Kompilation und
  Ausführung der Testfälle (Beispiele: JUnit, AssertJ etc.).
* runtime – Dependency nur für Laufzeit, aber nicht für
  Kompilation, z.B. für dynamisch geladene Implementationen.

Abhängig von den Scopes sorgt Maven für spezifische Classpaths!
* Daraus ergibt sich eine implizite Verifikation des Designs.

## Sie kennen das Versionskonzept und die  Funktionsweise von Snapshots.

* In einer dynamischen Entwicklungsphase sind fixe Versionen aber eher hinderlich, die Versionierung würde sonst (für jede kleinste Änderung) förmlich «gallopieren» müssen.
  * Es würde eine Unmenge von (unnützen) Versionen produziert,
    welche nie mehr benötigt werden.
* Darum wurde das Snapshot-Konzept integriert: Sobald man einer Version den Appendix –SNAPSHOT trägt, gilt diese als «erneuerbar» und (noch) nicht stabil, sondern in Entwicklung.
  * Sie wird bei jedem Build immer wieder vom Repository aufgelöst und aktualisiert.
  * Im Repository sind Snapshots mit einem Timestamp versehen.
* Beispiel: 5.0.1-SNAPSHOT
  * Die noch nicht stabil veröffentlichte, zukünftige Version 5.0.1

## Sie wissen auf welche Art Dependencies deployed werden.

In Java werden Artefakte in der Regel als JARs ausgetauscht. Ursprünglich wurden JARs direkt in Projekte kopiert (_/lib_). Dies ist Fehleranfällig, bringt hohe Redundanz und einen grossen Platzbedarf mit sich.
Darum wird auch in Java ein Dependency Management Tool verwendet, nachfolgend ist der Fokus nur auf Maven. Der Maven Quasi-Standard ist sehr populär - zahlreiche Dependency Managment Tools basieren auf Maven (z.B. Grape, Gradle, SBT, usw.)

## Sie wissen was ein Buildserver ist.

ja

## Sie kennen die Vorteile des Einsatzes eines Buildservers.

Ja

## Sie kennen beispielhafte Produkte von Buildservern und können diese als Anwender nutzen.

Ja

## Sie können die Ziele der Continuous Integration (CI) erklären

Ziele bei der Entwicklung von Software nach CI:

- Immer ein lauffähiges Produkt (Buildresultat) zu haben, damit kontinuirlich getestet werden kann.
- Bei Fehlern jeder Art möglichst schnell ein Feedback erhalten, durch automatisierte Tests und statische Prüfungen.
- Im Team parallel entwickeln können und den Überblick nicht verlieren, Integrationsaufwand zu minieren und laufend über den aktuellen Stand auf dem Laufenden zu sein.

## Sie kennen das Potential von automatisierten CI-Prozessen.

Yo

## Sie kennen die zehn wesentlichen Praktiken der CI.

### Einsatz eines (zentralen) Versionskontrollsystem

Sämtliche Quellen-Artefakte welche für den vollständigen Build einer Software benötigt werden unterliegen der Versionskontrolle.

Fähigkeiten des Versionskontrollsystem nutzen:

1. Sinnvolle Commit-Kommentare (z.B. mit Verweis auf ein Issue)
2. Tagging: Bestimmte Versionen markieren (z.B. um einen Release eindeutig zu identifizieren)
3. Branches für parallele Entwicklung (z.B. bugfixing oder feature branches)

### Automatisierter Buildprozess 

Ausschliesslich auf der Basis der aktuellen Quellen aus dem Versionskontrollsystem (VCS). Ausführung auf einem Build-Server. Führt ebenfalls die Testfälle aus.

### Automatisierte Testfälle

- Möglichst viel durch automatisierte Testfälle abdecken.
  - Primär Unit Tests, weil einfach und überall lauffähig.
  - Sekundär auch Integrationstests, z.B. Abhängig von Datenbank.
- Fehlerhafte oder nicht vollständige Implementationen sollen so schnell wie möglich aufdecken werden
  - Bei Integrationstests auch häufig unerwartete Nebeneffekte.
- Bewährt haben sich auf Performance Tests (z.B. hat sich eine Änderung negativ auf die Performance ausgewirkt?)
- Primäres Ziel: Tests müssen immer laufen bzw. im Fehlerfall so schnell wie möglich wieder gefixt werden (sollte ein gemeinsames Ziel für alle Entwickler sein)

### Alle Ändern den Quellcode auf dem Hauptzweig

Das ist eine doofe Idee. Aber gemäss Vorlesung:

- Wenn möglich, immer auf Hauptzweig commiten. Dafür kleinere aber häufigere Changes

### Bei einer Änderung wird automatisch ein Build durchgeführt.

Buildserver prüft regelmässig auf Veränderungen im Versionskontrollsystem (poll), bzw. wird vom SCM aktiv informiert (push).
Alle Resultate des Build werden offensiv kommuniziert (Testfälle, Laufzeit, Metriken, usw.).

Gemeinsames Ziel für das Team: Sobald ein Build bricht sollte es die erste Priorität sein, den Build zu stabilisieren. So soll ein stabiler Build jederzeit sichergestellt werden.

### Der Buildprozess muss schnell sein

Je schneller die Entwickler ein Feedback bekommen dass etwas nicht mehr läuft, je besser!
Natürlich muss ein Kompromiss gefunden werden – manche Tests benötigen mehr Zeit. Eine Möglichkeit ist, zwei (oder mehr) Builds durchzuführen:

- Schneller "continuous build" für Feedback an die EntwicklerInnen
- Langsamer, umfangreicher Build über Nacht (nightly build)

### Auf/mit Kopien der produktiven Umgebung testen

Die zentrale Build- und Testumgebung sollte möglichst ähnlich zur produktiven Umgebung sein, zum Beispiel:

- ähnliche Hardwareausstattung
- Betriebssystem
- Laufzeitumgebung (z.B. Java)
- Netzwerkzugriff und Kommunikation mit Drittsystemen
- Datenqualität und Datenmenge

Bei kleinen Systemen in der Realität gut zu erreichen, bei grossen Systemen aber häufig zu teuer.

### Einfacher Zugriff auf aktuelle Buildartefakte

Die Buildresultate sollten jederzeit für weitere (typisch manuelle) Tests zur Verfügung stehen.
Wird typisch über Buildserver erreicht, welche Buildresultate archivieren können.
Zusätzlich werden die binären (ausführbaren) Artefakte zusätzlich noch in ein binäres Repository deployed.

### Offensive Information über den aktuellen Zustand

Es gibt keine Geheimnisse! Offene Information nicht zur Kontrolle, sondern als gegenseitige Unterstützung!

Für alle ist jederzeit einsehbar welche Änderungen:

- von wem und wann eingecheckt wurden
- von welchem Build erstmals erfasst wurden
- zu welchen Ergebnissen geführt haben (Build, Tests)
- zu welchem issue gehören
- welche Massnahmen getroffen wurden
- etc

### Automatisches Deployment (CD)

Wenn immer möglich sollte das Buildergebnis auch automatisch verteilt werden.
Damit steht die aktuelle Software sofort wieder für weiterführende, (z.B. manuelle) Systemtests bereit:

- hat ein schnelleres Feedback zur Folge
- vermeidet Meldungen von Fehlern, die schon behoben sind

Siehe auch DevOps.

## Sie verstehen die Vorteile beim Einsatz von Entwurfsmustern.

> Bewährte objektorientierte Entwürfe (Schablonen) für ein wiederkehrendes Problem

- Wiederverwendung von bewährten Entwurfsmustern als Ziel.
- Verschiedene Arten von Wiederverwendung in der Softwareentwicklung:
  - Objekte zur Laufzeit wiederverwenden.
  - Wiederverwendung von Quellcode / Klassen.
  - Wiederverwendung von einzelnen Komponenten.
  - Einsatz von Klassen-Bibliotheken / Frameworks.
  - Wiederverwendung von Konzepten, z.B:
    - Entwurfs-, Architektur- oder Kommunikationsmuster



## Sie kennen verschiedene, ausgewählte Entwurfsmuster.

WELCHEEE???

## Erzeugungsmuster

### Ziel

Hier ist das Ziel die Abstrahierung der Erzeugung von Objekten. Entscheidung über: 

- zu verwendenden konkreten Typ
- Zeitpunkt der Erzeugung
- Art der Erzeugung (Kontext, Initial-Erzeugung)

### Beispiele

Die folgenden Muster gehören zur Gruppe der Erzeugungsmuster:

- Abstrakte Fabrik (Abstract Factory, Kit)
- Erbauer (Builder)
- Fabrikmethode (Factory Method, Virtual Constructor)
- Prototyp (Prototype)
- [Einzelstück (Singleton)](#singleton)

#### Singleton

Durch die Verwendung von Singletons kann sichergestellt werden, dass nur eine einzige Instanz einer Klasse instanziert werden kann. Dazu wird der Konstruktor mit dem Zugriffsmodifikator `private` ausgestattet.

**Beispiel-Code:**

```java
public final class Singleton {

    private String displayName
    private static Singleton instance = new Singleton("hello vsk");

    private Singleton(String displayName) {
        this.displayName = displayName;
    }

    public static Singleton getInstance() {
        return this.instance;
    }
}
```

**Remarks:**

Im obigen Beispiel wird die statische Klassenvariable `instance` direkt bei der Deklaration instanziert (*Eager initialization*).
Man kann hier alternativ auch eine *Lazy*-Initialization verwenden, welche das Objekt erst beim ersten Aufruf der `getInstance()` Methode instanziert. 
Der Eager-Ansatz ist einfach umzusetzen, da man sich nicht im selben Umfang um Synchronisations-Probleme kümmern muss. 
Für weitere Informationen über die Implementation eines "perfekten Singletons" [siehe hier](https://medium.com/@kevalpatel2106/how-to-make-the-perfect-singleton-de6b951dfdb0);

**Empfehlung:**

Das Singleton-Pattern hat mittlerweile einen schlechten Ruf. 
Man soll dieses nur zurückhaltend und gezielt einsetzen, niemals als universellen, globalen Zugriffspunkt.

## Strukturmuster

### Ziel

Die Verwendung von Strukturmustern bezweckt jeweils einen der folgenden Punkte:

- Objekte (oder Klassen) zu grösseren oder veränderten Strukturen zusammenfassen
- Unterschiedliche Strukturen einander anzupassen und miteinander zu verbinden

### Beispiele

- [Adapter (Adapter, Wrapper)](#adapter-wrapper)
- Brücke (Bridge, Handle/Body)
- Dekorierer (Decorator, Wrapper)
- [Fassade (Facade)](#facade)
- Fliegengewicht (Flyweight)
- Kompositum (Composite)*
- Stellvertreter (Proxy, Surrogate)*

#### Facade

Das Facade-Pattern stellt eine zusammengefasste Schnittstelle zu einer Menge von Schnittstellen mehrerer Subsysteme zur Verfügung.

**Beispiel:**

![Example Facade Pattern](assets/facadepattern.png)

Die Fassade weiss nichts über die konkreten Implementationen der einzelnen Methoden.
Sie kennt lediglich die Subklassen und deren Zuständigkeiten und delegiert die Anfragen entsprechend. 
Die Subklassen wiederum wissen nichts über ihre Verwendung in der Fassade, es besteht keinerlei Referenz.

Für Beispielcode und weiterführende Erklärung [klicke hier](https://www.geeksforgeeks.org/facade-design-pattern-introduction/).

**Ziel:**

Dieses Entwurfsmuster vereinfacht die Anwendung mehrerer Subsysteme und minimiert die Abhängigkeiten zu den Subsystemen - die Kopplung wird minimiert. 
Der Austausch bzw. die Ablösung eines Subsystems (beispielsweise infolge Refactoring) wird enorm vereinfacht, da der Aufruf der konkreten Implementation zentral in der Fassade erfolgt. Es verbirgt daher auch die Komplexität der Subsysteme hinter einer einfach verwendbaren Fassade.

**Empfehlung:**

Das Facade-Pattern kann einfach zur Entkopplung eingesetzt werden. 
Es ist hauptsächlich darauf zu achten, dass die Fassade keinerlei weitere Funktionenn bzw. Business-Logic enthält!

#### Adapter (Wrapper)

Durch das Adapter-Pattern wird die Schnittstelle einer Klasse an die von den Klienten erwartete (Ziel-)Schnittstelle angepasst. In der echten Welt gibt es viele Adapter, die als Beispiel funktionieren, z.B.: Ein USB zu Ethernet Adapter. Diese sind eigentlich zueinander inkompatibel, aber der Adapter übersetzt.

Für alternative Erklärung inkl. Beispiel [siehe Artikel auf geeksforgeeks](https://www.geeksforgeeks.org/adapter-pattern).

![Example Adapter Pattern](assets/adapterpattern.png)

##### Teilnehmer

- Interface (*hier `LogPerisistor`*): gewünschte Schnittstelle, kann abstrakte Klasse oder Interface sein
- Adapter (*hier `StringPersistorAdapter`*): verwendet adaptierte Klasse/Objekt, spezialisiert oder implementiert Zielschnittstelle
- Adaptierte Klasse (*hier `StringPersistor`*): Klasse, deren Schnittstelle adaptiert/gerwappt werden soll

##### Motivation

- Einfachere Wiederverwendung von existierenden Klassen oder Komponenten, deren Schnittstelle aber unpassend ist.
- Implementation einer möglichst allgemeinen Schnittstelle und diese durch Adapter anpassen.

## Verhaltensmuster

### Ziel

Die Verhaltensmuster decken jeweils einen oder mehrere der folgenden Punkte ab:

- Beschreibung der Interaktion zwischen Objekten
- Festlegen der Kontrollflüssen zw. Objekten
- Delegation der Zuständigkeit und/oder Kontrolle

### Beispiele

- Befehl (Kommando, Command, Action, Transaction)
- Beobachter (Observer, Dependents, Publish/Subscribe, Listener)*
- Besucher (Visitor)
- Interpreter (Interpreter)
- Iterator (Iterator, Cursor)*
- Memento (Memento, Token)
- Plugin (Plugin)
- Schablonenmethode (Template Method)
- Strategie (Strategy, Policy)
- Vermittler (Mediator)
- Zustand (State, Objects for States)
- Zuständigkeitskette (Chain of Responsibility)

#### Strategy-Pattern

Beim *Strategy*-Pattern werden verschiedene Implementationen derselben Methode generalisiert bzw. austauschbar gemacht.
Ein Interface schreibt die zu implementierenden Methoden (gleich Verhalten) vor. 
Verschiedene Implementationen dieses Interfaces stellen dann die konkreten Verhaltensweisen zur Verfügung.

Die Klassen, welche die vorgeschriebenen Methoden verwenden, halten sich jeweils die konkrete Implementation in einer Variable des Interface-Typs, damit das Verhalten ausgetauscht werden kann. 
Vorzugsweise wird die konkrete Implementation im Konstruktor übergeben oder per *Dependency Injection* injiziert.

![Example Strategy Pattern](assets/strategypattern.png)

##### Teilnehmer

- Strategie (*hier `Sortable`*): Vollabstrakte Klasse oder Interface, definiert Schnittstelle
- Kontext (*hier `Context`*): optional, kann direkt durch Client erledigt werden
  - Besitzt Referenz auf konkrete Strategie, erstellt diese ggf. selber
  - Stellt ggf. Datenschnittstelle für Strategien zur Verfügung
  - Meinung: Nur verwenden, wenn dies nicht Concern des Clients ist, bzw. wenn das SRP verletzt würde.
- Konkrete Strategien (*hier `BubbleSort`, `MergeSort` etc.*): Implementieren konkreten Algorithmus, greifen ggf. auf Kontext zu

##### Motivation

- Anbieten von unterschiedlichen Implementationen eines Algorithmus
- Eng verwandte Klasen, die sich nur im Verhalten unterscheiden, zusammenfassen
- Vermeiden von unzähligen Bedingungsanweisungen in der/den aufrufenden Klasse(n)

##### Empfehlung

Dieses Pattern wird leicht unterschätzt und kann sich bereits bei sehr kleinen Methoden lohnen. 
Es lassen sich z.B. grosse `switch`-Statements oder viele aufeinanderfolgende `if`-Anweisungen eliminieren.
Die Entscheidung, welche konkrete Implemenation verwendet werden soll, kann der aufrufenden Klasse (z.B. Client) abgenommen und an einem adäquaten Ort vorgenommen werden.

#### Beobachter

Definiert eine Abhängigkeit zwischen einem Subjekt (Observable) dessen Zustand ändern kann, und einer Menge von Beobachtern (Observer) die darüber informiert werden sollen

![1560418025167](assets/1560418025167.png)

Teilnehmer:

- Subjekt - Observable: Verwaltet seine Beobachter (0..n) und bietet Methoden zur An- und Abmeldung an
- Beobachter - Observer: Definiert eine Benachrichtigungsschnittstelle
- Konkretes Subjekt / Konkreter Beobachter: Konkrete Typen senden und empfangen Aktualisierungen

Motivation:

- Wenn nur eine lose Kopplung der Zuhörer bestehen soll/darf.
- Wenn die Anzahl der vorhandenen Zuhörer nicht interessiert.
- Zur Kommunikation entgegen der Abhängigkeitsrichtung.
- Auch zur Auflösung von zyklischen Referenzen.

Sehr typisch für MVC: Änderungen des Modelles müssen an die verschiedenen Views propagiert werden.

##### Event/Listener in Java

In Java nutzt man als Ersatz für das Observer-Pattern das Event/Listener Pattern (in unserem VSK Projekt ebenfalls eingesetzt bei dem Logger-Viewer als Entkoppelung der RMI Kommunikation. RMI-Client leitet die Nachrichten an die registrierten Beobachter (der Viewer) weiter).

![1560418234591](assets/1560418234591.png)



Namensgebung:

- Event -> ist das eigentliche Subjekt (folgend als `XXX`)
- Eventquelle (verwaltet die Beobachter)
  - `public addXXXListener(...)`
  - `public removeXXXListener(...)`
  - `public fireXXXEvent(...)`
- Listener (Beobachter):
  - `public XXX[Event|Performed]` (in unserem Projekt: `notify(Event)`)



**Bei Java konsequent das Event-/Listener-Modell verwenden!** Es ist deutlich besser und flexibler als das reine Observer-Pattern.

##  Sie können geeignete Entwurfsmuster auswählen und gezielt einsetzen.

Okay

## Sie kennen die verschiedenen Testarten und sind in der Lage gute Unit- und Integrationstests zu schreiben

## Unit Tests

Sind funktionale Test von einzelnen, in sich abgeschlossenen Units (typisch Klasse, aber auch Komponente oder Modul).
Unit Tests müssen auf einem beliebigen System und jederzeit lauffähig sein.
Unit Tests sollen nie aufgrund von Fremdeinflüssen fehlschlagen.
Der Nutzen von Unit Tests hat folgende positive und negative Aspekte.

**Positiv**:

- Neue oder veränderte Komponenten können sehr schnell getestet werden (regressiv).
- Automatisiertes, übersichtliches Feedback / Reporting.

**Negativ**:

- Für GUI-Komponenten etwas aufwändiger
- Zu viele Tests verhindern innovation
- Qualität und Nachvollziehbarkeit der Testfälle muss im Auge behalten werden: Qualität vor Quantität!
- In manchen Architekturen / Umgebungen schwierig umsetzbar.

**Ziele** von guten Unit Tests:

- schnell
- einfach ausführbar
- selbstvalidierend
- automatisiert
- lose Kopplung

## Integrations Test

Testfälle welche mit I/O interagieren sind Integrationstests.

## Sie beherrschen die Entwicklung nach dem Test First Prinzip.

isi bro

## Sie nutzen Werkzeuge zur Messung der Codeabdeckung aktiv zu Verbesserung Ihres Codes und der Testfälle

Jep

## Sie kennen das Prinzip der Dependency Injection.

jääjo

## Sie verstehen was Test Doubles sind und können sie erklären.

Ein _Double_ ist ein Platzhalter für die echte, produktive Implementation während Tests.

Hauptsächlich dienen Test Doubles dazu den Aufwand für Integrations-Tests zu reduzieren.
Somit können _fast integrative_ Tests schnell, häufig, überall lauffähig, und vollständig automatisiert ausgeführt werden.

Häufig spricht man unpräzis nur von Mocks und Mocking.
Es gibt **Dummies, Stubs, Spies, Mocks und Fakes**:

![Test Double Klassenhierarchie](assets/test-doubles.png)

Mit Dummies und Stubs erreicht man eine bessere Testisolation durch einfache Ersatzimplementationen.
Mit Spies und Mocks kann das Verhalten einfacher testen.
Mit einem Fake erreicht man die vollständige Entkopplung zu einer Abhängigkeit.

## Dummy

Ein Dummy ist eine sehr primitive und oft **leere** Ersatz-Implementation.
Er dient zur **funktionslosen** Entkopplung von unerwünschten Abhängigkeiten.

**Beispiel**:
Einem Objekt muss ein Logger übergeben werden. 
Weil das Loggen ist nicht das eigentliche Testziel, kann man mit einem Dummy einen Logger übergeben der nichts macht.

## Stub

Ein Stub ist eine einfache Implementation, welche sinnvolle, vordefinierte Werte zurückliefert.
Erleichtert es Tests mit verschiedenen Zuständen (States) zu testen.
Ein Zustand (State) ist bei Stubs in der Regel konstant.
Daher werden für die unterschiedlichen Testziele auch oft mehrere unterschiedliche Stubs erstellt.

## Spy

Ein Spy ist eine alternative Implementation, welche dynamische Werte zurückliefert.
Unteranderem misst ein Spy folgende Metriken von Methoden:

- Anzahl/Häufigkeit
- Parameter
- Zeitpunkt
- Exceptions

Erleichtert es das Verhalten (Behavior) von Klassen zu testen.

## Mock

Ein Mock ist eine Spezialisierung eines Spy.
Im Unterschied zu einem Spy kann ein Mock eine korrekte Interaktion selbst verifizieren.
Einziger Unterschied ist der Ort der Verifikation, Mocks sind dadurch spezifischer.

## Fake

Ein Fake ist eine alternative Implementation einer Komponente. Erleichtert es die vollständige Entkopplung einer Abhängigkeit innerhalb von Tests.



## Sie kennen die verschiedenen Arten von Test Doubles und können diese adäquat einsetzen.

Siehe oben

## Sie kennen exemplarische Mocking-Frameworks und können diese nutzen.

Mockito 

##  Sie kennen die verschiedenen Aspekte die es beim Deployment zu beachten gilt.

![Folie](./assets/deployment-aspekt-1.png)
![Folie](./assets/deployment-aspekt-2.png)
![Folie](./assets/deployment-aspekt-3.png)
![Folie](./assets/deployment-aspekt-4.png)
![Folie](./assets/deployment-aspekt-5.png)
![Folie](./assets/deployment-aspekt-6.png)



## Sie verstehen einfache Deploymentdiagramme und können diese erstellen.

### UML 1.x

![Example](./assets/deployment-uml-1.png)

### UML 2

![Example](./assets/deployment-uml-2.png)



## Sie kennen das dreistellige Versionsschema nach «semantic versioning» und können es anwenden.

* `<Major>.<Minor>.<Bugfix/Maintenance>`

## Wie kennen typische Deployment-Artefakte von Java.

- Die häufigste Art von Deployment sind JAR-Dateien.
- Beispiel für Artefakt ch.hslu.vsk:stringpersistor-api:5.0.0:
  - POM (Metainformationen): stringpersistor-api-5.0.0.pom
  - JAR (Binary): stringpersistor-api-5.0.0.jar
  - JavaDoc: stringpersistor-api-5.0.0-javadoc.jar
  - Source (bei OSS): stringpersistor-api-5.0.0-sources.jar
  - Zu allen Artefakten werden noch Hashes produziert.
- Dass die Quellen und die JavaDoc auch als JAR (eigentlich ZIP) geliefert werden ist Konvention und kann Anfänger verwirren.
  - Letztlich aber egal, die Einheitlichkeit ist wichtiger!
- Vorteil, z.B. für Entwicklungsumgebungen:
  Es ist implizit klar, wo die Dokumentation und ggf. der Source für
  ein bestimmtes JAR gefunden wird  Selbstkonfiguration.

## Sie kennen den Zweck eines Binär-Repositories und können dieses nutzen.

Bei Maven ist der zentrale Server ein Maven Repository (OSS).
Es gibt verschiedene öffentliche Repositories zum Abhängigkeiten zu beziehen ([Maven Central](http://repo.maven.apache.org/maven2/), [BinTray](https://bintray.com/bintray/jcenter).
Auf öffentliche Repositores haben nur ausgewählte Personen Schreibrechte.
Unternehmen betreiben in der Regel interne Repositores (z.B. mit [Sonatype/Nexus](https://de.sonatype.com/nexus-repository-sonatype), [JFrog/Artifactory](https://www.jfrog.com/open-source/)).
Auf dem lokalen Rechner existiert auch ein Repository (_$HOME/.m2/repository_) welches zum cachen von Artefakten verwendet wird.
Repositores werden in der Maven Konfiguration (_$HOME/.m2/settings.xml_) definiert.

## Sie kennen die Motivation von Clean Code.



## Sie kennen die Kriterien von Clean Code bezüglich der Implementation von guten Testfällen

## Unit Tests

Gute und umfassende Tests sind die fundamentale Basis für alle weiteren Bemühungen zur Verbesserung der (Code-)Qualität.
Qualität in Form von Reliability, Changeability, Efficiency, Security, Maintainability, Portability, Reusability etc.

Gute Unit Tests sind die erste, schnellste, einfachste Teststufe. Sie bieten schnelles erstes Feedback ob es funktioniert und dieenen als Regression, als auch als Basis für jedes Refactoring.

Nach Roy Osherove ist die Definition eines Unit Tests wie folgt: 

> A unit test is an automated piece of code that invokes a unit of work in the system and then checks a single assumption about the behavior of that unit of work.

### Test Driven Development (TDD)

Die drei Gesetze des TDD:

1. Produktiver Code darf erst implementiert werden, wenn es dafür einen Unit-Test gibt.
2. Dieser Unit-Test darf nur gerade so viel Code enthalten, dass er fehlerfrei kompiliert, aber als Test scheitert.
3. Man ergänzt jeweils nur gerade so viel produktiven Code, dass der scheiternde Test besteht.

Der Zyklus dieses Ablaufes liegt dabei im Bereich von Sekunden bis Minuten!
Tests und Produktivcode werden praktisch zeitgleich geschrieben; Tests eilen nur wenig voraus.

### Saubere Unit Tests

Für Testcode sollen die identischen Qualitätsstandards gelten wie für produktiven Code!

Drei Dinge machen einen sauberen Unit Test aus:

1. Lesbarkeit durch Klarheit
2. Lesbarkeit durch Einfachheit
3. Lesbarkeit durch Ausdrucksdichte

Jeder Testfall nutzt das Build-Operate-Check-Pattern (vergleiche Triple A):

1. Erstellen der Testdaten
2. Manipulieren der Testdaten
3. Verifikation der Ergebnisse

Um den Code lesbarer zu machen schreiben uns ein domänenspezifisches Set von (typisch statischen) Utility-Methoden.
Diese machen den Testcode kompakter und aussagekräftiger.

```java
assertResponeIsXML()
assertResponseContainsElement()
```

Des weiteren ist es ein Ziel nur ein `assert` pro Test zu haben.
Nicht immer sinnvoll umsetzbar, aber wenn: VIEL VIEL VIEL VIEL BESSER! (YEAH VOLL COOL, YUHU)

Weniger (bzw. keine) assert-Messages notwendig, weil die Testfälle selber schon sehr selektiv sind.

Aus bei Tests soll maan SLA, SRP und SOC einhalten:

- Single Level of Abstraction (SLA)
- Single Responsibility Principle (SRP)
- Separation of Concerns (SoC)

Ein untrügliches Zeichen für Verletzung: Eine Testmethode wird in mehrere Abschnitte gegliedert, vielleicht sogar noch mit Kommentarblöcken unterteilt.

### F.I.R.S.T Prinzip

Das First Prinzip besteht aus folgenden Begriffen:

- **Fast**: Tests sollen schnell sein, damit man sie jederzeit und regelmässig ausführt.
- **Independent**: Tests sollen voneinander unabhängig sein, damit sie in beliebiger Reihenfolge und einzeln ausgeführt werden können.
- **Repeatable**: Tests sollten in/auf jeder Umgebung lauffähig sein, egal wo und wann.
- **Self-Validating**: Tests sollen mit einem einfachen boolschen Resultat zeigen ob sie ok sind oder nicht.
- **Timely**: Tests sollten rechtzeitig, d.h. vor dem produktiven Code geschrieben werden. 

### Uncle Bob's Unit-Test Heuristiken

Unclue Bob's Unit-Test Heuristiken bestehen aus folgenden 9 Heuristiken:

1. Unzureichende Tests vermeiden (Ziel: 100% Testabdeckung wegen Murphy's Law)
2. Coverage-Werkzeug verwenden (machen es leicht ungetesteten Code audzudecken)
3. Triviale Tests nicht überspringen
4. Deaktivierte Tests sind ein Waarnsignal (Temporär ok, aber nie für immer)
5. Grenzbedingungen testen (Meist wird «die Mitte» eines Algorithmus richtig implementiert, aber seine Grenzen falsch beurteilt)
6. Fehler-Nachbarschaft gründlich testen (Findet man in einer Klasse / Funktion einen Fehler sollte man diese erschöpfend testen. Es besteht eine hohe Wahrscheinlichkeit, dass darin noch weitere Fehler gefunden werden.)
7. Muster des Scheiterns zur Diagnose nutzen
8. Hinweise von Coverage Patterns nutzen (beim Troubleshooting von Tests)
9. Tests sollen schnell sein (Need for speed!)

## Sie kennen die Kriterien von Clean Code zur Implementation von guten Methoden.

### Anforderungen an Funktionen

1. Funktionen sollten klein sein
2. Pro Funktion nur eine Aufgabe (SRP und "to"-Ansatz)
3. Nur eine Abstraktionsebene pro Funktion (SLA)
4. Switch-Anweisungen vermeiden (SRP, OCP, DRY)
5. Anzahl der Funktionsargumente minimieren (max. 3)
6. Kein Flag-Argumente (formale Parameter).
7. Keine Nebeneffekte einbauen
8. Output-Argumente vermeiden
9. Anweisungen und Abfragen trennen
10. Keine Fehlercodes, besser Exceptions!
11. Fehlerverarbeitung ist eine Aufgabe (separate Methode)
12. Gute Namensgebung von Funktionen (weniger als 20 Zeilen im Schnitt, max 100 Zeilen, max. zwei Ebenen)

### Uncle Bob's Funktions Smells

1. Zu viele Argumente (max. 3)
2. Output Argumente 
3. Flag-Argumente 
4. Tote Funktionen 