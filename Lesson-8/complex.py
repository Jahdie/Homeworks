# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методовсложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
z1 = "-2+3i"
z2 = "-1+i"
z1_1 = z1.replace("i", "")
z2_1 = z2.replace("i", "")
new_list1 = ['-2', '+3']
new_list2 = ['-1', '1']
for i in range(1, len(z1_1)):
    if z1_1[i] == "-" or z1_1[i] == "+":
        new_list1.append(z1_1[:i])
        new_list1.append(z1_1[i:])
for i in range(1, len(z2_1)):
    if z2_1[i] == "-" or z2_1[i] == "+":
        new_list2.append(z2_1[:i])
        new_list2.append(z2_1[i:])
print(new_list1)
print(new_list2)
z = []
z3 = []
z.append(int(new_list1[0])+int(new_list2[0]))
z.append(int(new_list1[1])+int(new_list2[1]))
z3.append((int(new_list1[0])*int(new_list2[0]))-(int(new_list1[1])*int(new_list2[1])))
z3.append((int(new_list1[1])*int(new_list2[0]))+(int(new_list1[0])*int(new_list2[1])))

string = f"{z[0]}{'+' if z[1]>0 else ''}{z[1]}i"
string1 = f"{z3[0]}{'+' if z3[1]>0 else ''}{z3[1]}i"

print(string)
print(string1)
