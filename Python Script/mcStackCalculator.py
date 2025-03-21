file_path = "StackCalcolati.txt"

def write_header(file_path):
    headers = (
        "Nome Oggetto", "Quantità", "Stack Completi", "Blocchi Rimanenti", "Stack per Eccesso"
    )
    h = f'|{headers[0]:^20}|{headers[1]:^20}|{headers[2]:^20}|{headers[3]:^20}|{headers[4]:^20}|\n'
    with open(file_path, "w") as f:
        f.write('+' + ('-' * (len(h) - 2)) + '+\n')
        f.write(h)
        f.write('+' + ('-' * (len(h) - 2)) + '+\n')        

def calcola_gruppi(nome_oggetto, qnt_blocchi, stack=64):
    stack_completi = qnt_blocchi // stack
    blocchi_rimanenti = qnt_blocchi % stack
    stack_eccesso = stack_completi + (1 if blocchi_rimanenti > 0 else 0)  # Per arrotondare in eccesso
    
    risultato = f'|{nome_oggetto[:20]:^20}|{qnt_blocchi:^20}|{stack_completi:^20}|{blocchi_rimanenti:^20}|{stack_eccesso:^20}|\n'
    with open(file_path, "a") as file:
        file.write(risultato)
        file.write('+' + ('-' * (len(risultato) - 2)) + '+\n')
    
    print(f"Stack: {stack_completi}")
    print(f"Oggetti rimanenti: {blocchi_rimanenti}")

write_header(file_path)

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