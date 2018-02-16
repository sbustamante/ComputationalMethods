import requests
import io
from configparser import ConfigParser
'''
Based on:
http://stackoverflow.com/a/39225272
'''
cfg=ConfigParser()
cfg.optionxform=str
tmp=cfg.read('drive.cfg')
drive_file=cfg['FILES']

def load_drive_files_keys():
    cfg=ConfigParser()
    cfg.optionxform=str
    tmp=cfg.read('drive.cfg')
    return cfg['FILES']

    
def pandas_from_google_drive_csv(id,gss_sheet=0,gss_query=None):
    '''
    Read Google spread sheet by id.
    Options:
       gss_sheet=N : if in old format select the N-sheet
       gss_query=SQL_command: Filter with some SQL command
       example 
         SQL_command: 'select B,D,E,F,I where (H contains 'GFIF') order by D desc'
    '''
    import pandas as pd
    if not gss_query:
        url='https://docs.google.com/spreadsheets/d/%s/gviz/tq?tqx=out:csv&gid=%s' %(id,gss_sheet)
    else:
        url='https://docs.google.com/spreadsheets/d/%s/gviz/tq?tqx=out:csv&gid=%s&tq=%s' %(id,gss_sheet,gss_query)
    r=requests.get(url)
    if r.status_code==200:
        csv_file=io.StringIO(r.text) # or directly  with: urllib.request.urlopen(url)
        return pd.read_csv( csv_file,keep_default_na=False)

def download_file_from_google_drive(id,destination=None,binary=True):
    '''
    Download file from google drive as binary (default) or txt file.
    If not destination the file object is returned
    Example: Let id="XXX" a txt file:
    1) fb=download_file_from_google_drive("XXX") ; fb.decode() #to convert to text file
    2) ft=download_file_from_google_drive("XXX",binary=False) # txt file
    3) fb=download_file_from_google_drive("XXX",'output_file') # always binay
    '''
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    
    return save_response_content(response, destination=destination,binary=binary)

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination=None,binary=True):
    CHUNK_SIZE = 32768

    if destination:
        f=open(destination, "wb") #binary file
    else:
        chunks=b''
    for chunk in response.iter_content(CHUNK_SIZE):
        if chunk: # filter out keep-alive new chunks
            if destination:
                f.write(chunk)
            else:
                chunks=chunks+chunk
    if destination:
        f.close()  #writes the file
    else:
        if binary:
            return io.BytesIO(chunks) # returns the file object
        else:
            return io.StringIO(chunks.decode()) # returns the file object
        
def read_drive_excel(file_name,**kwargs):
    '''Read excel from google drive
     Requieres a drive_file dictionary with the keys for the google drive
     file names.
     If the file_name is not found in the drive_file dictionary it is read locally.
     If the file_name have an extension .csv, tray to read the google spreadsheet 
     directly: check pandas_from_google_drive_csv for passed options
     WARNING: ONLY OLD Google Spread Sheet allows to load sheet different from 0
     '''
    import pandas as pd
    import re
    if re.search('\.csv$',file_name):
        if drive_file.get(file_name):
            return pandas_from_google_drive_csv(drive_file.get(file_name),**kwargs)
        else:
            return pd.read_csv(file_name,**kwargs)

    if drive_file.get(file_name):    
        return pd.read_excel( download_file_from_google_drive(
            drive_file.get(file_name) ) ,**kwargs)  # ,{} is an accepted option   
    else:
        return pd.read_excel(file_name,**kwargs)
    

def query_drive_csv(
    gss_url="https://spreadsheets.google.com",
    gss_format="csv",
    gss_key="0AuLa_xuSIEvxdERYSGVQWDBTX1NCN19QMXVpb0lhWXc",
    gss_sheet=0,
    gss_query="select B,D,E,F,I where (H contains 'GFIF') order by D desc",
    gss_keep_default_na=False
    ):
    import pandas as pd
    issn_url="%s/tq?tqx=out:%s&tq=%s&key=%s&gid=%s" %(gss_url,\
                                           gss_format,\
                                           gss_query,\
                                           gss_key,\
                                           str(gss_sheet))

    return pd.read_csv( issn_url.replace(' ','+') )