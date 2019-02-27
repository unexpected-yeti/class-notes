# Entity-Relationship Models

## Lernziele

### Aufgrund einer Ausgangslage Entitätsmengen, Beziehungsmengen (inkl. Assoziationen, deren Typ und Grad) und Merkmale (inkl. Identifikationsschlüssel erkennen und diese im ER-Modell darstellen.

### Fortgeschrittene Beziehungsarten in der Modellierung anwenden (Generalisierung, Disjunkte Spezialisierung, Vollständige Spezialisierung, Aggregation).

## Kontrollfragen

### Was ist ein Modell?

### Wozu brauchen wir Modelle?

### Was sind Entitäten? 

### Was sind Beziehungen?

### Was sind Assoziationen?

### Was sind Generalisation & Aggregation?

## Aufgaben

### Aufgabe 1

- Welche Assottiationstypen gibt es?
  - Einfache Assoziation (1)
  - Konditionelle Assoziation (c)
  - Mehrfache Assoziation (m)
  - Mehrfach konditionelle Assoziation (mc)
- Was ist der Unterschied zwischen Generalisierung un Aggregation?
  - Generalisation = Verallgemeinern von Entitäten.
  - Aggregation = Zusammenfügen von Entitäten zu einem übergeordneten Ganzen.
- Was ist der Unterschied zwischen Generalisierung und Spezialisierung?
  - Spezialisierung = spezialisierung von Entitätsmengen.
- Wann ist eine Spezialisierung vollständig?
  - Wenn die Entitätsmenge die Subentitätsmengen vollständig umfasst.
  - "Kein Mitarbeiter ist *Abteilungslos*"
- Wann ist sie disjunkt?
  - Die Subentitätsmengen schliessen sich gegenseitig aus und haben keine Schnittmenge.

### Aufgabe 2 (Bonus)

- Wie definiert Chen den Begriff „Entity“?
- Was ist der Unterschied zu einem Entity Set?
- Wie definiert Chen den Begriff „Relationship“?
- Was ist der Unterschied zum Relationship Set?
- Schauen Sie sich die Abbildung 11 an. Wie unterscheidet sich die Notation von der Variante, wie sie	im Buch von Meier dargestellt wird?
- Worin unterscheiden sich die Notationen von Meier & Kaufmannl (2016) und Chen (1976)? Vergleichen Sie.

### Aufgabe 3

> Aufgabenbeschreibung
> TODO

### Aufgabe 4

> TODO

## Entitäten und Entitätsmengen
Unter Entität (engl. entity) versteht man einen bestimmten, von anderen unterscheidbaren, d.h. erkennbaren Gegenstand der realen Welt oder unserer Vorstellung.
Entitäten des gleichen Typs werden zu Entitätsmengen zusammengefasst und durch Merkmale weiter charakterisiert.
Für jede Entitätsmenge ist ein Identifikationsschlüssel, der die Entitäten innerhalb der Entitätsmenge eindeutig bestimmt.
￼
![Example](./assets/entities_entity-sets_example.png)

## Beziehungen und Beziehungsmengen
Die Beziehungen (engl. relationships) zwischen Entitäten geben diesen Bedeutung und Kontext.
Beziehungen könne wiederum Mengen bilden.
Beziehungsmengen können, ebenso wie Entitätsmengen, durch eigene Merkmale näher charakterisiert werden.

![Example](./assets/relationship_relationship-sets_example.png)

## Assoziationstypen
Unter Assoziation (engl. association) versteht man die Bezeichnung der Bedeutung einer Beziehung in dessen Richtung.
Assoziationstypen, auch genannt Kardinalitäten, sagen, wie oft ein Element der jeweiligen Entitätsmenge in der Beziehung vorkommen kann.

![Assoziationstypen](./assets/assoziationstypen.png)

![Example](./assets/assoziationstypen_example.png)

### Grade von Beziehungen
![Grade von Beziehungen](./assets/relationship_degrees.png)

## Generalisation

