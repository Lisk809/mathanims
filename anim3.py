from manim import *
import numpy as np

class MHDGenerator(Scene):
    def construct(self):
        # 标题
        title = Text("磁流体发电机原理", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 介绍磁流体发电机
        intro_text = Text(
            "磁流体发电机: 将热能直接转换为电能",
            font_size=30,
            color=WHITE
        )
        intro_text.next_to(title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(2)
        self.play(FadeOut(intro_text))
        
        # 创建基本结构
        self.create_mhd_structure()
        
        # 展示工作原理
        self.show_working_principle()
        
        # 展示电动势计算
        self.show_emf_calculation()
        
        # 展示内阻成因与计算
        self.show_internal_resistance()
        
        # 总结
        self.show_conclusion()

    def create_mhd_structure(self):
        # 创建磁场区域
        magnetic_field_rect = Rectangle(
            width=6, height=4,
            fill_color=BLUE, fill_opacity=0.2,
            stroke_color=BLUE, stroke_width=2
        )
        
        # 磁场标签
        magnetic_field_label = Text("磁场 B", font_size=24, color=BLUE)
        magnetic_field_label.next_to(magnetic_field_rect, UP, buff=0.2)
        
        # 创建电极
        left_electrode = Rectangle(
            width=0.2, height=3,
            fill_color=GOLD, fill_opacity=0.8,
            stroke_color=GOLD_E, stroke_width=2
        )
        left_electrode.move_to(LEFT * 2.5)
        
        right_electrode = Rectangle(
            width=0.2, height=3,
            fill_color=GOLD, fill_opacity=0.8,
            stroke_color=GOLD_E, stroke_width=2
        )
        right_electrode.move_to(RIGHT * 2.5)
        
        # 电极标签
        left_electrode_label = Text("电极(-)", font_size=20)
        left_electrode_label.next_to(left_electrode, LEFT, buff=0.2)
        
        right_electrode_label = Text("电极(+)", font_size=20)
        right_electrode_label.next_to(right_electrode, RIGHT, buff=0.2)
        
        # 添加所有元素
        self.play(
            Create(magnetic_field_rect),
            Write(magnetic_field_label)
        )
        self.wait(1)
        
        self.play(
            Create(left_electrode),
            Create(right_electrode),
            Write(left_electrode_label),
            Write(right_electrode_label)
        )
        self.wait(1)
        
        # 存储这些元素供后续使用
        self.magnetic_field_rect = magnetic_field_rect
        self.magnetic_field_label = magnetic_field_label
        self.left_electrode = left_electrode
        self.right_electrode = right_electrode
        self.left_electrode_label = left_electrode_label
        self.right_electrode_label = right_electrode_label

    def show_working_principle(self):
        # 添加流动方向指示
        flow_arrow = Arrow(
            start=LEFT * 3.5, end=RIGHT * 3.5,
            color=RED, buff=0,
            stroke_width=5
        )
        flow_arrow.shift(DOWN * 0.5)
        
        flow_label = Text("等离子体流动方向 v", font_size=24, color=RED)
        flow_label.next_to(flow_arrow, DOWN, buff=0.2)
        
        self.play(
            Create(flow_arrow),
            Write(flow_label)
        )
        self.wait(1)
        
        # 创建带电粒子
        positive_particles = VGroup()
        negative_particles = VGroup()
        
        for i in range(8):
            # 正电荷粒子
            pos_particle = Dot(
                point=LEFT * 3 + UP * (1 - i * 0.5) + RIGHT * i * 0.2,
                color=RED, radius=0.08
            )
            plus = Text("+", font_size=16, color=WHITE)
            plus.move_to(pos_particle.get_center())
            positive_particles.add(VGroup(pos_particle, plus))
            
            # 负电荷粒子
            neg_particle = Dot(
                point=LEFT * 3 + DOWN * (1 - i * 0.5) + RIGHT * i * 0.2,
                color=BLUE, radius=0.08
            )
            minus = Text("-", font_size=16, color=WHITE)
            minus.move_to(neg_particle.get_center())
            negative_particles.add(VGroup(neg_particle, minus))
        
        # 显示粒子流动
        self.play(
            LaggedStart(*[Create(p) for p in positive_particles], lag_ratio=0.1),
            LaggedStart(*[Create(p) for p in negative_particles], lag_ratio=0.1)
        )
        
        # 动画粒子移动
        positive_animation = LaggedStart(*[
            p.animate.shift(RIGHT * 6) for p in positive_particles
        ], lag_ratio=0.1)
        
        negative_animation = LaggedStart(*[
            p.animate.shift(RIGHT * 6) for p in negative_particles
        ], lag_ratio=0.1)
        
        self.play(positive_animation, negative_animation, run_time=3)
        self.wait(1)
        
        # 清除粒子
        self.play(
            FadeOut(positive_particles),
            FadeOut(negative_particles),
            FadeOut(flow_arrow),
            FadeOut(flow_label)
        )
        
        # 显示洛伦兹力
        self.show_lorentz_force()

    def show_lorentz_force(self):
        # 添加洛伦兹力说明
        lorentz_text = Text("洛伦兹力: F = q(v × B)", font_size=28, color=YELLOW)
        lorentz_text.to_edge(DOWN)
        
        self.play(Write(lorentz_text))
        self.wait(1)
        
        # 创建单个正电荷粒子
        pos_particle = Dot(color=RED, radius=0.1)
        pos_particle.move_to(LEFT * 2 + UP * 0.5)
        plus = Text("+", font_size=20, color=WHITE)
        plus.move_to(pos_particle.get_center())
        positive_charge = VGroup(pos_particle, plus)
        
        # 创建速度向量
        velocity_vector = Arrow(
            start=positive_charge.get_center(),
            end=positive_charge.get_center() + RIGHT * 1.5,
            color=RED, buff=0,
            stroke_width=4
        )
        velocity_label = Text("v", font_size=20, color=RED)
        velocity_label.next_to(velocity_vector, UP, buff=0.1)
        
        # 创建磁场向量
        magnetic_vector = Arrow(
            start=positive_charge.get_center(),
            end=positive_charge.get_center() + UP * 1.5,
            color=BLUE, buff=0,
            stroke_width=4
        )
        magnetic_label = Text("B", font_size=20, color=BLUE)
        magnetic_label.next_to(magnetic_vector, LEFT, buff=0.1)
        
        # 创建洛伦兹力向量
        force_vector = Arrow(
            start=positive_charge.get_center(),
            end=positive_charge.get_center() + OUT * 1.5,
            color=YELLOW, buff=0,
            stroke_width=4
        )
        # 由于Manim 3D限制，我们用虚线表示向外的向量
        force_vector_dashed = DashedLine(
            start=positive_charge.get_center(),
            end=positive_charge.get_center() + RIGHT * 1.5,
            color=YELLOW, stroke_width=4
        )
        force_label = Text("F", font_size=20, color=YELLOW)
        force_label.next_to(force_vector_dashed, DOWN, buff=0.1)
        
        self.play(Create(positive_charge))
        self.wait(0.5)
        
        self.play(
            Create(velocity_vector),
            Write(velocity_label)
        )
        self.wait(0.5)
        
        self.play(
            Create(magnetic_vector),
            Write(magnetic_label)
        )
        self.wait(0.5)
        
        self.play(
            Create(force_vector_dashed),
            Write(force_label)
        )
        self.wait(2)
        
        # 清除单个粒子演示
        self.play(
            FadeOut(positive_charge),
            FadeOut(velocity_vector),
            FadeOut(velocity_label),
            FadeOut(magnetic_vector),
            FadeOut(magnetic_label),
            FadeOut(force_vector_dashed),
            FadeOut(force_label),
            FadeOut(lorentz_text)
        )

    def show_emf_calculation(self):
        # 电动势计算标题
        emf_title = Text("电动势计算", font_size=36, color=GREEN)
        emf_title.to_edge(UP)
        
        self.play(ReplacementTransform(self.magnetic_field_label, emf_title))
        self.wait(1)
        
        # 显示电极间距
        distance_line = DashedLine(
            start=self.left_electrode.get_right() + UP * 1.5,
            end=self.right_electrode.get_left() + UP * 1.5,
            color=WHITE, stroke_width=2
        )
        distance_label = Text("d", font_size=24, color=WHITE)
        distance_label.next_to(distance_line, UP, buff=0.1)
        
        self.play(
            Create(distance_line),
            Write(distance_label)
        )
        self.wait(1)
        
        # 电动势公式
        emf_formula = MathTex(
            "\\mathcal{E} = B \\cdot v \\cdot d",
            font_size=40,
            color=GREEN
        )
        emf_formula.shift(DOWN * 0.5)
        
        self.play(Write(emf_formula))
        self.wait(2)
        
        # 公式解释
        explanation = VGroup(
            Text("其中:", font_size=24),
            Text("ℰ - 电动势"),
            Text("B - 磁感应强度"),
            Text("v - 等离子体流速"),
            Text("d - 电极间距")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        explanation.scale(0.8)
        explanation.next_to(emf_formula, DOWN, buff=0.5)
        
        self.play(Write(explanation))
        self.wait(3)
        
        # 清除电动势部分
        self.play(
            FadeOut(emf_formula),
            FadeOut(explanation),
            FadeOut(distance_line),
            FadeOut(distance_label),
            FadeOut(emf_title)
        )
        
        # 恢复磁场标签
        self.magnetic_field_label = Text("磁场 B", font_size=24, color=BLUE)
        self.magnetic_field_label.next_to(self.magnetic_field_rect, UP, buff=0.2)
        self.play(Write(self.magnetic_field_label))

    def show_internal_resistance(self):
        # 内阻标题
        resistance_title = Text("内阻成因与计算", font_size=36, color=ORANGE)
        resistance_title.to_edge(UP)
        
        self.play(ReplacementTransform(self.magnetic_field_label, resistance_title))
        self.wait(1)
        
        # 创建等离子体区域
        plasma_region = Rectangle(
            width=5, height=3,
            fill_color=PURPLE, fill_opacity=0.3,
            stroke_color=PURPLE, stroke_width=2
        )
        
        plasma_label = Text("等离子体", font_size=24, color=PURPLE)
        plasma_label.move_to(plasma_region.get_center())
        
        self.play(
            Create(plasma_region),
            Write(plasma_label)
        )
        self.wait(1)
        
        # 内阻公式
        resistance_formula = MathTex(
            "R_{int} = \\frac{d}{\\sigma \\cdot A}",
            font_size=40,
            color=ORANGE
        )
        resistance_formula.shift(DOWN * 0.5)
        
        self.play(Write(resistance_formula))
        self.wait(2)
        # 公式解释
        explanation = VGroup(
            Text("其中:", font_size=24),
            Text("R - 内阻"),
            Text("σ - 等离子体电导率"),
            Text("A - 电极面积"),
            Text("d - 电极间距")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        explanation.scale(0.8)
        explanation.next_to(resistance_formula, DOWN, buff=0.5)
        
        self.play(Write(explanation))
        self.wait(3)
        # 内阻成因说明
        cause_text = Text(
            "内阻成因: 等离子体本身具有电阻，\n" +
            "电流通过时会产生焦耳热损耗",
            font_size=24,
            color=YELLOW
        )
        cause_text.next_to(explanation, DOWN, buff=0.5)
        
        self.play(Write(cause_text))
        self.wait(3)
        
        # 清除内阻部分
        self.play(
            FadeOut(resistance_formula),
            FadeOut(explanation),
            FadeOut(cause_text),
            FadeOut(plasma_region),
            FadeOut(plasma_label),
            FadeOut(resistance_title)
        )

    def show_conclusion(self):
        # 总结标题
        conclusion_title = Text("磁流体发电机总结", font_size=36, color=GOLD)
        conclusion_title.to_edge(UP)
        
        self.play(Write(conclusion_title))
        self.wait(1)
        
        # 总结要点
        summary_points = VGroup(
            Text("• 直接将热能转换为电能", font_size=24),
            Text("• 利用等离子体在磁场中运动产生电动势", font_size=24),
            Text("• 电动势公式: ℰ = B·v·d", font_size=24),
            Text("• 内阻公式: R = d/(σ·A)", font_size=24),
            Text("• 高效率、无运动部件、环保", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        summary_points.shift(UP * 0.5)
        
        self.play(Write(summary_points))
        self.wait(4)
        
        # 结束语
        final_text = Text(
            "磁流体发电机是高效能源转换技术的重要发展方向",
            font_size=28,
            color=GREEN
        )
        final_text.to_edge(DOWN)
        
        self.play(Write(final_text))
        self.wait(3)
        
        # 淡出所有元素
        self.play(*[FadeOut(mob) for mob in self.mobjects])