"""
if 3<2 :
    print('ok')
elif 5<4 :
    print('hmm')
else :
    print(1+1)


print('Hello')
"""

print('Enter your command')
robot_move = input()

if robot_move == 'front':
    print('Robot Moving Front')
elif robot_move == 'back':
    print('Robot Moving Back')
else:
    print('Stand Robot')