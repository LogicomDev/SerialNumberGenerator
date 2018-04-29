
from src.lsng.export.csv.csv_export import CSVHandler


class Exporter(object):
    '''
    classdocs
    '''

    def __init__(self, export_format, parent):
        if export_format == "csv":
            self.exporter = CSVHandler(parent)
        else:
            self.exporter = None

    def export_generation(self, generation_obj):
        filepath = self.exporter.export_generation(generation_obj)
        return filepath
