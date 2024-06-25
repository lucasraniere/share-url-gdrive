import os
import pandas as pd
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

g_auth = GoogleAuth()
g_auth.LocalWebserverAuth()

drive = GoogleDrive(g_auth)

FILE_NAME = 'arquivos_links.csv'
FOLDER_ID = '' # COLOQUE O ID DA PASTA <<<<
query = "'{}' in parents and trashed=false".format(FOLDER_ID)
PERMISISONS = {
    'type': 'anyone',
    'value': 'anyone',
    'role': 'reader'
}

def main():
    files = []
    record = []
    file_list = drive.ListFile({'q': query}).GetList()
    file_amount = len(file_list)
    if FILE_NAME in os.listdir():
        files = pd.read_csv(FILE_NAME)['title'].to_list()
    try:
        for idx, file in enumerate(file_list):
            if file['title'] not in files:
                print('Processando arquivo {} de {}...'.format(idx+1, file_amount))
                file.InsertPermission(PERMISISONS)
                record.append({'title': file['title'], 'link' : file['alternateLink']})
    finally:
        if files and record:
            df = pd.read_csv(FILE_NAME)
            df = pd.concat([df, pd.DataFrame.from_records(record)], ignore_index=True)
            df.to_csv(FILE_NAME, index=False)
        elif record:
            df = pd.DataFrame.from_records(record)
            df.to_csv(FILE_NAME, index=False)
        else:
            print('Nenhum arquivo novo encontrado.')


if __name__ == '__main__':
    main()
