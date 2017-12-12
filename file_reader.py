import argparse
from ines import iNES
from opcode_factory import OpcodeFactory

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path to the nes file", type=str)
    args = parser.parse_args()

    with open(args.path, "rb") as f:
        nes = iNES(f)
        factory = OpcodeFactory()
        bank = nes.rom_banks[0]

        i = 0
        while i < len(bank):
            byte = bank[i]
            params_count = factory.params_count(byte)
            params = bank[i + 1: params_count + i + 1]
            factory.desc(byte, params)
            i += params_count + 1


if __name__ == "__main__":
    main()
