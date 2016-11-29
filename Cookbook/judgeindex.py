def list_get(L, i, v=None):
    if -len(L) < i < len(L):
        return L[i]
    else:
        return v

if __name__ == '__main__':
    x = list_get([1,2,3,4], 2)
    print x
    x = list_get([1,2,3,4], 5)
    print x
