all_state = []
state = []
action = []

def water_jug(jug1, jug2):

    if (jug1, jug2) in all_state:
        return False
    else:
        all_state.append((jug1, jug2))

    if jug1 == final or jug2 == final:
        action.append('')
        state.append((jug1, jug2))
        return True

    elif jug1 < 0 or jug2 < 0:
        return False

    elif water_jug(jug1,0):
        action.append('empty2')
        state.append((jug1, jug2))
        return True

    elif water_jug(0,jug2):
        action.append('empty1')
        state.append((jug1, jug2))
        return True

    elif water_jug(0,min(volumn2,jug2+jug1)):
        action.append('pour all of 1 into 2')
        state.append((jug1, jug2))
        return True

    elif water_jug(min(volumn1,jug1+jug2),0):
        action.append('pour all of 2 into 1')
        state.append((jug1, jug2))
        return True

    elif water_jug(jug1-(volumn2-jug2),volumn2):
        action.append('pour 1 into 2 to fill')
        state.append((jug1, jug2))
        return True

    elif water_jug(volumn1, jug2-(volumn1-jug1)):
        action.append('pour 2 into 1 to fill')
        state.append((jug1, jug2))
        return True

    elif water_jug(volumn1, jug2):
        action.append('fill 1')
        state.append((jug1, jug2))
        return True

    elif water_jug(jug1,volumn2):
        action.append('fill 2')
        state.append((jug1, jug2))
        return True

    else:
        return False


volumn1,volumn2 = 4,3
final = 2
water_jug(0, 0)
for i in range(len(state)):
    print(state.pop())
    print(action.pop())

