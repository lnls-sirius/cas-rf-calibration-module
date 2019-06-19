TOP=..
include $(TOP)/configure/CONFIG
#=======================================
.PHONY: install-dependencies

install-dependencies:
	/usr/bin/python3 db.py > RFCalibrationModule.db
# Install .dbd and .db files
DB_INSTALLS += $(TOP)/RFCalibrationModuleSup/RFCalibrationModule.db
DB_INSTALLS += $(TOP)/RFCalibrationModuleSup/RFCalibrationModule.proto

#=======================================
include $(TOP)/configure/RULES
