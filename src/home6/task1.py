"""
Создайте модель из жизни. Это может быть бронирование комнаты в отеле,
покупка билета в транспортной компании, или простая РПГ.
Создайте несколько объектов классов, которые описывают ситуацию.
Объекты должны содержать как атрибуты так и методы класса для симуляции
различных действий. Программа должна инстанцировать объекты и эмулировать
какую-либо ситуацию
 - вызывать методы, взаимодействие объектов и т.д.
****************************************************************************
 Учет некоторых банковский операций по счетам клиентов:
 1. Расчет вознаграждения банка по обслуживанию банковских
    счетов/услуг разных типов
 2. Учет выпущенных карт
 3. Учет операций по картам
"""


class AccountOwners:
    """Общий класс для учета владельца банковского счета.

    Атрибут класса: type_account - тип аккаунта (str)
    Конструктор принимает:
    name - ФИО клиента (str);
    account_num - номер счета (str)
    """
    type_account = None

    def __init__(self, name, account_num):
        self.name = name
        self.account_num = account_num


class DebitAccountOwners(AccountOwners):
    """Класс владельца счета *депозит* с расчетом платы банку

    Конструктор принимает:
     - Унаследовано от класса AccountOwners:
    name - ФИО клиента (str);
    account_num - номер счета (str)
    - Добавлено:
    monthly_fee - плата за обслуживание счета в месяц (int)
    """
    type_account = 'депозит'

    def __init__(self, name, account_num, monthly_fee):
        super().__init__(name, account_num)
        self.monthly_fee = monthly_fee

    def calculation_fees(self):
        """Метод возвращает сумму платы за обслуживание счета"""
        return self.monthly_fee


class CreditAccountOwners(AccountOwners):
    """Класс для владельца счета *кредит* с расчетом платы банку

    Конструктор принимает:
     - Унаследовано от класса AccountOwners:
    name - ФИО клиента (str);
    account_num - номер счета (str)
    - Добавлено:
    interest_rate - процент за пользование кредитом (int)
    amount_credit - сумма кредита (int)
    """
    type_account = 'кредит'

    def __init__(self, name, account_num, interest_rate, amount_credit):
        super().__init__(name, account_num)
        self.interest_rate = interest_rate
        self.amount_of_credit = amount_credit

    def calculation_fees(self):
        """Метод возвращает сумму процентов за пользование кредитом в месяц"""
        a = self.amount_of_credit / 100
        b = (a * self.interest_rate) / 365
        c = b * 30
        return round(c)


class DebitWithCashbackOwners(DebitAccountOwners):
    """Класс владельца депозитного счета с кешбеком с расчетом платы банку

    Конструктор принимает:
     - Унаследовано от класса DebitAccountOwners:
    name - ФИО клиента (str);
    account_num - номер счета (str)
    monthly_fee - плата за обслуживание счета в месяц (int)
    - Добавлено:
    cashback (int) - сумма бонусов, возвращаемая клиенту за расчеты с картой
    """
    type_account = 'депозит с кешбеком'

    def __init__(self, name, account_num, monthly_fee, cashback):
        super().__init__(name, account_num, monthly_fee)
        self.cashback = cashback

    def calculation_fees(self):
        """Метод возвращает сумму платы за обслуживание счета

        за вычетом суммы кэшбека
        """
        fees = super().calculation_fees()
        return fees - self.cashback


class CellRent:
    """Класс клиента, арендующего банковскую ячейку

    Атрибут класса:
    type_account - тип аккаунта клиента
    Конструктор принимает:
    name - ФИО клиента (str);
    account_num - номер счета (str)
    """
    type_account = 'банковская ячейка'

    def __init__(self, name, account_num):
        self.name = name
        self.account_num = account_num

    @classmethod
    def calculation_fees(cls):
        """Метод возвращает сумму платы за аренду банковской ячейки"""
        return 150


class SMSMixin:
    """Отправление клиенту СМС об операции"""

    @classmethod
    def send_sms(cls, message):
        """Метод возвращает уведомление об отправке клиенту СМС

         о проведенной операции вместе с текстом сообщения
         """
        print(f'Клиенту отправлено уведомление об операции: {message}')


