import logging
from random import randint

from company import CompanyEmployeeWage

logging.basicConfig(filename="logfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class Companys:
    IS_FULL_TIME = 1
    IS_PART_TIME = 2

    def __init__(self):
        self.company = CompanyEmployeeWage()
        self.company_dic = dict()

    def input_from_user(self):
        """
        taking input from user
        :return: none
        """

        self.company.set_company_name(input("Enter the company "))
        logger.info("company name inserted")
        logger.info(f"{self.company.company_name}")
        self.company.set_num_of_working_days(int(input("Enter number of Working days in a month: ")))
        logger.info("Inserted total working days")
        self.company.set_max_hrs_in_month(int(input("Enter number of Working hours in a month: ")))
        logger.info("Inserted working hours")
        self.company.set_emp_rate_per_hour(int(input("Rate per hours: ")))
        logger.info("Inserted rate per hours")
        # company = CompanyEmployeeWage(company_name, input_working_days, input_working_hours, input_emp_rate)
        # print("\nTotal wages:", CompanyEmployeeWage.get_total_wage())
        self.company.set_total_wage(self.company.get_employee_wage())
        self.company_dic[self.company.company_name] = {
            "working_hours": self.company.get_max_hrs_in_month(),
            "working_days": self.company.get_num_of_working_days(),
            "rate_per_hour": self.company.get_emp_rate_per_hour(),
            "Total_wages": self.company.get_employee_wage()
        }
        # except Exception:
        #     print("Input error")
        #     logger.error("Input Error")
        # else:
        #     logger.info("No Error in input")

    def display(self,):
        """

        :param name:company name
        :return:company_dic 
        """
        logger.info(f"{self.company_dic}")
        print(self.company_dic)
        return self.company_dic
