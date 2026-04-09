class AccountException(Exception):
    pass

class SingleBankAccount:
    def __init__(self):
        self.__account_number = 1111111111111111
        self.__account_balance = 6000
    
    @property
    def account_number(self):
        return self.__account_number
    
    @account_number.setter
    def account_number(self, new_value):
        raise AccountException("ALARM, you cannot change account_number")
    
    @property
    def account_balance(self):
        return self.__account_balance
    
    @account_balance.setter
    def account_balance(self, new_value):
        if (new_value < 0):
            raise AccountException("ALARM, you cannot set negative account_balance")
        
        if (abs(self.__account_balance - new_value) > 100000):
            print('operation above 100.000')

        self.__account_balance = new_value
        print('you changed balance to {}'.format(new_value))
    
    @account_balance.deleter
    def account_balance(self):
        if (self.__account_balance > 0):
            raise AccountException("ALARM, you cannot delete non zero account_balance")

        del self.__account_balance
        print('you delete account_balance')

single_bank_account = SingleBankAccount()

try:
    single_bank_account.account_balance = 1000
except Exception as e:
    print(e)

print('======================================')

try:
    single_bank_account.account_balance = -200
except Exception as e:
    print(e)

print('======================================')

try:
    single_bank_account.account_number = 000000000000000000000000
except Exception as e:
    print(e)

print('======================================')

try:
    single_bank_account.account_balance = single_bank_account.account_balance + 1000000
except Exception as e:
    print(e)    

print('======================================')

try:
    del single_bank_account.account_balance
except Exception as e:
    print(e)    

print('======================================')
