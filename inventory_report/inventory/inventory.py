from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter

report = {"simples": SimpleReport, "completo": CompleteReport}


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        if path.endswith(".csv"):
            product_list = CsvImporter.import_data(path)
        elif path.endswith(".json"):
            product_list = JsonImporter.import_data(path)
        elif path.endswith(".xml"):
            product_list = XmlImporter().import_data(path)

        return report[report_type].generate(product_list)
