# Gom Jabbar - gj_processes.py
# Michael D'Argenio
# mjdargen@gmail.com
# https://dargenio.dev
# https://github.com/mjdargen

from pydub import AudioSegment
from pydub.playback import play
from pydub.playback import _play_with_simpleaudio
from gpiozero import DistanceSensor
from gpiozero import AngularServo
from time import sleep


# audio player process
def audio(conn,):
    sleep(5)
    # load clip to play with simple audio
    clip = AudioSegment.from_mp3('gom_jabbar.mp3')
    playback = _play_with_simpleaudio(clip)
    # while it's playing, look for message from other process
    while playback.is_playing():
        if conn.poll():
            msg = conn.recv()
            print(msg)
            playback.stop()
            end = AudioSegment.from_mp3('die.mp3')
            play(end)
            break


# ultrasonic sensor/servo process
# ultrasonic sensor
# VCC   - 5V
# TRIG  - GPIO23
# ECHO  - GPIO24 - needs 330/470GND voltage divider
# GND   - GND (also connected to ground on voltage divider)
# servo
# BROWN - GND
# RED   - 5V
# ORANGE- GPIO17
def ultra(conn, ):
    # initialize servo
    servo = AngularServo(17, min_angle=-90, max_angle=90)
    servo.angle = 90  # move to start position
    sleep(.5)
    servo.detach()  # stop jitter
    sleep(5)  # wait to get situated
    # initialize ultrasonic sensor
    dist_sensor = DistanceSensor(echo=24, trigger=23, queue_len=1)
    count = 0

    while True:
        sleep(.1)
        # check distance
        if ((dist_sensor.distance * 100)) > 20:
            # print(f'Distance: {dist_sensor.distance * 100} cm')
            count += 1
        else:
            count = 0
        # five sequential distances over 40
        if count >= 5:
            # took hand out of the box
            conn.send("Gom Jabbar")
            break

    # move servo to jab
    servo.angle = -90
    sleep(.5)
    servo.detach()  # stop jitter
    sleep(1)
    servo.angle = 90
    sleep(.5)
    servo.detach()  # stop jitter
