import time
#data sheet
min_hz=24
max_hz=1526 
max_step=4096 #12 bit
min_color=0
max_color=255
def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min + 1) / (in_max - in_min + 1) + out_min

class LedPCA9685_single(object):
    def __init__(self, pca9685, channel):
        self.pca9685 = pca9685
        self.channel = channel
        self.set_pwm_freq(1000)
        #self.set_pulse(300)
    def set_pwm_freq(self, freq):
        if(freq>=min_hz and freq<=max_hz):
            self.pca9685.set_pwm_freq(freq)
            time.sleep(0.005)
        else:
            print("out of range hz")
    def set_on_cycle(self,on):
        if(on>=0 and on <=100):
            on_time=on
        elif on <0:
            on_time=0
        elif on>100:
            on_time=100 
        time_off =map(on_time,0,99,0,4095)
        time_off=int(time_off)
        self.pca9685.set_pwm(self.channel,0,time_off) # high on 0 and off on time_off
    def disable(self):
        self.pca9685.set_pwm(self.channel, 0, 0)
        time.sleep(0.005)
    def reset_all(self):
        self.pca9685.reset()
class LedPCA9685_rgb(object):
    def __init__(self, pca9685, channel1,channel2,channel3):
        self.pca9685 = pca9685
        self.channel1 = channel1
        self.channel2 = channel2
        self.channel3 = channel3
        self.set_pwm_freq(1000)
        #self.set_pulse(300)
    def set_pwm_freq(self, freq):
        if(freq>=min_hz and freq<=max_hz):
            self.pca9685.set_pwm_freq(freq)
            time.sleep(0.005)
        else:
            print("out of range hz")
    def set_on_cycle(self,channel,on):
        if(on>=min_color and on <=max_color):
            on_time=on
        elif on <min_color:
            on_time=min_color
        elif on>max_color:
            on_time=max_color 
        time_off =map(on_time,min_color,max_color,0,4095)
        time_off=int(time_off)
        self.pca9685.set_pwm(channel,0,time_off) # high on 0 and off on time_off
    def set_rgb_value(self,r,g,b):
        self.set_on_cycle(self.channel1,r)
        self.set_on_cycle(self.channel2,g)
        self.set_on_cycle(self.channel3,b)