from datetime import datetime 

from application import salary
from application import people

if __name__ == '__main__':
    print(datetime.now())
    people.get_employees()
    salary.calculate_salary()
    
