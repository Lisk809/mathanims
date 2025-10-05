from manim import *
from patch.auto_chinese_patch import *

class EllipseProblem(Scene):
    def construct(self):
        # Part 1: Ellipse Equation
        question0 = Tex(r"已知椭圆 $ C: \frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 (a, b > 0) $，长轴长为4，且过点 $ (1, \frac{3}{2}) $。")
        question0.shift(UP * 1.25)

        question1 = Tex(r"（1）求椭圆 $ C $ 的方程；")
        question0.shift(UP * 0)

        question2 = Tex(r"（2）过点 $ P(-1, 0) $ 作两条互相垂直的直线 $ l_1, l_2 $，直线 $ l_1 $ 交椭圆 $ C $ 于 $ A, B $ 两点，直线 $ l_2 $ 交椭圆 $ C $ 于 $ C, D $ 两点，线段 $ AB, CD $ 的中点分别为 $ M, N $，证明：直线 $ MN $ 过定点；")
        question0.shift(DOWN * 1.25)

        question3 = Tex(r"（3）若点 $ E $ 在椭圆 $ C $ 上的运动，$ F(0, 1), Q(0, -1) $，直线 $ EF, EQ $ 分别交椭圆 $ C $ 于点 $ H, K $，且满足 $\frac{FH}{EH} = \frac{1}{1 + \lambda}, \quad \frac{QK}{EK} = \frac{1}{1 + \mu},$ 证明：$\lambda + \mu$ 为定值。")
        question0.shift(DOWN * 2.5)
        self.play(Write(question0))
        self.play(Write(question1))
        self.play(Write(question2))
        self.play(Write(question3))
        self.clear()
        
        
        title1 = Text("第一问  求方程", font_size=48)
        self.play(Write(title1))
        self.wait(2)
        self.play(FadeOut(title1))

        a_eq = Tex(r"长轴长为 4，即 $ 2a = 4 $，所以  $a = 2 $")
        self.play(Write(a_eq))
        self.wait(2)
        self.play(FadeOut(a_eq))

        point_eq = Tex(r"椭圆过点 $ (1, \frac{3}{2}) $，代入方程：")
        point_eq.shift(UP * 1.5)
        self.play(Write(point_eq))
        self.wait(2)

        simplify_eq = MathTex("\\frac{1}{4} + \\frac{9}{4b^2} = 1")
        simplify_eq.shift(UP * 0)
        self.play(Transform(point_eq, simplify_eq))
        self.wait(2)

        b_eq = MathTex("\\frac{9}{4b^2} = \\frac{3}{4} \\Rightarrow b^2 = 3")
        b_eq.shift(DOWN * 1.5)
        self.play(Write(b_eq))
        self.wait(2)

        final_eq = MathTex(r"\frac{x^2}{4} + \frac{y^2}{3} = 1")
        final_eq.shift(DOWN * 3)
        self.play(Write(final_eq))
        self.wait(3)

        self.clear()

        # Part 2: Fixed Point of MN
        title2 = Text("第二问 求MN所过定点", font_size=48)
        self.play(Write(title2))
        self.wait(2)
        self.play(FadeOut(title2))

        # 此处可添加直线 l1, l2 的动画，展示中点 M, N 及直线 MN 过定点 (-4/7, 0)
        # 创建坐标系
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2.5, 2.5, 1],
            x_length=7,
            y_length=5,
            axis_config={"color": WHITE, "stroke_width": 2},
            tips=False
        )
        axes.add_coordinates()
        # axes.shift(DOWN * 0.5)
        
        self.play(Create(axes))
        self.wait(1)
        
        # 绘制椭圆 x²/4 + y²/3 = 1
        ellipse = axes.plot_implicit_curve(
            lambda x, y: x**2/4 + y**2/3 - 1,
            color=YELLOW,
            stroke_width=4
        )
        ellipse_label = MathTex(r"\frac{x^2}{4} + \frac{y^2}{3} = 1", color=YELLOW)
        ellipse_label.next_to(ellipse, RIGHT, buff=0.5)
        
        self.play(Create(ellipse), Write(ellipse_label))
        self.wait(1)
        
        # 标记点 P(-1, 0)
        P = axes.coords_to_point(-1, 0)
        P_dot = Dot(P, color=RED, radius=0.08)
        P_label = MathTex("P(-1,0)", color=RED)
        P_label.next_to(P_dot, DOWN, buff=0.1)
        
        self.play(Create(P_dot), Write(P_label))
        self.wait(1)
        
        # 标记定点 (-4/7, 0)
        fixed_point = axes.coords_to_point(-4/7, 0)
        fixed_dot = Dot(fixed_point, color=GREEN, radius=0.08)
        fixed_label = MathTex(r"\left(-\frac{4}{7}, 0\right)", color=GREEN)
        fixed_label.next_to(fixed_dot, UP, buff=0.1)
        
        self.play(Create(fixed_dot), Write(fixed_label))
        self.wait(1)
        
        # 创建斜率值跟踪器
        k_tracker = ValueTracker(-2.0)  # 初始斜率
        
        # 创建直线 l1 和 l2 的函数
        def get_l1():
            k = k_tracker.get_value()
            return axes.plot(
                lambda x: k * (x + 1),
                x_range=[-3, 3],
                color=BLUE,
                stroke_width=2
            )
        
        def get_l2():
            k = k_tracker.get_value()
            if abs(k) < 0.01:  # 避免除以零
                return axes.plot(
                    lambda x: 1000,  # 近似垂直线
                    x_range=[-3, 3],
                    color=PURPLE,
                    stroke_width=2
                )
            return axes.plot(
                lambda x: -1/k * (x + 1),
                x_range=[-3, 3],
                color=PURPLE,
                stroke_width=2
            )
        
        # 创建直线 l1 和 l2
        l1 = always_redraw(get_l1)
        l2 = always_redraw(get_l2)
        
        # 添加斜率标签
        k_label = always_redraw(
            lambda: MathTex(f"k = {k_tracker.get_value():.2f}", color=BLUE)
            .to_edge(UR)
        )
        
        self.play(Create(l1), Create(l2), Write(k_label))
        self.wait(1)
        
        # 计算中点 M 和 N 的函数
        def get_M():
            k = k_tracker.get_value()
            if abs(k) < 0.01:  # 特殊情况处理
                return axes.coords_to_point(-1, 0)
            
            x_M = -4*k**2/(3+4*k**2)
            y_M = 3*k/(3+4*k**2)
            return axes.coords_to_point(x_M, y_M)
        
        def get_N():
            k = k_tracker.get_value()
            if abs(k) < 0.01:  # 特殊情况处理
                return axes.coords_to_point(-1, 0)
            
            x_N = -4/(3*k**2+4)
            y_N = -3*k/(3*k**2+4)
            return axes.coords_to_point(x_N, y_N)
        
        # 创建中点 M 和 N
        M_dot = always_redraw(
            lambda: Dot(get_M(), color=ORANGE, radius=0.06)
        )
        N_dot = always_redraw(
            lambda: Dot(get_N(), color=PINK, radius=0.06)
        )
        
        M_label = always_redraw(
            lambda: Text("M", color=ORANGE, font_size=24)
            .next_to(M_dot, UP, buff=0.05)
        )
        N_label = always_redraw(
            lambda: Text("N", color=PINK, font_size=24)
            .next_to(N_dot, DOWN, buff=0.05)
        )
        
        self.play(Create(M_dot), Create(N_dot), Write(M_label), Write(N_label))
        self.wait(1)
        
        # 创建直线 MN
        def get_MN():
            M_point = get_M()
            N_point = get_N()
            
            # 计算直线方程 y = mx + b
            if abs(M_point[0] - N_point[0]) < 0.001:  # 垂直线
                return axes.plot(
                    lambda x: 1000,  # 近似垂直线
                    x_range=[-3, 3],
                    color=RED,
                    stroke_width=3
                )
            
            m = (M_point[1] - N_point[1]) / (M_point[0] - N_point[0])
            b = M_point[1] - m * M_point[0]
            
            return axes.plot(
                lambda x: m * x + b,
                x_range=[-3, 3],
                color=RED,
                stroke_width=3
            )
        
        MN_line = always_redraw(get_MN)
        
        self.play(Create(MN_line))
        self.wait(1)
        
        k_values = [-1.5, -0.5, 0.5, 1.5, 2.5, -2.5]
        
        for k_val in k_values:
            self.play(
                k_tracker.animate.set_value(k_val),
                run_time=2
            )
            self.wait(1)
        self.wait(3)
        self.clear()
        # 为简洁起见，省略详细动画代码
        text20 = Tex("过点 $ P(-1, 0) $ 作两条互相垂直的直线  $l_1, l_2$ ，设 $ l_1 $ 的斜率为 $ k $，则方程为：")
        text20.shift(UP * 1)
        text21 = MathTex("y = k(x + 1)")
        text22 = Text("代入椭圆方程：")
        text22.shift(UP * 1)
        text23 = MathTex(r"\frac{x^2}{4} + \frac{[k(x+1)]^2}{3} = 1")
        text24 = Text("整理得：")
        text24.shift(UP * 1)
        text25 = MathTex("(3 + 4k^2)x^2 + 8k^2 x + (4k^2 - 12) = 0")
        
        self.play(Write(text20))
        self.play(Write(text21))
        self.wait(3)
        self.clear()
        
        self.play(Write(text22))
        self.play(Write(text23))
        self.wait(3)
        self.clear()
        
        self.play(Write(text24))
        self.play(Write(text25))
        self.wait(3)
        self.clear()
        
        text26 = Tex("设  $C(x_3, y_3), D(x_4, y_4)$ ，则中点  N  的坐标为：")
        text26.shift(UP * 1)
        text27 = MathTex(r"x_N = \frac{x_3 + x_4}{2} = -\frac{4}{3k^2 + 4}, \quad y_N = -\frac{1}{k}(x_N + 1) = -\frac{3k}{3k^2 + 4}")
        text28 = Text("即：")
        text28.shift(UP * 1)
        text29 = MathTex(r"N\left( -\frac{4}{3k^2 + 4}, -\frac{3k}{3k^2 + 4} \right)")
        self.play(Write(text26))
        self.play(Write(text27))
        self.wait(3)
        self.clear()
        self.play(Write(text28))
        self.play(Write(text29))
        self.wait(3)
        self.clear()
        text210 = Tex("设直线  MN  的斜率为 $ k_{MN} $，计算得：")
        text210.shift(UP * 1)
        text211 = Tex(r"k_{MN} = \frac{-7k}{4(k^2 - 1)}")
        self.play(Write(text210))
        self.play(Write(text211))
        self.wait(3)
        self.clear()
        text212 = Tex("取点  M  写直线方程：")
        text212.shift(UP)
        text213 = MathTex(r"y - \frac{3k}{3 + 4k^2} = \frac{-7k}{4(k^2 - 1)} \left( x + \frac{4k^2}{3 + 4k^2} \right)")
        self.play(Write(text212))
        self.play(Write(text213))
        self.wait(3)
        self.clear()
        text214 = Tex("令 $ y = 0 $，解得 $ x = -\frac{4}{7} $，与  k  无关。")
        text215 = Text("因此，直线  MN  恒过定点：")
        text216 = MathTex(r"\boxed{\left( -\frac{4}{7},\ 0 \right)}")
        self.play(Write(text214))
        self.play(Write(text215))
        self.play(Write(text216))
        self.wait(5)
        self.clear()
        
        # Part 3: Constant Sum λ + μ
        title3 = Text("第三问 求 λ + μ", font_size=48)
        self.play(Write(title3))
        self.wait(2)
        self.play(FadeOut(title3))

        text311 = Tex("设点 $ E(x_0, y_0) $ 在椭圆上，满足：")
        text311.shift(UP)
        text312 = Tex(r"\frac{x_0^2}{4} + \frac{y_0^2}{3} = 1 \implies 3x_0^2 + 4y_0^2 = 12")

        text313 = Tex("过  E(x_0, y_0) 、 F(0, 1)  的直线参数方程为：")
        text313.shift(UP)
        text314 = MathTex(r"x = x_0(1 - t), \quad y = y_0 + t(1 - y_0)")

        text315 = Tex("代入椭圆方程，整理得关于  $t$  的二次方程。已知  $t = 0 $ 对应点 $ E $，另一解 $ t_H $ 对应点 $ H $，计算得：")
        text315.shift(UP)
        text316 = MathTex(r"t_H = \frac{3 - y_0}{2 - y_0}")

        text317 = Text("由比例关系：")
        text315.shift(UP)
        text318 = MathTex(r"\frac{FH}{EH} = \frac{1}{1 + \lambda} \implies \lambda = 2 - y_0")
        
        self.play(Write(text311))
        self.play(Write(text312))
        self.wait(3)
        self.clear()
        self.play(Write(text313))
        self.play(Write(text314))
        self.wait(3)
        self.clear()
        self.play(Write(text315))
        self.play(Write(text316))
        self.wait(3)
        self.clear()
        self.play(Write(text317))
        self.play(Write(text318))
        self.wait(3)
        self.clear()
        
        text321 = Tex("过 $ E(x_0, y_0) $、 $Q(0, -1) $ 的直线参数方程为：")
        text321.shift(UP)
        text322 = MathTex(r"x = x_0(1 - t), \quad y = y_0 - t(1 + y_0)")

        text323 = Tex("代入椭圆方程，得另一解 $ t_K $ 对应点  K ：")

        text324 = MathTex(r"t_K = \frac{3 + y_0}{2 + y_0}")

        text325 = Text("由比例关系：")

        text326 = MathTex(r"\frac{QK}{EK} = \frac{1}{1 + \mu} \implies \mu = 2 + y_0")

        text327 = Text("因此：")

        text328 = MathTex(r"\lambda + \mu = (2 - y_0) + (2 + y_0) = \boxed{4}")
        
        self.play(Write(text321))
        self.play(Write(text322))
        self.wait(3)
        self.clear()
        self.play(Write(text323))
        self.play(Write(text324))
        self.wait(3)
        self.clear()
        self.play(Write(text325))
        self.play(Write(text326))
        self.wait(3)
        self.clear()
        self.play(Write(text327))
        self.play(Write(text328))
        self.wait(5)
        self.clear()

        like = Text("点个赞呗( ๑ŏ ﹏ ŏ๑ ) ", font_size=48,t2c={'[0:3]': BLUE, '[4:-1]': RED})
        self.play(Write(like))
        expr = Text("•﹏•", font_size=48)
        self.play(Transform(like, expr))
        self.wait(3)
        