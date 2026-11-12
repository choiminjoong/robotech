import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


# Matplotlib : 데이터를 표현할 수 있게 해주는 파이썬 라이브러리
# figure => 큰 도화지
# subplots => 도화지 윈에 나눠진 작은 칸들

# 기본 스타일 적용
plt.style.use('default')

# x = [2,4,6,8]
# y = [1,3,5,7]
#plt.plot(x,y)
#plt.show()

fig = plt.figure()

# (행 개수, 열 개수, 위치값)
#fig.add_subplot(1,2,1)
#fig.add_subplot(2,2,2)

a1 = fig.add_subplot(1,2,1)
a2 = fig.add_subplot(1,2,2)

x1 = range(0,10)
y1 = range(5,15)
a1.plot(x1,y1, 'c*')

x2 = range(0,50)
y2 = range(0,50)
a2.plot(x2,y2, 'yh')


plt.show()
