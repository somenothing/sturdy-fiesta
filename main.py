MAX_LENGTH = 50
DICT = ['哞哞', '哞牛', '牛哞', '牛牛', '哞~', '~哞', '牛~', '~牛']


def mou_encode(text: str) -> str:
    if len(text) > MAX_LENGTH:
        raise ValueError('The maximum input length is limited to %s.' % MAX_LENGTH)
    result = ''
    for char in text:
        if '\u4e00' <= char <= '\u9fa5':
            n = oct(ord(char) - 19968)[2:]
            n = n.zfill(5)
            # print(char, n)
            for _n in n:
                result += DICT[int(_n)]
        elif char == '~':
            pass
        else:
            result += char
    return result


def mou_decode(text: str) -> str:
    result = ''
    begin = 0
    while begin < len(text):
        if text[begin:begin + 2] in DICT:
            t = text[begin:begin + 10]
            oct_code = ''
            for i in range(0, 10, 2):
                n = DICT.index(t[i:i + 2])
                oct_code += str(n)
            char = chr(int(oct_code, 8) + 19968)
            # print(oct_code, char)
            result += char
            begin += 10
        else:
            result += text[begin]
            begin += 1
    return result


if __name__ == '__main__':
    e = mou_encode('如输出的数值要求小数点后保留2位有效数字、按照规定的格式对字符串和数值混合输出等。')
    print(e)
    d = mou_decode(e)
    print(d)
