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


def get_employee_wage():

    """

    :return: 
    """
    emp_hour = 0
    emp_wage = 0
    is_present = randint(0, 2)
    if is_present == IS_FULL_TIME:
        emp_hour = 8
    elif is_present == IS_PART_TIME:
        emp_hour = 4
    else:
        emp_hour = 0
    emp_wage = emp_hour * EMP_RATE_PER_HOUR
    logger.info(emp_wage)


if __name__ == '__main__':
    logging.info("UC3")
    get_employee_wage()