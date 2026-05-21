import socket

def capturar_banner(ip, porta):
    try:
        # Cria o socket e define o tempo limite de espera para 2 segundos
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2.0)
        
        # Tenta se conectar à porta
        s.connect((ip, porta))
        
        # Envia uma mensagem genérica de "olá" (alguns servidores só mostram o banner após receberem dados)
        s.send(b"Hello\r\n")
        
        # Recebe a resposta do servidor (até 1024 bytes)
        resposta = s.recv(1024)
        
        # Decodifica a resposta para texto legível
        banner = resposta.decode('utf-8', errors='ignore').strip()
        return banner
        
    except socket.timeout:
        return "Conectado, mas o servidor não enviou nenhuma mensagem (Timeout)"
    except Exception as e:
        return f"Não foi possível obter o banner: {e}"
    finally:
        s.close()

# --- Fluxo Principal do Programa ---
print("=" * 50)
print("SISTEMA DE RECONHECIMENTO: BANNER GRABBER")
print("=" * 50)

alvo_ip = input("Digite o IP para analisar (Ex: 127.0.0.1): ")
alvo_porta = int(input("Digite a porta para capturar o banner (Ex: 3389): "))

print(f"\n[+] Conectando em {alvo_ip}:{alvo_porta}...")

# Chama a função que criamos lá em cima
resultado_banner = capturar_banner(alvo_ip, alvo_porta)

print("\n" + "-" * 40)
print(f"RESULTADO PARA A PORTA {alvo_porta}:")
print(resultado_banner)
print("-" * 40)