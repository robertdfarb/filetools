import argparse
import os

def add_args():

    '''Argument parser for taking arguments from the command line.
        This application can also be run using Python Interactive Shell
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('--gui', help='Optional GUI Interface to be included in a future release', action="store_true")
    parser.add_argument('-i', '--inputfile', help='Optional positional argument for the import file or directory')
    parser.add_argument('-t', '--inputtype', help='Optional positional argument for the file type format for forcing the processing of the file. \
                                                   using a specific type.  Note that default')
    parser.add_argument('-ext', help='Optional keyword argument argument to limit the extensions searched')
    parser.add_argument('--log', help='Creates an optional load log which tracks files and processed record counts', action="store_true")
    parser.add_argument('--r', help='Recursively reads all files in directory', action="store_true")
    parser.add_argument('--unzip', help='Process all files within archived formats', action="store_true")
    parser.add_argument('--archived', help='Process all files within archived formats', action="store_true")
    parser.add_argument('--print', help='Prints results to console', action="store_true")
    parser.add_argument('--combine', help='Create', action="store_true")
    parser.add_argument('-output_type', help='Selected method for for outputting file.  This will default to the original file type'\
                                                , choices =['SQL','MSAccess','XLSX', 'XLS', 'CSV','DELIMITED'])
    return parser.parse_args()

class Application:

    def __init__(self):
        self.args = add_args()

    files = []

    def add_files(self):
        if os.path.isdir(self.args.inputfile):
            if self.args.r:
                pass
            else:
                self.files = [f for f in os.listdir(self.args.inputfile)]

        elif os.path.isfile(self.args.inputfile):
            self.files.append(self.args.inputfile)
        elif os.path.isfile(os.path.join(os.getcwd(),self.args.inputfile)):
            print (os.getcwd())
            files = [os.path.join(os.getcwd(),self.args.inputfile)]
            print (files)
        else:
            print ("File not found")

if __name__ =='__main__':
    app = Application()
