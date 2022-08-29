# 21번
letters = 'python'
print(letters[0],letters[2])
# 22번
license_plate= "24가 2210"
print(license_plate[-4:])
# 23번
string ="홀짝홀짝홀짝"
print(string[::2])
# 24번
string="PYTHON"
print(string[::-1])
# 25번
phone_number="010-1111-2222"
answer=phone_number.replace('-',' ')
print(answer)
# 26번
phone_number="010-1111-2222"
answer=phone_number.replace('-','')
print(answer)
# 27번
url ="http://sharebook.kr"
print(url[-2:])
# 28번
# lang ='python'
# lang[0]='P'
# print(lang) #문자열을 수정할 수 없음
# 29번
string='abcdef2a354a32a'
answer1=string.replace('a','A')
print(answer1)
# 30번
string='abcd'
string.replace('b','B')
print(string) #aBcd로 출력
# 31번
a="3"
b="4"
print(a+b) #34로 출력
# 32번
print("Hi"*3) #HiHiHi로 출력
# 33번
print("-"*80)
# 34번
t1='python'
t2='java'
t3= t1+' '+t2+' '
print(t3*4)
# 35번
name1="김민수"
age1=10
name2="이철희"
age2=13
print("이름: %s 나이: %d"%(name1,age1))
print("이름: %s 나이: %d"%(name2,age2))
# 36번
name1="김민수"
age1=10
name2="이철희"
age2=13
print("이름: {} 나이: {}".format(name1,age1))
print("이름: {} 나이: {}".format(name2,age2))
# 37번
name1="김민수"
age1=10
name2="이철희"
age2=13
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")
# 38번
상장주식수 ="5,969,782,550"
answer2=상장주식수.replace(',','')
print(int(answer2))
# 39번
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])
# 40번
data="   삼성전자   "
data1=data.strip()
print(data1)
# 41번
ticker="btc_krw"
ticker1=ticker.upper()
print(ticker1)
# 42번
ticker="BTC_KRW"
ticker2=ticker.lower()
print(ticker2)
# 43번
b='hello'
b1=b.capitalize()
print(b1)
# 44번
file_name="보고서.xlsx"
if file_name.endswith('xlsx'):
    print("True")
# 45번
file_name="보고서.xlsx"
if file_name.endswith('xlsx') or file_name.endswith('xls'):
    print("True")
# 46번
file_name="2020_보고서.xlsx"
if file_name.startswith('2020'):
    print("True")
# 47번
a="hello world"
a1=a.split()
print(a1)
# 48번
ticker="btc_krw"
ticker3=ticker.split('_')
print(ticker3)
# 49번
data="2020-05-01"
data1= data.split('-')
print(data1)
# 50번
data="039490        "
data2=data.rstrip()
print(data2)
# 51번
movie_rank=['닥터 스트레인지','스플릿','럭키']
# 52번
movie_rank.append('배트맨')
# 53번
movie_rank.insert(1,'슈퍼맨')
# 54번
movie_rank.remove('럭키')
# 55번
movie_rank.remove('스플릿')
movie_rank.remove('배트맨')
# 56번
lang1 = ["C","C++","Java"]
lang2=["Python","GO","C#"]
langs=lang1+lang2
print(langs)
# 57번
nums=[1,2,3,4,5,6,7]
print("max: {}".format(max(nums)))
print("min: {}".format(min(nums)))
# 58번
nums=[1,2,3,4,5]
total=0
for i in nums:
    total+= i
print(total)
# 59번
cook=["피자","김밥","만두","양념치킨","족발","피자","김치만두","쫄면","소시지","라면","팥빙수","김치전"]
print(len(cook))
# 60번
nums=[1,2,3,4,5]
total=0
for i in nums:
    total+=i
average=total/len(nums)
print(average)
# 61번
price=['20180728',100,130,140,150,160,170]
print(price[1:])
# 62번
nums=[1,2,3,4,5,6,7,8,9,10]
print(nums[::2])
# 63번
nums=[1,2,3,4,5,6,7,8,9,10]
print(nums[1::2])   
# 64번
nums=[1,2,3,4,5]
print(nums[::-1]) 
# 65번
interest=['삼성전자', 'LG전자', 'Naver']
print(interest[0],interest[2])