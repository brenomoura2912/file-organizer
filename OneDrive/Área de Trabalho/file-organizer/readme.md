# 📂 File Organizer 

Automação em Python desenvolvida para organização inteligente de arquivos baseada em suas extensões. Ideal para manter pastas como "Downloads" ou "Área de Trabalho" sempre limpas e estruturadas.

## 🚀 Funcionalidades

* **Categorização Automática:** Separa arquivos por tipos (Imagens, Documentos, Planilhas, PDFs, etc).
* **Criação Dinâmica de Pastas:** Cria os diretórios automaticamente caso eles não existam.
* **Relatório de Movimentações:** Gera um arquivo `log_organizacao.json` detalhando tudo o que foi movido.
* **Feedback Interativo:** Exibe uma mensagem de sucesso com o total de arquivos organizados e mantém a tela aberta para visualização do usuário.

## 🛠️ Tecnologias Utilizadas

* **Python**
* **Biblioteca `os`** (Manipulação dinâmica de caminhos do sistema)
* **Biblioteca `shutil`** (Movimentação e gerenciamento de arquivos)
* **Biblioteca `json`** (Estruturação do relatório de log)

## 📦 Como Usar

### ⚡ Opção 1: Baixar a Versão Executável (Pronto para Uso no Windows)
Você **não precisa** ter o Python instalado na sua máquina para testar a ferramenta!
1. Acesse a aba de **[Releases](https://github.com/brenomoura2912/file-organizer/releases)** deste repositório.
2. Faça o download do arquivo `organizer.exe`.
3. Execute o programa, cole o caminho da pasta que deseja organizar e dê Enter.
*(Nota: Como é um executável independente criado de forma autoral, o Windows pode exibir um alerta na primeira execução. Basta clicar em "Mais informações" e "Executar assim mesmo").*

### 💻 Opção 2: Rodar o Código-Fonte (Para Desenvolvedores)
Caso queira rodar ou fazer modificações no código:
1. Clone este repositório:
```bash
git clone https://github.com/brenomoura2912/file-organizer.git