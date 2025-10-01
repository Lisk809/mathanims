from manim import *
import numpy as np

class AmpereForce(ThreeDScene):
    def construct(self):
        # 设置3D视角
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        
        # 标题
        title = Text("安培力：条形磁铁与通电线圈", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 创建条形磁铁
        magnet = VGroup(
            Prism(dimensions=[1, 0.3, 0.3], fill_color=RED, stroke_color=RED_E, fill_opacity=0.8),  # N极
            Prism(dimensions=[1, 0.3, 0.3], fill_color=BLUE, stroke_color=BLUE_E, fill_opacity=0.8)  # S极
        ).arrange(RIGHT, buff=0)
        
        # 标记磁极
        n_label = Text("N", font_size=24, color=WHITE).next_to(magnet[0], UP, buff=0.1)
        s_label = Text("S", font_size=24, color=WHITE).next_to(magnet[1], UP, buff=0.1)
        
        magnet_group = VGroup(magnet, n_label, s_label)
        magnet_group.move_to(ORIGIN)
        
        # 创建通电线圈
        coil = self.create_coil(radius=0.8, turns=3, height=0.2)
        coil.move_to(ORIGIN + 2*RIGHT + 0.5*UP)
        coil.set_color(YELLOW)
        
        # 电流方向指示
        current_arrow = Arrow(
            start=coil.get_center() + 0.5*LEFT,
            end=coil.get_center() + 0.5*RIGHT,
            color=GREEN,
            buff=0.1,
            stroke_width=5
        )
        current_label = Text("I", font_size=20, color=GREEN).next_to(current_arrow, UP, buff=0.1)
        # 显示磁铁和线圈
        self.play(Create(magnet), Write(n_label), Write(s_label))
        self.play(Create(coil), GrowArrow(current_arrow), Write(current_label))
        self.wait(2)
        
        # 绘制磁感线
        magnetic_field_lines = self.create_magnetic_field_lines(magnet)
        self.play(Create(magnetic_field_lines), run_time=3)
        
        # 显示安培力方向
        force_arrow = Arrow(
            start=coil.get_center(),
            end=coil.get_center() + 1.5*RIGHT,
            color=ORANGE,
            buff=0.1,
            stroke_width=8
        )
        force_label = Text("F", font_size=24, color=ORANGE).next_to(force_arrow, RIGHT, buff=0.1)
        
        self.play(GrowArrow(force_arrow), Write(force_label))
        
        explanation = Text("通电线圈在磁场中受到安培斥力", font_size=24, color=WHITE)
        explanation.to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(2)
        
        # 清除当前场景，准备微分分析
        self.play(
            FadeOut(title),
            FadeOut(explanation),
            FadeOut(force_arrow),
            FadeOut(force_label),
            FadeOut(current_arrow),
            FadeOut(current_label),
            FadeOut(magnetic_field_lines)
        )
        
        # 放大分析一条磁感线
        self.zoom_in_magnetic_field_analysis(magnet, coil)
        
        # 回到整体计算合力
        self.overall_force_calculation(magnet, coil)
        
    def create_coil(self, radius=1, turns=4, height=0.5):
        """创建3D线圈"""
        coil = VGroup()
        
        for i in range(turns):
            angle = i * 2 * PI / turns
            next_angle = (i + 1) * 2 * PI / turns
            
            # 创建螺旋线
            helix = ParametricFunction(
                lambda t: np.array([
                    radius * np.cos(angle + t * (next_angle - angle)),
                    radius * np.sin(angle + t * (next_angle - angle)),
                    height * t - height/2
                ]),
                t_range=[0, 1],
                color=YELLOW,
                stroke_width=4
            )
            coil.add(helix)
        
        return coil
    
    def create_magnetic_field_lines(self, magnet):
        """创建磁感线"""
        field_lines = VGroup()
        
        # N极发出的磁感线
        for i in range(8):
            angle = i * 2 * PI / 8
            start_point = magnet[0].get_center() + 0.3 * np.array([np.cos(angle), np.sin(angle), 0])
            # 创建弯曲的磁感线
            field_line = ParametricFunction(
                lambda t: self.magnetic_field_equation(t, angle),
                t_range=[0, 2],
                color=RED,
                stroke_width=2
            )
            field_lines.add(field_line)
        
        # S极进入的磁感线
        for i in range(8):
            angle = i * 2 * PI / 8
            end_point = magnet[1].get_center() + 0.3 * np.array([np.cos(angle), np.sin(angle), 0])
            
            # 创建弯曲的磁感线
            field_line = ParametricFunction(
                lambda t: self.magnetic_field_equation(t, angle, reverse=True),
                t_range=[0, 2],
                color=BLUE,
                stroke_width=2
            )
            field_lines.add(field_line)
        
        return field_lines
    
    def magnetic_field_equation(self, t, angle, reverse=False):
        """磁感线方程"""
        if reverse:
            x = -1.5 + 1.5 * t
            y = 0.5 * np.sin(angle) * np.sin(PI * t)
            z = 0.5 * np.cos(angle) * np.sin(PI * t)
        else:
            x = 1.5 - 1.5 * t
            y = 0.5 * np.sin(angle) * np.sin(PI * t)
            z = 0.5 * np.cos(angle) * np.sin(PI * t)
        
        return np.array([x, y, z])
    
    def zoom_in_magnetic_field_analysis(self, magnet, coil):
        """放大分析一条磁感线"""
        # 标题
        zoom_title = Text("微分分析：单条磁感线受力", font_size=36)
        zoom_title.to_edge(UP)
        self.play(Write(zoom_title))
        
        # 选择一条磁感线进行放大分析
        selected_field_line = ParametricFunction(
            lambda t: self.magnetic_field_equation(t, PI/4),
            t_range=[0, 2],
            color=RED,
            stroke_width=4
        )
        
        # 放大并移动到中心
        self.play(Create(selected_field_line))
        
        # 创建放大的视图
        zoom_frame = Rectangle(height=2, width=3, color=WHITE, stroke_width=2)
        zoom_frame.move_to(selected_field_line.get_center() + 0.5*RIGHT)
        
        # 创建放大的磁感线段
        field_segment = ParametricFunction(
            lambda t: self.magnetic_field_equation(t, PI/4),
            t_range=[0.4, 0.6],
            color=RED,
            stroke_width=6
        )
        
        # 创建电流元
        current_element = Line(
            start=field_segment.point_from_proportion(0.5) + 0.2*UP,
            end=field_segment.point_from_proportion(0.5) + 0.2*DOWN,
            color=GREEN,
            stroke_width=8
        )
        
        # 创建磁场向量
        field_vector = Arrow(
            start=field_segment.point_from_proportion(0.5),
            end=field_segment.point_from_proportion(0.5) + 0.5*RIGHT + 0.3*UP,
            color=RED,
            buff=0,
            stroke_width=4
        )
        
        # 创建电流元向量
        current_vector = Arrow(
            start=current_element.get_center(),
            end=current_element.get_center() + 0.3*OUT,
            color=GREEN,
            buff=0,
            stroke_width=4
        )
        
        # 创建安培力向量
        force_vector = Arrow(
            start=current_element.get_center(),
            end=current_element.get_center() + 0.5*RIGHT,
            color=ORANGE,
            buff=0,
            stroke_width=6
        )
        
        # 标签
        b_label = Text("B", font_size=20, color=RED).next_to(field_vector.get_end(), RIGHT, buff=0.1)
        dl_label = Text("dl", font_size=20, color=GREEN).next_to(current_vector.get_end(), OUT, buff=0.1)
        df_label = Text("dF", font_size=20, color=ORANGE).next_to(force_vector.get_end(), RIGHT, buff=0.1)
        # 显示放大视图
        self.play(Create(zoom_frame))
        self.play(
            selected_field_line.animate.set_stroke(width=1, opacity=0.3),
            Create(field_segment),
            Create(current_element),
            GrowArrow(field_vector),
            GrowArrow(current_vector),
            GrowArrow(force_vector),
            Write(b_label),
            Write(dl_label),
            Write(df_label)
        )
        
        # 显示安培力公式
        formula = MathTex("d\\vec{F} = I(\\vec{dl} \\times \\vec{B})", font_size=32)
        formula.to_edge(DOWN)
        self.play(Write(formula))
        
        explanation = Text("电流元在磁场中受到的安培力", font_size=24)
        explanation.next_to(formula, UP, buff=0.2)
        self.play(Write(explanation))
        
        self.wait(3)
        
        # 清除放大视图
        self.play(
            FadeOut(zoom_title),
            FadeOut(zoom_frame),
            FadeOut(field_segment),
            FadeOut(current_element),
            FadeOut(field_vector),
            FadeOut(current_vector),
            FadeOut(force_vector),
            FadeOut(b_label),
            FadeOut(dl_label),
            FadeOut(df_label),
            FadeOut(formula),
            FadeOut(explanation),
            FadeOut(selected_field_line)
        )
    
    def overall_force_calculation(self, magnet, coil):
        """整体计算合力"""
        # 标题
        overall_title = Text("整体合力计算", font_size=36)
        overall_title.to_edge(UP)
        self.play(Write(overall_title))
        
        # 重新显示磁铁和线圈
        self.play(
            magnet.animate.set_opacity(1),
            coil.animate.set_opacity(1)
        )
        
        # 创建多个电流元和受力向量
        current_elements = VGroup()
        force_vectors = VGroup()
        
        # 在圆周上均匀分布电流元
        for i in range(12):
            angle = i * 2 * PI / 12
            element_pos = coil.get_center() + 0.8 * np.array([np.cos(angle), np.sin(angle), 0])
            
            # 电流元方向（切线方向）
            dl_direction = np.array([-np.sin(angle), np.cos(angle), 0])
            
            # 创建电流元
            current_element = Line(
                start=element_pos - 0.1 * dl_direction,
                end=element_pos + 0.1 * dl_direction,
                color=GREEN,
                stroke_width=4
            )
            current_elements.add(current_element)
            
            # 计算安培力方向（假设磁场方向从N到S）
            # 简化模型：力方向大致向外
            force_direction = np.array([np.cos(angle), np.sin(angle), 0])
            
            # 创建受力向量
            force_vector = Arrow(
                start=element_pos,
                end=element_pos + 0.5 * force_direction,
                color=ORANGE,
                buff=0,
                stroke_width=3
            )
            force_vectors.add(force_vector)
        
        # 显示电流元和受力向量
        self.play(Create(current_elements), run_time=2)
        self.play(Create(force_vectors), run_time=2)
        
        # 显示合力
        resultant_force = Arrow(
            start=coil.get_center(),
            end=coil.get_center() + 2*RIGHT,
            color=RED,
            buff=0,
            stroke_width=10
        )
        resultant_label = Text("F = ∮ I(dl × B)", font_size=24, color=RED).next_to(resultant_force, RIGHT, buff=0.2)
        
        self.play(GrowArrow(resultant_force), Write(resultant_label))
        
        explanation = Text("对所有电流元积分得到总安培力", font_size=24)
        explanation.to_edge(DOWN)
        self.play(Write(explanation))
        # 演示斥力效果
        self.play(
            coil.animate.shift(1.5*RIGHT),
            force_vectors.animate.shift(1.5*RIGHT),
            resultant_force.animate.shift(1.5*RIGHT),
            resultant_label.animate.shift(1.5*RIGHT),
            run_time=3
        )
        
        self.wait(2)
        
        # 总结
        conclusion = Text("通电线圈在条形磁铁磁场中受到安培斥力", font_size=30, color=YELLOW)
        conclusion.move_to(ORIGIN)
        
        self.play(
            FadeOut(overall_title),
            FadeOut(current_elements),
            FadeOut(force_vectors),
            FadeOut(resultant_force),
            FadeOut(resultant_label),
            FadeOut(explanation),
            FadeOut(magnet),
            FadeOut(coil)
        )
        
        self.play(Write(conclusion))
        self.wait(2)