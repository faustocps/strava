import requests
from bs4 import BeautifulSoup
import os

def scrape_website(url):
    try:

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'Referer': 'https://www.google.com/',
            'Accept-Encoding': 'gzip, deflate, br'
        }

        session = requests.Session()
        session.headers.update(headers)
        response = session.get(url)

        # Enviar requisição GET
        # response = requests.get(url, headers=headers)
        response.raise_for_status()  # Verificar erros HTTP

        # Parsear o conteúdo HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Remover scripts e estilos
        for script in soup(["script", "style", "nav", "footer", "header", "aside"]):
            script.decompose()

        # Extrair texto principal
        text = soup.get_text(separator='\n', strip=True)

        # Limpar espaços em branco excessivos
        lines = (line.strip() for line in text.splitlines())
        cleaned_text = '\n'.join(line for line in lines if line)

        return cleaned_text

    except Exception as e:
        print(f"Erro: {e}")
        return None

def save_content(content, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Arquivo salvo como {filename}")
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")     

if __name__ == "__main__":
    dominio = input("Digite o domínio (ex: https://deepseek.com): ")
    
    # Adicionar protocolo se necessário
    if not dominio.startswith(('http://', 'https://')):
        dominio = 'https://' + dominio
    
    # Coletar conteúdo
    conteudo = scrape_website(dominio)
    
    
        # Opcional: Salvar HTML completo
        # html_completo = requests.get(dominio).text
        # save_content(html_completo, nome_arquivo.replace('.txt', '.html'))