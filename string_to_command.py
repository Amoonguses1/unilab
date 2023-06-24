
def string_to_command(string, prev):
    if len(string) > 4:
        string = string[:4]
    go = ["まえ"]
    jump = ["うえ"]
    ret = ["うしろ"]
    print(string)
    if string == "あ":
        return prev
    if string in go:
        return "1"
    if string in ret:
        return "2"
    if string in jump:
        return "3"
    return "0"
