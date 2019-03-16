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

