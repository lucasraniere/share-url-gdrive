import pandas as pd
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

g_auth = GoogleAuth()
g_auth.LocalWebserverAuth()

drive = GoogleDrive(g_auth)

FOLDER_ID = ''
query = "'{}' in parents and trashed=false".format(FOLDER_ID)
PERMISISONS = {
    'type': 'anyone',
    'value': 'anyone',
    'role': 'reader'
}

def main():
    record = []
    file_list = drive.ListFile({'q': query}).GetList()
    for file in file_list:
        file.InsertPermission(PERMISISONS)
        record.append({'title': file['title'], 'link' : file['alternateLink']})
    df = pd.DataFrame.from_records(record)
    df.to_csv('file_list.csv', index=False)


if __name__ == '__main__':
    main()
