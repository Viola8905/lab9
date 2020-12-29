arrayOffactoryDict = [{"Name": "Родинна ковбаска", "Adress": "Університетська 16", "Phone": "123456789",
                       "Specialisation": "хавка", "Work time": "24/7"},
                      {"Name": "АБС Зіна", "Adress": "Корятовича 46", "Phone": "123456789",
                       "Specialisation": "всьо і вся", "Work time": "24/7"},
                      {"Name": "Делікат", "Adress": "площа Петефі", "Phone": "112345543",
                       "Specialisation": "чай кофє потанцуєм", "Work time": "8:00-22:00"}]
while True:
    print("\n")
    print("1. Вивести всю інформацію\n"
          "2. Пошук підприємства\n"
          "3. Вийти\n")

    choose = int(input("Виберіть номер:"))
    if choose == 1:
        for i in arrayOffactoryDict:
            print(i)
    elif choose == 2:
        print("Знайти за:\n"
              "1.Назва\n"
              "2.Адресса\n"
              "3.Телефон\n"
              "4.Спеціалізація\n"
              "5.Час роботи\n")
        criteria = int(input("Виберіть номер: "))
        if criteria == 1:
            value = input("Введіть назву:")
            for i in range(len(arrayOffactoryDict)):

                if arrayOffactoryDict[i]["Name"] == value:
                    print(arrayOffactoryDict[i])
        elif criteria == 2:

            value = input("Введіть адресу:")
            for i in range(len(arrayOffactoryDict)):

                if arrayOffactoryDict[i]["Adress"] == value:
                    print(arrayOffactoryDict[i])
        elif criteria == 3:

            value = input("Введіть телефон:")
            for i in range(len(arrayOffactoryDict)):

                if arrayOffactoryDict[i]["Phone"] == value:
                    print(arrayOffactoryDict[i])
        elif criteria == 4:

            value = input("Введіть спеціалізацію:")
            for i in range(len(arrayOffactoryDict)):

                if arrayOffactoryDict[i]["Specialisation"] == value:
                    print(arrayOffactoryDict[i])
        elif criteria == 5:

            value = input("Час роботи:")
            for i in range(len(arrayOffactoryDict)):

                if arrayOffactoryDict[i]["Work time"] == value:
                    print(arrayOffactoryDict[i])
        else :
            print("Wrong number")
    elif choose ==3:
        break
    else:
        print("Wrong number")