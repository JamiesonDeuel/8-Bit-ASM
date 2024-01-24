@echo off 

SET /P file=Please enter the name of the file you want to run: 

SET logfiles=D:\Documents\8-Bit-ASM\%file%.asm
SET out=D:\Documents\8-Bit-ASM\%file%.hex
D:\Documents\8-Bit-ASM\customasm\customasm.exe "%logfiles%" -f annotated,base:2,group:8 


C:/Users/Koby/AppData/Local/Programs/Python/Python310/python.exe "d:/Documents/8-Bit-ASM/Run.py" "%logfiles%"

D:\Documents\8-Bit-ASM\customasm\customasm.exe "%logfiles%" -f intelhex -o "%out%"

C:/Users/Koby/AppData/Local/Programs/Python/Python310/python.exe "d:/Documents/8-Bit-ASM/hextobin.py" "%out%"