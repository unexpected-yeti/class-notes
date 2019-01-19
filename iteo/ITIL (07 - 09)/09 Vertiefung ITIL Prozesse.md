# 09 - Vertiefung ITIL-Prozesse

## Stoffabgrenzung

* Sie kennen ITIL Vers. 3 und dessen Phasenmodell und Prozessgruppen
* Sie kennen und verstehen die wichtigsten IT-Betriebsprozesse aus ITIL V3 und deren Bedeutung für das
  Unternehmen.
* Sie kennen folgende ITIL-Prozesse vertieft: Continual Service Improvement, Service Asset & Configuration Mgmt., Change Mgmt., Software Deployment, Incident Mgmt.
* Die ausgewählten und als Experte bearbeiteten IT-Betriebsprozesse aus der Testatübung gehören dazu.
* Die zu den vertieften Prozessen zugehörigen Kapitel im Buch ITIL V3 gehören auch zum Prüfungsstoff.

## Prozessgruppen

* ITILv3 basiert im Kern auf dem Service Lifecycle
* Der Service Lifecycle beschreibt den Lebenszyklus des IT-Services
  von der Erfassung der Anforderung über die Gestaltung,
  Implementierung und den Betrieb bis hin zur kontinuierlichen
  Anpassung der Servicequalität und letztlich der Außerbetriebnahme.
* Im Mittelpunkt steht also nicht mehr die Prozesse als solche,
  sondern der zu liefernde Service.



## ITIL v3

* Good Practice Framework
* Öffentlich Zugänglich, seit Ende 80er Jahre entwickelt, besteht heute aus 5 Kern-"Büchern"
* ITIL beschreibt die Prozesse, die einen effektiven und effizienten Betrieb der gesamten IT-Infrastruktur ermöglichen



## Service Lifecycle

![1542631301540](assets\1542631301540.png)

## Prozessgruppen im Überblick

### Service Strategy

* Ausgangspunkt für alle Aktivitäten im Lifecycle
* Führt ITSM als organisatorische Fähigkeit und deren strategischen Wert
* Ausrichtung von Business und IT
* Ziele identifizieren, neue Chances und Möglichkeiten neuer IT Services
* Kosten & Risiken des Service Portfolio betrachen

#### Wichtige Fragen

 * Welche Services sollen wem angeboten werden?
 * Wie unterscheiden wir uns vom Wettbewerb?
 * Wie erzeugen wir echten Nutzen für unsere Kunden?
 * Wie definieren wir Servicequalität?
 * Wie finden wir den richtigen Weg zur Serviceoptimierung?
 * Wie gestalten wir die Services wirtschaftlich?

#### Prozesse

 * Strategy Management for IT-Services
 * Service Portfolio Management
 * Financial Management
 * Demand Management
 * Business Relationship Management

### Service Design

Beschreibt den Entwurf und Entwicklnug von IT Services.

Aktivitäten:

 Planung und Gestaltung neuer und veränderter Services
 Service-Management-Systeme und Tools, wie Service
Portfolio und Servicekatalog
 Planung und Gestaltung von Technologie und Architektur
 Planung und Gestaltung der benötigten Prozesse
 Planung und Gestaltung von Messmethoden und
Metriken

#### Prozesse

 Design Coordination
 Service Catalogue Management
 Service Level Management
 Availability Management
 Capacity Management
 Information Security Management
 IT Service Continuity Management
 Supplier Management

### Service Transition

Beschreibt kontrollierte Überführung von neuen und geänderten IT-Services in den IT-Betrieb:

* Stellt eine Anleitung und Prozessaktivitäten für den Übergang der Services in die Business-Umgebung bereit
* Behandelt auch Themen wie Veränderungen der Unternehmenskultur, Wissens- und Risikomanagement

