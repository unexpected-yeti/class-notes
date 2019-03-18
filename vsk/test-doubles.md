# Test Doubles (Mocking)

Ein _Double_ ist ein Platzhalter für die echte, produktive Implementation während Tests.

Hauptsächlich dienen Test Doubles dazu den Aufwand für Integrations-Tests zu reduzieren.
Somit können _fast integrative_ Tests schnell, häufig, überall lauffähig, und vollständig automatisiert ausgeführt werden.

Häufig spricht man unpräzis nur von Mocks und Mocking.
Es gibt **Dummies, Stubs, Spies, Mocks und Fakes**:

![Test Double Klassenhierarchie](./assets/test-doubles.png)

Mit Dummies und Stubs erreicht man eine bessere Testisolation durch einfache Ersatzimplementationen.
Mit Spies und Mocks kann das Verhalten einfacher testen.
Mit einem Fake erreicht man die vollständige Entkopplung zu einer Abhängigkeit.

## Dummy

Ein Dummy ist eine sehr primitive und oft **leere** Ersatz-Implementation.
Er dient zur **funktionslosen** Entkopplung von unerwünschten Abhängigkeiten.

**Beispiel**:
Einem Objekt muss ein Logger übergeben werden. 
Weil das Loggen ist nicht das eigentliche Testziel, kann man mit einem Dummy einen Logger übergeben der nichts macht.

## Stub

Ein Stub ist eine einfache Implementation, welche sinnvolle, vordefinierte Werte zurückliefert.
Erleichtert es Tests mit verschiedenen Zuständen (States) zu testen.
Ein Zustand (State) ist bei Stubs in der Regel konstant.
Daher werden für die unterschiedlichen Testziele auch oft mehrere unterschiedliche Stubs erstellt.

## Spy

Ein Spy ist eine alternative Implementation, welche dynamische Werte zurückliefert.
Unteranderem misst ein Spy folgende Metriken von Methoden:
- Anzahl/Häufigkeit
- Parameter
- Zeitpunkt
- Exceptions

Erleichtert es das Verhalten (Behavior) von Klassen zu testen.

## Mock

Ein Mock ist eine Spezialisierung eines Spy.
Im Unterschied zu einem Spy kann ein Mock eine korrekte Interaktion selbst verifizieren.
Einziger Unterschied ist der Ort der Verifikation, Mocks sind dadurch spezifischer.

## Fake

Ein Fake ist eine alternative Implementation einer Komponente.
Erleichtert es die vollständige Entkopplung einer Abhängigkeit innerhalb von Tests.

