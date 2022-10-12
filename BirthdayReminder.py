class BR():
    def __init__(self, date, name):
        self.date = date
        self.name = name

def addToList(Bday_array, date, name):
    Bday_array.append(BR(date, name))
    print("Именинник добавлен!")
    return Bday_array[0].date + ' ' + Bday_array[0].name

def showList(Bday_array):
    print("Список именинников:\n")
    cnt = 0
    for i in Bday_array:
        print("У", i.name, "День Рождения", i.date)
        cnt += 1
    return len(Bday_array)

def main():
    Bday_array = []
    
    while True:
        print("\n1) Добавить День Рождения\n2) Показать все Дни Рождения\n3) У кого сегодня День Рождения?\n4) Удалить День Рождения\n5) Найти День Рождения по имени\n6) У кого ближайший День Рождения")
        switch = int(input())
        if switch == 1:
            print("Введите дату и имя. Формат даты dd/mm/yyyy")
            date = input()
            name = input()
            addToList(Bday_array, date, name)
            continue
        if switch == 2:
            showList(Bday_array)
            continue

if __name__ == "__main__":
    main()