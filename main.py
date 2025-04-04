import requests
from bs4 import BeautifulSoup
import re
from config import data, post_data

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
}

with requests.Session() as s:
    login_url = 'https://saude.sulamericaseguros.com.br/prestador/login/?accessError=2'
    print("Acessando página de login para obter cookies...")
    r = s.get(login_url, headers=headers)
    
    login_headers = headers.copy()
    login_headers.update({
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://saude.sulamericaseguros.com.br',
        'referer': login_url,
    })

    print("Fazendo login...")
    login_response = s.post(login_url, headers=login_headers, data=data)

    if login_response.status_code == 200:
        # Verificar se o login foi bem-sucedido
        if "accessError" in login_response.url:
            print("Falha no login. Verifique suas credenciais.")
            exit()
        else:
            print("Login realizado com sucesso!")
    else:
        print(f"Erro na requisição de login: {login_response.status_code}")
        exit()
    
    consulta_url = 'https://saude.sulamericaseguros.com.br/prestador/servicos-medicos/contas-medicas/faturamento-tiss-3/faturamento/guia-de-consulta/'
    print("Acessando página de consulta...")

    consulta_headers = headers.copy()
    consulta_headers.update({
        'referer': 'https://saude.sulamericaseguros.com.br/prestador/',
    })

    acessar_consulta = s.get(consulta_url, headers=consulta_headers)

    post_headers = consulta_headers.copy()
    post_headers.update({
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://saude.sulamericaseguros.com.br',
        'referer': consulta_url,
    })

    print("Pesquisando...")
    response = s.post(consulta_url, headers=post_headers, data=post_data)
    

    if response.status_code == 200:
        print("Extraindo dados...")
        soup = BeautifulSoup(response.text, 'html.parser')
        
        dados_extraidos = {}
        
        def extrair_valor_apos_strong(soup, texto_strong):
            elemento = soup.find('strong', string=texto_strong)
            if elemento:
                valor = elemento.parent.get_text().replace(texto_strong, '', 1).strip()
                return valor
            return None
        
        dados_extraidos['Referenciado'] = extrair_valor_apos_strong(soup, 'Referenciado:')
        dados_extraidos['Código'] = extrair_valor_apos_strong(soup, 'Código:')
        dados_extraidos['CNES'] = extrair_valor_apos_strong(soup, 'CNES:')
        dados_extraidos['Usuário'] = extrair_valor_apos_strong(soup, 'Usuário:')

        telefone_strong = soup.find('strong', string='Telefone:')

        if telefone_strong:
            telefone_span = telefone_strong.find_next('span', id='telFor')

            if telefone_span:
                telefone_texto = telefone_span.get_text()
                telefone_limpo = re.sub(r'\s+', '', telefone_texto)

                if len(telefone_limpo) >= 10:
                    ddd = telefone_limpo[:2]
                    numero = telefone_limpo[2:]
                    telefone_formatado = f"({ddd}) {numero}"
                    dados_extraidos['Telefone'] = telefone_formatado
                else:
                    dados_extraidos['Telefone'] = telefone_limpo
            else:
                # tentando pegar o tel
                telefone_valor = telefone_strong.parent.get_text().replace('Telefone:', '', 1).strip()
                dados_extraidos['Telefone'] = telefone_valor
        
        dados_extraidos['E-mail Funcionário'] = extrair_valor_apos_strong(soup, 'E-mail Funcionário:')
        
        # exibindo os dados

        print("\nDados extraídos:")
        print("-" * 40)
        for campo, valor in dados_extraidos.items():
            if valor:
                print(f"{campo}: {valor}")
            else:
                print(f"{campo}: Não encontrado")
                
    else:
        print(f"Erro na requisição: {response.status_code}")
        print(response.text[:200])