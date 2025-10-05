from manim import *

class EllipseProblem(Scene):
    def construct(self):
        # Part 1: Ellipse Equation
        title1 = Text("Part 1: Ellipse Equation", font_size=48)
        self.play(Write(title1))
        self.wait(2)
        self.play(FadeOut(title1))

        a_eq = MathTex("2a = 4", "\\Rightarrow", "a = 2")
        a_eq.shift(UP * 2)
        self.play(Write(a_eq))
        self.wait(2)

        point_eq = MathTex("\\frac{1^2}{2^2} + \\frac{(3/2)^2}{b^2} = 1")
        point_eq.shift(UP * 1)
        self.play(Write(point_eq))
        self.wait(2)

        simplify_eq = MathTex("\\frac{1}{4} + \\frac{9}{4b^2} = 1")
        simplify_eq.shift(UP * 0)
        self.play(Transform(point_eq, simplify_eq))
        self.wait(2)

        b_eq = MathTex("\\frac{9}{4b^2} = \\frac{3}{4}", "\\Rightarrow", "b^2 = 3")
        b_eq.shift(DOWN * 1)
        self.play(Write(b_eq))
        self.wait(2)

        final_eq = MathTex("\\frac{x^2}{4} + \\frac{y^2}{3} = 1")
        final_eq.shift(DOWN * 2)
        self.play(Write(final_eq))
        self.wait(3)

        self.clear()

        # Part 2: Fixed Point of MN
        title2 = Text("Part 2: Fixed Point of MN", font_size=48)
        self.play(Write(title2))
        self.wait(2)
        self.play(FadeOut(title2))

        # 此处可添加直线 l1, l2 的动画，展示中点 M, N 及直线 MN 过定点 (-4/7, 0)
        # 为简洁起见，省略详细动画代码

        fixed_point = MathTex("\\text{Fixed point: }", "\\left(-\\frac{4}{7}, 0\\right)")
        fixed_point.shift(UP)
        self.play(Write(fixed_point))
        self.wait(3)

        self.clear()

        # Part 3: Constant Sum λ + μ
        title3 = Text("Part 3: Constant Sum λ + μ", font_size=48)
        self.play(Write(title3))
        self.wait(2)
        self.play(FadeOut(title3))

        lambda_mu_eq = MathTex("\\lambda = 2 - y_0", ",\\quad", "\\mu = 2 + y_0")
        lambda_mu_eq.shift(UP)
        self.play(Write(lambda_mu_eq))
        self.wait(2)

        sum_eq = MathTex("\\lambda + \\mu = 4")
        sum_eq.shift(DOWN)
        self.play(Write(sum_eq))
        self.wait(3)
