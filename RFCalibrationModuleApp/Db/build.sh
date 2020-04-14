#!/bin/bash
./db.py > RFCalibrationModule.db
cat RFCalibrationModule.db | grep record | grep PwrdBm | grep Mon | grep -Po  '(?<=")(.*?)(?="\){)' | sed 's/.*/&\.DESC/' > RFCalibrationModule.req
cat RFCalibrationModule.db | grep record | grep OFSdB | grep -Po  '(?<=")(.*?)(?="\){)' >> RFCalibrationModule.req

