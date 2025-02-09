s = input("Enter the numerical expression: ")
curr_operation = "+"
curr_number = 0
stack = []

for i in s:
    if i.isnumeric():
        curr_number=curr_number*10+int(i)
    elif i in "+-*/(":
        if curr_operation=="+":
            stack.append(curr_number)
        elif curr_operation=="-":
            stack.append(-curr_number)
        elif curr_operation=="*":
            stack[-1] = stack[-1] * curr_number
        elif curr_operation=="/":
            stack[-1] = stack[-1]/curr_number
        curr_operation = i
        curr_number = 0

if curr_number:
    if curr_operation=="+":
        stack.append(curr_number)
    elif curr_operation=="-":
        stack.append(-curr_number)
    elif curr_operation=="*":
        stack[-1] = stack[-1] * curr_number
    elif curr_operation=="/":
        stack[-1] = stack[-1]/curr_number

res = 0
for i in stack:
    res+=i

print("result", res)

        