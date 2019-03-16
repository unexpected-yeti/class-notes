# Structured Query Language (SQL)

## Lernziele

### Tabellen erstellen `(create table)`

### Daten einfügen, ändern, löschen `(insert – update – delete)`

### Einfache Abfragen `(select – from – where)`

### Einfache Filterkriterien `(=, <=, <, and)`

### Abfragen über mehrere Tabellen: `Join (,)`

### Aggregationen `(count, sum, min, max, avg)`

## Kontrollfragen

### Theorie

#### Welche Benutzergruppen gibt es und wie interagieren sie mit der Datenbank?

#### Welche Benutzergruppen gibt es und wie interagieren sie mit der Datenbank?

#### Wie ist der Zusammenhang von Kreuzprodukt und Division?

#### Was ist der Zusammehang von mengenorientierten Abfragesprachen und der Relationenalgebra?

#### Wie wird die Selektion in SQL umgesetzt?

#### Wie wird die Projektion in SQL umgesetzt?

#### Wie wird der Join in SQL umgesetzt?

#### Wie zeigt sich die Eigenschaft von SQL, dass sie deskriptiv ist?

#### Wie zeigt sich die Eigenschaft von SQL, dass sie deskriptiv ist?

### SQL und Relationenalgebra

#### Selektion
Welche Professoren haben Rang _C4_?

**SQL**
```sql
SELECT * FROM professoren WHERE rang='C4';
```

**Relationenalgebra**
```math
\sigma_{rang=C4}(professoren)
```

#### Projektion
Projizieren Sie die Relation Professoren auf die Attribute Personennummer und Name. Tun Sie in einem zweiten Schritt dasselbe für die Relation Assistenten.

## Allgemein
Die Sprache SEQUEL („Structured English QUEry Language“) wurde Mitte der siebziger Jahre für «System R» geschaffen; dieses Testsystem war eines der ersten lauffähigen relationalen Datenbanksysteme.
Das Prinzip von SEQUEL war eine relational vollständige Abfragesprache, welche nicht auf mathematischen Symbolen, sondern auf englischen Wörtern wie ‚select’, ‚from’, ‚where’, ‚count’, ‚group by’ etc. basiert.
Eine Weiterentwicklung dieser Sprache ist unter dem Namen SQL (Structured Query Language) erst durch die ANSI und später durch die ISO normiert worden. 
SQL ist seit Jahren die führende Sprache für Datenbankabfragen und -interaktionen.

SQL ist gleich mächtig wie die Relationenalgebra und gilt deshalb als relational vollständige Sprache.
Die relationale Vollständigkeit einer Datenbanksprache bedeutet, dass die Operatoren der Relationenalgebra (vgl. Lektionen R1-R2) in ihr darstellbar sind:
- Selektion (Auswahl von Zeilen)
- Projektion (Auswahl von Spalten)
- Kartesisches Produkt (Menge aller möglichen Kombinationen von Zeilen zweier Tabellen)
- Plus die mengenorientierten Operationen Vereinigung
- Differenz

## Aufbau von SQL
Mit dem Projektionsoperator (`SELECT`) werden eine Liste von Merkmalen angegeben.
In der `FROM`-Klausel wird die Domäne (benötigte Tabellen) der Relation angegeben.
Selektion (`WHERE`) kann mittels Aussagen durch logische Operatoren (z.B. `AND` und `OR`) gewährleistet werden.

**Generelles Schema**:
```sql
SELECT Projection
FROM   Domain
WHERE  Selection-Predicate
```

### Beispiele

**Projektion**:
```sql
SELECT Unt, Name
FROM   MITARBEITER
```

**Kartesisches Produkt**:
```sql
SELECT M#, Name, Strasse, Ort, Unt, A#, Bezeichnung
FROM   MITARBEITER, ABTEILUNG
```

**Inner Join (Gleichheitsverbund)**:
```sql
SELECT M#, Name, Strasse, Ort, Unt, A#, Bezeichnung
FROM   MITARBEITER, ABTEILUNG
WHERE  Unt=A#
```

**Selektion**:
```sql
SELECT *
FROM   MITARBEITER
WEHERE ORT='Schrottkreuz' AND Unt='A666'
```

**Aggregation** kann mittel folgender Funktionen geschehen:
- COUNT: Zählung
- SUM: Summenbildung
- AVG: Mittelwert
- MAX: Maximalwert
- MIN: Minimalwert

```sql
SELECT COUNT (M#)
FROM   MITARBEITER
WHERE  Unt='A666'
```

### Tabellen definieren und löschen
Tabellen lassen sich mit dem `CREATE TABLE`-Befehl definieren und mit dem `DROP TABLE`-Befehl löschen.

```sql
CREATE TABLE MITARBEITER
  ( M#   CHAR(6) NOT NULL, 
    NAME VARCHAR(20),
    ...
  )
```

### Daten einfügen
Daten lassen sich mit dem `INSERT`-Befehl einfügen.

```sql
INSERT INTO MITARBEITER
VALUES ('M20', 'Peter', 'Hässig', 'Schrottkreuz', 'A666')
```

### Daten verändern
Eine Datenmanipulation lässt sich mit dem `UPDATE`-Befehl vornehmen.

```sql
UPDATE MITARBEITER
SET    Ort = 'Schrottkreuz'
WHERE  Ort = 'Rotkreuz'
```

### Daten löschen
Ganze Tabellen oder Teile davon durch den `DELETE`-Befehl löschen.

```sql
DELETE FROM MITARBEITER
WHERE Ort = 'Schrottkreuz'
```
