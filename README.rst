tmc_uart
========

A python package to talk via the uart to TMC motion controllers. This package includes
register address for specicially for TMC5160 as specified here: 

https://www.trinamic.com/fileadmin/assets/Products/ICs_Documents/TMC5160A_Datasheet_Rev1.14.pdf

Other TMC controllers could be adapted by providing an include file with its specific register addresses. 


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

    