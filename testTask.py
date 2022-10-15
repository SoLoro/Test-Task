class ClientsAB():
    def __init__(self):
        self.users=set() # Множество id покупателей (ID повторяться не могут, всегда уникальны)
    def newID(self,id): # Добавление нового id
        self.users.add(id)
    def countBuyersID0(self): # Посчёт количества покупателей по группам со сквозной нумерацией в id и началом с 0
        groupID0 = dict()  # Словарь групп посчёта количества покупателей со сквозной нумерацией в id и началом с 0
        for i in self.users:
            sumNegative = 0
            sumPositive = 0
            flag = True
            for j in range(len(i)):
                sumNegative += int(i[j])
                if flag == True and int(i[j]) == j:
                    sumPositive += j
                else:
                    flag = False
            if flag == True:
                groupID0[sumPositive] = 1
            else:
                if sumNegative not in groupID0:
                    groupID0[sumNegative] = 0
        return groupID0 # На выходе словарь: ключ - сумма цифр, значение по ключу - количество покупателей
    def countBuyers(self): # Посчёт количества покупателей по группам с произвольной нумерацией
        group = dict()  # Словарь групп с произвольной нумерацией
        for i in self.users:
            sum = 0
            for j in i:
                sum+=int(j)
            if sum not in group:
                group[sum]=1
            else:
                group[sum]+=1
        return group # На выходе словарь: ключ - сумма цифр, значение по ключу - количество покупателей
client = ClientsAB()
"""
#Тест
client.newID("133133")
client.newID("012345")
client.newID("4353525")
client.newID("526535")
client.newID("0123456")
client.newID("5353524")
client.newID("6123450")
client.newID("0123456")
client.newID("6123450")
print(client.countBuyersID0())
print(client.countBuyers())
"""