#oracle.py

import cx_Oracle

try:
    # 접속정보 만들기: 컴퓨터 ip, port 번호, sid
    dsnStr = cx_Oracle.makedsn("211.183.7.81", "1521", "xe")
    #데이터베이스 연결 객체 생성
    con = cx_Oracle.connect(user = "scott", password = "tiger", dsn = dsnStr)
    #데이터베이스 작업 객체 생성
    cursor = con.cursor()

    cursor.execute("select * from filesave")

    #전체 데이터 가져오기
    data = cursor.fetchall()

    #데이터 순회
    for imsi in data:
        print(imsi[0])
        #파일 기록을 위한 경로 생성
        f = open("c:/image/" + imsi[0], "wb")
        #기록할 데이터 가져오기
        blob = imsi[1]
        #파일에 기록
        offset = 1
        while True:
            #65536 바이트만큼 읽기 - 한번에 읽을 크기를 설정하는 것이므로 메모리 크기로 조절
            temp = blob.read(offset, 65536)  #숫자는 8의 배수 아무거나
            #읽을 데이터가 있으면 파일에 기록
            if temp:
                f.write(temp)
            #읽은 데이터가 65536보다 작으면 전부 읽은 것이므로 읽기 중단
            if len(temp) < 65536:
                break
            #앞쪽의 64k를 읽고 다음 데이터를 읽기 위해 offset 조정
            offset = offset + len(temp) #그림파일이 65536보다 클 것 같을 때
        f.close()
        #동작 후 image 파일에 jpeg 생성된 것을 볼 수 있음



    #sql은 excute를 호출하고 프로시저는 callproc를 호출
    #cursor.callproc("insert_dept", (14, "재무", "이대"))

    #읽을 파일 경로 만들기(파이썬은 디렉토리 기호를 '\' 혹은 '/' 모두 사용 가능)
    #파일 경로 찾기 어려우면 커맨드 창에 파일 끌어다 붙이면 경로 알려줌
    #filepath = "C:/cupcake.jpeg"  #c드라이브에 파일 저장하는 건 위험할 수 있음

    #파일 내용 읽기
    #f = open(filepath, 'rb')
    #photo = f.read()

    #파일 닫기(읽으면 꼭 닫아줘야)
    #f.close()

    #파일 이름 만들기 ('/'로 분할해서 가장 마지막 부분을 파일 이름으로 설정)
    #path = filepath.split("/")
    #filename = path[len(path) - 1]

    #sql 실행
    #cursor.execute('insert into filesave(filename, filecontent) values(:1, :2)', (filename, photo))


    #작업 내용을 원본 데이터베이스에 반영
    con.commit()

except Exception as e:
    print(e)

finally:
    #데이터베이스 연결 해제
    con.close()
