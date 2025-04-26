import tkinter as tk
import random

WIDTH = 400
HEIGHT = 400
PLAYER_SIZE = 20
OBSTACLE_SIZE = 20
OBSTACLE_SPEED = 10
INTERVAL = 100  # ms
SPAWN_RATE = 15  # lower = more obstacles

class DodgeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Dodge Master")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        
        self.player = self.canvas.create_rectangle(
            WIDTH//2 - PLAYER_SIZE//2,
            HEIGHT - PLAYER_SIZE*2,
            WIDTH//2 + PLAYER_SIZE//2,
            HEIGHT - PLAYER_SIZE,
            fill="lime"
        )

        self.obstacles = []
        self.score = 0
        self.running = True

        self.root.bind("<KeyPress>", self.move_player)
        self.update_game()

    def move_player(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.player)
        if event.keysym == "Left" and x1 > 0:
            self.canvas.move(self.player, -20, 0)
        elif event.keysym == "Right" and x2 < WIDTH:
            self.canvas.move(self.player, 20, 0)

    def create_obstacle(self):
        x = random.randint(0, WIDTH - OBSTACLE_SIZE)
        return self.canvas.create_rectangle(x, 0, x + OBSTACLE_SIZE, OBSTACLE_SIZE, fill="red")

    def update_game(self):
        if not self.running:
            return

        if random.randint(1, SPAWN_RATE) == 1:
            self.obstacles.append(self.create_obstacle())

        for obstacle in self.obstacles[:]:
            self.canvas.move(obstacle, 0, OBSTACLE_SPEED)
            if self.check_collision(obstacle):
                self.game_over()
                return
            x1, y1, x2, y2 = self.canvas.coords(obstacle)
            if y2 > HEIGHT:
                self.canvas.delete(obstacle)
                self.obstacles.remove(obstacle)
                self.score += 1

        self.root.after(INTERVAL, self.update_game)

    def check_collision(self, obstacle):
        px1, py1, px2, py2 = self.canvas.coords(self.player)
        ox1, oy1, ox2, oy2 = self.canvas.coords(obstacle)
        return not (px2 < ox1 or px1 > ox2 or py2 < oy1 or py1 > oy2)

    def game_over(self):
        self.running = False
        self.canvas.create_text(WIDTH//2, HEIGHT//2, text="GAME OVER", fill="white", font=("Arial", 24, "bold"))
        self.canvas.create_text(WIDTH//2, HEIGHT//2 + 30, text=f"Score: {self.score}", fill="white", font=("Arial", 16))

if __name__ == "__main__":
    root = tk.Tk()
    game = DodgeGame(root)
    root.mainloop()