#### Wichtige Aufgaben und Ziele sind:
 * Erkennen und Steuern der Kundenerwartungen bezüglich neuer und geänderter Services.
 * Übereinstimmung neuer oder geänderter Services mit den in den Service Requirements spezifizierten Anforderungen und Sachzwängen
 * Integration neuer oder geänderter Services in den BusinessProzess des Kunden
 * Serviceveränderungen werden in Bezug auf Kosten, Zeit und Qualität überwacht und gesteuert
 * Die effektive Umsetzung der definierten Servicestrategie in den Betrieb der Services ist sichergestellt

#### Prozesse

 * Transition Planning & Support
 * Change Management
 * Service Asset & Configuration Mgmt.
 * Release & Deployment Management (*Installation, Software verteilen etc.*)
 * Service Validation & Testing (*Produktionstest, im Verbund mit anderen Services testen*)
 * Change Evaluation (*"Qualitätsmanagement des Service Transition"*)
 * Knowledge Management

### Service Operation

Beschreibt den effizienten und effektiven **Betrieb**, **Support** und **Unterhalt** der IT-Services



#### Aufgaben und Ziele

Monitoring und Reporting zur optimierten Entscheidungsfindung
beim Steuern von Verfügbarkeit, Nachfrage, Kapazität und aller
weiteren Belange des Betriebs
• Sammeln und Bereitstellen von Informationen, Rückmeldungen
und Ideen als Basis für den kontinuierlichen
Verbesserungsprozess
• Sicherstellen der Verfügbarkeit und Stabilität der Services
• Bearbeiten und Beseitigen von Incidents und Problems

#### Prozesse

 Event Management (Monitoring)
 Incident Management
 Problem Management *(Probleme, die immer wieder auftreten)*
 Request Fullfilment *(Benutzeranfragen erledigen, z.B. Könnt ihr mir ein File restoren)*
 Access Management *(AuthZ)*



#### Funktionen

Sind nicht Prozesse; sondern OEs - diese verwenden die oben geführten Prozessen.

* Service Desk
* Technical Management
* IT-Operations Management
* Application Management



## Zielkonflikte Service Operation

![1542632338636](assets\1542632338636.png)



Ein Serviceprovider muss den IT-Betrieb so ausrichten, dass er eine akzeptierte Balance zwischen Stabilität und Reaktionsfähigkeit findet.

## Service Asset & Configuration Management

> Das Service Asset und Konfiguration Management (SACM) hilft den Überblick darüber zu behalten, welches Equipment vorhanden ist, wo es ist und wofür es verwendet wird.

* Konfiguration Management ist mehr als Asset Management – es legt ein logisches Abbild der (relevanten)   IT und ihrer Beziehungen an
* Es ist die zentrale Basis für alle IT-Betriebsprozesse und deren Automatisierung
* Stellt in Zusammenarbeit mit dem Change Management sicher, dass Einträge richtig und aktuell sind
* Hilft bei der schnellen Problemlösung durch besseres Verständnis der Infrastruktur



### Ziel & Zweck

Bereitstellung von aktuellen und konsistenten Informationen
- zur Konfiguration der IT-Infrastruktur
  und
- über alle zur Service-Erbringung benötigten Komponenten

### Configuration Management - Definition

* Verwaltung IT-Metadaten
* Umfasst **alle** IT-Objekte (administrative Informationen wie z.B. Pikett-Team / Verantwortliche, + [...] todo)
* Stellt Datenqualität sicher

SACM Prozess:

![1542635039786](assets\1542635039786.png)



## Terminologie

### CI - Configuration Item

> Ein CI ist eine IT-Komponente, welche unter der Kontrolle des Configuration Managements steht. Alle CIs stehen unter der Kontrolle des Change
> Managements. 

Diese können wie folgt klassifiziert werden:
- Hardware
- Software
- Dokumente
- Verträge
- Konfigurationen
- Beziehungen SW und HW
- Software-Konfiguration (SW- und Instanz-bezogen)
- IT-Services
- Gebäude 

