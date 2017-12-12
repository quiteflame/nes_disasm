import json

data = json.load(open('table1.json'))

for row in data:
    if row["opcode"] != "":
        mode = row["mode"]
        params = 0
        if mode == "Absolute":
            params = 2
            mode = "abs"
        elif mode == "Absolute, X":
            mode = "abs_x"
            params = 3
        elif mode == "Absolute, Y":
            mode = "abs_y"
            params = 3
        elif mode == "":
            params = 0
            mode = "impl"
        elif mode == "Zero Page":
            params = 1
            mode = "zpg"
        elif mode == "Zero Page, X":
            mode = "zpg_x"
            params = 2
        elif mode == "Zero Page, Y":
            mode = "zpg_y"
            params = 2
        elif mode == "Immediate":
            params = 1
            mode = "#"
        elif mode == "Accumulator":
            mode = "A"
            params = 1
        elif mode == "Indirect":
            mode = "ind"
            params = 2
        elif mode == "(Indirect, X)" or mode == "(Indirect), X":
            mode = "ind_x"
            params = 2
        elif mode == "(Indirect, Y)" or mode == "(Indirect), Y":
            mode = "ind_y"
            params = 2

        print "0x{}: (\"{}\", \"{}\", {}),".format(row["hex"], row["opcode"], mode, params)