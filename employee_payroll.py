import logging

from operation import input_from_user

logging.basicConfig(filename="logfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def exit_choice():
    return "exit"


if __name__ == '__main__':
    logging.info("UC10")
    while True:

        user_choice = int(input("1.Add 2.Exit"))
        choice = {
            1: input_from_user,
            2: exit_choice
        }
        if choice.get(user_choice)() == "exit":
            break

