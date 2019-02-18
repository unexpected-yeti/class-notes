# Database Theory

## Lernziele
Siehe auch Meier & Kaufmann (2016) Kapitel 1.1; 1.2.3; 1.3; 1.4.3

### Das Konzept Datenbank definieren und erklären
Eine Datenbank ist eine Datenbanksystem (zur Verwaltung von Datenbeständen) und eine Datenbasis (die Daten), welche zusammen als Einheit gekapselt sind.

### Die Konzept Informationssystem und Datenbanksystem abgrenzen
Eine Datenbank ist ein Teil eines Informationssystems.

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

#### Was ist der Unterschied zwischen einm Datenbank-System und einem Dateisystem?
In einem Dateisystem kann jedes Anwenderprogramm direkt auf die Daten zugreifen.
Beim Datenbanksystem passiert dies via das DBMS.

#### Was ist der Unterschied zwischen einer SQL- und einer NoSQL-Datenbank?

#### Was ist der Unterschied zwischen Datenbanken und Datenmanagement?

#### Inwiefern handelte es sich gemäss der Datenbanktheorie bei IDS um eine Datenbank?

### Gruppenarbeiten

#### Was ist eine mögliche eigene Definition des Begriffs Datenbanken? Formulieren Sie Ihre eigene Definition in Ihren Worten

#### Warum ist eine XML-Datei keine Datenbank?

#### Welche Vor- und Nachteile hat aus Ihrer Perspektive der Einsatz von Datenbanken? Bzw. welche Vor- und Nachteile hat die Verarbeitung mit Dateien? Vergleichen Sie.

### Präsentation

#### Welchen Bezug haben Sie persönlich zum Thema Datenbanken?

#### Welches Beispiel von Datenbanken aus der Praxis können Sie uns im Detail erklären?

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

## Nicht-relationale Datenbanken
Der Begriff NoSQL wird heute für nicht-relationale Ansätze im Datenmanagement verwendet, mit folgenden zwei Bedingungen:
- Die Speicherung der Daten erfolgt nicht in Tabellen
- Die Datenbanksprache ist nicht SQL 

Nicht-relationale Datenbanken sind stark für parallele Ausführungen und haben schwache bis starke Konsistenzgewährung.

Die Daten werden in Spalten, Dokumenten oder Graphen gespeichert.
Dabei existieren in der Regel verteilte Datenreplikate.

## Big Data: 3V
Daten welche in die drei untenstehenden Dimensionen an Quantität und Qualität fallen werden oft Big Data genannt:
- *Volume:* Der Datenbestand ist umfangreich und liegt im Tera- bis Zettabytebereich.
- *Variety:* Speicherung von strukturierten, semi-strukturierten und unstrukturierten Daten.
- *Velocity:* Der Begriff bedeutet Geschwindigkeit und verlangt, dass Datenströme (engl. data streams) in Echtzeit ausgewertet und analysiert werden können.

SQL-Datenbanken sind nicht für Big Data ausgerichtet. Aus diesem Grund werden vermehrt NoSQL-Datenbanksysteme eingesetzt.

