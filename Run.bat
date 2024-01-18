@ECHO OFF
SETLOCAL

SET /P file=Please enter the name of the file you want to run: 

SET logfiles=D:\Documents\8-Bit-ASM\%file%

D:\Documents\8-Bit-ASM\customasm\customasm.exe "%logfiles%" -f annotated,base:2,group:8 

C:/Users/Koby/AppData/Local/Programs/Python/Python310/python.exe "d:/Documents/8 Bit/Run.py" "%logfiles%"