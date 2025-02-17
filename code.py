from time import sleep

from sd_mount import sdmounter
from audioplayer import soundplayer
from buttons import buttoninput
from cfg import buttons

test_interval = .01


s = sdmounter()
a = soundplayer()
b = buttoninput()
playing_state = False


if s.loadcfg('files.ini'):
    buttons = s.loadcfg('files.ini')
    b.update_btns(buttons)
    s.update_btns(buttons)
while True:
    try:
        playfile = None
        result = b.get_btn()
        if result != []:
            if result[0] in buttons:
                if buttons[result[0]]['file'] is not None:
                    playfile = s.get_fn(buttons[result[0]]['file'])
                    if playfile is not None:
                        a.play_file(playfile)
#         sleep(.01)
    except KeyboardInterrupt:
        print('main code loop interrupted')
        a.close()
        
    sleep(test_interval)

