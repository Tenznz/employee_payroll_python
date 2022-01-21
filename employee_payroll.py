import logging
from random import randint

logging.basicConfig(filename="logfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

IS_FULL_TIME = 1
EMP_RATE_PER_HOUR = 20


def get_employee_wage():

    """

    :return: 
    """
    emp_hour = 0
    emp_wage = 0
    is_present = randint(0, 1)
    if is_present == IS_FULL_TIME:
        emp_hour = 8
    else:
        emp_hour = 0
    emp_wage = emp_hour * EMP_RATE_PER_HOUR
    logging.info(str(emp_wage))


if __name__ == '__main__':
    logging.info("UC2")
    get_employee_wage()