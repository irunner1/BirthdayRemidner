import datetime

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

def showTodayBirthday(Bday_array):
    flag = 0
    today = datetime.datetime.today().strftime("%d/%m")
    for i in Bday_array:
        if i.date[:5] == today:
            print("Сегодня День Рождения у", i.name)
            flag = 1
            return i.name
    if flag == 0:
        print("Сегодня без праздников")
    return 'nah'

def deleteFromList(Bday_array, del_date):
    flag = 0
    for i in range(0, len(Bday_array)):
        if Bday_array[i].date == del_date:
            Bday_array.pop(i)
            flag = 1
    if flag == 0:
        print("Такой даты нет")
        return 1
    else:
        print("Дата успешно забыта")
    return 0

def showPersonBirthday(Bday_array, find_name):
    flag = 0
    for i in Bday_array:
        if i.name == find_name:
            print ("У", i.name, "День Рождения", i.date)
            flag = 1
            temp = i.name
            temp += " "
            temp += i.date
            return temp
        if flag == 0:
            print("Такого имени нет")
    return "nah"

def showNearestBirthday(Bday_array):
    min_count = 366
    rem = 0
    today = datetime.datetime.today().strftime("%m-%d")
    for i in range (0, len(Bday_array)):
        temp_date = Bday_array[i].date[3:5] + "-" + Bday_array[i].date[:2]
        today_date_format = datetime.datetime.strptime(today, "%m-%d")
        date_format = datetime.datetime.strptime(temp_date, "%m-%d")
        count = date_format - today_date_format
        if min_count > int(count.days) and int(count.days) > 0:
            min_count = count.days
            rem = i
    print("Ближайший День Рождения у", Bday_array[i].name, "через", min_count, "дней")
    return min_count

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
        if switch == 3:
            showTodayBirthday(Bday_array)
            continue
        if switch == 4:
            print("Введите дату, которую хотите удалить")
            del_date = input()
            deleteFromList(Bday_array, del_date)
            continue
        if switch == 5:
            print ("Введите имя")
            find_name = input()
            showPersonBirthday(Bday_array, find_name)
            continue
        if switch == 6:
            showNearestBirthday(Bday_array)
            continue

if __name__ == "__main__":
    main()