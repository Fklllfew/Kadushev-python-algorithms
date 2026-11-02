# def levenstein(a, b):
#     m = len(a)
#     n = len(b)

#     dp = [[0] * (n + 1) for _ in range(m + 1)]

#     # база: первая строка (вставки) и первый столбец (удаления)
#     for i in range(m + 1):
#         dp[i][0] = i
#     for j in range(n + 1):
#         dp[0][j] = j

#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             if a[i-1] == b[j-1]:
#                 dp[i][j] = dp[i-1][j-1]
#             else:
#                 dp[i][j] = min(dp[i-1][j],      # удаление
#                                dp[i][j-1],      # вставка
#                                dp[i-1][j-1]) + 1  # замена
#     return dp[m][n]


# def subseq(a, b):
#   dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
#   for i in range(1, len(a) + 1):
#     for j in range(1, len(b) + 1):
#       if a[i - 1] == b[j - 1]:
#         dp[i][j] = dp[i - 1][j - 1] + 1
#       else:
#         dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
#   return dp[len(a)][len(b)]
# print(subseq('abcabaac', 'baccbca'))





def growingsubseq(a):
    if not a:
        return []

    n = len(a)
    dp = [1] * n
    prev = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if a[j] < a[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    # индекс конца лучшей подпоследовательности
    end = 0
    for i in range(1, n):
        if dp[end] < dp[i]:
            end = i

    # восстановление
    answer = []
    i = end
    print(dp)
    print(prev)
    while i != -1:
        print(i)
        answer.append(a[i])
        i = prev[i]

    return answer[::-1]      # разворачиваем: шли с конца
  

  # return max(dp)

print(growingsubseq([-1,7,3,4,1,6,12]))


  
# def backpack(w, price, weight):
#   dp = [[0] * (w + 1) for _ in range(len(weight) + 1)]
#   for i in range(1, len(weight) + 1):
#     for j in range(1, w + 1):
      
  
