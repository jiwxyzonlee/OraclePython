#py_mongo

from pymongo import MongoClient

#mongo db 연결
#변수 = MongoClient("ip주소", "포트번호")
#con = MongoClient("ip주소", "포트번호")
#포트 번호를 생략하면 27017
#ip주소를 생략하면 로컬 컴퓨터

con = MongoClient()
#print(con)

#(도움을 얻고 싶을 때)
#con이 사용할 수 있는 속성과 메소드 확인
con = MongoClient()
print(dir(con))

#데이터베이스 연결 및 생성
#데이터베이스변수 = 변수.데이터베이스이름
#-->데이터베이스 이름이 없으면 새로 만들어짐
db = con.mymongo

#컬렉션 연결 및 생성
#컬렉션변수 = 데이터베이스변수.컬렉션이름
#--> 컬렉션 이름 없으면 새로 생성됨
collection = db.sample

dict1 = {"name":"조지나", "nation":"라이베리아"}
dict2 = {"name":"에이미", "nation":"네덜란드"}
dict3 = {"name":"메림", "nation":"포르투갈"}

li = [dict2, dict3]

"""
#데이터 삽입
collection.insert_one(dict1)
collection.insert_many(li)
"""
#데이터 조회
result = collection.find_one()
#-->dict는 바로 출력해도 되고 dict['key']를 이용해서 부분적으로 사용
print(result)

#이름만 출력하기
#print(result['name'])

result = collection.find()

"""
#조건 넣어 데이터 찾기
#result = collection.find({"name":"조지나"})
#print(type(result))
#자료형이 모르는 클래스이므로 사용 가능한 속성 확인
#print(dir(result))
#__iter__ 가 있으면 for - in 사용 가능
for temp in result:
    print(temp)
"""


"""
#name이 조지나인 데이터의 nation을 모잠비크로 변경
collection.update_one({"name":"조지나"}, {"$set":{"nation":"모잠비크"}})
result = collection.find({"name":"조지나"})
for temp in result:
    print(temp)
"""

#print(dir(collection))