# API Rest com Flask - The Games

## Criar o ambiente virtual

```bash
python -m venv venv
```

## Ativar o ambiente virtual

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

```bash
venv/Scripts/activate
```

# Desativando o ambiente virtual

```bash
deactivate
```

# Exportando a lista de dependências

```bash
pip freeze > requirements.txt
```

# Instalando dependências do requirements

```bash
pip install -r requirements.txt
```

# Variáveis de ambiente no Flask

## Instalação
Instalar a biblioteca python-dotenv usando o pip:

```bash
pip install python-dotenv
```
## Utilização
Exemplo de como usar python-dotenv com Flask:

* Crie um arquivo .env no diretório raiz do seu projeto:

```bash
FLASK_APP=myapp
FLASK_ENV=development
SECRET_KEY=mysecretkey
DATABASE_URL=mongodb://localhost:27017/yourdbname
```

* Modifique o aplicativo Flask para carregar essas variáveis de ambiente:

```bash
from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os
```

* Carregar variáveis de ambiente do arquivo .env

```bash
load_dotenv()

app = Flask(__name__)
```

* Configurar a aplicação Flask usando as variáveis de ambiente
```bash
app.config["MONGO_URI"] = os.getenv("DATABASE_URL")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

mongo = PyMongo(app)

# Resto do código Flask...

if __name__ == "__main__":
    app.run()
```

### Explicação

* Arquivo .env: Contém suas variáveis de ambiente. Mantenha esse arquivo fora do controle de versão (adicione ao seu .gitignore).
* load_dotenv: Carrega as variáveis de ambiente do arquivo .env para o ambiente de execução do Python.
* os.getenv: Recupera os valores das variáveis de ambiente carregadas.
* Usar python-dotenv ajuda a manter suas configurações seguras e flexíveis, permitindo que você altere configurações facilmente sem modificar seu código fonte.

# MongoDB Atlas

## Instalação

```bash
pip install pymongo[srv]
```

_pip install pymongo[srv]: Esse comando instala a biblioteca principal do PyMongo juntamente com dependências adicionais necessárias para o uso do protocolo DNS SRV para conexão. O protocolo DNS SRV é utilizado para facilitar a conexão a clusters MongoDB, especialmente em ambientes gerenciados como o MongoDB Atlas. Basicamente, ele permite que você use strings de conexão DNS SRV, que são mais simples e automáticas na descoberta de servidores em um cluster._

### Em resumo:

* pip install pymongo instala apenas o pacote básico.
* pip install pymongo[srv] instala o pacote básico junto com dependências adicionais para suportar conexões com strings de conexão DNS SRV.
* Se você está planejando se conectar a um cluster MongoDB usando uma string de conexão SRV (como as fornecidas pelo MongoDB Atlas), é recomendado usar pip install pymongo[srv].