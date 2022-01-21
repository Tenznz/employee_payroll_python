import logging
from random import randint

logging.basicConfig(filename="logfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

IS_FULL_TIME = 1
IS_PART_TIME = 2
EMP_RATE_PER_HOUR = 20
NUM_OF_WORKING_DAYS = 20
MAX_HRS_IN_MONTH = 100


def get_employee_wage():

    """

    :return: 
    """
    emp_hour = 0
    emp_wage = 0
    total_hours = 0
    total_wage = 0
    for i in range(NUM_OF_WORKING_DAYS):
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
        if total_hours > MAX_HRS_IN_MONTH:
            break

        emp_wage = emp_hour * EMP_RATE_PER_HOUR
        total_wage = total_wage + emp_wage
    logger.info("Total wage below")
    logger.info(total_wage)
    print("total wage :-",total_wage)


if __name__ == '__main__':
    logging.info("UC6")
    get_employee_wage()
