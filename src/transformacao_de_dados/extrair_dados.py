import pdfplumber
import pandas as pd
import zipfile
import os

# Caminho do PDF e pasta para salvar os CSVs
pdf_path = "src/web_scraping/Anexo_I_Rol.pdf"
csv_folder = "src/transformacao_de_dados/tabelas_extraidas/"
zip_output = "src/transformacao_de_dados/tabelas.zip"

# Criar a pasta para salvar os CSVs, se não existir
os.makedirs(csv_folder, exist_ok=True)

# Extração de tabelas do PDF
with pdfplumber.open(pdf_path) as pdf:
    tabelas = [pd.DataFrame(t) for p in pdf.pages for t in p.extract_tables()]

# Verifique se tabelas foram extraídas
if tabelas:
    # Salvar os CSVs individualmente (não zipados)
    for idx, tabela in enumerate(tabelas):
        # Substitui as abreviações pelas descrições completas
        tabela.replace({'OD': 'Seg. Odontológica', 'AMB': 'Seg. Ambulatorial'}, inplace=True)
        tabela_csv = os.path.join(csv_folder, f"tabela_{idx + 1}.csv")
        tabela.to_csv(tabela_csv, index=False, header=True)
        print(f"Tabela {idx + 1} salva em: {tabela_csv}")
    
    # Criar um arquivo ZIP com todos os CSVs
    with zipfile.ZipFile(zip_output, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Adiciona os arquivos CSV ao ZIP
        for csv_file in os.listdir(csv_folder):
            if csv_file.endswith('.csv'):
                file_path = os.path.join(csv_folder, csv_file)
                zipf.write(file_path, arcname=csv_file)
                print(f"Adicionando {csv_file} ao arquivo ZIP.")
        print(f"CSV zipado em: {zip_output}")
else:
    print("Nenhuma tabela encontrada no PDF.")

