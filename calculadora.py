

valor = 0
while True:
    print("""seleccione opcion
            1- Sumar 
            2- Restar
            3- Multiplicar
            4- dividir             
            5- sumar 3 valores 

        """)

    valor = int(input("Elige una opcion: ") )     

    if valor == 1:
        num1 = int(input("numero 1: ")) 
        num2 = int(input("numero 2: ")) 
        print("la suma es",num1+num2)
        break;
    if valor == 2:
        num1 = int(input("numero 1: ")) 
        num2 = int(input("numero 2: ")) 
        print("la resta es",num1-num2)
        break;
    if valor == 3:
        num1 = int(input("numero 1: ")) 
        num2 = int(input("numero 2: ")) 
        print("la multiplicacion es",num1*num2)
        break;
    if valor == 4:
        num1 = int(input("numero 1: ")) 
        num2 = int(input("numero 2: ")) 
        print("la division es",num1/num2)
        break;
    if valor == 5: #update
        num1 = int(input("numero 1: ")) 
        num2 = int(input("numero 2: ")) 
        num3 = int(input("numero 3: "))
        print("la suma es",num1+num2+num3)
        break;

    else:
        print("Opcion incorrecta")
        break;