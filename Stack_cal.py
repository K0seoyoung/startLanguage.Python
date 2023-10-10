class Stack:
    def __init__(self):
        self.items = []                 #데이터 저장을 위한 리스트 준비

    def push(self,val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()     #pop할 아이템이 없으면
        except IndexError:              #indexError 발생
            print("Stack is Empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is Empty")

    def __len__(self):                  #len()로 호출하면 stack의 item 수 변환
        return len(self.items)

    def isEmpty(self):
        return len(self) == 0

def get_token_list(expr):
    l = list(expr)
    operand = str()
    token_list = []
    length = len(expr)

    for token in l:
        if token in '()+-*/^':
            if len(operand) == 0:
                token_list.append(token)
            else:
                token_list.append(operand)
                token_list.append(token)
                operand = str()
        elif token == ' ':
            continue
        elif token == '.':
            operand += token
        elif token.isdecimal():
            operand += token
    if operand is not None and token.isdecimal():
        token_list.append(operand)
    return token_list

priority = {'+':1, '-':1, '*':2, '/':2, '^':3, '(':4, ')':0}

def infix_to_postfix(token_list):
    opstack = Stack()
    outstack = []

    for i in token_list:
        if i == '(':
            opstack.push(i)
        elif i == ')':
            while opstack.top() != '(':
                outstack.append(opstack.pop())
            opstack.pop()
        elif i in '+-*/^()':
            while not opstack.isEmpty():
                if priority[opstack.top()] >= priority[i]:
                    outstack.append(opstack.pop())
                else:
                    break
            opstack.push(i)
        else:
            outstack.append(i)
    while not opstack.isEmpty():
        outstack.append(opstack.pop())
    return outstack

def compute_postfix(token_list):
    s = Stack()
    for i in token_list:
        for i in priority:
            num1 = s.pop()
            num2 = s.pop()
            if i == '+':
                s.push(num2 + num1)
            elif i == '-':
                s.push(num2 - num1)
            elif i == '/':
                s.push(num2 / num1)
            elif i == '*':
                s.push(num2 * num1)

        else:
            s.push(float(i))
    return s.pop()

expr = input()
value = compute_postfix(infix_to_postfix(get_token_list(expr)))
print(value)