# Manim 动画项目集

![manim_animation](https://img.shields.io/badge/Manim-Animation-blue?style=flat-square)
![python3.7+](https://img.shields.io/badge/Python-3.7+-green?style=flat-square)
![MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

这是一个使用 Manim 数学动画引擎创建的动画项目集合。所有动画都是用 Python 代码编写和生成的，展示了数学概念、算法可视化、物理模拟等各种主题的动画。

✨ 项目特色

· 🎬 丰富的动画示例 - 包含各种类型的 Manim 动画
· 📚 学习资源 - 适合 Manim 初学者学习和参考
· 🔧 可复现 - 所有源代码开源，可直接运行和修改
· 🎯 高质量渲染 - 提供高清的数学动画和可视化

📁 项目结构

```
.
├── scenes/                    # 动画场景目录
│   ├── mathematical/         # 数学相关动画
│   ├── algorithms/          # 算法可视化
│   ├── physics/             # 物理模拟
│   └── geometric/           # 几何图形动画
├── assets/                  # 资源文件
├── output/                  # 渲染输出文件
├── utils/                   # 工具函数和自定义类
└── requirements.txt         # 项目依赖
```

🚀 快速开始

环境要求

· Python 3.7+
· Manim 社区版
· FFmpeg
· LaTeX (可选，用于数学公式渲染)

安装步骤

1. 克隆仓库
   ```bash
   git clone https://github.com/your-username/your-manim-project.git
   cd your-manim-project
   ```
2. 安装依赖
   ```bash
   pip install -r requirements.txt
   ```
3. 安装 Manim
   ```bash
   pip install manim
   ```

运行动画

渲染单个场景：

```bash
manim -pql scenes/mathematical/example_scene.py ExampleScene
```

渲染高质量版本：

```bash
manim -pqh scenes/mathematical/example_scene.py ExampleScene
```

渲染为 GIF：

```bash
manim -pql --format=gif scenes/mathematical/example_scene.py ExampleScene
```

🎥 动画示例

数学动画

· fourier_series.py - 傅里叶级数可视化
· complex_plane.py - 复平面变换
· calculus_derivatives.py - 微积分导数可视化

算法可视化

· sorting_algorithms.py - 排序算法动画
· pathfinding.py - 路径查找算法
· data_structures.py - 数据结构操作

物理模拟

· wave_propagation.py - 波传播模拟
· projectile_motion.py - 抛体运动
· electromagnetic.py - 电磁场可视化

🛠️ 自定义开发

创建新场景

```python
from manim import *

class MyNewScene(Scene):
    def construct(self):
        # 创建数学表达式
        text = MathTex(r"\int_a^b f(x)dx = F(b) - F(a)")
        
        # 创建图形
        circle = Circle(radius=2, color=BLUE)
        
        # 动画序列
        self.play(Write(text))
        self.play(Create(circle))
        self.play(Transform(text, circle))
        self.wait()
```

使用自定义工具

项目中提供了一些有用的工具函数：

```python
from utils.helpers import create_grid, fade_in_sequence
from utils.custom_animations import spiral_in, wave_transform
```

📖 学习资源

· Manim 官方文档
· Manim 示例库
· 3Blue1Brown 的动画教程

🤝 贡献指南

我们欢迎各种形式的贡献！

1. Fork 本仓库
2. 创建特性分支 (git checkout -b feature/AmazingAnimation)
3. 提交更改 (git commit -m 'Add some AmazingAnimation')
4. 推送到分支 (git push origin feature/AmazingAnimation)
5. 开启 Pull Request

贡献规范

· 保持代码风格一致
· 为新的动画场景添加详细注释
· 更新 README 中的示例列表
· 确保动画能够正确渲染

📝 更新日志

[1.0.0] - 2024-01-01

· 初始版本发布
· 包含基础数学动画示例
· 添加工具函数库

📄 许可证

本项目采用 MIT 许可证 - 查看 LICENSE 文件了解详情。

🙏 致谢

· 感谢 3Blue1Brown 创建了 Manim
· 感谢 Manim 社区的所有贡献者
· 感谢所有为本项目提供反馈和建议的用户

---

⭐ 如果这个项目对你有帮助，请给它一个 star！