Je nach Typ werden unterschiedliche Informationen zur betreffenden
Konfigurationseinheit benötigt und unterschiedliche Anforderungen gestellt.
Typische Attribute sind:
 Eindeutige Bezeichnung
 CI-Typ (HW, SW, etc.)
 Name
 Beschreibung
 Version
 Hersteller
 Status (in Betrieb, defekt, …)
 Beziehungen zu anderen CI (Abhängigkeiten)
 Owner
Hardware wird Beispielsweise in vielen Unternehmen mit einer eindeutigen
**Inventarnummer** versehen. Ein Gerät oder eine Komponente kann dadurch
schnell identifiziert werden. Neben den üblichen Bezeichnungen des Gerätes
und der Kategorie (PC, Drucker, Monitor) gehören auch geräte-spezifische
Informationen dazu.



### CMDB / CMS

* Applikation, welche die Daten verwaltet
*  Die CMDB verwaltet Daten, die in mehr als einem Systems Management Bereich
  bzw. mehr als einem Prozess benutzt werden, in einer (möglicherweise
  föderierten) Datenbank und stellt diese Daten über definierte Schnittstellen zur
  Verfügung.
   Diese Configuration Management Database (CMDB) ermöglicht eine prozess- und
  werkzeugübergreifende Informationsverarbeitung. Erst die integrative
  Beschreibung der Datenbestände und die Verknüpfung der Dateninseln
  ermöglichen durchgängige Betriebsprozesse.
   Wesentliche Funktionen sind:
  - Verwaltung Konfigurationseinheiten (CIs)
  - Versionierung sämtlicher Komponenten
  - Beschreibung des Zusammenspiels der einzelnen Komponenten, z.B. SW und Rechner
  - Journalisierung/Historisierung sämtlicher Änderungen auf Personen-Ebene 

## Aufgabe 1

In einem Asset- & Configuration System werden Hardware und Software «typisiert», sprich die einzelnen Geräte und auch die Software werden in Haupt- und Unterkategorien unterteilt, z.B. «Server» (Hauptkategorie) und «Linux», «Wintel» und «HP-UX» (Unterkategorie).



Hardware:

* Server
  * Intel
  * Solaris
  * ...
* Mainframe
* Client
  * Desktop
  * Laptop
* ...



Software:

* Base
  * OS
  * Directory SW
  * Security SW
  * ...
* Middleware
  * DBMS
  * Webserver
  * Appserver
  * ...
* Application
  * Büro-Appl
  * Business-Appl



## Rollen

### Configuration Manager (Process Owner)
Der Configuration Manager ist als Process Owner ganzheitlich für den Erfolg des
Configuration Management verantwortlich. Zu den Verantwortlichkeiten zählen:
 Planung und Überwachung der Aktivitäten im Configuration Management
 Definition und Pflege von Schnittstellen zu anderen Prozessen, z.B.
Change Management
 Überwachung und Sicherstellung der Datenqualität
 Tool-Evaluierung und Auswahl für das CMS
 Definition eindeutiger Konventionen für Configuration Items (z. B.
Namenskonventionen, CI-Typen, Versionen, Templates)
 Pflege und Aktualisierung des CMS
 Reporting an andere Prozesse und an das Management



### Configuration Administrator
Inhaber dieser Rolle sind verantwortlich für
 die Durchführung der Pflegeaktivitäten im Service Asset and Configuration
Management sowie
 für die Bereitstellung der Informationen und des Status der gespeicherten CI.
 Sie unterstützen den Configuration Manager bei der Pflege des Service-Asset-andConfiguration-Management-Planes

### Datenverantwortlicher / Data Owner
Die Daten werden an der Quelle aufgrund klar definierter Rollen und Autorisierungen
erfasst. Für jede Entität ist ein Datenverantwortlicher bestimmt, der die Daten im Rahmen
eines definierten Prozesses pflegt. Mehrfacherfassungen werden dadurch vermieden.

