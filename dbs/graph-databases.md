# Graph Databases

## Property Graph
Ein Eigenschaftsgraph (engl. _property graph_) besteht aus Knoten (Objekten) und _gerichteten Kanten_ (Beziehungen).
Sowohl die Knoten als auch die Kanten tragen Namen (engl. _labels_) und können Eigenschaften (engl. _properties_) aufweisen.

Je nach Reifegradd enthalten die Datenbanken Algorithmen zur Berechnung unter anderem folgender bedeutender Eigenschaften:
- *Zusammenhang:* Jeder Knoten hat einen Pfad zu jedem aanderen Knoten des Graphen.
- *Kürzester Pfad*
- *Nächster Nachbar*
- *Matching:* Berechnung einer Menge von Kanten, die keine gemeinsamen Knoten enthalten.

## Cypher
Cypher ist eine deklarative Abfragesprache, um Muster in Graphdatenbanken extrahieren zu können.
Die Anwendenden spezifizieren ihre Suchfrage durch die Angabe von Knoten und Kanten. 
Daraufhin berechnet das Datenbanksystem alle gewünschten Muster, indem es die möglichen Pfade (Verbindungen zwischen Knoten via Kanten) auswertet. 
Mit anderen Worten deklarieren die Anwendenden die Eigenschaften des gesuchten Musters, und die Algorithmen des Datenbanksystems traversieren alle notwendigen Verbindungen (Pfade) und stellen das Resultat zusammen.

Untenstehend ein Beispiel zum Abfragen von Filmtitel, Rollen und Schauspieler für einen Schauspieler mit dem Namen _Keanu Reeves_, welcher in einem Film gespielt hat:
```cypher
match (a : Actor) -- [r : Acted_In] --> (m : Movie)
where (a.name = "Keanu Reeves")
return m.Titel, a.Name, r.Rolle
```

Cypher ist ähnlich wie SQL deklarativ aufgebaut. 
Allerdings ist das Auswerten von Beziehungsgeflechten, das Verwenden re- kursiver Suchstrategien oder die Analyse von Eigenschaften von Graphen mit SQL kaum zu bewa ̈ltigen.

