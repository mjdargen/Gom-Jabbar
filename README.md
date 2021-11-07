# Gom-Jabbar
Recreate the pivotal scene from Dune using a Raspberry Pi, ultrasonic sensor, servo, and a bit of Python code!

*Michael D'Argenio  
mjdargenio@gmail.com  
https://dargen.io  
https://github.com/mjdargen  
Created: November 11, 2021*   

Here is a video demo of the project:  
[![Gom Jabbar Demo](https://img.youtube.com/vi/v0kx15oTRYM/0.jpg)](https://www.youtube.com/watch?v=v0kx15oTRYM)

In this tutorial, I will walk you through the process of creating the black box in the pivotal scene from Dune where the Reverend Mother Gaius Helen Mohiam tests Paul Atreides. The Gom Jabbar is the name for the handheld needle tipped with meta-cyanide poison. When driven into a victim, it brings almost instantaneous death. The Gom Jabbar test was used to determine whether an individual's awareness was stronger than their animal instincts. If their awareness of the Gom Jabbar's presence was strong enough, it would override their instincts to withdraw from the immense pain of the test.  

In this project, I created a Python script that uses gpiozero to interface with an HC-SR04 ultrasonic sensor to detect the presence of a hand and a servo to actuate the Gom Jabbar. Multiple processes are used: one for playing the audio and the other to constantly check the ultrasonic sensor to see whether the hand has been removed from the box and actuate the servo motor with the pin.

To run this code in your environment, you will need to:  
   * Install Python 3 and pip
   * Install ffmpeg for pydub
   * Install python dependencies: pydub, simpleaudio, pigpio

You can do this on your own or use the script I provide for you. To use the script, complete the following steps:
  * Make the script executable - `sudo chmod +x ./install.sh`
  * Run the script - `./install.sh`

Video demo: https://www.youtube.com/watch?v=v0kx15oTRYM

For a complete walkthrough of how this program works, you can go here: [Instructables Tutorial](https://www.instructables.com/Gom-Jabbar-From-Dune/).
