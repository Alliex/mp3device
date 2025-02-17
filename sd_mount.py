import busio
import sdcardio
import storage
from os import listdir

from time import sleep

from cfg import DEF_MOSI, DEF_MISO, DEF_CLK, DEF_CS,SD_DIR, buttons


class sdmounter:
    def __init__(self,*args,**kwargs):
        self.spi = busio.SPI(DEF_CLK, MOSI=DEF_MOSI, MISO=DEF_MISO)
        self.cs = DEF_CS
        self.sdcard = sdcardio.SDCard(self.spi, self.cs)
        self.vfs = storage.VfsFat(self.sdcard)
        storage.mount(self.vfs, SD_DIR)
        self.file_list = listdir('{}/'.format(SD_DIR))
        sleep(.2)
        print('SD Card Mounted')
    
    def listfiles(self):
        print('Files: {}'.format(listdir('{}/'.format(SD_DIR))))
    
    def get_fn(self,fn):
        if fn in self.file_list:
            r = '{}/{}'.format(SD_DIR,fn)
        else:
            r = None
        return r
    
    def loadcfg(self,fn):
        fl = {}
        try:
            with open('{}/{}'.format(SD_DIR,fn), 'r') as fp:
                f = fp.readlines()
            for line in f:
                parsedline = line.split(':')
                if 'button_{}'.format(parsedline[0]) in buttons:
                    fl['button_{}'.format(parsedline[0])]={}
                    fl['button_{}'.format(parsedline[0])]['file']=parsedline[1].strip().strip('"')
                    fl['button_{}'.format(parsedline[0])]['pin']=buttons['button_{}'.format(parsedline[0])]['pin']
            if fl != {}:
                return fl
            else:
                return False
        except OSError as e:
            print('error: {}'.format(e))
            return False
    
    def update_btns(self,btns):
        buttons = btns

    def savefile(self,fn):
        pass