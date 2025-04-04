import requests
from bs4 import BeautifulSoup
import re
from config import data, post_data

cookies = {
    'NSC_JOvli21vbwcnm34cfqy1czem22l1tbm': 'ffffffff09e9fa0145525d5f4f58455e445a4a42378b',
    '_gid': 'GA1.3.770700420.1743728816',
    '_hjSessionUser_1955131': 'eyJpZCI6ImVmZDQzNzE5LTc3MDQtNTYyZi05N2EwLThiNmM3NzcwMTNiNiIsImNyZWF0ZWQiOjE3NDM3Mjg4MTU4MjUsImV4aXN0aW5nIjpmYWxzZX0=',
    '_uetsid': '1a0afb9010f111f09f343d476f87cb77',
    '_uetvid': '1a0b104010f111f08ad1bfd9b841a4d4',
    'nvg55705': '1603eadda497588d39e5fdf9b610|0_94',
    '_clck': '1mao1gj%7C2%7Cfus%7C0%7C1920',
    '_clsk': '1imt4ge%7C1743728816755%7C1%7C1%7Cn.clarity.ms%2Fcollect',
    'cto_bundle': 'UsKaGF94U3JWR2llY3ZMUW1rWXhnVFBERyUyRmtybU1RTFczVDNqaGR3RDlHQk1FdVNBa0J0MWVjNCUyRk5BUDdVbkZpeCUyRjZXbnBEaHJLbDJuVVloeWZOaHklMkZLSmV5UXkzUnR5OG93UXh5JTJGYUZlM2RmVDQ3V0ZvVkdhSEpPbWJKYVN3bG1QNzZGejR2U05CWXB1MWZia2tkN1czakt3JTNEJTNE',
    'lumClientId': '8A61649095B0A4C20195FE566FF824CC',
    'lumUserLocale': 'pt_BR',
    '__app': 'prestador',
    '__site': 'sulamerica-saude',
    'tel': 'central_atendimento_doctorline.gif',
    '__utmc': '11233718',
    '__utmz': '11233718.1743728922.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'liveagent_oref': 'https://saude.sulamericaseguros.com.br/prestador/',
    'liveagent_ptid': '5db721da-9de4-4f60-b20b-ef2a207f405b',
    '__codp': '100000009361',
    '_ga_565NE9S6RK': 'GS1.3.1743728816.1.1.1743729644.60.0.0',
    '_ga_XDNXH4S93Y': 'GS1.1.1743728815.1.1.1743729652.0.0.676466996',
    '_ga_YZ8V1YKTQR': 'GS1.1.1743728815.1.1.1743729652.0.0.0',
    '__utma': '11233718.767877916.1743728816.1743734252.1743737519.3',
    'liveagent_sid': '3bae6ff8-edc8-414f-8085-d6621054740d',
    'liveagent_vc': '5',
    'lumIsLoggedUser': 'false',
    'lumUserId': '00000000D00000000000000000000002',
    'JSESSIONID': 'Z4Bs6unGO15HpEFSxiDX2wF3zlkoqFNr5Yd44v5I.s01jbs159',
    'lumUserSessionId': 'q2R0nTvrV2KrmQNcovs7YNIGp-1y-yB3',
    '_gat': '1',
    '__page': 'Home | SulAmerica',
    '_ga': 'GA1.1.767877916.1743728816',
    '_ga_GT8PCDTCXZ': 'GS1.3.1743743886.3.0.1743743886.60.0.0',
    '_dd_s': 'rum=2&id=ead37607-e46d-4012-8573-05a26d6e550c&created=1743743886735&expire=1743744807151',
    '_ga_8MDSH1YG45': 'GS1.1.1743743886.4.1.1743743907.0.0.0',
    '_ga_M3S5VMZ7VB': 'GS1.1.1743743886.4.1.1743743907.0.0.0',
    '_ga_3HQMVENFZW': 'GS1.1.1743743887.4.1.1743743907.0.0.0',
    'ADRUM': 's=1743743907193&r=https%3A%2F%2Fsaude.sulamericaseguros.com.br%2Fprestador%2Flogin%2F%3F877518778',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'origin': 'https://saude.sulamericaseguros.com.br',
    'priority': 'u=0, i',
    'referer': 'https://saude.sulamericaseguros.com.br/prestador/login/?accessError=2',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    # 'cookie': 'NSC_JOvli21vbwcnm34cfqy1czem22l1tbm=ffffffff09e9fa0145525d5f4f58455e445a4a42378b; _gid=GA1.3.770700420.1743728816; _hjSessionUser_1955131=eyJpZCI6ImVmZDQzNzE5LTc3MDQtNTYyZi05N2EwLThiNmM3NzcwMTNiNiIsImNyZWF0ZWQiOjE3NDM3Mjg4MTU4MjUsImV4aXN0aW5nIjpmYWxzZX0=; _uetsid=1a0afb9010f111f09f343d476f87cb77; _uetvid=1a0b104010f111f08ad1bfd9b841a4d4; nvg55705=1603eadda497588d39e5fdf9b610|0_94; _clck=1mao1gj%7C2%7Cfus%7C0%7C1920; _clsk=1imt4ge%7C1743728816755%7C1%7C1%7Cn.clarity.ms%2Fcollect; cto_bundle=UsKaGF94U3JWR2llY3ZMUW1rWXhnVFBERyUyRmtybU1RTFczVDNqaGR3RDlHQk1FdVNBa0J0MWVjNCUyRk5BUDdVbkZpeCUyRjZXbnBEaHJLbDJuVVloeWZOaHklMkZLSmV5UXkzUnR5OG93UXh5JTJGYUZlM2RmVDQ3V0ZvVkdhSEpPbWJKYVN3bG1QNzZGejR2U05CWXB1MWZia2tkN1czakt3JTNEJTNE; lumClientId=8A61649095B0A4C20195FE566FF824CC; lumUserLocale=pt_BR; __app=prestador; __site=sulamerica-saude; tel=central_atendimento_doctorline.gif; __utmc=11233718; __utmz=11233718.1743728922.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); liveagent_oref=https://saude.sulamericaseguros.com.br/prestador/; liveagent_ptid=5db721da-9de4-4f60-b20b-ef2a207f405b; __codp=100000009361; _ga_565NE9S6RK=GS1.3.1743728816.1.1.1743729644.60.0.0; _ga_XDNXH4S93Y=GS1.1.1743728815.1.1.1743729652.0.0.676466996; _ga_YZ8V1YKTQR=GS1.1.1743728815.1.1.1743729652.0.0.0; __utma=11233718.767877916.1743728816.1743734252.1743737519.3; liveagent_sid=3bae6ff8-edc8-414f-8085-d6621054740d; liveagent_vc=5; lumIsLoggedUser=false; lumUserId=00000000D00000000000000000000002; JSESSIONID=Z4Bs6unGO15HpEFSxiDX2wF3zlkoqFNr5Yd44v5I.s01jbs159; lumUserSessionId=q2R0nTvrV2KrmQNcovs7YNIGp-1y-yB3; _gat=1; __page=Home | SulAmerica; _ga=GA1.1.767877916.1743728816; _ga_GT8PCDTCXZ=GS1.3.1743743886.3.0.1743743886.60.0.0; _dd_s=rum=2&id=ead37607-e46d-4012-8573-05a26d6e550c&created=1743743886735&expire=1743744807151; _ga_8MDSH1YG45=GS1.1.1743743886.4.1.1743743907.0.0.0; _ga_M3S5VMZ7VB=GS1.1.1743743886.4.1.1743743907.0.0.0; _ga_3HQMVENFZW=GS1.1.1743743887.4.1.1743743907.0.0.0; ADRUM=s=1743743907193&r=https%3A%2F%2Fsaude.sulamericaseguros.com.br%2Fprestador%2Flogin%2F%3F877518778',
}

with requests.Session() as s:
    login_url = 'https://saude.sulamericaseguros.com.br/prestador/login/?accessError=2'
    r = s.get(login_url)
    
    login_response = s.post(login_url, cookies=cookies, headers=headers, data=data)
    if login_response.status_code == 200:
        print("Login realizado com sucesso")
    
    consulta_url = 'https://saude.sulamericaseguros.com.br/prestador/servicos-medicos/contas-medicas/faturamento-tiss-3/faturamento/guia-de-consulta/'
    acessar_consulta = s.get(consulta_url)
    
    # enviar os dados do post para obter a resposta com os dados
    response = s.post(consulta_url, cookies=cookies, headers=headers, data=post_data)
    if response.status_code == 200:
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
        for campo, valor in dados_extraidos.items():
            if valor:
                print(f"{campo}: {valor}")
            else:
                print(f"{campo}: Não encontrado")
                
    else:
        print(f"Erro na requisição: {response.status_code}")