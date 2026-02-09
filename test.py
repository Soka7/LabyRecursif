from pyray import *
dedale = open("dedales.txt", "r")
laby = str(dedale.read())
tableau = [list(ligne) for ligne in laby.splitlines()]
print(tableau)
print(laby[0:30])
init_window(800, 450, "Hello")
def DwarSquare():
    while not window_should_close():
        trucenx = 100
        truceny = 100
        rouge = 0
        vert = 0
        bleu = 0
        begin_drawing()
        clear_background(WHITE)
        draw_text("Hello world", 190, 200, 20, VIOLET)
        for truc in tableau:
            for machin in range(len(truc)):
                Letruc = truc[machin]
                if Letruc == "X":
                    rouge = 255
                    vert = 0
                    bleu = 0
                if Letruc == " ":
                    rouge = 0
                    vert = 255
                    bleu = 0
                if Letruc == "E":
                    rouge = 0
                    vert = 0
                    bleu = 255
                if Letruc == "S":
                    rouge = 0
                    vert = 255
                    bleu = 255
                draw_rectangle_rec(
                    Rectangle(trucenx + machin*50, truceny, 50, 50),
                    (rouge, vert, bleu, 255)
                )
                if rouge < 255:
                    rouge += 5
            vert += 20
            truceny += 50
        end_drawing()
DwarSquare()
close_window()

# Set-up : pip3 install raylib==5.5.0.3 --break-system-packages