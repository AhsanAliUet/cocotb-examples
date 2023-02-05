# Cocotb Examples
To use them, change variables inside Makefile according to the name of the module. For example, if you want to test mux_2x1.sv module, you must change variable ```TOPLEVEL = mux_2x1``` and ```MODULE = test_mux_2x1``` which is simply name of the python testbench file.  

You must have cocotb installed for this purpose. In Ubuntu/WSL/PowerShell of Windows, write ```pip install cocotb```. It will install cocotb for you. Also, you must have installed ```make``` command for windows. It is not a problem if you are using Ubuntu/macOS/Unix based operating systems.   

Change directory to this folder (where rtl and tests are present) and write   

```make SIM=questa```    
```make SIM=verilator```  
```make SIM=icarus```  
Depending upon which simulator you want to use.   

# Summary
Use the following commands:   

```git clone https://github.com/AhsanAliUet/cocotb-examples```   

```cd cocotb-examples```   

```make SIM=questa```
