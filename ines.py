from helper import *


class iNES(object):
    def __init__(self, nes):
        self.header = nes.read(16)
        self.magic = self.header[:4]

        if self.magic.encode("hex") != "4e45531a":
            raise Exception("Magic is incorrect: " + self.magic.encode("hex"))

        self.rom_banks_count = ord(self.header[4:5])
        self.vrom_banks_count = ord(self.header[5:6])
        self.flags_6 = Flags6(ord(self.header[6:7]))
        self.flags_7 = Flags7(ord(self.header[7:8]))
        self.ram_banks = ord(self.header[8:9])
        self.tvSystem = bit_val(ord(self.header[9:10]), 0)
        self.flags_10 = ord(self.header[10:11])
        self.rest = self.header[11:]
        self.mapper = combine_nibble(self.flags_7.mapperUpper,
                                     self.flags_6.mapperLower)

        self.trainer = None
        if self.flags_6.trainerPresent:
            self.trainer = nes.read(512)

        self.rom_banks = []
        for i in range(self.rom_banks_count):
            self.rom_banks.append(nes.read(16384))

    def __str__(self):
        return "magic: {}\n" \
               "rom_banks: {}\n" \
               "vrom_banks: {}\n" \
               "flag_6: {}\n" \
               "flag_7: {}\n" \
               "ram_banks: {}\n" \
               "TV system: {}\n" \
               "mapper: {}\n" \
               "rom banks: {}".format(self.magic.encode("hex"),
                                      self.rom_banks_count,
                                      self.vrom_banks_count,
                                      self.flags_6,
                                      self.flags_7,
                                      self.ram_banks,
                                      self.tvSystem,
                                      self.mapper,
                                      self.rom_banks[0].encode("hex"))


class Flags6(object):
    def __init__(self, flags):
        # Mirroring: 0: horizontal (vertical arrangement) (CIRAM A10 = PPU A11)
        #            1: vertical (horizontal arrangement) (CIRAM A10 = PPU A10)
        self.mirroring = flag_val(flags, 0)
        # 1: Cartridge contains battery-backed PRG RAM ($6000-7FFF) or other persistent memory
        self.persistentMem = flag_val(flags, 1)
        # 1: 512-byte trainer at $7000-$71FF (stored before PRG data)
        self.trainerPresent = flag_val(flags, 2)
        # 1: Ignore mirroring control or above mirroring bit; instead provide four-screen VRAM
        self.fullScreen = flag_val(flags, 3)
        # Lower nybble of mapper number
        self.mapperLower = low_nibble(flags)

    def __str__(self):
        return "mirroring: {}\n" \
               "       persistent mem: {}\n" \
               "       trainer present: {}\n" \
               "       fullscreen: {}\n" \
               "       mapper lower: {}".format(self.mirroring,
                                                self.persistentMem,
                                                self.trainerPresent,
                                                self.fullScreen,
                                                self.mapperLower)


class Flags7(object):
    def __init__(self, flags):
        # VS Unisystem
        self.unisystem = bit_val(flags, 0)
        # PlayChoice-10 (8KB of Hint Screen data stored after CHR data)
        self.playerChoice = bit_val(flags, 1)
        # If equal to 2, flags 8-15 are in NES 2.0 format
        self.nes_2_0 = bit_val(flags, 2) == 2
        # Upper nybble of mapper number
        self.mapperUpper = high_nibble(flags)

    def __str__(self):
        return "unisystem: {}\n" \
               "        player choice: {}\n" \
               "        nes 2.0: {}\n" \
               "        mapper upper: {}".format(self.unisystem,
                                                 self.playerChoice,
                                                 self.nes_2_0,
                                                 self.mapperUpper)
