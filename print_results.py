def print_average(gender, state, year, average):
    print(f'Srednia liczba przystępujących maturzystów dla:\n'
          f'Płeć: {gender}\n'
          f'Województwo: {state}\n'
          f'Lata: 2010-{year}\n'
          f'wynosi: {average}')


def print_pass_rate(gender, state, pass_rate_list):
    print(f'Średnia zdawalność dla:\n'
          f'Płeć: {gender}\n'
          f'Województwo: {state}')
    for i in range(len(pass_rate_list)):
        print(f'Rok {i + 2010}: {pass_rate_list[i]}%')


def print_compare(gender, state1, state2, result_dic):
    print(f'Porównanie zdawalności województ: {state1} i {state2}\n'
          f'Płeć: {gender}')
    for year, state in result_dic.items():
        print(year, " -> ", state)


def print_best(gender, year, result):
    print(f'Najlepsza zdawalność dla:\n'
          f'Płeć: {gender}\n'
          f'Rok: {year}\n'
          f'{result[0]} {round(result[1], 2)}%')


def print_regression(gender, results):
    print(f'Płeć {gender}')
    for result in results:
        print(result[0], ': ', result[1])
