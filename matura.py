import sys


def main(argv):
    for arg in argv:
        if arg in ('-s', '--srednia'):
            pass
        if arg in ('-z', '--zdawalnosc'):
            pass
        if arg in ('-n', '--najlepsze'):
            pass
        if arg in ('-r', '--regresja'):
            pass
        if arg in ('-p', '--porownaj'):
            pass
        if arg in ('-h', '--help'):
            print('Mozesz podac nastepujace argumenty: ...')


if __name__ == "__main__":
    main(sys.argv[1:])
