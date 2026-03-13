# FLUXO DE CAIXA PESSOAL 


Sistema automatizado do meu fluxo de caixa, objetivo é vincular seu sonho material/pessoal com o seu fluxo de caixa atual, encontrando o melhor preço, nas melhores lojas e afins. 
Trazendo melhor conforto e organização pro seu bolso...

FLUXODECAIXA_PROJECT/
│
├── .venv/                  #  Local Python environment (isolated packages).
├── .env                    #  Secret vault for API keys and sensitive tokens.
├── .gitignore              #  Git safety filter (keeps junk and secrets out of the cloud).
├── requirements.txt        #  Project dependencies (Pandas, Streamlit, yFinance).
├── README.md               #  Project documentation and roadmap.
│
├── data/                   #  THE VAULT (Data Storage)
│   ├── raw/                # Unprocessed bank & meal voucher (VA) CSV files.
│   ├── financas.db         # Core SQLite database (The brain's permanent memory).
│   └── desejos.json        # Wishlist tracking with target price thresholds.
│
└── src/                    #  THE CORE (Source Code)
    ├── __init__.py         # Package initializer.
    ├── config.py           # Global settings, salary inputs, and budget limits.
    │
    ├── database/           #  STORAGE MANAGEMENT
    │   ├── connection.py   # Handles SQLite database handshake.
    │   ├── models.py       # DB Schema (Tables for Expenses, VA, and Investments).
    │   └── crud.py         # Business logic for Creating, Reading, and Updating data.
    │
    ├── core/               #  THE INTELLIGENCE ENGINE
    │   ├── etl_extratos.py # Data cleaning: sorts "Personal" vs "Meal Voucher" spend.
    │   ├── scraper.py      # Real-time price hunter for wishlist items.
    │   ├── investimentos.py# Asset tracker: pulls live stock and REIT (FII) data.
    │   └── gamificacao.py  #  The RPG Engine: converts cash into "Days of Life".
    │
    └── app/                # THE INTERFACE (Streamlit Frontend)
        ├── dashboard.py    # Main entry point (The "Days Remaining" progress bar).
        ├── forms.py        # Quick-entry sidebar for daily expenses.
        ├── views.py        # Tab management: RPG, Portfolio, and Deal Radar.
        └── utils.py        # UI helpers, currency formatting, and visual alerts.
