from pyray import *
from Game import *

game = Game()
game.Launch()
game.Update()
dedale = open("dedales.txt", "r")
laby = str(dedale.read())
tableau = [list(ligne) for ligne in laby.splitlines()]
print(tableau)
print(laby[0:30])
init_window(800, 450, "Hello")
def DwarSquare(taille_carre, taille_titre):
    while not window_should_close():
        trucenx = 100
        truceny = 100
        rouge = 0
        vert = 0
        bleu = 0
        begin_drawing()
        clear_background(WHITE)
        draw_text("Labyrinthe", trucenx - 50 - taille_titre, truceny- 50 - (taille_titre // 2), taille_titre, RED)
        for truc in tableau:
            for machin in range(len(truc)):
                Letruc = truc[machin]
                match Letruc:
                    case "X":
                        rouge = 255
                        vert = 0
                        bleu = 0
                    case " ":
                        rouge = 0
                        vert = 255
                        bleu = 0
                    case "E":
                        rouge = 0
                        vert = 0
                        bleu = 255
                    case "S":
                        rouge = 0
                        vert = 255
                        bleu = 255
                draw_rectangle_rec(
                    Rectangle(trucenx + machin*taille_carre, truceny, taille_carre, taille_carre),
                    (rouge, vert, bleu, 255)
                )
            truceny += taille_carre
        end_drawing()
DwarSquare(10, 50)
close_window()

# Set-up : pip3 install raylib==5.5.0.3 --break-system-packages