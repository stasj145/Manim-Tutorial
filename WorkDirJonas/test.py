from manim import *


class test(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        
        arrow = Arrow(start=RIGHT, end=LEFT, color=GREEN)
        arrow.next_to(circle, LEFT)

        dot = Dot()
        dot.next_to(circle, RIGHT, buff=2)
        
        dotOnCircle = dot.copy()
        dotOnCircle.move_to(circle)
        dotOnCircle.shift(RIGHT)

        self.add(dot)
        self.play(Create(circle))
        self.play(Create(arrow))
        self.play(Transform(dot, dotOnCircle))
        self.play(MoveAlongPath(dot,circle))
