#!../../bin/linux-arm/RFCalibrationModule

## You may have to change RFCalibrationModule to something else
## everywhere it appears in this file

< envPaths

cd "${TOP}"

epicsEnvSet("P", "RA-RaBO01:RF-LLRFCalSys")

## Register all support components
dbLoadDatabase "dbd/RFCalibrationModule.dbd"
RFCalibrationModule_registerRecordDeviceDriver pdbbase

drvAsynIPPortConfigure("P1", "unix://${TOP}/RFCalibrationModuleSPI/unix-socket")

## Load record instances
dbLoadRecords("db/RFCalibrationModule.db","PORT=P1,P=$(P),A=0")

#save_restoreSet_FilePermissions(0777)

set_savefile_path("$(TOP)/autosave")
 
# Offsets
set_pass0_restoreFile("$(P).sav")
set_pass1_restoreFile("$(P).sav")

cd "${TOP}/iocBoot/${IOC}"
iocInit

cd "${TOP}"
create_monitor_set("$(TOP)/db/RFCalibrationModule.req", 10, "TOP=$(TOP), SAVENAMEPV=$(P):SaveName")
