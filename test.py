print('네이버' in '네이버예약')


addr = '서울 강남구 역삼동'

for i in range(1, 51):
    if any(i in addr for i in ['강남구']):
        print(f"i : {i}")
        print(F'addr : {addr}')
