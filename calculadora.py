# Importações
import ast
import FreeSimpleGUI as sg

# Variáveis e etcs
linhas_visíveis = 5
historico = []
limite_caracteres_expressao = 16
limite_caracteres_resposta = 12

# Classe ou funções principais
def criar_layout():
    global window
    sg.theme("DarkBlue17")
    layout = [
        [sg.Input("",  key="display_de_cima", size=(1, 1), expand_x=True, justification='left', readonly=True)],
        [sg.Input("0.",  key="display_debaixo", size=(1, 1), expand_x=True, justification='right', text_color='white', readonly=True)],
        [sg.Button("OFF", key="OFF", size=(2, 2), button_color="crimson"), sg.Button("C", key="C", size=(2, 2), button_color="navy"), sg.Button("CE", key="CE", size=(2, 2), button_color="navy"), sg.Button("←", key="←", size=(2, 2), button_color="navy")],
        [sg.Button("1", key="1", size=(2, 2)), sg.Button("2", key="2", size=(2, 2)), sg.Button("3", key="3", size=(2, 2)), sg.Button("+", key="+", size=(2, 2), button_color="navy")],
        [sg.Button("4", key="4", size=(2, 2)), sg.Button("5", key="5", size=(2, 2)), sg.Button("6", key="6", size=(2, 2)), sg.Button("-", key="-", size=(2, 2), button_color="navy")],
        [sg.Button("7", key="7", size=(2, 2)), sg.Button("8", key="8", size=(2, 2)), sg.Button("9", key="9", size=(2, 2)), sg.Button("*", key="*", size=(2, 2), button_color="navy")],
        [sg.Button("0", key="0", size=(2, 2)), sg.Button("=", key="=", size=(4, 2), button_color="navy"), sg.Button("/", key="/", size=(2, 2), button_color="navy")],
        [sg.Text("Histórico:")],
        [sg.Listbox(values=[], key="historico", size=(1,linhas_visíveis), expand_x=True)]
        
        ]
    
    window = sg.Window("Calculadora", layout)
    return window

def atualizar_display_superior(expressão):
    if len(expressão) > limite_caracteres_expressao:
        tratar_erro("Display Overflow")
        return False
    window["display_de_cima"].Widget.configure(justify="left")
    window["display_de_cima"].update(expressão)
    return True


def atualizar_display_inferior(resposta):
    texto = str(resposta)
    if len(texto) > limite_caracteres_resposta:
        tratar_erro("Display Overflow")
        return False
    window["display_debaixo"].update(texto)
    return True
    
def calcular(expressão):
    if len(expressão) > limite_caracteres_expressao:
        tratar_erro("Display Overflow")
        return None

    def avaliar(no):
        if isinstance(no, ast.Expression):
            return avaliar(no.body)
        if (
            isinstance(no, ast.Constant)
            and isinstance(no.value, (int, float))
            and not isinstance(no.value, bool)
        ):
            return no.value
        if isinstance(no, ast.BinOp):
            esquerda = avaliar(no.left)
            direita = avaliar(no.right)
            if isinstance(no.op, ast.Add):
                return esquerda + direita
            if isinstance(no.op, ast.Sub):
                return esquerda - direita
            if isinstance(no.op, ast.Mult):
                return esquerda * direita
            if isinstance(no.op, ast.Div):
                return esquerda / direita
        if isinstance(no, ast.UnaryOp):
            valor = avaliar(no.operand)
            if isinstance(no.op, ast.UAdd):
                return valor
            if isinstance(no.op, ast.USub):
                return -valor
        raise ValueError("A expressão contém uma operação não permitida.")

    try:
        arvore = ast.parse(expressão, mode="eval")
        resposta = avaliar(arvore)
    except SyntaxError:
        tratar_erro("Erro: Expressão inválida")
        return None
    except ValueError:
        tratar_erro("Erro: Expressão inválida")
        return None
    except ZeroDivisionError:
        tratar_erro("Erro: Divisão por zero")
        return None

    if len(str(resposta)) > limite_caracteres_resposta:
        tratar_erro("Display Overflow")
        return None
    return resposta

def tratar_erro(mensagem):
    window["display_de_cima"].Widget.configure(justify="right")
    window["display_debaixo"].update("")

def adicionar_ao_historico(expressão, resposta):
    historico.append(f"{expressão} = {resposta}")
    window["historico"].update(values=historico)

def main():
    window = criar_layout()
    expressão = ""
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "OFF":
            break
        elif event in "0123456789+-*/":
            expressão += event
            atualizar_display_superior(expressão)
        elif event == "C":
            expressão = ""
            atualizar_display_superior(expressão)
            atualizar_display_inferior("0.")
        elif event == "CE":
            expressão = ""
            atualizar_display_superior(expressão)
            atualizar_display_inferior("0.")
        elif event == "←":
            expressão = expressão[:-1]
            atualizar_display_superior(expressão)
        elif event == "=":
            resposta = calcular(expressão)
            if resposta is not None:
                atualizar_display_inferior(resposta)
                adicionar_ao_historico(expressão, resposta)
                expressão = str(resposta)

    window.close()

main()