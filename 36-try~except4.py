import time

count = 1

try :
    while True:
        county = "\r%d"%count
        count+=1
        print(''*len(county), end='')
        print(county, end='')
        time.sleep(0.5)
except KeyboardInterrupt:
    print("사용자에 의해 프로그램이 중단되었습니다")
