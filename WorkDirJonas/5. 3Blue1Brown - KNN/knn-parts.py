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


        #Draw lines between nodes
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


                    #node color change

        def animateNodeColor (row, divisor1, divisor2, array, color):
            for i in range(len(row)):
                if i % divisor1 == 0:
                    array.append(row[i].animate(run_time=2).set_fill(color, 0.7))
                if i % divisor2 == 0:
                    array.append(row[i].animate(run_time=2).set_fill(color, 0.7))
                
        nodeAnimationFirstRow = []
        nodeAnimationSecondRow = []
        nodeAnimationThirdRow = []
        nodeAnimationFourthRow = rowArray[3][6].animate(run_time=2).set_fill(RED, 0.7)

        animateNodeColor(rowArray[0], 2, 3, nodeAnimationFirstRow, RED)
        animateNodeColor(rowArray[1], 3, 5, nodeAnimationSecondRow, RED)
        animateNodeColor(rowArray[2], 4, 6, nodeAnimationThirdRow, RED)


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


        self.play(*nodeAnimationFirstRow)
        self.play(*lineAnimationsFirstRow, *nodeAnimationSecondRow)
        self.play(*lineAnimationsSecondRow, *nodeAnimationThirdRow)
        self.play(*lineAnimationsThirdRow, nodeAnimationFourthRow)
