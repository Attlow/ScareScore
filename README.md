# ScareScore
Este projeto é um exemplo básico de API em Flask, criado como um blueprint para servir de ponto de partida no desenvolvimento de APIs RESTful. Ele faz uso da biblioteca pandas para manipulação de dados a partir de um arquivo CSV, retornando dados no formato JSON.

Funcionalidades
Consulta de dados: A API permite a visualização de todos os dados disponíveis e a busca por registros específicos com base no nome.
Estrutura básica: Inclui uma configuração inicial para endpoints RESTful, retorno de dados em JSON e manipulação de arquivos CSV.

Endpoints
/: Verificação de status da API.
/movies: Retorna todos os dados da tabela em formato JSON.
/movies/<name>: Retorna dados de um item específico pelo nome.

Como usar
Clone o repositório.
Instale as dependências.
Coloque um arquivo CSV no diretório (exemplo: ScareScore.csv).
Execute com python <nome_do_arquivo>.py.
