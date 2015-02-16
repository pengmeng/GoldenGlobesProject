__author__ = 'mengpeng'
from cli import CLI
"""
Main entrance of the project
"""

if __name__ == '__main__':
    cli = CLI('Golden Golbes Project')
    subcli = CLI('Sub menu')
    cli.register('test func', cli.samplefunc, '1', 'test1')
    cli.register('show nominees', cli.samplefunc, '2', 'test2')
    cli.register('sub menu', subcli.show)
    cli.exitcomm('q')
    subcli.register('sub test', subcli.samplefunc, '1', 'test1')
    subcli.exitcomm('s')
    cli.show()