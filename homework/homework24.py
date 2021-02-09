'''
Użyj wbudowanej biblioteki Turtle, żeby narysować wybrany przez siebie kształt (np. prostokąt, kwadrat,
trójkąt lub coś bardziej zaawansowanego).
'''
import turtle

star = turtle.Turtle()

for i in range(10):
    star.forward(50)
    star.right(144)

turtle.done()