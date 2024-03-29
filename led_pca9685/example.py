import time
import smbus
import PCA9685
import LedPCA9685

i2cBus = smbus.SMBus(1) # 0 ,1
pca9685 = PCA9685.PCA9685(i2cBus)
led00 = LedPCA9685.LedPCA9685_single(pca9685, PCA9685.CHANNEL00)
led01 = LedPCA9685.LedPCA9685_single(pca9685, PCA9685.CHANNEL01)
led02 = LedPCA9685.LedPCA9685_single(pca9685, PCA9685.CHANNEL02)
led_rgb1=LedPCA9685.LedPCA9685_rgb(pca9685,PCA9685.CHANNEL03,PCA9685.CHANNEL04,PCA9685.CHANNEL05)
# all on
#pca9685.all_pwm_set(50) # 50%
led00.set_on_cycle(50)
led01.set_on_cycle(75)
led02.set_on_cycle(25)
print("mode1")
time.sleep(2)
print("mode2")
led_rgb1.set_rgb_value(255,100,255)
time.sleep(2)


    

