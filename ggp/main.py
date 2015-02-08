__author__ = 'mengpeng'
from cli import CLI
"""
Main entrance of the project
"""

if __name__ == '__main__':
    cli = CLI('Golden Golbes Project')
    cli.register('test func', cli.samplefunc)
    cli.register('show nominees', cli.samplefunc)
    cli.exitcomm('q')
    while cli.show():
        pass