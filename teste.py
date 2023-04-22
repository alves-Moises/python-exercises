def cal_fat(n): 
    fat = 1 
    for i in range(2,n+1): 
        fat *= i 
    return fat 

n = -1 
while n <= 0: 
    n = int(input("Digite um número positivo: ")) 

h = 1 
h += n 
n_pow = 2 
termos = 3 
while termos <= n: 
    h += n_pow * n 
    n_pow *= termos * (termos-1) 
    termos += 1 
h -= (n-3) * cal_fat(4) 
h -= (n-4) * cal_fat(5) 
print(h)


