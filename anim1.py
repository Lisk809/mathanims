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
        
        # 推导椭圆方程 - 使用两列布局
        derivation_title = Text("推导椭圆方程", font_size=36, color=BLUE)
        derivation_title.to_edge(UP)
        
        # 左列
        left_column = VGroup()
        
        step1 = Text("设椭圆方程为：", font_size=24)
        left_column.add(step1)
        
        general_eq = MathTex("\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1", font_size=32)
        general_eq.next_to(step1, DOWN, buff=0.3)
        left_column.add(general_eq)
        
        step2 = Text("代入点A(0,-2)：", font_size=24)
        step2.next_to(general_eq, DOWN, buff=0.5)
        left_column.add(step2)
        
        eq_A = MathTex("\\frac{0^2}{a^2} + \\frac{(-2)^2}{b^2} = 1", font_size=32)
        eq_A.next_to(step2, DOWN, buff=0.3)
        left_column.add(eq_A)
        
        eq_A_simplified = MathTex("\\frac{4}{b^2} = 1", font_size=32)
        eq_A_simplified.next_to(eq_A, DOWN, buff=0.3)
        left_column.add(eq_A_simplified)
        
        eq_A_result = MathTex("b^2 = 4", font_size=32)
        eq_A_result.next_to(eq_A_simplified, DOWN, buff=0.3)
        left_column.add(eq_A_result)
        
        # 右列
        right_column = VGroup()
        
        step3 = Text("代入点B(3/2,-1)：", font_size=24)
        right_column.add(step3)
        
        eq_B = MathTex("\\frac{(3/2)^2}{a^2} + \\frac{(-1)^2}{4} = 1", font_size=32)
        eq_B.next_to%(step3, DOWN, buff=0.3)
        right_column.add(eq_B)
        
        eq_B_simplified = MathTex("\\frac{9/4}{a^2} + \\frac{1}{4} = 1", font_size=32)
        eq_B_simplified.next_to(eq_B, DOWN, buff=0.3)
        right_column.add(eq_B_simplified)
        
        eq_B_further = MathTex("\\frac{9}{4a^2} = \\frac{3}{4}", font_size=32)
        eq_B_further.next_to(eq_B_simplified, DOWN, buff=0.3)
        right_column.add(eq_B_further)
        
        eq_B_result = MathTex("a^2 = 3", font_size=32)
        eq_B_result.next_to(eq_B_further, DOWN, buff=0.3)
        right_column.add(eq_B_result)
# 最终方程
        final_eq = MathTex("\\frac{x^2}{3} + \\frac{y^2}{4} = 1", font_size=36)
        final_eq.next_to(eq_B_result, DOWN, buff=0.5)
        right_column.add(final_eq)
        
        # 定位两列
        left_column.move_to(LEFT * 3.5)
        right_column.move_to(RIGHT * 3.5)
        
        self.play(Write(derivation_title))
        self.wait(1)
        
        # 显示左列
        for obj in left_column:
            self.play(Write(obj))
            self.wait(0.5)
        
        # 显示右列
        for obj in right_column:
            self.play(Write(obj))
            self.wait(0.5)
        
        self.wait(2)
        
        # 清除文字，重新显示图形
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        
        # 重新显示坐标系和椭圆
        self.axes = axes
        self.ellipse = ellipse
        self.point_A = point_A
        self.point_B = point_B
        self.point_P = point_P
        self.label_A = label_A
        self.label_B = label_B
        self.label_P = label_P
        
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
        
        # 左列 - 理论解释
        left_column = VGroup()
        
        explanation1 = Text("极点极线理论：", font_size=24)
        left_column.add(explanation1)
        
        explanation2 = Text("对于圆锥曲线，给定一点P，", font_size=20)
        explanation2.next_to(explanation1, DOWN, buff=0.2)
        left_column.add(explanation2)
        
        explanation3 = Text("存在一条直线l，使得过P的", font_size=20)
        explanation3.next_to(explanation2, DOWN, buff=0.1)
        left_column.add(explanation3)
        
        explanation4 = Text("任意弦MN的端点M、N处", font_size=20)
        explanation4.next_to(explanation3, DOWN, buff=0.1)
        left_column.add(explanation4)
        
        explanation5 = Text("的切线交于l上，这条", font_size=20)
        explanation5.next_to(explanation4, DOWN, buff=0.1)
        left_column.add(explanation5)
        
        explanation6 = Text("直线l称为P的极线。", font_size=20)
        explanation6.next_to(explanation5, DOWN, buff=0.1)
        left_column.add(explanation6)
        
        explanation7 = Text("对于椭圆，点P(x₀,y₀)", font_size=20)
        explanation7.next_to(explanation6, DOWN, buff=0.3)
        left_column.add(explanation7)
        
        explanation8 = Text("对应的极线方程为：", font_size=20)
        explanation8.next_to(explanation7, DOWN, buff=0.1)
        left_column.add(explanation8)
        
        polar_general = MathTex("\\frac{xx_0}{a^2} + \\frac{yy_0}{b^2} = 1", font_size=28)
        polar_general.next_to(explanation8, DOWN, buff=0.3)
        left_column.add(polar_general)
