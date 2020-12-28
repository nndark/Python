
# 

# 파이썬 시각화

# import
import matplotlib as mpl
import matplotlib.pylab as plt


# 출력 
%matplotlib inline # 코드북에 출력
%matplotlib qt # 팝업창 출력

# 차트 시각화 호출
plt.show()

# 선 그래프 
plt.plot(x, y)
plt.plot(y)

# 그래프 다중으로 그리기
plt.plot(x1, y1, x2, y2, x3, y3)

# 새로운 창 생성하기 - 여러 창으로 분할해서 보기 위해서 사용
plt.fiqure(2,2,1) # 2*2 분할 플랏 중 1번 
plt.fiqure(2,2,2) # 2*2 분할 플랏 중 2번
plt.fiqure(2,2,3) # 2*2 분할 플랏 중 3번
plt.fiqure(2,2,4) # 2*2 분할 플랏 중 4번

# 하나의 창에 여러 그래프 그리

plt.sublot()

# 그래프 지우기
plt.clf())

# 타이틀 추가하기
plt.title('TITLE')

# Grid 추가하기
plt.grid(True)

# X, Y 라벨 추가하기
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 범례 추가하기
plt.legend(['legend1', 'legend2'])
plt.legend(['legend1', 'legend2'], loc = 'lower right') # 범례 위치 조정
plt.legend(['legend1', 'legend2'], loc = 'best') # 범례 위치 조정
plt.legend(['legend1', 'legend2'], loc = 'upper center') # 범례 위치 조정


# 텍스트 추가하기
plt.text(0, 1, "text1")
plt.text(1, 1, "text1")
plt.text(5, 1, "text1")
plt.text(5, 5, "text1")

# 그래프  컬러 선스타일, 마커 꾸미기
fmt = '[color][line_style][marker]'

# X,Y 축 최대 출력 제한하기
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)


# 히스토 그램 그리기
plt.hist(x)
plt.hist(x, ,bins = 10)

# 산점도 그리기
plt.scatter(x, y, s = 5, c= r) #  s= size , c = color

# 막대 그래프 그리기
plt.bar(x, y)
plt.hbar(x, y) # 막대 가로 형태로 그리기 
plt.bar(x, y, tick_label = label_name) # 라벨 보여주기 
plt.bar(x, y, tick_label = label_name, width = 0.3) # 바 두께 조절

# 파이 차트 그리기
plt.fiqure(figsize = (5, 5)) # 차트 비율 마추기 
plt.pie(x, labels = label_name, autopct = '%.1f%%', startangle = 90) # 라벨 추가와 퍼센트 노출, 파트 시작 각도 

# 그래프 저장하기
plt.savefig(file_name, dpi = 100)
plt.savefig('c:/python/plt.png', dpi = 100)

# 그래프 옵션
format string(fmt)

# 그래프 한글 사용하는 방법
matplotlib.rcParams['font.family']

# 폰트 변경 방법
matplotlib.rcParams['font.family'] = 'font_name'
matplotlib.rcParams['font.family'] = 'Malgun Gothic'

matplotlib.rcParams['axes.Unicode_minus'] = False #폰트 마이너스 깨짐 문제 해결

# 폰트 이름 리스트 확인
import matplotlib.font_manager
Font_list = matplotlib.font_manager.get_fontconfig_fonts()
Font_names = matplotlib.font_manager.Fontproperties(fname = fname).Get_name() for fname in font_list




