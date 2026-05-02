arr = list(map(int,input().split()))

arr.sort()

target = int(input("Enter target value: "))

n = len(arr)
left = 0
right = n - 1

found = False

while left < right:
    current_sum = arr[left] + arr[right]
    
    if current_sum == target:
        print(f"Found {arr[left]} + {arr[right]} = {target}")
        found = True
        break
    elif current_sum < target:
        left += 1
    else:
        right -= 1

if not found:
    print("No Pair Found")