import array
import math
import audiocore
import audiomp3
import audiobusio

from time import sleep

from cfg import i2s_clk, i2s_ws, i2s_d

class soundplayer:
    def __init__(self,*args,**kwargs):
        self.audio = audiobusio.I2SOut(i2s_clk,i2s_ws,i2s_d)
        self.is_playing = False
        self.playing_file = None
        
    def test_tone(self,length=None): #unused, for testing
        if length is None:
            pausetime=1
        else:
            pausetime = length
        tone_volume = 0.1  # Increase this to increase the volume of the tone.
        frequency = 440  # Set this to the Hz of the tone you want to generate.
        length = 8000 // frequency
        sine_wave = array.array("h", [0] * length)
        for i in range(length):
            sine_wave[i] = int((math.sin(math.pi * 2 * i / length)) * tone_volume * (2 ** 15 - 1))
        sine_wave_sample = audiocore.RawSample(sine_wave)
        self.audio.play(sine_wave_sample, loop=True)
        sleep(pausetime)
        self.audio.stop()
    
    def get_play_status(self):
        return self.is_playing
    
    def play_file(self,file):
        try:
            if self.audio.playing:
                self.audio.stop()
                self.playing_file = None
#                 print('stopped by button')
            else:
                mp3 = audiomp3.MP3Decoder(open(file, "rb"))
                self.audio.play(mp3)
                self.playing_file = file
#                 print('playing {}'.format(file))
        except KeyboardInterrupt:
            self.close()
            print('audio loop interrupted')
    
    def interrupt_play(self):
        self.interrupted = True
    
    def close(self,*args,**kwargs):
        if self.audio.playing:
            self.audio.stop()