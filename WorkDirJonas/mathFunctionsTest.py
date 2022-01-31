from pdb import line_prefix
from manim import *

class mathFunctionTest(Scene):
    def construct(self):
        
        #function
        def func(x):
            return 2*x+np.cos(x) + 1
        
        axes = Axes(x_range=[0, 10], y_range=[0,10], axis_config={"numbers_to_include": np.arange(10)})
        graph = axes.plot(func)
        
        lineX = axes.get_vertical_line(axes.input_to_graph_point(3, graph))
        lineY = axes.get_horizontal_line(axes.input_to_graph_point(3, graph))

        dot = Dot() 
        dot.move_to(axes.input_to_graph_point(0, graph))
        dot.set_color(RED)

        self.add(axes, graph, lineX, lineY, dot)
        self.play(MoveAlongPath(dot, graph), run_time=10)

