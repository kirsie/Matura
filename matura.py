import sys
import getopt
from data import Data
from results import Results


def main(argv):

    long_option_list = ['plec=', 'srednia=',
                        'zdawalnosc', 'najlepsze=',
                        'regresja', 'wojewodztwo=']
    try:
        options, args = getopt.getopt(argv, 'p:s:zn:rw:x:y:', long_option_list)
    except getopt.GetoptError as err:
        print(err)
        options = []

    cmd_args_dic = {}

    for opt, arg in options:
        if opt in ('-p', '--plec'):
            cmd_args_dic['gender'] = arg
        if opt in ('-s', '--srednia'):
            cmd_args_dic['average'] = arg
        if opt in ('-z', '--zdawalnosc'):
            cmd_args_dic['pass_rate'] = ''
        if opt in ('-n', '--najlepsze'):
            cmd_args_dic['best'] = arg
        if opt in ('-r', '--regresja'):
            cmd_args_dic['regression'] = ''
        if opt in ('-w', '--wojewodztwo'):
            cmd_args_dic['state'] = arg
        if opt in '-x':
            cmd_args_dic['state1'] = arg
        if opt in '-y':
            cmd_args_dic['state2'] = arg

    data = Data()
    Results(data.data_dicts, cmd_args_dic)


if __name__ == "__main__":
    main(sys.argv[1:])
