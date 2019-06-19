TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = RFCalibrationModule
# RFCalibrationModule.dbd will be created and installed
DBD += RFCalibrationModule.dbd

# RFCalibrationModule.dbd will be made up from these files:
RFCalibrationModule_DBD += base.dbd
RFCalibrationModule_DBD += calcSupport.dbd
RFCalibrationModule_DBD += asSupport.dbd

RFCalibrationModule_DBD += asyn.dbd
RFCalibrationModule_DBD += stream.dbd
RFCalibrationModule_DBD += drvAsynSerialPort.dbd
RFCalibrationModule_DBD += drvAsynIPPort.dbd

# Include dbd files from all support applications:
#RFCalibrationModule_DBD += xxx.dbd

# Add all the support libraries needed by this IOC
RFCalibrationModule_LIBS += calc
RFCalibrationModule_LIBS += autosave
RFCalibrationModule_LIBS += asyn
RFCalibrationModule_LIBS += calc
RFCalibrationModule_LIBS += stream

# RFCalibrationModule_registerRecordDeviceDriver.cpp derives from RFCalibrationModule.dbd
RFCalibrationModule_SRCS += RFCalibrationModule_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
RFCalibrationModule_SRCS_DEFAULT += RFCalibrationModuleMain.cpp
RFCalibrationModule_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#RFCalibrationModule_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
RFCalibrationModule_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

