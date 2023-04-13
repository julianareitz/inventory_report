import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if ".csv" not in path:
            raise ValueError("Arquivo inválido")

        with open(path, "r") as file:
            content = csv.DictReader(file, delimiter=",", quotechar='"')
            return list(content)
