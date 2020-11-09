tmc_uart
========

A python package to read/write to registers to TMC motion controllers via the uart. This package includes
register addresses for the TMC5160 as specified here: 

https://www.trinamic.com/fileadmin/assets/Products/ICs_Documents/TMC5160A_Datasheet_Rev1.14.pdf

Other TMC controllers could be adapted by providing the register include file with its specific register addresses. 

There are some test scripts in the ./bin directory.  Tested on both Windows and Raspberry PI with a USB/RS485 adapter
to a custom board with a TMC5160 chip with uart pins broken out.  

There are two read functions. read_int() and read_reg(). The first returns a 32 bit value and second returns a 4 byte object.


Synopsis
-------------------------

.. code-block:: python

    from tmc_uart import TMC5160_UART
    from tmc_uart import tmc5160_reg as reg

    drvconf = { 'comm_dev':'/dev/ttyUSB0', 'baud':500000 }
    drv = TMC5160_UART(drvconf)

    mtr_id = 0
    
    ifcnt0 =  drv.read_int(0, reg.IFCNT)
    drv.write_reg(mtr_id,reg.GCONF,0x0000000C)
    ifcnt1 =  drv.read_int(0, reg.IFCNT)
    print("IFCNT before and after: {} {}".format(ifcnt0,ifcnt1))

    gconf = drv.read_reg(mtr_id, reg.GCONF)
    print("GONF = ",gconf)

    xactual = drv.read_int(mtr_id,reg.XACTUAL)
    print("XACTUAL = ",xactual)

    