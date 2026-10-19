french = set(map(int, input().split()))
swim = set(map(int, input().split()))
music = set(map(int, input().split()))
res = (swim & music) - french
print(res)
