# Datenvisualisierung

## Referenzmodell für die Visualisierung

![image-20190919164628451](assets/image-20190919164628451.png)

## Visuelle Variablen nach Bertin

![image-20190919164657658](assets/image-20190919164657658.png)

Quelle: https://www.axismaps.com/guide/general/visual-variables/ 

## Design von visuellen Anwendungen nach Mazza

*TLDR;*:
	- Was
	- Für wen
	- Wozu
	- Wie

> The main problem in designing a visual representation lies in creating visual mapping that, on the one hand, faithfully reproduces the information codified in the data and, on the other, facilitates the user in the redetermined goal. ..., there is no way to know, given a collection of abstract data, which type of visual representation is suitable for such data. This depends on the nature of the data, the type of user it’s designed for, the type of information that has to be represented, and its use, but also on the creativity, experience, and ability of the representation’s designers. In these cases, the most precious and important information comes to us from potential users of the visual application, those who will use the system and ordain its success or failure. Believe it or not, most authors of works of visual representation of information don’t carry out preliminary research ...
(Mazza 2009, p 24)

## Prinzipien des analytischen Designs nach Tufte

Folgende Prinzipien des analytischen Designs werden von Tufte beschrieben:
  1. **Comparisons**: Show comparisons, contrasts, differences.
  2. **Causality**: Show causality, mechanisms, explanation, systematic structure.
  3. **Multivariate analysis**: Show multivariate data, that is, show more then 1 or 2 variables.
  4. **Integration of evidence**: Completely integrate words, numbers, images, diagrams.
  5. **Documentation**
  6. **Content counts most of all**: Analytical presentations ultimately stand or fall depending on the quality, relevance, and integrity of their content. 

Quelle: http://atc.berkeley.edu/201/readings/Tufte_BE_2006.pdf 

### Relation der Prinzipien mit der Karte von Minard

Folgende Relationen konnten u.a. identifiziert werden:
  1. Der Armeebestand wird verglichen, *ausgehend* und *eingehend* mit unterschiedlicher Farbe. Dabei wird der Armeebestand untereinander resp. übereinander dargestellt.
  2. Kausalität ist nur schwach dargestellt. Ein Hinweis ist die Veränderung Armeebestandes im Bezug auf die sich verändernde Temperatur (*eingehend*). Es werden jedoch weitere Informationen benötigt um Kausalität herzustellen.
  3. Es werden mehrere Dimensionen dargestellt: u.a. Temperatur, Armeebestand und Richtung der Armee.
  4. Die Karte wird mit Text, Elementen aus einer echten Karte (Flüsse), Tabellen, Beschreibungen und Überschriften annotiert, welche gewissermassen Beweise liefern.
  5. Es werden Informationen zur Kredibilität dokumentiert: Kurzbeschreibung der dargestellten Information, Author, Erstellungsort- und Datum, Quellen, Annahmen, Skalen der Messung, Veröffentlichungsdatum und Verleger.
  6. Im Fokus stehen die Verluste der Armee. Da nie Napoleon erwähnt wird, zeigt dies umso mehr.

### Identifikation der verwendeten Visualisierungsformen

Folgende Visualisierungsformen wurden u.a. verwendet:
  1. Armeebestand wird durch eine eingefärbte Fläche dargestellt. Diese verändert sich im Verlauf der Zeit, dargestellt durch den Verlauf der Strecke.
  2. Temperatauren werden mittels einer Tabelle dargestellt.
  3. Ort und Richtung der Armee wird mit der Position der eingefärbten Fläche und Ausschnitten von echten Karten (Flüsse) dargestellt.

## Die ultimativen Design Goals 
Zusammenhänge in der Datenstruktur entsprechen den visuellen Zusammenhängen der entsprechenden Symbole.

## Features, Patterns and Objects

![image-20190926150224120](assets/image-20190926150224120.png)

![image-20190926150237591](assets/image-20190926150237591.png)

### Preattentive Processing

https://infovis-wiki.net/wiki/Preattentive_processing
https://www.csc2.ncsu.edu/faculty/healey/PP/index.html

### Features: Visuelle Variablen
- Position
- Shape (Mark/Glyph)
- Size (Length, Area, Volume)
- Brightness (Luminence, Greyscale)
- Colour
- Orientation
- Texture
- Motion

> Effective design should start with a visual task analysis, determine the set of
visual queries to be supported by a design, and then use color, form, and
space to efficiently serve those queries. (Ware 2008, p 21)

https://infovis-wiki.net/wiki/Visual_Variables

#### Position

![image-20190926150458332](assets/image-20190926150458332.png)

#### Shape (Mark/Glyph)

![image-20190926150524179](assets/image-20190926150524179.png)

![image-20190926150544015](assets/image-20190926150544015.png)

#### Size (Length, Area and Volume)

![image-20190926150605128](assets/image-20190926150605128.png)

![image-20190926150635883](assets/image-20190926150635883.png)

#### Brightness (Luminence, Greyscale)

![image-20190926150656145](assets/image-20190926150656145.png)

![image-20190926150707783](assets/image-20190926150707783.png)

#### Color

![image-20190926150738265](assets/image-20190926150738265.png)

##### Common colormaps

![image-20190926150812328](assets/image-20190926150812328.png)

##### Cultural influences

http://muyueh.com/greenhoney/

#### Orientation

![image-20190926150911804](assets/image-20190926150911804.png)

![image-20190926150922021](assets/image-20190926150922021.png)

#### Texture

![image-20190926150933591](assets/image-20190926150933591.png)

![image-20190926150946764](assets/image-20190926150946764.png)

#### Motion

![image-20190926151010246](assets/image-20190926151010246.png)

### Patterns: Gestalt Principles
Perceptual laws about how we group visual objects together to form visual entities:
-  Proximity
-  Similarity
-  Closure
-  Simplicity
-  Continuity
-  Connectedness
-  Common Region

#### Proximity

![image-20190926152828344](assets/image-20190926152828344.png)

#### Similarity

![image-20190926152838086](assets/image-20190926152838086.png)

#### Closure

![image-20190926152845587](assets/image-20190926152845587.png)

#### Simplicity

?

#### Continuity

![image-20190926152918999](assets/image-20190926152918999.png)

#### Connectedness

![image-20190926152927342](assets/image-20190926152927342.png)

#### Common Region

![image-20190926152936375](assets/image-20190926152936375.png)

### Gestalt Laws
https://www.e-teaching.org/didaktik/gestaltung/visualisierung/gestaltgesetze/

### Effekte von Visuellen Variablen (Assoziativität gegeben)
#### Ordinale visuelle Variablen
-  Texture
-  Grösse
-  Brightness

#### Proportionale visuelle Variable
- Grösse
- Ausrichtung
- Brightness

#### Separierende visuelle Variablen
- Textur
- Farbe
- Ausrichtung
- Form

### Pattern reading
https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content-discovered/

### Visual Usability: Content Characteristics

![image-20190926153544162](assets/image-20190926153544162.png)

![image-20190926153552102](assets/image-20190926153552102.png)

![image-20190926153600557](assets/image-20190926153600557.png)

![image-20190926153613209](assets/image-20190926153613209.png)
