📊 MarketView

MarketView é um sistema web para visualização de cotações financeiras, incluindo ações brasileiras e internacionais, câmbio e carteira de ativos.
O projeto foi desenvolvido com foco em organização de código, boas práticas e escalabilidade.

🚀 Funcionalidades

📈 Consulta de ações da B3 e mercado internacional

💱 Visualização de câmbio (USD / BRL, EUR / BRL)

📊 Gráficos interativos com histórico de preços

⭐ Carteira de ativos personalizada

🎨 Interface web responsiva (HTML, CSS e JavaScript)

🛠 Tecnologias Utilizadas

Python 3

Flask

yfinance

Plotly

HTML5 / CSS3 / JavaScript

Git & GitHub

📂 Estrutura do Projeto
MARKETVIEW/
│
├── services/
│   ├── stocks.py        # Lógica de ações
│   ├── currency.py     # Lógica de câmbio
│   └── portfolio.py    # Carteira de ativos
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
│
├── templates/           # Templates HTML (Jinja2)
│
├── app.py               # Aplicação principal Flask
├── requirements.txt     # Dependências do projeto
├── README.md
└── .gitignore

▶️ Como Executar o Projeto
1️⃣ Clone o repositório
git clone https://github.com/SEU_USUARIO/MarketView.git
cd MarketView

2️⃣ Crie o ambiente virtual
python -m venv venv

3️⃣ Ative o ambiente virtual

Windows:

venv\Scripts\activate


Linux / macOS:

source venv/bin/activate

4️⃣ Instale as dependências
pip install -r requirements.txt

5️⃣ Execute a aplicação
python app.py


Acesse no navegador:

http://127.0.0.1:5000

🎯 Objetivo do Projeto

Este projeto foi desenvolvido com foco em aprendizado prático, organização de backend, integração com APIs financeiras e construção de dashboards web — ideal para portfólio em desenvolvimento web e Python.