import numpy as np
import pandas as pd
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


#zad3
print("zad3")
a= np.genfromtxt('Zadanie_3_macierz_A.csv', delimiter=',')
b= np.genfromtxt('Zadanie_3_macierz_B.csv', delimiter=',')
print(a.dot(b.transpose())/(np.std(a)*np.std(b)))

#zad4
print("zad4")


df= pd.read_csv('Zadanie_4.csv', sep=';')
df['Hour'] = pd.to_datetime(df['DateTime']).dt.hour
df['Date'] = pd.to_datetime(df['DateTime']).dt.date
df['Minute'] = pd.to_datetime(df['DateTime']).dt.minute

result = df[["DoctorID",'Type',"City","Date",'Hour']].groupby(['DoctorID','Type',"City","Date","Hour"]).nunique()
result[["First Minute"]] = df.groupby(["DoctorID",'Type',"City","Date","Hour"])[["Minute"]].first()
result[["Last Minute"]] = df.groupby(["DoctorID",'Type',"City","Date","Hour"])[["Minute"]].last()
result.to_csv("result.csv", sep=";")
print(result)




