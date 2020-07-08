# Sim, eu usei cammelCase no codigo inteiro mesmo sendo python...
import matplotlib.pyplot as plt

# Funcao menu, principal do codigo
def menu():
    print("Bem vindo ao menu!\nDigite uma das seguintes opcoes:")
    selectedNumber = input(
        "1 para checar o dia com a maior temperatura.\n2 para checar o dia que mais choveu.\n3 para ver o grafico da "
        "temperatura de um dia.\n4 para ver o grafico com a temperatura media diaria de um mes.\n5 para ver o grafico "
        "com a precipitacao acumulada de um mes.\nOpcao escolhida: ")
    if selectedNumber == "1" or selectedNumber == "2" or selectedNumber == "3" or selectedNumber == "4" or selectedNumber == "5":
        if selectedNumber == "1":
            highestTemp()
        if selectedNumber == "2":
            hardestRain()
        if selectedNumber == "3":
            monthTemp()
        if selectedNumber == "4":
            averageTemp()
        if selectedNumber == "5":
            precipitation()
    else:
        print("\nEntrada inválida.\nRetornando ao menu.\n")
        menu()


def highestTemp():  # funcao que retorna o dia com a maior temperatura dentro de um mes
    print("Voce selecionou a opcao 1.")
    searchedMonthTest = input("Digite o mês no formato 'mm': ")
    searchedYearTest = input("Digite o ano no formato 'aaaa': ")
    #valida se o mes informado esta no formato solicitado e se está entre 01 e 12 e salva o valor
    if searchedMonthTest == '01' or searchedMonthTest == '02' or searchedMonthTest == '03' or searchedMonthTest == '04' or searchedMonthTest == '05' or searchedMonthTest == '06' or searchedMonthTest == '07' or searchedMonthTest == '08' or searchedMonthTest == '09' or searchedMonthTest == '10' or searchedMonthTest == '11' or searchedMonthTest == '12':
        searchedMonth = searchedMonthTest
    else:
        print("\nEntrada inválida.\nRetornando ao menu.\n")
        menu()
    #valida se o ano informado esta no formato solicitado e se esta no range 2019 2021, aceitando 2019 ou 2020 apenas e salvando o valor
    if searchedYearTest.isnumeric() and int(searchedYearTest) in range(2019, 2021):
        searchedYear = searchedYearTest
    else:
        print("\nEntrada inválida.\nRetornando ao menu.\n")
        menu()

    holdTheData = []
    maxTemp = [0, 0, 0, 0, 0.0, 0, 0.0]
    #separa a string principal nas classes desejadas e testa os valores
    for hourData in stringMain:
        splittedString = hourData.split(',')
        day = int(splittedString[0])
        month = int(splittedString[1])
        year = int(splittedString[2])
        hour = int(splittedString[3])
        temperature = float(splittedString[4])
        humidity = int(splittedString[5])
        rain = float(splittedString[6])
        if month == int(searchedMonth):
            if year == int(searchedYear):
                hold = [day, month, year, hour, temperature, humidity, rain]
                holdTheData.append(hold)
    #testa se a data existe no arquivo e, caso passe, pega a temperatura maior
    if len(holdTheData) == 0:
        print("\nDados no periodo solicitado não encontrados\n")
        menu()
    else:
        for temp in holdTheData:
            if temp[4] > maxTemp[4]:
                maxTemp = temp

        if maxTemp[0] == 0:
            print("\nDados no periodo solicitado não encontrados\n")
            menu()
        else:
            print("\nO dia com a maior temperatura no mes escolhido foi o dia", maxTemp[0], "com a temperatura de", maxTemp[4], "graus.")

        print("\nRetornando voce ao menu inicial.\n\n")
        menu()


