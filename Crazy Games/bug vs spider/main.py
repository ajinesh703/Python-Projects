import tkinter as tk
import random
import time
import math

WIDTH = 600
HEIGHT = 400
ENEMY_SPEED = 2.5
SPAWN_INTERVAL = 1000  # ms

class BugVsSpiders:
    def __init__(self, root):
        self.root = root
        self.root.title("Bug vs Spiders")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.player = self.draw_bug(WIDTH//2, HEIGHT//2)
        self.enemies = []
        self.running = True
        self.score = 0
        self.start_time = time.time()

        self.canvas.bind("<Motion>", self.move_player)
        self.spawn_enemy()
        self.update_game()

    def draw_bug(self, x, y):
        body = self.canvas.create_oval(x-10, y-10, x+10, y+10, fill="lime")
        antenna1 = self.canvas.create_line(x-5, y-10, x-10, y-20, fill="white")
        antenna2 = self.canvas.create_line(x+5, y-10, x+10, y-20, fill="white")
        return [body, antenna1, antenna2]

    def draw_spider(self, x, y):
        body = self.canvas.create_oval(x-12, y-12, x+12, y+12, fill="red")
        legs = []
        for i in range(4):
            offset = 14 + i*2
            legs.append(self.canvas.create_line(x-offset, y-10, x-offset+5, y-20, fill="white"))
            legs.append(self.canvas.create_line(x+offset, y-10, x+offset-5, y-20, fill="white"))
            legs.append(self.canvas.create_line(x-offset, y+10, x-offset+5, y+20, fill="white"))
            legs.append(self.canvas.create_line(x+offset, y+10, x+offset-5, y+20, fill="white"))
        return [body] + legs

    def get_center(self, parts):
        coords = self.canvas.coords(parts[0])
        x = (coords[0] + coords[2]) / 2
        y = (coords[1] + coords[3]) / 2
        return x, y

    def move_player(self, event):
        px, py = self.get_center(self.player)
        dx = event.x - px
        dy = event.y - py
        for part in self.player:
            self.canvas.move(part, dx, dy)

    def spawn_enemy(self):
        if not self.running:
            return
        x = random.randint(50, WIDTH - 50)
        y = random.randint(50, HEIGHT - 50)
        spider = self.draw_spider(x, y)
        self.enemies.append(spider)
        self.root.after(SPAWN_INTERVAL, self.spawn_enemy)

    def update_game(self):
        if not self.running:
            return
        self.move_enemies()
        self.check_collisions()
        self.update_score()
        self.root.after(30, self.update_game)

    def move_enemies(self):
        px, py = self.get_center(self.player)
        for enemy in self.enemies:
            ex, ey = self.get_center(enemy)
            dx = px - ex
            dy = py - ey
            dist = max(math.sqrt(dx**2 + dy**2), 1)
            move_x = ENEMY_SPEED * dx / dist
            move_y = ENEMY_SPEED * dy / dist
            for part in enemy:
                self.canvas.move(part, move_x, move_y)

    def check_collisions(self):
        px, py = self.get_center(self.player)
        for enemy in self.enemies:
            ex, ey = self.get_center(enemy)
            if abs(px - ex) < 20 and abs(py - ey) < 20:
                self.game_over()

    def update_score(self):
        self.score = int(time.time() - self.start_time)
        self.root.title(f"Bug vs Spiders - Score: {self.score}")

    def game_over(self):
        self.running = False
        self.canvas.create_text(WIDTH//2, HEIGHT//2, text="YOU GOT EATEN", fill="white", font=("Courier", 28, "bold"))
        self.canvas.create_text(WIDTH//2, HEIGHT//2 + 40, text=f"Score: {self.score}", fill="white", font=("Arial", 16))

if __name__ == "__main__":
    root = tk.Tk()
    game = BugVsSpiders(root)
    root.mainloop()
