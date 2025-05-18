import requests
from bs4 import BeautifulSoup
from datetime import datetime
import yagmail

# Função para coletar produtos da página de barras de chocolate
def coletar_produtos():
    url = "https://www.stuttgart.com.br/bomboniere/barras-de-chocolate.html"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Erro ao acessar a página: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    produtos = []

    for item in soup.select('ol.products.list.items.product-items li.product-item'):
        nome_elem = item.select_one('.product-item-link')
        preco_elem = item.select_one('.price')

        if not nome_elem or not preco_elem:
            continue

        nome = nome_elem.get_text(strip=True)
        preco = preco_elem.get_text(strip=True)
        data_coleta = datetime.now()

        produtos.append({
            'nome': nome,
            'preco': preco,
            'data_coleta': data_coleta
        })

    return produtos

# Função para enviar e-mail com os produtos
def enviar_email(produtos):
    if not produtos:
        print("Nenhum produto encontrado. E-mail não enviado.")
        return

    yag = yagmail.SMTP(user='seu_email@gmail.com', password='sua_senha_app')

    corpo_tabela = "<table border='1' style='border-collapse: collapse;'>"
    corpo_tabela += "<tr><th>Produto</th><th>Preço</th></tr>"
    for p in produtos:
        corpo_tabela += f"<tr><td>{p['nome']}</td><td>{p['preco']}</td></tr>"
    corpo_tabela += "</table>"

    corpo_email = f"""
    <h2>Feliz Páscoa!</h2>
    <p>Confira as ofertas de barras de chocolate da Stuttgart:</p>
    {corpo_tabela}
    <p>Data/Hora da coleta: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</p>
    <p><a href='https://www.stuttgart.com.br/bomboniere/barras-de-chocolate.html'>Visitar loja</a></p>
    """

    yag.send(
        to='destinatario@email.com'
        subject='Ofertas de Páscoa - Chocolates Stuttgart',
        contents=corpo_email
    )

    print("Email enviado com sucesso!")

# Execução principal
if __name__ == "__main__":
    produtos = coletar_produtos()
    enviar_email(produtos)
