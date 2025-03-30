CREATE TABLE operadoras_plano_saude (
    cnpj VARCHAR(18) PRIMARY KEY,            -- CNPJ da operadora (identificador único)
    razao_social VARCHAR(255) NOT NULL,      -- Razão social da operadora
    nome_fantasia VARCHAR(255),              -- Nome fantasia (opcional)
    modalidade VARCHAR(50),                  -- Modalidade (ex: Administradora de Benefícios)
    logradouro VARCHAR(255),                 -- Logradouro (endereço)
    numero VARCHAR(20),                      -- Número do endereço
    complemento VARCHAR(255),                -- Complemento do endereço
    bairro VARCHAR(100),                     -- Bairro
    cidade VARCHAR(100),                     -- Cidade
    uf CHAR(2),                              -- UF (estado) com 2 caracteres
    cep VARCHAR(10),                         -- CEP
    ddd VARCHAR(3),                          -- DDD
    telefone VARCHAR(20),                    -- Número de telefone
    fax VARCHAR(20),                         -- Número de fax (opcional)
    endereco_eletronico VARCHAR(255),        -- Endereço eletrônico (email)
    representante VARCHAR(255),              -- Nome do representante
    cargo_representante VARCHAR(100),        -- Cargo do representante
    regiao_comercializacao VARCHAR(50),      -- Região de comercialização
    data_registro_ans DATE                   -- Data do registro ANS
);

LOAD DATA INFILE 'C:/Users/Rennifer/Desktop/RENNIFER/PROJETOS EM BUSCA DO EMPREGO/src/banco_de_dados/banco_de_dados/Relatorio_cadop.csv'
INTO TABLE operadoras_plano_saude
FIELDS TERMINATED BY ','          -- Delimitador de campo (vírgula)
ENCLOSED BY '"'                  -- Caso os campos sejam delimitados por aspas (opcional)
LINES TERMINATED BY '\n'         -- Delimitador de linha (nova linha)
IGNORE 1 ROWS                    -- Ignora a primeira linha (cabeçalho)
(cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante, cargo_representante, regiao_comercializacao, data_registro_ans);  -- Mapeamento das colunas

