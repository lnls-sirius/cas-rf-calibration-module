#!/usr/bin/python3
from string import Template

wf = Template('''
record(stringin, "$(P):SaveName"){
    field(VAL,  "$(P).sav")
    field(PINI, "YES")
    field(DESC, "Autosave destination file")
}

record(waveform, "${PV_VALS}"){
    field(DTYP, "stream")
    field(SCAN, ".5 second")
    field(DTYP, "stream")
    field(INP,  "@RFCalibrationModule.proto getData $(PORT) $(A)")
    field(FTVL, "FLOAT")
    field(NELM, "17")
}

record(calc, "${PV_VALS}_enbl"){
   field(CALC, "A#0")
   field(INPA, "${PV_VALS}.STAT CP")
   field(INPB, "${PV_VALS} CP")
}

''')

'''
:param PV:
:param PV_VALS:
:param N:
:param MIN:
:param p5:
:param p4:
:param p3:
:param p2:
:param p1:
'''
adc = Template('''
record(calc, "${PV}${N}_ADC"){
    field(CALC, "((A/10)/4095.)*5.")
    field(INPA, "${PV_VALS}.VAL[${N}] CP MSS")

}

record(calc, "${PV}${N}_CALC"){
    field(CALC, "A*(F**4) + B*(F**3) + C*(F**2) + D*F + E")

    field(INPA, "${p5}")
    field(INPB, "${p4}")
    field(INPC, "${p3}")
    field(INPD, "${p2}")
    field(INPE, "${p1}")

    field(INPF, "${PV}${N}_ADC CP MSS")
    
    field(DISV, "1")
    field(DISS, "INVALID")
    field(SDIS, "${PV_VALS}_enbl")
}

record(ao, "${PV_OFS}${N}-Mon"){
    field(PREC, "2")
    field(EGU,  "dB")
    field(VAL,  "0")
    field(PINI, "YES")
}

record(calc, "${PV}${N}-Mon"){
    field(CALC, "(A>${MIN})?(A + B):(-Inf)")
    field(INPA, "${PV}${N}_CALC CP MSS")
    field(INPB, "${PV_OFS}${N}-Mon CP MSS")
    field(PREC, "2")
    field(EGU,  "dBm")
    field(DISV, "1")
    field(DISS, "INVALID")
    field(SDIS, "${PV_VALS}_enbl")
}

record(calc, "${PV_W}${N}-Mon"){
    field(CALC, "(10**(A/10))*(1/1000)")
    field(INPA, "${PV}${N}-Mon CP MSS")
    field(PREC, "2")
    field(EGU,  "W")
    field(DISV, "1")
    field(DISS, "INVALID")
    field(SDIS, "${PV_VALS}_enbl")
}
''')

on_off = Template('''
record(mbbi, "${PV_STAT}"){
    field(INP, "${PV_VALS}.VAL[0] CP MSS")

    field(ZRVL, "0")
    field(ONVL, "1")

    field(ZRST, "Off")
    field(ONST, "On")
}
''')

