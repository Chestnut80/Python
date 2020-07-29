bit1 = 0x61
bit2 = 0x62

print(hex(bit1 & bit2)) #and 연산
print(hex(bit1 | bit2)) #or 연산
print(hex(bit1 ^ bit2)) #xor 연산
print(hex(bit1 >> 1))   #n만큼 오른쪽으로 시프트 연산
print(hex(bit1 << 2))   #n만큼 왼쪽으로 시프트 연산
