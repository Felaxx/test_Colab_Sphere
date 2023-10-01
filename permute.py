S = 'spam'
'''Bad'''
def permute_bad(S, x = '', L = []):              # параметры x и L нужны для внутреннего использования, передавать при вызове не нужно
    if len(S)==1:
        L.append(x+S) 
    for i in range(len(S)):
        permute_bad(S[i+1:]+S[:i], x+S[i], L)    # Пояснение : S2 = S[i:] + S[:i]; permute_bad(S2[1:], x+S2[0], L)
    if not x: return L
res_bad = permute_bad(S)
print(res_bad, len(res_bad))

'''Good'''
def permute_good(S):
    if not S: return [S]
    else:
        res = []
        for i in range(len(S)):
            rest = S[:i] + S[i+1:]
            for x in permute_good(rest):
                res.append(S[i:i+1]+x)
        return res
res_good = permute_good(S)
print(res_good, len(res_good))

'''Проверка'''
A, B = set(res_bad), set(res_good)
print('Проверка:', A == B)

'''Еще один вариант'''
def all_perms(arr):
    if len(arr)==1:
        return [arr] # терминальная ветвь
    else:
        a=arr[0] # первый элемент списка
        p=all_perms(arr[1:]) # все перестановки хвоста
        r=[]  # вставляем a в каждую возможную позицию каждой
        for pp in p: # перестановки хвоста
            for i in range(len(pp)):
                tmp=pp[0:i]+[a]+pp[i:]
                r.append(tmp)
            r.append(pp+[a])    
        return r
     
print(all_perms(list(S)))