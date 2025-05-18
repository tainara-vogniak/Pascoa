# Automação de Coleta e Envio de Ofertas de Chocolates Stuttgart

Este projeto automatiza a coleta de ofertas de barras de chocolate da loja online [Stuttgart](https://www.stuttgart.com.br/bomboniere/barras-de-chocolate.html) e envia um e-mail com os produtos encontrados, facilitando a divulgação das promoções para a Páscoa.

---

## Funcionalidades

- Realiza web scraping da página de barras de chocolate da Stuttgart para extrair nome e preço dos produtos.
- Gera um e-mail com uma tabela HTML contendo os produtos coletados.
- Envia o e-mail automaticamente para destinatários definidos.
- Código organizado para fácil extensão, por exemplo, para salvar os dados em banco de dados.

---

## Tecnologias Utilizadas

- Python
- Requests
- BeautifulSoup4
- Yagmail (para envio de e-mails via SMTP)
- HTML para formatação do corpo do e-mail

---

## Como usar

1. **Clone o repositório:**

```bash
git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositorio
