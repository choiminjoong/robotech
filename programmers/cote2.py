import numpy as np

# k= 방 개수
# room_number= 원하는 방 번호
# answer = 배정된 방 번호
def solution(k, room_number):
    answer = []
    room_number = np.array(room_number)
    if (type(k) != int) | (k < 1) | (k > 10**12):
        print('방 개수 오류')
        return False
    
    rooms = np.arange(k) +1
    answer = np.zeros_like(room_number) # 배정현황 초깃값 [0, 0, 0, .....] 
    cnt_reserved_rooms = np.count_nonzero(answer) # 배정된 방 수
    cnt_nonreserved_rooms = len(room_number) # 대기중인 방 수
    print(f'\n배정된 방 수: {cnt_reserved_rooms}')
    print(f'대기중인 방 수: {cnt_nonreserved_rooms}')



    # 예약 함수
    def reserve(number_arr):
        cnt_fail = 0
        for idx, num in enumerate(number_arr):
            if (num == 0):
                print(f'{print(f'\nRoom{num} 예약실패')    }')    
            elif(rooms[num-1] != 0) & (num <= k):
                answer[idx] = num
                rooms[num-1] = 0
                room_number[idx] = 0
                print(f'\n{idx+1 }번 손님 Room{num} 예약완료')
            else:
                print(f'\nRoom{num} 예약실패')    
                      
        
        if np.count_nonzero(room_number) > 0:
            room_number[room_number !=0] +=1
            print(f'\n대기자 현황: {room_number}')
            return True
        else:
            print(f'\n대기자 없음')
            return False
    
    # 최초 예약
    reserve(room_number)
    
    #while cnt_reserved_rooms != len(room_number):
    reserve(room_number)

    print('\ntest 결과')
    print(f'rooms: {rooms}')
    print(f'room_number: {room_number}')
    print(f'\nanswer: {answer}')

    return answer

solution(10, [1,5,7,6,7])