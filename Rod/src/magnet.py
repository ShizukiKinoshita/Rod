#磁石センサーによる竿の操作
from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory
from signal import pause
import vibration as vib
import time

# SENSOR PIN
PIN_MAGNET = 21
# GPIOモードを設定
GPIO.setmode(GPIO.BCM)

def main():
    # ピンを入力に設定(プルアップ設定)
    factory = PiGPIOFactory()
    magnet = Button(PIN_MAGNET, pull_up=True, bounce_time=3, pin_factory=factory) #最初の変更があってから、状態の変更を無視する時間をbounce_timeで秒単位で指定
    vibration = vib.Vibration()

    def stick():
        vibration.motor_on
        print("magnets stick")

    def leave():
        vibration.motor_off
        print("magnets leave")

    magnet.when_pressed = stick
    magnet.when_released = leave
    pause()

    return

if __name__ == "__main__": #直接このシートを実行したらmain()を動かすようにする。スクリプトを他のモジュールとしてインポートした場合、動作部分が自動的に実行されることを防ぐことができる。
    main()
