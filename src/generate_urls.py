import pandas as pd
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

g_auth = GoogleAuth()
g_auth.LocalWebserverAuth()

drive = GoogleDrive(g_auth)

FOLDER_ID = ''
SHARE_URL = 'https://drive.google.com/file/d/{}/view?usp=sharing'

query = "'{}' in parents and trashed=false".format(FOLDER_ID)

def main():
    record = []
    file_list = drive.ListFile({'q': query}).GetList()
    for file in file_list:
        record.append({'title': file['title'], 'link' : SHARE_URL.format(file['id'])})
    df = pd.DataFrame.from_records(record)
    df.to_csv('file_list.csv', index=False)

if __name__ == '__main__':
    main()
