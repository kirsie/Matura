from data import Data
from results import Results

data_example = [{'state': 'Lubuskie', 'mode': 'przystąpiło', 'gender': 'kobiety', 'year': 2010, 'result': 24},
                {'state': 'Lubuskie', 'mode': 'przystąpiło', 'gender': 'mężczyźni', 'year': 2010, 'result': 48},
                {'state': 'Lubuskie', 'mode': 'zdało', 'gender': 'kobiety', 'year': 2010, 'result': 6},
                {'state': 'Lubuskie', 'mode': 'zdało', 'gender': 'mężczyźni', 'year': 2010, 'result': 6},
                {'state': 'Lubuskie', 'mode': 'przystąpiło', 'gender': 'mężczyźni', 'year': 2011, 'result': 50},
                {'state': 'Lubuskie', 'mode': 'przystąpiło', 'gender': 'kobiety', 'year': 2011, 'result': 40},
                {'state': 'Lubuskie', 'mode': 'zdało', 'gender': 'mężczyźni', 'year': 2011, 'result': 10},
                {'state': 'Lubuskie', 'mode': 'zdało', 'gender': 'kobiety', 'year': 2011, 'result': 5},
                {'state': 'Opolskie', 'mode': 'zdało', 'gender': 'wszyscy', 'year': 2011, 'result': 1},
                {'state': 'Pomorskie', 'mode': 'zdało', 'gender': 'wszyscy', 'year': 2011, 'result': 2},
                {'state': 'Opolskie', 'mode': 'przystąpiło', 'gender': 'wszyscy', 'year': 2011, 'result': 0},
                {'state': 'Pomorskie', 'mode': 'przystąpiło', 'gender': 'wszyscy', 'year': 2011, 'result': 2}]


def test_data_is_valid():
    data = Data()
    data_dicts = data.data_dicts
    valid = True
    for dic in data_dicts:
        for key in data_example[0].keys():
            if key in dic.keys():
                pass
            else:
                print(dic)
                valid = False
    assert valid is True


def test_count_average_all():
    results = Results(data_example)
    assert results.count_average(2011, 'Lubuskie', 'wszyscy') == 81


def test_count_average_gender():
    results = Results(data_example)
    assert results.count_average(2011, 'Lubuskie', 'kobiety') == 32


def test_count_pass_rate_all():
    results = Results(data_example)
    assert results.count_pass_rate('Lubuskie', 'wszyscy') == [16.67, 16.67, 0, 0, 0, 0, 0, 0, 0]


def test_count_pass_rate_gender():
    results = Results(data_example)
    assert results.count_pass_rate('Lubuskie', 'kobiety') == [25, 12.5, 0, 0, 0, 0, 0, 0, 0]


def test_compare_states():
    results = Results(data_example)
    compare_dict = dict.fromkeys(['2010', '2012', '2013',
                                  '2014', '2015', '2016',
                                  '2017', '2018'], 'Remis')
    compare_dict['2011'] = 'Pomorskie'
    assert results.compare_states('wszyscy', 'Opolskie', 'Pomorskie') == compare_dict


def test_count_best_state():
    results = Results(data_example)
    assert results.count_best(2011, 'wszyscy') == ['Pomorskie', 100]


def test_count_regression():
    results = Results(data_example)
    assert results.count_regression('kobiety') == [('Lubuskie', '2010->2011'),
                                                   ('Lubuskie', '2011->2012')]