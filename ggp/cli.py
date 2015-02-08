__author__ = 'mengpeng'
from collections import OrderedDict


class CLI(object):

    def __init__(self, description='Default Menu'):
        self.description = description
        self.menu = OrderedDict({'description': description})
        self.menu['exit'] = 'exit'

    def register(self, name, func):
        self.menu[str(len(self.menu) - 1)] = (name, func)

    def exitcomm(self, comm):
        self.menu['exit'] = comm

    def show(self):
        for k, v in self.menu.iteritems():
            if k is 'description':
                print(v)
            elif k is not 'exit':
                print('{0}:   {1}'.format(k, v[0]))
        print('{0}:   to exit program'.format(self.menu['exit']))
        return self.execfunc()

    def execfunc(self):
        num = raw_input('Please enter menu #: ')
        if num == self.menu['exit']:
            print('Exiting...')
            return False
        if num in self.menu:
            self.menu[num][1](num, self.menu[num])
        else:
            print('#{0} is not in the menu.'.format(num))
        return True

    def samplefunc(self, *args):
        print('#{0} is selected and {1} is executed.'.format(args[0], args[1][1]))


if __name__ == '__main__':
    cli = CLI('Test menu')
    cli.register('test function', cli.samplefunc)
    cli.register('show selected', cli.samplefunc)
    cli.show()