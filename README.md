# Desafio-dev

Esta aplicação foi implementada em duas partes: um frontend feito em React que está implementado no seguinte diretório do projeto

```
frontend-react-desafio-dev
```

Também há um backend implementado em Django que está no seguinte diretório do projeto

```
backend-django-desafio-dev
```

# Instalação e utilização do backend

O backend está Dockerizado com as migrations e banco de dados atualizados. Para instalar o backend basta executar a partir da <b>raíz</b> do diretório do projeto o comando

```
sudo docker-compose up
```

Com isso todas as dependencias serão instaladas e o backend será executado automaticamente

<h2>Documentação da API do backend</h2>

<h4>Gravação de todas as transações a partir de um arquivo (POST /api/stores/transactions/)</h4>

Através dessa rota, enviamos um arquivo de texto com as informações de diversas lojas.

```sh
POST /api/stores/transactions/

REQUEST

file text/plain CNAB.txt

```

Será retornada um resposta de status 201 (CREATED) com as informações de todas as transações. Por exemplo

```sh
POST /api/stores/transactions/

RESPONSE 201 (CREATED)

[
  {
    "id": 1,
    "nome_loja": "BAR DO JOÃO",
    "dono_loja": "JOÃO MACEDO",
    "transacoes": [
      {
        "tipo": 3,
        "data": "20190301",
        "valor": 142.0,
        "cpf": "09620676017",
        "cartao": "4753****3153",
        "hora": "153453"
      },
      {
        "tipo": 2,
        "data": "20190301",
        "valor": 112.0,
        "cpf": "09620676017",
        "cartao": "3648****0099",
        "hora": "234234"
      },
      {
        "tipo": 1,
        "data": "20190301",
        "valor": 152.0,
        "cpf": "09620676017",
        "cartao": "1234****7890",
        "hora": "233000"
      }
    ]
  },
  {
    "id": 2,
    "nome_loja": "LOJA DO Ó - MATRIZ",
    "dono_loja": "MARIA JOSEFINA",
    "transacoes": [
      {
        "tipo": 5,
        "data": "20190301",
        "valor": 132.0,
        "cpf": "55641815063",
        "cartao": "3123****7687",
        "hora": "145607"
      },
      {
        "tipo": 1,
        "data": "20190301",
        "valor": 200.0,
        "cpf": "55641815063",
        "cartao": "1234****3324",
        "hora": "090002"
      },
      {
        "tipo": 9,
        "data": "20190301",
        "valor": 102.0,
        "cpf": "55641815063",
        "cartao": "6228****9090",
        "hora": "000000"
      }
    ]
  }
  ...
]

```

<h4>Criar um loja com transações cadastradas (POST /api/stores/)</h4>

Nesse endpoint podemos criar uma loja já com transações cadastradas como é possível ver no exemplo a seguir.

```sh

POST /api/stores/

REQUEST

{
  "nome_loja": "BAR DO JOÃO",
  "dono_loja": "JOÃO MACEDO",
  "transacoes": [
    {
      "tipo": 3,
      "data": "20190301",
      "valor": 142.0,
      "cpf": "09620676017",
      "cartao": "4753****3153",
      "hora": "153453"
    },
    {
      "tipo": 2,
      "data": "20190301",
      "valor": 112.0,
      "cpf": "09620676017",
      "cartao": "3648****0099",
      "hora": "234234"
    },
    {
      "tipo": 1,
      "data": "20190301",
      "valor": 152.0,
      "cpf": "09620676017",
      "cartao": "1234****7890",
      "hora": "233000"
    }
  ]
}

```

Se tudo ocorrer bem teremos uma resposta com status 201 (CREATED) retornando no corpo os dados da loja com as transações.

```sh

POST /api/stores/

RESPONSE 201

{
  "nome_loja": "BAR DO JOÃO",
  "dono_loja": "JOÃO MACEDO",
  "transacoes": [
    {
      "tipo": 3,
      "data": "20190301",
      "valor": 142.0,
      "cpf": "09620676017",
      "cartao": "4753****3153",
      "hora": "153453"
    },
    {
      "tipo": 2,
      "data": "20190301",
      "valor": 112.0,
      "cpf": "09620676017",
      "cartao": "3648****0099",
      "hora": "234234"
    },
    {
      "tipo": 1,
      "data": "20190301",
      "valor": 152.0,
      "cpf": "09620676017",
      "cartao": "1234****7890",
      "hora": "233000"
    }
  ]
}

```

