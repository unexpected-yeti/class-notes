# Verteilung & Kommunikation (RMI)

> TODO: Claudio macht noch (https://elearning.hslu.ch/ilias/goto.php?target=file_4028968_download&client_id=hslu)[https://elearning.hslu.ch/ilias/goto.php?target=file_4028968_download&client_id=hslu]

## Begriffserklärungen

### Verteilte Systeme

Ein verteiltes System ist ein System, in dem sich Hardware- und Softwarekomponenten auf vernetzten Computern befinden und miteinander über den Austausch von Nachrichten kommunizieren.

### Verteilte Anwendungen

Eine verteilte Anwendung nutzt ein verteiltes System als Kommunikationsinfrastruktur für ihre verteilten Komponenten.

### Middleware

Middleware (englisch für Dienste-Schicht oder Zwischenanwendung) oder Vermittlungssoftware bezeichnet in der Informatik anwendungsneutrale Programme, die so zwischen Anwendungen vermitteln, dass die Komplexität dieser Applikationen und ihre Infrastruktur verborgen werden.

Sie sind transparent in Bezug auf [verschiedene Aspekte](#transparenz).

#### Kategorien

Middlewares werden in die folgenden Kategorien unterteilt:

- **Kommunikationsorientiert**: Der Schwerpunkt liegt in der Abstraktion der Netzwerkprogrammierung (RPC, RMI, Web-Service)
- **Nachrichtenorientiert**: Arbeitet über Austausch von Nachrichten mithilfe von Warteschlangen (JMS, SOAP)
- **Anwendungsorientiert**: Im Mittelpunkt steht neben Kommunikation v.a. die Unterstützung verteilter Anwendungen (Hazelcast, JEE, Microsoft .NET und WCF, CORBA)

### Transparenz

- **Ortstransparenz:** Benutzer kennt Lokation einer Ressource oder eines Dienstes nicht
- **Zugriffstransparent:** Zugriff auf Ressource erfolgt immer identisch, egal ob sich diese lokal oder entfernt im Netz befindet.
- **Nebenläufigkeitstransparenz:** Mehrbenutzerbetrieb wird von Diensten und Ressourcen unterstützt. Das System ermöglicht exklusive Zugriffe und Datensynchronisation und -replikation.
- **Fehler- und Ausfalltransparenz:** Typische durch Verteilung entstehende Fehler (Übertragungsfehler, Komponentenausfall etc.) bleiben der Anwendung weitgehend verborgen.
- **Sprachtransparenz:** Die Kommunikation zwischen den Komponenten ist unabhängig von der jeweils verwendeten Programmiersprache.
- **Replikationstransparenz:** Aus Performancegründen kann es mehrere Kopien derselben Ressource geben. Das System sorgt für die transparente Änderung der darin vorgenommenen Änderungen.

## Architekturmodelle

### Client-Server / Peer-to-Peer

* Client-Server: langlebender Server, kurzlebende Client-Prozesse
* Peer-to-Peer: Gleichberechtigte Prozesse laufen lokal und tauschen nur bei Bedarf untereinander Informationen aus, es wird kein zentraler Prozess benötigt.

### Fat-Client und Thin-Client

* Fat-Client: Verarbeitung der Daten i.d.R. vor Ort vollzogen, oftmals stellt es auch ein GUI zur Verfügung
* Thin-Client: Stark auf die Hilfe anderer Computer oder Server angewiesen ist um seine Computeraufgaben zu erfüllen

### Multi-Tier Architektur (2-Tier, 3-Tier und n-Tier)

* 2-Tier: Präsentation, Anwendungslogik und Datenhaltung auf zwei Anwendungen verteilt
* 3-Tier: Die Anwendungslogik erhält einen eigenen Tier
* n-Tier: Verteilung der Anwendungslogik und Datenhaltung auf mehrere Tiers

## RMI (Remote Method Invocation)

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

#### Parameterübergabe

- Elementare Datentypen: können wie gewöhnlich *by value* übergeben werden.
- Lokale Objekte: können nur übergeben werden (oder als Rückgabewerte), wenn sie serialisierbar sind (Implementation des `Serializable` Interfaces); werden als Kopie übergeben (also auch *by value*)
- Verweise auf Remote-Objekte: werden z.B. vom Namensservice zurückgegeben und werden als Objektreferenzen (*by reference*) behandelt.

### RMI in Java

- Sprachelement seit JDK 1.1
- RMI-Compiler zur Stub-Erzeugung: rmic.exe (seit 1.5 von der Runtime übernommen)
- Remote-Protokolle
    - JRMP: Java Remote Method Protocol
    - RMI-IIOP: Java Remote Method Invocation (RMI) über Internet Inter-Orb Protocol (IIOP)

#### Vorgehen

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



### RMI Push Prinzip

* Das Remote-Interface bietet eine Registrierungsmethode als Dienst zur Verfügung
* Der Server (hier Logger Server) implementiert dieses Interface und erzeugt eine Remote-Instanz, diese Instanz wird bei der Registry registriert
* Der Viewer erzeugt ein Remote Push Receiver und exportiert diesen in die RMI Runtime (implizit oder explizit möglich)
* Der Viewer holt sich die Remote-Referenz zum Server und registriert sich (übergibt den Receiver für den Remote Push)
* Der Server ruft den Receiver bei Bedarf auf, um Nachrichten an den Client zu senden

#### Callback Beispiel (Fibonacci)

* Der Server stellt einen Dienst zur Berechnung einer Fibonacci Zahl zur Verfügung (kann bei grossen Zahlen eine längere Zeit dauern). Dazu ruft der Server intern die Methode `calc` auf.
* Wenn der Client die Methode des Server aufruft gibt er eine Referenz zu sich mit
* Der Fibonacci rechnet die Zahl asynchron und benachrichtigt den Client nach Abschluss der Berechnung. Dies macht er über ein Callback des Clients. Der Client stellt also eine Methode zur Verfügung (z.B. `handle`), die der Server aufrufen kann

Aufbau:

* Remote Schnittstellen:
  * `RemoteFibonacci` für die Berechnung der Fibonacci Zahl
  * `RemoteCallbackHandler` für den Callback
* RMI Server
  * `FibonacciImpl` implementiert den Server-Dienst zur Berechnung
  * `Request`, hier wird die eigentliche Berechnung durchgeführt
  * `FibonacciServer` erstellt die RMI Registry, erzeugt das Remote Objekt (`FibonacciImpl`)
* RMI Client
  * `FibonacciTask` implementiert den Callback und den Aufruf der Remote Methode `calc`
  * `FibonacciClient` erzeugt einen `FibonacciTask` und lässt diesen asynchron / nebenläufig ausführen

#### Verwendung der RMI Registry vom Server

* Server holt sich über die Methode `getRegistry` der Klasse `LocateRegistry` eine Referenz zur lokalen Registry. Aus Sicherheitsgründen kann ein RMI Server Referenzen von Remote Objekten nur in einer lokalen Registry registrieren
* `getRegistry` ermöglicht eine Referenz zur Registry auf dem lokalen Host auf einem Default Port (1099) oder einem spezifizierten Port.

#### Verwendung der RMI Registry vom Client

* Der RMI Client holt sich mit Hilfe der Klasse LocateRegistry und der Methode getRegistry eine Referenz zur Registry.
* Die getRegistry Methode ermöglicht eine Referenz zur Registry
  * auf dem lokalen Host am Default Port (1099) oder
  * auf dem lokalen Host an einem spezifizierten Port oder
  * auf einen entfernten Host am Default Port oder
  * auf einen entfernten Host an einem spezifizierten Port.

### RMI Remote Code Base

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

![1560420176718](./assets/1560420176718.png)

Codebase einrichten:

* Das Property `java.rmi.server.codebase` gibt die Codebase an, für Klassen welche die JVM benötigt. Das Property wird via `System.setProperty(...)` gesetzt, z.B. `System.setProperty("java.rmi.server.codebase", "http://localhost:8080/")`
* Sobald Code von Remote geladen wird ist ein Security Manager notwendig

Codebase zur Verfügung stellen:

* Am einfachsten: Die Klassen-Bytecode via HTTP-Server zur Verfügung stellen
* Wichtig: Der HTTP-Server benötigt Zugriff auf die .class-Dateien (und keine Java Archives (jar)!)
* JDK hat selbst einen HTTP-Server (in den neuen Versionen nicht mehr dabei), oder via Nginx/Apache oder ähnliches (z.B. mit Python `python -m http.server 8080`)



### RMI Security Manager

Java unterscheidet zwischen lokalem und remote Code bezüglich der Sicherheitsanforderungen:

* Lokaler Code hat Zugriff auf alle verfügbaren Ressourcen
* Remote Code hat eingeschränkten Zugriff, er kann z.B. nicht:
  * auf Dateien auf dem lokalen Computer zugreifen
  * Netzwerkverbindungen öffnen, die auf einen anderen Host als von dem der Code geladen wurde verbinden
  * Netzwerkverbindungen auf privilegierten Ports (< 1024) akzeptieren
  * Lesen von benutzerbezogenen System-Properties ("user.name", "user.home" etc)
  * Ausführen von externen Programmen
  * Laden von System-Libraries

#### Security Manager aktivieren

* `java.lang.SecurityManager` (seit JDK1.2) bietet eine Default-Implementierung an, die folgende Möglichkeiten hat:
  * Aktivieren über die Kommandozeile via `-Djava.security.manager`
  * Instanziieren des SecurityManagers via `System.setSecurityManager(new SecurityManager())`
  * `System.getSecurityManager()` prüft ob ein Security Manager aktiviert ist
* Man kann eine eigene Security Policy definieren. Dies wirdin einer Text-Datei (sog. policy file) statt im Code definiert.

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

* Codebase: Vergibt Rechte für Klassen, die von einem bestimmten Ort kommen.
* Signierung: Es wird nur das Recht eingeräumt, wenn Programmcode signiert ist.
* Principal: Gewährt bestimmte Rechte für authentifizierte Benutzer. 

#### Beispiel Policy für Fibonacci Calculator

* Die RMI-Registry muss Rechte besitzen, um
  * am Registry Port 1099 hören können
  * Verbindung zu Codebase Port 8080 machen können
  * Verbindungen mit lokalen Prozess Ports akzeptieren können
  * Verbindungen mit Client Prozess Ports akzeptieren können
* Der RMI-Server muss Rechte besitzen, um
  * Verbindung zu Registry Port 1099 machen können
  * Verbindung zu Codebase Port 8080 machen können
  * Verbindungen mit lokalen Prozess Ports akzeptieren können
  * Verbindungen mit Client Prozess Ports akzeptieren können

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

#### Zusammenfassung

* Beim Push Prinzip in einem verteilten System übergibt der Client dem Remote Objekt eine Remote Callback Referenz auf sich selbst.
* Das Remote Callback Objekt muss für die RMI Middelware exportiert werden.
* Um den RMI Server zu entlasten wird die RMI Registry als eigene Komponente erstellt und ausgeführt.
* Wenn Remote Objekte als Argumente übergeben werden, muss eventuell Byte-Code (Code der kompilierten Klasse) nachgeladen werden.
* Um Byte-Code während der Laufzeit nachzuladen, wird eine entsprechende Codebase (Quelle für den Code) und einen Security Manager mit Policy (Berechtigungen für den Zugriff) benötigt.