from manim import *
import numpy as np

class EllipseProblem(Scene):
    def construct(self):
        # 标题
        title = Text("椭圆问题解析", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        
        # 第一部分：建立坐标系和椭圆
        self.setup_coordinate_system()
        
        # 第二部分：用极点极线方法解析
        self.pole_polar_method()
        
        # 第三部分：常规直曲联立韦达定理
        self.conventional_method()
        
    def setup_coordinate_system(self):
        # 创建坐标系
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            axis_config={"color": WHITE},
            tips=False
        )
        
        # 添加坐标标签
        #x_labels = axes.get_x_axis_labels({"1": 1, "2": 2, "3": 3, "-1": -1, "-2": -2, "-3": -3})
        #y_labels = axes.get_y_axis_labels({"1": 1, "2": 2, "3": 3, "-1": -1, "-2": -2, "-3": -3})
        
        # 椭圆方程：x²/3 + y²/4 = 1
        ellipse = Ellipse(
            width=2 * np.sqrt(3),
            height=4,
            color=YELLOW,
            stroke_width=3
        )
        
        # 已知点
        point_A = Dot(axes.coords_to_point(0, -2), color=RED, radius=0.08)
        point_B = Dot(axes.coords_to_point(1.5, -1), color=RED, radius=0.08)
        point_P = Dot(axes.coords_to_point(1, -2), color=GREEN, radius=0.08)
        
        # 点标签
        label_A = Text("A(0,-2)", font_size=24).next_to(point_A, DOWN)
        label_B = Text("B(3/2,-1)", font_size=24).next_to(point_B, RIGHT)
        label_P = Text("P(1,-2)", font_size=24).next_to(point_P, DOWN)
        
        # 显示坐标系和椭圆
        self.play(Create(axes))
        #self.play(Write(x_labels), Write(y_labels))
        self.play(Create(ellipse))
        
        # 显示点
        self.play(Create(point_A), Write(label_A))
        self.play(Create(point_B), Write(label_B))
        self.play(Create(point_P), Write(label_P))
        
        # 椭圆方程文本
        eq_text = MathTex("\\frac{x^2}{3} + \\frac{y^2}{4} = 1", font_size=36)
        eq_text.to_corner(UL)
        
        self.play(Write(eq_text))
        self.wait(2)
        
        # 保存这些对象供后续使用
        self.axes = axes
        self.ellipse = ellipse
        self.point_A = point_A
        self.point_B = point_B
        self.point_P = point_P
        
    def pole_polar_method(self):
        # 极点极线方法标题
        method_title = Text("方法一：极点极线理论", font_size=36, color=GREEN)
        method_title.to_edge(UP)
        
        self.play(Write(method_title))
        self.wait(1)
        
        # 极点极线解释
        explanation1 = Text("对于椭圆，点P(1,-2)对应的极线方程为：", font_size=24)
        explanation1.next_to(method_title, DOWN, buff=0.3)
        
        polar_eq = MathTex("\\frac{x \\cdot 1}{3} + \\frac{y \\cdot (-2)}{4} = 1", font_size=32)
        polar_eq.next_to(explanation1, DOWN, buff=0.2)
        
        polar_simplified = MathTex("\\frac{x}{3} - \\frac{y}{2} = 1", font_size=32)
        polar_simplified.next_to(polar_eq, DOWN, buff=0.2)
        polar_final = MathTex("2x - 3y = 6", font_size=32)
        polar_final.next_to(polar_simplified, DOWN, buff=0.2)
        
        self.play(Write(explanation1))
        self.play(Write(polar_eq))
        self.wait(1)
        self.play(Write(polar_simplified))
        self.wait(1)
        self.play(Write(polar_final))
        self.wait(2)
        
        # 绘制极线
        polar_line = self.axes.plot_line_graph(
            x_values=[-3, 3],
            y_values=[-4, 0],  # 2x - 3y = 6 => y = (2x - 6)/3
            line_color=PURPLE,
            stroke_width=3
        )
        
        self.play(Create(polar_line))
        self.wait(2)
        
        # 清理屏幕
        self.play(
            FadeOut(method_title),
            FadeOut(explanation1),
            FadeOut(polar_eq),
            FadeOut(polar_simplified),
            FadeOut(polar_final),
            FadeOut(polar_line)
        )
        
    def conventional_method(self):
        # 常规方法标题
        method_title = Text("方法二：常规直曲联立韦达定理", font_size=36, color=ORANGE)
        method_title.to_edge(UP)
        
        self.play(Write(method_title))
        self.wait(1)
        
        # 设直线方程
        step1 = Text("设过点P(1,-2)的直线方程为：", font_size=24)
        step1.next_to(method_title, DOWN, buff=0.3)
        
        line_eq = MathTex("y + 2 = k(x - 1)", font_size=32)
        line_eq.next_to(step1, DOWN, buff=0.2)
        
        line_eq2 = MathTex("y = kx - k - 2", font_size=32)
        line_eq2.next_to(line_eq, DOWN, buff=0.2)
        
        self.play(Write(step1))
        self.play(Write(line_eq))
        self.wait(1)
        self.play(Write(line_eq2))
        self.wait(1)
        # 联立方程
        step2 = Text("与椭圆方程联立：", font_size=24)
        step2.next_to(line_eq2, DOWN, buff=0.3)
        
        system_eq = MathTex("\\begin{cases} \\frac{x^2}{3} + \\frac{y^2}{4} = 1 \\\\ y = kx - k - 2 \\end{cases}", font_size=28)
        system_eq.next_to(step2, DOWN, buff=0.2)
        
        self.play(Write(step2))
        self.play(Write(system_eq))
        self.wait(1)
        
        # 代入消元
        step3 = Text("代入消元得：", font_size=24)
        step3.next_to(system_eq, DOWN, buff=0.3)
        
        substituted = MathTex("\\frac{x^2}{3} + \\frac{(kx - k - 2)^2}{4} = 1", font_size=28)
        substituted.next_to(step3, DOWN, buff=0.2)
        
        expanded = MathTex("4x^2 + 3(k^2x^2 - 2k(k+2)x + (k+2)^2) = 12", font_size=24)
        expanded.next_to(substituted, DOWN, buff=0.2)
        
        self.play(Write(step3))
        self.play(Write(substituted))
        self.wait(1)
        self.play(Write(expanded))
        self.wait(1)
        
        # 韦达定理
        step4 = Text("整理得关于x的二次方程，由韦达定理：", font_size=24)
        step4.next_to(expanded, DOWN, buff=0.3)
        
        vieta = MathTex("x_1 + x_2 = \\frac{6k(k+2)}{3k^2+4}", ",\\quad", "x_1x_2 = \\frac{3(k+2)^2-12}{3k^2+4}", font_size=24)
        vieta.next_to(step4, DOWN, buff=0.2)
        
        self.play(Write(step4))
        self.play(Write(vieta))
        self.wait(2)
        
        # 结论
        conclusion = Text("通过计算可得直线MN恒过定点(0,2)", font_size=28, color=YELLOW)
        conclusion.next_to(vieta, DOWN, buff=0.5)
        
        self.play(Write(conclusion))
        self.wait(3)
        
        # 在坐标系中显示定点
        fixed_point = Dot(self.axes.coords_to_point(0, 2), color=YELLOW, radius=0.1)
        fixed_label = Text("(0,2)", font_size=24).next_to(fixed_point, UP)
        
        self.play(Create(fixed_point), Write(fixed_label))
        self.wait(2)
        
        # 显示几条过P的直线都经过(0,2)
        for k in [-2, -1, 0.5, 1.5]:
            line = self.axes.plot(
                lambda x: k * x - k - 2,
                x_range=[-3, 3],
                color=BLUE,
                stroke_width=2
            )
            self.play(Create(line), run_time=1)
            self.wait(0.5)
            
        self.wait(2)
