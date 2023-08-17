import turtle as t

isim = input("Doğum Gününü Kutlamak İstediğiniz Kişinin İsmi ? ")
mesaj = "Doğum Günün Kutlu Olsun",isim,"<3" 

# Ekranı ayarla
t.setup(400, 400)
t.bgcolor("white")
t.title("Doğum Günü Pastası")

# Kare çizimi için fonksiyon
def draw_square(color, x, y, size):
    t.penup()
    t.fillcolor(color)
    t.goto(x - size/2, y - size/2)
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

# Daire çizimi için fonksiyon
def draw_circle(color, x, y, radius):
    t.penup()
    t.fillcolor(color)
    t.goto(x, y - radius)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Taban
draw_square("orange", 0, 0, 200)

# Pastanın katmanları
for i in range(3):
    draw_square("yellow", 0, i*40 + 40, 160)

# Mumlar
for i in range(3):
    t.penup()
    t.goto(-70 + i*50, 120)
    t.pendown()
    draw_circle("red", -50 + i*50, 120, 10)

# Metin çizimi
t.penup()
t.goto(0, -180)
t.pendown()
t.color("black")
t.write(mesaj, align="center", font=("Arial", 16, "bold"))

# Ekranı kapatmak için tıkla
t.exitonclick()
