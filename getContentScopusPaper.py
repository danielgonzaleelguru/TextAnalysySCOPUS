import httpx 
import time
import xml.etree.ElementTree as ET
from xml.dom.minidom import parse
import xml.dom.minidom


def scopus_paper_date(paper_doi,apikey):
    apikey=apikey
    headers={
        "X-ELS-APIKey":apikey,
        "Accept":'text/xml'
         }

    timeout = httpx.Timeout(10.0, connect=60.0)
    client = httpx.Client(timeout=timeout,headers=headers)
    query="&view=FULL"    
    url=f"https://api-elsevier-com.biblioteca.unimagdalena.edu.co/content/article/doi/10.1016/j.ibusrev.2010.09.002"
    r=client.get(url)   
    return r.text

y = scopus_paper_date('10.3390/su11226248',"56c99a76116facd7f462f42ef0ece786")
print(y)