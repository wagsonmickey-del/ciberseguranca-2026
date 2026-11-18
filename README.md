# Cibersegurança 2026 — estudo seguro de keyloggers e ransomware

## Sobre o projeto

Este repositório documenta um estudo introdutório sobre duas classes de ameaça: keyloggers, que tentam capturar teclas sem autorização, e ransomware, que pode bloquear o acesso a dados para extorsão.

O objetivo é compreender os riscos, reconhecer sinais de comprometimento e estudar medidas de defesa. O exemplo deste projeto é apenas demonstrativo: mostra mensagens e dados fictícios no terminal. Não monitora o teclado, acessa ou altera arquivos, cifra dados, coleta credenciais nem usa a rede.

## Objetivos de aprendizagem

- Explicar, em alto nível, como keyloggers e ransomware podem afetar a confidencialidade e a disponibilidade.
- Diferenciar uma simulação controlada de uma atividade real de coleta ou extorsão.
- Identificar medidas preventivas e ações iniciais de resposta a incidentes.
- Registrar resultados com clareza, sem afirmar que uma ameaça foi executada quando houve apenas uma simulação.

## Conceitos estudados

### Keylogger

Um keylogger malicioso tenta registrar entradas do teclado sem conhecimento ou autorização da pessoa, podendo expor informações sensíveis. Este projeto não implementa captura de teclas: a demonstração usa somente um texto fictício definido no próprio exemplo.

### Ransomware

Ransomware é um tipo de malware que pode impedir o acesso a dados, frequentemente por meio de criptografia, e exigir pagamento. Este projeto não criptografa nem modifica arquivos. A demonstração apenas apresenta, em texto, um fluxo hipotético e formas de resposta defensiva.

## Demonstração segura

O script scripts/demo_segura.py exibe mensagens fictícias no terminal. Não acessa a APIs de teclado, arquivos pessoais, inicialização do sistema ou rede. Não coleta, armazena ou transmite informações.

Uma simulação didática ajuda a discutir conceitos, mas não detecta nem remove malware e não substitui ferramentas de segurança ou uma análise profissional.

## Boas práticas defensivas

- Mantenha o sistema operacional, o navegador e os aplicativos atualizados.
- Use autenticação multifator e senhas únicas, guardadas em um gerenciador confiável.
- Baixe programas somente de fontes confiáveis e desconfie de anexos ou links inesperados.
- Use proteção de endpoint e mantenha cópias de segurança protegidas contra alterações; teste a restauração.
- Restrinja privilégios administrativos e aplique o princípio do menor privilégio.
- Se suspeitar de ransomware, desconecte o dispositivo da rede, evite conectar backups e avise a equipe responsável. Preserve evidências e busque orientação especializada antes de tentar recuperar os dados.
- Se suspeitar de captura de credenciais, use outro dispositivo confiável para trocar senhas importantes, encerre sessões ativas e contate o suporte responsável.

## Conclusão

Compreender uma ameaça não exige executá-la. Simulações sem efeitos no sistema permitem estudar conceitos e controles de defesa sem coletar dados nem colocar arquivos em risco.

## Referências para estudo

Consulte materiais de conscientização e resposta a incidentes de fontes reconhecidas, como CERT.br, CISA e a documentação oficial dos sistemas utilizados. Verifique a data e o contexto das recomendações.
