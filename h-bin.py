#!/usr/bin/python
# -*- coding: UTF-8 -*-
# README:
#   For firmware
#       1. change *.h   to *.bin
#       2. change *.bin to *.h
#   USAGE:
#       1.copy file to current dir
#       2.run.bat


import os
import re


def h2bin(file_name):
    try:
        h = open(f"./{file_name}.h", 'r')
        b = open(f"./{file_name}_output.bin", 'wb+')
    except Exception as ex:
        print("[X] Open file error! ex: ", ex)
        return

    hex_list = re.findall(r"0x[0-9a-fA-F]+", ''.join(h.readlines()), flags=re.IGNORECASE)
    if hex_list:
        hex_list = [int(i, 16) for i in hex_list]

    b.write(bytearray(hex_list))
    print(f"[√] Change {file_name}.h -> {file_name}_output.bin done!")
    b.close()
    h.close()


def bin2h(file_name):
    cnt = 0

    try:
        b = open(f"./{file_name}.bin", 'rb')
        h = open(f"./{file_name}_output.h", 'w+')
    except Exception as ex:
        print("[X] Open file error! ex: ", ex)
        return

    h.write("static unsigned char array[] = {\n")

    for i in range(os.path.getsize(f"./{file_name}.bin")):
        num = b.read(1)

        # read 16 nums, input new line
        if not cnt % 16 and cnt:
            h.write("\n\t")
        elif not cnt:
            h.write("\t")

        h.write(f"0x{num.hex()}, ")
        cnt += 1

    h.write("\n};")
    print(f"[√] Change {file_name}.bin -> {file_name}_output.h done!")
    b.close()
    h.close()


if __name__ == '__main__':
    # var
    head_file_name = []
    bin_file_name = []

    # Init
    for file in os.listdir("./"):
        # head file
        if os.path.isfile(file) and "output" not in os.path.splitext(file)[0] and os.path.splitext(file)[1] == ".h":
            head_file_name.append(os.path.splitext(file)[0])
        # bin file
        elif os.path.isfile(file) and "output" not in os.path.splitext(file)[0] and os.path.splitext(file)[1] == ".bin":
            bin_file_name.append(os.path.splitext(file)[0])

    # Start
    for file in head_file_name:
        h2bin(file)
    for file in bin_file_name:
        bin2h(file)

    print("[√] All done, exit program...")
    os.system("pause")
    exit(0)
