import numpy as np

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    matrix1 = np.genfromtxt('Zadanie_1.csv', delimiter=';', skip_header=True)

    print("Liczba komórek: ")
    print(matrix1.size)


    print("Liczba wierszy i kolumn: ")
    print(matrix1.shape)

    print("Średnia: ")
    print(np.mean(matrix1))

    print("Mediana: ")
    print(np.median(matrix1))

    print("Wariancja: ")
    print(np.var(matrix1))

    matrix1 =np.nan_to_num(matrix1)


    print("Średnia: ")
    print(np.mean(matrix1))

    print("Mediana: ")
    print(np.median(matrix1))

    print("Wariancja: ")
    print(np.var(matrix1))

    matrix2 = np.genfromtxt('Zadanie_2.csv', delimiter=';', skip_header=False)

    print("Wartości własne i wektory własne: ")
    print(np.linalg.eig(matrix2))

    print("Macierz odwrotna: ")
    print(np.linalg.inv(matrix2))






