def main():
    print("Welcome to the Salary Calculator")
    name = input("Please enter your name: ")
    while name == str(""):
        print("Sorry, you must enter your name.")
        name = input("Please enter your name: ")
    start_salary = int(input("Please enter your beginning salary: "))
    min_start_salary = 10000
    while start_salary <= min_start_salary:
        print("Sorry, your beginning salary must be at least 10000")
        start_salary = int(input("Please enter your beginning salary: "))
    years = int(input("Please enter the years worked: "))
    while years not in range(1, 11):
        print("Sorry, your years worked must be from 1 to 10.")
        years = int(input("Please enter the years worked: "))
    print("Thank you.")
    print("Your salary will be:")
    yearly_salary = start_salary
    for first in range(1, 2):
        print("Year {} : ${:.2f}".format(first, start_salary))
        for num in range(2, years + 1):
            raise_per_year = float(0.02)
            salary_increase = (yearly_salary * raise_per_year)
            yearly_salary += salary_increase
            print("Year {} : ${:.2f}".format(num, yearly_salary))


main()
