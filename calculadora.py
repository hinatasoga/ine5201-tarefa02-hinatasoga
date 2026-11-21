# Importações
import ast
import FreeSimpleGUI as sg

# Variáveis e etcs
linhas_visíveis = 5
historico = []

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
        [sg.Button("0", key="0", size=(2, 2)), sg.Button(".", key=".", size=(2, 2), button_color="navy"), sg.Button("=", key="=", size=(2, 2), button_color="navy"), sg.Button("/", key="/", size=(2, 2), button_color="navy")],
        [sg.Text("Histórico:")],
        [sg.Listbox(values=[], key="historico", size=(1,linhas_visíveis), expand_x=True)]
        
        ]
    
    window = sg.Window("Calculadora", layout)
    return window

def atualizar_display_superior(expressão):
    window["display_de_cima"].update(expressão)


def atualizar_display_inferior(resposta):
    window["display_debaixo"].update(resposta)
    
def calcular(expressão):
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
        return avaliar(arvore)
    except (SyntaxError, ValueError, ZeroDivisionError):
        tratar_erro("Math ERROR")
        return None

def tratar_erro(mensagem):
    window["display_de_cima"].update(mensagem, justification="right")
    window["display_debaixo"].update("")

def adicionar_ao_historico(expressão, resposta):
    historico.append(f"{expressão} = {resposta}")
    window["historico"].update(values=historico)

def main():
    pass

# Loop de eventos da GUI