def hardestRain():  # funcao que retorna o dia que mais choveu dentro de um mes
    print("Voce selecionou a opcao 2.")
    searchedMonthTest = input("Digite o mês no formato 'mm': ")
    searchedYearTest = input("Digite o ano no formato 'aaaa': ")
     #valida se o mes informado esta no formato solicitado e se está entre 01 e 12 e salva o valor
    if searchedMonthTest == '01' or searchedMonthTest == '02' or searchedMonthTest == '03' or searchedMonthTest == '04' or searchedMonthTest == '05' or searchedMonthTest == '06' or searchedMonthTest == '07' or searchedMonthTest == '08' or searchedMonthTest == '09' or searchedMonthTest == '10' or searchedMonthTest == '11' or searchedMonthTest == '12':
        searchedMonth = searchedMonthTest
    else:
        print("\nEntrada inválida.\nRetornando ao menu.\n")
        menu()
    #valida se o ano informado esta no formato solicitado e se esta no range 2019 2021, aceitando 2019 ou 2020 apenas e salvando o valor
    if searchedYearTest.isnumeric() and int(searchedYearTest) in range(2019, 2021):
        searchedYear = searchedYearTest
    else:
        print("\nEntrada inválida.\nRetornando ao menu.\n")
        menu()

    holdTheData = []
    #separa a string principal nas classes desejadas e testa os valores
    for data in stringMain:
        splittedString = data.split(',')
        day = int(splittedString[0])
        month = int(splittedString[1])
        year = int(splittedString[2])
        hour = int(splittedString[3])
        temperature = float(splittedString[4])
        humidity = int(splittedString[5])
        rain = float(splittedString[6])
        if month == int(searchedMonth):
            if year == int(searchedYear):
                hold = (day, month, year, hour, temperature, humidity, rain)
                holdTheData.append(hold)
     #testa se a data existe no arquivo e, caso passe, pega o dia com mais chuva
    if len(holdTheData) == 0:
        print("\nDados no periodo solicitado não encontrados\n")
        menu()
    else:
        actualDay = 0
        sumRain = 0
        hardestRainVar = 0
        hardestRainDay = 0

        for anotherData in holdTheData:
            day = int(anotherData[0])
            rain = float(anotherData[6])
            if actualDay == 0:
                actualDay = day
            if actualDay == day:
                sumRain += rain
            else:
                if sumRain > hardestRainVar:
                    hardestRainVar = sumRain
                    hardestRainDay = actualDay
                actualDay = day
                sumRain = 0
                sumRain += rain

        print("\nO dia que mais choveu no mes escolhido foi o dia", hardestRainDay, "com", hardestRainVar, "mm de chuva.")

        print("\nRetornando voce ao menu inicial.\n")
        menu()


def monthTemp():  # funcao que plota a temp de um dia de um mes, das 0hrs ate as 23
    print("Voce selecionou a opcao 3.")
    searchedDayTest = input("Digite o dia no formato 'dd': ")
    searchedMonthTest = input("Digite o mês no formato 'mm': ")
    searchedYearTest = input("Digite o ano no formato 'aaaa': ")
    #testa se o dia informado e valido
    if searchedDayTest.isnumeric() and int(searchedDayTest) in range(1, 32) and len(searchedDayTest) == 2:
        searchedDay = searchedDayTest
    else:
        print("\nEntrada inválida.\nRetornando ao menu.\n")
        menu()
    #valida se o mes informado esta no formato solicitado e se está entre 01 e 12 e salva o valor
    if searchedMonthTest == '01' or searchedMonthTest == '02' or searchedMonthTest == '03' or searchedMonthTest == '04' or searchedMonthTest == '05' or searchedMonthTest == '06' or searchedMonthTest == '07' or searchedMonthTest == '08' or searchedMonthTest == '09' or searchedMonthTest == '10' or searchedMonthTest == '11' or searchedMonthTest == '12':
        searchedMonth = searchedMonthTest
    else:
        print("\nEntrada inválida.\nRetornando ao menu.\n")
        menu()
    #valida se o ano informado esta no formato solicitado e se esta no range 2019 2021, aceitando 2019 ou 2020 apenas e salvando o valor
    if searchedYearTest.isnumeric() and int(searchedYearTest) in range(2019, 2021):
        searchedYear = searchedYearTest
    else:
        print("\nEntrada inválida.\nRetornando ao menu.\n")
        menu()

    listX = []
    listY = []
    #separa a string principal nas classes desejadas e testa os valores
    for data in stringMain:
        splittedString = data.split(',')
        day = int(splittedString[0])
        month = int(splittedString[1])
        year = int(splittedString[2])
        hour = int(splittedString[3])
        temperature = float(splittedString[4])
        if day == int(searchedDay):
            if month == int(searchedMonth):
                if year == int(searchedYear):
                    listX.append(hour)
                    listY.append(temperature)
    
    #testa se a data existe no arquivo e, caso passe, plota o grafico
    if len(listX) == 0:
        print("\nDados no periodo solicitado não encontrados\n")
        menu()
    else:
        plt.plot(listX, listY, "ro")
        plt.xlabel("Horario")
        plt.ylabel("Temperatura")
        plt.show()

        print("Retornando voce ao menu inicial.\n\n")
        menu()


def getData(day, month, year): #funcao para dar o split, validar informacoes e salvar as variaveis (apenas para nao repetir como nas defs anteriores)
    my_list = []
    for s in stringMain:
        splittedString = s.split(',')
        thisDay = int(splittedString[0])
        thisMonth = int(splittedString[1])
        thisYear = int(splittedString[2])
        hour = int(splittedString[3])
        temperature = float(splittedString[4])
        humidity = int(splittedString[5])
        rain = float(splittedString[6])
        if month is not None and year is not None:
            if day is not None:
                if day == thisDay and month == thisMonth and year == thisYear:
                    my_list.append((thisDay, thisMonth, thisYear, hour, temperature, humidity, rain))
            else:
                if month == thisMonth and year == thisYear:
                    my_list.append((thisDay, thisMonth, thisYear, hour, temperature, humidity, rain))
    return my_list


