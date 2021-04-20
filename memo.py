###デスクトップに配置するメモ帳、リマインダーを作りたい
###かっこいいUIにしたい

import PySimpleGUI as sg
import subprocess

sg.theme_background_color(color='LightBlue2')
sg.theme_input_text_color(color ='black')
background_color = sg.theme_background_color()
###入力
def Btn(key,image_filename):
    return sg.Button(key=key, image_filename=image_filename, image_size=(25, 25), pad=((10,1),5),button_color=('black','LightBlue2'),border_width=0)
###UIレイアウト
layout1 = [
    [Btn(key='plus',image_filename='images/plus25.png'),Btn('dot',image_filename='images/detail25.png'),Btn('batsu',image_filename='images/delete25.png')],
    [sg.InputText(key=f'-ROW1-',font=('游明朝',11), size=(48,1),pad=((5,0.5),1), border_width=0, background_color=background_color)],
    [sg.InputText(key=f'-ROW2-',font=('游明朝',11), size=(48,1),pad=((5,0.5),1), border_width=0, background_color=background_color)],
    [sg.InputText(key=f'-ROW3-',font=('游明朝',11), size=(48,1),pad=((5,0.5),1), border_width=0, background_color=background_color)],
    [sg.InputText(key=f'-ROW4-',font=('游明朝',11), size=(48,1),pad=((5,0.5),1), border_width=0, background_color=background_color)],
    [sg.InputText(key=f'-ROW5-',font=('游明朝',11), size=(48,1),pad=((5,0.5),1), border_width=0, background_color=background_color)],
    [sg.InputText(key=f'-ROW6-',font=('游明朝',11), size=(48,1),pad=((5,0.5),1), border_width=0, background_color=background_color)],
    [sg.InputText(key=f'-ROW7-',font=('游明朝',11), size=(48,1),pad=((5,0.5),1), border_width=0, background_color=background_color)],
    [Btn(key='a',image_filename='images/plus25.png'),Btn(key='b',image_filename='images/plus25.png')]
    ]
###ウインドウを表示
window = sg.Window('入力', layout1, no_titlebar=True, grab_anywhere=True, keep_on_top=True, margins=(0,0),alpha_channel=0.9)
while True:
    event, values = window.read()
    ###batsuならウインドウを閉じる
    if event in 'batsu':
        break
    ###plusならウインドウを増やす
    elif event in 'plus':
        subprocess.Popen (('python memo.py'), stdout = subprocess.PIPE, shell=True)
window.close()
