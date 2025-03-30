-- Criação da tabela demonstracoes_contabeis
CREATE TABLE demonstracoes_contabeis (
    id INT AUTO_INCREMENT PRIMARY KEY,      -- ID único para cada registro
    ano INT NOT NULL,                       -- Ano de referência (exemplo: 2023)
    operadora VARCHAR(255) NOT NULL,        -- Nome da operadora de saúde
    cnpj VARCHAR(18) NOT NULL,              -- CNPJ da operadora
    valor_contabil DECIMAL(15, 2) NOT NULL, -- Valor contábil da operadora
    FOREIGN KEY (cnpj) REFERENCES operadoras_plano_saude(cnpj)  -- Relaciona com a tabela de operadoras
);

-- Habilitar local_infile, se necessário
SET GLOBAL local_infile = 1;

-- Importar dados para a tabela demonstracoes_contabeis
LOAD DATA INFILE 'C:/Users/Rennifer/Desktop/RENNIFER/PROJETOS EM BUSCA DO EMPREGO/src/banco_de_dados/banco_de_dados/Relatorio_cadop.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ','                  -- Delimitador de campo (vírgula)
ENCLOSED BY '"'                          -- Caso os campos sejam delimitados por aspas (opcional)
LINES TERMINATED BY '\n'                 -- Delimitador de linha (nova linha)
IGNORE 1 ROWS                            -- Ignora a primeira linha (cabeçalho)
(ano, operadora, cnpj, valor_contabil);   -- Mapeamento das colunas, com base na tabela
