while True:
    print("--------------CONVERSOR DE MEDIDAS----------------")
    
    valor=float(input('Informe o valor que deseja converter'))

    print('DE METROS PARA CENTIMETROS DIGITE [MC]')
    print('DE CENTIMETROS PARA METROS DIGITE [CM]')
    print('DE METROS PARA KILOMETRO DIGITE [KM]')
    print('DE KILOMETROS PARA METRO DIGITE [MK]')
    print("Para sair digite [S]")

    conversor=input('Para qual unidade deseja converter?')

    if conversor == 'MC' or conversor== 'mc':
        print(f"{valor} metros convertido é igual a  {valor*100} centimetros")
    elif conversor == 'CM'or conversor== 'cm':
       print(f"{valor} centimetros convertido é igual a  {valor/100} metros")
    elif conversor == 'KM'or conversor=='km':
       print(f"{valor} metros convertido é igual a  {valor/1000} km")
    elif conversor == 'MK'or conversor=='mk':
       print(f"{valor} km convertido é igual a  {valor*1000} metros")
    elif conversor =='S' or conversor=='s':
        break
    else:
        print("Informe uma medida disponivel")
    
print('conversor finalizado')  