if __name__ == '__main__':
    PV_VALS = 'RA-RaBO01:RF-LLRFCalSys:Vals'
    PV_STAT = 'RA-RaBO01:RF-LLRFCalSys:StatusCalOn'
    PV      = 'RA-RaBO01:RF-LLRFCalSys:PwrdBm'
    PV_W    = 'RA-RaBO01:RF-LLRFCalSys:PwrW'
    PV_OFS  = 'RA-RaBO01:RF-LLRFCalSys:OFSdB'
    MIN     = str(-41.)

    # WF
    kwargs = {'PV_STAT':PV_STAT, 'PV_VALS':PV_VALS}
    print(wf.safe_substitute(**kwargs))

    # On/Off
    kwargs = {'N':0, 'MIN':MIN, 'PV':PV, 'PV_STAT':PV_STAT, 'PV_VALS':PV_VALS}
    print(on_off.safe_substitute(**kwargs))

    # Power Readings

    # Channel 1 (ADC PCB 1, CH1)
    kwargs = {'N':1, 'MIN': MIN, 'PV':PV, 'PV_VALS':PV_VALS, 'PV_OFS':PV_OFS, 'PV_W':PV_W}
    kwargs['p1'] = 26.307
    kwargs['p2'] = 7.6581
    kwargs['p3'] = -53.648
    kwargs['p4'] = 26.107
    kwargs['p5'] = -4.6759
    print(adc.safe_substitute(**kwargs))

    # Channel 2 (ADC PCB 1, CH1)
    kwargs = {'N':2, 'MIN': MIN, 'PV':PV, 'PV_VALS':PV_VALS, 'PV_OFS':PV_OFS, 'PV_W':PV_W}
    kwargs['p1'] = 29.637
    kwargs['p2'] = -2.9709
    kwargs['p3'] = -39.974
    kwargs['p4'] = 18.446
    kwargs['p5'] = -3.1204
    print(adc.safe_substitute(**kwargs))

    # Channel 3 (ADC PCB 1, CH2)
    kwargs = {'N':3, 'MIN': MIN, 'PV':PV, 'PV_VALS':PV_VALS, 'PV_OFS':PV_OFS, 'PV_W':PV_W}
    kwargs['p1'] = 23.264
    kwargs['p2'] = 17.234
    kwargs['p3'] = -65.181
    kwargs['p4'] = 32.361
    kwargs['p5'] = -5.9411
    print(adc.safe_substitute(**kwargs))

    # Channel 4 (ADC PCB 1, CH3)
    kwargs = {'N':4, 'MIN': MIN, 'PV':PV, 'PV_VALS':PV_VALS, 'PV_OFS':PV_OFS, 'PV_W':PV_W}
    kwargs['p1'] = 29.996
    kwargs['p2'] = -2.412
    kwargs['p3'] = -41.851
    kwargs['p4'] = 20.226
    kwargs['p5'] = -3.6413
    print(adc.safe_substitute(**kwargs))

    # Channel 5 (ADC PCB 1, CH4)
    kwargs = {'N':5, 'MIN': MIN, 'PV':PV, 'PV_VALS':PV_VALS, 'PV_OFS':PV_OFS, 'PV_W':PV_W}
    kwargs['p1'] = 24.592
    kwargs['p2'] = 13.793
    kwargs['p3'] = -60.338
    kwargs['p4'] = 29.492
    kwargs['p5'] = -5.3428
    print(adc.safe_substitute(**kwargs))

    # Channel 6 (ADC PCB 1, CH5)
    kwargs = {'N':6, 'MIN': MIN, 'PV':PV, 'PV_VALS':PV_VALS, 'PV_OFS':PV_OFS, 'PV_W':PV_W}
    kwargs['p1'] = 23.949
    kwargs['p2'] = 15.762
    kwargs['p3'] = -62.507
    kwargs['p4'] = 30.325
    kwargs['p5'] = -5.4278
    print(adc.safe_substitute(**kwargs))

    # Channel 7 (ADC PCB 1, CH6)
    kwargs = {'N':7, 'MIN': MIN, 'PV':PV, 'PV_VALS':PV_VALS, 'PV_OFS':PV_OFS, 'PV_W':PV_W}
    kwargs['p1'] = 25.86
    kwargs['p2'] = 9.2711
    kwargs['p3'] = -56.011
    kwargs['p4'] = 27.684
    kwargs['p5'] = -5.077
    print(adc.safe_substitute(**kwargs))

    # Channel 8 (ADC PCB 1, CH7)
    kwargs = {'N':8, 'MIN': MIN, 'PV':PV, 'PV_VALS':PV_VALS, 'PV_OFS':PV_OFS, 'PV_W':PV_W}
    kwargs['p1'] = 26.347
    kwargs['p2'] = 6.0158
    kwargs['p3'] = -49.13
    kwargs['p4'] = 22.541
    kwargs['p5'] = -3.8038
    print(adc.safe_substitute(**kwargs))

    # Channel 9 (ADC PCB 2, CH0)
    kwargs = {'N':9, 'MIN': MIN, 'PV':PV, 'PV_VALS':PV_VALS, 'PV_OFS':PV_OFS, 'PV_W':PV_W}
    kwargs['p1'] = 24.396
    kwargs['p2'] = 12.915
    kwargs['p3'] = -57.398
    kwargs['p4'] = 26.944
    kwargs['p5'] = -4.6637
    print(adc.safe_substitute(**kwargs))

    # Channel 10 (ADC PCB 2, CH1)
    kwargs = {'N':10, 'MIN': MIN, 'PV':PV, 'PV_VALS':PV_VALS, 'PV_OFS':PV_OFS, 'PV_W':PV_W}
    kwargs['p1'] = 26.928
    kwargs['p2'] = 5.7414
    kwargs['p3'] = -50.567
    kwargs['p4'] = 24.195
    kwargs['p5'] = -4.2941
    print(adc.safe_substitute(**kwargs))

    # Channel 11 (ADC PCB 2, CH2)
    kwargs = {'N':11, 'MIN': MIN, 'PV':PV, 'PV_VALS':PV_VALS, 'PV_OFS':PV_OFS, 'PV_W':PV_W}
    kwargs['p1'] = 24.27
    kwargs['p2'] = 13.93
    kwargs['p3'] = -59.559
    kwargs['p4'] = 28.652
    kwargs['p5'] = -5.1056
    print(adc.safe_substitute(**kwargs))

    # Channel 12 (ADC PCB 2, CH3)
    kwargs = {'N':12, 'MIN': MIN, 'PV':PV, 'PV_VALS':PV_VALS, 'PV_OFS':PV_OFS, 'PV_W':PV_W}
    kwargs['p1'] = 23.393
    kwargs['p2'] = 17.506
    kwargs['p3'] = -65.01
    kwargs['p4'] = 31.765
    kwargs['p5'] = -5.7288
    print(adc.safe_substitute(**kwargs))

    # Channel 13 (ADC PCB 2, CH4)
    kwargs = {'N':13, 'MIN': MIN, 'PV':PV, 'PV_VALS':PV_VALS, 'PV_OFS':PV_OFS, 'PV_W':PV_W}
    kwargs['p1'] = 25.407
    kwargs['p2'] = 10.57
    kwargs['p3'] = -56.513
    kwargs['p4'] = 27.402
    kwargs['p5'] = -4.9173
    print(adc.safe_substitute(**kwargs))

    # Channel 14 (ADC PCB 2, CH5)
    kwargs = {'N':14, 'MIN': MIN, 'PV':PV, 'PV_VALS':PV_VALS, 'PV_OFS':PV_OFS, 'PV_W':PV_W}
    kwargs['p1'] = 26.805
    kwargs['p2'] = 6.3015
    kwargs['p3'] = -50.449
    kwargs['p4'] = 23.956
    kwargs['p5'] = -4.2051
    print(adc.safe_substitute(**kwargs))

    # Channel 15 (ADC PCB 2, CH6)
    kwargs = {'N':15, 'MIN': MIN, 'PV':PV, 'PV_VALS':PV_VALS, 'PV_OFS':PV_OFS, 'PV_W':PV_W}
    kwargs['p1'] = 24.922
    kwargs['p2'] = 10.916
    kwargs['p3'] = -56.348
    kwargs['p4'] = 27.076
    kwargs['p5'] = -4.7969
    print(adc.safe_substitute(**kwargs))

    # Channel 16 (ADC PCB 2, CH7)
    kwargs = {'N':16, 'MIN': MIN, 'PV':PV, 'PV_VALS':PV_VALS, 'PV_OFS':PV_OFS, 'PV_W':PV_W}
    kwargs['p1'] = 20.502
    kwargs['p2'] = 25.687
    kwargs['p3'] = -73.787
    kwargs['p4'] = 35.747
    kwargs['p5'] = -6.3593
    print(adc.safe_substitute(**kwargs))
