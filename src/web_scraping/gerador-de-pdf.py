import ftplib
import os

# Função para baixar arquivos do FTP
def baixar_arquivos_ftp():
    # Conexão com o FTP
    ftp = ftplib.FTP('dadosabertos.ans.gov.br')
    ftp.login()  # login anônimo

    # Definindo os diretórios de 2023 e 2024
    diretórios = ['2023', '2024']

    # Caminho do diretório onde os arquivos serão salvos
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_salvar = os.path.join(diretorio_atual, "arquivos_baixados")

    # Verifica se a pasta existe, se não, cria
    os.makedirs(caminho_salvar, exist_ok=True)

    # Baixando arquivos dos dois últimos anos
    for ano in diretórios:
        try:
            # Acessando o diretório do ano no FTP
            ftp.cwd(f'FTP/PDA/demonstracoes_contabeis/{ano}')
            
            # Listando arquivos disponíveis no diretório
            arquivos = ftp.nlst()  # Lista de arquivos no diretório atual
            print(f'Arquivos encontrados para o ano {ano}: {arquivos}')

            for arquivo in arquivos:
                # Caminho completo para salvar o arquivo localmente
                caminho_arquivo_local = os.path.join(caminho_salvar, arquivo)

                # Abrindo o arquivo local para escrever os dados
                with open(caminho_arquivo_local, 'wb') as f:
                    # Baixando o arquivo
                    ftp.retrbinary(f'RETR {arquivo}', f.write)

                print(f'Arquivo {arquivo} baixado com sucesso!')
        
        except ftplib.error_perm as e:
            print(f"Erro de permissão ao acessar o diretório {ano}: {e}")
    
    # Fechando a conexão com o FTP
    ftp.quit()

# Rodando a função para baixar os arquivos
baixar_arquivos_ftp()
