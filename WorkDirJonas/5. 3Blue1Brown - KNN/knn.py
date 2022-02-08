from tkinter import CENTER
from numpy import number, spacing
from manim import *

class knn(Scene):
    def construct(self):

        nOfRows = 4
        nodesInRows = [16, 16, 16, 10]
        spacingMultiplier = 0.3
        circleRadius = 0.1
        circleStrokeWidth = 2
        circleCollor = BLUE

        rowArray = []
        rowGroups = []
        
        for row in range(nOfRows):
            group = VGroup()
            circleArray = []

            for i in range(nodesInRows[row]):
                newCircle = Circle(stroke_color=circleCollor, stroke_width=circleStrokeWidth, radius=circleRadius)
                circleArray.append(newCircle)
                group.add(newCircle)
                circleArray[i].shift(DOWN*i*spacingMultiplier)
                self.add(circleArray[i])
            
            rowArray.append(circleArray)
            rowGroups.append(group)

        #Create Space in first row
        for i in range(int(nodesInRows[0]/2), nodesInRows[0]):
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


        lineArray = []
        lineStrokeWidth = 0.4

        #Draw lines between nodes
        for i in range(nOfRows-1):
            startRow = rowArray[i]
            endRow = rowArray[i+1]
            linesFromRow = []
            for startCircle in startRow:
                startCirclePointCoords = startCircle.point_at_angle(0*DEGREES)
                linesFromCircle = []
                for endCircle in endRow:
                    endCirclePointCoords = endCircle.point_at_angle(180*DEGREES)
                    line = Line(startCirclePointCoords, endCirclePointCoords, stroke_width=lineStrokeWidth).set_resampling_algorithm("antialias")
                    self.add(line)
                    linesFromCircle.append(line)
                linesFromRow.append(linesFromCircle)
            lineArray.append(linesFromRow)


        #line color change
        def animateLineColor (lineNumber, divisor1, divisor2, array, color):
            for node in lineArray[lineNumber]:
                for i in range(len(node)):
                    if i % divisor1 == 0:
                        array.append(ShowPassingFlash(node[i].copy().set_color(color), run_time=2, time_width=1))
                    if i % divisor2 == 0:
                        array.append(ShowPassingFlash(node[i].copy().set_color(color), run_time=2, time_width=1))


        lineAnimationsFirstRow = []        
        lineAnimationsSecondRow = []
        lineAnimationsThirdRow = []

        animateLineColor(0, 2, 3, lineAnimationsFirstRow, RED)
        animateLineColor(1, 3, 5, lineAnimationsSecondRow, RED)
        animateLineColor(2, 4, 6, lineAnimationsThirdRow, RED)


        #node color change

        def animateNodeColor (lineNumber, divisor1, divisor2, array, color):
            row = rowArray[lineNumber]
            for i in range(len(row)):
                if i % divisor1 == 0:
                    array.append(row[i].animate(run_time=2).set_fill(color, 0.7))
                if i % divisor2 == 0:
                    array.append(row[i].animate(run_time=2).set_fill(color, 0.7))
                
        nodeAnimationFirstRow = []
        nodeAnimationSecondRow = []
        nodeAnimationThirdRow = []
        nodeAnimationFourthRow = rowArray[3][6].animate(run_time=2).set_fill(RED, 0.7)

        animateNodeColor(0, 2, 3, nodeAnimationFirstRow, RED)
        animateNodeColor(1, 3, 5, nodeAnimationSecondRow, RED)
        animateNodeColor(2, 4, 6, nodeAnimationThirdRow, RED)


        numberTextArray = []
        #add numbers to last row
        for i in range(len(rowArray[3])):
            text = Text(str(i), font_size=15)
            text.next_to(rowArray[3][i], RIGHT)
            self.add(text)
            numberTextArray.append(text)

        brace = Brace(rowGroups[0], LEFT)
        braceText = brace.get_text("784")

        self.add(brace, braceText)



        self.play(*nodeAnimationFirstRow)
        self.play(*lineAnimationsFirstRow, *nodeAnimationSecondRow)
        self.play(*lineAnimationsSecondRow, *nodeAnimationThirdRow)
        self.play(*lineAnimationsThirdRow, nodeAnimationFourthRow)

        #draw box around number and node in last row
        self.play(Circumscribe(VGroup(rowArray[3][6], numberTextArray[6]), time_width=5, run_time=5))

        self.wait(2)