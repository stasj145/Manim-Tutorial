# 5. 3Blue1Brown - Künstliches Neuronales Netz (KNN)
Nachdem in den vorherigen Kapiteln verschiedene Grundlagen dargestellt wurden, sollen diese nun verbunden werden, um komplexere Szenen zu erstellen. Als vorlage dient dafür eine Grafik aus den Videos von 3Blue1Brow auf YouTube.
In diesem Kapitel soll eine Visualisierung eines einfachen künstlichen neuronalen Netzes erzeugt werden.

Vorlage: 3Blue1Brown - [But what is a neural network? | Chapter 1, Deep learning](https://www.youtube.com/watch?v=aircAruvnKk&t=103s) [Zeit: 1:43-2:05]

Ziel dieses Kapitels ist das Erstellen des folgenden Videos:

https://user-images.githubusercontent.com/50620058/152992613-4eec1536-6a23-4994-9444-9d7e46e7034d.mp4

Das erstellen dieser Szene kann grob in 4 Abschnitte unterteilt werden:
1. Erstellen der Knotenpunkte (Kreise)
2. Erstellen der Kanten (Linien zwischen Knotenpunkten)
3. Animieren der Knoten und Kanten
4. Einfügen von Details (Klammer, Beschriftung, Hervorhebung)

Dabei wird neben den bereits bekannten Konzepten auch die neue Funktionalität der ```VGroup``` eingeführt. Eine ```VGroup``` ermöglicht es mehrere Objekte zu verbinden und gemeinsam zu bearbeiten.

## 1. Erstellen der Knotenpunkte
Zuerst sollen die Knotenpunkte erstellt werden, welche die künstlichen Neuronen des Netzes darstellen. Dabei soll es vier Schichten geben: eine Input-Schicht mit 784 Knoten, zwei versteckte-Schichten mit je 16 Knoten und eine output-Schicht mit 10 Knoten.

Die einzelnen Knoten werden mithilfe der ```Circle()``` Funktion erzeugt. Dabei müssen die folgenden drei Eigenschaften angepasst werden: ```stroke_color```, ```stroke_width``` und ```radius```. In diesem Fall habe ich mich für einen Radius von 0,1 und eine ```stroke_width``` von 2 enschieden, außerdem werden die Kreise in blau dargestellt.

```python
circleRadius = 0.1
circleStrokeWidth = 2
circleCollor = BLUE

newCircle = Circle(stroke_color=circleCollor, stroke_width=circleStrokeWidth, radius=circleRadius)
```
Daraus ergibt sich der folgende Kreis:

![basicNode](./mediaFiles/basicNode.png)

Für die Grafik werden natürlich deutlich mehr Kreise benötigt. Beginnen wir damit eine einzelne Schicht des KNN zu erstellen. Dazu wird eine einfach for-Schleife verwendet und die neuen Kreise mit jeder Iteration weiter nach unter verschoben. Dazu kann die ```shift```  Methode verwendet werden. Das sieht dann etwa so aus:
```python
circleRadius = 0.1
circleStrokeWidth = 2
circleCollor = BLUE

spacingMultiplier = 0.3

for i in range(16):
    newCircle = Circle(stroke_color=circleCollor, stroke_width=circleStrokeWidth, radius=circleRadius)
    #arrange node
    newCircle.shift(DOWN*i*spacingMultiplier)
    #draw node
    self.add(newCircle)

```
Wie zu sehen ist, wurde hier zusätzlich noch die Variable "spacingMultiplier" eingeführt, mit dieser kann der Abstand zwischen den Kreisen verändert werden. Da dieser standarmäßig recht groß ist, wird hier ein Multiplikator von 0,3 eingesetzt. Außerdem werden die Kreise mit ```self.add(newCircle)``` jeweils zur Grafik hinzugefügt.

Damit ergibt sich dieses Bild:

![basicLayerBroken](./mediaFiles/basicLayerBroken.png)

Wie zu sehen ist, wurde eine Reihe von Kreisen erzeugt. Diese ist allerdings nicht gut im Bild positioniert. Um die Position der Kreise zu ändern, werden diese zu einer ```VGroup``` hinzugefügt. Das ermöglicht es, die gesamte Schicht auf einmal zu bewegen, anstatt alle einzeln zu positionieren. Außerdem werden die Kreise nun zu einem Array hinzugefügt, dies ermöglicht es später noch auf jeden einzelnen Kreis zuzugreifen.
Der veränderte Code sieht wie folgt aus:

```python
circleArray = []
group = VGroup()

for i in range(16):
    newCircle = Circle(stroke_color=circleCollor, stroke_width=circleStrokeWidth, radius=circleRadius)
    #arrange node
    newCircle.shift(DOWN*i*spacingMultiplier)
    #draw node
    self.add(newCircle)

    #add node to array
    circleArray.append(newCircle)
    #add node to group
    group.add(newCircle)

#move group to center
group.move_to(ORIGIN)
```

So ergibt sich nun diese Grafik:

![basicLayerFixed](./mediaFiles/basicLayerFixed.png)

Damit wurde nun erfolgreich eine erste Schicht des KNN erzeugt. Es werden allerding vier Schichten benötigt. Dazu wird eine weitere for-Schleife verwendet. Um auch später noch Zugriff auf die einzelnen Kreise sowie die VGroups zu haben, werden diese jeweils wieder einem Array hinzugefügt. Dadurch ergibt sich schließlich ein Array mit allen VGroups, sowie ein 2-Dimensionales Array mit allen Kreisen.

```python
nOfRows = 4
rowArray = []
rowGroups = []

for row in range(nOfRows):
    group = VGroup()
    circleArray = []

    for i in range(16):
        newCircle = Circle(stroke_color=circleCollor, stroke_width=circleStrokeWidth, radius=circleRadius)
        #arrange node
        newCircle.shift(DOWN*i*spacingMultiplier)
        #draw node
        self.add(newCircle)
        #add node to array
        circleArray.append(newCircle)
        #add node to group
        group.add(newCircle)
    
    rowArray.append(circleArray)
    rowGroups.append(group)
```

Wie schon zuvor müssen die erzeugten Schichten nun noch positioniert werden. Dazu werden wieder die VGroups verwendet auf die über ```rowGroups``` zugegriffen werden kann:

```python
rowGroups[0].move_to(LEFT*5)
rowGroups[1].move_to(LEFT*2)
rowGroups[2].move_to(RIGHT)
rowGroups[3].move_to(RIGHT*4)
```

Nun sieht die Grafk so aus:

![allLayersSameSize](./mediaFiles/allLayersSameSize.png)

Momentan haben noch alle Schichten die gleiche Größe von 16 Knotenpunkten. Eigentlich sollen die Schichten aber 784 - 16 - 16 - 10 groß sein. Da es nicht genug Platz gibt um in der ersten Schicht 784 Knoten anzuzeigen, werden hier einfach 16 Knoten dargestellt und in der Mitte drei Punkte angezeigt, welche zeigen, dass es dort eigentlich noch mehr Knoten gibt.

Zu diesem Zweck wird einfach die untere Hälfte der Kreise der ersten Schicht nach unter bewegt. Dabei ist es wichtig, das dies geschieht bevor die Schichten über die VGroups angeordnet werden. Auf die einzelnen Kreise kann über ```rowArray``` zugegriffen werden:

```python
#Create space in first row
for i in range(int(len(rowArray[0])/2), len(rowArray[0])):
    circle = rowArray[0][i]
    circle.shift(DOWN)

rowGroups[0].move_to(LEFT*5)
rowGroups[1].move_to(LEFT*2)
rowGroups[2].move_to(RIGHT)
rowGroups[3].move_to(RIGHT*4)
```

Nun gibt es Platz in der Mitte der ersten Schicht, in dem die Punkte eingefügt werden können. Dazu werden drei kleine Punkte erzeugt und untereinander angeordnet. Diese Punkte werden dann wieder einer VGroup hinzugefügt und die Gruppe dann nach Links verschoben:

```python
#add points in first row
rad=0.02
buff=0.2
p1, p2, p3= Dot(radius = rad), Dot(radius = rad), Dot(radius = rad)

p1.next_to(p2, UP, buff=buff)
p3.next_to(p2, DOWN, buff=buff)

dotGroup = VGroup(p1, p2, p3)
dotGroup.move_to(LEFT*5)

self.add(p1, p2, p3)
```

Daraus ergibt sich nun folgendes Bild:

![allLayersFirstRowFixed](./mediaFiles/allLayersFirstRowFixed.png)

Nachdem jetzt die erste Schicht angepasst wurde, muss nun noch die letzte Schicht verändert werden, diese sollte eigentlich nur 10 Knoten enthalten, besteht aber akktuell noch aus 16. Ein einfacher Weg dies zu lösen und den Code dabei auch noch modularer zu machen, ist das ändern der for-Schleife, die die Schichten erzeugt. Statt immer fest 16 Knoten zu erzeugen, wird nun stattdessen ein Array verwendet, in dem die Größe jeder einzelnen Schicht festgelegt ist. Dazu wird zuerst das Array angelegt ```nodesInRows = [16, 16, 16, 10]``` und schließlich die for-Schleife verändert.

```python
for i in range(16):
```

wird zu:

```python
for i in range(nodesInRows[row]):
```

Damit sieht das Bild nun wie folgt aus und die Erstellung der Knotenpunkte ist abgeschlossen:
![layersFull](./mediaFiles/layersFull.png)

## 2. Erstellen der Kanten

Nachdem nun alle Knotenpunkte erstellt wurden, müssen jetzt die Kanten erstellt werden. Dazu werden Linien zwischen den Knoten erzeugt. Dabei soll jeder Knotenpunkt einer Schicht mit jedem Kontenpunkt der nächsten Schicht verbunden werden. Die grundlegende Idee zur Lösung dieser Aufgabe lässt sich dabei sehr einfach mit folgendem Algorithmus beschreiben:
```
für alle Schichten s außer der letzten:
    für alle Knoten k in s:
        für alle Knoten k2 der nächsten Schicht:
            erzeuge Linie zwischen k und k2
```

Implementiert in unserem Programm sieht das dann so aus:

```python
#Draw lines between nodes
lineStrokeWidth = 0.4

for i in range(nOfRows-1):
    for startCircle in rowArray[i]:
        for endCircle in rowArray[i+1]:
            line = Line(startCircle, endCircle, stroke_width=lineStrokeWidth)
            self.add(line)
```

Damit ergibt sich das folgende Bild:

![basicEdges](./mediaFiles/basicEdges.png)

Das sieht schon ganz gut aus, lässt sich aber noch verbessern. Es gibt zwei Probleme:

1. Das Bild ist etwas wirr, da die Linien nicht am gleichen Punkt eines Kreises anfangen und aufhören.
2. Wir haben keinen Zugriff mehr auf die einzelnen Linien.

Im Übrigen empfiehlt es sich, ab hier eine möglichst hohe Render-Auflösung zu wählen, da es bei geringen Auflösungen zu einem starken Staircase-Effekt bei den Linien kommt. Die hier gezeigten Bilder und Videos wurden in 3840x2160 erstellt. Dass kann zum Beispiel mit dem CLI Flag ```-qk``` erreicht werden.

Zur Lösung des ersten Problems kann die Funktion ```point_at_angle(angle)``` eines Kreises verwendet werden um einen speziellen Startpunkt/Endpunkt für die Linien zu finden. Die Implementierung wäre dann folgende:

```python
lineStrokeWidth = 0.4

for i in range(nOfRows-1):
    for startCircle in rowArray[i]:
        startCirclePointCoords = startCircle.point_at_angle(0*DEGREES)
        
        for endCircle in rowArray[i+1]:
            endCirclePointCoords = endCircle.point_at_angle(180*DEGREES)

            line = Line(startCirclePointCoords, endCirclePointCoords, stroke_width=lineStrokeWidth)
            self.add(line)
```

Das zweite Problem kann ganz einfach wie zuvor bei den Knotenpunkten gelöst werden, indem die Linien mithilfe von Arrays gespeichert werden. Die Struktur des Arrays ist dann diese: ```rows[nodes[lines[]]]```. Auf die erste Kante des ersten Knoten der ersten Schicht kann dann zum Beispiel so zugegriffen werden: ```lineArray[0][0][0]```. Die Implementierung dieses Konzepts sieht dann so aus:

```python
lineStrokeWidth = 0.4
lineArray = []

for i in range(nOfRows-1):
    linesFromRow = []
    
    for startCircle in rowArray[i]:
        startCirclePointCoords = startCircle.point_at_angle(0*DEGREES)

        linesFromCircle = []

        for endCircle in rowArray[i+1]:
            endCirclePointCoords = endCircle.point_at_angle(180*DEGREES)

            line = Line(startCirclePointCoords, endCirclePointCoords, stroke_width=lineStrokeWidth)
            self.add(line)

            linesFromCircle.append(line)

        linesFromRow.append(linesFromCircle)

    lineArray.append(linesFromRow)
```

Damit sind die Kanten nun vollständig erzeugt und es ergibt sich folgendes Bild:

![edgesFull](./mediaFiles/edgesFull.png)

## 3. Animieren der Knoten und Kanten

Jetzt wo die grundlegende Grafik erzeugt wurde, müssen die Animationen hinzugefügt werden.

Die Animationen der Knoten ist eine Farbveränderungen der Füllfarbe der Kreise. Prinzipiell kann die Füllfarbe eines Objekts mithilfe der Methode ```set_fill(color, opacity)``` durchgeführt werden. Damit diese Veränderung allerdings animiert wird muss zuerst auf ```animate(run_time)``` zugegriffen werden. Um die Veränderung der Füllfarbe zu animieren wird dann beispielsweise folgender Code benötigt: ```animation = object.animate(run_time=2).set_fill(RED, 0.7)```. Zur Auswahl welche Knoten animiert werden und welche nicht gibt es verschiedene Möglichkeiten. Es wäre zum Beispiel möglich, die Knoten per Hand auszuwählen oder die Knoten mit Zufallszahlen zu bestimmen. In diesem Fall werden allerdings Divisoren verwendet, um die Knoten zu bestimmen. Das hat den Vorteil, dass man etwas mehr Kontrolle darüber hat, welche Objekte animiert werden und welche nicht. Mit ```i % divisor == 0``` kann bestimmt werden ob ```i``` durch einen Divisor ohne Rest teilbar ist. So ergibt sich die folgende Funktion:

```python
def animateNodeColor (row, divisor1, divisor2, array, color):
    for i in range(len(row)):
        if i % divisor1 == 0:
            array.append(row[i].animate(run_time=2).set_fill(color, 0.7))
        if i % divisor2 == 0:
            array.append(row[i].animate(run_time=2).set_fill(color, 0.7))
```

Wie zu sehen ist, werden die Animationen einem Array hinzugefügt anstatt sie gleich abzuspielen. Der Grund dafür ist einfach: Die Animationen einer Schicht sollen alle gleichzeitig abgespielt werden, würden die Animationen direkt in der for-Schleife ausgeführt, würden diese nacheinander abgespielt werden.

Mithilfe dieser Funktion ist es nun möglich, die Knoten-Animationen der ersten drei Schichten zu erzeugen:

```python
nodeAnimationFirstRow = []
nodeAnimationSecondRow = []
nodeAnimationThirdRow = []

animateNodeColor(rowArray[0], 2, 3, nodeAnimationFirstRow, RED)
animateNodeColor(rowArray[1], 3, 5, nodeAnimationSecondRow, RED)
animateNodeColor(rowArray[2], 4, 6, nodeAnimationThirdRow, RED)
```

Da in der Output-Schicht nur ein einziger Knoten animiert werden soll, wird dieser manuell animiert:

```pyhton
nodeAnimationFourthRow = rowArray[3][6].animate(run_time=2).set_fill(RED, 0.7)
```

Um die Animationen auszuführen wird folgender Code verwendet:

```python
self.play(*nodeAnimationFirstRow)
self.play(*nodeAnimationSecondRow)
self.play(*nodeAnimationThirdRow)
self.play(nodeAnimationFourthRow)
```

Es gilt darauf zu achten, dass hier der ```*``` Operator verwendet wird um die Arrays zu entpacken. Damit ergibt sich nun folgende Animation:

https://user-images.githubusercontent.com/50620058/153039693-d7dbd714-51b7-4a7e-9a57-2b4f16689cd8.mp4


Als Nächstes müsssen noch die Kanten animiert werden. Dies läuft grundlegend sehr ähnlich ab wie zuvor bei den Knoten, allerdings wird für das Erzeugen der eigentlichen Animation eine andere Funktion verwendet. Mithilfe von ```ShowPassingFlash(object, run_time, time_width)``` kann eine Animation erstellt werden, die nur einen Teil eines Objekts auf einmal zeigt. Das bedeutet, dass eigentlich nicht die bereits exestierenden Linien animiert werden, sondern jeweils eine neue Linie über den alten Linien erzeugt, wird die aber immer nur teilweise zu sehen ist. Dazu können die Linien-Objekte mit ```.copy()``` kopiert werden und dann die Kopien in ```ShowPassingFlash(object, run_time, time_width)``` verwendet werden um die Animationen zu erzeugen. Das könnte dann beispielsweise so aussehen: ```animation = ShowPassingFlash(line.copy().set_color(RED), run_time=2, time_width=1)```. Neben dieser Veränderung funktioniert der Rest wieder genauso wie zuvor:

```python
#line color change
def animateLineColor (nodeArray, divisor1, divisor2, array, color):
    for node in nodeArray:
        for i in range(len(node)):
            if i % divisor1 == 0:
                array.append(ShowPassingFlash(node[i].copy().set_color(color), run_time=2, time_width=1))
            if i % divisor2 == 0:
                array.append(ShowPassingFlash(node[i].copy().set_color(color), run_time=2, time_width=1))


lineAnimationsFirstRow = []        
lineAnimationsSecondRow = []
lineAnimationsThirdRow = []

animateLineColor(lineArray[0], 2, 3, lineAnimationsFirstRow, RED)
animateLineColor(lineArray[1], 3, 5, lineAnimationsSecondRow, RED)
animateLineColor(lineArray[2], 4, 6, lineAnimationsThirdRow, RED)
```

Zur Ausführung der neuen Animationen müssen die exestierenden ```self.play()``` statements angepasst werden:

```python
self.play(*nodeAnimationFirstRow)
self.play(*lineAnimationsFirstRow, *nodeAnimationSecondRow)
self.play(*lineAnimationsSecondRow, *nodeAnimationThirdRow)
self.play(*lineAnimationsThirdRow, nodeAnimationFourthRow)
```

Die fertige Animation sieht dann so aus:

https://user-images.githubusercontent.com/50620058/153039740-a005f9ba-0ce0-4579-8bd6-59b7e1575c25.mp4

## 4. Einfügen von Details (Klammer, Beschriftung, Hervorhebung)

Das Video ist nun fast fertig. Es fehlen nur noch ein paar Details. In diesem letzten Schritt wird nun noch die Klammer, die Beschriftung und die Hervorhebung des Output-Knoten eingefügt.

Zuerst wird die Klammer für die erste Schicht erstellt. Das ist sehr einfach und kann mit ```Brace(object, orientation)``` durchgeführt werden. Um einen Text hinzuzufügen stellt die ```Brace``` Klasse die Methode ```get_text(text)``` zur Verfügung. Zusammen sieht das dann so aus:

```python
brace = Brace(rowGroups[0], LEFT)
braceText = brace.get_text("784")

self.add(brace, braceText)
```

Nachdem nun die Klammer erzeugt wurde, gilt es jetzt die Output-Knoten zu beschriften. Dafür wird mit ```Text()``` für jeden Knoten der letzten Schicht ein Text erstellt und dann rechts neben dem jeweiligen Knoten angeordnet. Außerdem werden die Texte wieder wie zuvor einem Array hinzugefügt, um auf sie weiter Zugriff zu haben.

```python
numberTextArray = []

for i in range(len(rowArray[3])):
    text = Text(str(i), font_size=15)
    text.next_to(rowArray[3][i], RIGHT)
    self.add(text)
    numberTextArray.append(text)
```

Jetzt bleibt nur noch eine einzige Sache übrig: das Hervorheben des Output-Knotens. Eine solche Hervorhebung kann mit ```Circumscribe(object)``` durchgeführt werden. Dabei macht es Sinn, auch wieder die Eigenschaften ```time_width``` und ```run_time``` festzulegen. Da der Knotenpunkt zusammen mit der dazugehörigen Beschriftung hervorgehoben werden soll, wird hier wieder eine VGroup verwendet:

```python
self.play(Circumscribe(VGroup(rowArray[3][6], numberTextArray[6]), time_width=5, run_time=5))
```

Damit wurden nun auch die Details hinzugefügt und das Video ist komplett:

https://user-images.githubusercontent.com/50620058/152992613-4eec1536-6a23-4994-9444-9d7e46e7034d.mp4

Wie zu sehen ist, ist es mit Manim gut möglich auch komplexere Szenen zu erstellen. Die einzelnen Bausteine sind einfach zu verwenden und lassen sich leicht zu größeren Szenen kombinieren.
