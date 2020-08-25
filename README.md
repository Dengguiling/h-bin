# h-bin
![](https://img.shields.io/badge/author-Ling0220-brightgreen.svg) ![](https://img.shields.io/badge/version-v0.0.1-blue.svg) ![](https://img.shields.io/badge/platform-windows|linux|mac-lightgrey.svg) ![](https://img.shields.io/badge/language-python-orange.svg) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


-   [Background](#Background)
-   [Install](#Install)
-   [Usage](#Usage)
-   [License](#License)


# Background
这是一个为嵌入式工作人员制作的软件。  
This is software for embedded workers.  

某些触摸屏的固件是bin文件，需要转换成C语言中的头文件。  
The firmware for some touch screens is a bin file that needs to be converted to a header file in C.  

所以制作本工具，用于头文件和bin文件的互相转换。  
So make this tool, for the header file and bin file conversion.  

# Install
``` shell
git clone https://github.com/Ling0220/h-bin.git
```

# Usage
**拷贝你需要转换的头文件或bin文件到h-bin文件夹下。**  
**Copy the header file or bin file you need to convert to the h-bin folder.**
``` shell
python3 h-bin.py
```

# License
[MIT © Ling0220](./LICENSE)