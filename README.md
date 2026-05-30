# Sistema Nota Fiscal em Python V1

Um sistema simples e eficiente de linha de comando (CLI) para geração de notas fiscais de produtos e serviços. Desenvolvido em Python, o sistema permite o cadastro de dados do cliente, inserção de itens da nota e a exportação automática para uma planilha Excel totalmente formatada.

## 🚀 Funcionalidades

- **Entrada de Dados Simplificada:** Cadastro dinâmico do cliente (Nome, CPF) e loop intuitivo para inclusão de múltiplos itens na mesma nota.
- **Validação Automática:** Tratamento de erros rigoroso (via `try/except`) para garantir que as entradas de quantidades e valores sejam numéricas.
- **Formatação de CPF:** Máscara aplicada automaticamente ao CPF do cliente via módulo interno de validação.
- **Cálculo de Total Automatizado:** O valor total da nota é gerado através da multiplicação da quantidade pelo valor unitário de cada item cadastrado.
- **Exportação para Excel (.xlsx):** Geração dinâmica de planilhas na pasta `./Notas` (criada automaticamente caso não exista).
- **Estilização Elegante:** A planilha gerada mescla o poder analítico do `pandas` e o design do `openpyxl` para aplicar cabeçalhos coloridos, mesclagem de células, ajuste de colunas e formatação monetária padrão BRL.

## ⚠️ Avisos Importantes

- **Dados da Empresa (Hardcoded):** Atualmente, as informações da empresa emissora (*Empresa: Uhalace de Souza S/A* e o *CNPJ*) estão fixas no código-fonte do arquivo de exportação (`Excel.py`). Caso vá utilizar o sistema em ambiente real, lembre-se de alterar esses dados para os da sua empresa na classe `Excel`.

## 📋 Pré-requisitos

Para rodar este projeto, você precisará do Python 3 instalado em sua máquina e das seguintes bibliotecas externas:

- `pandas`
- `openpyxl`

## 🔧 Instalação e Uso

1. Clone ou baixe este repositório para a sua máquina local.
2. Abra o terminal na pasta raiz do projeto.
3. Instale as dependências executando o comando abaixo:
   ```bash
   pip install pandas openpyxl
   ```
4. Execute o script principal:
   ```bash
   python main.py
   ```
5. Siga as instruções no terminal:
   - Digite o nome e CPF do cliente.
   - Insira o número da nota.
   - Cadastre os itens (nome, valor, quantidade).
   - Ao finalizar a inserção dos itens, confirme que deseja exportar para Excel.
6. O arquivo Excel final (ex: `Nº 123.xlsx`) será salvo dentro da pasta `Notas/`.

## 📁 Estrutura do Projeto

O sistema possui uma arquitetura modular separada em diretórios lógicos:

- `main.py`: Arquivo principal responsável pela interação primária, captura dos dados do cliente e orquestração do fluxo de geração da nota fiscal.
- `/dependencias/`
  - `Base/BD.py`: Estrutura Singleton para armazenamento do banco de dados temporário em memória (lista).
  - `Forms/CadItem.py`: Interface de linha de comando (CLI) responsável pelo loop de perguntas e validação de entradas do usuário via teclado.
  - `Porcess/Salvar.py`: Camada de serviços que converte as entradas do usuário, valida e as injeta de forma estruturada na memória.
  - `Porcess/Validation.py`: Abstração de regras de negócio adicionais, como checagem unificada de tipos e máscara para CPF.
  - `Export/Excel.py`: Motor de exportação responsável por consolidar os dados da nota, gerar o diretório `/Notas`, e estilizar a planilha dinamicamente.

## 👤 Autor

Desenvolvido por **Uhalace de Souza**.