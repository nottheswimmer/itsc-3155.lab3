class Invoice:
    def __init__(self):
        self.items = {}

    def addProduct(self, qnt, price, discount):
        self.items.update({'qnt': qnt, 'unit_price': price, 'discount': discount})
        return self.items

    # def totalImpurePrice(self, products):
    #     return round(sum(float(v['unit_price'] * int(v['qnt'])) for v in products.values()), 2)

    def totalImpurePrice(self, products):
        total_impure_price = 0
        for k, v in products.items():
            total_impure_price += float(v['unit_price']) * int(v['qnt'])
        total_impure_price = round(total_impure_price, 2)
        return total_impure_price

    def totalPurePrice(self, products):
        total_pure_price = self.totalImpurePrice(products) - self.totalDiscount(products)
        return total_pure_price

    def totalDiscount(self, products):
        return round(sum(float(v['unit_price'] * int(v['qnt']) * float(v['discount'])) / 100
                         for v in products.values()), 2)

    def inputAnswer(self, input_value):
        while True:
            userInput = input(input_value)
            if userInput in ['y', 'n']:
                return userInput
            print("y or n! Try again.")

    def inputNumber(self, input_value):
        while True:
            try:
                userInput = float(input(input_value))
            except ValueError:
                print("Not a number! Try again.")
                continue
            else:
                return userInput