### CMS Tools-Administrator
Der CMS/Tools-Administrator ist verantwortlich für die
 Funktionsfähigkeit und Weiterentwicklung des CMS
 und die anforderungsgerechte Konfiguration der eingesetzten Tools.



## KPI

Folgende KPIs sind für das CM relevant:

* Dimension Qualität:
  * Datenaktualität und –qualität der Konfigurationsdaten
  * Anteil erfolgloser RFC aufgrund falscher oder fehlender Informationen aus dem CMS
  * Quote genutzter Lizenzen in Bezug zu gekauften Lizenzen
*  Dimension Wirtschaftlichkeit:
  * Stückkosten pro Konfigurationsitem für Erfassung und Pflege
* Dimension Leistung:
  * Verfügbarkeit: Soll-/Ist-Vergleich der geplanten und effektiven Zeiten



![1542637350098](assets\1542637350098.png)



## Change Management

CM kontrolliert:

* alle Veränderungen an vorhandenen Services
* das Hinzufügen von neuen Services
* die Ausserbetriebnahme von Services

### Ziele

1. Effiziente & effektive Durchführung von Changes
2. Negative Auswirkungen von Veränderungen auf Geschäftsprozesse minimieren
3. Störungen und Service-Unterbrechungen auf Grund von Changes reduzieren
4. Unnötige Nacharbeiten minimieren

Erweiterte Ziele:

1. Anforderungen aus Business & IT zur **Ausrichtung der Services auf die Geschäftsanforderungen** erfüllen
2. Changes in **angemessener Zeit durchführen**
3. **Dokumentation** aller Changes sicherstellen
4. Genehmigte Changes werden: priorisiert, geplant, getestet, implementiert und überprüft
5. Stellt sicher, dass **alle Änderungen** an Configuration Items im **Configuration Management System** dokumentiert sind
6. Risiken für das Business reduzieren

### Begriffe

* **Request for Change (RFC)**: Antrag zur Durchführung eines Service Change; Basis für die Bewertung, Planung und Genehmigung des Changes
* **Change Schedule (CS)**: Enthält alle genehmigten Changes inklusive des geplanten Datums der Implementierung
* **Change Model**:
  * Vordefinierte & dokumentierte Abläufe um Changes durchzuführen. Gemäss ITIL sollten folgende Elemente enthalten sein:
    * Arbeitsschritte und Umgang mit unvorhergesehenen Ereignissen
    * Zeitliche Reihenfolge der Arbeitsschritte
    * Verantwortlichkeiten während Durchführung
    * Zeitvorgaben & Schwellwerte, die zu einer Eskalation führen können
    * Vorgehensweise bei Eskalation
  * Change Arten:
    * Normale Changes
    * Standard Changes
    * Emergency Changes (SOS)
  * Standard Change ist das wohl am weitest verbreitete Change Model

### Standard Change

* Entlastet CM von unnötiger Bürokratie
* Für einfache, häufig wiederkehrende Changes mit überschaubarem Risiko
* Vom Change Management bewertet und **einmalig vorab genehmigt**
* Finanzielle Freigabe ist im Voraus erteilt oder liegt im Verantwortungsbereich des Antragstellers
* **Risiko niedrig** und immer **bekannt**
* Standard Change beinhaltet:
  * Bedingungen für Auslösung
  * Definiertes Startereignis (Trigger)
  * Detaillierte Beschreibung der für die Durchführung erforderlichen und bewährten Aktivitäten
  * Definierte Personen / Gruppen (z.B. Service Desk) für Durchführung
* **Beispiel**: Installation eines Arbeitsplatzes (Desktop / PC)

### Aufgaben

* **Kommunikation** mit den Beteiligten
* **Steuerung** der durchzuführenden Changes
* **Planung** der Changes (ab RFC bis Nachbearbeitung)
* **Zeitplanung** für die Change-Durchführung
* **Bewertung** der Changes bzgl. Risiken und Auswirkungen
* **Autorisierung** der Changes
* Erstellen von **Management Reports**

