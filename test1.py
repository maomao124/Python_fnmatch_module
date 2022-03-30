"""
 * Project name(项目名称)：Python_fnmatch模块
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/30 
 * Time(创建时间)： 21:04
 * Version(版本): 1.0
 * Description(描述)：
 函数名	功能
fnmatch.filter(names, pattern)	对 names 列表进行过滤，返回 names 列表中匹配 pattern 的文件名组成的子集合。
fnmatch.fnmatch(filename, pattern)	判断 filename 文件名，是否和指定 pattern 字符串匹配
fnmatch.fnmatchcase(filename, pattern)	和 fnmatch() 函数功能大致相同，只是该函数区分大小写。
fnmatch.translate(pattern)	将一个 UNIX shell 风格的 pattern 字符串，转换为正则表达式

*：可匹配任意个任意字符。
？：可匹配一个任意字符。
[字符序列]：可匹配中括号里字符序列中的任意字符。该字符序列也支持中画线表示法。比如 [a-c] 可代表 a、b 和 c 字符中任意一个。
[!字符序列]：可匹配不在中括号里字符序列中的任意字符。

 """
import fnmatch

if __name__ == '__main__':
    # filter()
    print(fnmatch.filter(['abc', '123.txt', 'test1.py', 'test2.py', 'test1.txt'], '*.txt'))
    print(fnmatch.filter(['abc', '123.txt', 'test1.py', 'test2.py', 'test1.txt'], 'test?.*'))
    # fnmatch()
    for file in ['abc', 'test1.py', 'test2.py', 'test1.txt','test1.TXT']:
        if fnmatch.fnmatch(file, '*.txt'):
            print(file)
    # fnmatchcase()
    print([i for i in ['test2.py', 'test1.txt', 'test1.TXT'] if fnmatch.fnmatchcase(i, '*.txt')])
    # translate()
    print(fnmatch.translate('ab.tx?'))
