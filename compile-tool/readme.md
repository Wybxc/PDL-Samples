# PDL 编译工具

`pdl.py` 是将 PDL 编译为 C++ 的工具，其原理为**向 OpenJudge 发起一次提交**，并将编译结果输出到 `.cpp` 文件中。

## 需求

运行脚本需要已经安装 (Playwright)[https://playwright.dev/python/] 的 Python 3 环境。

另外，需要一个已经加入 (PDL 学习)[http://pdl.openjudge.cn/]小组的 OpenJudge 账号。

## 用法

```
$ python .\compile-tool\pdl.py -h
usage: pdl.py [-h] [-o OUTPUT] -u USERNAME -p PASSWORD source

PDL编译工具

positional arguments:
  source                PDL源码文件

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        输出文件名
  -u USERNAME, --username USERNAME
                        OpenJudge 用户名
  -p PASSWORD, --password PASSWORD
                        OpenJudge 密码
```