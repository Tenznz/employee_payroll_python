import logging
from random import randint

from company import Company

logging.basicConfig(filename="logfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class EmployeeWage:
    IS_FULL_TIME = 1
    IS_PART_TIME = 2

    def __init__(self):
        self.company_dic = dict()

    def add_employee(self):
        """
        inserting employee details
        :return: none
        """
        employee_name = input("Enter your name: ")
        company_name = input("Enter the company: ")
        input_working_days = int(input("Enter number of Working days in a month: "))
        input_working_hours = int(input("Enter number of Working hours in a month: "))
        input_emp_rate = int(input("Rate per hours: "))
        self.company_dic[employee_name] = Company(company_name, input_working_days, input_working_hours,
                                                  input_emp_rate)

    def display(self):
        """
        employee
        :return: none
        """
        logger.info(f"{self.company_dic}")
        for employee in self.company_dic:
            print(employee)
            print(self.company_dic.get(employee).__str__())
            print(self.get_employee_wage(self.company_dic.get(employee)))

    def get_employee_wage(self, company):
        """

        :return:total_wage
        """
        total_hours = 0
        total_wage = 0

        logger.info("Checking presence and add wage accordingly")
        for i in range(company.num_of_working_days):
            logger.info("Enter in loop")
            is_present = randint(0, 2)
            switch = {
                1: 8,
                2: 4,
                0: 0
            }
            emp_hour = switch.get(is_present)
            total_hours = total_hours + emp_hour
            # print("day-", i, "hours-", emp_hour)
            if total_hours > company.max_hrs_in_month:
                break

            emp_wage = emp_hour * company.emp_rate_per_hour
            total_wage = total_wage + emp_wage
        logger.info("Total wage below")
        # logger.info(total_wage)
        print("total wage :-", total_wage)
        return total_wage
