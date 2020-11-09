'''
Registers from the TMC5160 datasheet:
'''
# ===== TMC5160 register set =====

GCONF          =    0x00
GSTAT          =    0x01
IFCNT          =    0x02
SLAVECONF      =    0x03
INP_OUT        =    0x04
X_COMPARE      =    0x05
OTP_PROG       =    0x06
OTP_READ       =    0x07
FACTORY_CONF   =    0x08
SHORT_CONF     =    0x09
DRV_CONF       =    0x0A
GLOBAL_SCALER  =    0x0B
OFFSET_READ    =    0x0C
IHOLD_IRUN     =    0x10
TPOWERDOWN     =    0x11
TSTEP          =    0x12
TPWMTHRS       =    0x13
TCOOLTHRS      =    0x14
THIGH          =    0x15

RAMPMODE        =   0x20
XACTUAL         =   0x21
VACTUAL         =   0x22
VSTART          =   0x23
A1              =   0x24
V1              =   0x25
AMAX            =   0x26
VMAX            =   0x27
DMAX            =   0x28
D1              =   0x2A
VSTOP           =   0x2B
TZEROWAIT       =   0x2C
XTARGET         =   0x2D

VDCMIN          =   0x33
SWMODE          =   0x34
RAMPSTAT        =   0x35
XLATCH          =   0x36
ENCMODE         =   0x38
XENC            =   0x39
ENC_CONST       =   0x3A
ENC_STATUS      =   0x3B
ENC_LATCH       =   0x3C
ENC_DEVIATION   =   0x3D

MSLUT0        = 0x60
MSLUT1        = 0x61
MSLUT2        = 0x62
MSLUT3        = 0x63
MSLUT4        = 0x64
MSLUT5        = 0x65
MSLUT6        = 0x66
MSLUT7        = 0x67
MSLUTSEL      = 0x68
MSLUTSTART    = 0x69
MSCNT         = 0x6A
MSCURACT      = 0x6B
CHOPCONF      = 0x6C
COOLCONF      = 0x6D
DCCTRL        = 0x6E
DRVSTATUS     = 0x6F
PWMCONF       = 0x70
PWMSCALE      = 0x71
PWM_AUTO      = 0x72
LOST_STEPS    = 0x73

# ramp modes (Register TMC5160_RAMPMODE)
MODE_POSITION = 0
MODE_VELPOS   = 1
MODE_VELNEG   = 2
MODE_HOLD     = 3

# limit switch mode bits (Register TMC5160_SWMODE)
SW_STOPL_ENABLE   = 0x0001
SW_STOPR_ENABLE   = 0x0002
SW_STOPL_POLARITY = 0x0004
SW_STOPR_POLARITY = 0x0008
SW_SWAP_LR        = 0x0010
SW_LATCH_L_ACT    = 0x0020
SW_LATCH_L_INACT  = 0x0040
SW_LATCH_R_ACT    = 0x0080
SW_LATCH_R_INACT  = 0x0100
SW_LATCH_ENC      = 0x0200
SW_SG_STOP        = 0x0400
SW_SOFTSTOP       = 0x0800

# Status bits (Register TMC5160_RAMPSTAT)
RS_STOPL         =  0x0001
RS_STOPR         =  0x0002
RS_LATCHL        =  0x0004
RS_LATCHR        =  0x0008
RS_EV_STOPL      =  0x0010
RS_EV_STOPR      =  0x0020
RS_EV_STOP_SG    =  0x0040
RS_EV_POSREACHED =  0x0080
RS_VELREACHED    =  0x0100
RS_POSREACHED    =  0x0200
RS_VZERO         =  0x0400
RS_ZEROWAIT      =  0x0800
RS_SECONDMOVE    =  0x1000
RS_SG            =  0x2000

# Encoderbits (Register TMC5160_ENCMODE)
EM_DECIMAL    = 0x0400
EM_LATCH_XACT = 0x0200
EM_CLR_XENC   = 0x0100
EM_NEG_EDGE   = 0x0080
EM_POS_EDGE   = 0x0040
EM_CLR_ONCE   = 0x0020
EM_CLR_CONT   = 0x0010
EM_IGNORE_AB  = 0x0008
EM_POL_N      = 0x0004
EM_POL_B      = 0x0002
EM_POL_A      = 0x0001


























reg_analog = {}
reg_analog['XTARGET'] = 1
reg_analog['XACTUAL'] = 1
reg_analog['VACTUAL'] = 1
reg_analog['VACTUAL'] = 1
