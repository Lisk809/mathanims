from manim import *
import random

class AbsurdMathLife(Scene):
    def construct(self):
        # 场景1：函数求导的"中年危机"
        self.function_midlife_crisis()
        
        # 场景2：向量的社交尴尬
        self.vector_social_awkwardness()
        
        # 场景3：无限级数的购物狂
        self.infinite_series_shopper()
        
        # 场景4：矩阵的相亲现场
        self.matrix_dating()
        
        # 结尾
        self.ending()

    def function_midlife_crisis(self):
        title = Text("场景1: 函数的中年危机", font_size=36).to_edge(UP)
        self.play(Write(title))
        
        # 创建函数
        func = MathTex("f(x) = x^2").scale(1.5)
        self.play(Write(func))
        self.wait(1)
        
        # 函数求导（中年危机）
        derivative = MathTex("f'(x) = 2x").scale(1.5)
        self.play(Transform(func, derivative))
        
        # 添加思考泡泡
        thought_bubble = ThoughtBubble().scale(0.5).next_to(func, UP+RIGHT)
        thought_text = Text("我的斜率\n越来越大了...", font_size=20).move_to(thought_bubble.get_bubble_center())
        
        self.play(Create(thought_bubble), Write(thought_text))
        self.wait(2)
        
        # 清除场景
        self.play(FadeOut(title), FadeOut(func), FadeOut(thought_bubble), FadeOut(thought_text))

    def vector_social_awkwardness(self):
        title = Text("场景2: 向量的社交尴尬", font_size=36).to_edge(UP)
        self.play(Write(title))
        
        # 创建两个向量
        vector_a = Arrow(ORIGIN, [2, 1, 0], buff=0, color=BLUE)
        label_a = MathTex("\\vec{a}").next_to(vector_a.get_end(), RIGHT)
        
        vector_b = Arrow(ORIGIN, [-1, 2, 0], buff=0, color=RED)
        label_b = MathTex("\\vec{b}").next_to(vector_b.get_end(), LEFT)
        
        vector_group = VGroup(vector_a, label_a, vector_b, label_b)
        vector_group.move_to(ORIGIN)
        
        self.play(Create(vector_a), Write(label_a))
        self.play(Create(vector_b), Write(label_b))
        
        # 向量试图点积
        dot_product = MathTex("\\vec{a} \\cdot \\vec{b} = ?").scale(1.2).to_edge(DOWN)
        self.play(Write(dot_product))
        
        # 尴尬的互动
        self.play(vector_a.animate.shift(LEFT*0.5), vector_b.animate.shift(RIGHT*0.5))
        self.wait(0.5)
        self.play(vector_a.animate.shift(RIGHT*1), vector_b.animate.shift(LEFT*1))
        self.wait(0.5)
        
        # 结果显示
        result = MathTex("\\vec{a} \\cdot \\vec{b} = 0").scale(1.2).move_to(dot_product)
        self.play(Transform(dot_product, result))
        
        # 添加尴尬的注释
        awkward_text = Text("(它们正交了...真尴尬)", font_size=24).next_to(result, DOWN)
        self.play(Write(awkward_text))
        
        self.wait(2)
        self.play(FadeOut(title), FadeOut(vector_group), FadeOut(dot_product), FadeOut(awkward_text))

    def infinite_series_shopper(self):
        title = Text("场景3: 无限级数的购物狂", font_size=36).to_edge(UP)
        self.play(Write(title))
        
        # 创建无限级数
        series = MathTex("\\sum_{n=1}^{\\infty} \\frac{1}{2^n}").scale(1.5)
        self.play(Write(series))
        
        # 级数开始"购物"
        shopping_items = VGroup(
            Text("买了一半的蛋糕", font_size=20),
            Text("买了四分之一件衣服", font_size=20),
            Text("买了八分之一的咖啡", font_size=20),
            Text("...", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(series, DOWN, buff=0.5)
        
        for item in shopping_items:
            self.play(Write(item), run_time=0.5)
        
        # 显示总和
        total = MathTex("= 1").scale(1.5).next_to(series, RIGHT)
        self.play(Write(total))
        
        # 添加注释
        comment = Text("永远买不到完整的东西!", font_size=24).next_to(shopping_items, DOWN)
        self.play(Write(comment))
        
        self.wait(2)
        self.play(FadeOut(title), FadeOut(series), FadeOut(shopping_items), FadeOut(total), FadeOut(comment))

    def matrix_dating(self):
        title = Text("场景4: 矩阵的相亲现场", font_size=36).to_edge(UP)
        self.play(Write(title))
        
        # 创建两个矩阵
        matrix_a = Matrix([["a", "b"], ["c", "d"]]).scale(1.2)
        matrix_a_label = Text("矩阵A", font_size=20).next_to(matrix_a, UP)
        
        matrix_b = Matrix([["e", "f"], ["g", "h"]]).scale(1.2)
        matrix_b_label = Text("矩阵B", font_size=20).next_to(matrix_b, UP)
        
        # 并排显示
        matrices = VGroup(matrix_a, matrix_b).arrange(RIGHT, buff=1)
        labels = VGroup(matrix_a_label, matrix_b_label)
        
        self.play(Write(matrix_a), Write(matrix_a_label))
        self.play(Write(matrix_b), Write(matrix_b_label))
        
        # 矩阵尝试相乘
        multiply_symbol = MathTex("\\times").scale(1.5).move_to(matrices.get_center())
        self.play(Write(multiply_symbol))
        
        # 显示相乘结果
        result_matrix = Matrix([
            ["ae+bg", "af+bh"],
            ["ce+dg", "cf+dh"]
        ]).scale(1).next_to(matrices, DOWN, buff=0.5)
        
        self.play(Write(result_matrix))
        
        # 添加搞笑评论
        comment = Text("这关系太复杂了!", font_size=24).next_to(result_matrix, DOWN)
        self.play(Write(comment))
        
        self.wait(2)
        self.play(FadeOut(title), FadeOut(matrices), FadeOut(labels), 
                  FadeOut(multiply_symbol), FadeOut(result_matrix), FadeOut(comment))

    def ending(self):
        # 结尾场景
        ending_text = Text("数学的荒谬人生", font_size=48)
        self.play(Write(ending_text))
        self.wait(1)
        
        # 添加副标题
        subtitle = Text("当抽象概念有了情感...", font_size=24).next_to(ending_text, DOWN)
        self.play(Write(subtitle))
        
        # 最后搞笑的数学公式
        funny_equation = MathTex("\\text{生活} = \\frac{\\text{荒谬}}{\\text{意义}}").scale(1.5).next_to(subtitle, DOWN, buff=0.5)
        self.play(Write(funny_equation))
        
        self.wait(3)

class ThoughtBubble(VMobject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 创建一个简单的思考泡泡形状
        bubble = Circle(radius=0.8, color=WHITE, fill_opacity=0.1)
        self.add(bubble)
    
    def get_bubble_center(self):
        return self.get_center()
