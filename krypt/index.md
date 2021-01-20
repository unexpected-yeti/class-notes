# SW 1 -2 Grundlagen

* Ich kann die Grundbegriffe der Kryptologie richtig einordnen.
* Ich kann den Nutzen von kryptographischen Massnahmen beurteilen.
* Ich kann die verschiedenen Schutzmechanismen unterscheiden.
* Ich kann die 8 typischen Angriffe, die mit Hilfe der Kryptographie verhindert werden können, aufzählen.
* Ich kann die Zuordnung, mit welchen Schutzmechanismen welche Angriffe verhindert werden können, anwenden.
* Ich kann bei einem kryptographischen System erkennen, welches der Schlüssel und welches das Verfahren (Algorithmus) ist.
* Ich kenne den Unterschied zwischen symmetrischer und asymmetrischer Kryptographie.
* Ich kenne den Unterschied zwischen Verschlüsseln und Integritätsschutz.
* Ich kenne den Unterschied zwischen einer digitalen Signatur und einem MAC. 
* Ich kann die Stärke eines Passwortes in die Länge eines kryptographischen Schlüssels umrechnen.

# SW 3 - Symmetrische Kryptographie

* Ich habe ein gutes Verständnis der Stromchiffren und Blockchiffren erlangt.
* Ich kenne die verschiedenen Modi der Blockchiffren und kann deren Stärken und Schwächen benennen.

# SW4 - Key Management für sym. Verfahren & Hashfunktionen

* Ich kann die Elemente eines symmetrischen Key Managements aufzählen.
* Ich kann ein einfaches Key Management gemäss den vorgegebenen Eigenschaften beurteilen.
* Ich kann den Unterschied zwischen einer keyedHashfunction und einer keyless-Hashfunction erklären.
* Ich kann den CBC-MAC und HMAC aufzeichnen.
* Ich kann die Einsatzgebiete von CBC-MAC und HMAC benennen.

# SW5 - Kryptoanalyse mit Schwerpunkt symmetrische Kryptographie

* Ich erhalte einen ersten Einblick in die Kryptoanalyse.
* Ich kenne die Definitionen der Attacken
* Ich kann die verschiedenen Grundtypen der Kryptoanalyse unterscheiden
* Ich kann den Nutzen einer Brute-Force Attacke abschätzen
* Ich kann das Prinzip eines Time-Memory Tradeoff Angriffs erklären
* Ich kann den 2-DES analysieren und kenne die wahre Schlüsselstärke.
* Ich kann einen Angriff auf eine Stromchiffre analysieren, resp. erklären, wieso die Stromchiffre keine Integrität gewährt

# SW6 - Mathematische Grundlagen der asymmetrischen Kryptographie»

* Ich habe die mathematischen Grundlagen (siehe auch Vorkenntnisse) repetiert und gefestigt
* Ich kenne insbesondere
  * Die Mod N Operationen wie Addition, Subtraktion, Multiplikation, Bilden des Inversen.
  * Potenzieren, Square and Multiply, usw.
* Ich kann die Anzahl Primzahlen bis zur Grösse n, resp. der Grösse n berechnen.
* Ich kenne den Unterschied zw. dem deterministischen und dem probabilistischen Ansatz zum Finden von Primzahlen.
* Ich kenne die Sätze und Berechnungen zu den Primzahlen.
* Ich kann die Sätze von Euler und Fermat einsetzen
* Ich kenne die Elemente der Gruppen- und Körpertheorie.
* Ich habe die Aufgaben im JS Skript „Aufgaben und Lösungen zum Modul KRYPT an der HSLU-I“, Kap. 2.2 durchgearbeitet.

# SW7 & 8- Public Key Kryptographie I & II

* Ich kann die mathematischen Grundlagen in der asymmetrischen Kryptographie anwenden und vertiefen.
* Ich kann die verschiedenen Schlüsseltypen der asymmetrischen Kryptographie richtig einsetzen.
* Ich kann eine RSA-Berechnung im Detail ausführen. 
* Ich kann eine "square and multiply" Berechnung durchführen und den Aufwand berechnen. 
* Ich kenne den Unterschied zwischen einem „Schoolbook“ RSA und einem „RSA in Practice“.
* Ich kenne Homorphie Eigenschaft des RSA und kann eine RSA Verschlüsselung.
* Ich kann einen DH Schlüsselaustausch im Detail ausführen
* Ich kann eine Elgamal Verschlüsselung durchführen.
* **Wichtig**: Mindestens einer der 4 folg. Algorithmen wird in der Prüfung vorkommen:
  * RSA-Berechnung
  * Homomorphe Eigenschaft des RSA
  * Diffie-Hellman Schlüsselverteilung
  * Elgamal-Verschlüsselung



