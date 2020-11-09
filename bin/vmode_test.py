import signal
import sys
import time

from tmc_uart import TMC5160_UART
from tmc_uart import tmc5160_reg as reg

from pprint import pprint
      
# --- need to stop motor if cntl-c
def signal_handler(sig, frame):
    drv.write_reg(mtr_id, reg.VMAX, 0)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# check for required comm device input
try:
    dev_file = sys.argv[1]
except:
    print("\nSpecify device eg:\n >python tmc_uart.py COM7")
    sys.exit(1)
drvconf = { 'comm_dev':dev_file, 'baud':500000 }

drv = TMC5160_UART(drvconf)
mtr_id = 0

# Reset
#drv.write_reg(mtr_id, reg.GSTAT, 7);

rst = drv.write_reg(0,reg.GCONF,0x0000000C)
rst = drv.read_reg(0, reg.GCONF)
print("GONF = ",rst)
# MULTISTEP_FILT=1, EN_PWM_MODE=1 enables stealthChop™
drv.write_reg(mtr_id, reg.GCONF, 0x0000000C);
# TOFF=3, HSTRT=4, HEND=1, TBL=2, CHM=0 (spreadCycle™)
drv.write_reg(mtr_id, reg.CHOPCONF, 0x000100C3);
# IHOLD=8, IRUN=15 (max. current), IHOLDDELAY=6
#drv.write_reg(mtr_id, reg.IHOLD_IRUN, 0x00080F0A);
drv.write_reg(mtr_id, reg.IHOLD_IRUN, 0x00087F0A);
# TPOWERDOWN=10: Delay before power down in stand still
drv.write_reg(mtr_id, reg.TPOWERDOWN, 0x0000000A);
# TPWMTHRS=500
drv.write_reg(mtr_id, reg.TPWMTHRS, 0x000001F4); 
# Values for speed and acceleration
drv.write_reg(mtr_id, reg.VSTART, 4);
drv.write_reg(mtr_id, reg.A1, 5000);
drv.write_reg(mtr_id, reg.V1, 1000);
drv.write_reg(mtr_id, reg.AMAX, 3000);   
drv.write_reg(mtr_id, reg.VMAX, 10000);
drv.write_reg(mtr_id, reg.DMAX, 5000);
drv.write_reg(mtr_id, reg.D1, 1000);
drv.write_reg(mtr_id, reg.VSTOP, 5);
rst =  drv.read_int(0, reg.IFCNT)
print("IFCNT reg = ",rst)
cnt = 0
vmode_dir = 2
while(1):
    swmode = drvstatus = drv.read_reg(mtr_id,reg.SWMODE)
    gstat = drv.read_reg(mtr_id, reg.GSTAT)
    lost = drv.read_int(mtr_id,reg.LOST_STEPS)
    xactual = drv.read_int(mtr_id,reg.XACTUAL)
    xactual_reg = drv.read_reg(mtr_id,reg.XACTUAL)
    
    dvrstatus = drvstatus = drv.read_reg(mtr_id,reg.DRVSTATUS)
    print("gstat dvrstatus {} {} {} {} |{}| {}".format(gstat.hex(),dvrstatus.hex(),swmode.hex(),lost,xactual,xactual_reg.hex()))
  
    if cnt % 2:
        if vmode_dir == 2:
            vmode_dir = 1
        else:
            vmode_dir = 2
    drv.write_reg(mtr_id,reg.RAMPMODE, vmode_dir )
    drv.write_reg(mtr_id, reg.VMAX, 20000);
   
    cnt =+ 1
    
    time.sleep(7)
    if cnt >= 100: 
        drv.write_reg(mtr_id, reg.VMAX, 0);
        sys.exit(1)