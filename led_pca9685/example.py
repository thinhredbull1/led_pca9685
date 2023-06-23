import time
import smbus
import PCA9685
import LedPCA9685

i2cBus = smbus.SMBus(0) # 0 ,1
pca9685 = PCA9685.PCA9685(i2cBus)
led00 = LedPCA9685.LedPCA9685(pca9685, PCA9685.CHANNEL00)
led01 = LedPCA9685.LedPCA9685(pca9685, PCA9685.CHANNEL01)
led02 = LedPCA9685.LedPCA9685(pca9685, PCA9685.CHANNEL02)
# all on
LedPCA9685.all_pwm_set(50) # 50%
time.sleep(2)
led00.disable() # 0%
led01.disable()
led02.disable()
for i in range(0,100,2):
    led00.set_on_cycle(i)
    led01.set_on_cycle(i+2)
    led02.set_on_cycle(i+4)
    

