__author__ = 'mengpeng'
from collections import OrderedDict


class CLI(object):

    def __init__(self, description='Default Menu'):
        self.description = description
        self.menu = OrderedDict({'description': description})
        self.menu['exit'] = 'exit'

    def register(self, name, func, *args):
        self.menu[str(len(self.menu) - 1)] = (name, func, args)

    def exitcomm(self, comm):
        self.menu['exit'] = comm

    def show(self):
        self._print()
        while self.execfunc():
            self._print()

    def _print(self):
        for k, v in self.menu.iteritems():
            if k is 'description':
                print('\n' + v)
                print('-'*len(v))
            elif k is not 'exit':
                print('{0}:   {1}'.format(k, v[0]))
        print('{0}:   to exit menu'.format(self.menu['exit']))

    def execfunc(self):
        num = raw_input('Please enter menu #: ')
        if num == self.menu['exit']:
            #print('Exiting...')
            return False
        if num in self.menu:
            self.menu[num][1](*self.menu[num][2])
        else:
            print('#{0} is not in the menu.'.format(num))
        return True

    def samplefunc(self, num, name):
        print('#{0} is selected and {1} is executed.'.format(num, name))


if __name__ == '__main__':
    cli = CLI('Test menu')
    cli.register('test function', cli.samplefunc)
    cli.register('show selected', cli.samplefunc)
    cli.show()