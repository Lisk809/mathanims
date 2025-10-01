from manim import *

class CurrentMicroExpression(Scene):
    def construct(self):
        # 标题
        title = Text("电流的微观表达式推导", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        self.wait(1)

        # 微观视角：导体中的电子运动
        self.show_microscopic_view(title)

        # 初始假设
        self.show_assumptions(title)

        # 推导过程
        self.show_derivation(title)

        # 最终结果和特殊文字
        self.show_final_result()

    def show_microscopic_view(self, title):
        # 创建导体示意图
        conductor = Rectangle(
            width=6, height=1.5, 
            fill_color=BLUE_E, fill_opacity=0.3,
            stroke_color=BLUE, stroke_width=2
        )
        conductor.next_to(title, DOWN, buff=0.8)
        
        # 添加导体标签
        conductor_label = Text("金属导体", font_size=24, color=BLUE)
        conductor_label.next_to(conductor, DOWN, buff=0.2)
        
        # 创建多个电子点
        electrons = VGroup()
        for i in range(15):
            electron = Dot(radius=0.05, color=RED)
            # 随机分布在导体内
            x = conductor.get_left()[0] + 0.2 + 0.4 * i
            y = conductor.get_center()[1] + 0.5 * np.random.uniform(-1, 1)
            electron.move_to([x, y, 0])
            electrons.add(electron)
        
        # 电子运动动画
        electron_movements = []
        for electron in electrons:
            start_pos = electron.get_center()
            # 向右移动一段距离
            end_pos = start_pos + RIGHT * 0.8
            movement = electron.animate.move_to(end_pos)
            electron_movements.append(movement)
        
        # 显示导体和电子
        self.play(Create(conductor), Write(conductor_label))
        self.play(LaggedStartMap(GrowFromCenter, electrons, lag_ratio=0.1))
        self.wait(1)
        
        # 显示电子运动
        movement_text = Text("电子定向移动形成电流", font_size=28, color=RED)
        movement_text.next_to(conductor_label, DOWN, buff=0.3)
        self.play(Write(movement_text))
        
        # 电子移动动画
        self.play(LaggedStart(*electron_movements, lag_ratio=0.05), run_time=2)
        self.wait(1)
        
        # 清理微观视图
        self.play(
            FadeOut(conductor),
            FadeOut(conductor_label),
            FadeOut(electrons),
            FadeOut(movement_text)
        )
        self.wait(1)

    def show_assumptions(self, title):
        # 假设条件标题
        assumption_title = Text("基本假设:", font_size=36, color=YELLOW)
        assumption_title.next_to(title, DOWN, buff=0.5)
        
        # 假设条件列表
        assumptions = VGroup(
            Text("自由电子数密度: n", font_size=32),
            Text("导线横截面积: S", font_size=32),
            Text("电子平均漂移速度: v", font_size=32),
            Text("电子电荷量: e", font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        assumptions.next_to(assumption_title, DOWN, buff=0.4)
        
        self.play(Write(assumption_title))
        self.wait(0.5)
        self.play(LaggedStartMap(Write, assumptions, lag_ratio=0.2))
        self.wait(2)
        
        # 淡出假设条件
        self.play(
            FadeOut(assumption_title),
            FadeOut(assumptions)
        )
        self.wait(1)

    def show_derivation(self, title):
        # 步骤1：时间Δt内电子移动距离
        step1_text = Text("在时间Δt内，电子移动距离:", font_size=32)
        step1_eq = MathTex("L = v \\Delta t", font_size=36)
        step1_group = VGroup(step1_text, step1_eq).arrange(RIGHT, buff=0.3)
        step1_group.next_to(title, DOWN, buff=0.8)
        
        self.play(Write(step1_text))
        self.play(Write(step1_eq))
        self.wait(2)

        # 步骤2：通过截面的电子数
        step2_text = Text("通过截面的电子数:", font_size=32)
        step2_eq = MathTex("N = n \\cdot S \\cdot L", font_size=36)
        step2_group = VGroup(step2_text, step2_eq).arrange(RIGHT, buff=0.3)
        step2_group.next_to(step1_group, DOWN, buff=0.5)
        
        self.play(Write(step2_text))
        self.play(Write(step2_eq))
        self.wait(1)
        
        # 代入L
        step2_sub = MathTex("N = n S v \\Delta t", font_size=36)
        step2_sub.next_to(step2_group, DOWN, buff=0.3)
        
        self.play(Write(step2_sub))
        self.wait(2)

        # 步骤3：总电荷量
        step3_text = Text("通过的总电荷量:", font_size=32)
        step3_eq = MathTex("\\Delta Q = N \\cdot e", font_size=36)
        step3_group = VGroup(step3_text, step3_eq).arrange(RIGHT, buff=0.3)
        step3_group.next_to(step2_sub, DOWN, buff=0.5)
        
        self.play(Write(step3_text))
        self.play(Write(step3_eq))
        self.wait(1)
        
        # 代入N
        step3_sub = MathTex("\\Delta Q = n S v \\Delta t \\cdot e", font_size=36)
        step3_sub.next_to(step3_group, DOWN, buff=0.3)
        
        self.play(Write(step3_sub))
        self.wait(2)

        # 步骤4：电流定义
        step4_text = Text("电流定义:", font_size=32)
        step4_eq = MathTex("I = \\frac{\\Delta Q}{\\Delta t}", font_size=36)
        step4_group = VGroup(step4_text, step4_eq).arrange(RIGHT, buff=0.3)
        step4_group.next_to(step3_sub, DOWN, buff=0.5)
        
        self.play(Write(step4_text))
        self.play(Write(step4_eq))
        self.wait(1)
        
        # 代入ΔQ
        step4_sub1 = MathTex("I = \\frac{n S v \\Delta t \\cdot e}{\\Delta t}", font_size=36)
        step4_sub1.next_to(step4_group, DOWN, buff=0.3)
        
        self.play(Write(step4_sub1))
        self.wait(1)
        
        # 简化
        step4_sub2 = MathTex("I = n S v e", font_size=36)
        step4_sub2.next_to(step4_sub1, DOWN, buff=0.3)
        
        self.play(Write(step4_sub2))
        self.wait(2)
        
        # 清理屏幕，突出最终结果
        self.play(
            FadeOut(step1_group),
            FadeOut(step2_group),
            FadeOut(step2_sub),
            FadeOut(step3_group),
            FadeOut(step3_sub),
            FadeOut(step4_group),
            FadeOut(step4_sub1),
            step4_sub2.animate.move_to(ORIGIN).scale(1.5)
        )
        self.wait(2)

    def show_final_result(self):
        # 最终结果
        final_eq = MathTex("I", "=", "n", "S", "v", "e", font_size=72)
        
        # 添加特殊文字
        special_text = Text("爱=你是唯一", font_size=36, color=PINK)
        special_text.next_to(final_eq, DOWN, buff=0.3)
        
        self.play(Write(final_eq))
        self.wait(1)
        self.play(Write(special_text))
        self.wait(2)

        # 最终强调
        box = SurroundingRectangle(
            VGroup(final_eq, special_text), 
            color=GOLD, buff=0.5,
            corner_radius=0.2
        )
        self.play(Create(box))
        self.wait(3)

        # 淡出所有元素
        self.play(
            FadeOut(final_eq),
            FadeOut(special_text),
            FadeOut(box)
        )
        self.wait(1)