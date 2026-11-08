# 🎵 YouTube Audio Downloader CLI

Uma ferramenta em Python via linha de comando para baixar o áudio de vídeos do YouTube em alta qualidade, com uma interface bonita e barra de progresso em tempo real no terminal.

---

## 🛠️ Recursos

- 📥 **Download de áudio:** Extrai o melhor formato de áudio disponível do link fornecido.
- 📋 **Processamento em lote:** Baixa múltiplos links listados em um arquivo de texto.
- 🎨 **Interface Rica no Terminal:** Barra de progresso visual interativa, velocidade de download e tempo restante estilizados usando a biblioteca `rich`.

---

## 📋 Pré-requisitos

Antes de iniciar, certifique-se de ter instalado em sua máquina:

1. **Python 3.8+** ([Download do Python](https://www.python.org/downloads/))
2. **Git** *(opcional, para clonar o repositório)* ([Download do Git](https://git-scm.com/))

---

## 🔧 Instalação e Configuração

Siga os passos abaixo para preparar o ambiente e rodar o projeto:

### 1. Clonar ou baixar o repositório

Se você utiliza o Git, clone o repositório via terminal:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

Ou simplesmente baixe o código-fonte e extraia o conteúdo em uma pasta de sua escolha.

---

### 2. Criar um Ambiente Virtual (Recomendado)

É uma boa prática utilizar um ambiente virtual para isolar as dependências do projeto.

- **No Windows:**
  ```cmd
  python -m venv venv
  venv\Scripts\activate
  ```

- **No Linux/macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

---

### 3. Instalar as Dependências

Com o ambiente virtual ativado, instale as bibliotecas necessárias:

```bash
pip install rich yt-dlp
```

---

## 🚀 Como Usar

1. **Adicionar os links:**
   Crie ou edite o arquivo `link.txt` na raiz do projeto e insira as URLs dos vídeos do YouTube que deseja baixar (uma URL por linha).

   *Exemplo de conteúdo para `link.txt`:*
   ```text
   https://youtu.be/v1qc_u7MujU?list=RDv1qc_u7MujU
   https://www.youtube.com/watch?v=EXEMPLO_ID
   ```

2. **Executar a aplicação:**
   No terminal, execute o script principal:

   ```bash
   python main.py
   ```

3. **Acompanhar o download:**
   A aplicação exibirá uma barra de progresso no terminal detalhando a porcentagem concluída, velocidade da transferência e tempo estimado. Os arquivos de áudio baixados serão salvos diretamente na pasta do projeto.

---

## 📁 Estrutura do Projeto

```text
├── main.py          # Script principal com a lógica de download e interface
├── link.txt          # Arquivo contendo as URLs dos vídeos a serem baixados
└── README.md         # Documentação do projeto
```

---

## 🛠️ Tecnologias Utilizadas

- [Python](https://www.python.org/) - Linguagem principal.
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Biblioteca para download e extração de mídia do YouTube.
- [Rich](https://github.com/Textualize/rich) - Biblioteca para estilização de texto e barras de progresso no terminal.
