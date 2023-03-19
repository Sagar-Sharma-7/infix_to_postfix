output_stack = list()
operator_stack = list()

c_alpha = list()
c_not_alpha = list()
eqn = "A+B*C"
priority = {"+": 0, "-": 0, "*": 1, "/": 1}

def infix_postfix():
    # print(eqn)
    for i in eqn:
        if i.isalpha():
            c_alpha.append(i)
        elif i in list(priority.keys()):
            c_not_alpha.append(i)

    print(c_alpha)
    print(c_not_alpha)
    for i in eqn:
        if i in c_alpha:
            output_stack.append(i)
        elif i in c_not_alpha:
            if len(operator_stack) == 0:
                operator_stack.append(i)
                print(operator_stack)
                
            else:
                print(priority[operator_stack[c_not_alpha.index(i)-1]])
                print(priority[i])
                if priority[operator_stack[c_not_alpha.index(i) - 1]] == priority[i] or priority[operator_stack[c_not_alpha.index(i) - 1]] == 1:
                       x = operator_stack.pop()
                       output_stack.append(x)
                       operator_stack.append(i)
                else:
                    operator_stack.append(i)

infix_postfix()

if len(operator_stack) != 0:
    while len(operator_stack) != 0:
        y = operator_stack.pop()
        output_stack.append(y)

print(output_stack)
print(operator_stack)
