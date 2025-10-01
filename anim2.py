from manim import *
from patch.auto_chinese_patch import *

class CurrentMicroExpression(Scene):
    def construct(self):
        # 标题
        title = Text("电流的微观表达式推导", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        self.wait(1)

        # 初始假设
        assumptions = VGroup(
            Text("假设条件：", font_size=36, color=YELLOW),
            Text("1. 自由电子数密度：n", font_size=32),
            Text("2. 导线横截面积：S", font_size=32),
            Text("3. 电子平均漂移速度：v", font_size=32),
            Text("4. 电子电荷量：e", font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        assumptions.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(assumptions))
        self.wait(2)
        self.play(FadeOut(assumptions))

        # 推导步骤1：时间Δt内通过截面的电子数
        step1 = VGroup(
            MathTex("\\text{在时间}\\Delta t\\text{内，电子移动距离：}", font_size=36),
            MathTex("L = v \\Delta t", font_size=36),
            MathTex("\\text{通过截面的电子数：}", font_size=36),
            MathTex("N = n \\cdot S \\cdot L", font_size=36),
            MathTex("N = n \\cdot S \\cdot v \\Delta t", font_size=36)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        step1.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(step1[0]))
        self.wait(1)
        self.play(Write(step1[1]))
        self.wait(1)
        self.play(Write(step1[2]))
        self.wait(2)

        # 推导步骤2：总电荷量
        step2 = VGroup(
            MathTex("\\text{通过的总电荷量：}", font_size=36),
            MathTex("\\Delta Q = N \\cdot e", font_size=36),
            MathTex("\\Delta Q = n S v \\Delta t \\cdot e", font_size=36)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        step2.next_to(step1, DOWN, buff=0.5)
        
        self.play(Write(step2[0]))
        self.wait(1)
        self.play(Write(step2[1]))
        self.wait(2)

        # 推导步骤3：电流定义
        step3 = VGroup(
            MathTex("\\text{电流定义：}", font_size=36),
            MathTex("I = \\frac{\\Delta Q}{\\Delta t}", font_size=36),
            MathTex("I = \\frac{n S v \\Delta t \\cdot e}{\\Delta t}", font_size=36),
            MathTex("I = n S v e", font_size=36)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        step3.next_to(step2, DOWN, buff=0.5)
        
        self.play(Write(step3[0]))
        self.wait(1)
        self.play(Write(step3[1]))
        self.wait(1)
        self.play(Write(step3[2]))
        self.wait(2)

        # 清理屏幕，突出最终结果
        self.play(
            FadeOut(step1),
            FadeOut(step2),
            FadeOut(step3[0]),
            FadeOut(step3[1]),
            step3[2].animate.move_to(ORIGIN).scale(1.5)
        )
        self.wait(1)

        # 最终结果
        final_eq = MathTex("I = n S v e", font_size=60)
        self.play(Transform(step3[2], final_eq))
        self.wait(1)

        # 添加特殊文字
        special_text = Text("爱=你是唯一", font_size=36, color=PINK)
        special_text.next_to(final_eq, DOWN, buff=0.3)
        
        self.play(Write(special_text))
        self.wait(3)

        # 最终强调
        box = SurroundingRectangle(VGroup(final_eq, special_text), color=GOLD, buff=0.5)
        self.play(Create(box))
        self.wait(2)

        # 淡出所有元素
        self.play(
            FadeOut(final_eq),
            FadeOut(special_text),
            FadeOut(box),
            FadeOut(title)
        )
        self.wait(1)