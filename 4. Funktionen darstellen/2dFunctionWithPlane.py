from manim import *

class twoDFuntionWithPlane(MovingCameraScene):

    def construct(self):
         #koordinatensystem erstellen
        plane = NumberPlane(
            #beschränkt auf -7.11, 7.11, -4, 4
            x_range=[-10, 10, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": np.arange(-10, 11, 1)},
            y_axis_config={"numbers_to_include": np.arange(-5, 6, 1)})
        
        sinGraph = plane.plot(lambda x: np.sin(x), color=GREEN)
        cosGraph = plane.plot(lambda x: np.cos(x), color=TEAL)


        self.add(plane, sinGraph, cosGraph)

        #Position speichern
        self.camera.frame.save_state()
        #2,5 Sekunden warten
        self.wait(2.5)
        #Kamera nach rechts Bewegen
        self.play(self.camera.frame.animate.shift(RIGHT*10))
        #Herranzoomen
        self.play(self.camera.frame.animate.set(width=self.camera.frame.width/2))
        #2,5 Sekunden warten
        self.wait(2.5)
        #Kamera zurücksetzen
        self.play(Restore(self.camera.frame))
        #Kamera nach links Bewegen
        self.play(self.camera.frame.animate.shift(LEFT*10))
        #2,5 Sekunden warten
        self.wait(2.5)
        #Kamera zurücksetzen
        self.play(Restore(self.camera.frame))
        #Herrauszoomen
        self.play(self.camera.frame.animate.set(width=plane.width*2))
        #Kamera zurücksetzen
        self.play(Restore(self.camera.frame))





