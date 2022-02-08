from manim import *

class knnParts(Scene):
    def construct(self):
        circleRadius = 0.1
        circleStrokeWidth = 2
        circleCollor = BLUE


        spacingMultiplier = 0.3

        nOfRows = 4
        nodesInRows = [16, 16, 16, 10]

        rowArray = []
        rowGroups = []
        
        for row in range(nOfRows):
            group = VGroup()
            circleArray = []

            for i in range(nodesInRows[row]):
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


        #Create Space in first row
        for i in range(int(len(rowArray[0])/2), len(rowArray[0])):
            circle = rowArray[0][i]
            circle.shift(DOWN)

        #Arrange rows
        rowGroups[0].move_to(LEFT*5)
        rowGroups[1].move_to(LEFT*2)
        rowGroups[2].move_to(RIGHT)
        rowGroups[3].move_to(RIGHT*4)


        #add points in first row
        rad=0.02
        buff=0.2
        p1, p2, p3= Dot(radius = rad), Dot(radius = rad), Dot(radius = rad)
        p1.next_to(p2, UP, buff=buff)
        p3.next_to(p2, DOWN, buff=buff)

        dotGroup = VGroup(p1, p2, p3)
        dotGroup.move_to(LEFT*5)

        self.add(p1, p2, p3)