### Ablauf

![1542724649873](assets\1542724649873.png)

### Rollen

#### Change Manager

* **Steuert** Zielerreichung des Change-Management-Prozesses
* Verantwortet:
  * Zielerreichung des Change-Management-Prozesses
  * Annahme, Filterung, Dokumentation und Priorisierung der RFC
  * Einberufen des CAB ( Change Advisory Board) und Vorlage der relevanten Changes
  * Autorisieren der Changes, ggf. nach Abstimmung mit dem CAB
  * Bereitstellen der Change-Planung
  * Koordinieren der Change-Erstellung, der Tests und der Implementierung
  * Review aller implementierten Changes
  * Schließen der RFC nach Abschluss der Implementierung und des Review
  * Bereitstellen des Management Reportings

#### Change Advisory Board (CAB)
 * Changes bewerten, genehmigen und planen
 * Technische sowie Business-Sicht vertreten
 * Mitglieder: Kundenverteter, Spezialisten (Entwickler), Lieferanten, Anwendervertreter, Change Manager, Service Owner

#### Emergency CAB (ECAB)
 * Bei zeitkritischen Changes mit in der Regel hohen Auswirkungen
 * Muss kurzfristig erreichbar sein
 * Besitzt Autorität für notwendige Entscheidungen

### Herausforderungen

Die Ziele des CM:
 * Auswirkungen von Changes minimieren
 * Innovationsfähigkeiten zu erhalten

Dies führt zum Abwägen zwischen Flexibilität und Stabilität:

![1542724938422](assets\1542724938422.png)

# Software Deployment / Release Management

## Ziele

>  Erfolgreiche Integrationen von Releases in die geplante Zielumgebung unter Einhaltung der vorgegebenen Zeitplanung ohne Beeinträchtigung oder Störung des laufenden Betriebs.

## Build

Ein Build kann alles zusammenfassen:

* Änderungen, Ergänzungen, Neuerungen, Updates, Patches, Anpassungen dürfen nicht einfach ausgebreitet werden.
* Planung, Integration, Tests, Kundenvorbereitung und diverse Randbedingungen müssen feste und stabile  Umgebungen gewährleisten.

## Begriffe

* **Release Unit**:
  * Getestete und ausgerollte Einheit
  * Enthält Services, Applikationen und IT-Equipment, die Abhängigkeiten haben
  * Level wird von Geschäftsprozessen beinflusst
  * Kann relativ gross sein, gegenseitige Beeinflussung
* **Release Package**:
  * Kann aus mehreren Release Units bestehen
  * Definiert alle Veränderungen, um neue Baseline zu erreichen
  * Enthält auch Dokumente, Handbücher und Checklisten die zusammen benötigt werden
* **Release Cycle**:
  * Täglich, wöchentlich, monatlich etc.
  * Kann zu oft erfolgen, zu viele kleine Änderungen (kann nervig sein)

## Release- und Deployment-Modelle

Modelle haben folgende Informationen:

- Kriterien für Start und Ende eines Releases
- Release-Struktur (Gestaltung des Release Package und Informationen zur Zielumgebung)
- Beschreibt die Entwicklungs- und Testumgebungen, Rollen, Zeitpläne, Templates und Vorgaben für die Dokumentation sowie Übergabe- und Abnahmekriterien für die Durchführung

Optionen:

* **Big Bang**: Alles auf einmal; rasche Einführung; höheres Risiko für Fehler
* **Phased**: gestaffelt nach z.B. Standort, Funktion; Hoher Zeitbedarf, Learning von Phase zu Phase
* **Push**: Aktive Verteilung mit "Zwang"; Rasche Verteilung; Oft Benutzerbeeinträchtigung
* **Pull**: SW-Kiosk, evtl. fixer Endtermin, weniger Störungen des Benutzers durch Nutzung von Rand- oder Pausenzeiten

## Rollen im R&D Management

