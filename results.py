from print_results import *


class Results:

    oldest_year = 2010
    newest_year = 2018
    data_dicts = []
    states = ['Pomorskie', 'Zachodniopomorskie',
              'Dolnośląskie', 'Mazowieckie',
              'Warmińsko-Mazurskie', 'Opolskie',
              'Podkarpackie', 'Łódzkie',
              'Podlaskie', 'Śląskie',
              'Świętokrzyskie', 'Wielkopolskie',
              'Małopolskie', 'Kujawsko-pomorskie',
              'Lubuskie', 'Lubelskie']

    def __init__(self, data, cmd_args_dic={}):
        self.data_dicts = data
        self.check_cmd_args(cmd_args_dic)

    def check_cmd_args(self, cmd_args_dic):

        if 'gender' in cmd_args_dic.keys():
            if cmd_args_dic['gender'] == 'm' or cmd_args_dic['gender'] == 'mężczyźni':
                cmd_args_dic['gender'] = 'mężczyźni'
            elif cmd_args_dic['gender'] == 'k' or cmd_args_dic['gender'] == 'kobiety':
                cmd_args_dic['gender'] = 'kobiety'
            else:
                cmd_args_dic['gender'] = 'wszyscy'
        else:
            cmd_args_dic['gender'] = 'wszyscy'

        if 'average' in cmd_args_dic.keys():
            if 'state' in cmd_args_dic.keys():
                self.count_average(int(cmd_args_dic['average']), cmd_args_dic['state'], cmd_args_dic['gender'])

        if 'pass_rate' in cmd_args_dic.keys():
            if 'state' in cmd_args_dic.keys():
                self.count_pass_rate(cmd_args_dic['state'], cmd_args_dic['gender'])

        if 'best' in cmd_args_dic.keys():
            self.count_best(int(cmd_args_dic['best']), cmd_args_dic['gender'])

        if 'regression' in cmd_args_dic.keys():
            self.count_regression(cmd_args_dic['gender'])

        if 'state1' in cmd_args_dic.keys() and 'state2' in cmd_args_dic.keys():
            self.compare_states(cmd_args_dic['gender'], cmd_args_dic['state1'], cmd_args_dic['state2'])

    def count_average(self, year, state, gender):
        counter = 0
        denominator = year - (self.oldest_year - 1)
        for dic in self.data_dicts:
            if dic['state'] == state and dic['year'] <= year and dic['mode'] == 'przystąpiło':
                if dic['gender'] == gender:
                    counter += dic['result']
                if gender == 'wszyscy':
                    counter += dic['result']
        average = int(counter/denominator)
        print_average(gender, state, year, average)
        return average

    def count_pass_rate(self, state, gender, year=None, mode='pass_rate'):
        number_of_years = self.newest_year - self.oldest_year + 1
        pass_list = [0]*number_of_years
        students_list = [0]*number_of_years
        pass_rate_list = [0]*number_of_years
        for dic in self.data_dicts:
            if dic['state'] == state and dic['mode'] == 'przystąpiło':
                if dic['gender'] == gender:
                    index = dic['year'] - self.oldest_year
                    students_list[index] += dic['result']
                if gender == 'wszyscy':
                    index = dic['year'] - self.oldest_year
                    students_list[index] += dic['result']
            if dic['state'] == state and dic['mode'] == 'zdało':
                if dic['gender'] == gender:
                    index = dic['year'] - self.oldest_year
                    pass_list[index] += dic['result']
                if gender == 'wszyscy':
                    index = dic['year'] - self.oldest_year
                    pass_list[index] += dic['result']
        for i in range(len(pass_list)):
            if students_list[i] != 0:
                pass_rate_list[i] = round((100 * pass_list[i] / students_list[i]), 2)

        if mode == 'pass_rate':
            print_pass_rate(gender, state, pass_rate_list)
            return pass_rate_list
        elif mode == 'best':
            index = year - self.oldest_year
            return pass_rate_list[index]
        elif mode == 'compare' or mode == 'regression':
            return pass_rate_list

    def compare_states(self, gender, state1, state2):
        pass_rate_state1 = self.count_pass_rate(state1, gender, mode='compare')
        pass_rate_state2 = self.count_pass_rate(state2, gender, mode='compare')
        result_dic = {}

        for i in range(len(pass_rate_state1)):
            if pass_rate_state1[i] > pass_rate_state2[i]:
                result_dic[str(i+self.oldest_year)] = state1
            elif pass_rate_state2[i] > pass_rate_state1[i]:
                result_dic[str(i+self.oldest_year)] = state2
            else:
                result_dic[str(i+self.oldest_year)] = 'Remis'
        print_compare(gender, state1, state2, result_dic)
        return result_dic

    def count_best(self, year, gender):
        best_result = ['', 0]
        for state in self.states:
            result = self.count_pass_rate(state, gender, year, mode='best')
            if result >= best_result[1]:
                best_result[0] = state
                best_result[1] = result
        print_best(gender, year, best_result)
        return best_result

    def count_regression(self, gender):
        results = []
        for state in self.states:
            pass_rate_list = self.count_pass_rate(state, gender, mode='regression')
            for i in range(len(pass_rate_list)-1):
                if pass_rate_list[i] > pass_rate_list[i+1]:
                    results.append((state, f'{i+self.oldest_year}->{i+self.oldest_year+1}'))
        print_regression(gender, results)
        return results
