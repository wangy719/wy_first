import pygame
import random
import sys

# 初始化pygame
pygame.init()

# 游戏设置
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
DARK_GREEN = (0, 128, 0)
LIGHT_GREEN = (144, 238, 144)

# 方向定义
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT
        self.grow = False
        
    def move(self):
        head_x, head_y = self.positions[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        
        # 检查边界碰撞
        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or 
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
            return False
            
        # 检查自身碰撞
        if new_head in self.positions:
            return False
            
        self.positions.insert(0, new_head)
        
        if not self.grow:
            self.positions.pop()
        else:
            self.grow = False
            
        return True
    
    def change_direction(self, direction):
        # 防止反向移动
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction
    
    def grow_snake(self):
        self.grow = True
    
    def draw(self, screen):
        for i, pos in enumerate(self.positions):
            x = pos[0] * GRID_SIZE
            y = pos[1] * GRID_SIZE
            
            if i == 0:  # 蛇头
                pygame.draw.rect(screen, DARK_GREEN, (x, y, GRID_SIZE, GRID_SIZE))
                # 画眼睛
                pygame.draw.circle(screen, WHITE, (x + 5, y + 5), 3)
                pygame.draw.circle(screen, WHITE, (x + 15, y + 5), 3)
                pygame.draw.circle(screen, BLACK, (x + 5, y + 5), 1)
                pygame.draw.circle(screen, BLACK, (x + 15, y + 5), 1)
            else:  # 蛇身
                pygame.draw.rect(screen, LIGHT_GREEN, (x, y, GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(screen, DARK_GREEN, (x, y, GRID_SIZE, GRID_SIZE), 1)

class Food:
    def __init__(self):
        self.position = self.generate_position()
    
    def generate_position(self):
        return (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    
    def respawn(self, snake_positions):
        while True:
            self.position = self.generate_position()
            if self.position not in snake_positions:
                break
    
    def draw(self, screen):
        x = self.position[0] * GRID_SIZE
        y = self.position[1] * GRID_SIZE
        pygame.draw.rect(screen, RED, (x, y, GRID_SIZE, GRID_SIZE))
        # 画苹果的高光
        pygame.draw.rect(screen, YELLOW, (x + 2, y + 2, 6, 6))

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("贪吃蛇游戏 - Python版")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.big_font = pygame.font.Font(None, 72)
        
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.high_score = self.load_high_score()
        self.game_over = False
        self.paused = False
        
    def load_high_score(self):
        try:
            with open("high_score.txt", "r") as f:
                return int(f.read())
        except:
            return 0
    
    def save_high_score(self):
        with open("high_score.txt", "w") as f:
            f.write(str(self.high_score))
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction(RIGHT)
                elif event.key == pygame.K_SPACE:
                    if self.game_over:
                        self.restart_game()
                    else:
                        self.paused = not self.paused
                elif event.key == pygame.K_r:
                    self.restart_game()
                elif event.key == pygame.K_ESCAPE:
                    return False
        return True
    
    def update(self):
        if self.game_over or self.paused:
            return
            
        if not self.snake.move():
            self.game_over = True
            if self.score > self.high_score:
                self.high_score = self.score
                self.save_high_score()
            return
        
        # 检查是否吃到食物
        if self.snake.positions[0] == self.food.position:
            self.snake.grow_snake()
            self.food.respawn(self.snake.positions)
            self.score += 10
    
    def draw(self):
        self.screen.fill(BLACK)
        
        # 画网格线
        for x in range(0, WINDOW_WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, (40, 40, 40), (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, (40, 40, 40), (0, y), (WINDOW_WIDTH, y))
        
        # 画游戏对象
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        
        # 画分数
        score_text = self.font.render(f"得分: {self.score}", True, WHITE)
        high_score_text = self.font.render(f"最高分: {self.high_score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(high_score_text, (10, 50))
        
        # 画游戏状态
        if self.game_over:
            game_over_text = self.big_font.render("游戏结束!", True, RED)
            restart_text = self.font.render("按空格键重新开始", True, WHITE)
            text_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
            restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20))
            self.screen.blit(game_over_text, text_rect)
            self.screen.blit(restart_text, restart_rect)
        elif self.paused:
            pause_text = self.big_font.render("游戏暂停", True, YELLOW)
            continue_text = self.font.render("按空格键继续", True, WHITE)
            text_rect = pause_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
            continue_rect = continue_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20))
            self.screen.blit(pause_text, text_rect)
            self.screen.blit(continue_text, continue_rect)
        
        # 画控制说明
        if not self.game_over and not self.paused:
            controls = [
                "方向键: 控制移动",
                "空格键: 暂停/继续",
                "R键: 重新开始",
                "ESC键: 退出游戏"
            ]
            for i, control in enumerate(controls):
                control_text = pygame.font.Font(None, 24).render(control, True, WHITE)
                self.screen.blit(control_text, (WINDOW_WIDTH - 200, 10 + i * 25))
        
        pygame.display.flip()
    
    def restart_game(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.game_over = False
        self.paused = False
    
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(10)  # 控制游戏速度
        
        pygame.quit()
        sys.exit()

def main():
    print("贪吃蛇游戏启动中...")
    print("游戏控制:")
    print("- 方向键: 控制蛇的移动")
    print("- 空格键: 暂停/继续游戏")
    print("- R键: 重新开始游戏")
    print("- ESC键: 退出游戏")
    print("\n游戏目标: 控制蛇吃食物，避免撞墙和撞到自己!")
    
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