Caso já exista uma loja com esse nome então é retornada uma resposta com status 409 (CONFLICT) com a mensagem

```sh

POST /api/stores/

RESPONSE 409

{
  "erro": "Essa loja já existe"
}

```

Caso algum campo esteja faltando será retornado status 400 (BAD REQUEST)

```sh

POST /api/stores/

RESPONSE 404

{
  "dono_loja": [
    "This field is required."
  ]
}

```

<h4>Exibir todas as lojas cadastradas no sistema (GET /api/stores/)</h4>

A requisição desse endpoint retorna todas as lojas cadastradas no sistema e retorna status 200 (OK). A seguir temos um exemplo de resposta.

```sh
GET /api/stores/

RESPONSE 200

[
  {
    "id": 1,
    "nome_loja": "BAR DO JOÃO",
    "dono_loja": "JOÃO MACEDO",
    "transacoes": [
      {
        "tipo": 3,
        "data": "20190301",
        "valor": 142.0,
        "cpf": "09620676017",
        "cartao": "4753****3153",
        "hora": "153453"
      },
      {
        "tipo": 2,
        "data": "20190301",
        "valor": 112.0,
        "cpf": "09620676017",
        "cartao": "3648****0099",
        "hora": "234234"
      },
      {
        "tipo": 1,
        "data": "20190301",
        "valor": 152.0,
        "cpf": "09620676017",
        "cartao": "1234****7890",
        "hora": "233000"
      }
    ]
  },
  {
    "id": 2,
    "nome_loja": "LOJA DO Ó - MATRIZ",
    "dono_loja": "MARIA JOSEFINA",
    "transacoes": [
      {
        "tipo": 5,
        "data": "20190301",
        "valor": 132.0,
        "cpf": "55641815063",
        "cartao": "3123****7687",
        "hora": "145607"
      },
      {
        "tipo": 1,
        "data": "20190301",
        "valor": 200.0,
        "cpf": "55641815063",
        "cartao": "1234****3324",
        "hora": "090002"
      },
      {
        "tipo": 9,
        "data": "20190301",
        "valor": 102.0,
        "cpf": "55641815063",
        "cartao": "6228****9090",
        "hora": "000000"
      }
    ]
  }
  ...
]
```

<h4>Adicionar uma transação a uma loja (POST /api/stores/id/transactions/)</h4>

Esse endpoint permite adicionar transações a lojas que já existem. A seguir temos um exemplo de requisição

```sh
POST /api/stores/1/transactions/

REQUEST

{
"transacoes": [
      {
        "tipo": 4,
        "data": "20210301",
        "valor": 100.5,
        "cpf": "09620676017",
        "cartao": "1234****5678",
        "hora": "201553"
      },
      {
        "tipo": 5,
        "data": "20210301",
        "valor": 75.0,
        "cpf": "09620676017",
        "cartao": "5678****1234",
        "hora": "114234"
      }
    ]
}
```

Como resposta temos os dados da loja com as com todas as transações adicionadas e as que já existiam. O status da resposta é 201 (CREATED)

```sh
POST /api/stores/1/transactions/

RESPONSE 201

{
  "id": 1,
  "nome_loja": "BAR DO JOÃO",
  "dono_loja": "JOÃO MACEDO",
  "transacoes": [
    {
      "tipo": 3,
      "data": "20190301",
      "valor": 142.0,
      "cpf": "09620676017",
      "cartao": "4753****3153",
      "hora": "153453"
    },
    {
      "tipo": 2,
      "data": "20190301",
      "valor": 112.0,
      "cpf": "09620676017",
      "cartao": "3648****0099",
      "hora": "234234"
    },
    {
      "tipo": 1,
      "data": "20190301",
      "valor": 152.0,
      "cpf": "09620676017",
      "cartao": "1234****7890",
      "hora": "233000"
    },
    {
      "tipo": 4,
      "data": "20210301",
      "valor": 100.5,
      "cpf": "09620676017",
      "cartao": "1234****5678",
      "hora": "201553"
    },
    {
      "tipo": 5,
      "data": "20210301",
      "valor": 75.0,
      "cpf": "09620676017",
      "cartao": "5678****1234",
      "hora": "114234"
    }
  ]
}

```

