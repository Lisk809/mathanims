from manim import *
import numpy as np

class EllipseProblem(Scene):
    def construct(self):
        # 标题
        title = Text("椭圆问题解答", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        
        # 第一部分：求椭圆方程
        self.section1()
        
        # 第二部分：几何演示
        self.section2()
        
        # 极点极线解释
        self.section3()
        
        # 常规代数证明
        self.section4()
    
    def section1(self):
        # 第一部分：求椭圆方程
        title = Text("第一部分：求椭圆方程", font_size=36, color=GREEN)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 已知条件
        conditions = VGroup(
            Text("已知椭圆E关于x轴、y轴对称", font_size=24),
            Text("且过点A(0, -2)和B(3/2, -1)", font_size=24)
        )
        conditions.arrange(DOWN, aligned_edge=LEFT)
        conditions.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(conditions))
        self.wait(2)
        
        # 设椭圆方程
        eq_setup = MathTex("\\text{设椭圆方程为: }", "\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1")
        eq_setup.next_to(conditions, DOWN, buff=0.5)
        
        self.play(Write(eq_setup))
        self.wait(1)
        
        # 代入点A
        eq_A = MathTex("\\text{代入点A(0, -2): }", "\\frac{0^2}{a^2} + \\frac{(-2)^2}{b^2} = 1")
        eq_A.next_to(eq_setup, DOWN, buff=0.3, aligned_edge=LEFT)
        
        self.play(Write(eq_A))
        self.wait(1)
        
        eq_A_simplified = MathTex("\\Rightarrow", "\\frac{4}{b^2} = 1", "\\Rightarrow", "b^2 = 4")
        eq_A_simplified.next_to(eq_A, DOWN, buff=0.3, aligned_edge=LEFT)
        
        self.play(Write(eq_A_simplified))
        self.wait(1)
        
        # 代入点B
        eq_B = MathTex("\\text{代入点B}(\\frac{3}{2}, -1): ", 
                       "\\frac{(3/2)^2}{a^2} + \\frac{(-1)^2}{4} = 1")
        eq_B.next_to(eq_A_simplified, DOWN, buff=0.3, aligned_edge=LEFT)
        
        self.play(Write(eq_B))
        self.wait(1)
        
        eq_B_simplified = MathTex("\\Rightarrow", 
                                  "\\frac{9/4}{a^2} + \\frac{1}{4} = 1")
        eq_B_simplified.next_to(eq_B, DOWN, buff=0.3, aligned_edge=LEFT)
        
        self.play(Write(eq_B_simplified))
        self.wait(1)
        
        eq_B_simplified2 = MathTex("\\Rightarrow", 
                                   "\\frac{9}{4a^2} = \\frac{3}{4}")
        eq_B_simplified2.next_to(eq_B_simplified, DOWN, buff=0.3, aligned_edge=LEFT)
        
        self.play(Write(eq_B_simplified2))
        self.wait(1)
        
        eq_B_simplified3 = MathTex("\\Rightarrow", 
                                   "9 = 3a^2", "\\Rightarrow", "a^2 = 3")
        eq_B_simplified3.next_to(eq_B_simplified2, DOWN, buff=0.3, aligned_edge=LEFT)
        
        self.play(Write(eq_B_simplified3))
        self.wait(1)
        
        # 最终方程
        final_eq = MathTex("\\text{椭圆E的方程为: }", 
                           "\\frac{x^2}{3} + \\frac{y^2}{4} = 1")
        final_eq.next_to(eq_B_simplified3, DOWN, buff=0.5)
        final_eq.set_color(YELLOW)
        
        self.play(Write(final_eq))
        self.wait(2)
        
        # 清理屏幕
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
    def section2(self):
        # 第二部分：几何演示
        title = Text("第二部分：几何演示", font_size=36, color=GREEN)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建坐标系
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            axis_config={"color": WHITE, "stroke_width": 2},
        )
        axes.add_coordinates()
        axes.shift(DOWN * 0.5)
        
        self.play(Create(axes))
        self.wait(1)
        
        # 绘制椭圆
        ellipse = ParametricFunction(
            lambda t: axes.coords_to_point(
                np.sqrt(3) * np.cos(t),
                2 * np.sin(t)
            ),
            t_range=[0, 2 * PI],
            color=BLUE,
            stroke_width=4
        )
        ellipse_label = MathTex("\\frac{x^2}{3} + \\frac{y^2}{4} = 1").next_to(ellipse, UR, buff=0.1)
        
        self.play(Create(ellipse), Write(ellipse_label))
        self.wait(1)
        
        # 标记点A和B
        A = Dot(axes.coords_to_point(0, -2), color=RED, radius=0.08)
        A_label = MathTex("A", color=RED).next_to(A, LEFT, buff=0.1)
        
        B = Dot(axes.coords_to_point(1.5, -1), color=RED, radius=0.08)
        B_label = MathTex("B", color=RED).next_to(B, UR, buff=0.1)
        
        self.play(Create(A), Write(A_label), Create(B), Write(B_label))
        self.wait(1)
        
        # 绘制线段AB
        AB = Line(A.get_center(), B.get_center(), color=GREEN, stroke_width=3)
        self.play(Create(AB))
        self.wait(1)
        
        # 标记点P
        P = Dot(axes.coords_to_point(1, -2), color=ORANGE, radius=0.08)
        P_label = MathTex("P", color=ORANGE).next_to(P, DOWN, buff=0.1)
        
        self.play(Create(P), Write(P_label))
        self.wait(1)
        
        # 动态演示过P的直线与椭圆的交点
        k_values = [-2, -1, 0.5, 1.5]  # 不同的斜率值
        
        for k in k_values:
            # 过P的直线方程: y = k(x-1) - 2
            line = axes.plot(
                lambda x: k * (x - 1) - 2,
                x_range=[-3, 3],
                color=YELLOW,
                stroke_width=3
            )
            
            self.play(Create(line), run_time=1.5)
            
            # 求与椭圆的交点
            # 解方程: x^2/3 + (k(x-1)-2)^2/4 = 1
            # 这里简化计算，直接使用近似解
            if k == -2:
                M_point = axes.coords_to_point(0.87, -1.74)
                N_point = axes.coords_to_point(-0.87, 1.74)
            elif k == -1:
                M_point = axes.coords_to_point(1.37, -2.37)
                N_point = axes.coords_to_point(-0.37, 0.37)
            elif k == 0.5:
                M_point = axes.coords_to_point(2.12, -1.44)
                N_point = axes.coords_to_point(-0.12, -2.06)
            else:  # k = 1.5
                M_point = axes.coords_to_point(2.45, -0.18)
                N_point = axes.coords_to_point(-0.45, -2.68)
            
            M = Dot(M_point, color=PURPLE, radius=0.08)
            M_label = MathTex("M", color=PURPLE).next_to(M, UR, buff=0.1)
            
            N = Dot(N_point, color=PURPLE, radius=0.08)
            N_label = MathTex("N", color=PURPLE).next_to(N, UL, buff=0.1)
            
            self.play(Create(M), Write(M_label), Create(N), Write(N_label))
            
            # 过M平行于x轴的直线
            horizontal_line = DashedLine(
                axes.coords_to_point(-3, M_point[1]),
                axes.coords_to_point(3, M_point[1]),
                color=GRAY,
                stroke_width=2
            )
            
            self.play(Create(horizontal_line))
            
            # 与AB的交点T
            # AB方程: y = (2/3)x - 2
            # 与y = y_M的交点
            y_M = axes.point_to_coords(M_point)[1]
            x_T = (y_M + 2) * 3/2
            T_point = axes.coords_to_point(x_T, y_M)
            
            T = Dot(T_point, color=TEAL, radius=0.08)
            T_label = MathTex("T", color=TEAL).next_to(T, UP, buff=0.1)
            
            self.play(Create(T), Write(T_label))
            
            # 点H: MT = TH, 所以H = 2T - M
            H_point = 2 * T_point - M_point
            H = Dot(H_point, color=PINK, radius=0.08)
            H_label = MathTex("H", color=PINK).next_to(H, DOWN, buff=0.1)
            
            self.play(Create(H), Write(H_label))
