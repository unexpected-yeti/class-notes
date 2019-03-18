# Automated testing

## Lernziele

### Sie kennen die verschiedenen Testarten und sind in der Lage gute Unit- und Integrationstests zu schreiben.

### Sie beherrschen die Entwicklung nach dem Test-First Prinzip.

### Sie nutzen Werkzeuge zur Messung der Codeabdeckung aktiv zu Verbesserung Ihres Codes und der Testfälle.

### Sie kennen das Prinzip der Dependency Injection (DI).

### Wie wissen was Test Doubles sind und können Mocking- Frameworks einsetzen.

## Motivation

Wir testen kontinuierlich während der Implementation, um die Gewissheit zu haben dass es funktioniert!
Eine Methodik um kontinuirlich zu testen ist der Test First Ansatz, enwickelt aus XP.


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

## Integrations Test

Testfälle welche mit I/O interagieren sind Integrationstests.

## Tests mit JUnit

Tests werden unter _src/test/java/{pkg-name}_ aabgelegt.
Integrationstests werden _{test-name}IT_ benannt.
Unit Tests werden _{test-name}Test_ benannt.

Integrationstest können mit Apache Maven mit dem eigenen Stage _integration-test_ ausgeführt werden.
Getrennte Plugins _surefire_ und _failsafe_ weisen die Testresultate auch getrennt (Unit und Integration) aus.

## Code Coverage

Code Coverage ist eine Metrik welche zur Laufzeit misst, welche Quellcodezeilen ausgeführt wurden.
Diese Messung erfolgt meistens bei der Ausführung der Testfälle.
Somit kann eine Aussage gemacht werden, wie umfassend der Code tatsächlich genutzt bzw. getestet wurde!
Eine hohe Coverage ist aber kein Beweis für gute Testfälle oder gar die Fehlerfreiheit des Codes!

Man unterscheidet verschiedene Messtechniken und -werte: 
- Statement Coverage (Line Coverage)
- Branch Coverage
- Decision Coverage
- Path Coverage
- Function Coverage - Race Coverage

Technisch kann Coverage auf folgende Arten umgesetzt werden:
- **Instrumentierung des Codes**: Preprocessor-Makros im Code ergänzen. (Nachteil: Modifizierter Quellcode)
- **Instrumentierung des Bytecodes**: Der Bytecode wird bei/nach der Kompilierung mit Bytecode zur Coverage-Messung ergänzt. (Nachteil: class-Dateien müssen separiert werden)
- **JIT Instrumentierung**: Instrumentiert den Bytecode dirket während des Classloadings. 

### Statement Coverage (Line Coverage)

Misst ob (und wie häufig) eine Codezeile durchlaufen wurde.
Problem: Handelt es sich bei der Zeile z.B. um einen logischen Vergleich/Ausdruck, ist ein einmaliger Durchlauf nicht repräsentativ.

### Branch Coverage

Prüft, dass alle Zweige einer bedingten Anweisung ausgeführt wurden.

### Decision Coverage

Bei Fallunterscheidungen (if, while etc.) wird geprüft, dass alle Teilausdrücke in der Bedingung auf true und false aufgelöst wurden (strenger als Branch Coverage).

### Path Coverage

Bei der Path Coverage wird gemessen, ob alle möglichen Kombinationen von Programmablaufpfäden durchlaufen wurden.

### Function Coverage

Misst auf der Basis der Funktionen ob sie aufgerufen wurden.

### Race Coverage

Konzentriert sich auf Codestellen die parallel ablaufen.

## Dependency Injection

Bei Dependency Injection (DI) erzeugen Klasse/Komponenten ihre Abhängigkeiten nicht selber, sondern lassen sich diese (wahlweise) auch von Aussen übergeben.
Eine sehr einfache Lösung für Dependency Injection ist ein überladener Konstruktor!

**Vorteile** von DI:
- Dependency Inversion Principle (**DIP**)
- Verschiedene Implementationen könnnen genutzt werden.
- Seperation of Concerns (**SoC**) ist erhöht.

