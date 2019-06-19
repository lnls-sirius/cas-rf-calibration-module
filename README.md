# Sirius RF calibration module IOC
## Dependencies
The following are required

|Module|Path|
|:----:|:---|
|ASYN|/opt/epics-R3.15.5/modules/asyn4-35|
|STREAM|/opt/epics-R3.15.5/modules/StreamDevice-2.8.8|
|AUTOSAVE|/opt/epics-R3.15.5/modules/autosave-R5-9|
|CALC|/opt/epics-R3.15.5/modules/synApps/calc-R3-7-1|
|EPICS_BASE|/opt/epics-R3.15.5/base|

## Installing
```
cd RFCalibrationModuleSup
make install-dependencies
cd ..
make
```
Installing the services

```
cp services/cas-rf-calibration-module-spi.service /etc/systemd/system
cp services/cas-rf-calibration-module-ioc.service /etc/systemd/system

systemctl daemon-reload
systemctl start 

systemctl enable cas-rf-calibration-module-spi.service
systemctl enable cas-rf-calibration-module-ioc.service

systemctl start cas-rf-calibration-module-spi.service
systemctl start cas-rf-calibration-module-ioc.service
```
Error check
```
systemctl status cas-rf-calibration-module-spi.service
systemctl status cas-rf-calibration-module-ioc.service
```

## Running
To manually run first start the SPI interface (`-h` will show additional information)
```
cd RFCalibrationModuleSPI/
./run.py
```
Start the IOC
```
cd iocBoot/iocRFCalibrationModule/
./st.cmd
```
