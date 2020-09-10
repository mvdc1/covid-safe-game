import arcade, sys, json, os, time, http.server, socketserver, threading

SPRITE_SCALING_PLAYER = 0.12
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 425
SCREEN_TITLE = "COVID-19 Safe Game"
endx = range(520, 600)
endy = range(213-30,213+30)

def time_format(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    return "{0}:{1}:{2}".format(int(hours), int(mins), round(sec, 2))

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.background = None
        self.player_list = None

        self.player_sprite = None
        self.score = 0
        self.set_mouse_visible(False)

    def setup(self):
        self.background = arcade.load_texture("../map.png")
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite("../spriteSTILL.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)
        print("Game has started.")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.player_list.draw()

    def on_mouse_motion(self, x, y, dx, dy):

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y
        if x in endx and y in endy:
            end = time.time()
            lapse = end - start
            print(colours.yellow + "Saving your result." + colours.reset)
            os.chdir(os.path.dirname(os.getcwd()))
            os.chdir(os.path.dirname(os.getcwd()))
            success = False
            try:
                if os.path.exists("assets/web/scores.json"):
                    with open("assets/web/scores.json") as scoresreader:
                        scores = json.load(scoresreader)
                    if len(scores) <= 13:
                        with open("assets/web/scores.json", "w") as scoresfile:
                            scores.append({"time": time_format(lapse), "total": int(end - start)})
                            json.dump(scores, scoresfile, indent=4, sort_keys=True)
                    else:
                        with open("assets/web/scores.json", "w") as scoresfile:
                            json.dump([{"time": time_format(lapse), "total": int(end - start)}], scoresfile, indent=4, sort_keys=True)
                else:
                    with open("assets/web/scores.json", "w") as newf:
                        json.dump([{"time": time_format(lapse), "total": int(end - start)}], newf, indent=4, sort_keys=True)
                    with open("assets/web/scores.json") as scoresreader:
                        scores = json.load(scoresreader)
                success = True
            except:
                print("Your score could not be saved.")
            if success:
                os.chdir("assets/web")
                print(colours.lblue + "Your score has been saved successfully." + colours.reset)
                if len(scores) >= 2:
                    arcade.close_window()
                    print("You completed the course in the following time: " + colours.yellow + time_format(lapse) + colours.reset)
                    print("You can view how this score matches up against any previous scores by heading to " + colours.purple + "'localhost:3000'" + colours.reset + ".")
                    for i in range(30, 0, -1):
                        if i < 30:
                            print(colours.clearlastline)
                            print(colours.reset + "This program will close in " + colours.red + str(i) + colours.reset + " seconds.")
                            sys.stdout.flush()
                            time.sleep(1)
                        else:
                            print(colours.reset + "This program will close in " + colours.red + str(i) + colours.reset + " seconds.")
                            sys.stdout.flush()
                            time.sleep(1)
                    sys.exit()
                else:
                    arcade.close_window()
                    print("You completed the course in the following time: " + colours.yellow + time_format(lapse))
                    print("This was your first game, you can view your score by heading to " + colours.purple + "'localhost:3000'" + colours.reset + ", but in the future you will see all of your scores which have been saved.")
                    for i in range(30, 0, -1):
                        if i < 30:
                            print(colours.clearlastline)
                            print(colours.reset + "This program will close in " + colours.red + str(i) + colours.reset + " seconds.")
                            sys.stdout.flush()
                            time.sleep(1)
                        else:
                            print(colours.reset + "This program will close in " + colours.red + str(i) + colours.reset + " seconds.")
                            sys.stdout.flush()
                            time.sleep(1)
                    sys.exit()
        else:
            return

def main():
    print("Game rendering.")
    window = MyGame()
    window.setup()
    arcade.run()

def server():
    os.chdir("assets/web")
    newl = open("server_log.txt", "w")
    sys.stderr = newl
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", 3000), handler) as httpd:
        httpd.serve_forever()

if __name__ == "__main__":
    try:
        if os.name.lower() == "nt":
            try:
                if os.environ["COLORTERM"] == "truecolor":
                    class colours:
                        red = "\u001b[31m"
                        black = "\u001b[30m"
                        white = "\u001b[37m"
                        lblue = "\u001b[36m"
                        purple = "\u001b[34m"
                        pink = "\u001b[35m"
                        green = "\u001b[32m"
                        yellow = "\u001b[33m"
                        reset = "\u001b[0m"
                        clearlastline = "\033[A                             \033[A"
                else:
                    class colours:
                        red = ""
                        black = ""
                        white = ""
                        lblue = ""
                        purple = ""
                        pink = ""
                        green = ""
                        yellow = ""
                        reset = ""
                        clearlastline = ""
            except KeyError:
                class colours:
                    red = ""
                    black = ""
                    white = ""
                    lblue = ""
                    purple = ""
                    pink = ""
                    green = ""
                    yellow = ""
                    reset = ""
                    clearlastline = ""
            daemon = threading.Thread(name="daemon server", target=server)
            daemon.setDaemon(True)
            daemon.start()
            print(colours.reset + "Server started at " + colours.green + "localhost:3000" + colours.reset + ".")
            start = time.time()
            print("Building game.")
            main()

        else:
            print("Sorry, this program is only compatible on Windows based platforms.")
            sys.exit()
    except KeyboardInterrupt:
        print("Closing the program due to the user pressing 'Ctrl + C'.")
        print("If this was a mistake feel free to launch the game again.")
        sys.exit()
    except:
        print("Sorry, this program is only compatible on Windows based platforms.")
        sys.exit()