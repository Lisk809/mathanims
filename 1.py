from manim import *
import numpy as np

class OptimizationJourney(Scene):
    def construct(self):
        # --- 0. 配置与常数定义 ---
        # 这种常数看着头疼，考试时第一步就是设 r = e/(e+1)
        # r ≈ 0.73
        e_val = np.exp(1)
        r_val = e_val / (e_val + 1)
        
        # 坐标系配置 (放大一点以便观察)
        axes = Axes(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[0, 3, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_numbers": False}
        ).shift(LEFT * 2)
        
        y_label = axes.get_y_axis_label("y")
        x_label = axes.get_x_axis_label("x")

        # --- 1. 思考过程：化简与识图 ---
        # 文本：原本的方程
        orig_eq = MathTex(r"x^2 + (\ln y)^2 = \left(\frac{e}{e+1}\right)^2")
        orig_eq.to_corner(UR)
        
        # 文本：思维转化
        think_bubble_1 = Text("太复杂了... 换元!", font_size=24, color=YELLOW).next_to(orig_eq, DOWN)
        simple_eq = MathTex(r"x^2 + (\ln y)^2 = r^2", color=BLUE).next_to(think_bubble_1, DOWN)
        
        self.play(Write(axes), Write(y_label), Write(x_label))
        self.play(Write(orig_eq))
        self.play(FadeIn(think_bubble_1))
        self.play(TransformFromCopy(orig_eq, simple_eq))
        self.wait()

        # 绘制曲线 Gamma
        # 这是一个关于 x 轴对称，关于 ln(y) 对称的图形
        graph = axes.plot_parametric_curve(
            lambda t: np.array([
                r_val * np.sin(t),
                np.exp(r_val * np.cos(t)),
                0
            ]),
            t_range=[0, TAU],
            color=BLUE
        )
        
        label_gamma = MathTex(r"\Gamma").next_to(graph, UP+RIGHT, buff=0)
        self.play(Create(graph), Write(label_gamma))
        
        # 标记最高点 P
        p_point = axes.coords_to_point(0, np.exp(r_val))
        dot_p = Dot(p_point, color=RED)
        label_p = MathTex("P").next_to(dot_p, UP)
        self.play(FadeIn(dot_p), Write(label_p))

        # --- 2. 求解第一问：面积函数构建 ---
        self.play(FadeOut(think_bubble_1), FadeOut(orig_eq))
        
        # 动态演示直线 l (斜率为0)
        u_tracker = ValueTracker(0) # u = ln(y), 范围 (-r, r)
        
        # 辅助函数：根据 u 计算几何元素
        def get_lines_and_area():
            u = u_tracker.get_value()
            y = np.exp(u)
            x = np.sqrt(r_val**2 - u**2)
            
            # 点 A, B
            pt_a = axes.coords_to_point(x, y)
            pt_b = axes.coords_to_point(-x, y)
            
            # 三角形
            tri = Polygon(p_point, pt_a, pt_b, color=YELLOW, fill_opacity=0.3, stroke_width=2)
            
            # 直线 l
            line_l = Line(axes.coords_to_point(-2, y), axes.coords_to_point(2, y), color=GRAY, stroke_opacity=0.5)
            
            return VGroup(tri, line_l)

        dynamic_obj = always_redraw(get_lines_and_area)
        self.add(dynamic_obj)

        # 侧边栏：显示推导过程
        deriv_step1 = MathTex(r"S(u) = \frac{1}{2} \cdot 2x \cdot (y_P - y)").scale(0.7).to_corner(UR).shift(DOWN*1.5)
        deriv_step2 = MathTex(r"S(u) = \sqrt{r^2-u^2}(e^r - e^u)").scale(0.7).next_to(deriv_step1, DOWN)
        deriv_step3 = MathTex(r"S'(u) = 0 \Rightarrow u = -\frac{1}{e+1}").scale(0.7).next_to(deriv_step2, DOWN)
        
        self.play(Write(deriv_step1))
        self.wait(1)
        self.play(Write(deriv_step2))
        
        # 动画：上下滑动寻找最大值
        self.play(u_tracker.animate.set_value(r_val - 0.05), run_time=1.5) # 向上变窄
        self.play(u_tracker.animate.set_value(-r_val + 0.05), run_time=1.5) # 向下变矮
        
        # 文本提示：矛盾
        hint_text = Text("底边长 vs 高度 的博弈", font_size=20, color=ORANGE).next_to(graph, LEFT)
        self.play(FadeIn(hint_text))
        
        # 定位到最优解
        optimal_u = -1 / (e_val + 1)
        self.play(u_tracker.animate.set_value(optimal_u), run_time=2)
        self.play(Indicate(dynamic_obj[0]), Write(deriv_step3)) # 高亮三角形
        self.wait()

        # --- 3. 求解第二问：为什么斜率必须为0？(几何直观) ---
        # 清理屏幕
        self.play(
            FadeOut(deriv_step1), FadeOut(deriv_step2), FadeOut(deriv_step3), 
            FadeOut(hint_text), FadeOut(dynamic_obj)
        )
        
        think_bubble_2 = Text("如果直线倾斜会怎样？", font_size=24, color=YELLOW).to_corner(UR).shift(DOWN)
        self.play(FadeIn(think_bubble_2))

        # 演示切线原理 (Parallel Tangent Theorem)
        # 只有当切线平行于底边时，距离最远
        
        # 画出 P 点的切线 (水平的)
        tangent_line = DashedLine(
            axes.coords_to_point(-2, np.exp(r_val)),
            axes.coords_to_point(2, np.exp(r_val)),
            color=RED
        )
        tangent_label = Text("P处切线水平", font_size=18, color=RED).next_to(tangent_line, UP)
        self.play(Create(tangent_line), Write(tangent_label))

        # 演示一个倾斜的三角形
        # 固定一个稍微倾斜的直线，截取 A', B'
        slope = 0.5
        intercept = 0.8
        
        # 这是一个示意性的倾斜三角形，为了视觉直观，不一定要严格解方程
        # 我们用简单的几何变换来展示"底边没变长多少，但高变短了"的直觉
        
        line_tilted = Line(axes.coords_to_point(-1, -0.5 + intercept), axes.coords_to_point(1, 0.5 + intercept), color=GREY)
        tri_tilted = Polygon(
            p_point, 
            axes.coords_to_point(-0.8, -0.4 + intercept), 
            axes.coords_to_point(0.8, 0.4 + intercept),
            color=ORANGE, fill_opacity=0.3
        )
        
        self.play(Create(line_tilted), FadeIn(tri_tilted))
        
        logic_text = Tex(r"Max Area $\iff$ Tangent $\parallel$ Base", color=GREEN).scale(0.8).next_to(think_bubble_2, DOWN)
        logic_text2 = Tex(r"Tangent at P is horizontal $\Rightarrow$ Base is horizontal", color=GREEN).scale(0.8).next_to(logic_text, DOWN)
        
        self.play(Write(logic_text))
        self.wait(1)
        self.play(Write(logic_text2))
        
        # 动画：将倾斜三角形“扶正”
        self.play(
            Transform(tri_tilted, dynamic_obj[0]), # 变回之前的最佳水平三角形
            FadeOut(line_tilted)
        )
        self.play(Indicate(tri_tilted, color=GOLD))
        
        final_res = MathTex(r"S_{max} = (e-1)\sqrt{\frac{e-1}{e+1}} e^{-\frac{1}{e+1}}", color=GOLD)
        final_res.scale(0.8).to_edge(DOWN)
        self.play(Write(final_res))
        
        self.wait(3)
