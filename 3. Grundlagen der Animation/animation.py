from manim import *

class basicAnimations(Scene):

    def construct(self):

        circle1 = Circle().move_to(LEFT*2)

        circle2 = Circle().move_to(RIGHT*2)

        self.play(Create(circle1), run_time=2)

        # #Transform

        self.play(Transform(circle1, circle2))

        self.wait(1)

        dot1 = Dot(color=BLUE)

        dot2 = Dot(color=GREEN).move_to(LEFT*2)

        self.play(Transform(dot1, dot2))

        self.play(Transform(circle1, dot1))

        self.wait(1)

        self.play(Transform(circle1, circle2))

        self.wait(1)

        self.clear()

        #.animate

        dot3 = Dot(radius=0.5)

        self.play(dot3.animate.move_to(LEFT*4).set_color(GREEN))

        self.wait(1)

        self.remove(dot3)

        # updater

        newDot = Dot(color=GREEN)

        moveTracker = ValueTracker(0)

        newDot.add_updater(lambda obj: obj.move_to(LEFT*moveTracker.get_value()))

        self.add(newDot)

        self.play(moveTracker.animate.set_value(3))

        self.clear()

        # updater and MoveAlongPath

        newDot = Dot(color=GREEN)

        newCircle = Circle(radius=3, color=RED)

        line = Line(ORIGIN, newDot)
        
        line.add_updater(lambda line: line.become(Line(ORIGIN, newDot)))

        self.add(line)

        self.add(newDot, newCircle)

        self.wait(1)

        self.play(newDot.animate.shift(RIGHT*3))

        self.play(MoveAlongPath(newDot, newCircle), run_time=6)

        self.play(newDot.animate.move_to(ORIGIN))

        self.wait(1)

