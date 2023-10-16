def valid(segment):
    if not segment:
        return False
    if segment[0] == '0' and len(segment) > 1:
        return False
    if len(segment) > 3:
        return False
    if not (0 <= int(segment) <= 255):
        return False
    return True

def helper(result, state, i):
    if i == 0:
        for segment in state:
            if not valid(segment):
                return
        result.append('.'.join(state))
        return

    for j in range(len(state[i])):
        if valid(state[i][j:]):
            old_state = [state[i - 1][:], state[i][:]]
            state[i - 1] = state[i - 1] + state[i][:j]
            state[i] = state[i][j:]
            helper(result, state, i - 1)
            state[i - 1], state[i] = old_state


def restore_ip_addresses(s):
    result = []
    state = []
    i = 0
    for i in range(3):
        state.append(s[i])
    state.append(s[i + 1:])
    helper(result, state, 3)
    return result

print(restore_ip_addresses("010010"))
# print(restore_ip_addresses("00000000"))
# print(restore_ip_addresses("201023"))
# print(restore_ip_addresses("255255255255"))
# print(restore_ip_addresses("12121212"))