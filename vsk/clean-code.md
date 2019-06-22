# Clean Code - en Schissdreck

## Kommentare

Kommentare sind ein notwendiges Übel - Kommentare \(und auch Dokumentationen\) lügen! Nur im Code liegt die Wahrheit, das ist ein fundamentaler Wechsel des Paradigmas.

_Grundsatz:_ Der beste Kommentar ist derjenige, den man gar nicht zu schreiben braucht!

Akzeptable Kommentare können sein:

* juristische Kommentare \(Copyright etc.\)
* TODO-Kommentare \(aber nur temporär!\)
* verstärkende, unterstreichende Kommentare, welche Dinge hervorheben, die sonst zu unauffällig wären
* Kommentare zur \(Er-\)Klärung der übergeordneten Absicht oder zur expliziten Warnung vor Konsequenzen

Inakzeptable Kommentare sind:

* Redundante Kommentare 
* Irreführende Kommentare
* vorgeschriebene oder erzwungene Kommentare \(sture JavaDoc Kommentare, nur damit sie da sind\)
* Tagebuch- oder Changelog-Kommentare
* Positionsbezeichner und Banner \(zur optischen Unterteilung von grossen Quellcodedateien\)
* Zuschreibungen und Nebenbemerkungen \(Hinweise auf Autor, sinnlose Zusatzbemerkungen\)
* Auskommentierter Code
* HTML\(-formatierte\) Kommentare \(Kommentare müssen direkt lesbar sein\)
* zu viel Kommentar / Information

## Namensgebung

Ein guter Name sollte:

* absolut zweckbeschreibend sein
* Fehlinformationen vermeiden
* Unterschiede deutlich machen \(differenzierend sein\)
* gut aussprechbar und gut suchbar sein
* möglichst keine Codierungen enthalten

Heuristiken zur Namensgebung: 1. Beschreibende Namen wählen 2. Namen passend zur Abstraktionsebene wählen 3. Standardnomenklatur verwenden 4. Eindeutige Namen wählen 5. Namenlänge abhängig vom Geltungsbereich 6. Codierungen vermeiden 7. Namen sollten auch Nebeneffekte beschreiben \(da das Typensystem of scheisse ist ;\)

## Clean Code Developer

Clean Code Developer ist eine wohldefinierte Auswahl von Prinzipien und Praktiken \(in sieben Grade eingeteilt\). Die Basis ist ein Wertesystem basierend auf:

* Evolvierbarkeit
* Korrektheit
* Produktionseffizienz
* Reflexion

### Der erste Grad - Schwarz

Sie wissen nun bereits was Clean Code Developer ist.

### Der zweite Grad - Rot

Prinzipien:

* Don ́t Repeat Yourself \(DRY\) \(CCD:G05\)
* Keep it simple, stupid \(KISS\)
* Vorsicht vor Optimierungen \(Bloch:Item 55\)
* Favour Composition over Inheritance \(FCoI\) \(Bloch:Item 16\) 

Praktiken:

* Die Pfadfinderregel beachten \(CCD:02\)
* Root Cause Analysis \(RCA\)
* Ein Versionskontrollsystem einsetzen
* Einfache Refaktorisierungsmuster anwenden
* Täglich reflektieren

### Der dritte Grad - Orange

Prinzipien:

* Single Level of Abstraction \(SLA\) \(CCD:04\)
* Single Responsibility Principle \(SRP\) \(CCD:05\)
* Separation of Concerns \(SoC\) \(CCD:06\)
* Source Code Konventionen: Namensregeln, Kommentare

Praktiken:

* Issue Tracking
* Automatisierte Integrationstests
* Lesen, Lesen, Lesen
* Reviews

### Der vierte Grad - Gelb

Prinzipien:

* Interface Segregation Principle \(ISP\) \(CCD:08\)
* Dependency Inversion Principle \(DIP\) \(CCD:09\)
* Liskov Substitution Principle \(LSP\) \(CCD:10\)
* Principle of Least Astonishment \(CCD:11\)
* Information Hiding Principle \(IHP\) \(CCD:12\)

Praktiken:

* Automatisierte Unit Tests
* Mockups \(Testattrappen\)
* Code Coverage Analyse
* Teilnahme an Fachveranstaltungen
* Komplexe Refaktorisierungen

### Der fünfte Grad - Grün

Prinzipien:

* Open Closed Principle \(OCP\) \(CCD:14\)
* Tell, don ́t ask \(CCD:15\)
* Law of Demeter \(CCD:16\)

Praktiken:

* Continuous Integration \(CI\)
* Statische Codeanalyse \(Metriken\)
* Inversion of Control Container \(z.B. CDI\)
* Erfahrung weitergeben
* Messen von Fehlern

### Der sechste Grad - Blau

Prinzipien:

* Implementation spiegelt Entwurf \(CCD:18\)
* Entwurf und Implementation überlappen nicht \(CCD:19\)
* You Ain ́t Gonna Need It \(YAGNI\) \(CCD:20\)

Praktiken:

* Continuous Integration \(CI\)
* Iterative Entwicklung
* Komponentenorientierung
* Test First \(CCD:21\)

### Der siebte Grad - Weiss

Weisser Grad vereinigt alle Prinzipien und Praktiken der farbigen Grade. Eine gleichschwebende Aufmerksamkeit ist jedoch sehr schwer zu halten, darum beginnt der Clean Code Developer im Gradesystem nach einiger Zeit wieder von vorne. Die zyklische Wiederholung bringt stetige Verbesserung auf der Basis von überschaubaren Schwerpunkten

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

## Funktionen

### Anforderungen an Funktionen

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
