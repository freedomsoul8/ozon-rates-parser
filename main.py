import PySimpleGUI as sg

layout = [
    [sg.Text('Vendor code excel file'), sg.InputText(), sg.FileBrowse()],
    [sg.Submit(button_text='Parse'), sg.Cancel()]]
window = sg.Window('Ozon parser', layout)
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit', 'Cancel'):
        break
    if event == 'Parse':
        print(values)