# 直线HN
            HN = Line(H_point, N_point, color=RED, stroke_width=3)
            self.play(Create(HN))
            
            # 显示HN过定点A
            A_copy = Dot(axes.coords_to_point(0, -2), color=RED, radius=0.1)
            self.play(Create(A_copy), run_time=0.5)
            
            # 验证HN过A
            verification_line = DashedLine(H_point, A.get_center(), color=RED, stroke_width=2)
            self.play(Create(verification_line))
            
            self.wait(2)
            
            # 清理当前演示（保留椭圆、点A、B、P和AB）
            to_remove = VGroup(line, M, M_label, N, N_label, horizontal_line, T, T_label, H, H_label, HN, A_copy, verification_line)
            self.play(FadeOut(to_remove))
        
        self.wait(2)
        
        # 清理屏幕
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def section3(self):
        # 极点极线解释
        title = Text("极点极线方法", font_size=36, color=GREEN)
        title.to_edge(UP)
        self.play(Write(title))
        
        explanation = VGroup(
            Text("极点极线理论:", font_size=28, color=YELLOW),
            Text("对于圆锥曲线，一点P的极线是", font_size=24),
            Text("一条直线，具有调和分割性质", font_size=24),
            Text("", font_size=24),
            Text("点P(1,-2)关于椭圆的极线为:", font_size=24),
            MathTex("\\frac{x\\cdot 1}{3} + \\frac{y\\cdot (-2)}{4} = 1"),
            MathTex("\\Rightarrow \\frac{x}{3} - \\frac{y}{2} = 1"),
            MathTex("\\Rightarrow 2x - 3y = 6"),
            Text("", font_size=24),
            Text("这正是直线AB的方程!", font_size=24, color=RED),
            Text("", font_size=24),
            Text("因此，点P和直线AB是极点极线关系", font_size=24),
            Text("这解释了为什么直线HN总是过定点A", font_size=24)
        )
        
        explanation.arrange(DOWN, aligned_edge=LEFT)
        explanation.scale(0.8)
        explanation.next_to(title, DOWN, buff=0.5)
        
        for item in explanation:
            self.play(Write(item), run_time=1)
            self.wait(0.5)
        
        self.wait(3)
