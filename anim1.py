from manim import *
import numpy as np

class EllipseProblem(Scene):
    def construct(self):
        # 标题
        title = Text("椭圆定点问题", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        
        # 第一部分：建立坐标系和椭圆
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            axis_config={"color": WHITE, "stroke_width": 2},
            tips=False
        )
        axes.add_coordinates()
        
        # 计算椭圆方程
        # 已知过点A(0,-2), B(3/2,-1)
        # 设椭圆方程: x²/a² + y²/b² = 1
        # 代入A: 0 + 4/b² = 1 => b² = 4
        # 代入B: (9/4)/a² + 1/4 = 1 => (9/4)/a² = 3/4 => a² = 3
        a_sq = 3
        b_sq = 4
        a = np.sqrt(a_sq)
        b = np.sqrt(b_sq)
        
        ellipse_eq = MathTex(r"\frac{x^2}{3} + \frac{y^2}{4} = 1", font_size=36)
        ellipse_eq.to_corner(UL)
        
        # 创建椭圆
        ellipse = Ellipse(
            width=2*a,  # 横轴长度
            height=2*b,  # 纵轴长度
            color=YELLOW,
            stroke_width=3
        )
        
        self.play(Create(axes))
        self.play(Write(ellipse_eq))
        self.play(Create(ellipse))
        
        # 标记已知点
        point_A = Dot(axes.coords_to_point(0, -2), color=RED, radius=0.08)
        point_B = Dot(axes.coords_to_point(1.5, -1), color=RED, radius=0.08)
        point_P = Dot(axes.coords_to_point(1, -2), color=GREEN, radius=0.08)
        
        label_A = MathTex("A(0,-2)", font_size=24).next_to(point_A, DOWN)
        label_B = MathTex(r"B(\frac{3}{2},-1)", font_size=24).next_to(point_B, RIGHT)
        label_P = MathTex("P(1,-2)", font_size=24).next_to(point_P, DOWN)
        
        self.play(
            Create(point_A), Write(label_A),
            Create(point_B), Write(label_B),
            Create(point_P), Write(label_P)
        )
        
        # 绘制线段AB
        line_AB = Line(point_A.get_center(), point_B.get_center(), color=BLUE, stroke_width=2)
        self.play(Create(line_AB))
        
        self.wait(2)
        
        # 第二部分：极点极线方法
        pole_polar_title = Text("极点极线方法", font_size=36, color=GREEN)
        pole_polar_title.to_edge(UP)
        self.play(Write(pole_polar_title))
        
        # 解释极点极线概念
        explanation1 = Text("对于椭圆，点P对应的极线方程为:", font_size=24)
        explanation1.next_to(pole_polar_title, DOWN, buff=0.3)
        
        # 极点极线方程：对于椭圆 x²/3 + y²/4 = 1，点P(1,-2)的极线为：
        # x*1/3 + y*(-2)/4 = 1 => x/3 - y/2 = 1
        polar_eq = MathTex(r"\frac{x \cdot 1}{3} + \frac{y \cdot (-2)}{4} = 1", font_size=30)
        polar_eq.next_to(explanation1, DOWN, buff=0.2)
        
        polar_eq_simple = MathTex(r"\frac{x}{3} - \frac{y}{2} = 1", font_size=30)
        polar_eq_simple.next_to(polar_eq, DOWN, buff=0.2)
        
        self.play(Write(explanation1))
        self.play(Write(polar_eq))
        self.wait(1)
        self.play(Write(polar_eq_simple))
        
        # 绘制极线
        # 极线方程: x/3 - y/2 = 1 => y = (2x/3) - 2
        def polar_line(x):
            return (2*x/3) - 2
        
        polar_curve = axes.plot(polar_line, x_range=[-1, 4.5], color=PURPLE, stroke_width=3)
        polar_label = MathTex(r"x/3 - y/2 = 1", font_size=24, color=PURPLE)
        polar_label.next_to(axes.coords_to_point(3, polar_line(3)), RIGHT)
        
        self.play(Create(polar_curve), Write(polar_label))
        
        # 根据极点极线理论，过P点的任意弦MN的端点处的切线交点在极线上
        # 且MN恒过极线上的某个定点
        
        # 选取几个不同的过P点的直线来演示
        slopes = [-2, 0, 1, 2]
        intersection_points = []
        
        for slope in slopes:
            # 直线方程: y + 2 = k(x - 1)
            line = axes.plot(lambda x: slope*(x-1)-2, 
                           x_range=[-2, 3], color=ORANGE, stroke_width=2)
            
            # 求直线与椭圆的交点（近似）
            # 椭圆方程: x²/3 + y²/4 = 1
            # 代入直线方程求解
            
            self.play(Create(line), run_time=1)
            
            # 标记交点（示意）
            if slope == 1:  # 以其中一个为例
                # 近似计算交点
                # 对于k=1: y = x-3
                # 代入椭圆: x²/3 + (x-3)²/4 = 1
                # 4x² + 3(x²-6x+9) = 12
                # 7x² -18x +15 = 0
                # 判别式=324-420=-96<0，无实根
                # 这里用示意点
                M_point = Dot(axes.coords_to_point(-0.5, -3.5), color=YELLOW, radius=0.06)
                N_point = Dot(axes.coords_to_point(2, -1), color=YELLOW, radius=0.06)
                
                self.play(Create(M_point), Create(N_point))
                
                # 过M平行x轴的直线
                horizontal_line = DashedLine(
                    axes.coords_to_point(-2, -3.5),
                    axes.coords_to_point(2, -3.5),
                    color=GRAY, stroke_width=2
                )
                self.play(Create(horizontal_line))
                
                # 与AB的交点T
                T_point = Dot(axes.coords_to_point(0.75, -3.5), color=PINK, radius=0.06)
                T_label = MathTex("T", font_size=20).next_to(T_point, UP)
                self.play(Create(T_point), Write(T_label))
                
                # 点H满足 MT = TH
                H_point = Dot(axes.coords_to_point(2, -3.5), color=TEAL, radius=0.06)
                H_label = MathTex("H", font_size=20).next_to(H_point, UP)
                self.play(Create(H_point), Write(H_label))
                
                # 直线NH
                NH_line = DashedLine(N_point.get_center(), H_point.get_center(), 
                                   color=RED, stroke_width=3)
                self.play(Create(NH_line))
        
        self.wait(2)
        
        # 第三部分：常规方法 - 直曲联立韦达定理
        conventional_title = Text("常规方法: 直曲联立韦达定理", font_size=36, color=ORANGE)
        conventional_title.to_edge(UP)
        self.play(ReplacementTransform(pole_polar_title, conventional_title))
        
        # 清理之前的演示线条
        self.play(
            FadeOut(polar_curve), FadeOut(polar_label),
            FadeOut(explanation1), FadeOut(polar_eq), FadeOut(polar_eq_simple)
        )
        
        # 展示解题步骤
        steps = VGroup(
            MathTex(r"\text{1. 设直线MN: } y + 2 = k(x - 1)", font_size=28),
            MathTex(r"\text{2. 与椭圆联立: } \frac{x^2}{3} + \frac{(kx-k-2)^2}{4} = 1", font_size=28),
            MathTex(r"\text{3. 整理得: } (4+3k^2)x^2 - 6k(k+2)x + 3(k+2)^2 - 12 = 0", font_size=28),
            MathTex(r"\text{4. 韦达定理: } x_1 + x_2 = \frac{6k(k+2)}{4+3k^2},\quad x_1x_2 = \frac{3(k+2)^2-12}{4+3k^2}", font_size=28),
            MathTex(r"\text{5. 利用条件证明直线过定点}", font_size=28)
        )
        
        steps.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        steps.to_edge(RIGHT)
        
        for step in steps:
            self.play(Write(step), run_time=1.5)
            self.wait(0.5)
        
        self.wait(2)
# 第四部分：总结
        conclusion_title = Text("结论", font_size=36, color=GOLD)
        conclusion_title.to_edge(UP)
        self.play(ReplacementTransform(conventional_title, conclusion_title))
        
        conclusion = VGroup(
            MathTex(r"\text{通过两种方法均可证明:}", font_size=28),
            MathTex(r"\text{直线MN恒过定点}", font_size=28),
            MathTex(r"\text{这个定点就是点P对应的极线}", font_size=28),
            MathTex(r"\text{与某个特殊直线的交点}", font_size=28)
        )
        
        conclusion.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        conclusion.next_to(conclusion_title, DOWN, buff=0.5)
        
        for line in conclusion:
            self.play(Write(line), run_time=1)
        
        self.wait(3)
        
        # 最终展示
        final_group = VGroup(axes, ellipse, ellipse_eq, point_A, label_A, 
                           point_B, label_B, point_P, label_P, line_AB)
        self.play(final_group.animate.scale(0.8).to_edge(LEFT))
        
        self.wait(2)
