# dodatkowa
import requests
import json
import csv
import urllib.request

class Data:

    def csv_to_list_of_sets(self):
        url = self.get_csv_link()
        csv = urllib.request.urlopen(url).read().decode('iso-8859-1')
        print(csv)



    @staticmethod
    def get_csv_link():
        r = requests.get('https://api.dane.gov.pl/resources/17363')
        packages_json = r.json()
        csv_link = packages_json['data']['attributes']['link']
        return csv_link





data = Data()
data.csv_to_list_of_sets()