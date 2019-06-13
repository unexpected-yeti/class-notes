# Design Patterns

Im Vorfeld gilt anzumerken, dass die im folgenden verwendeten deutschen Bezeichnungen oft nicht nur lächerlich klingen, sondern wohl auch im Selbststudium oder bei Google-Suchen zu eher bescheidenen Ergebnissen führen. Es wird stark empfohlen, die englischen Bezeichnungen zu verwenden.

## Lernziele

* Sie verstehen die Vorteile beim Einsatz von Entwurfsmustern.
* Sie kennen verschiedene, ausgewählte Entwurfsmuster.
* Sie können konkrete Entwurfsmuster auswählen und gezielt einsetzen.

## Gruppierung

Primär wird nach Zweck gruppiert. Daraus entstandene Gruppen:

- [Creational Patterns (Erzeugungsmuster)](#erzeugungsmuster)
- [Structural Patterns (Strukturmuster)](#strukturmuster)
- [Behavioral Patterns (Verhaltensmuster)](#verhaltensmuster)

Sekundäre Unterteilung:

- Klassenmuster: Beziehungen zu Kompilierungszeitpunkt bereits festgelegt.
- Objektmuster: Beziehungen zur Laufzeit dynamisch veränderbar.

## Ziele

> Elemente wiederverwendbarer, objektorientierter Software

oder

> Bewährte objektorientierte Entwürfe (Schablonen) für ein wiederkehrendes Problem

## Wiederverwendung

* Wiederverwendung von bewährten Entwurfsmustern als Ziel.

* Verschiedene Arten von Wiederverwendung in der Softwareentwicklung:

  * Objekte zur Laufzeit wiederverwenden.

  * Wiederverwendung von Quellcode / Klassen.
  * Wiederverwendung von einzelnen Komponenten.
  * Einsatz von Klassen-Bibliotheken / Frameworks.
  * Wiederverwendung von Konzepten, z.B:
    * Entwurfs-, Architektur- oder Kommunikationsmuster


### Wiederverwendung von Objekten in einer Software während der Laufzeit

* Beispiele:
  * Threads in einem Executor-Pool
  * DB-Connection in einem Connection-Pool

* Effekt:

  * Bessere Performance, höhere Effizienz
  * Geringerer Ressourcenbedarf

* Herausforderung

  * Effiziente Verwaltung der Objekte
  * Hier können Entwurfsmuster bereits konkret helfen!

### Wiederverwendung von Klassen / Source Code
* Copy & Paste -> Schlecht!
* Vererbung -> meistens schlecht!
* Aggregation und Komposition -> Gut! (FCoI!)

Effekte:
* Geringerer Entwicklungsaufwand
* Geringere Fehlerrate (Klassen sind meistens bereits gut getestet)

Herausforderungen:

* Schnittstellen der Klassen eher fremdbestimmt
* Auswahl der geeigneten Klassen / Libraries
* Lernaufwand, Wartung und Weiterentwicklung
* Wiederverwendung von Quellcode ist und bleibt eine grosse Herausforderung

### Wiederverwendung von Komponenten

* Beispiele: Logging-Komponente, Java EE-Beans, Corba-Components, etc.
* Effekte:
  * Geringerer Entwicklungsaufwand, weniger Fehler
  * Ganzheitlicher Ansatz, Blackbox Abstraktion
* Herausforderungen:
  * Anforderungen an die Umgebung und Kontext
  * Abhängigkeit vom Lieferant (intern oder extern) der Komponente
  * Schnittstellen können eventuell inkompatibel sein (daher gute Patterns verwenden)
  * Konfigurationsmanagement (Komponenten verwalten)
  * Wartung und Weiterentwicklung der Komponente

## Alternative: Wiederverwendung von Konzepten

* Vorteil: Konzepte bleiben in der Regel relativ konstant und stabil
* Meistens sind sie ebenfalls unabhängig von der Programmiersprache
* **Die Wiederverwendung von bewährten Entwurfsmustern ist eine sehr elegante, wirkungsvolle,  unproblematische und kostensparende Form von Wiederverwendung!**
* Vergleiche:
  * Kommunikationsmuster wie Handshaking
  * Architekturmuster wie MVC etc.



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

![Example Facade Pattern](./assets/facadepattern.png)

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

![Example Adapter Pattern](./assets/adapterpattern.png)

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

![Example Strategy Pattern](./assets/strategypattern.png)

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

![1560418025167](./assets/1560418025167.png)

Teilnehmer:

* Subjekt - Observable: Verwaltet seine Beobachter (0..n) und bietet Methoden zur An- und Abmeldung an
* Beobachter - Observer: Definiert eine Benachrichtigungsschnittstelle
* Konkretes Subjekt / Konkreter Beobachter: Konkrete Typen senden und empfangen Aktualisierungen

Motivation:

* Wenn nur eine lose Kopplung der Zuhörer bestehen soll/darf.
* Wenn die Anzahl der vorhandenen Zuhörer nicht interessiert.
* Zur Kommunikation entgegen der Abhängigkeitsrichtung.
* Auch zur Auflösung von zyklischen Referenzen.

Sehr typisch für MVC: Änderungen des Modelles müssen an die verschiedenen Views propagiert werden.

##### Event/Listener in Java

In Java nutzt man als Ersatz für das Observer-Pattern das Event/Listener Pattern (in unserem VSK Projekt ebenfalls eingesetzt bei dem Logger-Viewer als Entkoppelung der RMI Kommunikation. RMI-Client leitet die Nachrichten an die registrierten Beobachter (der Viewer) weiter).

![1560418234591](./assets/1560418234591.png)



Namensgebung:

* Event -> ist das eigentliche Subjekt (folgend als `XXX`)
* Eventquelle (verwaltet die Beobachter)
  * `public addXXXListener(...)`
  * `public removeXXXListener(...)`
  * `public fireXXXEvent(...)`
* Listener (Beobachter):
  * `public XXX[Event|Performed]` (in unserem Projekt: `notify(Event)`)



**Bei Java konsequent das Event-/Listener-Modell verwenden!** Es ist deutlich besser und flexibler als das reine Observer-Pattern.

## Empfehlung - Einsatz von Entwurfsmustern

* Man muss die Entwurfsmuster kennen und insb. verstehen. Diese einfach blind zu verwenden ist sinnlos.
* Sinnvolle Auswahl und gut überlegter Einsatz
  * Entwurfsmuster sind keine ultimative Lösung für Alles!
  * Erfahrungen sammeln, diese ist notwendig
  * **Besser kein Muster einsetzen, als das Falsche**
* Sinnvolles Vorgehen:
  * Geht es um Erzeugung, Struktur oder Verhalten?
  * Vor- und Nachteile der Muster abwägen
  * Wenn unentschieden: Wo haben Sie die meisten Variablen? Das Muster mit der grössten Flexibilität auswählen

### Verifikation des Entscheides

* Nach dem man sich für ein Muster entschieden hat, dies unbedingt verifizieren (hat das Muster den gewünschten Effekt erzeugt / das Problem vereinfacht?)
* 