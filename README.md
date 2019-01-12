# rocknes
rocknes is a NES emulator, written from scratch in Python.
I have always admired CPU emulation, and the best way to understand how it works is to build one.

----

## Table of Contents

* **[6502 CPU](#6502-cpu)**
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
    

----

## 6502 CPU

### Instruction Set

#### ADC
Add with carry.

#### AND
Logical and.

#### ASL
Arithmetic shift left.

#### BCC
Branch if carry clear.

#### BCS
Branch if carry set.

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
