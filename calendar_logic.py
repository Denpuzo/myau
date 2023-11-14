import datetime

def вивести_календар():
    поточна_дата = datetime.datetime.now()
    рік = поточна_дата.year
    місяць = поточна_дата.month

    перший_день_місяця = datetime.date(рік, місяць, 1)
    останній_день_місяця = datetime.date(рік, місяць + 1, 1) - datetime.timedelta(days=1)
    початок_тижня = перший_день_місяця.weekday()

    дні = []
    день = 1
    for _ in range(6):
        row = []
        for i in range(7):
            if день > останній_день_місяця.day:
                break
            if i < початок_тижня and день == 1:
                row.append("   ")
            else:
                row.append(f"{день:2d}")
                день += 1
        дні.append(row)

    return {
        "місяць": поточна_дата.strftime("%B %Y"),
        "дні": дні
    }
