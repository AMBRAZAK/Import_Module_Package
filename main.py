from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
from colorama import Fore, Style

if __name__=='__main__':
    print(Fore.RED + "Дата запуска:" + str(datetime.now().date()) + Style.RESET_ALL)
    calculate_salary()
    get_employees()