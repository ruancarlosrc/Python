num = int (input("Digite um numero: "));

resto = int(num/2);
resto = num - (resto*2);

if resto == 0:
    print("Numero par");
else:
    print("Numero ímpar");