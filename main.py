# This is a sample Python script.
from Email import Email
import random


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def aleatoria():
    print("Empezando")
    equipos = {"Gema", "Cori", "Luis", "Raquel", "Ale"}
    dias = [7.1, 7.2, 8.1, 8.2, 8.3]

    for i in range(100):
        random.shuffle(dias)

    mensaje = ""
    for equipo, dia in zip(equipos, dias):
        mensaje = mensaje + equipo + " Le toca el dia: " + str(dia) + "\n"

    print(mensaje)
    #change email
    email = ""
    Email.SendEmail(email, mensaje)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    aleatoria()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