# SW9 & 10 - Public Key Krypto III, ECC und Weiteres

**ECC:**

* Ich kann bei einer gegebenen Gleichung überprüfen, ob sie eine Elliptische Kurve darstellt.
* Ich kann die Nichtsingularitätsbedingung einer EC überprüfen.
* Ich kann entscheiden, ob ein gegebener Punkt auf einer gegebenen Elliptischen Kurve liegt oder nicht
* Ich kann eine Punktverdoppelung einer EC berechnen
* Ich kann eine Kurvenpunktaddition einer EC berechnen.
* Ich kann einen "double and add" Algorithmus durchführen
* Ich kann mit einer EC eine Verschlüsselung durchführen.
* Ich kann den DH- Schlüsselaustausch auf Basis von EC durchführen
* Ich kann die Anzahl der Punkte einer EC bestimmen (Theorem von Hasse).
* Ich kann die Ordnung eines Punktes einer EC bestimmen.

**RSA**:

* Ich kann eine Codebuchanalyse mit dem RSA durchführen.
* Ich kann eine RSA Verschlüsselung verfälschen.
* Ich kann das RSA Signaturverfahren erklären. 
* Ich kann eine Meldung mit RSA signieren
* Ich kann den Unterschied zwischen RSA und DSA sowie Schnorr erklären.
* Ich kann bei einer Meldung das blinde Signaturverfahren anwenden.
* Ich kann beide Typen Doppelunterschrift mit dem RSA durchführen.
* Ich kann das Protokoll einer blinden Signatur mit RSA durchführen

# SW11 - PKI

* Sie kennen die Mechanismen, die PKI-Verfahren zugrunde liegen (verschlüsseln, signieren)
* Sie wissen, wann öffentliche und wann private Schlüssel beim Einsatz von PKI-Verfahren zur Anwendung gelangen
* Sie wissen, worauf beim Beantragen von Zertifikaten zu achten ist
* Sie wissen, wie Zertifikate erzeugt werden
* Sie kennen die wichtigsten Key-Management-Aspekte beim Umgang mit öffentlichen und privaten Schlüsseln

# SW12 - Protokolle

* Ich erhalte einen Überblick über das weitläufige Thema «Kryptographische Protokolle». 
* Der Aspekt der Horizonterweiterung ist grundsätzlich wichtiger als das spezifische Vermitteln von detaillierten Algorithmen.
* Ich kann die Grundbegriffe der Protokolle aufzählen
* Ich kann wichtige Protokolle (z.B. Mutual Authentication) aufzeichnen
* Ich kann die Grundprinzipien des Key Establishment aufzählen.
* Ich habe einen Eindruck erhalten, wie man Protokolle analysiert

# SW13 - Quantenkryptographie

* Ich kann die Schlüsselbits bei einem Quantenschlüsselaustausch bestimmen.
* Ich kann berechnen, wie viele Ausgangsbit nötig sind, um n Bit Schlüssel nach dem Quantenschlüsselaustausch zu haben.
* Ich kann die Stärken und Schwächen der Quantenschlüsselverteilung aufzählen
* Ich kann die Anzahl Qbits berechnen, um einen RSA mit Modulus N zu brechen (resp. N zu faktorisieren), resp. um eine Elliptische Kurve mod p zu brechen.
* Ich kann aufgrund der Qbits die Sicherheit von RSA und EC in Bezug auf den Einsatz von Quantencomputer vergleichen.
* Ich kenne eine (weitere) Begründung, warum der AES auch mit 256 Bit Schlüssellänge standardisiert ist. 

# SW13+ - Kennzahlen, etc

* Ich kenne die aktuellen Kennzahlen der Kryptographischen Algorithmen. 
* Ich kann Irrmeinungen der Kryptologie erkennen.

