# FLUXO DE CAIXA PESSOAL 


Sistema automatizado do meu fluxo de caixa, objetivo é vincular seu sonho material/pessoal com o seu fluxo de caixa atual, encontrando o melhor preço, nas melhores lojas e afins. 
Trazendo melhor conforto e organização pro seu bolso...

```text
fluxodecaixa_project/
│
├── .env                    # Variáveis de ambiente e segredos
├── .gitignore             # Arquivos temporários, venv, etc.
├── requirements.txt       # Dependências Python
├── README.md              # Documentação e roadmap
│
├── data/
│   ├── raw/               # Extratos brutos (OFX, CSV, PDF etc.)
│   └── financas.db        # Banco de dados principal (SQLite)
│
└── src/
    │
    ├── ingestion/
    │   ├── __init__.py
    │   ├── readers/
    │   │   ├── __init__.py
    │   │   ├── base.py         # Leitor genérico / abstrato
    │   │   ├── ofx_reader.py   # Leitura de extrato OFX
    │   │   ├── csv_reader.py   # Leitura de CSV
    │   │   └── pdf_reader.py   # Leitura de PDF (se entrar depois)
    │   ├── ingest.py          # Coordena a ingestão (ex: processa raw → banco)
    │   └── cotacoes.py        # Pegar cotações de mercado (yFinance, B3 etc.)
    │
    ├── database/
    │   ├── __init__.py
    │   ├── connection.py      # Conexão com SQLite
    │   ├── table.py           # Definição das tabelas (flow, investment, wishes)
    │   └── crud.py            # Insert, select, update de dados
    │
    ├── transform/
    │   └── .gitkeep           # Futura pasta para transformações (dbt, etl, etc.)
    │
    ├── api/
    │   ├── __init__.py
    │   └── main.py            # API FastAPI raiz (vai expor endpoints)
    │
    └── app/                   # (Futuro) Frontend / app que consome a API
        └── .gitkeep           # Frontend ainda não implementado
