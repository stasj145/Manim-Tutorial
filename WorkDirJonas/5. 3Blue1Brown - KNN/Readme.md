# 5. 3Blue1Brown - KNN
Nachdem in den vorherigen Kapiteln verschiedene Grundlagen dargestellt wurden, sollen diese nun verbunden werden um komplexere Szenen zu erstellen. Als vorlage dienen dafür Grafiken aus den Videos von 3Blue1Brow auf YouTube.
In diesem Kapitel soll eine Visualisierung eines einfachen künstlichen neuronalen Netzes erzeugt werden.

Vorlage: 3Blue1Brown - [But what is a neural network? | Chapter 1, Deep learning](https://www.youtube.com/watch?v=aircAruvnKk&t=103s) [Zeit: 1:43-2:05]

Ziel dieses Kapitels ist das Erstellen des folgenden Videos:

https://user-images.githubusercontent.com/50620058/152992613-4eec1536-6a23-4994-9444-9d7e46e7034d.mp4

Das erstellen dieser Szene kann grob in 4 Abschnitte unterteilt werden:
1. Erstellen der Knotenpunkte (Kreise)
2. Erstellen der Kanten (Linien zwischen Knoten)
3. Animieren der Knoten und Kanten
4. Einfügen von Details (Klammer, Beschriftung, hervorhebung)

Dabei wird neben den bereits bekannten Konzepten auch die neue Funktionalität der ```VGroup``` eingeführt. Eine ```VGroup``` ermöglicht es mehrere Objekte zu verbinden und gemeinsam zu bearbeiten.

## 1. Erstellen der Knotenpunkte
Zuerst sollen die Knotenpunkte erstellt werden welche die künstlichen Neuronen des Netzes darstellen. Dabei solle es vier Schichten schichten geben: eine Input-Schicht mit 784 Knoten, zwei versteckte-Schichten mit je 16 Knoten und eine output-Schicht mit 10 Knoten.

Die Einzelnen Knoten werden mithilfe der ```Circle()``` Funktion erzeugt. Dabei müssen die folgenden drei Eigenschaften angepasst werden: ```stroke_color```, ```stroke_width``` und ```radius```. In diesem Fall habe ich mich für einen Radius von 0,1 und eine ```stroke_width``` von 2 enschieden, außerdem werden die Kreise in Blau dargestellt.

```python
circleRadius = 0.1
circleStrokeWidth = 2
circleCollor = BLUE

newCircle = Circle(stroke_color=circleCollor, stroke_width=circleStrokeWidth, radius=circleRadius)
```
Daraus ergibt sich der folgende Kreis:

![basicNode](./mediaFiles/basicNode.png)

Für die Grafik werden natürlich deutlich mehr Kreise benötigt. Beginnen wir damit eine einzelne Schicht des knn zu erstellen. Dazu wird eine einfach for-Schleife verwendet und die neuen Kreise mit jeder Iteration weiter nach unter verschoben. Dazu kann die ```shift```  Funktion verwendet werden. Das sieht dann etwa so aus:
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
Wie zu sehen ist wurde hier zusätzlich noch die Variable "spacingMultiplier" eingeführt, mit dieser kann der Abstand zwischen den Kreise verändert werden. Da dieser standarmäßig recht groß ist wird hier ein Multiplikator von 0,3 eingesetzt. Außerdem werden die Kreise mit ```self.add(newCircle)``` jeweils zur Grafik hinzugefügt.

Damit ergibt sich dieses Bild:

![basicLayerBroken](./mediaFiles/basicLayerBroken.png)

Wie zu sehen ist wurde eine Reihe von Kreisen erzeugt. Diese ist allerdings nicht gut im Bild positioniert. Um die Position der Kreise zu ändern werden diese zu einer ```VGroup``` hinzugefügt. Das ermöglicht es die gesamte Schicht auf einmal zu bewegen, anstatt alle einzeln zu positionieren. Außerdem werden die Kreise nun zu einem Array hinzugefügt, dies ermöglicht es später noch auf jeden einzelnen Kreis zuzugreifen.
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

Damit wurde nun erfolgreich eine erste Schicht des KNN erzeugt. Es werden allerding vier Schichten benötigt. Dazu wird eine weitere for-Schleife benötigt. Um auch später noch Zugriff auf die einzelnen Kreise sowie die VGroups zu haben werden diese jeweils wieder einem Array hinzugefügt. Dadurch ergibt sich schließlich ein Array mit allen VGroups, sowie ein 2-Dimensionales Array mit allen Kreisen.

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

Wie schon zuvor müssen die erzeugten Schichten nun noch Positioniert werden. Dazu werden wieder die VGroups verwendet auf die über ```rowArray``` zugegriffen werden kann:

```python
rowGroups[0].move_to(LEFT*5)
rowGroups[1].move_to(LEFT*2)
rowGroups[2].move_to(RIGHT)
rowGroups[3].move_to(RIGHT*4)
```

Nun sieht die Grafk so aus:

![allLayersSameSize](./mediaFiles/allLayersSameSize.png)

Momentan haben noch alle Schichten die gleiche Größe von 16 Knotenpunkten. Eigentlich sollen die Schichten aber 784 - 16 - 16 - 10 Groß sein. Da es nicht genug Platz gibt um in der ersten schicht 784 Knoten anzuzeigen werden hier einfach 16 Knoten dargestellt und in der Mitte drei Punkte angezeigt welche zeigen das es dort eigentlich noch mehr Knoten gibt.

Zu diesem Zweck wird einfach die untere Hälfte der Kreise der ersten Schicht nach unter bewegt. Dabei ist es wichtig das dies geschiet bevor die Schichten über die VGroups angeordnet werden. Auf die einzelnen Kreise kann über ```rowArray``` zugegriffen werden:

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

Nun gibt es Platz in der Mitter der ersten Schicht in dem die Punkte eingefügt werden können. Dazu werden drei kleine Punkte erzeugt und untereinander angeordnet. Diese Punkte werden dann wieder einer VGroup hinzugefügt und die Gruppe dann nach Links verschoben:

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

Nachdem jetzt die erste Schicht angepasst wurde musss nun noch die letzte Schicht verändert werden, diese sollte eigentlich nur 10 Knoten enthalten besteht aber akktuell noch aus 16. Ein einfache Weg dies zu lösen und den Code dabei auch noch modularer zu machen ist das ändern der for-Schleife die die Schichten erzeugt. Statt immer fest 16 Knoten zu erzeugen wird nun stattdessen ein Array verwendet in dem die Größe jeder einzelnen Schicht festgelegt ist. Dazu wird zuerst das Array angelegt ```nodesInRows = [16, 16, 16, 10]``` und schließlich die for-Schleife verändert.

```python
for i in range(16):
```

wird zu:

```python
for i in range(nodesInRows[row]):
```

Damit sieht das Bild nun wie folgt aus und die Erstellung der Knotenpunkte ist abgeschloßen.
![layersFull](./mediaFiles/layersFull.png)

## 2. Erstellen der Kanten

