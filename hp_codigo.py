import json
import requests
response = requests.get("http://hp-api.herokuapp.com/api/characters")
todos = json.loads(response.text)
#print(json.dumps(todos, indent=4))

print('\033[1;35mBEM-VINDO AO SISTEMA ESCOLAR DE HOGWARTS!\033[m')
print('Informações disponíveis ao seu usuário:')
print('[1] Alunos matriculados\n[2] Funcionários\n[3] Integrantes da Sonserina\n[4] Integrantes da Grifinória\n[5] '
      'Integrantes da Lufa-Lufa\n[6] Integrantes da Corvinal\n[7] Patrono\n[8] Sair')
print('Para acessar as informações acima, digite o número de interesse.')
resp = ''
while resp != 8:
    resp = int(input('\nNúmero de interesse: '))
    if resp == 1:
        print('\033[1;37m\nOs alunos de Hogwards são:\033[m')
        for i in range(len(todos)):
            isStudent = todos[i]['hogwartsStudent']
            if isStudent == True:
                print(todos[i]['name'])
    elif resp == 2:
        print('\033[1;34m \nOs funcionários de Hogwards são:\033[m')
        for i in range(len(todos)):
            isStaff = todos[i]['hogwartsStaff']
            if isStaff == True:
                print(todos[i]['name'])

    elif resp == 3:
        print('\n\033[1;32mIntegrantes da Sonserina:\033[m ')
        for i in range(len(todos)):
            isSlytherin = todos[i]['house']
            if isSlytherin == "Slytherin":
                print(todos[i]['name'])

    elif resp == 4:
        print('\n\033[1;31mIntegrantes da Grifinória:\033[m ')
        for i in range(len(todos)):
            isGryffindor = todos[i]['house']
            if isGryffindor == "Gryffindor":
                print(todos[i]['name'])

    elif resp == 5:
        print('\n\033[1;33mIntegrantes da Lufa-Lufa:\033[m ')
        for i in range(len(todos)):
            isHufflepuff = todos[i]['house']
            if isHufflepuff == "Hufflepuff":
                print(todos[i]['name'])

    elif resp == 6:
        print('\n\033[1;36mIntegrantes da Corvinal:\033[m ')
        for i in range(len(todos)):
            isRavenclaw = todos[i]['house']
            if isRavenclaw == "Ravenclaw":
                print(todos[i]['name'])

    elif resp == 7:
        print('\033[1;30m\nPatrono\033[m')
        nome = str(input('Digite o nome da pessoa que você deseja saber o patrono: '))
        for i in range(len(todos)):
            isName = todos[i]['name']
            if nome == isName:
                if todos[i]['patronus'] != "":
                    print('O patrono de {} é um \033[4m{}\033[m.'.format(nome, todos[i]['patronus']))
                else:
                    print('Esta pessoa não sabe fazer patrono kkkkk')

    elif resp == 8:
        print('Até logo!')

    else:
        print('Resposta inválida')
