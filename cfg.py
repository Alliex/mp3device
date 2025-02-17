import board

#SD Card
DEF_MOSI = board.GP11
DEF_MISO = board.GP8
DEF_CLK = board.GP10
DEF_CS = board.GP9
SD_DIR = '/sd'

#audio amp
i2s_clk = board.GP0
i2s_ws = board.GP1
i2s_d = board.GP2

#buttons
buttons = {'button_1':{'pin':board.GP3,
                       'file':'entertainer.mp3'},
           'button_2':{'pin':board.GP4,
                       'file':'itsbeen.mp3'},
           'button_3':{'pin':board.GP5,
                       'file':'somebody.mp3'},
           'button_4':{'pin':board.GP7,
                       'file':'mario.mp3'},
           'button_5':{'pin':board.GP18,
                       'file':None},
           'button_6':{'pin':board.GP19,
                       'file':None},
           'button_7':{'pin':board.GP20,
                       'file':None},
           }