# Deployments

## Lernziele

### Sie kennen die verschiedenen Aspekte die es beim Deployment zu beachten gibt

### Sie verstehen einfache Deploymentdiagramme und können diese erstellen

### [anki] Sie kennen SemVer und können es anwenden

### Sie kennen Sinn und Zweck eines Binär-Repository und können dieses nutzen

### Sie kennen verschiedene Deployment-Arten von Java und können diese umsetzen

## Übersicht
Ein Deployment besteht aus folgenden Punkten:
  - **Verteilung**: Versand von Datenträgern mit Programm und Dokumentation, zur Verfügung stellen von entsprechenden Downloads, automatisiertes Installation (z.B. Java Webstart).
  - **Installation**: Kopieren der nötigen Dateien an die vorgesehenen Orte und Registrieren der Anwendung, allenfalls überprüfen, ob das Zielsystem für die Anwendung geeignet ist. 
  - **Konfiguration**: Einstellungen der/des Programme(s) auf Benutzer, Netzwerkumgebung, Hardware etc. 
  - **Organisation**: Information, Schulung, Support, Planung, Produktion

Ein Deployment findet auf jeden Fall am ende eines Projektes statt.
Jedoch auch früher/häufiger bei Continuous Delivery (so z.B. am Ende nach jedem Sprint oder nach jedem entwickelten Feature).
bei Continuous Deployment werden einezlne Build-/Sprint-/Iterationsergebnisse forlaufend deployt (z.B, auf interne Testumgebungen oder direkt beim Kunden).

> Staging ist Deployment auf verschiedenen Umgebungen (Entwicklung, Test, Integration, Produktion, usw.)

Technisch gesehen besteht ein Deployment aus folgenden Aspekten:
  - **Deployment Diagramme** (Zuordnung Komponenten/Hardware)
  - **Installations- und Deinstallationsprogramme/-skripe**
  - **Konfiguration** (Default~, Beispiel~,etc.)
  - **Installationsmedium**
  - **Repositories** 

Organisatorisch gesehen besteht ein Deployment aus folgenden Aspekten:
  - **Konfigurationsmanagement** (Welche Komponenten bilden welchen Release?)
  - **Installations- und Bedienungsanleitungen**
  - **Erwartungsmanagement** (Welche Funktionalität ist vorhanden?)
  - **Bereitstellung von Support**

> Deployment-Dokumentation als Quelle der Information!!!!

### Aspekte (ein Müll)

![Folie](./assets/deployment-aspekt-1.png)
![Folie](./assets/deployment-aspekt-2.png)
![Folie](./assets/deployment-aspekt-3.png)
![Folie](./assets/deployment-aspekt-4.png)
![Folie](./assets/deployment-aspekt-5.png)
![Folie](./assets/deployment-aspekt-6.png)

## Deployment Diagramme

### UML 1.x

![Example](./assets/deployment-uml-1.png)

### UML 2

![Example](./assets/deployment-uml-2.png)

## Versionierung

### Semantic Versioning
Einmal [SemVer.org](https://semver.org/) durchlesen...

### Release Notes
Sauberes Nachführen von allen Änderungen, Erweiterungen und Korrekturen.
Meist manuell nachgeführt, da qualitative Aussage.
Evt. unterstützt durch Issue-Tracking-Systeme.
Für Entwickler die zentrale Informationsquelle um die Möglichkeit bzw. die Notwendigkeit einer Migration auf eine neue Version (und das damit verbundene Risiko) einschätzen zu können.

## Technisches Deployment

![Folie](./assets/deployment-technical-1.png)
![Folie](./assets/deployment-technical-2.png)
![Folie](./assets/deployment-technical-3.png)
![Folie](./assets/deployment-technical-4.png)
![Folie](./assets/deployment-technical-5.png)
![Folie](./assets/deployment-technical-6.png)
