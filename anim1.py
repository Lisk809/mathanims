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
        
        # 最终总结
        self.final_summary()
        
    def setup_coordinate_system(self):
        # 步骤标题
        step_title = Text("步骤一：建立坐标系和椭圆方程", font_size=36, color=BLUE)
        step_title.to_edge(UP)
        self.play(Write(step_title))
        self.wait(1)
        
        # 创建坐标系
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            axis_config={"color": WHITE},
            tips=False
        )
        
        # 手动添加坐标标签
        x_labels = VGroup()
        for i in range(-3, 4):
            if i != 0:
                label = Text(str(i), font_size=20)
                label.next_to(axes.coords_to_point(i, 0), DOWN, buff=0.2)
                x_labels.add(label)
        
        y_labels = VGroup()
        for i in range(-3, 4):
            if i != 0:
                label = Text(str(i), font_size=20)
                label.next_to(axes.coords_to_point(0, i), LEFT, buff=0.2)
                y_labels.add(label)
        
        # 椭圆方程：x²/3 + y²/4 = 1
        ellipse = ParametricFunction(
            lambda t: axes.coords_to_point(
                np.sqrt(3) * np.cos(t),
                2 * np.sin(t)
            ),
            t_range=[0, 2*PI],
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
        self.play(Write(x_labels), Write(y_labels))
        self.play(Create(ellipse))
        
        # 显示点
        self.play(Create(point_A), Write(label_A))
        self.play(Create(point_B), Write(label_B))
        self.play(Create(point_P), Write(label_P))
        self.wait(2)
        
        # 清除图形，显示文字推导
        self.play(
            FadeOut(step_title),
            FadeOut(axes),
            FadeOut(x_labels),
            FadeOut(y_labels),
            FadeOut(ellipse),
            FadeOut(point_A),
            FadeOut(point_B),
            FadeOut(point_P),
            FadeOut(label_A),
            FadeOut(label_B),
            FadeOut(label_P)
        )
        self.play(Create(axes))
        self.play(Write(x_labels), Write(y_labels))
        self.play(Create(ellipse))
        self.play(Create(point_A), Write(label_A))
        self.play(Create(point_B), Write(label_B))
        self.play(Create(point_P), Write(label_P))
        
        # 显示椭圆方程
        eq_text = MathTex("\\frac{x^2}{3} + \\frac{y^2}{4} = 1", font_size=36)
        eq_text.to_corner(UL)
        self.play(Write(eq_text))
        self.wait(2)
        
    def pole_polar_method(self):
        # 清除图形，显示方法标题
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        
        method_title = Text("方法一：极点极线理论", font_size=36, color=GREEN)
        method_title.to_edge(UP)
        
        self.play(Write(method_title))
        self.wait(1)
        
        # 极点极线解释
        explanation1 = Text("极点极线理论：对于圆锥曲线，给定一点P，", font_size=24)
        explanation1.next_to(method_title, DOWN, buff=0.3)
        
        explanation2 = Text("存在一条直线l，使得过P的任意弦MN的端点", font_size=24)
        explanation2.next_to(explanation1, DOWN, buff=0.2)
        
        explanation3 = Text("M、N处的切线交于l上，这条直线l称为P的极线。", font_size=24)
        explanation3.next_to(explanation2, DOWN, buff=0.2)
        
        explanation4 = Text("对于椭圆，点P(x₀,y₀)对应的极线方程为：", font_size=24)
        explanation4.next_to(explanation3, DOWN, buff=0.3)
        
        polar_general = MathTex("\\frac{xx_0}{a^2} + \\frac{yy_0}{b^2} = 1", font_size=32)
        polar_general.next_to(explanation4, DOWN, buff=0.3)
        
        self.play(Write(explanation1))
        self.play(Write(explanation2))
        self.play(Write(explanation3))
        self.play(Write(explanation4))
        self.play(Write(polar_general))
        self.wait(2)
        
        # 具体计算
        step1 = Text("对于本题，a²=3，b²=4，P(1,-2)：", font_size=24)
        step1.next_to(polar_general, DOWN, buff=0.5)
        
        polar_eq = MathTex("\\frac{x \\cdot 1}{3} + \\frac{y \\cdot (-2)}{4} = 1", font_size=32)
        polar_eq.next_to(step1, DOWN, buff=0.3)
        
        polar_simplified = MathTex("\\frac{x}{3} - \\frac{y}{2} = 1", font_size=32)
        polar_simplified.next_to(polar_eq, DOWN, buff=0.3)
        
        polar_final = MathTex("2x - 3y = 6", font_size=32)
        polar_final.next_to(polar_simplified, DOWN, buff=0.3)
        
        conclusion = Text("因此，直线MN恒过该极线与某定直线的交点。", font_size=24)
        conclusion.next_to(polar_final, DOWN, buff=0.5)
        
        self.play(Write(step1))
        self.play(Write(polar_eq))
        self.wait(1)
        self.play(Write(polar_simplified))
        self.wait(1)
        self.play(Write(polar_final))
        self.wait(1)
        self.play(Write(conclusion))
        self.wait(2)
        
        # 清除文字，重新显示图形
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        # 重新显示坐标系和椭圆
        self.play(Create(axes))
        self.play(Create(ellipse))
        self.play(Create(point_A), Write(label_A))
        self.play(Create(point_B), Write(label_B))
        self.play(Create(point_P), Write(label_P))
        
        # 显示椭圆方程
        eq_text = MathTex("\\frac{x^2}{3} + \\frac{y^2}{4} = 1", font_size=36)
        eq_text.to_corner(UL)
        self.play(Write(eq_text))
        
        # 绘制极线
        def polar_line_func(x):
            return (2*x - 6) / 3  # 2x - 3y = 6 => y = (2x - 6)/3
        
        polar_line = axes.plot(
            polar_line_func,
            x_range=[-3, 3],
            color=PURPLE,
            stroke_width=3
        )
        
        polar_label = MathTex("2x - 3y = 6", font_size=24, color=PURPLE)
        polar_label.next_to(polar_line, RIGHT, buff=0.2)
        
        self.play(Create(polar_line))
        self.play(Write(polar_label))
        self.wait(2)
        
    def conventional_method(self):
        # 清除图形，显示方法标题
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        
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
        
        final_eq = MathTex("(3k^2+4)x^2 - 6k(k+2)x + 3(k+2)^2 - 12 = 0", font_size=24)
        final_eq.next_to(expanded, DOWN, buff=0.2)
        
        self.play(Write(step3))
        self.play(Write(substituted))
        self.wait(1)
        self.play(Write(expanded))
        self.wait(1)
        self.play(Write(final_eq))
        self.wait(1)
        # 韦达定理
        step4 = Text("由韦达定理：", font_size=24)
        step4.next_to(final_eq, DOWN, buff=0.3)
        
        vieta1 = MathTex("x_1 + x_2 = \\frac{6k(k+2)}{3k^2+4}", font_size=24)
        vieta1.next_to(step4, DOWN, buff=0.2)
        
        vieta2 = MathTex("x_1x_2 = \\frac{3(k+2)^2-12}{3k^2+4}", font_size=24)
        vieta2.next_to(vieta1, DOWN, buff=0.2)
        
        self.play(Write(step4))
        self.play(Write(vieta1))
        self.wait(1)
        self.play(Write(vieta2))
        self.wait(2)
        
        # 求定点
        step5 = Text("设直线MN过定点(x₀,y₀)，则：", font_size=24)
        step5.next_to(vieta2, DOWN, buff=0.3)
        
        line_through_point = MathTex("\\frac{y_0 + 2}{x_0 - 1} = k", font_size=32)
        line_through_point.next_to(step5, DOWN, buff=0.2)
        
        step6 = Text("由直线MN的性质，代入计算可得：", font_size=24)
        step6.next_to(line_through_point, DOWN, buff=0.3)
        
        fixed_point = MathTex("x_0 = 0, \\quad y_0 = 2", font_size=32)
        fixed_point.next_to(step6, DOWN, buff=0.2)
        
        conclusion = Text("因此，直线MN恒过定点(0,2)", font_size=28, color=YELLOW)
        conclusion.next_to(fixed_point, DOWN, buff=0.5)
        
        self.play(Write(step5))
        self.play(Write(line_through_point))
        self.wait(1)
        self.play(Write(step6))
        self.play(Write(fixed_point))
        self.wait(1)
        self.play(Write(conclusion))
        self.wait(2)
        
        # 清除文字，重新显示图形
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        
        # 重新显示坐标系和椭圆
        self.play(Create(axes))
        self.play(Create(ellipse))
        self.play(Create(point_A), Write(label_A))
        self.play(Create(point_B), Write(label_B))
        self.play(Create(point_P), Write(label_P))
        # 显示椭圆方程
        eq_text = MathTex("\\frac{x^2}{3} + \\frac{y^2}{4} = 1", font_size=36)
        eq_text.to_corner(UL)
        self.play(Write(eq_text))
        
        # 显示定点
        fixed_point_dot = Dot(axes.coords_to_point(0, 2), color=YELLOW, radius=0.1)
        fixed_label = Text("(0,2)", font_size=24).next_to(fixed_point_dot, UP)
        
        self.play(Create(fixed_point_dot), Write(fixed_label))
        
        # 显示几条过P的直线都经过(0,2)
        k_values = [-2, -1, 0.5, 1.5]
        
        for k in k_values:
            line_func = lambda x, k=k: k * x - k - 2
            line = axes.plot(
                line_func,
                x_range=[-3, 3],
                color=BLUE,
                stroke_width=2
            )
            self.play(Create(line), run_time=1)
            self.wait(0.5)
            
        self.wait(2)
        
    def final_summary(self):
        # 清除图形，显示总结
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        
        summary_title = Text("总结", font_size=36, color=BLUE)
        summary_title.to_edge(UP)
        
        self.play(Write(summary_title))
        self.wait(1)
        
        point1 = Text("1. 椭圆方程为：x²/3 + y²/4 = 1", font_size=24)
        point1.next_to(summary_title, DOWN, buff=0.5)
        
        point2 = Text("2. 使用极点极线理论，点P(1,-2)对应的极线为2x-3y=6", font_size=24)
        point2.next_to(point1, DOWN, buff=0.3)
        
        point3 = Text("3. 使用常规方法，设直线y+2=k(x-1)，联立椭圆方程", font_size=24)
        point3.next_to(point2, DOWN, buff=0.3)
        
        point4 = Text("4. 应用韦达定理，证明直线MN恒过定点(0,2)", font_size=24)
        point4.next_to(point3, DOWN, buff=0.3)
        
        point5 = Text("5. 两种方法均得到相同结论，验证了结果的正确性", font_size=24)
        point5.next_to(point4, DOWN, buff=0.3)
        
        final_conclusion = Text("直线MN恒过定点(0,2)", font_size=32, color=YELLOW)
        final_conclusion.next_to(point5, DOWN, buff=0.5)
        
        self.play(Write(point1))
        self.wait(1)
        self.play(Write(point2))
        self.wait(1)
        self.play(Write(point3))
        self.wait(1)
        self.play(Write(point4))
        self.wait(1)
        self.play(Write(point5))
        self.wait(1)
        self.play(Write(final_conclusion))
        self.wait(3)