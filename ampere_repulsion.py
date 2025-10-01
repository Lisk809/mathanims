from manim import *
import numpy as np

class AmpereForce(Scene):
    def construct(self):
        # 标题
        title = Text("安培力：条形磁铁与通电线圈", font_size=36, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建坐标系
        axes = Axes(
            x_range=[-8, 8, 1],
            y_range=[-5, 5, 1],
            x_length=16,
            y_length=10,
            axis_config={"color": WHITE, "stroke_width": 1},
            tips=False
        )
        axes.shift(DOWN * 0.5)
        
        # 创建条形磁铁
        magnet_height = 3.0
        magnet_width = 1.0
        magnet = Rectangle(
            height=magnet_height,
            width=magnet_width,
            fill_color=RED,
            fill_opacity=0.8,
            stroke_color=WHITE,
            stroke_width=2
        )
        magnet.move_to(LEFT * 5)
        
        # 磁极标签
        n_label = Text("N", font_size=24, color=WHITE).next_to(magnet, UP, buff=0.2)
        s_label = Text("S", font_size=24, color=WHITE).next_to(magnet, DOWN, buff=0.2)
        
        # 创建通电线圈
        coil_radius = 1.2
        coil = Circle(radius=coil_radius, color=YELLOW, stroke_width=4)
        coil.move_to(RIGHT * 3)
        
        # 电流方向指示
        self.current_dots = VGroup()
        self.current_arrows = VGroup()
        for angle in np.linspace(0, 2*PI, 12, endpoint=False):
            dot = Dot(radius=0.05, color=YELLOW)
            dot.move_to(coil.point_at_angle(angle))
            
            # 使用向量来计算方向
            start_point = coil.point_at_angle(angle + 0.1)
            end_point = coil.point_at_angle(angle - 0.1)
            direction = end_point - start_point
            direction = direction / np.linalg.norm(direction) * 0.3
            
            arrow = Arrow(
                start=start_point,
                end=start_point + direction,
                color=YELLOW,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.3
            )
            
            self.current_dots.add(dot)
            self.current_arrows.add(arrow)
        
        self.play(
            Create(magnet),
            Write(n_label),
            Write(s_label),
            Create(coil),
            Create(self.current_dots),
            Create(self.current_arrows)
        )
        self.wait(2)
        
        # 显示电流方向文字
        current_text = Text("电流方向: 逆时针", font_size=20, color=YELLOW)
        current_text.next_to(coil, DOWN, buff=0.5)
        self.play(Write(current_text))
        self.wait(1)
        
        # 第一部分：绘制磁感线
        section1 = Text("1. 磁铁的磁场分布", font_size=28, color=GREEN)
        section1.next_to(title, DOWN, buff=0.5)
        self.play(Write(section1))
        self.wait(1)
        
        # 绘制磁感线
        field_lines = self.create_magnetic_field_lines(magnet, coil)
        self.play(LaggedStartMap(Create, field_lines, lag_ratio=0.1), run_time=3)
        self.wait(2)
        
        # 第二部分：微分分析
        self.play(FadeOut(section1))
        section2 = Text("2. 微分分析：单条磁感线的作用", font_size=28, color=GREEN)
        section2.next_to(title, DOWN, buff=0.5)
        self.play(Write(section2))
        self.wait(1)
        
        # 放大显示一条磁感线
        self.show_single_field_line_analysis(magnet, coil, field_lines[5])
        self.wait(2)
        
        # 第三部分：合力计算
        self.play(FadeOut(section2))
        section3 = Text("3. 合力计算：所有微分力的矢量和", font_size=28, color=GREEN)
        section3.next_to(title, DOWN, buff=0.5)
        self.play(Write(section3))
        self.wait(1)
        
        # 显示合力效果
        self.show_net_force_effect(magnet, coil, field_lines)
        self.wait(2)
        
        # 结论
        conclusion = Text("结论：线圈受到向左的安培斥力", font_size=24, color=RED)
        conclusion.next_to(section3, DOWN, buff=0.5)
        self.play(Write(conclusion))
        self.wait(3)
    
    def create_magnetic_field_lines(self, magnet, coil):
        """创建磁感线"""
        lines = VGroup()
        
        # N极发出的磁感线
        n_center = magnet.get_center() + UP * magnet.height/2
        s_center = magnet.get_center() + DOWN * magnet.height/2
        
        # 创建多条磁感线
        for i, angle in enumerate(np.linspace(-PI/2, PI/2, 8)):
            # 从N极出发的曲线
            start_point = n_center + RIGHT * 0.5 * np.sin(angle)
            
            # 控制点使曲线更自然
            control1 = start_point + RIGHT * 2 + UP * 0.5
            control2 = start_point + RIGHT * 4 + DOWN * 0.5 * np.sin(angle)
            end_point = s_center + RIGHT * 6 * (0.5 + 0.5 * np.sin(angle))
            
            line = CubicBezier(
                start_point, control1, control2, end_point,
                color=BLUE,
                stroke_width=2,
                stroke_opacity=0.7
            )
            
            # 添加箭头表示方向 - 使用手动计算的方向
            arrow_tip = Triangle(fill_color=BLUE, fill_opacity=0.7, stroke_width=0)
            arrow_tip.scale(0.1)
            arrow_tip.rotate(PI/2)
            
            # 在磁感线上放置多个箭头
            for t in np.linspace(0.2, 0.8, 3):
                point = line.point_from_proportion(t)
                
                # 手动计算方向向量（导数近似）
                t1 = max(0, t - 0.01)
                t2 = min(1, t + 0.01)
                p1 = line.point_from_proportion(t1)
                p2 = line.point_from_proportion(t2)
                direction = p2 - p1
                
                if np.linalg.norm(direction) > 0:
                    angle_rad = np.arctan2(direction[1], direction[0])
                    
                    arrow = arrow_tip.copy()
                    arrow.move_to(point)
                    arrow.rotate(angle_rad - PI/2)
                    
                    line.add(arrow)
            
            lines.add(line)
        
        return lines
    
    def show_single_field_line_analysis(self, magnet, coil, field_line):
        """显示单条磁感线的分析"""
        
        # 创建放大框
        zoom_rect = Rectangle(height=4, width=6, color=YELLOW, stroke_width=3)
        zoom_rect.move_to(RIGHT * 2 + UP * 1)
        
        # 复制并放大磁感线片段
        line_segment = field_line.copy()
        line_segment.set_color(RED)
        line_segment.set_stroke_width(4)
        
        # 创建微分段
        differential_text = Text("微分段 dl", font_size=18, color=WHITE)
        differential_text.next_to(zoom_rect, UP, buff=0.2)
        
        self.play(Create(zoom_rect), Write(differential_text))
        self.play(line_segment.animate.scale(1.5).move_to(zoom_rect.get_center()))
        self.wait(1)
        
        # 显示磁场方向
        b_vector = Arrow(
            start=line_segment.point_from_proportion(0.5),
            end=line_segment.point_from_proportion(0.5) + UP * 0.8,
            color=BLUE,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.3
        )
        b_label = Text("B", font_size=18, color=BLUE).next_to(b_vector.get_end(), UP, buff=0.1)
        
        self.play(GrowArrow(b_vector), Write(b_label))
        self.wait(1)
        
        # 显示电流方向
        i_vector = Arrow(
            start=line_segment.point_from_proportion(0.5),
            end=line_segment.point_from_proportion(0.5) + OUT * 0.8,
            color=YELLOW,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.3
        )
        i_label = Text("I", font_size=18, color=YELLOW).next_to(i_vector.get_end(), RIGHT, buff=0.1)
        
        self.play(GrowArrow(i_vector), Write(i_label))
        self.wait(1)
        
        # 显示安培力方向
        force_vector = Arrow(
            start=line_segment.point_from_proportion(0.5),
            end=line_segment.point_from_proportion(0.5) + LEFT * 1.0,
            color=RED,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.3
        )
        force_label = Text("dF", font_size=18, color=RED).next_to(force_vector.get_end(), LEFT, buff=0.1)
        
        force_eq = MathTex("d\\vec{F} = I \\, d\\vec{l} \\times \\vec{B}", font_size=20, color=WHITE)
        force_eq.next_to(zoom_rect, DOWN, buff=0.2)
        
        self.play(GrowArrow(force_vector), Write(force_label), Write(force_eq))
        self.wait(2)
        
        # 清理放大视图
        self.play(
            FadeOut(zoom_rect),
            FadeOut(differential_text),
            FadeOut(line_segment),
            FadeOut(b_vector),
            FadeOut(b_label),
            FadeOut(i_vector),
            FadeOut(i_label),
            FadeOut(force_vector),
            FadeOut(force_label),
            FadeOut(force_eq)
        )
    
    def show_net_force_effect(self, magnet, coil, field_lines):
        """显示合力效果"""
        
        # 在多个位置显示力向量
        force_vectors = VGroup()
        for angle in np.linspace(0, 2*PI, 8, endpoint=False):
            point = coil.point_at_angle(angle)
            force_vec = Arrow(
                start=point,
                end=point + LEFT * 0.8,
                color=RED,
                stroke_width=4,
                max_tip_length_to_length_ratio=0.3
            )
            force_vectors.add(force_vec)
        
        self.play(LaggedStartMap(GrowArrow, force_vectors, lag_ratio=0.1))
        self.wait(1)
        
        # 显示合力向量
        net_force = Arrow(
            start=coil.get_center(),
            end=coil.get_center() + LEFT * 2.5,
            color=RED,
            stroke_width=8,
            max_tip_length_to_length_ratio=0.2
        )
        net_force_label = Text("F_net", font_size=24, color=RED).next_to(net_force.get_end(), DOWN, buff=0.2)
        
        net_force_eq = MathTex("\\vec{F}_{net} = \\oint I \\, d\\vec{l} \\times \\vec{B}", font_size=24, color=WHITE)
        net_force_eq.next_to(coil, DOWN, buff=1.0)
        
        self.play(GrowArrow(net_force), Write(net_force_label), Write(net_force_eq))
        self.wait(2)
        
        # 显示排斥效果
        # 线圈向左移动，磁铁向右移动（排斥）
        self.play(
            coil.animate.shift(LEFT * 1.5),
            self.current_arrows.animate.shift(LEFT * 1.5),
            force_vectors.animate.shift(LEFT * 1.5),
            net_force.animate.shift(LEFT * 1.5),
            net_force_label.animate.shift(LEFT * 1.5),
            magnet.animate.shift(RIGHT * 0.3),
            n_label.animate.shift(RIGHT * 0.3),
            s_label.animate.shift(RIGHT * 0.3),
            run_time=2,
            rate_func=rate_functions.ease_out_sine
        )
        self.wait(1)