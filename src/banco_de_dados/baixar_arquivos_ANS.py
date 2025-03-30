import ftplib
import os
import requests

# Configuração do FTP
FTP_HOST = 'dadosabertos.ans.gov.br'
FTP_PATHS = {
    'demonstracoes_contabeis': 'FTP/PDA/demonstracoes_contabeis',
    'operadoras_ativas': 'FTP/PDA/operadoras_de_plano_de_saude_ativas'
}

# Diretório local para salvar os arquivos
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_salvar = os.path.join(diretorio_atual, "banco_de_dados")
os.makedirs(caminho_salvar, exist_ok=True)

def listar_diretorios_ftp(caminho):
    """Lista os diretórios disponíveis no servidor FTP."""
    try:
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login()
        ftp.cwd(caminho)
        diretorios = ftp.nlst()
        ftp.quit()
        return [d for d in diretorios if d.isdigit()]
    except ftplib.all_errors as e:
        print(f"Erro ao listar diretórios FTP ({caminho}): {e}")
        return []

def baixar_arquivos_ftp(caminho, anos=None):
    """Baixa arquivos do FTP."""
    try:
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login()
        ftp.cwd(caminho)
        if anos:
            for ano in anos:
                try:
                    ftp.cwd(f"{caminho}/{ano}")
                    arquivos = ftp.nlst()
                    for arquivo in arquivos:
                        baixar_arquivo_ftp(ftp, arquivo)
                    ftp.cwd("..")
                except ftplib.error_perm as e:
                    print(f"Erro ao acessar diretório {ano}: {e}")
        else:
            arquivos = ftp.nlst()
            for arquivo in arquivos:
                baixar_arquivo_ftp(ftp, arquivo)
        ftp.quit()
    except ftplib.all_errors as e:
        print(f"Erro ao conectar ao FTP: {e}")

def baixar_arquivo_ftp(ftp, arquivo):
    """Baixa um único arquivo do FTP."""
    caminho_arquivo = os.path.join(caminho_salvar, arquivo)
    with open(caminho_arquivo, 'wb') as f:
        ftp.retrbinary(f"RETR {arquivo}", f.write)
    print(f"Arquivo {arquivo} baixado com sucesso!")

def baixar_arquivos_http(base_url, anos=None):
    """Baixa arquivos via HTTP se o FTP falhar."""
    urls = [f"{base_url}/{ano}/exemplo.pdf" for ano in anos] if anos else [f"{base_url}/dados.csv"]
    for url in urls:
        nome_arquivo = os.path.basename(url)
        caminho_arquivo = os.path.join(caminho_salvar, nome_arquivo)
        resposta = requests.get(url)
        if resposta.status_code == 200:
            with open(caminho_arquivo, "wb") as f:
                f.write(resposta.content)
            print(f"Arquivo {nome_arquivo} baixado via HTTP!")
        else:
            print(f"Falha ao baixar {nome_arquivo}: Status {resposta.status_code}")

# Baixar Demonstrações Contábeis
anos_disponiveis = listar_diretorios_ftp(FTP_PATHS['demonstracoes_contabeis'])
if anos_disponiveis:
    anos_mais_recentes = sorted(anos_disponiveis, key=int, reverse=True)[:2]
    print(f"Os dois anos mais recentes são: {anos_mais_recentes}")
    baixar_arquivos_ftp(FTP_PATHS['demonstracoes_contabeis'], anos_mais_recentes)
else:
    print("Tentando baixar via HTTP...")
    baixar_arquivos_http('https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis', ['2024', '2023'])

# Baixar Dados Cadastrais das Operadoras Ativas
print("Baixando dados cadastrais das operadoras ativas...")
baixar_arquivos_ftp(FTP_PATHS['operadoras_ativas'])
