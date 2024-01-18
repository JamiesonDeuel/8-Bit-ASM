#ruledef
{
    NOP => 0x00
    LDA, {address} => 0x01 @ address`8
    ADD, {address} => 0x02 @ address`8
    SUB, {address} => 0x03 @ address`8
    STA, {address} => 0x04 @ address`8
    LDI, {value} => 0x05 @ value`8
    JMP, {address} => 0x06 @ address`8
    JC, {address} => 0x07 @ address`8
    JZ, {address} => 0x08 @ address`8
    LCDC, {value}   => 0x09 @ value`8
    LCDD, {value}   => 0x0A @ value`8
    OUT => 0x0E
    HLT => 0x0F
    
}
