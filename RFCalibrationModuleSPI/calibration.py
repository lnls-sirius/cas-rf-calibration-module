#!/usr/bin/python
# -*- coding: utf-8 -*-

import Adafruit_BBIO.GPIO as GPIO
import converters
import threading
import time

class RF_Calibration_Module():

    def __init__(self):
        self.ADC1 = converters.ADC()
        self.ADC2 = converters.ADC2()

    def read(self):
        ADC1_values = [0.0] * 8
        ADC2_values = [0.0] * 8

        for i in range(10):
            ADC1_readings = self.ADC1.read(range(8))
            ADC2_readings = self.ADC2.read(range(8))
            for j in range(8):
                ADC1_values[j] += ADC1_readings[j]
                ADC2_values[j] += ADC2_readings[j]

        return str([1] + ADC1_values + ADC2_values)
