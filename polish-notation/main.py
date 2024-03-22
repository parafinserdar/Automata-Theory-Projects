def polish(ifade):
    stack = []

    liste = ifade.split()

    for l in liste[::-1]:
        if l.isdigit() or (l[0] == '-' and l[1:].isdigit()):
            stack.append(int(l))
        elif l in ['+', '-', '*', '/']:
            operand1 = stack.pop()
            operand2 = stack.pop()

            if l == '+':
                stack.append(operand1 + operand2)
            elif l == '-':
                stack.append(operand1 - operand2)
            elif l == '*':
                stack.append(operand1 * operand2)
            elif l == '/':
                stack.append(operand1 / operand2)

    return stack.pop()

ifade = input("String ifadeyi giriniz : ")
sonuc = polish(ifade)
print("Sonuç:", sonuc)
