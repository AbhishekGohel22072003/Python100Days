class Waiter:  #Class name in PascalCase
    is_holding_plate = True
    tables_responsible = [4, 5, 6]

    def take_order(self, table, order):
        pass

    def take_payment(self, amount):
        pass


# WAITER is a model(blueprint) using which is common/same for the waiters(objects) Yash and Viram
# This blueprint is called CLASS


'''IMP'''
# Object is actual thing we use in our code.