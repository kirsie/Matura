import sys
import getopt
import os
from data import Data
from results import Results


def main(argv):

    long_option_list = ['plec=', 'srednia=',
                        'zdawalnosc', 'najlepsze=',
                        'regresja', 'wojewodztwo=',
                        'lokalne']
    try:
        options, args = getopt.getopt(argv, 'p:s:zn:rw:x:y:l', long_option_list)
    except getopt.GetoptError as err:
        print(err)
        options = []

    cmd_args_dic = {}
    local_data = False
    data = []

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

        # choose local or remote data
        if opt in ('-l', '--lokalne'):
            local_data = True
            if os.path.isfile('matura.db'):
                data = Data.load_from_local_db()
            else:
                data_obj = Data()
                data_obj.load_to_local_db()
                data = data_obj.load_from_local_db()

    if not local_data:
        data = Data().data_dicts

    Results(data, cmd_args_dic)


if __name__ == "__main__":
    main(sys.argv[1:])
