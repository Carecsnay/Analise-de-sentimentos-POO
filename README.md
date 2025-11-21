# Análise de Sentimentos

Este é um projeto simples em Python para análise de sentimentos de textos. Ele utiliza a biblioteca NLTK para classificar textos como Positivo, Negativo ou Neutro e armazena os resultados em um banco de dados SQLite.

## Funcionalidades

-   Analisa o sentimento de uma lista de frases pré-definidas.
-   Classifica os sentimentos em Positivo, Negativo ou Neutro.
-   Armazena o post, a categoria, o status (ativo/inativo) e a pontuação da análise em um banco de dados SQLite.
-   Fornece uma estrutura básica de banco de dados para persistência dos dados.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

-   **`main.py`**: O ponto de entrada da aplicação. Ele popula o banco de dados com exemplos, realiza a análise de sentimentos e pode exibir os resultados.
-   **`analysis.py`**: Contém a lógica principal da análise de sentimentos, utilizando o `SentimentIntensityAnalyzer` do NLTK.
-   **`db/database.py`**: Gerencia a conexão com o banco de dados SQLite, incluindo a criação da tabela e as operações de inserção e leitura de posts.
-   **`db/models.py`**: Define o modelo de dados `Post` que representa uma entrada no banco de dados.
-   **`db/post_analysis.db`**: O arquivo de banco de dados SQLite gerado pela aplicação.

## Dependências

O projeto utiliza as seguintes bibliotecas Python:

-   **nltk**: Uma plataforma líder para a construção de programas Python para trabalhar com dados de linguagem humana.

Você pode instalar a dependência necessária usando o pip:

```bash
pip install nltk
```

## Como Executar

1. **Clone o repositório:**

    ```bash
    git clone <url-do-repositorio>
    cd <diretorio-do-projeto>
    ```

2. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Execute o script principal:**
    ```bash
    python main.py
    ```
    Na primeira execução, o script fará o download do léxico `vader_lexicon` do NLTK, necessário para a análise de sentimentos.

O script irá popular o banco de dados `db/post_analysis.db` com algumas frases de exemplo e suas respectivas análises de sentimento. Você pode descomentar a chamada da função `display_all_posts()` em `main.py` para ver os resultados impressos no console.
