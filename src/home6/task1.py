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
    """Общий класс для банковского счета"""
    type_account = None

    def __init__(self, name, account_num):
        self.name = name
        self.account_num = account_num


class DebitAccountOwners(AccountOwners):
    """Класс счета *депозит* с расчетом платы банку"""
    type_account = 'депозит'

    def __init__(self, name, account_num, monthly_fee):
        super().__init__(name, account_num)
        self.monthly_fee = monthly_fee

    def calculation_fees(self):
        return self.monthly_fee


class CreditAccountOwners(AccountOwners):
    """Класс для счета *кредит* с расчетом платы банку"""
    type_account = 'кредит'

    def __init__(self, name, account_num, interest_rate, amount_of_credit):
        super().__init__(name, account_num)
        self.interest_rate = interest_rate
        self.amount_of_credit = amount_of_credit

    def calculation_fees(self):
        return round((((self.amount_of_credit / 100)
                       * self.interest_rate) / 365) * 30)


class DebitWithCashbackOwners(DebitAccountOwners):
    """Класс депозитного счета с кешбеком с расчетом платы банку"""
    type_account = 'депозит с кешбеком'

    def __init__(self, name, account_num, monthly_fee, cashback):
        super().__init__(name, account_num, monthly_fee)
        self.cashback = cashback

    def calculation_fees(self):
        fees = super().calculation_fees()
        return fees - self.cashback


class CellRent:
    """Класс для банковской ячейки"""
    type_account = 'банковская ячейка'

    def __init__(self, name, account_num):
        self.name = name
        self.account_num = account_num

    @classmethod
    def calculation_fees(cls):
        return 150


class SMSMixin:
    """Отправление клиенту СМС об операции"""

    @staticmethod
    def send_sms():
        print(f'Клиенту отправлено уведомление об операции')


class IndividualWithCard(DebitWithCashbackOwners, SMSMixin):
    """
    Класс для физического лица, открывшего депозит
    с кешбеком с выпуском карты(для примера)
    """

    def __init__(self, name, account_num, monthly_fee, cashback, sum):
        super().__init__(name, account_num, monthly_fee, cashback)
        self.sum = sum

    def card_issue(self, type_of_card):
        print(f'{self.name} выпустил карту {type_of_card}'
              f' к счету {self.account_num}')
        SMSMixin.send_sms()

    def withdraw_money(self):
        print(f'{self.name} снял {self.sum} руб.'
              f' с карты к счету {self.account_num}')
        SMSMixin.send_sms()


class LegalEntityWithCard(CreditAccountOwners, SMSMixin):
    """Класс для юрлица, открывшего кредитный счет с выпуском карты (для примера)"""

    def __init__(self, name, account_num, interest_rate, amount_of_credit, sum):
        super().__init__(name, account_num, interest_rate, amount_of_credit)
        self.sum = sum

    def card_issue(self, type_of_card):
        print(f'{self.name} выпустил карту {type_of_card} к счету {self.account_num}')
        SMSMixin.send_sms()

    def withdraw_money(self):
        print(f'{self.name} перечислил зарплатный фонд на сумму {self.sum} руб.'
              f' со счета {self.account_num}')


def calculation_fees(account_owners):
    """
    Функция формирует список клиетов с номерами счетов,
    типами счетов и платой за обслуживание
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
    """Список выпущенных карт"""
    print('Выпущены карты')
    for card_holder in card_holders:
        card_holder.card_issue(type_of_card='VISA')
    print('****************************************')


def spent_money(card_holders):
    """Список проведенных операций по счетам с картой"""
    print('Операции по картам:')
    for card_holder in card_holders:
        card_holder.withdraw_money()


debit_account_owner = DebitAccountOwners('Иван Иванов', '123456', 10)
credit_account_owner = CreditAccountOwners('Петр Петров', '789012', 10, 50000)
with_cashback_owner = DebitWithCashbackOwners('Сергей Сергеев', '102938', 10, 2)
cell_rent = CellRent('Сидор Сидоров', '22')
individual = IndividualWithCard('Николай Николаев', '222222', 10, 2, 5)
legal_entity = LegalEntityWithCard('ООО "Восход"', '333333', 5, 10000, 1500)

calculation_fees([
    debit_account_owner,
    credit_account_owner,
    with_cashback_owner,
    cell_rent,
    individual,
    legal_entity])

issued_cards([individual,
              legal_entity])

spent_money([individual,
             legal_entity])
