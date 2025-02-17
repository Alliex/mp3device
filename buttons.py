from time import sleep
from cfg import buttons
from digitalio import DigitalInOut, Direction, Pull
from adafruit_debouncer import Button

class buttoninput:
    def __init__(self,*args,**kwargs):
        self.btns = {}
        self.btn_status = {}
        self.pins = {}
        for k,v in buttons.items():
            self.btn_status[k] = False
            self.pins[k]=DigitalInOut(v['pin'])
            self.pins[k].direction = Direction.INPUT
            self.pins[k].pull = Pull.DOWN
            self.btns[k] = Button(self.pins[k])
    
    def get_btn(self):
        dn_btns = []
        for bname,btn in self.btns.items():
            btn.update()
            if btn.pressed:
#                 print('[{}] Pressed'.format(bname))
                dn_btns.append(bname)
#             if btn.released:
#                 print('[{}] Released'.format(bname))
#             if btn.short_count:
#                 print('[{}] count: {}'.format(bname,btn.short_count))
        return dn_btns
        
    def do_bname(self):
        for bname,btn in self.btns.items():
            if not btn.value:
                return (bname,buttons[bname]['file'])
            else:
                return False

    def update_btns(self,btns):
        buttons = btns
#         print('s {}, p {}'.format(self.btns,btns)) ##ignore self.btn - it is only button obj - pass files to the right place
#         for k,v in btns.items():
#         for k,v in btns.items():
#             print(v.pressed)
#             if k in self.btns: #buttons here are not buttons there - no files in thbis imp?
#                 self.pins[k].deinit()
#                 print('{} ..'.format(v['file']))
#                 print(buttons[k]['pin']) # = v['file']
#                 DigitalInOut(buttons[k]['pin']).deinit()
#             print('{}, {}'.format(k,v['pin']))
#             print(v['pin'])
#             pin=DigitalInOut(v['pin'])
#             pin.direction = Direction.INPUT
#             pin.pull = Pull.DOWN
#             self.btns[k] = Button(pin)