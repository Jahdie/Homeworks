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
        return f"({self.complex_str})+({other.complex_str})={complex_add[0] if complex_add[0] !=0 else ''}" \
               f"{'+' if complex_add[1] > 0 and complex_add[0] !=0 else ''}" \
               f"{complex_add[1] if complex_add[1] !=0 else ''}i"

    def __mul__(self, other):
        complex_mul = []
        complex_mul.append((int(self.conversion(self.complex_str)[0]) * int(other.conversion(other.complex_str)[0])) -
                           (int(self.conversion(self.complex_str)[1]) * int(other.conversion(other.complex_str)[1])))
        complex_mul.append((int(self.conversion(self.complex_str)[1]) * int(other.conversion(other.complex_str)[0])) +
                           (int(self.conversion(self.complex_str)[0]) * int(other.conversion(other.complex_str)[1])))
        return f"({self.complex_str})*({other.complex_str})={complex_mul[0] if complex_mul[0] !=0 else ''}" \
               f"{'+' if complex_mul[1] > 0 and complex_mul[0] !=0 else ''}" \
               f"{complex_mul[1]if complex_mul[1] !=0 else '' }i"

    @staticmethod
    def conversion(complex_str):
        complex_list = []
        complex_str = complex_str.replace("i", "")
        if len(complex_str) == 0:
            complex_str = "1"
        if len(complex_str) == 1 or (complex_str[0] == "-" and len(complex_str) <= 2):
            complex_list.append(complex_str)
            complex_list.insert(0, "0")
        else:
            for i in range(1, len(complex_str)):
                if complex_str[i] == "-" or complex_str[i] == "+":
                    complex_list.append(complex_str[:i])
                    complex_list.append(complex_str[i:])
        if len(complex_list) == 1:
            complex_list.insert(0, "0")
        if complex_list[-1] == "-" or complex_list[-1] == "+":
            complex_list[-1] = complex_list[-1] + "1"

        return complex_list


my_complex1 = MyComplex("-8-3i")
my_complex2 = MyComplex("-3i")
print(my_complex1 + my_complex2)
print(my_complex1 * my_complex2)

