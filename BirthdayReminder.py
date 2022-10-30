import datetime


class BR():
    def __init__(self, date, name):
        self.date = date
        self.name = name


def addToList(bday_array, date, name):
    bday_array.append(BR(date, name))
    print("Именинник добавлен!")
    return bday_array[0].date + ' ' + bday_array[0].name


def showList(bday_array):
    print("Список именинников:\n")
    cnt = 0
    for i in bday_array:
        print("У", i.name, "День Рождения", i.date)
        cnt += 1
    return len(bday_array)


def showTodayBirthday(bday_array):
    flag = 0
    today = datetime.datetime.today().strftime("%d/%m")
    for i in bday_array:
        if i.date[:5] == today:
            print("Сегодня День Рождения у", i.name)
            flag = 1
            return i.name
    if flag == 0:
        print("Сегодня без праздников")
    return 'nah'


def deleteFromList(bday_array, del_date):
    flag = 0
    for i in range(0, len(bday_array)):
        if bday_array[i].date == del_date:
            bday_array.pop(i)
            flag = 1
    if flag == 0:
        print("Такой даты нет")
        return 1
    else:
        print("Дата успешно забыта")
    return 0


def showPersonBirthday(bday_array, find_name):
    flag = 0
    for i in bday_array:
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


def showNearestBirthday(bday_array):
    min_count = 366
    today = datetime.datetime.today().strftime("%m-%d")
    for i in range (0, len(bday_array)):
        temp_date = bday_array[i].date[3:5] + "-" + bday_array[i].date[:2]
        today_date_format = datetime.datetime.strptime(today, "%m-%d")
        date_format = datetime.datetime.strptime(temp_date, "%m-%d")
        count = date_format - today_date_format
        if min_count > int(count.days) and int(count.days) > 0:
            min_count = count.days
    print("Ближайший День Рождения у", bday_array[i].name, "через", min_count, "дней")
    return min_count


def main():
    bday_array = []

    while True:
        print("\n1) Добавить День Рождения")
        print("2) Показать все Дни Рождения")
        print("3) У кого сегодня День Рождения?")
        print("4) Удалить День Рождения")
        print("5) Найти День Рождения по имени")
        print("6) У кого ближайший День Рождения")
        switch = int(input())
        if switch == 1:
            print("Введите дату и имя. Формат даты dd/mm/yyyy")
            date = input()
            name = input()
            addToList(bday_array, date, name)
            continue
        if switch == 2:
            showList(bday_array)
            continue
        if switch == 3:
            showTodayBirthday(bday_array)
            continue
        if switch == 4:
            print("Введите дату, которую хотите удалить")
            del_date = input()
            deleteFromList(bday_array, del_date)
            continue
        if switch == 5:
            print ("Введите имя")
            find_name = input()
            showPersonBirthday(bday_array, find_name)
            continue
        if switch == 6:
            showNearestBirthday(bday_array)
            continue


if __name__ == "__main__":
    main()
