import sys
import getopt
from data import Data
from results import Results


def main(argv):

    options, args = getopt.getopt(argv, 'p:s:zn:r:w:w1:w2:h')

    conditions = {}
    data = Data()

    for opt, arg in options:
        if opt in ('-p', '-plec'):
            conditions['gender'] = arg
        if opt in ('-s', '--srednia'):
            conditions['average'] = arg
        if opt in ('-z', '--zdawalnosc'):
            conditions['pass_rate'] = ''
        if opt in ('-n', '--najlepsze'):
            conditions['best'] = ''
        if opt in ('-r', '--regresja'):
            conditions['regression'] = ''
        if opt in ('-w', '--wojewodztwo'):
            conditions['state'] = arg
        if opt in ('-w1', '--wojewodztwo1'):
            conditions['state1'] = ''
        if opt in ('-w2', '--wojewodztwo2'):
            conditions['state2'] = ''

    results = Results(data.data_dicts, conditions)


if __name__ == "__main__":
    main(sys.argv[1:])
