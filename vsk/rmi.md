# Verteilung & Kommunikation (RMI)

## Begriffserklärungen

### Verteilte Systeme

Ein verteiltes System ist ein System, in dem sich Hardware- und
Softwarekomponenten auf vernetzten Computern befinden und
miteinander über den Austausch von Nachrichten kommunizieren.

### Verteilte Anwendungen

Eine verteilte Anwendung nutzt ein verteiltes System als
Kommunikationsinfrastruktur für ihre verteilten Komponenten

### Middleware

Middleware (englisch für Dienste-Schicht oder
Zwischenanwendung) oder Vermittlungssoftware bezeichnet in der
Informatik anwendungsneutrale Programme, die so zwischen
Anwendungen vermitteln, dass die Komplexität dieser Applikationen
und ihre Infrastruktur verborgen werden.

#### Kategorien

Middlewares werden in die folgenden Kategorien unterteilt:

- **Kommunikationsorientiert**: Der Schwerpunkt liegt in der Abstraktion der Netzwerkprogrammierung (RPC, RMI, Web-Service)
- **Nachrichtenorientiert**: Arbeitet über Austausch von Nachrichten mithilfe von Warteschlangen (JMS, SOAP)
- **Anwendungsorientiert**: Im Mittelpunkt steht neben Kommunikation v.a. die Unterstützung verteilter Anwendungen (Hazelcast, JEE, Microsoft .NET und WCF, CORBA)

### Transparenz

- **Ortstransparenz:** Benutzer kennt Lokation einer Ressource oder eines Dienstes nicht
- **Zugriffstransparent:** Zugriff auf Ressource erfolgt immer identisch, egal ob sich diese lokal oder entfernt im Netz befindet.
- **Nebenläufigkeitstransparenz:** Mehrbenutzerbetrieb wird von Diensten und Ressourcen unterstützt. Das System ermöglicht exklusive Zugriffe und Datensynchronisation und -replikation.
- **Fehler- und Ausfalltransparenz:** Typische durch Verteilung entstehende Fehler (Übertragungsfehler, Komponentenausfall etc.) bleiben der Anwendung weitgehend verborgen.
- **Sprachtransparenz:** Die Kommunikation zwischen den Komponenten ist unabhängig von der jeweils verwendeten Programmiersprache.
- **Replikationstransparenz:** Aus Performancegründen kann es mehrere Kopien derselben Ressource geben. Das System sorgt für die transparente Änderung der darin vorgenommenen Änderungen.