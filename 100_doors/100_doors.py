 
for i in range(1, 101):
    if i % 2 == 0:
        state='closed'
    elif i % 3 ==0:
         state='closed'
    else:
        state='open'
    print("Door {}:{}".format(i, state))