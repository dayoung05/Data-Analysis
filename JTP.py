a='hello world'
print(a)

# 문자열 관련 함수
# count - 문자 개수 세기
a = "hobby"
print(a.count('b'))


a = "Python is the best choice"
print(a.find('b'))

print(a.find('k'))

print(",".join('abcd'))

# 소문자를 대문자로 upper
a = "hi"
print(a.upper())

# 대문자를 소문자로 lower
a= "hi"
print(a.lower())

a= " hi "
print(a.lstrip())
print(a.rstrip())
print(a.strip())

# replace - 문자열 바꾸기
a='Life is too short'
print(a.replace('Life','your leg'))


# split - 문자열 나누기
a='Life is too short'
print(a.split())

b='a:b:c:d'
print(b.split(':'))

#02-3 리스트 자료형
a=[1,2,3]
print(a[0])
print(a[0]+a[2])
print(a[-1])

a = [1,2,3,['a','b','c']]
print(a[-1])

# 리스트 a의 'a'값 인덱싱
print(a[-1][0])

# 리스트 슬라이싱
a=[1,2,3,4,5]
print(a[0:2])
print(len(a))

# 값 수정하기
a=[1,2,3,4,5]
a[2] =6
print(a)


del a[1]
print(a)
a.append(6)
print(a)
a.append([7,8])
print(a)

a=[1,2,7,4,5]
a.sort()
print(a)
a.reverse()
print(a)

a=[1,2,3,4,5]
a.insert(0,4)
print(a)

a=[1,2,3,4,5]
print(a.pop())
print(a)

'''02-4 튜플 ()
#  리스트와 같이 생성, 삭제, 수정 불가.
#  괄호 생략가능/한가지 요소만 가지는 경우 콤마, 반드시 입력
'''

"""02-5 딕셔너리 {}
대응관계("이름"="최다영")
key와 value
리스트나 튜플처럼 순차적으로 요솟값 구하지 않고 key와 value를 통해 얻는다. 
-key: 변하지 않는 값
-value: 변하는 값/리스트를 넣을 수 있다. 
"""

# 딕셔너리 쌍 추가
a={1:'a'}
a[2] = 'b'
print(a)

a["name"]="pey"
print(a)

# 딕셔너리 삭제
del a[1]
print(a)

# 동일한 key 값 사용시  하나를 제외한 나머지 것 모두 무시
# key 값 가능한 것 : 튜플O, 리스트 x (리스트는 값이 변할 수 있기 때문에 불가)
a = {'name':'pey', 'phone':'01023445567','birth':'1121'}
print(list(a.keys()))
print(a.items())
print(a.get('name'))

print(a.get('foo', 'bar'))

print('name' in a)

'''02-06 집합 자료형
집합 자료형 set
- 중복 허용 하지 않음
- 순서 없음

순서O: 리스트, 튜플
순서X: 집합(set), 딕셔너리
'''

s1 =set([1,2,3])
print(s1)

s2= set('hello')
print(s2)
# 리스트, 튜플은 순서가 있어 인덱싱을 통해 자료형 값을 얻을 수 있음

# 인덱싱 접근하려면 리스트, 튜블로 변경
s1 =set([1,2,3])
l1 = list(s1)
print(l1)

s1 = set([1,2,3,4])
s2 = set([5,6,7,8])

print(s1|s2)
s1.union(s2)

print(s1&s2)
s1.intersection(s2)

s1 = set([1,2,3,4])
s1.add(5)
print(s1)

# 02-8 자료형 값을 지정
# 변수란 객체를 가리키는 것

a=[1,2,3]
a[1]=4
print(a)

a=[1,2,3]
b=a[:]
a[1]=4
print(a)
print(b)
# a 리스트 값을 바꾸더라도 b값에 영향을 미치지 않는다.
from copy import copy
a =[1,2,3]
b=copy(a)

print(b is a)
# b와 a가 가리키는 객체는 서로 다르다.

