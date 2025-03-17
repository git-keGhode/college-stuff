
**DOSBOX :** ASM emulator

4 types of registers 
gpr
spr
flag reg
segment reg

**ASM :** used for programming for ALU as it can communicate directly with register
- we will conduct practicals on 8086

**GPR :** stores immediate res during execution.  
- 4 main registers (each 16-bits): divided into 2 parts (AH, AL; BH, BL ...)
	- AX - accumulatpr
	- BX - base
	- CX - counter
	- DX - data

**SPR :** 5
- ip - stores addr of next instruction
- bp - stores addr of memory
- sp - points to top of stack (addr of top of stack)
- si - stores offset addr of source
- di - stores offset addr of destination

**8086 :**
- works on 16 bit data
- 20-bit address

**Segment register :** 
- mem addr is 20 bits
- but microprocessor is only 16 bits wide. 
- so phy mem is divided into segments of logical memory
- 1mb of data is divided into 4 64k segments (4 segments)
- each segment is 16bits
- thus 20 bits (1mb) are converted to 16bits. by being divided into 5 segments each of 64k
- now the address is called logical address (4-bits)
- *5 bit addresses - physical addr; 5 bit addr - logical addr*
- These segments are: 
	- code segment
	- data segment
	- stack segment
	- extra segment

**flag register :**
- 16 bit registers (0-15 individual flip flop)
- each flip flop has a meaning (eg : carry flag)

// F3AB
// F02C

// 1111 0011 1010 1011 +
// 1111 0000 0010 1100


# programming tools 

1. **Emulator :** DOSBox(fast, good debugging), Emu 8086, PCspim
2. **Assembler :** TASM(Turvo assembler), MASM(ms macro assembler), NASM(netwide)
3. **Debugger :** DEBUG.EXE, Turbo Debugger

STEPS to setup DOSBOX : 
1. whenever you open dosbox you need to mount the assembler. 
```asm
mount c c:\TASM
c:
edit
```
2. 