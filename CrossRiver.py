all_state = []
state = []
action = []


def cross_river(missionary, cannibal, side):

    if (missionary, cannibal, side) in all_state:
        return False
    else:
        all_state.append((missionary, cannibal, side))

    if missionary < 0 or cannibal < 0:
        return False

    elif missionary > 3 or cannibal > 3:
        return False

    elif missionary != 0 and missionary < cannibal:
        return False

    elif 3-missionary != 0 and 3-missionary < 3-cannibal:
        return False

    elif (missionary, cannibal, side) == (0,0,'R'):
        action.append('')
        state.append((missionary, cannibal, side))
        return True

    elif side == 'L':
        side = 'R'
        if cross_river(missionary-1, cannibal-1, side):
            action.append('MCR')
            state.append((missionary, cannibal, 'L'))
            return True
        elif cross_river(missionary-2, cannibal, side):
            action.append('MMR')
            state.append((missionary, cannibal, 'L'))
            return True
        elif cross_river(missionary-1, cannibal, side):
            action.append('MR')
            state.append((missionary, cannibal, 'L'))
            return True
        elif cross_river(missionary, cannibal-2, side):
            action.append('CCR')
            state.append((missionary, cannibal, 'L'))
            return True
        elif cross_river(missionary, cannibal-1, side):
            action.append('CR')
            state.append((missionary, cannibal, 'L'))
            return True
        else:
            return False

    elif side == 'R':
        side = 'L'
        if cross_river(missionary+1, cannibal+1, side):
            action.append('MCL')
            state.append((missionary, cannibal, 'R'))
            return True
        elif cross_river(missionary+2, cannibal, side):
            action.append('MML')
            state.append((missionary, cannibal, 'R'))
            return True
        elif cross_river(missionary+1, cannibal, side):
            action.append('ML')
            state.append((missionary, cannibal, 'R'))
            return True
        elif cross_river(missionary, cannibal+2, side):
            action.append('CCL')
            state.append((missionary, cannibal, 'R'))
            return True
        elif cross_river(missionary, cannibal+1, side):
            action.append('CL')
            state.append((missionary, cannibal, 'R'))
            return True


cross_river(3, 3, 'L')
for i in range(len(state)):
    print(state.pop())
    print(action.pop())