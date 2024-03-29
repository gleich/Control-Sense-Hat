from sense_hat import SenseHat
import os
from os import system
import json
from time import sleep

os.chdir("./sense_hat_containerized")
# Writing templates
data_template = {
    "humidity": 0.0,
    "temperature": 0.0,
    "pressure": 0.0,
    "orientation_degrees": {}
}
leds_template = []
for i in range(64):
    leds_template.append((0, 0, 0))
with open("data.json", "w") as data_json_init:
    json.dump(data_template, data_json_init)
with open("leds.json", "w") as leds_json_init:
    json.dump(leds_template, leds_json_init)
# Init sense hat
sense = SenseHat()
sense.clear()
while True:
    # Gathering data and writing to data.json
    system("clear")
    data_template["temperature"] = sense.get_temperature()
    data_template["pressure"] = sense.get_pressure()
    data_template["humidity"] = sense.get_humidity()
    data_template["orientation_degrees"] = sense.get_orientation_degrees()
    with open("data.json", "w") as data_json:
        json.dump(data_template, data_json)
    # Gathering and setting LEDs
    with open("leds.json") as leds_json:
        led_matrix_config = json.load(leds_json)
    x = 0
    y = 0
    for i in range(64):
        sense.set_pixel(
            x, y, led_matrix_config[i][0], led_matrix_config[i][1], led_matrix_config[i][2])
        if x == 7:
            x = 0
            y += 1
        else:
            x += 1
    sleep(5)
