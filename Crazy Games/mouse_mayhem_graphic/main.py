import tkinter as tk
import random
import time
from PIL import Image, ImageTk

WIDTH = 600
HEIGHT = 400
ENEMY_SPEED = 3
SPAWN_INTERVAL = 1000  # ms

class BugVsSpidersGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Bug vs Spiders")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        # Load images
        self.bug_img = ImageTk.PhotoImage(Image.open("bug.png").resize((32, 32)))
        self.spider_img = ImageTk.PhotoImage(Image.open("spider.png").resize((40, 40)))

        self.player = self.canvas.create_image(WIDTH//2, HEIGHT//2, image=self.bug_img)
        self.enemies = []
        self.running = True
        self.score = 0
        self.start_time = time.time()

        self.canvas.bind("<Motion>", self.move_player)
        self.spawn_enemy()
        self.update_game()

    def move_player(self, event):
        self.canvas.coords(self.player, event.x, event.y)

    def spawn_enemy(self):
        if not self.running:
            return
        x = random.randint(0, WIDTH - 40)
        y = random.randint(0, HEIGHT - 40)
        spider = self.canvas.create_image(x, y, image=self.spider_img)
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
        px, py = self.canvas.coords(self.player)

        for enemy in self.enemies:
            ex, ey = self.canvas.coords(enemy)
            dx = px - ex
            dy = py - ey
            dist = max((dx**2 + dy**2)**0.5, 1)

            move_x = ENEMY_SPEED * dx / dist
            move_y = ENEMY_SPEED * dy / dist

            self.canvas.move(enemy, move_x, move_y)

    def check_collisions(self):
        px, py = self.canvas.coords(self.player)
        for enemy in self.enemies:
            ex, ey = self.canvas.coords(enemy)
            if abs(px - ex) < 25 and abs(py - ey) < 25:
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
    game = BugVsSpidersGame(root)
    root.mainloop()
