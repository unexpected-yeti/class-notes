# Database Theory

## Lernziele
Siehe auch Meier & Kaufmann (2016) Kapitel 1.1; 1.2.3; 1.3; 1.4.3

### Das Konzept Datenbank definieren und erklären
Eine Datenbank ist eine Datenbanksystem (zur Verwaltung von Datenbeständen) und eine Datenbasis (die Daten), welche zusammen als Einheit gekapselt sind.

### Die Konzept Informationssystem und Datenbanksystem abgrenzen
Eine Datenbank ist ein Teil eines Informationssystems. 
Bei einem Informationssystem steht der Nutzer im Zentrum, das System hat den Kontext des Benutzers.

Im Unterschied zu einer Datenbank bietet ein Informationssystem auch folgendes (teile können Datenbanken auch):
- Benutzerführung
- Dialoggestaltung
- Abfragesprache
- Manipulationssprache
- Recherchehilfen
- Zugriffsrechte
- Datenschutz

### Die Gründe für den Einsatz von Datenbanken beschreiben
Siehe [Motivation: Weshalb Datenbanken?](#motivation-weshalb-datenbanken?)

### Das Konzept der Relationalen Datenbank definieren und erklären
Siehe [Relationale Datenbanken](#relationale-datenbanken)

### Den Begriff Big Data definieren (3V)
Siehe [Erster Abschnitt Big Data: 3V](#big-data-3v)

### Das Konzept der NoSQL-Datenkbanken definieren und erklären
Siehe [Nicht-relationale Datenbanken](#nicht-relationale-datenbanken)

## Kontrollfragen

### Selbststudium

#### Was ist der Unterschied zwischen einer Datenbank und einem Informationssystem?
Ein Informationssystem erlaubt Anwendern interaktiv Informationen zu speichern und zu verknüpfen, Fragen zu stellen und Antworten zu erhalten.
Im Unterschied ist eine Datenbank eine Software zum speichern, beschreiben und abfragen von Daten.
Die Datenbank kennt keinen Informationsgehalt und ist anwendungsunabhängig.

#### Was ist der Unterschied zwischen einm Datenbank-System und einem Dateisystem?
In einem Dateisystem kann jedes Anwenderprogramm direkt auf die Daten zugreifen.
Beim Datenbanksystem passiert dies via das DBMS.

#### Was ist der Unterschied zwischen einer SQL- und einer NoSQL-Datenbank?
Im Unterschied zu SQL-Datenbanken arbeiten No-SQL-Datenbanken nicht mit Tabellen und verwenden nicht die Datenbanksprache SQL.
Des weiteren erfüllen NoSQL-Datenbanken folgende Eigenschaften nur teilweise:
- Relational Modelliert
- Schematisch
- Sprache SQL
- Dataenunabhängige Architektur
- Mehrbenutzerbetrieb
- Konsistenz
- Datensicherheit und Datenschutz

... und unterstützt die Eigenschaften aus dem Abschnitt [Nicht-relationales Datenbanksystem](#nicht-relationales-datenbanksystem)

#### Was ist der Unterschied zwischen Datenbanken und Datenmanagement?
Eine Datenbank ist das System, welches vom Datenmanagement betrieben und gewartet wird.
Die Datenbank ist eine Software und das Datenmanagement eine organisatorische Tätigkeit.

#### Inwiefern handelte es sich gemäss der Datenbanktheorie bei IDS um eine Datenbank?
> TODO

### Gruppenarbeiten

#### Was ist eine mögliche eigene Definition des Begriffs Datenbanken? Formulieren Sie Ihre eigene Definition in Ihren Worten
Eine Datenbank ist eine Software, welche sich aus einem System (Datenbanksystem) und einer Datenbasis zusammenstellt.
Der Zugriff auf die Daten erfolgt via dem System und nicht via File direkt.

#### Warum ist eine XML-Datei keine Datenbank?
Weil es eine Datei und keine Datenbank, bzw. die Datenbasis aber ohne Datenbanksystem.
Des weiteren ist XML mühsam.

#### Welche Vor- und Nachteile hat aus Ihrer Perspektive der Einsatz von Datenbanken? Bzw. welche Vor- und Nachteile hat die Verarbeitung mit Dateien? Vergleichen Sie.
Nachteile Datenbank:
- Zusätzliche Infrastruktur
- Operationeller und Wartungs Overhead
... 

## Datenbanksysteme
Ein Datenbanksystem besteht aus einer Datenbasis und einem Verwaltungsprogramm. Genauer:
1. System zur Verwaltung von Datenbeständen
2. bestehend aus Datenbasis
3. und Verwaltungsprograammen
4. welche zusammen als Einheit gekapselt sind

Nach Carl August Zehnder ist eine Datenbankverwaltungssystem folgendes:
> Das Datenbankverwaltungsssystem (DBMS = database management system) ist ein leistungsfähiges Programm für die flexible Speicherung und Abfrage von Daten.

Er definiert eine Datenbank wie folgt:
> Eine Datenbank ist eine selbstständige, auf Dauer und für flexiblen und sicheren Gebrauch ausgelegte Datenorganisaation, die einen Datenbestand (Datenbasis) und die dazugehörige Datenverwaltung (dbms) umfasst.

![Database Model](./assets/database_model.png)

## Motivation: Weshalb Datenbanken?
DBMS ermöglichen:
- Persistierung, Strukturierung und Organisation von Daten
- Mehrbenutzerbetrieb: Transaktionsmanagement
- Möglichkeiten für Zugriff und Manipulation von Datensätzen
- Konsistenz und Integrität der Daten
- Sicherheit der Daten
- Effizienz bei Applikationsentwicklung durch Wiederverwendung
- Einfachere Wartung durch Kapselung der Daten (Trennung von Daten und Anwendungen)

## Relationale Datenbanken
In relationalen Datenbanken (SQL-Datenbanken) werden Daten und Beziehung in Tabellen gespeichert.
Dabei entspricht ein Datensatz einer Zeile oder einem Tupel.
Metadaten werden in Systemtabellen gespeichert.

Mit Hilfe der strukturierten Abfragesprache SQL (Structured Query Language) können Daten abgefragt werden.
Dies gilt auch für Spezialfunktionen (Recovery, Reorganisation, Sicherheit, Datenschutz, etc.).

Zusammenfassend sind relationale Datenbanksysteme integrierte Systeme zur einheitlichen Verwaltung von Tabellen.

### Relationales Datenbanksystem
Ein Relationales Datenbanksystem ist durch folgende Eigenschaften charakterisiert:
- *Model:* Das Datenbankmodell unterliegt dem Relationenmodell, d. h. alle Daten und Datenbeziehungen werden in Form von Tabellen ausgedrückt.
- *Schema:* Die Definition der Tabellen und der Merkmale werden im relationalen Datenbankschema abgelegt. Dieses enthält zudem die Definition der Identifikationsschlüssel sowie Regeln zur Gewährung der Integrität.
- *Sprache:* Das Datenbanksystem umfasst SQL für Datendefinition, -selektion und -manipulation. Die Sprachkomponente ist deskriptiv.
- *Architektur:* Das System gewährleistet eine große Datenunabhängigkeit, d.h. Daten und Anwendungsprogramme bleiben weitgehend voneinander getrennt.
- *Mehrbenutzerbetrieb:* Das System sorgt dafür, dass parallel ablaufende Transaktionen auf einer Datenbank sich nicht gegenseitig behindern oder gar die Korrektheit der Daten beeinträchtigen.
- *Konsistenzgewährung:* Das System stellt Hilfsmittel zur Gewährleistung der Datenintegrität (fehlerfreie und korrekte Speicherung) bereit.
- *Datensicherheit und Datenschutz:* Das Datenbanksystem bietet Mechanismen für den Schutz der Daten vor Zerstörung, vor Verlust und vor unbefugtem Zugriff.

## Nicht-relationale Datenbanken
Der Begriff NoSQL wird heute für nicht-relationale Ansätze im Datenmanagement verwendet, mit folgenden zwei Bedingungen:
- Die Speicherung der Daten erfolgt nicht in Tabellen
- Die Datenbanksprache ist nicht SQL 

Nicht-relationale Datenbanken sind stark für parallele Ausführungen und haben schwache bis starke Konsistenzgewährung.

Die Daten werden in Spalten, Dokumenten oder Graphen gespeichert.
Dabei existieren in der Regel verteilte Datenreplikate.

### Nicht-relataionales Datenbanksystem
Ein Nicht-relationales Datenbanksystem ist durch folgende Eigenschaften charakterisiert:
- *Modell:* Das zugrundeliegende Modell ist nich relational.
- *Mindestens 3V:* Volume, Variety und Velocity wird unterstützt.
- *Schema:* Das System unterliegt keinem fixen Schema.
- *Architektur:* Die Architektur unterstützt masssiv verteilte Webanwendungen und horizontale Skalierung.
- *Replikation:* Datenreplikation wird unterstüzt.
- *Konsistenzgewährleistung:* Aufgrund des CAP-Theorems ist die Konsistenz lediglich verzögert gewährleistet (weak consistency), falls hohe Verfügbarkeit und Ausfalltoleranz angestrebt wird.

## Big Data: 3V
Daten welche in die drei untenstehenden Dimensionen an Quantität und Qualität fallen werden oft Big Data genannt:
- *Volume:* Der Datenbestand ist umfangreich und liegt im Tera- bis Zettabytebereich.
- *Variety:* Speicherung von strukturierten, semi-strukturierten und unstrukturierten Daten.
- *Velocity:* Der Begriff bedeutet Geschwindigkeit und verlangt, dass Datenströme (engl. data streams) in Echtzeit ausgewertet und analysiert werden können.

SQL-Datenbanken sind nicht für Big Data ausgerichtet. Aus diesem Grund werden vermehrt NoSQL-Datenbanksysteme eingesetzt.

In einigen Definitionen wird im Rahmen von Big Data auch von Informationskapital und Vermögenswert gesprochen.
Aus diesem Grund fügen einige Experten ein weiteres V hinzu:
- *Value:* Big Data Anwendungen sollen den Unternehmenswert steigern. 

Es liegen unterschiedliche Qualitäten von Datenbeständen vor.
Dies muss bei der Auswertung berücksichtigt werden.
Daher werden die drei oder vier V oft mit dem letzten V abgerundet:
- *Veracity (Aufrichtigkeit oder Wahrhaftigkeit):* Da viele Daten vage oder ungenau sind, müssen spezifische Algorithmen zur Bewertung der Aussagekraft resp. zur Qualitätseinschätzung der Resultate verwendet werden.

> Umfangreiche Datenbestände garantieren nicht per se bessere Auswertungsqualität!

