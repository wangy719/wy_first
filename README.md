# 🐍 贪吃蛇游戏 (Snake Game)

一个使用Python和Pygame开发的经典贪吃蛇游戏，具有精美的视觉效果和流畅的游戏体验。

## ✨ 游戏特性

- 🎮 **经典玩法** - 还原经典贪吃蛇游戏的核心机制
- 🎨 **精美视觉效果** - 蛇头蛇身区分设计，食物带有高光效果
- 📊 **分数系统** - 实时显示当前得分和历史最高分
- ⏸️ **暂停功能** - 随时暂停/继续游戏
- 💾 **数据持久化** - 自动保存和加载最高分记录
- 🎯 **智能食物生成** - 食物不会生成在蛇身上
- 📱 **响应式控制** - 流畅的键盘控制体验

## 🚀 快速开始

### 环境要求

- Python 3.6+
- Pygame 2.0+

### 安装步骤

1. **克隆仓库**
   ```bash
   git clone <repository-url>
   cd snake-game
   ```

2. **安装Pygame**
   ```bash
   pip install pygame
   ```

3. **运行游戏**
   ```bash
   python snake_game.py
   ```

## 🎯 游戏控制

| 按键 | 功能 |
|------|------|
| **↑ ↓ ← →** | 控制蛇的移动方向 |
| **空格键** | 暂停/继续游戏<br>游戏结束后重新开始 |
| **R键** | 重新开始游戏 |
| **ESC键** | 退出游戏 |

## 🎮 游戏规则

1. 使用方向键控制蛇移动，吃掉红色食物
2. 每吃一个食物得10分，蛇身长度增加
3. 撞到墙壁或自己的身体游戏结束
4. 挑战最高分！

## 🏗️ 代码结构

```python
snake_game.py
├── Snake类           # 蛇的移动、绘制和生长逻辑
├── Food类            # 食物的生成和重定位
├── Game类            # 游戏主逻辑和控制
│   ├── 游戏状态管理（开始/暂停/结束）
│   ├── 分数系统（当前分/最高分）
│   ├── 事件处理（键盘输入）
│   └── 画面渲染（网格、文字、游戏对象）
└── main函数          # 程序入口
```

### 核心类说明

**Snake类**
- `move()` - 处理蛇的移动和碰撞检测
- `change_direction()` - 改变移动方向（防止反向移动）
- `grow_snake()` - 蛇身生长
- `draw()` - 绘制蛇（区分头和身体）

**Food类**
- `generate_position()` - 随机生成食物位置
- `respawn()` - 在安全位置重新生成食物
- `draw()` - 绘制食物（带高光效果）

**Game类**
- 游戏状态管理（运行中、暂停、结束）
- 分数记录和持久化存储
- 用户输入处理
- 游戏画面渲染

## ⚙️ 自定义配置

你可以在代码开头轻松修改游戏参数：

```python
# 游戏窗口大小
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# 网格大小（影响游戏难度）
GRID_SIZE = 20

# 游戏速度（帧率，值越小蛇移动越慢）
self.clock.tick(10)

# 颜色配置
SNAKE_HEAD_COLOR = (0, 128, 0)     # 深绿色蛇头
SNAKE_BODY_COLOR = (144, 238, 144) # 浅绿色蛇身
FOOD_COLOR = (255, 0, 0)           # 红色食物
```

## 🎨 视觉效果特色

- **蛇头设计**：独特的深绿色头部，带有白色眼睛
- **蛇身渐变**：浅绿色身体配深绿色边框
- **食物细节**：红色食物带有黄色高光，像真正的苹果
- **网格背景**：半透明网格线，提升视觉层次感
- **UI界面**：清晰的分数显示和游戏状态提示

## 📊 分数系统

- **当前分数**：实时显示本次游戏得分
- **最高分数**：自动从`high_score.txt`文件读取和保存
- **得分规则**：每吃一个食物得10分

## 🐛 常见问题解决

