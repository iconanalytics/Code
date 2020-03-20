"""
This program assumes that there will be more results available that can be processed by the program
Therefore, out of index error is not a major concern when web scraping
"""



from googleapiclient.discovery import build   #Import the library


API_KEY = "AIzaSyAHFJi3FiHIvuM64a-Km5mqXExX0-C-dow"  
#api key from https://console.cloud.google.com/apis/credentials?folder=&organizationId=&project=pythonwebsearch 

CSE_ID = "011125311224649493392:r49ie4v4cav"

#custom search engine ID from https://cse.google.com/cse/setup/basic?cx=011125311224649493392%3Ar49ie4v4cav




class SearchConsole:
    def __init__(self,api_key=API_KEY,cse_id=CSE_ID):
        self.api_key = api_key
        self.cse_id = cse_id

        self.webmaster_service = build("webmasters", "v3", developerKey=api_key)  # custom search API from https://developers.google.com/resources/api-libraries/documentation/customsearch/v1/python/latest/customsearch_v1.cse.html


    def google_search(self,query,start_id=0):

        SERP_pages = []

        for SERP_page_number in range(MAX_SERP_PAGES): # we assume query returns at least 10 pages

            result_start_id = (SERP_page_number*10)   #result number 

            SERP_pages.append(self.query_service.cse().list(q=query,cx=self.cse_id,start=result_start_id).execute())

            import time
            time.sleep(5)

        return SERP_pages



def main():
    
    cs = CustomSearch()

    SERP_pages = cs.google_search("iconanalytics")

    count = 1

    for page_number in range (MAX_SERP_PAGES):
        for result_id in range (RESULT_PER_SERP_PAGE):
            result = SERP_pages[page_number]['items'][result_id]['link']
            print(str(count)+ "       "+result) # link for results found

            count = count+1
if __name__ == '__main__':
    main()



