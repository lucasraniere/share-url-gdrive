# share-url-gdrive

## EN

This script creates a list of files and their respective public share URL links from a Google Drive folder.

First, download your credential JSON from the Google Cloud Console and place it in the same directory as the script. Then, edit the script to include the ID of the folder you want to list the files from.

Next, run the script with Python and log in via your browser.

Even if an error occurs after logging in, a CSV file will be created. If you run the script again, it will check the CSV and process the files that haven't been processed yet.

#### Dependences:
 - pandas
 - PyDrive2

## PT-BR

Este script cria uma lista de arquivos e seus respectivos links de compartilhamento público de uma pasta do Google Drive.

Primeiro, baixe seu arquivo JSON de credenciais do Google Cloud Console e coloque-o no mesmo diretório do script. Em seguida, edite o script para incluir o ID da pasta da qual você deseja listar os arquivos.

Depois, execute o script com Python e faça login pelo navegador.

Mesmo que ocorra um erro após o login, um arquivo CSV será criado. Se você executar o script novamente, ele verificará o CSV e processará os arquivos que ainda não foram processados.

### Dependências
  - pandas
  - PyDrive2
