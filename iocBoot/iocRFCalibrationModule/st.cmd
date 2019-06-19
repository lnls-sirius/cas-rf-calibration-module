#!../../bin/linux-arm/RFCalibrationModule

## You may have to change RFCalibrationModule to something else
## everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/RFCalibrationModule.dbd"
RFCalibrationModule_registerRecordDeviceDriver pdbbase

drvAsynIPPortConfigure("P1", "unix://${TOP}/RFCalibrationModuleSPI/unix-socket")

## Load record instances
dbLoadRecords("db/RFCalibrationModule.db","PORT=P1, A=0")

cd "${TOP}/iocBoot/${IOC}"
iocInit
