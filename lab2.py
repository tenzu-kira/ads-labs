from queue import LifoQueue
PRIORITY = {
   "start": 0,
    "(": 1,
    ")": 1,
    "*": 3,
    "/": 3,
    "+": 2,
    "-": 2,
}

def tokenize(expression):
    expression = expression.replace(" ", "")
    expression = expression.removesuffix("=")
    for sym in PRIORITY.keys():
        expression = expression.replace(str(sym), f" {sym} ")
    return expression.split()

def convert(tokens):
    result = []
    temporary_stack = ["start"]
    while len(tokens):
        if tokens[0].isnumeric():
            result.append(tokens.pop(0))
            continue

        stack_item = temporary_stack[len(temporary_stack) - 1]
        input_item = tokens[0]

        if stack_item == "(" and input_item == ")":
            tokens.pop(0)
            temporary_stack.pop()
        elif stack_item == "start" and input_item == ")":
            raise SyntaxError("Incorrect expression")
        elif stack_item == "(" and not len(tokens):
            raise SyntaxError("Incorrect expression")
        else:
            if input_item == "(":
                temporary_stack.append(tokens.pop(0))
            elif PRIORITY.get(stack_item) < PRIORITY.get(input_item):
                temporary_stack.append(tokens.pop(0))
            else:
                result.append(temporary_stack.pop())
    temporary_stack.pop(0)
    temporary_stack.reverse()
    result.extend(temporary_stack)
    return result

def evaluate(tokens):
  stack = LifoQueue()
  for token in tokens:
    if token not in "+-*/":
      stack.put(float(token))
    else:
      right, left = stack.get(), stack.get()
      match token:
        case'+':
          stack.put(left + right)
        case '-':
          stack.put(left - right)
        case '*':
          stack.put(left * right)
        case '/':
          assert right != 0
          stack.put(left / right)
  return stack.get()

exp = input("введите выражение")
print(evaluate(convert(tokenize(exp))))
