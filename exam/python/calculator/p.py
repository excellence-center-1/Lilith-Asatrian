def update(op, val, stack):
    if op=="+":
        stack.append(val)
    elif op=="-":
        stack.append(-val)
    elif op=="*":
        stack.append(stack.pop()*val)
    elif op == "/":
        stack.append(int(stack.pop()/val))

def calculate(s):
    ind, curr_num, op, stack = 0, 0, "+", []
    while ind<len(s):
        ch = s[ind]
        if ch.isdigit():
            curr_num = curr_num*10+int(ch)
        elif ch in "+-*/":
            update(op, curr_num, stack)
            op, curr_num = ch, 0
        elif ch == "(":
            curr_num, j = calculate(s[ind+1:])
            ind = ind + j
        elif ch == ")":
            update(op, curr_num, stack)
            return sum(stack), ind+1
        ind+=1
    update(op, curr_num, stack)
    return sum(stack), ind

res, _ = calculate("(25+15)/8-3*15")
print("res: ", res)