import time

# A senha que o "sistema" está protegendo (nosso alvo)
SENHA_CORRETA = "admin123"

# Nossa mini "Wordlist" (lista de senhas comuns que usuários usam)
wordlist = ["senha", "123456", "root", "kali", "admin", "admin123", "password"]

print("=" * 50)
print("INICIANDO SIMULADOR DE FORÇA BRUTA...")
print("=" * 50)

tentativas = 0

# O laço 'for' vai pegar cada palavra da lista e testar automaticamente
for senha_teste in wordlist:
    tentativas += 1
    print(f"[Tentativa {tentativas}]: Testando a senha: '{senha_teste}'")
    
    # Colocamos um pequeno atraso de 0.5 segundos para conseguirmos ver o processo na tela
    time.sleep(0.5)
    
    # Verifica se a palavra da lista é igual à senha correta do sistema
    if senha_teste == SENHA_CORRETA:
        print("\n" + "*" * 45)
        print(f"[+] SUCESSO! Senha encontrada: {senha_teste}")
        print(f"[+] Total de tentativas: {tentativas}")
        print("*" * 45)
        break  # O 'break' interrompe o programa imediatamente porque já achamos a senha
else:
    print("\n[-] Falha: A senha correta não estava na nossa Wordlist.")