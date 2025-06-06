'''
# Validador de CPF - Calcula o primeiro e segundo dígito para verificar a validade do CPF informado pelo usuário
'''

import re

while True:

    try:

        cpf = input('Digite um CPF (somente números): ')
        
        # cpf_enviado_usuario = cpf.replace('.', '').replace('-', '').replace(' ', '')
        cpf_enviado_usuario = re.sub(r'[^0-9]','', cpf)     

        if len(cpf_enviado_usuario) <= 10:
            print('Você enviou dados insuficientes ou caracteres incorretos.')
            continue

        entrada_e_sequencial = cpf_enviado_usuario == cpf_enviado_usuario[0] * len(cpf_enviado_usuario)

        if entrada_e_sequencial:
            print('Você enviou dados sequenciais.')
            continue
        
        nove_digitos = cpf_enviado_usuario[:9]
        contador_regressivo_1 = 10

        resultado_digito_1 = 0
        for digito in nove_digitos:
            resultado_digito_1 += int(digito) * contador_regressivo_1
            contador_regressivo_1 -= 1
        digito_1 = (resultado_digito_1 * 10) % 11
        digito_1 = digito_1 if digito_1 <= 9 else 0


        dez_digitos = nove_digitos + str(digito_1)
        contador_regressivo_2 = 11

        resultado_digito_2 = 0
        for digito in dez_digitos:
            resultado_digito_2 += int(digito) * contador_regressivo_2
            contador_regressivo_2 -= 1
        digito_2 = (resultado_digito_2 * 10) % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0

        cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

        if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
            print(f'{cpf_enviado_usuario[:3]}.{cpf_enviado_usuario[3:6]}.{cpf_enviado_usuario[6:9]}-{digito_1}{digito_2} é válido')
            break
        else:
            print('CPF Inválido')
            break

    except:

        print('Informação inválida')
        break



        
