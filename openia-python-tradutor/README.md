# Tradutor com OpenAI

Este é um programa Python que utiliza a API da OpenAI para realizar traduções de texto. Ele utiliza o modelo "text-davinci-003" da OpenAI para realizar as traduções.

## Configuração

Antes de executar o programa, certifique-se de configurar corretamente as variáveis de ambiente:

1. Crie um arquivo `.env` na raiz do projeto.
2. Adicione as seguintes linhas ao arquivo `.env`:

    OPENAI_API_KEY=`SUA_CHAVE_DA_API`

    Substitua `SUA_CHAVE_DA_API` pela sua chave de API da OpenAI.

3. Execute o seguinte comando para instalar as dependências necessárias:

```shell
pip install openai python-dotenv
```
## Uso
Execute o programa digitando o seguinte comando no terminal:

```shell
python tradutor.py
```
O programa solicitará o texto a ser traduzido e o idioma de destino. Após a tradução, o resultado será exibido no console.

## Observações
Certifique-se de ter uma conta na OpenAI e de que sua chave de API esteja ativa.

Verifique sua cota de uso na OpenAI para garantir que você não exceda os limites permitidos.

Observe que este é um exemplo completo em linguagem de marcação, seguindo a sintaxe do Markdown, para um arquivo README.md. 

Certifique-se de copiar todo o conteúdo corretamente para o seu arquivo README.md.