# Makefile for Asyn RFCalibrationModule support
#
# Created by root on Mon Jun 17 15:35:02 2019
# Based on the Asyn streamSCPI template

TOP = .
include $(TOP)/configure/CONFIG

DIRS := configure
DIRS += $(wildcard *[Ss]up)
DIRS += $(wildcard *[Aa]pp)
DIRS += $(wildcard ioc[Bb]oot)
DIRS += RFCalibrationModuleSPI

include $(TOP)/configure/RULES_TOP
