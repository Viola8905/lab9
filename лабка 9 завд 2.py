
#                ---  Змінні  ---

arrayOfabonementDict = []


#               ---  Рішення ---
def serch(choose, criteria):
    if choose == 1:
        for i in range(len(arrayOfabonementDict)):
            if arrayOfabonementDict[i]["Adress"] == criteria:
                print(arrayOfabonementDict[i])
    if choose == 2:
        for i in range(len(arrayOfabonementDict)):
            if arrayOfabonementDict[i]["count Of Magazines"] == criteria:
                print(arrayOfabonementDict[i])
    if choose == 3:
        for i in range(len(arrayOfabonementDict)):
            if arrayOfabonementDict[i]["Names of magazines"] == criteria:
                print(arrayOfabonementDict[i])



while True:
    print("\n")
    print(".1. Вивести всю інформацію\n"
          "2. Ввести данні про абонента\n"
          "3. Знайти абонента\n"
          "4 Вийти\n")

    choose = int(input("Виберіть номер:"))

    if choose == 1:
        print(arrayOfabonementDit)
    elif choose == 2:

        '''----Ввід даних про абонента----'''
        adress = int(input("Введіть номер будинку: "))
        countOfMagazines= int(input("Введіть к-ть газет: "))
        namesofmagazines = input("Назви газет: ")
        abonementDict = {"Adress":0, "count Of Magazines": 0, "Names of magazines": ""}

        '''---Заповнення словника---'''
        abonementDict["Adress"] = adress
        abonementDict["count Of Magazines"] =countOfMagazines
        abonementDict["Names of magazines"] = namesofmagazines
        arrayOfabonementDict.append(abonementDict)
    elif choose == 3:
        print("Знайти за:\n"
              "1.Адресса\n"
              "2.Кількість газет\n"
              "3.Назви газет \n")

        criteria= int(input("Виберіть номер: "))
        if criteria == 1:
            searchCriteria = input("Введіть адресу: ")
            serch(1, searchCriteria)

        if criteria == 2:
            searchCriteria = int(input("Введіть кіль-ть газет: "))
            serch(2, searchCriteria)
        if criteria == 3:
            searchCriteria = int(input("Введіть назви газет: "))
            serch(3, searchCriteria)

        print("\n")
    elif choose == 4:
        break
    else:
        print("Введіть коректне число\n")