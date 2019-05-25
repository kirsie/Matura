import requests
import urllib.request
import sqlite3


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
            d = dict(zip(['state', 'mode', 'gender', 'year', 'result'], line))
            d['year'] = int(d['year'])
            d['result'] = int (d['result'])
            self.data_dicts.append(d)

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
                  ('', 'Ś'),
                  ('æ', 'ć'),
                  ('£', 'Ł'),
                  ('ñ', 'ń'),
                  ('\x9c', 'ś')]
        for char in parser:
            text = text.replace(char[0], char[1])
        return text

    def load_to_local_db(self):
        conn = sqlite3.connect('matura.db')
        c = conn.cursor()

        c.execute("""CREATE TABLE matura (
                    state text,
                    mode text,
                    gender text,
                    year integer,
                    result integer
                    )""")
        for record in self.data_dicts:
            c.execute('INSERT INTO matura VALUES (?, ?, ?, ?, ?)', (record['state'],
                                                                    record['mode'],
                                                                    record['gender'],
                                                                    record['year'],
                                                                    record['result']))
        conn.commit()
        conn.close()

    @staticmethod
    def load_from_local_db():
        conn = sqlite3.connect('matura.db')
        c = conn.cursor()
        data_dicts = []
        c.execute('SELECT * FROM matura')
        for record in c.fetchall():
            data_dicts.append(dict(zip(['state', 'mode', 'gender', 'year', 'result'], list(record))))
        return data_dicts
