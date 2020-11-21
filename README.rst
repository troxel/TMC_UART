tmc_uart
========

A python package to read/write to registers to TMC motion controllers via the uart. This package includes
register addresses for the TMC5160 as specified here: 

https://www.trinamic.com/fileadmin/assets/Products/ICs_Documents/TMC5160A_Datasheet_Rev1.14.pdf

Other TMC controllers could be adapted by providing the register include file with its specific register addresses. 

There are some test scripts in the ./bin directory.  Tested on both Windows and Raspberry PI with a USB/RS485 adapter
to a custom board with a TMC5160 chip with uart pins broken out.  

There are two read functions. read_int() and read_reg(). The first returns a 32 bit value and second returns a 4 byte object.

Repository can be found: 

https://github.com/troxel/TMC_UART


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
    
    ifcnt1 =  drv.read_int(0, reg.IFCNT)  # Number of successful uart writes
    
    print("IFCNT before and after: {} {}".format(ifcnt0,ifcnt1))

    gconf = drv.read_reg(mtr_id, reg.GCONF)
    print("GONF = ",gconf)

    xactual = drv.read_int(mtr_id,reg.XACTUAL)
    print("XACTUAL = ",xactual)


Notes:
-----------------------------

In read_reg and write_reg there is a sleep function call that should be tuned to your specific hardware and baud rate. Set up a loop with repeated read or write calls and 
decrease sleep time until you start missing transactions. I was able to get 500000k baud without problem. You can go higher but would need to supply an external clock to the chip. 

I used a regular RS485/USB adapter to communicate using differential signals. Trinamic has indicated that the interface is only designed for 3.3 volts. I measured the device I was using and it was around 4 volts peak-to-peak, no problems as of yet after hundreds of hours of operation.  

I am using a custom board with multiple TMC5160 designed by 

https://customcircuitsolutions.com/
    
