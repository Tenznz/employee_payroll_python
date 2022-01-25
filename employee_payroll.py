import logging

from operation import Companys

logging.basicConfig(filename="logfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

EXIT = 3


def exit_choice():
    return "exit"


if __name__ == '__main__':
    logging.info("UC10")
    company_obj = Companys()
    while True:
        user_choice = int(input("1.Add 2.Display 3.Exit"))
        choice = {
            1: company_obj.input_from_user,
            2: company_obj.display,
            EXIT: exit_choice
        }

        if choice.get(user_choice)() == "exit":
            break