# 右列 - 具体计算
        right_column = VGroup()
        
        step1 = Text("对于本题：", font_size=24)
        right_column.add(step1)
        
        params = MathTex("a^2 = 3,\\quad b^2 = 4,\\quad P(1,-2)", font_size=28)
        params.next_to(step1, DOWN, buff=0.3)
        right_column.add(params)
        
        polar_eq = MathTex("\\frac{x \\cdot 1}{3} + \\frac{y \\cdot (-2)}{4} = 1", font_size=28)
        polar_eq.next_to(params, DOWN, buff=0.3)
        right_column.add(polar_eq)
        
        polar_simplified = MathTex("\\frac{x}{3} - \\frac{y}{2} = 1", font_size=28)
        polar_simplified.next_to(polar_eq, DOWN, buff=0.3)
        right_column.add(polar_simplified)
        
        polar_final = MathTex("2x - 3y = 6", font_size=28)
        polar_final.next_to(polar_simplified, DOWN, buff=0.3)
        right_column.add(polar_final)
        
        conclusion = Text("因此，直线MN恒过该极线", font_size=20)
        conclusion.next_to(polar_final, DOWN, buff=0.5)
        right_column.add(conclusion)
        
        conclusion2 = Text("与某定直线的交点。", font_size=20)
        conclusion2.next_to(conclusion, DOWN, buff=0.1)
        right_column.add(conclusion2)
        
        # 定位两列
        left_column.move_to(LEFT * 3.5)
        right_column.move_to(RIGHT * 3.5)
        
        # 显示左列
        for obj in left_column:
            self.play(Write(obj))
            self.wait(0.3)
        
        # 显示右列
        for obj in right_column:
            self.play(Write(obj))
            self.wait(0.3)
        
        self.wait(2)
# 清除文字，重新显示图形
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        
        # 重新显示坐标系和椭圆
        self.play(Create(self.axes))
        self.play(Create(self.ellipse))
        self.play(Create(self.point_A), Write(self.label_A))
        self.play(Create(self.point_B), Write(self.label_B))
        self.play(Create(self.point_P), Write(self.label_P))
        
        # 显示椭圆方程
        eq_text = MathTex("\\frac{x^2}{3} + \\frac{y^2}{4} = 1", font_size=36)
        eq_text.to_corner(UL)
        self.play(Write(eq_text))
        
        # 绘制极线
        def polar_line_func(x):
            return (2*x - 6) / 3  # 2x - 3y = 6 => y = (2x - 6)/3
        
        polar_line = self.axes.plot(
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
        
        # 左列 - 设直线方程和联立
        left_column = VGroup()
        
        step1 = Text("设过点P(1,-2)的", font_size=24)
        left_column.add(step1)
        
        step1_2 = Text("直线方程为：", font_size=24)
        step1_2.next_to(step1, DOWN, buff=0.1)
        left_column.add(step1_2)
        
        line_eq = MathTex("y + 2 = k(x - 1)", font_size=28)
        line_eq.next_to(step1_2, DOWN, buff=0.3)
        left_column.add(line_eq)
        
        line_eq2 = MathTex("y = kx - k - 2", font_size=28)
        line_eq2.next_to(line_eq, DOWN, buff=0.3)
        left_column.add(line_eq2)
        
        step2 = Text("与椭圆方程联立：", font_size=24)
        step2.next_to(line_eq2, DOWN, buff=0.5)
        left_column.add(step2)
        
        system_eq = MathTex("\\begin{cases} \\frac{x^2}{3} + \\frac{y^2}{4} = 1 \\\\ y = kx - k - 2 \\end{cases}", font_size=24)
        system_eq.next_to(step2, DOWN, buff=0.3)
        left_column.add(system_eq)
        
        step3 = Text("代入消元得：", font_size=24)
        step3.next_to(system_eq, DOWN, buff=0.5)
        left_column.add(step3)
        
        substituted = MathTex("\\frac{x^2}{3} + \\frac{(kx - k - 2)^2}{4} = 1", font_size=24)
        substituted.next_to(step3, DOWN, buff=0.3)
        left_column.add(substituted)
        
        # 右列 - 展开和韦达定理
        right_column = VGroup()
        
        expanded = MathTex("4x^2 + 3(k^2x^2 -", font_size=20)
        right_column.add(expanded)
        
        expanded2 = MathTex("2k(k+2)x + (k+2)^2) = 12", font_size=20)
        expanded2.next_to(expanded, DOWN, buff=0.1)
        right_column.add(expanded2)
        
        final_eq = MathTex("(3k^2+4)x^2 - 6k(k+2)x", font_size=20)
        final_eq.next_to(expanded2, DOWN, buff=0.3)
        right_column.add(final_eq)
        
        final_eq2 = MathTex("+ 3(k+2)^2 - 12 = 0", font_size=20)
        final_eq2.next_to(final_eq, DOWN, buff=0.1)
        right_column.add(final_eq2)
        
        step4 = Text("由韦达定理：", font_size=24)
        step4.next_to(final_eq2, DOWN, buff=0.5)
        right_column.add(step4)

        # 定位两列
        left_column.move_to(LEFT * 3)
        right_column.move_to(RIGHT * 3)
        
        # 显示左列
        for obj in left_column:
            self.play(Write(obj))
            self.wait(0.3)
        
        # 显示右列
        for obj in right_column:
            self.play(Write(obj))
            self.wait(0.3)
        
        self.wait(3)
