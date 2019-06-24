TOP=..
include $(TOP)/configure/CONFIG
#=======================================

.PHONY: db
db:
	/usr/bin/python3 db.py > RFCalibrationModule.db
	cat RFCalibrationModule.db | grep record | grep PwrdBm | grep Mon | grep -Po  '(?<=")(.*?)(?="\){)' | sed 's/.*/&\.DESC/' > RFCalibrationModule.req
	cat RFCalibrationModule.db | grep record | grep OFSdB | grep -Po  '(?<=")(.*?)(?="\){)' >> RFCalibrationModule.req

# Install .dbd and .db files
DB_INSTALLS += $(TOP)/RFCalibrationModuleSup/RFCalibrationModule.db
DB_INSTALLS += $(TOP)/RFCalibrationModuleSup/RFCalibrationModule.proto
DB_INSTALLS += $(TOP)/RFCalibrationModuleSup/RFCalibrationModule.req

#=======================================
include $(TOP)/configure/RULES
