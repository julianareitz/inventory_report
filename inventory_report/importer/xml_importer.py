import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if ".xml" not in path:
            raise ValueError("Arquivo inválido")

        with open(path, "r") as file:
            content = xmltodict.parse(file.read())
            return content["dataset"]["record"]
