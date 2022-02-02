from manim import *
from scipy.optimize import fsolve


class twoDFuntion(Scene):

    def construct(self):
        #Koordinatensystem erstellen
        axes = Axes(
            x_range=[-1, 52, 2],
            y_range=[-1, 6],
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": np.arange(0, 51, 10), "numbers_with_elongated_ticks": np.arange(0, 51, 10)},
            y_axis_config={"numbers_to_include": np.arange(-1, 6)})
        
        #Erste Gleichung visualisieren
        logGraph = axes.plot(lambda x: np.log(x), x_range=[0.1, 51], color=RED)

        #Zweite Gleichung visualisieren
        def powerOf2(x):
            return (x-25)**2

        powerOf2Graph = axes.plot(powerOf2, x_range=[22, 28],  color=GREEN)

        #Punkt auf der ersten Gleichung markieren
        cords = axes.input_to_graph_point(25, logGraph)
        lines = axes.get_lines_to_point(cords, color=BLUE)

        #Finden der Schnittpunkte
        def findIntersection(function1, function2, x0):
            return fsolve(lambda x: function1(x) - function2(x), x0)
        
        firstIntersectX = findIntersection(powerOf2, np.log, 23)
        secondIntersectX = findIntersection(powerOf2, np.log, 26)
        print(firstIntersectX, secondIntersectX)

        #Hervorheben des Bereichs zwischen den Gleichungen
        area = axes.get_area(powerOf2Graph, bounded_graph=logGraph, x_range=[firstIntersectX, secondIntersectX], color=GREY)


        #Alle erstellten Ellemente zur Grafik hinzufügen
        self.add(axes, logGraph, powerOf2Graph, lines, area)