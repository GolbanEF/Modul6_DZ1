from application.salary import calculate_salary
from application.db.pepole import get_employees
import datetime
if __name__ == '__main__':
    print("Все работает")
    calculate_salary()
    get_employees()
    print(datetime.datetime.today())

