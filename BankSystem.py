import random

class BankSystem():
    def __init__(self):
        self.users = []
        
    def add(self, name):
        while True:
            account_id = random.randint(1, 500)
            for user in self.users:
                if user["id"] == account_id:
                    break
            else:
                break

        self.users.append(
            {
                "name": name,
                "balance": 0,
                "id": account_id,
                "history": []                                               
            }
        )
        print("\n" * 5)
        print("Вы успешно создали счет")
        for user in self.users:
            if user["id"] == account_id:
                print(f"Номер счета: {user["id"]}")
                print(f"Баланс: {user["balance"]}")

        
    
    def replenishment(self):
        try:
            account_id = int(input("Введите номер счета: "))
        except ValueError:
            print("Номер - число!")
            return
        print("\n" * 5)
        for user in self.users:
            if user["id"] == account_id:
                print("Пользователь найден!")
                print()
                print(f"Имя владельца: {user["name"]}")
                print(f"Баланс: {user["balance"]}")
                print()
                while True:
                    try:
                        num = int(input("На какую сумму хотите пополнить: "))
                        break
                    except ValueError:
                        print("Введите число!")
                if num > 0:
                    user["balance"] += num
                    print(f"Баланс: {user["balance"]}")
                    print("Баланс поплнен!")
                    user["history"].append(f"Поплнение счета на сумму: {num} руб.")
                else:
                    print("Не правильно введена сумма")
                break
        else:
            print("Не правильно введен номер счета")
    def removal(self):
        try:
            account_id = int(input("Введите номер счета: "))
        except ValueError:
            print("Номер - число!")
            return
        print("\n" * 5)
        for user in self.users:
            if user["id"] == account_id:       
                print("Пользователь найден!")
                print()
                print(f"Имя владельца: {user["name"]}")
                print(f"Баланс: {user["balance"]}")
                print()
                while True:
                    try:
                        num = int(input("Какую сумму хотите снять: "))
                        break
                    except ValueError:
                        print("Введите число!")
            
                if num <= 0:
                    print("Не правильно введена сумма!")
                    break
                elif num > user["balance"]:
                    print("Недостаточно средств")
                    break
                else:
                    user["balance"] -= num
                    print(f"Баланс: {user["balance"]}")
                print("Успешно сняли с баланса деньги")
                user["history"].append(f"Снятие со счета денег на сумму: {num} руб.")
                break
        else:
            print("Не правильно введен номер счета!")
    def transfer(self):
        try:
            account_id = int(input("Введите номер счета: "))
        except ValueError:
            print("Номер - число!")
            return
        print("\n" * 5)
        for user1 in self.users:
            if user1["id"] == account_id:       
                print("Пользователь найден!")
                print()
                print(f"Имя владельца: {user1["name"]}")
                print(f"Баланс: {user1["balance"]}")
                print()
                try:
                    account_toTransfer_id = int(input("Введите номер счета кому перевести: "))
                except ValueError:
                    print("Номер - число!")
                    return       
                for user2 in self.users:
                   
                    if user2["id"] == account_toTransfer_id:
                        while True:
                            if user1["id"] == user2["id"]:
                                print("Нельзя перевести себе!")
                            else:
                                break                           
                        print("Пользователь найден!")
                        print()
                        print(f"Имя владельца: {user2["name"]}")
                        print(f"Баланс: {user2["balance"]}")
                        print()
                        break
                else:
                    print("Пользователь не найден")
                    break
                while True:
                    try:
                        num = int(input("Введите сумму для отправки: "))
                        break
                    except ValueError:
                        print("Введите число!")
                        
                
                if num <= 0:
                    print("Не правильно введена сумма для перевода")
                    break
                elif num > user1["balance"]:
                    print("Недостаточно средств")
                    break
                else:
                    user1["balance"] -= num
                    user2["balance"] += num
                    print("Перевод произошел успешно!")
                    user1["history"].append(f"Перевод денег на чужой счет на сумму: {num} руб. для {user2["name"]} с id - {user2["id"]}")
                    user2["history"].append(f"Вам пришел перевод с другого счета на сумму: {num} руб. от {user1["name"]} с id - {user1["id"]}")
                    print()
                    print(f"Имя владельца 1: {user1["name"]}")
                    print(f"Баланс: {user1["balance"]}")
                    print()
                    print(f"Имя владельца 2: {user2["name"]}")
                    print(f"Баланс: {user2["balance"]}")
                    break
        else:
            print("Пользователь не найден")
    def history(self):
        try:
            account_id = int(input("Введите номер счета: "))
        except ValueError:
            print("Номер - число!")
            return
        print("\n" * 5)
        for user in self.users:
            if user["id"] == account_id:
                print("Пользователь найден!")
                if not user["history"]:
                    print("История пуста")
                    break 
                else:             
                    print("История: ", *user["history"], sep="\n")        
                    break
        else:
            print("Пользователь не найден")
system = BankSystem()       
                
print("Добро пожаловать в банк!")
while True:
    print("Выберите операцию", "1. Создание счета", "2. Пополнение счета", "3. Снятие денег", "4. Перевод между счетами", "5. Посмотреть историю счета", "6. Выход", sep="\n")
    n = int(input())
    if n == 1:
        name = input("Введите имя: ")
        system.add(name)
        print()
    elif n == 2:
        system.replenishment()
        print()
    elif n == 3:
        system.removal()
        print()
    elif n == 4:
        system.transfer()   
        print()
    elif n == 5:
        system.history()
        print()
    elif n == 6:
        break
    else:
        print("\n" * 3)
        print("Не правильно введен номер операции")                 
                    