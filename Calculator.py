import PySimpleGUIQt as sg

#Button Settings
bw = {'size':(7,2), 'button_color':("black","#F8F8F8")}
bt = {'size':(7,2), 'button_color':("black","#0a44f2")}
bo = {'size':(15,2), 'button_color':("black","#ECA527"), 'focus':True}

layout=[
        [sg.Text('Hasantha', size=(30,1), justification='right', background_color="#272533",
        text_color='white')],
        [sg.Text('0.0000', size=(30,1), justification='right', background_color='black', text_color='red',
        font=('Digital-7',13), relief='sunken', key="_DISPLAY_")],
        [sg.Button('C',**bw),sg.Button('CE',**bw),sg.Button('%',**bw),sg.Button('/',**bw)],
        [sg.Button('7',**bt),sg.Button('8',**bt),sg.Button('9',**bt),sg.Button('*',**bt)],
        [sg.Button('4',**bt),sg.Button('5',**bt),sg.Button('6',**bt),sg.Button('-',**bt)],
        [sg.Button('1',**bt),sg.Button('2',**bt),sg.Button('3',**bt),sg.Button('+',**bt)],
        [sg.Button('0',**bt),sg.Button(".",**bt),sg.Button('=',**bo)]
        ]
window = sg.Window(title="Simple Calculator", size=(320,480), layout=layout,return_keyboard_events=True)

var = {'front':[], 'back':[], 'decimal':False, 'x_val':0.0, 'y_val':0.0, 'result':0.0, 'operator':''}


def format_number():
    return float(''.join(var['front']) + '.' + ''.join(var['back']))

def update_display(display_value):
    try:
        window['_DISPLAY_'].update(value='{:,.4f}'.format(display_value))
    except:
        window['_DISPLAY_'].update(value=display_value)


def numbers_click(event):
        global var
        if var['decimal']:
                var['back'].append(event)
        else:
                var['front'].append(event)
        update_display(format_number())

def clear_click():
        global var
        var['front'].clear()
        var['back'].clear()
        var['decimal'] = False

def n_operation(event:str):
        global var
        var['operator'] = event
        try:
                var['x_val'] = format_number()
        except:
                var['x_val'] = var['result']
        clear_click()

def calculate_click():
        global var
        var['y_val'] = format_number()
        try:
                var['result'] = eval(str(var['x_val']) + var['operator'] + str(var['y_val']))
                update_display(var['result'])
                clear_click()
        except:
                update_display("ERROR! DIV/0")
                clear_click()



while True:
        event, values = window.read()
        if event is None:
                break
        if event in ['0','1','2','3','4','5','6','7','8','9']:
                numbers_click(event)
        if event in ['C','CE']:
                clear_click()
                update_display(0.0)
                var['result'] = 0.0
        if event in ['+','-','*','/']:
                 n_operation(event)
        if event == '=':
                calculate_click()
        if event == '.':
                var['decimal'] = True
        if event == '%':
                print(event)
                update_display(var['result'] / 100.0)




