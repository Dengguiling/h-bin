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
    """
    @name:      h2bin
    @param:     file_name
    @return:    None
    @info:
    """
    try:
        h = open(f"./{file_name}.h", 'r')
        b = open(f"./{file_name}_output.bin", 'wb+')
    except Exception as ex:
        print("[!] {file_name}.h 打开文件失败! ex: ", ex)
        return

    hex_list = re.findall(r"0x[0-9a-fA-F]+",
                          ''.join(h.readlines()), flags=re.IGNORECASE)

    if hex_list:
        hex_list = [int(i, 16) for i in hex_list]
        b.write(bytearray(hex_list))
        print(f"[-] {file_name}.h -> {file_name}_output.bin 转换成功!")
    else:
        print(f"[!] {file_name}.h 读取数据为空!")

    b.close()
    h.close()


def bin2h(file_name):
    """
    @name:      bin2h
    @param:     file_name
    @return:    None
    @info:
    """
    try:
        b = open(f"./{file_name}.bin", 'rb')
        h = open(f"./{file_name}_output.h", 'w+')
    except Exception as ex:
        print("[!] {file_name}.bin 打开失败! ex: ", ex)
        return

    h.write("static unsigned char array[] = {\n")

    for i in range(os.path.getsize(f"./{file_name}.bin")):
        num = b.read(1)

        # read 16 nums, input new line
        if not i % 16 and i:
            h.write("\n\t")
        elif not i:
            h.write("\t")

        h.write(f"0x{num.hex()}, ")

    h.write("\n};")
    print(f"[-] {file_name}.bin -> {file_name}_output.h 转换成功!")
    b.close()
    h.close()


if __name__ == '__main__':
    # var
    head_file_names = []
    bin_file_names = []

    # Init
    for file in os.listdir("./"):
        # head file
        if file.endswith(".h") and "output" not in file:
            head_file_names.append(os.path.splitext(file)[0])
        # bin file
        if file.endswith(".bin") and "output" not in file:
            bin_file_names.append(os.path.splitext(file)[0])

    # Start
    for file in head_file_names:
        h2bin(file)
    for file in bin_file_names:
        bin2h(file)

    if not len(head_file_names) and not len(bin_file_names):
        print("[!] 当前文件夹没有.h文件或者.bin文件！")

    print("[-] 转换完成，退出脚本...")
