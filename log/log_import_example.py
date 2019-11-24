import logging

logging.basicConfig(filename='employ.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

        logging.info('Created Employee:{}-{}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


if __name__ == "__main__":
    emp_1 = Employee('John', 'Smith')
    emp_2 = Employee('Corey', 'Schafer')