def averageTemp():  # funcao que plota a temp media de um mes (cada dia tem 24 medidas)
    print("Voce selecionou a opcao 4.")
    searchedMonthTest = input("Digite o mês no formato 'mm': ")
    searchedYearTest = input("Digite o ano no formato 'aaaa': ")
    #valida se o mes informado esta no formato solicitado e se está entre 01 e 12 e salva o valor
    if searchedMonthTest == '01' or searchedMonthTest == '02' or searchedMonthTest == '03' or searchedMonthTest == '04' or searchedMonthTest == '05' or searchedMonthTest == '06' or searchedMonthTest == '07' or searchedMonthTest == '08' or searchedMonthTest == '09' or searchedMonthTest == '10' or searchedMonthTest == '11' or searchedMonthTest == '12':
        searchedMonth = searchedMonthTest
    else:
        print("\nEntrada inválida.\nRetornando ao menu.\n")
        menu()
    #valida se o ano informado esta no formato solicitado e se esta no range 2019 2021, aceitando 2019 ou 2020 apenas e salvando o valor
    if searchedYearTest.isnumeric() and int(searchedYearTest) in range(2019, 2021):
        searchedYear = searchedYearTest
    else:
        print("\nEntrada inválida.\nRetornando ao menu.\n")
        menu()
    #utiliza a funcao getData, previamente comentada
    dataList = getData(day=None, month=int(searchedMonth), year=int(searchedYear))
    #testa se os dados se encontram no arquivo
    if len(dataList) == 0:
        print("\nDados no periodo solicitado não encontrados\n")
        menu()
    else:
        actualDay = 0
        actualTempSum = 0
        averageTempList = []
        averageTempDayList = []
        #pega as somas das temperaturas diarias
        for data in dataList:
            day = data[0]
            temp = data[4]
            if actualDay == 0:
                actualDay = day
            if actualDay == day:
                actualTempSum += temp
            else:
                averageTempList.append(actualTempSum // 24)
                averageTempDayList.append(actualDay)
                actualDay = day
                actualTempSum = 0
                actualTempSum += temp

        #plota o grafico
        plt.plot(averageTempDayList, averageTempList, "ro")
        plt.xlabel("Dia")
        plt.ylabel("Temperatura")
        plt.show()

        print("Retornando voce ao menu inicial.\n\n")
        menu()


def precipitation():  # funcao que plota a precipitacao acumulada por dia de um mes (cada dia tem 24 medidas)
    print("Voce selecionou a opcao 5.")
    searchedMonthTest = input("Digite o mês no formato 'mm': ")
    searchedYearTest = input("Digite o ano no formato 'aaaa': ")
    #valida se o mes informado esta no formato solicitado e se está entre 01 e 12 e salva o valor
    if searchedMonthTest == '01' or searchedMonthTest == '02' or searchedMonthTest == '03' or searchedMonthTest == '04' or searchedMonthTest == '05' or searchedMonthTest == '06' or searchedMonthTest == '07' or searchedMonthTest == '08' or searchedMonthTest == '09' or searchedMonthTest == '10' or searchedMonthTest == '11' or searchedMonthTest == '12':
        searchedMonth = searchedMonthTest
    else:
        print("\nEntrada inválida.\nRetornando ao menu.\n")
        menu()
    #valida se o ano informado esta no formato solicitado e se esta no range 2019 2021, aceitando 2019 ou 2020 apenas e salvando o valor
    if searchedYearTest.isnumeric() and int(searchedYearTest) in range(2019, 2021):
        searchedYear = searchedYearTest
    else:
        print("\nEntrada inválida.\nRetornando ao menu.\n")
        menu()
    
    #utiliza a funcao getData, previamente comentada
    dataList = getData(day=None, month=int(searchedMonth), year=int(searchedYear))
    #testa se os dados se encontram no arquivo
    if len(dataList) == 0:
        print("\nDados no periodo solicitado não encontrados\n")
        menu()
    else:
        actualDay = 0
        actualRainSum = 0
        averageRainList = []
        averageRainDayList = []
        
        #faz as somas e as bota em lista
        for data in dataList:
            day = data[0]
            rain = data[6]
            if actualDay == 0:
                actualDay = day
            if actualDay == day:
                actualRainSum += rain
            else:
                averageRainList.append(actualRainSum // 24)
                averageRainDayList.append(actualDay)
                actualDay = day
                actualRainSum = 0
                actualRainSum += rain
        
        #plota o grafico
        plt.plot(averageRainDayList, averageRainList, "ro")
        plt.xlabel("Dia")
        plt.ylabel("Chuva")
        plt.show()

        print("Retornando voce ao menu inicial.\n\n")
        menu()

#abre o arquivo dos dados (tem que estar na mesma pasta que o programa para funcionar)
refFile = open("inmet-poa-simplificado.csv")
# transforma o arquivo .csv em uma string
fileMainReading = refFile.readlines()
refFile.close()
# cria arrays com strings e remove os \n
stringMain = list(map(str.strip, fileMainReading))

print("\nCodigo criado por Matheus Kaiser\n")
menu()
