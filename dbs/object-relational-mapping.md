# Objekt-relationales Mapping

[TOC]

## Lernziele

* Die Vorteile von objekt-orientierten Datenbanken (OO-DB) erklären: OIDs, aggregierte Speicherung Methoden, Referenzierung mit Pointer, many-to-many-Relationships, Vererbung
* Objekt-relationale Datenbank definieren
* Objekt-relationales Mapping definieren
* Vorteile von objektrelationalen Mappern (ORM) erklärer
  * Basis RDBMS
  * Verwendung in OOP
* Daten mit ORM (JPA) anfragen (JPQL) und in Java anwenden
* Daten in Java erstellen und in die Datenbank schreiben (persist, merge)

## OOP und Relationale Datenbanken

Bei der Entwicklung von objektorientierten Sprachen und relationalen Datenbank gibt es einen Mismatch: beide Konzepte widersprechen sich in wichtigen Punkten. Dieses Problem wird als **object-relational impedance mismatch** beschrieben. Es tritt auf wenn Objekte aus einer OOP-Sprache in einer relationalen Datenbank gespeichert werden soll.

## Objektdatenbank

### OID (Objekt-Identität)

* Wesentliche Charakteristikum objekt-orientierter Datenmodellierung
* Verweise werden über die OID realisiert
* Zwei Realisierungsformen:
  * Physische OIDs: Enthalten Speicherort des Objekts, im Wesentlichen entsprechen diese den Tupel Identifikatoren (TID)
  * Logische OIDs: Unabhängig vom Speicherort der Objekte (dH Objekte können verschoben werden). Indirektion über eine Mapping-Struktur (B-Baum, Hash-Tabelle, Direct Mapping)

### Aggregierte Speicherung

### Referenzierung mit Pointer

### many-to-many Relationships

### Vererbung



## Objektdatenbank

