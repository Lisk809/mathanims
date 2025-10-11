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
            "磁流体发电机",
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
        
        # 添加磁场方向符号 (× 表示垂直纸面向内)
        field_symbols = VGroup()
        for x in np.arange(-2.5, 3, 1):
            for y in np.arange(-1.5, 2, 1):
                cross = Text("×", font_size=20, color=BLUE)
                cross.move_to([x, y, 0])
                field_symbols.add(cross)
        
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
        self.wait(0.5)
        
        self.play(LaggedStartMap(FadeIn, field_symbols, lag_ratio=0.05))
        self.wait(0.5)
        
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
        self.field_symbols = field_symbols
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
        
        # 创建带电粒子 - 增加粒子数量
        positive_particles = VGroup()
        negative_particles = VGroup()
        
        num_particles = 15  # 增加粒子数量
        
        for i in range(num_particles):
            # 随机位置
            x_offset = np.random.uniform(-0.5, 0.5)
            y_offset = np.random.uniform(-1, 1)
            
            # 正电荷粒子
            pos_particle = Dot(
                point=LEFT * 3.5 + UP * y_offset + RIGHT * i * 0.2 + RIGHT * x_offset,
                color=RED, radius=0.06
            )
            plus = Text("+", font_size=12, color=WHITE)
            plus.move_to(pos_particle.get_center())
            positive_particles.add(VGroup(pos_particle, plus))
            
            # 负电荷粒子
            neg_particle = Dot(
                point=LEFT * 3.5 + DOWN * y_offset + RIGHT * i * 0.2 + RIGHT * x_offset,
                color=BLUE, radius=0.06
            )
            minus = Text("-", font_size=12, color=WHITE)
            minus.move_to(neg_particle.get_center())
            negative_particles.add(VGroup(neg_particle, minus))
            # 显示粒子流动
        self.play(
            LaggedStart(*[Create(p) for p in positive_particles], lag_ratio=0.05),
            LaggedStart(*[Create(p) for p in negative_particles], lag_ratio=0.05)
        )
        
        # 动画粒子移动
        positive_animation = LaggedStart(*[
            p.animate.shift(RIGHT * 7) for p in positive_particles
        ], lag_ratio=0.05)
        
        negative_animation = LaggedStart(*[
            p.animate.shift(RIGHT * 7) for p in negative_particles
        ], lag_ratio=0.05)
        
        self.play(positive_animation, negative_animation, run_time=4)
        self.wait(1)
        
        # 清除粒子
        self.play(
            FadeOut(positive_particles),
            FadeOut(negative_particles),
            FadeOut(flow_arrow),
            FadeOut(flow_label)
        )
        
        # 显示洛伦兹力 - 动态展示单个粒子受力分析
        self.show_lorentz_force_dynamic()

    def show_lorentz_force_dynamic(self):
        # 添加洛伦兹力说明
        lorentz_text = Text("洛伦兹力: F = q(v × B)", font_size=28, color=YELLOW)
        lorentz_text.to_edge(DOWN)
        
        self.play(Write(lorentz_text))
        self.wait(1)
        
        # 创建单个正电荷粒子
        pos_particle = Dot(color=RED, radius=0.1)
        pos_particle.move_to(LEFT * 1 + UP * 0.5)
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
        # 创建洛伦兹力向量 - 修正为向下
        force_vector = Arrow(
            start=positive_charge.get_center(),
            end=positive_charge.get_center() + DOWN * 1.5,
            color=YELLOW, buff=0,
            stroke_width=4
        )
        force_label = Text("F", font_size=20, color=YELLOW)
        force_label.next_to(force_vector, RIGHT, buff=0.1)
        
        # 显示叉乘符号
        cross_product = MathTex("\\vec{v} \\times \\vec{B}", font_size=24, color=WHITE)
        cross_product.move_to(positive_charge.get_center() + RIGHT * 0.8 + UP * 0.8)
        
        # 显示右手定则示意图
        hand_rule_text = Text("右手定则", font_size=20, color=GREEN)
        hand_rule_text.move_to(positive_charge.get_center() + LEFT * 2 + UP * 1)
        
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
        
        self.play(Write(cross_product))
        self.wait(1)
        
        self.play(Write(hand_rule_text))
        self.wait(1)
        
        self.play(
            Create(force_vector),
            Write(force_label)
        )
        self.wait(2)
        
        # 显示电荷分离效果
        separation_text = Text("正负电荷分离产生电势差", font_size=24, color=PURPLE)
        separation_text.move_to(positive_charge.get_center() + DOWN * 2.5)
        
        self.play(Write(separation_text))
        self.wait(2)
        
        # 清除单个粒子演示
        self.play(
            FadeOut(positive_charge),
            FadeOut(velocity_vector),
            FadeOut(velocity_label),
            FadeOut(magnetic_vector),
            FadeOut(magnetic_label),
            FadeOut(force_vector),
            FadeOut(force_label),
            FadeOut(cross_product),
            FadeOut(hand_rule_text),
            FadeOut(separation_text),
            FadeOut(lorentz_text)
        )

    def show_emf_calculation(self):
        # 清除当前场景，专注于公式推导
        self.clear_scene_for_calculation()
        
        # 电动势计算标题
        emf_title = Text("电动势计算公式推导", font_size=36, color=GREEN)
        emf_title.to_edge(UP)
        
        self.play(Write(emf_title))
        self.wait(1)
        
        # 步骤1: 洛伦兹力公式
        step1 = MathTex(
            "\\vec{F} = q(\\vec{v} \\times \\vec{B})",
            font_size=36,
            color=YELLOW
        )
        step1.shift(UP * 2)
        
        self.play(Write(step1))
        self.wait(2)
        
        # 步骤2: 电场强度定义
        step2 = MathTex(
            "\\vec{E} = \\frac{\\vec{F}}{q} = \\vec{v} \\times \\vec{B}",
            font_size=36,
            color=YELLOW
        )
        step2.next_to(step1, DOWN, buff=0.5)
        
        self.play(Write(step2))
        self.wait(2)
        # 步骤3: 电动势定义
        step3 = MathTex(
            "\\mathcal{E} = \\oint \\vec{E} \\cdot d\\vec{l}",
            font_size=36,
            color=YELLOW
        )
        step3.next_to(step2, DOWN, buff=0.5)
        
        self.play(Write(step3))
        self.wait(2)
        
        # 步骤4: 在电极间积分
        step4 = MathTex(
            "\\mathcal{E} = \\int_{-}^{+} (\\vec{v} \\times \\vec{B}) \\cdot d\\vec{l}",
            font_size=36,
            color=YELLOW
        )
        step4.next_to(step3, DOWN, buff=0.5)
        
        self.play(Write(step4))
        self.wait(2)
        
        # 步骤5: 简化公式
        step5 = MathTex(
            "\\mathcal{E} = B \\cdot v \\cdot d",
            font_size=40,
            color=GREEN
        )
        step5.next_to(step4, DOWN, buff=0.5)
        
        self.play(Write(step5))
        self.wait(2)
        
        # 公式解释
        explanation = VGroup(
            Text("其中:", font_size=24),
            Text("\\mathcal{E} - 电动势"),
            Text("B - 磁感应强度"),
            Text("v - 等离子体流速"),
            Text("d - 电极间距")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        explanation.scale(0.8)
        explanation.next_to(step5, DOWN, buff=0.5)
        
        self.play(Write(explanation))
        self.wait(3)
        
        # 清除公式推导部分
        self.play(
            FadeOut(emf_title),
            FadeOut(step1),
            FadeOut(step2),
            FadeOut(step3),
            FadeOut(step4),
            FadeOut(step5),
            FadeOut(explanation)
        )
        
        # 恢复原始场景
        self.restore_scene_after_calculation()

    def show_internal_resistance(self):
        # 清除当前场景，专注于内阻推导
        self.clear_scene_for_calculation()
        
        # 内阻标题
        resistance_title = Text("内阻成因与计算", font_size=36, color=ORANGE)
        resistance_title.to_edge(UP)
        
        self.play(Write(resistance_title))
        self.wait(1)
        
        # 内阻成因说明
        cause_text = Text(
            "内阻成因: 等离子体本身具有电阻，\n" +
            "电流通过时会产生焦耳热损耗",
            font_size=24,
            color=YELLOW
        )
        cause_text.shift(UP * 2)
        
        self.play(Write(cause_text))
        self.wait(2)
        
        # 电阻公式
        resistance_formula = MathTex(
            "R = \\rho \\frac{L}{A}",
            font_size=40,
            color=ORANGE
        )
        resistance_formula.next_to(cause_text, DOWN, buff=0.5)
        
        self.play(Write(resistance_formula))
        self.wait(2)
        # 应用到磁流体发电机
        mhd_resistance = MathTex(
            "R_{int} = \\frac{d}{\\sigma \\cdot A}",
            font_size=40,
            color=ORANGE
        )
        mhd_resistance.next_to(resistance_formula, DOWN, buff=0.5)
        
        self.play(Write(mhd_resistance))
        self.wait(2)
        
        # 公式解释
        explanation = VGroup(
            Text("其中:", font_size=24),
            Text("R_{int} - 内阻"),
            Text("\\sigma - 等离子体电导率"),
            Text("A - 电极面积"),
            Text("d - 电极间距")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        explanation.scale(0.8)
        explanation.next_to(mhd_resistance, DOWN, buff=0.5)
        
        self.play(Write(explanation))
        self.wait(3)
        
        # 效率考虑
        efficiency_text = Text(
            "内阻导致能量损失，降低发电效率",
            font_size=24,
            color=RED
        )
        efficiency_text.next_to(explanation, DOWN, buff=0.5)
        
        self.play(Write(efficiency_text))
        self.wait(2)
        
        # 清除内阻部分
        self.play(
            FadeOut(resistance_title),
            FadeOut(cause_text),
            FadeOut(resistance_formula),
            FadeOut(mhd_resistance),
            FadeOut(explanation),
            FadeOut(efficiency_text)
        )
        
        # 恢复原始场景
        self.restore_scene_after_calculation()

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
            Text("• 洛伦兹力导致电荷分离", font_size=24),
            Text("• 电动势公式: ℰ = B·v·d", font_size=24),
            Text("• 内阻公式: R_int = d/(σ·A)", font_size=24),
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

    def clear_scene_for_calculation(self):
        # 存储当前场景的所有元素
        self.saved_scene = Group(*self.mobjects)
        
        # 淡出所有元素
        self.play(FadeOut(self.saved_scene))
        
    def restore_scene_after_calculation(self):
        # 恢复原始场景
        self.play(FadeIn(self.saved_scene))
        
        # 更新引用
        self.magnetic_field_rect = self.saved_scene[0]
        self.magnetic_field_label = self.saved_scene[1]
        self.field_symbols = self.saved_scene[2]
        self.left_electrode = self.saved_scene[3]
        self.right_electrode = self.saved_scene[4]
        self.left_electrode_label = self.saved_scene[5]
        self.right_electrode_label = self.saved_scene[6]
        