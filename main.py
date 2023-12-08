import RPi.GPIO as GPIO
import time
import board
import adafruit_dht
import psutil

from utils import auth, api

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27, GPIO.IN)

for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()
sensor = adafruit_dht.DHT11(board.D23)

token = auth.get_token("raspberrypi", "password")
id = api.registry_device(token, "raspberry pi zero", "capteur de la nuit de l'info")

while True:
    try:
        temp = sensor.temperature
        humidity = sensor.humidity
        print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))
        day = GPIO.input(27)
        print(day)
        api.push_data(token, id, temp, humidity, day, (45.2598, 1.256))
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error
    time.sleep(2.0)