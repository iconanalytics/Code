
import os.path

class DataSaver:
    def __init__(self, log_file_name,header):
        if os.path.isfile(log_file_name):   # if file exists, open it to append data to it

            self.log_file = open(log_file_name, 'a')

        else: # create file since it does not already exist, and write the header

            self.log_file = open(log_file_name, 'w')
            self.log_entry(header)

    def log_entry(self,entry):

        self.log_file.write(entry+"\r")

    def close_file(self):

        self.log_file.close()


def main():
    log_file_name = 'C://Users//charles.fawole//Dropbox//Icon Analytics//Code//workfile.csv'
    header = "datetime,query,target,found?,index"
    ds = DataSaver(log_file_name,header)
    ds.log_entry("1")
    ds.log_entry("2")

main()