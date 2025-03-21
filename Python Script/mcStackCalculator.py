def calcola_gruppi(nome_oggetto, qnt_blocchi, stack=64):
    stack_completi = qnt_blocchi // stack
    blocchi_rimanenti = qnt_blocchi % stack
    stack_eccesso = stack_completi + (1 if blocchi_rimanenti > 0 else 0)  # Per arrotondare in eccesso
    
    risultato = f"{nome_oggetto}\t{qnt_blocchi}\t{stack_completi}\t{blocchi_rimanenti}\t{stack_eccesso}\n"
    
    with open("C:/Users/Simone/Desktop/StackCalcolati.txt", "a") as file:
        file.write(risultato)
    
    print(f"Stack: {stack_completi}")
    print(f"Oggetti rimanenti: {blocchi_rimanenti}")


with open("risultati.txt", "w") as file:
    file.write("Nome Oggetto\tQuantità\tStack Completi\tBlocchi Rimanenti\tStack per Eccesso\n")

while True:
    nome = input("Nome oggetto o 'esci' per terminare: ")
    if nome.lower() == 'esci':
        break

    while True:
        try:
            numero = int(input(f"blocchi di {nome}: "))
            break  
        except ValueError:
            print("inserisci un numero valido!")
    
    calcola_gruppi(nome, numero)
