

class Results:

    data_dicts = []

    def __init__(self, data, conditions):
        self.data_dicts = data
        self.check_conditions(conditions)

    def check_conditions(self, conditions):

        if 'gender' in conditions.keys():
            if conditions['gender'] == 'm':
                conditions['gender'] = 'mężczyźni'
            elif conditions['gender'] == 'k':
                conditions['gender'] = 'kobiety'
            else:
                print("!!! zły argument płci !!!")
                conditions['gender'] = 'wszyscy'
        else:
            conditions['gender'] = 'wszyscy'

        if 'average' in conditions.keys():
            if 'state' in conditions.keys():
                self.count_average(int(conditions['average']), conditions['state'], conditions['gender'])

        if 'pass_rate' in conditions.keys():
            if 'state' in conditions.keys():
                self.count_pass_rate(conditions['state'], conditions['gender'])

    def count_average(self, year, state, gender):
        counter = 0
        denominator = year - 2009
        for dic in self.data_dicts:
            if dic['state'] == state and dic['year'] <= year and dic['mode'] == 'przystąpiło':
                if dic['gender'] == gender:
                    counter += dic['result']
                if gender == 'wszyscy':
                    counter += dic['result']
        average = int(counter/denominator)

        print(f'Srednia liczba przystępujących maturzystów dla:\n'
              f'Płeć: {gender}\n'
              f'Województwo: {state}\n'
              f'Lata: 2010-{year}\n'
              f'wynosi: {average}')

    def count_pass_rate(self, state, gender):
        pass_list = [0]*9
        students_list = [0]*9
        for dic in self.data_dicts:
            if dic['state'] == state and dic['mode'] == 'przystąpiło':
                if dic['gender'] == gender:
                    index = dic['year'] - 2010
                    students_list[index] += dic['result']
                if gender == 'wszyscy':
                    index = dic['year'] - 2010
                    students_list[index] += dic['result']
            if dic['state'] == state and dic['mode'] == 'zdało':
                if dic['gender'] == gender:
                    index = dic['year'] - 2010
                    pass_list[index] += dic['result']
                if gender == 'wszyscy':
                    index = dic['year'] - 2010
                    pass_list[index] += dic['result']

        print(f'Średnia zdawalność dla:\n'
              f'Płeć: {gender}\n'
              f'Województwo: {state}')
        for i in range(len(pass_list)):
            pass_rate = int(round((100*pass_list[i]/students_list[i]), 0))
            print(f'Rok {i+2010}: {pass_rate}%')
