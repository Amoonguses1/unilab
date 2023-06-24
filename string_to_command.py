
def string_to_command(string):
    if len(string) > 4:
        string = string[:4]
    go = ["すすめ", "すすむ", "むすめ"]
    jump = ["ジャンプ"]
    ret = ["もどれ"]
    print(string)
    if string in go:
        return "1"
    if string in ret:
        return "2"
    if string in jump:
        return "3"
    return "0"
