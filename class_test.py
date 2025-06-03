## Python test  
Section A


class Book:

    book_count = 0

    def __init__(self, title, author, year_published, genre):
        self.title = title
        self.author = author
        self.year_published = year_published
        self.year_published = year_published
        self.genre = genre
        Book.book_count += 1

    def get_info(self): 
        return f"{self.author}'s {self.genre} book titled {self.title} was pulblished in the  year {self.year_published}."
    
    def has_genre(self, genre):
      book_genre = input("Enter genre: ")
      if self.genre == book_genre:
            return True
      else:
            return False

book1 = Book("1984", "George Orwell", 1939, "Motivation")
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction")
book3 = Book("I will Marry when I want", "Ngugi wa Thiong'o", 1960, "Play")

print(book1.get_info()) 
print(f"Belongs to genre:{book1.has_genre('Motivation')}")
print(f"Total number of Books:{Book.book_count}") 



    
        
### Section B
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        return f"Name:{self.name}, Age:{self.age}, Salary:{self.salary}"
    
    def __str__(self):
        return f"[{self.name, self.age, self.salary}]"
    
    def __repr__(self):
        return self.__str__()
    

class Manager(Employee):
    def __init__(self, name, age, salary, team_size):
        super().__init__(name, age, salary)
        self.team_size = team_size

    def work(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Team_size: {self.team_size}"
    
class Developer(Employee):
    def __init__(self, name, age, salary, language):
        super().__init__(name, age, salary)
        self.language = language

    def code(self):
        return f"Developer {self.name} is experienced in {self.language}"
employee1 = Employee("Emmanuel", 23, 123099)
print(employee1.work())

management1 = Manager("Emmanuel", 23, 34000, 5)
print(management1.work())

dev1 = Developer("Emmanuel", 23, 34000, "PHP")
print(dev1.code())

employee_list = [employee1, management1, dev1]
for employee in employee_list:
    print(employee)



    def calculate_total_salary():
        total_salary = 0
        for item in employee_list:
            if item == employee.salary:
                total_salary += employee.salary
                print(f"Total Employee salary:{total_salary}")
print(calculate_total_salary())


## Section D
class BankAccount:
  def __init__(self, user, balance = 0):
    self.user = user
    self.balance = balance
  
  def deposit(self, amount):
    self.balance += amount
    print(f"You have successfully deposited {amount}, your new balance is {self.balance}.")

  def withdrawal(self, amount):
    if amount > self.balance:
      print(f"You do not have enough balance to withdraw{amount}")
    else:
      self.balance -= amount
      print(f"You have successfully withdrew {amount}, new balance {self.balance}")

  def get_balance(self):
    return f"your bank balance is {self.balance}"

acc = BankAccount("Emmanuel")
acc.deposit(200000)
acc.withdrawal(15000)
acc.get_balance()

new_deposit = [50000, 30000, 20000, 15000, 10000]
new_withdrawal =[55000, 70000, 25000]

for amount in new_deposit:
  acc.deposit(amount)

for amount in new_withdrawal:
  acc.withdrawal(amount)

class Cart:
  def __init__(self):
    self.shopping = dict()

  def add_item(self, name, qty):
    self.shopping[name] = qty
    return f"{qty} {name}'(s) successfully added "

  def remove_item(self, name):
    self.shopping.pop(name)

  def total_items (self):
    for item in self.shopping.items():
      print(item)

cart = Cart()
cart.add_item("Soap", 2)
cart.add_item("Bread", 3)
cart.add_item("Apple", 4)
cart.add_item("Bathing Soap", 2)

cart.remove_item("Soap")

cart.total_items()
class School:
    def __init__(self, *names):
        self.names = names

    def enroll_students(self):
        return f"{self.names} successfully added"

    def longest_name_loop(self):
        longest = ""
        for name in self.names:
            if len(name) > len(longest):
                longest = name
        return longest


    def student_list(self):
        student_names = []
        for name in self.names:
            student_names.append(name)

        return student_names
    
    def student_check(self, name):
        if name not in self.names:
            print("Student doesn't exist")
        else:
            print("student exists")

school_student1 = School("Emmanuel Kiriinya", "Alice Johnson", "Brian Smith", "Christopher Montgomery")


print(school_student1.enroll_students())
print("Longest name:", school_student1.longest_name_loop())

print(school_student1.student_list())

school_student1.student_check("Kiriinya Emmanuel")