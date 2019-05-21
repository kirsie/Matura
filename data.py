import requests
import urllib.request


class Data:
    data_dicts = []

    def __init__(self):
        self.csv_to_list_of_dict()

    def csv_to_list_of_dict(self):
        url = self.get_csv_link()
        csv = urllib.request.urlopen(url).read().decode('iso-8859-1')
        csv = self.parse_to_polish_chars(csv)
        data_all = csv.split('\r\n')
        data_list = []
        for line in data_all[1:]:
            data_list.append(list(line.split(';')))
        self.list_to_dict(data_list[:-1])

    def list_to_dict(self, data_list):
        for line in data_list:
            D = dict(zip(['state', 'mode', 'gender', 'year', 'result'], line))
            D['year'] = int(D['year'])
            D['result'] = int (D['result'])
            self.data_dicts.append(D)

    @staticmethod
    def get_csv_link():
        r = requests.get('https://api.dane.gov.pl/resources/17363')
        packages_json = r.json()
        csv_link = packages_json['data']['attributes']['link']
        return csv_link

    @staticmethod
    def parse_to_polish_chars(text):
        parser = [('³', 'ł'),
                  ('ê', 'ę'),
                  ('¿', 'ż'),
                  ('', 'ź'),
                  ('¹', 'ą'),
                  ('', 'ś'),
                  ('æ', 'ć'),
                  ('£', 'ł'),
                  ('ñ', 'ń'),
                  ('\x9c', 'ś')]
        for char in parser:
            text = text.replace(char[0], char[1])
        return text

