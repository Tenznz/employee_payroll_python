import logging
from random import randint

logging.basicConfig(filename="logfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

IS_FULL_TIME = 1
IS_PART_TIME = 2


class EmployeeWage:
    def __init__(self, max_days, max_hours, rate_per_hours):
        self.num_of_working_days = max_days
        self.max_hrs_in_month = max_hours
        self.emp_rate_per_hour = rate_per_hours

    def get_employee_wage(self):

        """

        :return:
        """
        emp_hour = 0
        emp_wage = 0
        total_hours = 0
        total_wage = 0
        logger.info("Checking presence and add wage accordingly")
        for i in range(self.num_of_working_days):
            is_present = randint(0, 2)
            switch = {
                1: 8,
                2: 4,
                0: 0
            }
            emp_hour = switch.get(is_present)
            total_hours = total_hours + emp_hour
            logger.info(total_hours)
            print("day-", i, "hours-", emp_hour)
            if total_hours > self.max_hrs_in_month:
                break

            emp_wage = emp_hour * self.emp_rate_per_hour
            total_wage = total_wage + emp_wage
        logger.info("Total wage below")
        logger.info(total_wage)
        print("total wage :-", total_wage)
        return total_wage


if __name__ == '__main__':
    logging.info("UC8")
    # company_name = input("Enter the company: ")
    # logger.info(company_name)
    max_working_days = int(input("Enter number of Working days in a month: "))
    logger.info("Inserted total working days")
    max_working_hours = int(input("Enter number of Working hours in a month: "))
    logger.info("Inserted working hours")
    emp_rate = int(input("Rate per hours: "))
    logger.info("Inserted rate per hours")
    employee1 = EmployeeWage(max_working_days, max_working_hours, emp_rate)
    print("\nTotal wages:", employee1.get_employee_wage())
    logger.info("program run successfully..!!")
