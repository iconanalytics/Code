
from googlesearch import search
from data_saver import DataSaver
import datetime

log_file_name = 'C://Users//charles.fawole//Dropbox//Icon Analytics//Code//rank_log.csv'
header = "datetime,query,target,found?,index"
target = 'iconanalytics.com'

logger = DataSaver(log_file_name,header)

query = "icon analytics"

my_results_list = []
index = 0

query_time = (datetime.datetime.now())
found = False

for i in search(query,        # The query you want to run
                #tld = 'com',  # The top level domain
                #lang = 'en',  # The language
                num = 10,     # Number of results per page
                start = 0,    # First result to retrieve
                stop = None,  # Last result to retrieve
                pause = 2.0,  # Lapse between HTTP requests

               ):
    index = index +1

    out_res = str(index)+"       "+i                
    my_results_list.append(out_res)
    print(out_res)

    found = target in i
    if found:
        break


logger.log_entry(str(query_time)+","+query+","+target+","+str(found)+","+str(index))