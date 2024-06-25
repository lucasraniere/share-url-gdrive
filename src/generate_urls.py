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
    file_amount = len(file_list)
    for idx, file in enumerate(file_list):
        print('Processando arquivo {} de {}...'.format(idx+1, file_amount))
        file.InsertPermission(PERMISISONS)
        record.append({'title': file['title'], 'link' : file['alternateLink']})
    df = pd.DataFrame.from_records(record)
    df.to_csv('file_list.csv', index=False)


if __name__ == '__main__':
    main()