a,b = ('python','life',)
(a,b) = 'python', 'life'

# 2장 연습문제
# Q3
pin = '881120-1068234'
yymmdd = pin[:6]
num = pin[7:]
print(yymmdd)
print(num)

# Q4
print(pin [7])

# Q5
a = 'a:b:c:d'
b= a.replace(':','#')
print(b)

# Q6
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

# Q7 (공백을 넣어주어야 한다.)
a = ['life','is','too','short']
result = " ".join(a)
print(result)

# Q8
a = (1,2,3)
a=a+(4,)
print(a)

# Q9
# a[[1]] = 'python'
# 오류 발생이유
# 리스트는 변하는 값으로  딕셔너리 키로 사용 불가

# Q10
a = {'A':90, 'B':80, 'c':70}
result = a.pop('B')
print(a)
print(result)

# Q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
print(a)
b = list(aSet)
print(b)
# 리스트 자료형이 집합으로 변환되면서 중복 삭제됨

# Q12
a=b=[1,2,3]
a[1] =3
print(b)

# 03-1 if문
money = True
if money:
    print('택시를 타고 가라')
else:
    print('걸어가라')

money = 20000
if money >= 30000:
    print('택시 타기')
else:
    print('걸어가자')

money = 20000
card =True

if money >= 30000 or card:
    print('택시')
else:
    print('걷자')

# x in s, x not in s
pocket = ['paper','cellphone','money']
if 'money' in pocket:
    print('택시타자')
else:
    print('걷자')

if 'money' in pocket:
    pass
else:
    print('걷자')
# 간략하게 하는법
if 'money' in pocket:pass
else: print("카드꺼내")


pocket = ['paper','handphone']
card = True
if 'money' in pocket:
    print('택시타')
else:
    if card:
        print('카드도 택시')
    else:
        print('걸어가자')

# 조건부 표현식
score = 70
if score >=60:
    massage = 'success'
else:
    massage = 'failure'
print(massage)
massage = 'success' if score >= 60 else "failure"

# 03-2 while문
treehit =0
while treehit <10:
    treehit = treehit+1
    print('나무를 %d번 찍었습니다'%treehit)
    if treehit ==10:
        print('나무 넘어갑니다.')

prompt = """
1. add
2. del
3. list
4. quit

enter number:"""

number = 0
while number !=4:
    print(prompt)
    number = int(input())

coffee =10
money = 300
while money:
    print('돈을 받아서 커피를 준다')
    coffee =coffee -1
    print('남은 커피양은 %d개'%coffee)
    if coffee == 0:
        print('커피가 없다. 판매 중지')
        break

coffee = 10
while True:
    money = int(input('돈줘:100'))
    if money == 300:
        print('커피를 줍니다.')
        coffee = coffee -1
    elif money >300:
        print('거스름돈 %d를 주고 커피 줘'% (money -300))
        coffee = coffee -1
    else:
        print('돈돌려주고 커피 안줌')
        print('남은 커피 양은 %d개' %coffee)
    if coffee == 0:
        print('커피 다팔았어')
        break

# 03-3 for
test_list = ['one','two','three']
for i in test_list:
    print(i)

a= [(1,2), (3,4),(5,6)]
for (first, last) in a:
    print(first+last)

marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number =number +1
    if mark >=60:
        print('%d 번 학생은 합격입니다.'%number)
    else:
        print('%d번 학생 불합격'%number)


number = 0
for mark in marks:
    if mark < 60:
        continue
    else:
        print('%d번 학생 합격 축'%number)

# range: 리스트를 자동으로 만들어주는 함수
a = range(10)
print(a)

add = 0
for i in range(1,11):
    add = add+i
print(add)

mark = [90, 25, 67, 45, 80]
for number in range(len(mark)):
    if mark[number] <60:
        continue
    print("%d번 학생 축하 합격임"%(number+1))

# 구구단
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print('')

a=[1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)
