import logging
from random import randint

logging.basicConfig(filename="logfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class Company:
    # def __int__(self):
    #     pass

    # def __init__(self):
    #     self.company_name = ""
    #     self.num_of_working_days = 0
    #     self.max_hrs_in_month = 0
    #     self.emp_rate_per_hour = 0
    #     self.total_wage = 0
    def __init__(self, company_name, num_of_working_days, max_hrs_in_month, emp_rate_per_hour):
        self.company_name = company_name
        self.num_of_working_days = num_of_working_days
        self.max_hrs_in_month = max_hrs_in_month
        self.emp_rate_per_hour = emp_rate_per_hour
        self.total_wage = 0

    # # getter company name
    # def get_company_name(self):
    #     return self.company_name
    #
    # # setter company name
    # def set_company_name(self, company_name):
    #     self.company_name = company_name
    #
    # # getter working days
    # def get_num_of_working_days(self):
    #     return self.num_of_working_days
    #
    # # setter working days
    # def set_num_of_working_days(self, num_of_working_days):
    #     self.num_of_working_days = num_of_working_days
    #
    # # getter hours in month
    # def get_max_hrs_in_month(self):
    #     return self.max_hrs_in_month
    #
    # # setter hours in month
    # def set_max_hrs_in_month(self, max_hrs_in_month):
    #     self.max_hrs_in_month = max_hrs_in_month
    #
    # # getter rate per hour
    # def get_emp_rate_per_hour(self):
    #     return self.emp_rate_per_hour
    #
    # # setter rate per hour
    # def set_emp_rate_per_hour(self, emp_rate_per_hour):
    #     self.emp_rate_per_hour = emp_rate_per_hour
    #
    # # getter total wage
    # def get_total_wage(self):
    #     return self.total_wage
    #
    # # setter total wage
    # def set_total_wage(self, total):
    #     self.total_wage = total

    def __str__(self):
        return "companyname:" + self.company_name + ", max hrs in month:" + str(self.max_hrs_in_month) \
               + ", number of working days: " + str(self.num_of_working_days) + ", rate per hours: " \
               + str(self.emp_rate_per_hour)


