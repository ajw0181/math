import math
year=int(input('처음 연도:'))
YEAR=int(input('매출액이 증가한 연도:'))
a=int(input('처음 연도의 매출액(억):'))
A=int(input('매출액이 증가한 연도의 매출액(억):'))
x=YEAR-year
b=round(math.log10(A/a),2)*1/x
r=round((round(10**b,2)-1)*100,1)
print('매년 증가한 매출액의 퍼센트는',r,'%이다.')