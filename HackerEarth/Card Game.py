def card_game(arr,brr):
    total = 0
    maximum = max(brr)+1
    for i in range(len(arr)):
        if arr[i]>=maximum:
            return total
        total += (maximum-arr[i])
    return total

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
brr = list(map(int, input().split()))
arr.sort()
print(card_game(arr, brr))
