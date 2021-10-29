from time import sleep

class TrafficLight:
    __color = "dark"

    def runnin(self):
        __color = "red"
        print('traflight now red')
        sleep(7)
        __color = "yellow"
        print('traflight now yellow')
        sleep(2)
        __color = "red"
        print('traflight now green')
        sleep(3)
        __color = "dark"
        print('traflight end work')
tf = TrafficLight()
tf.runnin()