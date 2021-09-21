import bank_account


def issue_a_check(operations):
    for operation in operations:
        print(f'По карте {bank_account.BankCard.type_card}{BankCard.num_of_card} операция проведена успешно')


class CashMachine:
    def __init__(self, series_num, address):
        self.series_num = series_num
        self.address = address

    @staticmethod
    def switched_on(self):
        print('Банкомат включен!')

    @staticmethod
    def on_off(self):
        print('Банкомат выключен!')

    def pin(self):
        pass

    def take_many(self):
        pass

    def show_balance(self):
        pass
