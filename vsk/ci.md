# Continuous Integration

## Lernziele

* Sie können die Ziele der Continuous Integration (CI) erklären
* Sie kennen die zehn wesentlichen Praktiken der CI.

## Ziele von CI

Ziele bei der Entwicklung von Software nach CI:
  - Immer ein lauffähiges Produkt (Buildresultat) zu haben, damit kontinuirlich getestet werden kann.
  - Bei Fehlern jeder Art möglichst schnell ein Feedback erhalten, durch automatisierte Tests und statische Prüfungen.
  - Im Team parallel entwickeln können und den Überblick nicht verlieren, Integrationsaufwand zu minieren und laufend über den aktuellen Stand auf dem Laufenden zu sein.

## 10 Praktiken von CI

### Einsatz eines (zentralen) Versionskontrollsystem

Sämtliche Quellen-Artefakte welche für den vollständigen Build einer Software benötigt werden unterliegen der Versionskontrolle.

Fähigkeiten des Versionskontrollsystem nutzen:

1. Sinnvolle Commit-Kommentare (z.B. mit Verweis auf ein Issue)
2. Tagging: Bestimmte Versionen markieren (z.B. um einen Release eindeutig zu identifizieren)
3. Branches für parallele Entwicklung (z.B. bugfixing oder feature branches)

### Automatisierter Buildprozess 

Ausschliesslich auf der Basis der aktuellen Quellen aus dem Versionskontrollsystem (VCS). Ausführung auf einem Build-Server. Führt ebenfalls die Testfälle aus.

### Automatisierte Testfälle

* Möglichst viel durch automatisierte Testfälle abdecken.
  * Primär Unit Tests, weil einfach und überall lauffähig.
  * Sekundär auch Integrationstests, z.B. Abhängig von Datenbank.
* Fehlerhafte oder nicht vollständige Implementationen sollen so schnell wie möglich aufdecken werden
  * Bei Integrationstests auch häufig unerwartete Nebeneffekte.
* Bewährt haben sich auf Performance Tests (z.B. hat sich eine Änderung negativ auf die Performance ausgewirkt?)
* Primäres Ziel: Tests müssen immer laufen bzw. im Fehlerfall so schnell wie möglich wieder gefixt werden (sollte ein gemeinsames Ziel für alle Entwickler sein)

### Alle Ändern den Quellcode auf dem Hauptzweig

Das ist eine doofe Idee. Aber gemäss Vorlesung:

* Wenn möglich, immer auf Hauptzweig commiten. Dafür kleinere aber häufigere Changes

### Bei einer Änderung wird automatisch ein Build durchgeführt.

Buildserver prüft regelmässig auf Veränderungen im Versionskontrollsystem (poll), bzw. wird vom SCM aktiv informiert (push).
Alle Resultate des Build werden offensiv kommuniziert (Testfälle, Laufzeit, Metriken, usw.).

Gemeinsames Ziel für das Team: Sobald ein Build bricht sollte es die erste Priorität sein, den Build zu stabilisieren. So soll ein stabiler Build jederzeit sichergestellt werden.

### Der Buildprozess muss schnell sein

Je schneller die Entwickler ein Feedback bekommen dass etwas nicht mehr läuft, je besser!
Natürlich muss ein Kompromiss gefunden werden – manche Tests benötigen mehr Zeit. Eine Möglichkeit ist, zwei (oder mehr) Builds durchzuführen:

* Schneller "continuous build" für Feedback an die EntwicklerInnen
* Langsamer, umfangreicher Build über Nacht (nightly build)

### Auf/mit Kopien der produktiven Umgebung testen

Die zentrale Build- und Testumgebung sollte möglichst ähnlich zur produktiven Umgebung sein, zum Beispiel:

* ähnliche Hardwareausstattung
* Betriebssystem
* Laufzeitumgebung (z.B. Java)
* Netzwerkzugriff und Kommunikation mit Drittsystemen
* Datenqualität und Datenmenge

Bei kleinen Systemen in der Realität gut zu erreichen, bei grossen Systemen aber häufig zu teuer.

### Einfacher Zugriff auf aktuelle Buildartefakte

Die Buildresultate sollten jederzeit für weitere (typisch manuelle) Tests zur Verfügung stehen.
Wird typisch über Buildserver erreicht, welche Buildresultate archivieren können.
Zusätzlich werden die binären (ausführbaren) Artefakte zusätzlich noch in ein binäres Repository deployed.

### Offensive Information über den aktuellen Zustand

Es gibt keine Geheimnisse! Offene Information nicht zur Kontrolle, sondern als gegenseitige Unterstützung!

Für alle ist jederzeit einsehbar welche Änderungen:

* von wem und wann eingecheckt wurden
* von welchem Build erstmals erfasst wurden
* zu welchen Ergebnissen geführt haben (Build, Tests)
* zu welchem issue gehören
* welche Massnahmen getroffen wurden
* etc

### Automatisches Deployment (CD)

Wenn immer möglich sollte das Buildergebnis auch automatisch verteilt werden.
Damit steht die aktuelle Software sofort wieder für weiterführende, (z.B. manuelle) Systemtests bereit:

* hat ein schnelleres Feedback zur Folge
* vermeidet Meldungen von Fehlern, die schon behoben sind

Siehe auch DevOps.
