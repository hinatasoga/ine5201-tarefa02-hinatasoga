Calculadora - INE5201 – Tarefa 02

# Como usar?
- Clique nos botões para fazer as operações básicas de adição, subtração, multiplicação e divisão;
- Conforme as expressões são calculadas, o histórico é atualizado;
- Use OFF para fechar a calculadora digital;
- Use AC (All Clear) para apagar todo o display;
- Use CE (Clear Expression) para apagar a expressão;
- Use LH (Limpar Histórico) para limpar o histórico;
- Não é possível digitar mais do que 16 caracteres (considerando algarismos, ponto e operadores);
- Os números são arredondados até a 6ª casa decimal.

# Requisitos
- Python instalado
- Windows e PowerShell

# Executando a calculadora:
Abra o PowerShell na pasta do projeto e execute:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install FreeSimpleGUI
.\.venv\Scripts\python.exe calculadora.py
```

O uso direto do Python dentro de `.venv` dispensa ativar o ambiente virtual.

# Estrutura do código (funções):
- criar_layout(): monta a janela da calculadora.
- atualizar_display_superior(expressão): atualiza o display de cima, mostrando a conta e chamando tratar_erro("Display Overflow") se o limite de caracteres for excedido.
- atualizar_display_inferior(resposta): atualiza o display debaixo, mostrando o resultado.
- calcular(expressão): usa ast para aceitar apenas números e as operações desejadas, usando try e except para tentar os erros, arredonda as casas decimais da resposta e apresenta os inteiros sem casas decimais desnecessárias.
- tratar_erro(mensagem): mostra mensagens "Erro: Divisão por zero", "Erro: Expressão inválida" ou "Display Overflow". escreve a mensagem no display de cima, alinhada à direita, e apaga o display de baixo.
- adicionar_ao_historico(expressão, resposta): acrescenta "expressão = resposta" e atualiza a caixa do histórico.
- limpar_historico(): limpa o histórico e atualiza a caixa.
- main(): cria a janela e executa a calculadora.