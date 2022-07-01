class Drug:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price


class Pharmacy:
    def __init__(self, name):
        self.name = name
        self.drugs = []
        self.employees = []

    def add_drug(self, drug):
        self.drugs.append(drug)

    def add_employee(self, first_name, last_name, age):
        self.employees.append({'first_name': first_name, 'last_name': last_name, 'age': age})

    def total_value(self):
        price = 0
        for drug in self.drugs:
            price += drug.amount * drug.price
        return price

    def employees_summary(self):
        res = []
        res.insert(0, 'Employees:\n')
        for i, emp in enumerate(self.employees):
            st = 'The employee number ' + str(i + 1) + ' is ' + emp['first_name'] + ' ' + emp['last_name'] + ' who is ' + str(emp['age']) + ' years old.\n'
            res.append(st)
        return ''.join(res)

                
drug1 = Drug("T1", 10, 1000)
drug2 = Drug("T2", 20, 2000)
drug3 = Drug("T3", 30, 3000)
store1 = Pharmacy('s1')
store1.add_drug(drug1)
store1.add_employee("Seyed Ali", "Babei", 15)
store1.add_employee("Seyed li", "Babae", 12)
store1.add_employee("Seyed Al", "Baaei", 14)
store1.add_employee("Seyed Ai", "Bbaei", 11)
print(store1.employees_summary())

    