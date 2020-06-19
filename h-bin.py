#!/usr/bin/python
# -*- coding: UTF-8 -*-


def h2bin(file_name):
    cnt = 0

    try:
        h = open(f"./{file_name}.h", 'r')
        b = open(f"./{file_name}.bin", 'wb+')
    except Exception as ex:
        print("[X] Open file error! ex: ", ex)
        return

    size = os.path.getsize(f"./{file_name}.h")
    for i in range(size):
        num = 0
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
    print(f"[√] Success, {file_name}.h -> {file_name}.bin  {cnt} byte data!")
    b.close()
    h.close()


def bin2h(file_name):
    cnt = 0

    try:
        b = open(f"./{file_name}.bin", 'rb')
        h = open(f"./{file_name}.h", 'w+')
    except Exception as ex:
        print("[X] Open file error! ex: ", ex)
        return

    size = os.path.getsize(f"./{file_name}.bin")
    h.write("static unsigned char array[] = {\n")
    for i in range(size):
        num = b.read(1)
        if not cnt % 16 and cnt:
            h.write("\n\t")
        elif not cnt:
            h.write("\t")
        h.write(f"0x{num.hex()}, ")
        cnt += 1
    h.write("\n};")
    print(f"[√] Success, {file_name}.bin -> {file_name}.h {cnt} byte data!")
    b.close()
    h.close()


if __name__ == '__main__':
    import os

    for f in os.listdir("./"):
        if os.path.splitext(f)[1] == ".h":
            h2bin(os.path.splitext(f)[0])
        elif os.path.splitext(f)[1] == ".bin":
            bin2h(os.path.splitext(f)[0])

    print("[√] All done, exit program...")
    exit(0)