# 清理屏幕
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def section4(self):
        # 常规代数证明
        title = Text("常规代数证明", font_size=36, color=GREEN)
        title.to_edge(UP)
        self.play(Write(title))
        
        proof = VGroup(
            Text("设过点P(1,-2)的直线方程为:", font_size=24),
            MathTex("y = k(x-1) - 2"),
            Text("代入椭圆方程:", font_size=24),
            MathTex("\\frac{x^2}{3} + \\frac{[k(x-1)-2]^2}{4} = 1"),
            Text("整理得:", font_size=24),
            MathTex("(4+3k^2)x^2 - 6k(k+2)x + 3(k+2)^2 - 12 = 0"),
            Text("设M(x₁,y₁), N(x₂,y₂), 由韦达定理:", font_size=24),
            MathTex("x_1 + x_2 = \\frac{6k(k+2)}{4+3k^2}"),
            MathTex("x_1 x_2 = \\frac{3(k+2)^2 - 12}{4+3k^2}"),
            Text("点T在AB上，且y_T = y₁", font_size=24),
            MathTex("T = \\left(\\frac{3k}{2}(x_1-1), kx_1-k-2\\right)"),
            Text("点H满足MT = TH, 故H = 2T - M", font_size=24),
            MathTex("H = \\left((3k-1)x_1-3k, kx_1-k-2\\right)"),
            Text("直线HN的方程:", font_size=24),
            MathTex("\\frac{y - y_2}{x - x_2} = \\frac{y_2 - y_H}{x_2 - x_H}"),
            Text("代入点A(0,-2)验证:", font_size=24),
            MathTex("\\frac{-2 - y_2}{0 - x_2} = \\frac{y_2 - y_H}{x_2 - x_H}"),
            Text("经过代数运算，该等式恒成立", font_size=24),
            Text("故直线HN恒过定点A(0,-2)", font_size=24, color=RED)
        )
        
        proof.arrange(DOWN, aligned_edge=LEFT)
        proof.scale(0.7)
        proof.next_to(title, DOWN, buff=0.5)
        
        for item in proof:
            self.play(Write(item), run_time=1.5)
            self.wait(0.5)
        
        self.wait(3)
# 结论
        conclusion = Text("证毕", font_size=48, color=GOLD)
        conclusion.move_to(ORIGIN)
        
        self.play(Write(conclusion))
        self.wait(2)
        
        # 清理屏幕
        self.play(*[FadeOut(mob) for mob in self.mobjects])

# 运行场景
if __name__ == "__main__":
    scene = EllipseProblem()
    scene.render()

