# 💰 FaucetCoin - Sistema de Recompensas com Flask

Este projeto é um site estilo [FaucetCrypto](https://faucetcrypto.com), onde usuários podem registrar-se, fazer login, reivindicar recompensas periódicas e ganhar bônus por indicar amigos. O backend é construído com **Flask** e o visual com **Bootstrap 5**.

## 🧩 Funcionalidades

- Autenticação de usuários (registro/login/logout)
- Sistema de recompensas (faucet)
- Sistema de níveis e XP
- Indicação com código de referência
- Histórico de transações
- Solicitação de saque
- Painel de usuário com Bootstrap 5

## 🚀 Como rodar o projeto

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/faucetcoin.git
   cd faucetcoin
   ```

2. **Crie um ambiente virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate   # Windows
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados**:
   ```bash
   flask db init
   flask db migrate -m "Inicial"
   flask db upgrade
   ```

5. **Inicie a aplicação**:
   ```bash
   flask run
   ```

## 🛠️ Tecnologias Usadas

- Python + Flask
- Flask-Login
- Flask-Migrate
- SQLite (padrão) ou MySQL (opcional)
- Bootstrap 5

## 📄 Licença

MIT License - fique à vontade para usar, melhorar e compartilhar!
