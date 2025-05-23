![image](https://github.com/user-attachments/assets/ac3726d8-55a4-474c-a32b-3ee97ac20f7a)

# Automação de Coleta e Envio de Ofertas de Chocolates Stuttgart

**Este projeto é para fins educacionais!**
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

## Como usar

### Pré-requisitos

- Python 3 instalado (recomendado Python 3.7+)
- Acesso à internet para scraping e envio de e-mail
- Conta de e-mail com SMTP habilitado (exemplo: Gmail com senha de app)

### Passo a passo para executar

1. Clone este repositório:

```bash
git clone https://github.com/tainara-vogniak/Pascoa.git
cd Pascoa

