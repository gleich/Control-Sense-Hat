# Control-Sense-Hat

Control you Raspberry Pi Sense hat from inside a docker container!

## Setup

As long as you have docker and docker-compose installed on your raspberry pi all you need to do is run the following:

1. `sh init.sh` (This sets up the files that you can read from another container with. More explained below)
2. `docker-compose up -d`

## How it works

This application reads the data from the sense hat every second and writes it to two files located in a folder called `sense_hat_containerized` located at `~`

### `data.json`

Data from the sense hat including:

1. Temperature
2. Pressure
3. Humidity
4. Orientation
    * Pitch
    * Roll
    * Yaw

An example is shown below:

```json
{
  "pressure": 992.531005859375,
  "orientation_degrees": {
    "yaw": 118.81641351841105,
    "roll": 93.25158236075444,
    "pitch": 0.460498023948871
  },
  "temperature": 40.61878967285156,
  "humidity": 17.378620147705078
}
```

### `leds.json`

RGB values for every single LED in the 8x8 Matrix on the sense hat. Change the values in this file to change the values on the sense hat. The LEDs go in order of left to right, top to bottom. Below is an example where every light it green:

```json
[
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0],
  [0, 250, 0]
]
```
