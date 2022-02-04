import logging

from employee_wage import EmployeeWage

logging.basicConfig(filename="logfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':

    company_obj = EmployeeWage()
    while True:
        user_choice = int(input("1.Add 2.Display 3.Exit"))
        choice = {
            1: company_obj.add_employee,
            2: company_obj.display,
            3: exit
        }
        choice.get(user_choice)()
