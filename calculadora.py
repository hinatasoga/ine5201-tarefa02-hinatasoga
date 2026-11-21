# Importações
import FreeSimpleGUI as sg

# Variáveis e etcs
linhas_visíveis = 5

# Classe ou funções principais
def criar_layout():
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


def atualizar_display(valor):
    
def calcular(expressao):
    
def tratar_erro(mensagem):
    
def adicionar_ao_historico(expressao, resultado):
    
def main():
    
# Loop de eventos da GUI
