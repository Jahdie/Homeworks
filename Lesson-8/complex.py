# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методовсложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
class MyComplex:
    def __init__(self, complex_str):
        self.complex_str = complex_str

    def __str__(self):
        return f"{self.complex_str}"

    def __add__(self, other):
        complex_add = []
        complex_add.append(int(self.conversion(self.complex_str)[0]) + int(other.conversion(other.complex_str)[0]))
        complex_add.append(int(self.conversion(self.complex_str)[1]) + int(other.conversion(other.complex_str)[1]))
        return f"{self.complex_str}+{other.complex_str}={complex_add[0]}{'+' if complex_add[1] > 0 else ''}" \
               f"{complex_add[1]}i"

    def __mul__(self, other):
        complex_mul = []
        complex_mul.append((int(self.conversion(self.complex_str)[0]) * int(other.conversion(other.complex_str)[0])) -
                           (int(self.conversion(self.complex_str)[1]) * int(other.conversion(other.complex_str)[1])))
        complex_mul.append((int(self.conversion(self.complex_str)[1]) * int(other.conversion(other.complex_str)[0])) +
                           (int(self.conversion(self.complex_str)[0]) * int(other.conversion(other.complex_str)[1])))
        return f"{self.complex_str}+{other.complex_str}={complex_mul[0]}{'+' if complex_mul[1] > 0 else ''}" \
               f"{complex_mul[1]}i"

    @staticmethod
    def conversion(complex_str):
        complex_list = []
        complex_str = complex_str.replace("i", "")
        for index in range(1, len(complex_str)):
            if complex_str[index] == "-" or complex_str[index] == "+":
                complex_list.append(complex_str[:index])
                complex_list.append(complex_str[index:])
        return complex_list


my_complex1 = MyComplex("-2+3i")
my_complex2 = MyComplex("-1+3i")
print(my_complex1 + my_complex2)
print(my_complex1 * my_complex2)
