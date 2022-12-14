# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Glucometer Code
--------------------------------------------------------------------------
License:   
Copyright 2022 Ibrahim Al-Akash

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Use the following hardware components to make a noninvasive NIR-based glucometer:
    - HT16K33 Display
    - Button
    - Red LED
    - Yellow LED
    - Green LED
    - White Indicator LEDs (x2)

Requirements:
    - Hardware:
        - Button
            - Waiting for button press to initiate sensor function
            - Upon completion of glucose measurement, wait for button input
            - Record press time and return
        - Display shows the status of the glucometer and glucose concentration after measurement

    - User Interaction (UI):
        - Needs to be able to initiate glucose reading
            - Can change the units of the glucose concentration displayed from mg/dL to mmol/L if button is pressed
            - Clear the measurement if the button is held for a certain interval
        - Easily interpret the glucose reading as healthy, moderate dysglycemia, or severe dysglycemia

Uses:
    - HT16K33 display library developed in class
        
"""

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC

import ht16k33 as HT16K33
from AS726X import IR_SENSOR

class Sensor():
    """ Sensor """
    clear_time = None
    red_led = None
    yellow_led = None
    green_led = None
    mmol_led = None
    mgdl_led = None
    display = None
    button = None
    ir_sensor = None
    sensor_reading = None

    def __init__(self, clear_time=3.0, button="P2_2",
                red_led="P2_6", yellow_led="P2_4",
                green_led="P2_8", mmol_led="P2_10",
                mgdl_led="P1_6", ir_sensor=0x49,
                ir_bus=2, display_address=0x70,
                display_bus=1):
        """ Initialize variables and set up display """
        self.clear_time = clear_time
        self.button = button
        self.red_led = red_led
        self.yellow_led = yellow_led
        self.green_led = green_led
        self.mmol_led = mmol_led
        self.mgdl_led = mgdl_led
        self.ir_sensor = IR_SENSOR(ir_bus, ir_sensor)
        self.display = HT16K33.HT16K33(display_bus, display_address)

        self._setup()

    # End def

    def _setup(self):
        """ Setup the hardware components """

        # Initialize Display
        self.set_display_dash()

        # Initialize Button
        GPIO.setup(self.button, GPIO.IN)

        # Initialize LEDs
        GPIO.setup(self.red_led, GPIO.OUT)
        GPIO.setup(self.yellow_led, GPIO.OUT)
        GPIO.setup(self.green_led, GPIO.OUT)
        GPIO.setup(self.mmol_led, GPIO.OUT)
        GPIO.setup(self.mgdl_led, GPIO.OUT)

        # IR Sensor is initialized when object is created

    # End def

    def set_display_dash(self):
        """Set display to word "----" """
        self.display.text("----")

    # End def

    def glucose_concentration(self):
        """Calculate glucose concentration from sensor NIR spectroscopy measurement"""
        pass

    # End def

    def read_sensor(self):
        """Read sensor value and save to object"""
        value = self.ir_sensor.take_measurements()
        self.sensor_reading = value

    # End def



