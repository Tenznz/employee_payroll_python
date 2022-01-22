import logging
from random import randint

from company import CompanyEmployeeWage

logging.basicConfig(filename="logfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

IS_FULL_TIME = 1
IS_PART_TIME = 2
company = CompanyEmployeeWage()

def input_from_user():
    """
    taking input from user
    :return: none
    """

    company.set_company_name(input("Enter the company "))
    logger.info("company name inserted")
    # logger.info(company.company_name)
    company.set_num_of_working_days(int(input("Enter number of Working days in a month: ")))
    logger.info("Inserted total working days")
    company.set_max_hrs_in_month(int(input("Enter number of Working hours in a month: ")))
    logger.info("Inserted working hours")
    company.set_emp_rate_per_hour(int(input("Rate per hours: ")))
    logger.info("Inserted rate per hours")
    # company = CompanyEmployeeWage(company_name, input_working_days, input_working_hours, input_emp_rate)
    # print("\nTotal wages:", CompanyEmployeeWage.get_total_wage())
    company.set_total_wage(get_employee_wage())
    # except Exception:
    #     print("Input error")
    #     logger.error("Input Error")
    # else:
    #     logger.info("No Error in input")


def get_employee_wage():
    """

    :return:total_wage
    """
    total_hours = 0
    total_wage = 0

    logger.info("Checking presence and add wage accordingly")
    for i in range(company.get_num_of_working_days()):
        logger.info("Enter in loop")
        is_present = randint(0, 2)
        switch = {
            1: 8,
            2: 4,
            0: 0
        }
        emp_hour = switch.get(is_present)
        total_hours = total_hours + emp_hour
        print("day-", i, "hours-", emp_hour)
        if total_hours > company.get_max_hrs_in_month():
            break

        emp_wage = emp_hour * company.get_emp_rate_per_hour()
        total_wage = total_wage + emp_wage
    logger.info("Total wage below")
    # logger.info(total_wage)
    print("total wage :-", total_wage)
    return total_wage
