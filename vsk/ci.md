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

### Automatisierter Buildprozess 

Ausschliesslich auf der Basis der aktuellen Quellen aus dem Versionskontrollsystem (VCS).

### Automatisierte Testfälle

Möglichst viel durch automatisierte Testfälle abdecken.
Primär Unit Tests, weil einfach und überall lauffähig.
Sekundär auch Integrationstests, z.B. Abhängig von Datenbank.
Fehlerhafte oder nicht vollständige Implementationen sollen so schnell wie möglich aufdecken werden
Bei Integrationstests auch häufig unerwartete Nebeneffekte.

### Alle Ändern den Quellcode auf dem Hauptzweig

Das ist eine doofe Idee.

### Bei einer Änderung wird automatisch ein Build durchgeführt.

Buildserver prüft regelmässig auf Veränderungen im Versionskontrollsystem (poll), bzw. wird vom SCM aktiv informiert (push).
Alle Resultate des Build werden offensiv kommuniziert (Testfälle, Laufzeit, Metriken, usw.).

### Der Buildprozess muss schnell sein

Je schneller die Entwickler ein Feedback bekommen dass etwas nicht mehr läuft, je besser!
Natürlich muss ein Kompromiss gefunden werden – manche Tests benötigen mehr Zeit.

### Auf/mit Kopien der produktiven Umgebung testen

Die zentrale Build- und Testumgebung sollte möglichst ähnlich zur produktiven Umgebung sein.

### Einfacher Zugriff auf aktuelle Buildartefakte

Die Buildresultate sollten jederzeit für weitere (typisch manuelle) Tests zur Verfügung stehen.
Wird typisch über Buildserver erreicht, welche Buildresultate archivieren können.
Zusätzlich werden die binären (ausführbaren) Artefakte zusätzlich noch in ein binäres Repository deployed.

### Offensive Information über den aktuellen Zustand

Es gibt keine Geheimnisse! 
Offene Information nicht zur Kontrolle, sondern als gegenseitige Unterstützung!

### Automatisches Deployment (CD)

Wenn immer möglich sollte das Buildergebnis auch automatisch verteilt werden.
Damit steht die aktuelle Software sofort wieder für weiterführende, (z.B. manuelle) Systemtests bereit.

Siehe auch DevOps.
