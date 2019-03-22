actions_key = ["wink", "double blink", "close your eyes", "jump"]

def handshake(code):
    actions = []
    for i, s in enumerate(str(bin(code))[2:]):
        if i < len(actions_key) and s == '1':
            actions.append(actions_key[i])
        elif i == 5 and s == '1':
            actions = reversed(actions)
    return actions


def secret_code(actions):
    pass