Caso a loja não exista teremos uma resposta com status 404 (NOT FOUND) com o seguinte corpo

```sh
POST /api/stores/1/transactions/

RESPONSE 404

{
  "erro": "Não há loja com essa id"
}
```

<h4>Exibir as transações de uma loja (GET /api/stores/id/transactions/)</h4>

Ao fazer uma requisição GET nesse endpoint, obtemos uma resposta de status 200 (OK) e é retornado no corpo os dados da loja selecionada e as transações como podemos ver a seguir

```sh
GET /api/stores/1/transactions/

RESPONSE 200
{
  "id": 1,
  "nome_loja": "BAR DO JOÃO",
  "dono_loja": "JOÃO MACEDO",
  "transacoes": [
    {
      "tipo": 3,
      "data": "20190301",
      "valor": 142.0,
      "cpf": "09620676017",
      "cartao": "4753****3153",
      "hora": "153453"
    },
    {
      "tipo": 2,
      "data": "20190301",
      "valor": 112.0,
      "cpf": "09620676017",
      "cartao": "3648****0099",
      "hora": "234234"
    },
    {
      "tipo": 1,
      "data": "20190301",
      "valor": 152.0,
      "cpf": "09620676017",
      "cartao": "1234****7890",
      "hora": "233000"
    }
  ]
}

```

Caso não exista loja com o id selecionado então é retornado uma resposta com status 404 (NOT FOUND)

```sh
GET /api/stores/1/transactions/

RESPONSE 404

{
  "erro": "Não há loja com essa id"
}
```

# Instalação e utilização do frontend

Primeiramente, para utilizar o frontend em React devemos instalar o npm e o nodeJS. Uma boa forma de instalar o npm e o nodeJS é instalando o nvm que permite instalar várias versões de ambos. Para isso basta seguir as instrução em

```sh
https://github.com/nvm-sh/nvm

```

Após isso, podemos instalar o gerenciador de pacote yarn que é utilizado nesse projeto. Para isso, após instalado o npm, basta rodar no terminal o comando

```sh
npm install --global yarn

```

Em seguida, podemos rodar o projeto indo pelo terminal até o diretório <b>frontend-react-desafio-dev</b> do projeto

Então, no terminal, para instalar todas as dependências do projeto frontend rodamos o comando

```
yarn
```

Depois que todas as dependências forem instaladas, basta digitar no terminal o comando para rodar a aplicação

```
yarn start
```

# Explorando a Aplicação Frontend

Ao entrar na página inicial da aplicação vemos um botão para selecionar o arquivo com as transações e outro para registrar as transações, como podemos ver a seguir

<p align="center">
  <img src="https://raw.githubusercontent.com/felipe16sm/desafio-dev/master/readme-images/Screenshot-from-2021-08-03-05-03-57.png" width="100%" title="Tela Inicial">
</p>

Após selecionar o arquivo com as transações, o nome do arquivo é mostrado

<p align="center">
  <img src="https://raw.githubusercontent.com/felipe16sm/desafio-dev/master/readme-images/Screenshot-from-2021-08-03-05-04-18.png" width="100%" title="Arquivo Selecionado">
</p>

Depois de clicar em registrar transações, somos redirecionados para a rota de lojas, onde são mostradas todas as lojas

<p align="center">
  <img src="https://raw.githubusercontent.com/felipe16sm/desafio-dev/master/readme-images/Screenshot-from-2021-08-03-05-04-32.png" width="100%" title="Lojas">
</p>

Então podemos clicar em uma loja para sermos redirecionados para a visualização das transações da

<p align="center">
  <img src="https://raw.githubusercontent.com/felipe16sm/desafio-dev/master/readme-images/Screenshot-from-2021-08-03-05-04-47.png" width="100%" title="Transações">
</p>

# Comandos úteis de docker

```
//Lista todos os containers ativos

sudo docker ps

-------------

//Entra no shell do container

sudo docker exec -it idcontainer /bin/bash

-------------

```

# Testes automatizados

```
//Roda testes automatizados e grava resultado em report.txt

TEST=TEST python manage.py test -v 2 &> report.txt
```