**Q: 游戏运行时报错"No module named 'pygame'"**
A: 请安装Pygame：`pip install pygame`

**Q: 游戏速度太快/太慢**
A: 修改`self.clock.tick(10)`中的数值（建议8-15）

**Q: 最高分文件损坏**
A: 删除`high_score.txt`文件，游戏会自动创建新的

## 🔧 扩展建议

想要进一步改进这个游戏？可以考虑：

1. **添加音效** - 吃食物、游戏结束的音效
2. **关卡系统** - 随着分数增加提高游戏速度
3. **特殊食物** - 临时加速、减速或得双倍分的特殊食物
4. **障碍物模式** - 在场景中添加固定障碍物
5. **多人模式** - 双人对战版本

## 📦 打包为可执行文件 (.exe)

如果你想将游戏打包成独立的Windows可执行文件，可以使用PyInstaller。

### 打包步骤

1. **安装PyInstaller**
   ```bash
   pip install pyinstaller
   ```

2. **创建打包脚本**（可选）
   创建一个名为`build.spec`的文件：
   ```python
   # build.spec
   block_cipher = None

   a = Analysis(
       ['snake_game.py'],
       pathex=[],
       binaries=[],
       datas=[],
       hiddenimports=[],
       hookspath=[],
       hooksconfig={},
       runtime_hooks=[],
       excludes=[],
       win_no_prefer_redirects=False,
       win_private_assemblies=False,
       cipher=block_cipher,
       noarchive=False,
   )

   pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

   exe = EXE(
       pyz,
       a.scripts,
       a.binaries,
       a.zipfiles,
       a.datas,
       name='SnakeGame',
       debug=False,
       bootloader_ignore_signals=False,
       strip=False,
       upx=True,
       upx_exclude=[],
       runtime_tmpdir=None,
       console=False,  # 设置为True显示控制台窗口，False不显示
       disable_windowed_traceback=False,
       argv_emulation=False,
       target_arch=None,
       codesign_identity=None,
       entitlements_file=None,
   )
   ```

3. **执行打包命令**
   ```bash
   # 简单打包（显示控制台窗口）
   pyinstaller --onefile snake_game.py

   # 不显示控制台窗口（推荐用于游戏）
   pyinstaller --onefile --noconsole snake_game.py

   # 添加图标（需要准备.ico文件）
   pyinstaller --onefile --noconsole --icon=snake.ico snake_game.py

   # 使用spec文件打包
   pyinstaller build.spec
   ```

4. **获取可执行文件**
   打包完成后，在生成的`dist`文件夹中找到`snake_game.exe`文件。

### 高级打包配置

如果你有资源文件（如图片、音效），需要额外配置：

```bash
# 包含资源文件
pyinstaller --onefile --noconsole --add-data "assets;assets" snake_game.py
```

创建对应的spec文件：
```python
# build_with_assets.spec
a = Analysis(
    ['snake_game.py'],
    pathex=[],
    binaries=[],
    datas=[('assets/*', 'assets')],  # 包含assets文件夹
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)
```

### 解决常见打包问题

**问题1：打包后运行闪退**
- 解决方案：先用`--console`参数打包，查看错误信息
- 确保所有依赖项都正确包含

**问题2：文件大小太大**
- 使用UPX压缩：
  ```bash
  pyinstaller --onefile --noconsole --upx-dir="path/to/upx" snake_game.py
  ```

**问题3：缺少依赖模块**
- 在spec文件中添加hiddenimports：
  ```python
  hiddenimports=['pygame'],
  ```

### 测试打包结果

打包完成后，建议在干净的Windows环境中测试.exe文件：
1. 将.exe文件复制到新文件夹
2. 双击运行测试功能是否正常
3. 测试所有游戏功能（移动、暂停、重新开始等）


这样就可以在没有Python环境的Windows电脑上直接运行你的贪吃蛇游戏了！

---

**享受游戏吧！** 🎮

如果你有任何问题或建议，欢迎在GitHub仓库中提出Issue。
