# CineInfo

Uma aplicação FastAPI que busca informações sobre filmes usando a API do Google Gemini.

## Funcionalidades

- Buscar informações de filmes por título
- Retornar JSON com data de lançamento, bilheteria e sinopse
- Respostas em português

## Configuração

1. Clone o repositório
2. Crie um arquivo `.env` no diretório raiz com sua chave da API do Google:
```
GOOGLE_API_KEY=sua_chave_api_aqui
GOOGLR_API_MODEL=gemini-1.5-flash
```

### Executando com Docker 

3. Construa a imagem Docker:
```bash
docker build -t apimovies .
```

4. Execute o container:
```bash
docker run --env-file=.env -p 5000:5000 apimovies
```

## Uso

Envie uma requisição POST para `/chat/completions/movie` com o título do filme.

Exemplo:
```bash
POST /chat/completions/movie
Content-Type: application/json

{
  "title": "Interstellar"
}
```

Resposta:
```json
{
  "title": "Interstellar",
  "release_date": "7 de novembro de 2014",
  "box_office": "$677.5 milhões",
  "synopsis": "Em um futuro próximo, a Terra está morrendo. Uma equipe de astronautas embarca em uma missão através de um buraco de minhoca para encontrar um novo lar para a humanidade."
}
```

## Documentação da API

Após executar a aplicação, acesse:
- Swagger UI: http://localhost:5000/docs
- ReDoc: http://localhost:5000/redoc