> Eine **Objektdatenbank** oder **objektorientierte Datenbank** ist eine [Datenbank](https://de.wikipedia.org/wiki/Datenbank), die auf dem **Objektdatenbankmodell**basiert. Im Unterschied zur [relationalen Datenbank](https://de.wikipedia.org/wiki/Relationale_Datenbank) werden Daten hier als [Objekte](https://de.wikipedia.org/wiki/Objekt_(Programmierung)) im Sinne der [Objektorientierung](https://de.wikipedia.org/wiki/Objektorientierung)verwaltet. Das zugehörige Datenbankmanagementsystem wird als das **objektorientierte Datenbankmanagementsystem** bezeichnet. Objektdatenbank und Objektdatenbankmanagementsystem bilden gemeinsam das **Objektdatenbanksystem**.



### Vorteile

TODO

## Objektrelationales Datenbanksystem

Ein objektrelationales Datenbankmanagementsystem (ORDBMS) lässt sich wie folgt umschreiben

* Es erlaubt die Definition von Objekttypen (in Anlehnung an die objektorientierte Programmierung oft Klassen genannt), die ihrerseits aus weiteren Objekttypen zusammengesetzt sein können.
* Jedes Datenbankobjekt kann aufgrund von Surrogaten (OID) strukturiert und identifiziert werden.
* Es unterstützt generische Operatoren (Methoden), die auf Objekte oder Teilobjekte wirken. Dabei bleibt die interne Darstellung der Objekte nach Außen unsichtbar (Datenkapselung).
* Eigenschaften von Objekten lassen sich vererben. Diese Vererbungseigenschaft bezieht sich sowohl auf die Struktur als auch auf die zugehörigen Operatoren.

## Objekt-Relationales Mapping (ORM)

Verknüpfung von objektorientierter Programmierung mit relationalen Datenbank-Management-Systemen.

Dabei gibt es zwei Ansätze:

* Top-Down: Man definiert zuerst Klassen und generiert daraus automatisch Tabellen (z.B. JPA tools, Eclipse)
* Bottom-Up: Man definiert zuerst Tabellen und generiert daraus automatisch Klassen (z.B. Netbeans)



Der Unterschied zwischen ORM und OODB ist, dass bei ORM für die Verwendung mit herkömmlicher Technologie (RDBMS) erschaffen wurden. OODBs hingegen benötigen keinen Mapper.



## Java Persistence API (JPA)

### EntityManager

* Erlaubt Zugriff auf JPA-Funktionalität
* `Persist` und `merge` werden immer in einer Transaktion ausgeführt

```java
EntityManagerFactory emf = Persistence.createEntityManagerFactory(„myPU");
EntityManager em = emf.createEntityManager();
// Neues Objekt und referenzierte Objekte speichern
em.persist(entityObject);
// Aktualisiert ein Objekt in der DB
em.merge();
                                                                  
// Aktualisiert Laufzeitobjekt
em.refresh(object);

EntityTransaction ta = em.getTransaction();
// ta.begin(); ta.commit(); ta.rollback()

```
### Entity & Annotations
Eine JPA-Entity ist eine Java-Klasse, welche auf eine Entitäts-Tabelle gemappt wird. Die Definition erfolg im Java-Code mit so genannten Annotations. Beispiel:
```java
@Entity
@Table(name = "Professoren")
public class Professoren implements Serializable {
	private static final long serialVersionUID = 1L;
	@Id
	@Column(name = "PersNr")
	private Integer persNr;
	@Column(name = "Name")
	private String name; ...
```

#### Annotations (Basic)

| Annotation                   | Beschreibung                                         |
| ---------------------------- | ---------------------------------------------------- |
| @Entity                      | Klasse ist persistent                                |
| @Table(name=...)             | Klasse wird auf Tabelle abgebildet                   |
| @Column(name=...)            | Klassen- zu Tabellenattribut (siehe obiges Beispiel) |
| @Id                          | Primärschlüsselattribut                              |
| @GeneratedValue(strategy=..) | Automatische Generierung eines Attributwertes (Id)   |

Beispiel:

```java
import javax.persistence.*;
@Entity
@Table(name = "vorlesungen")
public class JVorlesungen implements Serializable {
	@Id
	@GeneratedValue(strategy =GenerationType.IDENTITY)
	@Basic(optional = false) // null not allowed
	@Column(name = "vorlnr")
	private Integer jVorlnr;
	// Db-Feld vorlnr wird zu java-Feld jVorlnr
….}
```



#### Annotations (M-zu-1 Beziehungen)

M-zu-1 Beziehung zwischen JVorlesungen und JProfessoren. JVorlesungen benötigt somit eine Referenz auf JProfessoren:

```java
@JoinColumn(name="gelesenVon", referencedColumnName="PersNr)
@ManyToOne
private JProfessoren jGelesenVon
```

Umgekehrt in der Klasse JProfessoren:

```java
@OneToMany(mappyedBy="jGelesenVon")
private Collection<JVorlesungen> jVorlesungen;
```

#### Annotations (mc-zu-mc)

mc-zu-mc Beziehung zwischen JStudenten und JVorlesungen. In JStudenten:

```java
@JoinTable(name = "hoeren", 
	joinColumns = {@JoinColumn(name = "matrnr", referencedColumnName = "persnr")},
	inverseJoinColumns = {@JoinColumn(name = "vorlnr", referencedColumnName = "vorlnr")})
	@ManyToMany
	private Collection<JVorlesungen> jVorlesungen;
```

In JVorlesungen:

```java
@ManyToMany(mappedBy = "jVorlesungen")
private Collection<JStudenten> jHoerer;
```

 #### Annotations (Vererbungshierarchien)

Vererbungshierarchien in einer Tabelle (single table, joined tables als Alternative). Ein Eintrag in der Personen-Tabelle mit„ assi" in dtype ist ein Objekt der Klasse JAssistenten

```java
// In JPersonen
@Entity
@Table(name = "Personen")
@Inheritance( strategy = InheritanceType.SINGLE_TABLE)
@DiscriminatorColumn( name = "DTYPE", discriminatorType = DiscriminatorType.STRING)
```
```java
// In JAssistenten extends JPersonen
@Entity
@DiscriminatorValue("assi")
```

#### Annotations (zusätzliche Argumente für Beziehungen)
*  in @One.. ,@Many..:
  * CascadeType: Änderungen am referenzierten Objekt werden implizit gespeichert. 
  * FetchType: Laden des referenzierten Objekte
* Als Beispiel in der Klasse JProfessoren für die Collection jVorlesungen:
  `@OneToMany(mappedBy = „jGelesenVon", cascade=CascadeType.PERSIST, fetch=FetchType.EAGER)`
* liest der neue Prof p eine neue Vorlesung v (mit new erzeugt und zu jVorlesungen hinzugefügt ), wird sie automatisch gespeichert, wenn p persistiert wird. Aber `v.jGelesenVon` wird nicht automatisch gesetzt!!
* ein Prof-Objekt wird immer zusammen mit „seinen“ Vorlesungen geladen.

### Java Persistence Query Language (JPQL)

* http://docs.oracle.com/javaee/6/tutorial/doc/bnbtl.html
* Objekt-Anfragesprache, von OQL abgeleitet
* Ähnlich zu SQL, aber auf Java-Objekte bezogen

In SQL:
```sql
SELECT d
FROM Dozenten d JOIN d.module m
WHERE m.getName() = 'DMG'
```

In JPQL (Ausführung via Entity Manager):
```java
Query query = em.createQuery("select d from Dozenten d");
List list = query.getResultList();
```

Weiteres / Varia zu JPQL
*JPQL supports named parameters, which begin with the colon (:). We could write a function returning a list of authors with the given last name as follows:*

```java
import javax.persistence.EntityManager;
import javax.persistence.TypedQuery;
...
public List<Author> getAuthorsByLastName(String lastName) {
    String queryString = "SELECT a FROM Author a " +
                         "WHERE a.lastName IS NULL OR LOWER(a.lastName) = LOWER(:lastName)";

    TypedQuery<Author> query = getEntityManager().createQuery(queryString, Author.class);
    query.setParameter("lastName", lastName);
    return query.getResultList();
}
```

### persistence.xml

Diese Datei konfiguriert JPA. Sie kann automatisch generiert werden.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<persistence version="2.1" xmlns=...>
<persistence-unit name="HelloJpaPU" transaction-type="RESOURCE_LOCAL">
<provider>org.eclipse.persistence.jpa.PersistenceProvider</provider>
<class>HelloJpa.Professoren</class>
<class>HelloJpa.Studenten</class>
...
<properties>
<property name="javax.persistence.jdbc.url"
value="jdbc:mysql://localhost:3306/uni2?zeroDateTimeBehavior=convertToNull"/>
<property name="javax.persistence.jdbc.user" value="root"/>
<property name="javax.persistence.jdbc.driver" value="com.mysql.jdbc.Driver"/>
<property name="javax.persistence.jdbc.password" value=""/>
</properties> </persistence-unit> </persistence>
```



## Empfehlungen & Zu Beachten

* Veränderungen nur innerhalb von Transaktionen 
* Veränderungen werden (meist) erst mit dem Ende der Transaktion in die DB geschrieben – erst dann ist eine IDENTITY-ID (auto_increment) verfügbar!!
* Referenzen für die DB sollen bei dem Objekt mit @JoinColumn- bzw. @JoinTable-Angabe gesetzt werden
  (eingeschränkte Bidirektionalität).
* CascadeType.PERSIST speichert ein neues Objekt, aber setzt nicht automatisch die Beziehung dazu (siehe
  vorgehend)
* Laufzeitobjekte werden nicht automatisch aktualisiert, use em.refresh(object)
* Nur relevante Objekte, wenn möglich in **einer Anfrage** holen (und nicht mit vielen get-Aufraufen) - ist schneller und eleganter
* Einer Beziehungstabelle mit genau zwei Fremdschlüssel nie einen weiteren Primärschlüssel angeben (so benötigt es keine Beziehungsklasse)
  * Ansonsten: vergeben Sie auch für Beziehungstabellen mit Beziehungsatributen einen technischen Primärschlüssel, sonst werden für die Beziehungen keine oo-gerechten Felder generiert (im Projekt: Stückliste oder bestehtAus oder ..)