import csv

class FinanceManager:
    def __init__(self, filename='finance.csv'):
        self.filename = filename
        self.records = self.loading()

    # Reading a file
    def loading(self):
        try:
            with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                return list(reader)
        except FileNotFoundError:
            return []

    # Saving a new record
    def saving(self):
        with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(self.records)

    # Add new record
    def add_record(self, date, category, amount, description):
        if category == 1:
            self.records.append([date, 'income', amount, description])
        else:
            self.records.append([date, 'expense', amount, description])
        self.saving()

    # Edit existing record
    def editing(self, index, new_date, new_category, new_amount, new_description):
        if new_category == 1:
            self.records[index] = [new_date, 'income', new_amount, new_description]
        else:
            self.records[index] = [new_date, 'expense', new_amount, new_description]
        self.saving()

    def delete(self, index):
        del self.records[index]
        self.saving()

    def searching(self, search_term):
        return [record for record in self.records if search_term in record]

    def display_balance(self):
        balance = 0
        for record in self.records:
            if record[1] == 'income':
                balance += int(record[2])
            else:
                balance -= int(record[2])
        
        income = sum(int(record[2]) for record in self.records if record[1] == 'income')
        expense = sum(int(record[2]) for record in self.records if record[1] == 'expense')

        print(f"Current balance: {balance}")
        print(f"Total income: {income}")
        print(f"Total expenses: {expense}")

def main():

    finance_manager = FinanceManager()

    while True:
        print('')
        print("1. Show balance")
        print("2. Add record")
        print("3. Edit record")
        print("4. Delete record")
        print("5. Search records")
        print("6. Show records")
        print("7: Exit")
        choice = input("Select an action: ")
        print('')

        if choice == '1':
            finance_manager.display_balance()

        elif choice == '2':
            date = input("Date (yyyy-mm-dd): ")
            while True:
                category = int(input("Category: \n1: Income \n2: Expense\n "))
                if category==1 or category==2:
                    break
                else:
                    print("Please choose one of two options only!!!")
            amount = input("Amount: ")
            description = input("Description: ")
            finance_manager.add_record(date, category, amount, description)

        elif choice == '3':
            # show records before editing
            for i in range(len(finance_manager.loading())):
                print(i, finance_manager.loading()[i])

            index = int(input("Enter the index of the record to edit: "))
            new_date = input("New date (yyyy-mm-dd): ")
            while True:
                new_category = int(input("New category: \n1: Income \n2: Expense\n "))
                if new_category==1 or new_category==2:
                    break
                else:
                    print("Please choose one of two options only!!!")
            new_amount = input("New amount: ")
            new_description = input("New description: ")
            finance_manager.editing(index, new_date, new_category, new_amount, new_description)

        elif choice == '4':
            # show records before deleting
            for i in range(len(finance_manager.loading())):
                print(i, finance_manager.loading()[i])

            index = int(input("Enter the index of the record to delete: "))
            finance_manager.delete(index)

        elif choice == '5':
            search_term = input("Enter search term: ")
            results = finance_manager.searching(search_term)

            for result in results:
                print(result)

        elif choice == '6':
            for i in range(len(finance_manager.loading())):
                print(i, finance_manager.loading()[i])

        elif choice == '7':
            break

main()