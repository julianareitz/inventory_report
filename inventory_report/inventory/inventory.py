from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter

report = {"simples": SimpleReport, "completo": CompleteReport}


class Inventory:
    @classmethod
    def import_data(cls, filepath, report_type):
        if filepath.endswith(".csv"):
            product_list = CsvImporter.import_data(filepath)
        elif filepath.endswith(".json"):
            product_list = JsonImporter.import_data(filepath)
        elif filepath.endswith(".xml"):
            product_list = XmlImporter().read_xml_file(filepath)

        return report[report_type].generate(product_list)
