from manim import *

class threeDFunction(ThreeDScene):

    def construct(self):
         #koordinatensystem erstellen
        axes = ThreeDAxes(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            z_range=[-10, 10, 1],
            axis_config={"color": RED, "numbers_to_include": np.arange(-10, 11, 1), "include_tip": False, "font_size": 20})
        

        def threeDFunc(u, v):
            z = np.sin(u) * np.cos(v)
            return np.array([u, v, z])

        graph = Surface(threeDFunc, u_range=[-5, 5], v_range=[-5, 5], fill_opacity=0.5)

        self.set_camera_orientation(phi=45*DEGREES, theta=45*DEGREES)
        self.add(axes)