* **Release & Deployment Manager**
  * Verantwortet Steuerung aller Aspekte des kompletten Release-Prozesses, sowie:
  * Kommunikation während des Rollouts (Kundenzufriedenheit)
  * Aktualisierung von Service Knowledge Management System (SKMS) sowie Configuration Management System (CMS) bei Implementierung
  * Gestaltung & Betrieb der Testumgebung
  * Rollout-Planung
  * Einhaltung von Richtlinien & Release-Prozessen
  * Design, Erstellung und Konfiguration der Releases
  * Testdurchführungen und Erfüllung der Akzeptanzkriterien
  * Freigabe für die Implementierung
* **Release Packaging & Build Manager**
  * Zusammenstellung & Funktion eines Releases
  * Finale Tests eines Releases
  * Dokumentation der Ereignisse sowie ggf. Known-Errors und Workarounds innerhalb eines Releases
  * Informationen für die Release-Freigabe

## KPI im R&D

Was bewirkten KPIs im R&D?

* Verbesserung Kundenzufriedenheit bzgl. gelieferter Srevices
* Termintreue bei Implementierung neuer Services
* Weniger Unterbrüchen an den Services aufgrund Releases
* Weniger Fehler bei der Release-Planung
* Weniger Nachbesserungen pro Release

## Herausforderungen

Schnittstelle zum Change Management:

* nur ein **klar definiertes Ziel** des Rollouts und
* die **genau bekannten Erwartungen** des Kunden ermöglichen,
* einen **perfekt gestalteten Release-Management Prozess** und
* einen Service auszurollen, der den Kunden **zufriedenstellt**

Unklare Voraussetzungen oder Erwartungen machen eine genaue Zielerfüllung unmöglich!



# Continual Service Improvement

> Continual Service Improvement (CSI) ist im Kern ein Qualitätsmanagement für die angebotenen Services und die Service Management Prozesse.

Qualitätsmanagement für die Service Management Prozesse

## Ziel

Die Effektivität und Effizienz der IT-Services und der Service Mgmt. Prozesse kontinuierlich zu verbessern.

Folgende Voraussetzungen müssen erfüllt sein:
• Die Ergebnisse des Service Level Mgmt. sind betrachtet und analysiert.
• Benötigte Anpassungen zur Verbesserung der IT-Servicequalität
sowie der Prozesseffizienz und -effektivität sind identifiziert und
implementiert.
• Die Balance zwischen wirtschaftlicher Erbringung der IT-Services und
Kundenzufriedenheit ist gewährleistet und wird ständig verbessert.

## Prozesse

CSI hat genau 1 Prozess:

- 7-Step Service Improment

## Methoden

- Service Reporting
- Service Measurement

## "Demming" Zyklus

![1543236552138](assets\1543236552138.png)

* **Plan**: Ziele & Massnahmen erstellen, Rollen und Verantwortlichkeiten definieren
* **Do**: Umsetzung und Dokumentation
* **Check**: Messdaten erhoben und in Reports zusammengefasst
* **Act**: Abweichungen identifizieren, Korrekturmassnahmen, Input für neue Planungsphase (**Plan**)
* **Control**:  Erstreckt sich über alle Phasen, stellt sicher dass die definierten Aufgaben und Aktivitäten sowie Ergebnisse dokumentiert werden

## 7-Step Prozess

"Aufgeblasener Demming Zyklus"

**Könnte Prüfungsrelevant sein**

![1543237612532](assets\1543237612532.png)



## Methoden des CSI

### Service Measurement

* Notwendig, IT-Services strukturiert messen
* 2 Aspekte: Verfügbarkeit, Performance (Antwortzeiten)
  * Wichtig: End2End Betrachtung

### Service Reporting

* Reporting; Pro Service - Aussage über Performance und Verfügbarkeit
* Empfänger: Business, IT-Management, IT-interne Stellen



### KPIs in CSI

Reifegrad (0 - 5)

![1543237943600](assets\1543237943600.png)

