class OpcodeFactory(object):
    """
    A		....	Accumulator	 	        OPC A	 	    operand is AC
    abs		....	absolute	 	        OPC $HHLL	 	operand is address $HHLL
    abs,X	....	absolute, X-indexed	 	OPC $HHLL,X	 	operand is address incremented by X with carry
    abs,Y	....	absolute, Y-indexed	 	OPC $HHLL,Y	 	operand is address incremented by Y with carry
    #		....	immediate	 	        OPC #$BB	 	operand is byte (BB)
    impl	....	implied	 	            OPC	 	        operand implied
    ind		....	indirect	 	        OPC ($HHLL)	 	operand is effective address; effective address is value of address
    X,ind	....	X-indexed, indirect	 	OPC ($BB,X)	 	operand is effective zeropage address; effective address is byte (BB) incremented by X without carry
    ind,Y	....	indirect, Y-indexed	 	OPC ($LL),Y	 	operand is effective address incremented by Y with carry; effective address is word at zeropage address
    rel		....	relative	 	        OPC $BB	 	    branch target is PC + offset (BB), bit 7 signifies negative offset
    zpg		....	zeropage	 	        OPC $LL	 	    operand is of address; address hibyte = zero ($00xx)
    zpg,X	....	zeropage, X-indexed	 	OPC $LL,X	 	operand is address incremented by X; address hibyte = zero ($00xx); no page transition
    zpg,Y	....	zeropage, Y-indexed	 	OPC $LL,Y	 	operand is address incremented by Y; address hibyte = zero ($00xx); no page transition
    """
    opcodes = {
        0x00: ("BRK", "impl", 0),
        0x01: ("ORA", "ind_x", 2),
        0x05: ("ORA", "zpg", 1),
        0x06: ("ASL", "zpg", 1),
        0x08: ("PHP", "impl", 0),
        0x09: ("ORA", "#", 1),
        0x0A: ("ASL", "A", 1),
        0x0D: ("ORA", "abs", 2),
        0x0E: ("ASL", "abs", 2),
        0x10: ("BPL", "rel", 1),
        0x11: ("ORA", "ind_y", 2),
        0x15: ("ORA", "zpg_x", 2),
        0x16: ("ASL", "zpg_x", 2),
        0x18: ("CLC", "impl", 0),
        0x19: ("ORA", "abs_y", 3),
        0x1D: ("ORA", "abs_x", 3),
        0x1E: ("ASL", "abs_x", 3),
        0x20: ("JSR", "impl", 0),
        0x21: ("AND", "ind_x", 2),
        0x24: ("BIT", "zpg", 1),
        0x25: ("AND", "zpg", 1),
        0x26: ("ROL", "zpg", 1),
        0x28: ("PLP", "impl", 0),
        0x29: ("AND", "#", 1),
        0x2A: ("ROL", "A", 1),
        0x2C: ("BIT", "abs", 2),
        0x2D: ("AND", "abs", 2),
        0x2E: ("ROL", "abs", 2),
        0x30: ("BMI", "rel", 1),
        0x31: ("AND", "ind_y", 2),
        0x35: ("AND", "zpg_x", 2),
        0x36: ("ROL", "zpg_x", 2),
        0x38: ("SEC", "impl", 0),
        0x39: ("AND", "abs_y", 3),
        0x3D: ("AND", "abs_x", 3),
        0x3E: ("ROL", "abs_x", 3),
        0x40: ("RTI", "impl", 0),
        0x41: ("EOR", "ind_x", 2),
        0x45: ("EOR", "zpg", 1),
        0x46: ("LSR", "zpg", 1),
        0x48: ("PHA", "impl", 0),
        0x49: ("EOR", "#", 1),
        0x4A: ("LSR", "A", 1),
        0x4C: ("JMP", "abs", 2),
        0x4D: ("EOR", "abs", 2),
        0x4E: ("LSR", "abs", 2),
        0x50: ("BVC", "rel", 1),
        0x51: ("EOR", "ind_y", 2),
        0x55: ("EOR", "zpg_x", 2),
        0x56: ("LSR", "zpg_x", 2),
        0x58: ("CLI", "impl", 0),
        0x59: ("EOR", "abs_y", 3),
        0x5D: ("EOR", "abs_x", 3),
        0x5E: ("LSR", "abs_x", 3),
        0x60: ("RTS", "impl", 0),
        0x61: ("ADC", "ind_x", 2),
        0x65: ("ADC", "zpg", 1),
        0x66: ("ROR", "zpg", 1),
        0x68: ("PLA", "impl", 0),
        0x69: ("ADC", "#", 1),
        0x6A: ("ROR", "A", 1),
        0x6C: ("JMP", "ind", 2),
        0x6D: ("ADC", "abs", 2),
        0x6E: ("ROR", "abs", 2),
        0x70: ("BVS", "rel", 1),
        0x71: ("ADC", "ind_y", 2),
        0x75: ("ADC", "zpg_x", 2),
        0x76: ("ROR", "zpg_x", 2),
        0x78: ("SEI", "impl", 0),
        0x79: ("ADC", "abs_y", 3),
        0x7D: ("ADC", "abs_x", 3),
        0x7E: ("ROR", "abs_x", 3),
        0x81: ("STA", "ind_x", 2),
        0x84: ("STY", "zpg", 1),
        0x85: ("STA", "zpg", 1),
        0x86: ("STX", "zpg", 1),
        0x88: ("DEY", "impl", 0),
        0x8A: ("TXA", "impl", 0),
        0x8C: ("STY", "abs", 2),
        0x8D: ("STA", "abs", 2),
        0x8E: ("STX", "abs", 2),
        0x90: ("BCC", "rel", 1),
        0x91: ("STA", "ind_y", 2),
        0x94: ("STY", "zpg_x", 2),
        0x95: ("STA", "zpg_x", 2),
        0x96: ("STX", "zpg_y", 2),
        0x98: ("TYA", "impl", 0),
        0x99: ("STA", "abs_y", 3),
        0x9A: ("TXS", "impl", 0),
        0x9D: ("STA", "abs_x", 3),
        0xA0: ("LDY", "#", 1),
        0xA1: ("LDA", "ind_x", 2),
        0xA2: ("LDX", "#", 1),
        0xA4: ("LDY", "zpg", 1),
        0xA5: ("LDA", "zpg", 1),
        0xA6: ("LDX", "zpg", 1),
        0xA8: ("TAY", "impl", 0),
        0xA9: ("LDA", "#", 1),
        0xAA: ("TAX", "impl", 0),
        0xAC: ("LDY", "abs", 2),
        0xAD: ("LDA", "abs", 2),
        0xAE: ("LDX", "abs", 2),
        0xB0: ("BCS", "rel", 1),
        0xB1: ("LDA", "ind_y", 2),
        0xB4: ("LDY", "zpg_x", 2),
        0xB5: ("LDA", "zpg_x", 2),
        0xB6: ("LDX", "zpg_y", 2),
        0xB8: ("CLV", "impl", 0),
        0xB9: ("LDA", "abs_y", 3),
        0xBA: ("TSX", "impl", 0),
        0xBC: ("LDY", "abs_x", 3),
        0xBD: ("LDA", "abs_x", 3),
        0xBE: ("LDX", "abs_y", 3),
        0xC0: ("CPY", "#", 1),
        0xC1: ("CMP", "ind_x", 2),
        0xC4: ("CPY", "zpg", 1),
        0xC5: ("CMP", "zpg", 1),
        0xC6: ("DEC", "zpg", 1),
        0xC8: ("INY", "impl", 0),
        0xC9: ("CMP", "#", 1),
        0xCA: ("DEX", "impl", 0),
        0xCC: ("CPY", "abs", 2),
        0xCD: ("CMP", "abs", 2),
        0xCE: ("DEC", "abs", 2),
        0xD0: ("BNE", "rel", 1),
        0xD1: ("CMP", "ind_y", 2),
        0xD5: ("CMP", "zpg_x", 2),
        0xD6: ("DEC", "zpg_x", 2),
        0xD8: ("CLD", "impl", 0),
        0xD9: ("CMP", "abs_y", 3),
        0xDD: ("CMP", "abs_x", 3),
        0xDE: ("DEC", "abs_x", 3),
        0xE0: ("CPX", "#", 1),
        0xE1: ("SBC", "ind_x", 2),
        0xE4: ("CPX", "zpg", 1),
        0xE5: ("SBC", "zpg", 1),
        0xE6: ("INC", "zpg", 1),
        0xE8: ("INX", "impl", 0),
        0xE9: ("SBC", "#", 1),
        0xEA: ("NOP", "impl", 0),
        0xEC: ("CPX", "abs", 2),
        0xED: ("SBC", "abs", 2),
        0xEE: ("INC", "abs", 2),
        0xF0: ("BEQ", "rel", 1),
        0xF1: ("SBC", "ind_y", 2),
        0xF5: ("SBC", "zpg_x", 2),
        0xF6: ("INC", "zpg_x", 2),
        0xF8: ("SED", "impl", 0),
        0xF9: ("SBC", "abs_y", 3),
        0xFD: ("SBC", "abs_x", 3),
        0xFE: ("INC", "abs_x", 3),
    }

    def params_count(self, h):
        a = ord(h)
        if a in self.opcodes:
            return self.opcodes[a][2]
        else:
            return  0

    def desc(self, h, params):
        a = ord(h)
        if a in self.opcodes:
            op = self.opcodes[a]
            print "{}: {}".format(op[0], params.encode("hex"))
