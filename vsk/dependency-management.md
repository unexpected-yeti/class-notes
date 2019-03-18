# Dependency Management

Dependency Management beschreibt die Organisation und Techniken für den Umgang mit Abhängigkeiten.
Abhängigkeiten werden in der Regel in kompilierter Form aufgelöst und auf einem zentralen Server strukturiert verwaltet. 

## Dependency Management in Java mit Maven

In Java werden Artefakte in der Regel als JARs ausgetauscht.
Ursprünglich wurden JARs direkt in Projekte kopiert (_/lib_).
Dies ist Fehleranfällig, bringt hohe Redundanz und einen grossen Platzbedarf mit sich.
Darum wird auch in Java ein Dependency Management Tool verwendet, nachfolgend ist der Fokus nur auf Maven.
Der Maven Quasi-Standard ist sehr populär - zahlreiche Dependency Managment Tools basieren auf Maven (z.B. Grape, Gradle, SBT, usw.)

### Repositories 

Bei Maven ist der zentrale Server ein Maven Repository (OSS).
Es gibt verschiedene öffentliche Repositories zum Abhängigkeiten zu beziehen ([Maven Central](http://repo.maven.apache.org/maven2/), [BinTray](https://bintray.com/bintray/jcenter).
Auf öffentliche Repositores haben nur ausgewählte Personen Schreibrechte.
Unternehmen betreiben in der Regel interne Repositores (z.B. mit [Sonatype/Nexus](https://de.sonatype.com/nexus-repository-sonatype), [JFrog/Artifactory](https://www.jfrog.com/open-source/)).
Auf dem lokalen Rechner existiert auch ein Repository (_$HOME/.m2/repository_) welches zum cachen von Artefakten verwendet wird.
Repositores werden in der Maven Konfiguration (_$HOME/.m2/settings.xml_) definiert.

### Project Object Model (POM)

Das Project Object Model (POM) definiert ein Java Projekt, siehe _pom.xml_.

Ein Projekt wird mit den _Maven Coordinates_ eindeutig identifiziert, bestehend aus:
- **groupId**: entspricht dem **übergeordneter Namespace** - meistens der _reverse domain name_ der Organisation und einem Zusatz für die genauere Identifikation (z.B. Organisationseinheit, Projektgruppe, usw.)
- **artifactId**: entspricht dem Namen des Projektes
- **version**: entspricht der aktuellen Version des Projektes (z.B. mittels [Semantic Versioning](http://semver.org))

**Beispiel**:
```xml
<groupId>ch.hslu.vsk</groupId> 
<artifactId>stringpersistor-api</artifactId> 
<version>5.0.0</version>
```

Abhängigkeiten werden im POM mit den _Maven Coordinates_ und deren Scope (Verwendungsbereich) definiert.
Mittels Scopes können z.B. Test Abhängigkeiten von Runtime Abhängigkeiten getrennt werden.
Oft verwendete Scopes sind:
- _compile_: Abhängigkeit für die Kompilation (default)
- _test_: Abhängigkeit für Tests
- _runtime_: Abhängigkeit für die Laufzeit, z.B. für dynamisch geladene Implementationen
- _provided_: Abhängigkeit welche von der Zielumgebung zur Verfügung gestellt wird 

Diese Abhängigkeiten werden beim Build vom OSS herunter geladen, und im lokalen Repository gespeichert.
Der Buildprozess referenziert die Artefakte (JARs) dort mit dem Classpath.

**Beispiel**:
```xml
<dependencies>
  <dependency>
    <groupId>ch.hslu.vsk</groupId> 
    <artifactId>stringpersistor-api</artifactId> 
    <version>5.0.0</version> 
    <scope>compile</scope>
  </dependency>
</dependencies>
```

### Versionierung mit Snapshots

In einer dnamischen Entwicklungsphase sind fixe Versionen oft hinderlich, da man oft Änderungen von Komponenten vor deren Release integrieren möchte.
Um dieses Problem zu lösen werden Versionen welche mehrmal überschrieben werden können und noch nicht stabil sind mit dem Appendix _-SNAPSHOT_ gekennzeichnet.
Snapshots werden im OSS mit einer Timestamp versehen.
Man kann den Appendix mit Timestamp verwenden um sich auf eine spezifische Version festzulegen oder den Timestamp weglassen um die neuste Snapshot Version anzuziehen.

### Managed Dependencies

In Projekten mit Submodulen sind mehrere Submodule oft von den gleichen Abhöngigkeiten abhängig.
Um Redundanz zu vermeiden und überall die selbe Version dieser Abhängigkeit zu erhalten, kann man diese Versionen im Parent POM als Baseline definieren.
In den Submodulen können diese Abhängigkeiten dann mittels _groupId_ und _artifactId_ referenziert werden (Version und Scope können weggelassen werden).

**Beispiel Parent**:
```xml
<dependencyManagement> 
  <dependencies>
    <dependency> 
      <groupId>org.apache.logging.log4j</groupId> 
      <artifactId>log4j-api</artifactId> 
      <version>2.11.1</version> 
      <scope>compile</scope>
    </dependency> 
  </dependencies> 
</dependencyManagement>
```

**Beispiel Submodule**:
```xml
<dependencies>
  <dependency>
    <groupId>org.apache.logging.log4j</groupId> 
    <artifactId>log4j-api</artifactId>
  </dependency> 
</dependencies>
```
