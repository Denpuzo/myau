import PySimpleGUI as sg
from calendar_logic import вивести_календар
from calendar_data import отримати_конфігурацію

def відобразити_календар():
    календар = вивести_календар()
    конфігурація = отримати_конфігурацію()

    sg.theme('DarkPurple4')  

    layout = [
        [sg.Text("Календар на поточний місяць:", font=('Helvetica', 14))],
        [sg.Text(календар["місяць"], font=('Helvetica', 12))],
        [sg.Text("Пн Вт Ср Чт Пт Сб Нд", font=('Helvetica', 12))],
    ]

    for row in календар["дні"]:
        layout.append([sg.Text(day, font=('Helvetica', 12), justification='center') for day in row])

    sg.Window('Календар', layout, finalize=True).read(close=True)

if __name__ == "__main__":
    відобразити_календар()
