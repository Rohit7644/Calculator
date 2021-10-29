def str_data(str1):
    lst = [str(i) for i in range(0, 10)]
    lst.append(".")
    if str1 in lst:
        return True
    else:
        return False
def result(l, a, b):
    if '/' == l:
        res = a / b
    elif '*' == l:
        res = a * b
    elif '+' == l:
        res = a + b
    elif '-' == l:
        res = a - b
    elif '^' == l:
        res = a ** b
    else:
        pass
    return str(res)


def cal_data(str2, t):
    con_a=True
    con_b=True
    i = 1
    j = 1
    a = 0
    b = 0
    a = str2[t+i]
    if a in ['+', '*', '/', '-', '^']:
        print(str2[t+i])
        return "ERROR"
    while con_a:
        if t - i >= 0:
            if str_data(str2[t - i]):
                a = float(str2[t - i:t])
                i += 1
            else:
                con_a = False
        else:
            con_a = False
    while con_b:
        if t + j + 1 <= len(str2):
            if str_data(str2[t + j]):
                b = float(str2[t + 1:t + j + 1])
                j += 1
            else:
                con_b = False
        else:
            con_b = False

    return a, b, i, j

def simple_calc(str_pass):
    opr_dict ={
        '^' : str_pass.count('^'),
        '/' : str_pass.count('/'),
        '*' : str_pass.count('*'),
        '+' : str_pass.count('+'),
        '-' : str_pass.count('-')
    }

    for opr, count in opr_dict.items():
        prev_loc = 0
        for i in range(0, count):
            new_loc=str_pass.find(opr, prev_loc)
            prev_loc=new_loc

            # ERROR
            if  cal_data(str_pass, prev_loc) == "ERROR":
                return "SyntaxError"
            a, b, i1, j1 = cal_data(str_pass, prev_loc)
            res = result(opr, a, b)
            str_pass =str_pass.replace(str_pass[prev_loc-i1+1:prev_loc+j1], res)

    return str_pass

def scientifi_calculator(str1=""):
    termination = True
    while termination:
        if '(' not in str1:
            termination = False
            try:
                return simple_calc(str1)
            except:
                return "SyntaxError"
        else:
            if str1.count('(') != str1.count(')'):
                print("invalid input")
                termination =False
                return "SyntaxError"
            else:
                n = str1.find(')')
                f = 0
                while True:
                    if str1[n - f] == "(":
                        break
                    f += 1
                str2 = str1[n - f + 1:n]
                try:
                    res = simple_calc(str2)
                except:
                    return "SyntaxError"
                str1 = str1.replace(str1[n - f:n + 1], res)

