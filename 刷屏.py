from pynput.keyboard import Key,Controller
import time
import pyautogui as gui
def keyboard_input(string):
    '''
    :param string: 你想要发送的信息
    :return: None
    '''
   
    #导入相应的库
    次数=int(input("请输入你要轰炸的次数:"))
    time.sleep(2)
    gui.hotkey('ctrl','alt','z')
    while True:
      keyboard = Controller() #开始控制键盘
      keyboard.type(string) #键盘输入string
      gui.hotkey('enter')
      次数-=1
      if 次数==0:
          break
    return None
a=input("你想说什么:")
if __name__=="__main__":
    keyboard_input(a)
