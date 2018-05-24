import pyodbc
from filetools import Application
import abc

class Reader():

    READER_TYPES = []

    def __init__(self, filename):
        self.filename = filename
        if self.filename.endswith('accdb'):
            return MSAccessReader
        else:
            print ("File Type Unknown")

    @abc.abstractmethod
    def get_conn(self):
        """ Establish a connection to the File """

    @abc.abstractmethod
    def read_file(self):
        """ Read each line / record of the file """


class MSAccessReader(Reader):

    EXTENSION = '.accdb'

    def get_conn(self):
        conn_str = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ='+self.file+';'
            )
        with pyodbc.connect('conn_str') as cnxn:
            return cnxn.cursor()

class MSSQLReader(Reader):
    pass

class XLSXExcelReader(Reader):
    EXTENSION = '.xlsx'

    def get_conn(self):
        pass

    def read_file(self):
        pass

class FlatFileReader(Reader):
    def get_conn(self):
        pass

    def read_file(self):
        pass
