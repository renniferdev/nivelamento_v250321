import os
from tkinter import filedialog
from zipfile import ZipFile, ZIP_DEFLATED

def compactar_tudo(diretorio, ignore_zips=True):
    """Compacta arquivos e pastas em um único ZIP dentro do diretório selecionado, excluindo o próprio script."""
    arquivos = os.listdir(diretorio)
    
    # Nome do próprio script para não ser incluído
    script_atual = os.path.basename(__file__)
    arquivo_a_nao_incluir = "gerador-de-pdf.py"

    # Filtrar os arquivos para excluir ZIPs (se necessário) e o próprio script
    arquivos = [fn for fn in arquivos if fn != script_atual and fn != arquivo_a_nao_incluir and (not ignore_zips or not fn.endswith('.zip'))]

    if not arquivos:
        print("Nenhum arquivo encontrado para compactação.")
        return 0

    zip_path = os.path.join(diretorio, "arquivos_compactados.zip")

    try:
        with ZipFile(zip_path, "w", ZIP_DEFLATED) as zip_arquivo:
            for nome in arquivos:
                fullpath = os.path.join(diretorio, nome)
                if os.path.isdir(fullpath):
                    for raiz, _, files in os.walk(fullpath):
                        for file in files:
                            arquivo_absoluto = os.path.join(raiz, file)
                            arquivo_relativo = os.path.relpath(arquivo_absoluto, diretorio)
                            zip_arquivo.write(arquivo_absoluto, arquivo_relativo)
                else:
                    zip_arquivo.write(fullpath, nome)

        print(f"Compactação concluída! Arquivo salvo em: {zip_path}")
        return len(arquivos)

    except Exception as e:
        print(f"Erro ao compactar arquivos: {e}")
        return 0

if __name__ == '__main__':
    pasta = filedialog.askdirectory(title="Selecione uma pasta para compactar")
    
    if not pasta:
        print("Nenhuma pasta selecionada.")
    else:
        print(f"Compactando arquivos em {pasta}...")
        n = compactar_tudo(pasta)
        print(f"{n} arquivos e pastas compactados com sucesso!")
