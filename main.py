from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

class RotatingCube(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        cube = Cube(side_length=2, fill_color=BLUE, fill_opacity=0.7)
        
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes, cube)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(4)
        self.stop_ambient_camera_rotation()

class GraphExample(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 20, 2],
            x_length=9,
            y_length=6,
            axis_config={"color": WHITE},
        )
        
        # 抛物线函数
        graph = axes.plot(lambda x: x**2, color=YELLOW)
        
        self.play(Create(axes))
        self.play(Create(graph))
        self.wait(2)