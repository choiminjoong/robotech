def solution(n, w, num):
    answer = 0
    
    # 제한사항 충족
    if 2 <= n <= 100 and 1 <= w <= 10 and 1 <= num <= n:
        # 1층 이하
        if n <= w: 
            return 1
        
        # 배열화
        arr = [[j if j <= n else 0 for j in range(i, i + w)]
            for i in range(1, n + 1, w)]    

        # 배열 순서 정렬
        for i in range(len(arr)):
            if (i + 1) % 2 == 0:
                arr[i] = arr[i][::-1]

        # num열 숫자 나열
        numIndex = arr[int((num-1) / w)].index(num)
        
        for i in arr:
            if i[numIndex] >= num:
                answer = answer + 1 

        return answer
    # 제한사항 위반
    else:
        print("제한사항 위반")


solution(13,5,3)        