from TopUpUsers import Users

def processUser():
    usersList = []
    user_file = open('file/users.txt', 'r')
    for ulist in user_file:
        list = ulist.split(',')
        s = Users(list[0], list[1], int(list[2]))

        usersList.append(s)
    return usersList

"""def write(date1, details1, amount1):
    jandata = date1 +','+ details1 +',' + amount1 +'\n'"""

def processTopup(date,child_Name,camount):
    t_file = open('try.txt', 'r')
    a_file = open('try.txt','a')
    for trans in t_file:
        list = trans.split(', ')
        if list[1] == child_Name:
            tamount = int(list[2])+ camount
            a_file.write('\n'+date+', ' +child_Name+', ' +list[2]+', '+str(tamount))
            return [date], [child_Name], [list[2]], [str(tamount)]
