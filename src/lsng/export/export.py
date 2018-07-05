
from src.lsng.export.csv.csv_export import CSVHandler
from PyQt5.QtWidgets import QFileDialog
import os


class Exporter(object):
    '''
    classdocs
    '''

    def __init__(self, export_format, parent):
        self.parent = parent
        self.basefolder = os.path.join(parent.basefolder, "Traceability")
        if export_format == "csv":
            self.exporter = CSVHandler(parent)
        else:
            self.exporter = None

    def export_generation(self, generation_obj, seperator):
        """
        Here's where the magic happens
        """
        if not os.path.isdir(self.basefolder):
            # Create Traceability Folder (if not existing)
            os.mkdir(self.basefolder)
        
        # Folder should be : /Traceability/Supplier/Model/POxxxx/
        currentfolder = os.path.join(self.basefolder, generation_obj.supplier.name, generation_obj.device.name, "PO{}".format(generation_obj.po_number))
        os.makedirs(currentfolder, exist_ok=True)
        
        filename = os.path.join(currentfolder, "PO{}_{}_{}_{}_{}.{}".format(generation_obj.po_number, generation_obj.supplier.name,
                                                                       generation_obj.device.name, generation_obj.color,
                                                                       generation_obj.qty, self.exporter.file_extension))
        print(filename)
        
        while not filename or os.path.isfile(filename):
            # What to do when the file already exists ?
            print("filename already exists. User must change name.")
            filename, chosen_filter = QFileDialog.getSaveFileName(self.parent, "Select a new file name", currentfolder, "*.csv")
            print(filename, chosen_filter)
        
        self.exporter.export_generation(filename, generation_obj, seperator)
        
        return filename
