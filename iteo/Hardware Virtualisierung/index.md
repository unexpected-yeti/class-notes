# Hardware Virtualisierung

Privilegierte Instruktionen lösen einen Trap, in den Kernel (Supervisor Modus), im User Modus aus. Privilegiert sind alle Instruktionen, welche versuchen die Konfigurationen von Systemressourcen zu verändern oder abhängig von der Konfiguration der Ressourcen sind (z.B. Inhalt der Relocation Register oder Prozessor Modus).

[https://en.wikipedia.org/wiki/Protection\_ring](https://en.wikipedia.org/wiki/Protection_ring)
CPL (current privilege level) -\> 2bit = 4 Privilegien = 4 Sicherheitsringe

![](DraggedImage.png)![](DraggedImage-1.png)![](DraggedImage-2.png)

Warum Memory Rückgewinnung:
- Viel redundantes z.B. Kernel, Systemdateien, usw.

## Kontrollfragen

### Wann ist eine CPU nach Popper & Goldberg virtualisierbar?
Eine CPU (ISA) ist virtualisierbar, wenn alle privilegierten Instruktionen eine Exception erzeugen (somit [ge]trapped werden), wenn sie in einem umprivilegierten Prozessormodus ausgeführt werden.

###  Was versteht man unter Emulation?
Unter Emulation versteht man eine Nachbildung eines Systems, welches im Vergleich zum nachgebildeten System, möglichst gleiche Ergebnisse mit gleichen Daten und vergleichbaren Programmen erzielt.

### Welches sind einige wichtige Virtualisierungen, die im Datacenter eine Rolle spielen?
1. Hardware Partitionierung (auf High End Computer, wie z.B. Sparc, kann das höchste Sicherheitszertifikat mit sich bringen)
2. Hardware Virtualisierung (mittels Hypervisor)
3. Operating System Virtualisierung (z.B. mittels Docker)

### Wie geht Intel das Problem an damit die direct execution realisiert werden kann?
Das Problem wird mit Hilfe einer Kombination aus *direct execution* und *binary translation* realisiert. Alle privilegierten Instruktionen welche nicht Trap geschützt sind werden im Kernel übersetzt und gechached. Der übersetzte Kernel Code ersetzt nun die nicht virtualisierbaren Instruktionen. Alle anderen Instruktionen (*user level*) werden direkt ausgeführt. Somit ist keine Hardware Unterstützung notwendig. Gast OS ist abstrahiert, hat keine Ahnung dass es in einer VM läuft.

Ein Binary Translated System Call eines 32 bit Gast OS im Ring 1 braucht ~10x mal mehr Prozessor Zyklen.

### Was ist eine Virtualisation?
Virtualisation bezieht sich auf den Vorgang der Erstellung einer virtuellen (und nicht tatsächlichen) Version von etwas, was in seinem Wesen oder seiner Wirkung in dieser Form gleicht, wie zB. virtuelle Computer-Hardware-Plattform, Betriebssystem (OS), Speichergerät oder Computer-Netzwerk-Ressourcen.

###  Welche Herausforderungen muss ein VMM lösen können?
Probleme die es zu lösen gibt:
* Mehrere Betriebssysteme gleichzeitig auf einem physikalischen Server. 
* Betriebssysteme sind konstruiert dass sie die Zugriffe auf die
Betriebsmittel regeln.
* Betriebssystem kann nicht abgeändert werden (Microsoft)

Ein (Virtual Machine Monitor) muss folgendes gewährleisten:
* Gleichheit (Programm in VM verhält sich genau so wie in der originalen Maschine)
* Effektivität (Wann immer möglich *direct execution*, möglichst wenig im *VMM*)
* Ressourcenkontrolle (komplette Kontrolle über Ressourcen [z.B. Memory, I/O, Devices], jedoch nicht umbedingt über Prozessoraktivität)

Es muss für jedes Programm unmöglich sein System Ressourcen zu beeinflussen. Der **Allocator** (entscheidet wer welche Systemressourcen bekommt) der VMM muss bei jedem dieser Versuche aufgerufen werden. Für jede privilegierte Instruktion muss der **Interpreter** des VMM eine Methode zur Verfügung stellen.

Dispatcher dessen Initial Instruction am Speicherplatz liegt wohin die HW trapped.?KONTEXT

Dabei kann ein VMM vom OS unterstützt werden (Para Virtualisierung [neben]).

**OS Unterstützt**

Kernel vom OS muss modifiziert werden um nicht virtualisierbare Instruktionen mit Hypercalls zu ersetzen die direkt mit dem Virtualization Layer Hypervisor kommunizieren. Der Hypervisor stellt Hypercall Interfaces zur Verfügung. Keine unmodifizierte Gast OS!.?KONTEXT

Paravirtualisierung ist nicht so verschieden von Binary Translation. BT übersetzt „kritischen“ in „harmlosen“ Code. Paravirtualisierung macht dasselbe aber im Source Code. Änderungen im Source Code erlaubt grössere Flexibilität. Para Virtualisierung braucht keine „Laufzeit-Übersetzung“ und wird daher schneller ausgeführt. Unveränderte Betriebssysteme können nicht ausgeführt werden.

**HW Unterstützt**

Neuer CPU Modus eingeführt. Erlaubt Ausführung unterhalb Ring 0. Privilegierte und sensitive Calls trapen automatisch zum Hypervisor ohne binary translation. Der Gast Status wird in virtual machine control structures abgespeichert. CPUs seit 2006 erhältlich.

### Wo werden im HW unterstützten x86 Sicherheitsmodell der Kern, Hypervisor und die Applikationen ausgeführt?

VMM und VM haben getrennte Adressbereiche. VMCS (Virtual Memory Control Structure) sind zusätzliche Kontroll Strukturen im Memory. VMCS verfolgt die Kontextwechsel Prozessorinformationen für VMs. Neue Intel IA32 Instruktionen:
 2 neue Operationsmodi (die in Ring 0-3 vorhanden sind): - VMX root Operation:
- Voll Privilegiert für den VM Monitor - VMX non-root Operation:
- Nicht voll privilegiert für die Gast Betriebssysteme
- Reduziert Gast SW Privilegien ohne auf die Ringe zurückgreifen zu
müssen.

### Was sind Gründe für eine Hardware Virtualisierung
- Performanz
- OS muss nicht angepasst werden
- 

