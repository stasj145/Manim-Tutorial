from manim import *

class basic(Scene):

    def construct(self):

        circle = Circle()

        circle.set_color(GREEN)
        circle.set_fill(opacity=0.5)

        square = Square()

        square.set_color(BLUE)
        square.set_fill(RED, opacity=0.5)

        square.rotate(45*DEGREES)

        square.next_to(circle, RIGHT, buff=2)


        triangle = Triangle()
        triangle.set_color(BLUE)
        triangle.set_fill(opacity=0.5)

        triangle.shift(RIGHT + UP*3)


        text = Text("Mein Text", font_size=60, color=ORANGE).move_to(LEFT*4)


        line = Line(triangle, circle)

        arrow = Arrow(triangle, square)
        
        self.add(circle, square, triangle, line, arrow, text)
        
        # self.wait(1)
        # self.remove(text)
        # self.wait(1)
