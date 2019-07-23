TOP=../..
include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#----------------------------------------------------
#  Optimization of db files using dbst (DEFAULT: NO)
#DB_OPT = YES

#----------------------------------------------------
# Create and install (or just install) into <top>/db
# databases, templates, substitutions like this
#DB += xxx.db

#----------------------------------------------------
# If <anyname>.db template is not named <anyname>*.template add
# <anyname>_template = <templatename>

.PHONY: db
db:
	/usr/bin/python3 db.py > RFCalibrationModule.db
	cat RFCalibrationModule.db | grep record | grep PwrdBm | grep Mon | grep -Po  '(?<=")(.*?)(?="\){)' | sed 's/.*/&\.DESC/' > RFCalibrationModule.req
	cat RFCalibrationModule.db | grep record | grep OFSdB | grep -Po  '(?<=")(.*?)(?="\){)' >> RFCalibrationModule.req

# Install .dbd and .db files
DB += RFCalibrationModule.db
DB += RFCalibrationModule.proto
DB += RFCalibrationModule.req

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

