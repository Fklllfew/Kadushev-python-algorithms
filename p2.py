def bp(arr, n):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] > n:
            r = mid - 1
        elif arr[mid] < n:
            l = mid + 1
        else:
            return mid
    return -1

def fibs(n):
    prev = []
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibs(n - 1) + fibs(n - 2)

def fib(n, memo=[0, 1]):
    if n < len(memo):
        return memo[n]
    memo.append(fib(n - 1, memo) + fib(n - 2, memo))
    return memo[n]

def smith(arr):
    dp = [-1 for _ in range(len(arr))]
    dp[0], dp[1] = arr[0], arr[1]
    for i in range(2, len(arr)):
        dp[i] = min(dp[i - 1], dp[i - 2]) + arr[i]
    return(dp[-1])

def levenstein(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i

    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    return dp[n][m] 
    
def nopa(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]


def nvp(arr):
    dp = [1] * len(arr)

    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return(max(dp)) 



def backpack(v, p, w):
    n = len(w)
    dp = [[0] * (v + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        pi, wi = p[i - 1], w[i - 1]
        for j in range(1, v + 1):
            dp[i][j] = dp[i - 1, j]
            if wi <= j:
                dp[i][j] = max(dp[i - 1][j - wi] + wi, dp[i][j])
    return dp[n][v]




def levenstein(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b [j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1 
    return dp[n][m]   




def backpack(c, p, w):
    l = len(p)
    dp = [[0] * (c + 1) for _ in range(l + 1)]
    
    for i in range(1, l + 1):
        pi, wi = p[i-1], w[i-1]
        for j in range(1, c + 1):
            dp[i][j] = dp[i - 1][j]
            if wi <= j:
                dp[i][j] = max(dp[i][j], dp[i-1][j - wi] + pi)
    return dp[l][c]

def bubble_sort(m):
    n = len(m)
    for i in range(n):
        for j in range(n-i-1):
            if m[j] > m[j+1]:
                m[j], m[j+1] = m[j+1], m[j]
    return m

def insertion_sort(m):
    n = len(m)
    for i in range(n):
        el = m[i]
        j = i - 1
        while j >= 0 and el < m[j]:
            m[j+1] = m[j]
            j -= 1
        m[j+1] = el
    return m





print(insertion_sort([9,8,7,6,5,4,3,2]))            



