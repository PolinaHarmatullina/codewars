import numpy as np
lst = [0,45,90,135,180,225,270,315]
def combination_lock(dial, combination):
    ans = []
    if len(dial[0]) == len(dial[1]):
        for i in dial:
            x = []
            for j in i:
                x.append(j)
                x.append(' ')
            x = x[:-1]
            ans.append(x)
            ans.append([' ']*len(x))
        ans = ans[:-1]
    else:
        leng = len(dial)
        for i in dial:
            x = []
            for j in i:
                x.append(j)
                x.append(' ')
            x = x[:-1]
            temp = (leng - len(x))//2
            while temp > 0:
                x.append(' ')
                x.insert(0, ' ')
                temp -= 1
            ans.append(x)
    ans1 = np.array(ans)
    lst0 = []
    for i in combination:
        i = i%360
        x = lst.index(i)
        ans2 = ans1
        if x%2 == 0:
            lstA = np.rot90(ans2, k=-x//2).tolist()
            lst0.append(lstA)

        else:
            x1 = (x-1)//2
            ans2 = np.rot90(ans2, k=-x1-1)
            lstA = []
            for j in range(len(ans2)-1, -len(ans2), -1):
                lstA.append(np.diag(ans2, k=j).tolist())
            lst0.append(lstA)
    ansA = []
    for i in lst0:
        temp1 = []
        for j in i:
            temp2 = []
            for k in j:
                if k == ' ':
                    continue
                else:
                    temp2.append(int(k))
            if temp2 != []:
                temp1.append(temp2)
        if temp1 != []:
            ansA.append(temp1)
    return ansA