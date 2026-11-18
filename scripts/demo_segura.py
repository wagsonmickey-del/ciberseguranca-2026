#!/usr/bin/env python3
"""Demonstração didática sem captura de teclado, acesso a arquivos ou rede."""


def demo_keylogger():
    exemplo = "exemplo-ficticio-123"
    print("\n=== Ilustração: keylogger ===")
    print("Sequência fictícia definida no código:", exemplo)
    print("SIMULAÇÃO: nenhum teclado foi monitorado e nenhum dado foi coletado ou salvo.")
    print("Risco conceitual: um keylogger malicioso poderia tentar observar entradas sem consentimento.")


def demo_ransomware():
    print("\n=== Ilustração: ransomware ===")
    print("1. Um ransomware real poderia tentar localizar dados acessíveis.")
    print("2. Poderia bloquear o acesso a dados e exibir uma mensagem de extorsão.")
    print("3. Resposta defensiva: isolar o dispositivo e restaurar um backup seguro após investigação.")
    print("SIMULAÇÃO: nenhum arquivo foi localizado, lido, cifrado, renomeado ou alterado.")


def main():
    print("Demonstração segura — apenas mensagens fictícias no terminal")
    print("1) Ilustração de keylogger\n2) Ilustração de ransomware")
    opcao = input("Escolha 1 ou 2: ").strip()

    if opcao == "1":
        demo_keylogger()
    elif opcao == "2":
        demo_ransomware()
    else:
        print("Opção inválida. Nenhuma ação foi realizada.")


if __name__ == "__main__":
    main()