class IndividualWithCard(DebitWithCashbackOwners, SMSMixin):
    """Класс клиента-физического лица, открывшего депозит

    с кешбеком с выпуском карты(для примера)
    Конструктор принимает:
     - Унаследовано от класса DebitWithCashbackOwners:
    name - ФИО клиента (str);
    account_num - номер счета (str)
    monthly_fee - плата за обслуживание счета в месяц (int)
    cashback (int) - сумма бонусов, возвращаемая клиенту за расчеты с картой
    Добавлено:
    sum (int) - переменная для суммы денег. В данном классе используется
    в функции, информирующей банк и клиента о проведенной операции по снятию
    денежных средств
    """

    def __init__(self, name, account_num, monthly_fee, cashback, sum):
        super().__init__(name, account_num, monthly_fee, cashback)
        self.sum = sum

    def card_issue(self):
        """Метод выпуска карты по желанию владельца счета.

        Позволяет выбрать тип карты.
        """
        answer = str(input('Хотите выпустить карту? yes/no:'))
        if answer == 'yes':
            type_of_card = str(input('Какой тип карты вы хотите выпустить?'
                                     ' Mastercard/Visa: '))
            print(f'{self.name} выпустил карту {type_of_card}'
                  f' к счету {self.account_num}')
            SMSMixin.send_sms(message=f'{self.name}, Ваша карта готова')
        if answer == 'no':
            print('Карта к счету не выпускалась')

    def withdraw_money(self):
        """Метод информирует банк и клиента о произведенном снятии денег"""
        print(f'{self.name} снял {self.sum} руб.'
              f' с карты к счету {self.account_num}')
        SMSMixin.send_sms(message=f'Произведено снятие на сумму'
                                  f' {self.sum} руб.')


class LegalEntityWithCard(CreditAccountOwners, SMSMixin):
    """Класс клиента-юрлица, открывшего кредитный счет

    с выпуском карты (для примера).
    Конструктор принимает:
     - Унаследовано от класса CreditAccountOwners:
    name - ФИО клиента (str);
    account_num - номер счета (str)
    interest_rate - процент за пользование кредитом (int)
    amount_credit - сумма кредита (int)
    Добавлено:
    sum (int) - переменная для суммы денег. В данном классе используется
    в функции, фиксирующей проведенную операцию по движению
    денежных средств
    """

    def __init__(self, name, account_num, interest_rate, amount_credit, sum):
        super().__init__(name, account_num, interest_rate, amount_credit)
        self.sum = sum

    def card_issue(self):
        """Метод выпуска карты по желанию владельца счета.

        Позволяет выбрать тип карты.
        """
        answer = str(input('Хотите выпустить карту? yes/no:'))
        if answer == 'yes':
            type_of_card = str(input('Какой тип карты вы хотите выпустить?'
                                     ' Mastercard/Visa: '))
            print(f'{self.name} выпустил карту {type_of_card}'
                  f' к счету {self.account_num}')
            SMSMixin.send_sms(message=f'{self.name}, Ваша карта готова')
        if answer == 'no':
            print('Карта к счету не выпускалась')

    def withdraw_money(self):
        """Метод фиксирует информацию о движении денежных средств"""
        print(f'{self.name} перечислил зарплатный фонд'
              f' на сумму {self.sum} руб.'
              f' со счета {self.account_num}')


def calculation_fees(account_owners):
    """Функция выводит список клиентов с номерами счетов,

    типами счетов, платой за обслуживание, а также общей суммой вознаграждения,
    причитающегося банку за оказанные услуги
    """
    total = 0
    for account_owner in account_owners:
        print(f'Вознаграждение банка за обслуживание типа'
              f' *{account_owner.type_account}* '
              f'номер {account_owner.account_num}'
              f' для {account_owner.name}'
              f' за текущий месяц: {account_owner.calculation_fees()} руб.')
        a = account_owner.calculation_fees()
        total += a
    print(f'Итого вознаграждение банка {total} руб')
    print('*****************************************')


def issued_cards(card_holders):
    """Функция для управления выпуском карт к счету"""
    print('Выпуск карт')
    for card_holder in card_holders:
        print(f'Клиент {card_holder.name}')
        card_holder.card_issue()
    print('****************************************')


def spent_money(card_holders):
    """Список проведенных операций по счетам с картой"""
    print('Операции по картам:')
    for card_holder in card_holders:
        card_holder.withdraw_money()


debit_account_owner = DebitAccountOwners('Иван Иванов', '123456', 10)
credit_account_owner = CreditAccountOwners('Петр Петров', '789012', 10, 50000)
with_cashback_own = DebitWithCashbackOwners('Сергей Сергеев', '102938', 10, 2)
cell_rent = CellRent('Сидор Сидоров', '22')
individual = IndividualWithCard('Николай Николаев', '222222', 10, 2, 5)
legal_entity = LegalEntityWithCard('ООО "Восход"', '333333', 5, 10000, 1500)

calculation_fees([
    debit_account_owner,
    credit_account_owner,
    with_cashback_own,
    cell_rent,
    individual,
    legal_entity])

issued_cards([individual,
              legal_entity])

spent_money([individual,
             legal_entity])
