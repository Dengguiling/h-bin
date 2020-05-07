#!/usr/bin/python
# -*- coding: UTF-8 -*-


def h2bin():
    cnt = 0

    h = open(input_filename, 'r')
    b = open(output_filename, 'wb+')
    size = os.path.getsize(input_filename)

    for i in range(size):
        # hex for bin
        num = 0

        # char for h
        data = h.read(1)
        if data == '0':
            data = h.read(1)
            if data == 'x' or data == 'X':
                data = h.read(1)
                if ord('0') <= ord(data) <= ord('9'):
                    num += (ord(data) - ord('0')) * 16
                elif ord('a') <= ord(data) <= ord('z'):
                    num += (ord(data) - ord('a') + 10) * 16
                elif ord('A') <= ord(data) <= ord('Z'):
                    num += (ord(data) - ord('A') + 10) * 16

                data = h.read(1)
                if ord('0') <= ord(data) <= ord('9'):
                    num += (ord(data) - ord('0'))
                elif ord('a') <= ord(data) <= ord('z'):
                    num += (ord(data) - ord('a') + 10)
                elif ord('A') <= ord(data) <= ord('Z'):
                    num += (ord(data) - ord('A') + 10)
                num = num.to_bytes(1, 'big')
                b.write(num)

                cnt += 1
    print(f"转换成功, 共转换 {cnt} byte的数据!")
    b.close()
    h.close()


def bin2h():
    cnt = 0

    b = open(input_filename, 'rb')
    h = open(output_filename, 'w+')
    size = os.path.getsize(input_filename)

    h.write("static unsigned char change_me[] = {\n")

    for i in range(size):
        num = b.read(1)
        if not cnt % 16 and cnt:
            h.write("\n\t")
        elif not cnt:
            h.write("\t")
        h.write(f"0x{num.hex()}, ")
        cnt += 1
    h.write("\n};")
    print(f"转换成功, 共转换 {cnt} byte的数据!")
    b.close()
    h.close()


if __name__ == '__main__':
    import os
    import argparse

    # arg解析器
    parse = argparse.ArgumentParser(description="h文件和bin文件互相转换程序")
    parse.add_argument('-i', '--input_filename', action='store',
                       dest='input_filename', help="input_filename(输入文件名)", required=True)
    parse.add_argument('-o', '--output_filename', action='store',
                       dest='output_filename', help="output_filename(输出文件名)")

    res = parse.parse_args()
    input_filename = res.input_filename
    output_filename = res.output_filename

    if input_filename == output_filename:
        print("[ERR] 输入文件名不能和输出文件名相同!")
        exit(-1)

    if not os.path.isfile(input_filename) or not os.access(input_filename, os.R_OK):
        print("[ERR] 输入的文件名不存在或者不可读!")
        exit(-1)

    if input_filename.split('.')[-1] == 'h':
        if not output_filename:
            output_filename = 'output.bin'
        h2bin()
    elif input_filename.split('.')[-1] == 'bin':
        if not output_filename:
            output_filename = 'output.h'
        bin2h()
    else:
        change_flag = 0
        print(f"[ERR] 不支持这种文件类型 {input_filename.split('.')[-1]} !")
        exit(-1)
    exit(0)
