# rocknes
rocknes is a NES emulator, written from scratch in Python.
I have always admired CPU emulation, and the best way to understand how it works is to build one.

----

## Table of Contents

* **[6502 CPU](#6502-cpu)**
  * [Addressing modes](#addressing-modes)
    * [Implicit](#addressing-implicit)
    * [Accumulator](#addressing-accumulator)
    * [Immediate](#addressing-imediate)
    * [Zero Page](#addressing-zero-page)
    * [Zero Page,X](#addressing-zero-page-x)
    * [Zero Page,Y](#addressing-zero-page-y)
    * [Relative](#relative)
    * [Absolute](#addressing-absolute)
    * [Absolute,X](#addressing-absolute-x)
    * [Absolute,Y](#addressing-absolute-y)
    * [Indirect](#addressing-indirect)
    * [Indexed Indirect](#addressing-indexed-indirect)
    * [Indirect Indexed](#addressing-indirect-indexed)
  * [Instruction Set](#instruction-set)
    * [ADC](#adc)
    * [AND](#and)
    * [ASL](#asl)
    * [BCC](#bcc)
    * [BCS](#bcs)
    * [BEQ](#beq)
    * [BIT](#bit)
    * [BMI](#bmi)
    * [BNE](#bne)
    * [BPL](#bpl)
    * [BRK](#brk)
    * [BVC](#bvc)
    * [BVS](#bvs)
    * [CLC](#clc)
    * [CLD](#cld)
    * [CLI](#cli)
    * [CLV](#clv)
    * [CMP](#cmp)
    * [CPX](#cpx)
    * [CPY](#cpy)
    * [DEC](#dec)
    * [DEX](#dex)
    * [DEY](#dey)
    * [EOR](#eor)
    * [INC](#inc)
    * [INX](#inx)
    * [INY](#iny)
    * [JMP](#jmp)
    * [JSR](#jsr)
    * [LDA](#lda)
    * [LDX](#ldx)
    * [LDY](#ldy)
    * [LSR](#lsr)
    * [NOP](#nop)
    * [ORA](#ora)
    * [PHA](#pha)
    * [PHP](#php)
    * [PLA](#pla)
    * [PLP](#plp)
    * [ROL](#rol)
    * [ROR](#ror)
    * [RTI](#rti)
    * [RTS](#rts)
    * [SBC](#sbc)
    * [SEC](#sec)
    * [SED](#sed)
    * [SEI](#sei)
    * [STA](#sta)
    * [STX](#stx)
    * [STY](#sty)
    * [TAX](#tax)
    * [TAY](#tay)
    * [TSX](#tsx)
    * [TXA](#txa)
    * [TXS](#txs)
    * [TYA](#tya)
* **[References](#references)**    
----

## 6502 CPU

### Addressing Modes

#### Relative

Used in relative branch instructions.
Signed offset is added to the program counter. Offsets range from -128 to 127.
The offset is relative to the first byte of the next instruction. For example, 90 00 is a BCC with no effect.

### Instruction Set

#### ADC
Add with carry.

#### AND
Logical and.

#### ASL
Arithmetic shift left.

#### BCC
Branch if carry clear.

| Addressing mode | Opcode | Bytes | Cycles |
|-----------------|:------:|:-----:|:------:|
| Relative        | 90     | 2     | 2 (3 if branch taken, 4 if page boundary crossed) |

#### BCS
Branch if carry set.

| Addressing mode | Opcode | Bytes | Cycles |
|-----------------|:------:|:-----:|:------:|
| Relative        | B0     | 2     | 2 (3 if branch taken, 4 if page boundary crossed) |

#### BEQ
Branch if equal.

#### BIT
Bit test.

#### BMI
Branch if minus.

#### BNE
Branch if not equal.

#### BPL
Branch if positive.

#### BRK
Force interrupt.

#### BVC
Branch if overflow clear.

#### BVS
Branch if overflow set.

#### CLC
Clear carry flag.

#### CLD
Clear decimal mode.

#### CLI
Clear interrupt disable.

#### CLV
Clear overflow flag.

#### CMP
Compare.

#### CPX
Compare X register.

#### CPY
Compare Y register.

#### DEC
Decrement memory.

#### DEX
Decrement X register.

#### DEY
Decrement Y register.

#### EOR
Exclusive or.

#### INC
Increment memory.

#### INX
Increment X register.

#### INY
Increment Y register.

#### JMP
Jump.

#### JSR
Jump to subroutine.

#### LDA
Load accumulator.

#### LDX
Load X register.

#### LDY
Load Y register.

#### LSR
Logical shift right

#### NOP
No operation.

#### ORA
Logical inclusive or.

#### PHA
Push accumulator.

#### PHP
Push processor status.

#### PLA
Pull accumulator.

#### PLP
Pull processor status.

#### ROL
Rotate left.

#### ROR
Rotate right.

#### RTI
Return from interrupt.

#### RTS
Return from subroutine.

#### SBC
Subtract with carry.

#### SEC
Set carry flag.

#### SED
Set decimal flag.

#### SEI
Set interrupt disable.

#### STA
Store accumulator.

#### STX
Store X register.

#### STY
Store Y register.

#### TAX
Transfer accumulator to X.

#### TAY
Transfer accumulator to Y.

#### TSX
Transfer stack pointer to X.

#### TXA
Transfer X to accumulator.

#### TXS
Transfer X to stack pointer.

#### TYA
Transfer Y to accumulator.

## References
http://www.obelisk.me.uk/6502/reference.html
https://www.masswerk.at/6502/6502_instruction_set.html
https://en.wikibooks.org/wiki/6502_Assembly
