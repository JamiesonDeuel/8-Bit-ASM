@echo off 

SET /P file=Please enter the name of the file you want to run: 

SET logfiles=C:\Users\jkdeu\Documents\8-Bit-ASM\%file%.asm
SET out=C:\Users\jkdeu\Documents\8-Bit-ASM\%file%.hex
C:\Users\jkdeu\Documents\8-Bit-ASM\customasm\customasm.exe "%logfiles%" -f annotated,base:2,group:8 

C:\Users\jkdeu\AppData/Local/Programs/Python/Python312/python.exe "c:/Users/jkdeu/Documents/8-Bit-ASM/Run.py" "%logfiles%"

C:\Users\jkdeu\Documents\8-Bit-ASM\customasm\customasm.exe "%logfiles%" -f intelhex -o "%out%"

C:\Users\jkdeu\Users/Koby/AppData/Local/Programs/Python/Python312/python.exe "c:/Users/jkdeu/Documents/8-Bit-ASM/hextobin.py" "%out%"
