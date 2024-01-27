import requests
import json

def CEP():
    while True:
        try:
            print('Digite o cep sem caracteres especiais.')
            cep = int(input('Digite o Cep: '))
        except ValueError:
            MENU()
        url_cep = f'https://viacep.com.br/ws/{cep}/json/'
        result_cep = requests.get(url_cep)
        print('\nCEP:', result_cep.json()['cep'])
        print('Logradouro:', result_cep.json()['logradouro'])
        print('Complemento:', result_cep.json()['complemento'])
        print('Bairro:', result_cep.json()['bairro'])
        print('Localidade:', result_cep.json()['localidade'])
        print('Estado:', result_cep.json()['uf'])
        print('IBGE:', result_cep.json()['ibge'])
        print('GIA:', result_cep.json()['gia'])
        print('DDD:', result_cep.json()['ddd'])
        print('SIAFI:', result_cep.json()['siafi'], '\n')

def CNPJ():
    while True:
        try:
            cnpj = int(input('Digite o Cnpj: '))
        except ValueError:
            MENU()
        api = int(input('1 - Modo de busca 1\n2 - Modo de busca 2\nDigite o modo> '))
        match api:
            case 1:
                url_cnpj1 = f'https://brasilapi.com.br/api/cnpj/v1/{cnpj}'
                result_cnpj1 = requests.get(url_cnpj1)
                print('\nNome:', result_cnpj1.json()['razao_social'])
                print('CNPJ:', result_cnpj1.json()['cnpj'])
                print('Telefone:', result_cnpj1.json()['ddd_telefone_1'])
                print('Estado:', result_cnpj1.json()['uf'])
                print('Municipio:', result_cnpj1.json()['municipio'])
                print('CEP:', result_cnpj1.json()['cep'])
                print('Logradouro:', result_cnpj1.json()['logradouro'])
                print('Bairro:', result_cnpj1.json()['bairro'])
                print('Complemento: ', result_cnpj1.json()['complemento'])
                print('Número:', result_cnpj1.json()['numero'])
                print('CNAE Fiscal:', result_cnpj1.json()['cnae_fiscal'])
                print('Capital Social:', result_cnpj1.json()['capital_social'])
                print('Natureza Jurídica:', result_cnpj1.json()['natureza_juridica'])
                print('Situação Cadastral:', result_cnpj1.json()['descricao_situacao_cadastral'])
                print('Motivo da Situação Cadastral:', result_cnpj1.json()['descricao_motivo_situacao_cadastral'], '\n')
            case 2:
                url_cnpj2 = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}'
                result_cnpj2 = requests.get(url_cnpj2)
                print('\nNome:', result_cnpj2.json()['nome'])
                print('CNPJ:', result_cnpj2.json()['cnpj'])
                print('Telefone:', result_cnpj2.json()['ddd_telefone_1'])
                print('Estado:', result_cnpj2.json()['uf'])
                print('Municipio:', result_cnpj2.json()['municipio'])
                print('CEP:', result_cnpj2.json()['cep'])
                print('Logradouro:', result_cnpj2.json()['logradouro'])
                print('Bairro:', result_cnpj2.json()['bairro'])
                print('Complemento: ', result_cnpj2.json()['complemento'])
                print('Número:', result_cnpj2.json()['numero'])
                print('CNAE Fiscal:', result_cnpj2.json()['cnae_fiscal'])
                print('Capital Social:', result_cnpj2.json()['capital_social'])
                print('Natureza Jurídica:', result_cnpj2.json()['natureza_juridica'])
                print('Situação Cadastral:', result_cnpj2.json()['situacao'])
                print('Motivo da Situação Cadastral:', result_cnpj2.json()['motivo_situacao'])
                print('Ultima Atualização:', result_cnpj2.json()['ultima_atualizacao'], '\n')
            case _:
                print('Modo inexistente.')

def IP():
    while True:
        try:
            ip = input('Ip: ')
        except ValueError:
            MENU()
        url_ip = f'http://ip-api.com/json/{ip}'
        result_ip = requests.get(url_ip)
        print('\nIP:', result_ip.json()['query'])
        print('País:', result_ip.json()['country'],'/',result_ip.json()['countryCode'])
        print('Região:', result_ip.json()['regionName']+'/'+result_ip.json()['region'])
        print('Cidade:', result_ip.json()['city'])
        print('CEP/Zip Code:', result_ip.json()['zip'])
        print('Latitude:', result_ip.json()['lat'])
        print('Longitude:', result_ip.json()['lon'])
        print('Provedor de Internet:', result_ip.json()['isp'], '\n')

def MENU():
    while True:
        sla = int(input('1 - Cep\n2 - Ip\n3 - CNPJ\nTipo de consulta> '))
        match sla:
            case 1:
                CEP()
            case 2:
                IP()
            case 3:
                CNPJ()
            case _:
                print('Opção inexistente.')
MENU()