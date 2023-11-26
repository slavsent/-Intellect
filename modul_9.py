import datetime


class Transaction:
    def __init__(self):
        self.list_trs = []

    def add_trs(self, trs):
        self.list_trs.append(trs)

    def view_trs(self):
        for el in self.list_trs:
            print(el)


class Account(Transaction):
    def __init__(self, number, type_acc, sum_acc=0, limit=0):
        super().__init__()
        self.__number = number
        self.type_acc = type_acc
        self.__sum_acc = sum_acc
        self.__limit = limit

    @classmethod
    def __chek_value(cls, sum_money):
        if type(sum_money) in (int, float):
            if sum_money >= 0:
                return True
            else:
                raise ValueError('Сумма денег не может быть отрицательной')
        else:
            raise ValueError('Сумма должна быть числом')

    def expend_money(self, money):
        if self.__chek_value(money):
            if (self.__sum_acc + self.__limit - money) > 0:
                self.__sum_acc -= money
                self.add_trs(
                    f'Дата: {datetime.datetime.now()} счет {self.__number} тип {self.type_acc} Операция: расход на сумму: {money}')
            else:
                print('На счете не достаточно средств')

    def arrival_money(self, money):
        if self.__chek_value(money):
            self.__sum_acc += money
            self.add_trs(f'Дата: {datetime.datetime.now()} счет {self.__number} тип {self.type_acc} Операция: приход на сумму: {money}')

    def get_info(self):
        print(f'Счет номер {self.__number} тип {self.type_acc} средств {self.__sum_acc}')

    def proc_kredit(self, proc, period_day):
        if self.__chek_value(proc) and self.__chek_value(period_day):
            self.add_trs(
                f'Дата: {datetime.datetime.now()} счет {self.__number} тип {self.type_acc} Начислены проценты: {self.__sum_acc * proc / 36500 * period_day}')
            self.__sum_acc -= self.__sum_acc * proc / 36500 * period_day

    def proc_depo(self, proc, period_day):
        if self.__chek_value(proc) and self.__chek_value(period_day):
            self.add_trs(
                f'Дата: {datetime.datetime.now()} счет {self.__number} тип {self.type_acc} Начислены проценты: {self.__sum_acc * proc / 36500 * period_day}')
            self.__sum_acc += self.__sum_acc * proc / 36500 * period_day


class Client:
    def __init__(self, firstname, surname, document, address):
        self.__firstname = firstname
        self.__surname = surname
        self.__document = document
        self.__address = address
        self.__acc = {}

    def add_account(self, number, type_acc, sum_acc=0, limit=0):
        self.__acc[number] = Account(number, type_acc, sum_acc, limit)

    def info_client(self):
        print(f'Клиент: Имя {self.__firstname} Фамилия {self.__surname}\n Документ {self.__document}\n Адрес {self.__address}')
        for key in self.__acc.keys():
            self.__acc[key].get_info()
            self.__acc[key].view_trs()

    def __chek_acc(self, acc):
        return acc in self.__acc

    def expend_money(self, acc, money):
        if self.__chek_acc(acc):
            self.__acc[acc].expend_money(money)

    def arrival_money(self, acc, money):
        if self.__chek_acc(acc):
            self.__acc[acc].arrival_money(money)

    def proc_kredit(self, acc, proc, period_day):
        if self.__chek_acc(acc):
            self.__acc[acc].proc_kredit(proc, period_day)

    def proc_depo(self, acc, proc, period_day):
        if self.__chek_acc(acc):
            self.__acc[acc].proc_depo(proc, period_day)


if __name__ == '__main__':
    my_acc = Account('4234234', 'текущий', 0, 0)
    my_acc.arrival_money(100000)
    my_acc.expend_money(20000)
    my_acc.proc_depo(10, 30)
    my_acc.get_info()
    my_acc.view_trs()
    my_client = Client('Petr', 'Ivanov', 'passport', 'Moscow')
    my_client.add_account('111', 'текущий')
    my_client.arrival_money('111', 100000)
    my_client.expend_money('111', 20000)
    my_client.proc_depo('111', 10, 30)
    my_client.info_client()
