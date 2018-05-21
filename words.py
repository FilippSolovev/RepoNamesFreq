import json
import csv
from collections import Counter


class ExportJSON:
    def to_json(self, path='output.json'):
        with open(path, 'w') as json_file:
            json.dump(self.most_common(), json_file)


class ExportCSV:
    def to_csv(self, path='output.csv'):
        with open(path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerows(self.most_common())


class Words(Counter, ExportJSON, ExportCSV):
    def print_most_common(self, head=None):
        for word, occurence in super().most_common(head):
            print(word, occurence)
