import socket # send to unity


# socket config
HOST = '127.0.0.1'
PORT = 50007
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def string_to_command(string, prev):
    if len(string) > 4:
        string = string[:4]
    go = ["まえ", "すすめ", "すずめ", "うすめ", "つめ"]
    jump = ["うえ", "ジャンプ"]
    ret = ["うしろ", "もどれ"]
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

def command_admin(step, command, command_step):
    step[0] += 1
    step[0] += 1
    if step[0] % 4 == 0:
        client.sendto(command.encode('utf-8'),(HOST,PORT))
    if command != "0":
        step[1] += 1
    else:
        step[1] = 0
    if step[1] > command_step:
        return "0"
    return command