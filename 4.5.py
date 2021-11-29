'''Create a function showEmployee() in such a way that it should
accept the employee name and salary and display both. If the
salary is missing in function call, it should show Rs. 9000.'''
def show_Employee(name, salary=9000):
    # name = input()
    # salary = int(input())
    print(name, 'Employee has Rs.', salary, 'salary')


show_Employee('Jay', 1000)
show_Employee('hay')
