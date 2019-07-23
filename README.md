# Sirius RF calibration module IOC
Authors: Claudio Carneiro, Eduardo Coelho
 
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
The user should clone this repo at `/opt`
### procServ
Get the procServ-v2.8.0 tar file from [https://github.com/ralphlange/procServ/releases/download/v2.8.0/procServ-2.8.0.tar.gz](procServ-2.8.0)

```
wget https://github.com/ralphlange/procServ/releases/download/v2.8.0/procServ-2.8.0.tar.gz
tar -zxvf procServ-2.8.0.tar.gz
cd procServ-2.8.0
./configure --enable-access-from-anywhere
make install
cd ..
rm -rf procServ-2.8.0.tar.gz procServ-2.8.0
```
### User permission
This repository should be cloned at /opt
Make sure that the user iocuser is created and is part of dialout and ioc groups
Check the repository permisson

```
useradd  iocuser
groupadd ioc
usermod -aG ioc	    iocuser
usermod -aG gpio    iocuser
usermod -aG dialout iocuser

chown -R iocuser:ioc cas-rf-calibration-module
```
### Compiling

```
cd RFCalibrationModuleSup
make db
cd ..
make
```
Installing the services

```
cp services/cas-rf-calibration-module-spi.service /etc/systemd/system
cp services/cas-rf-calibration-module-ioc.service /etc/systemd/system

systemctl daemon-reload
systemctl start cas-rf-calibration-module-spi.service
systemctl start cas-rf-calibration-module-ioc.service

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
## Calibration Constants
In order to modify the calibration constants edit [RFCalibrationModuleSup/db.py](RFCalibrationModuleSup/db.py), update the EPICS database files and restart the IOC
```
make clean
make distclean
make
systemctl start cas-rf-calibration-module-ioc.service
```
