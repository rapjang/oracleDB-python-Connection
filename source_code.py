# Python 버전 :  3.8.8
import sys
print("Python 버전 : ", sys.version)


# cx_Oracle 버전 :  8.3.0
import cx_Oracle as oci
print("cx_Oracle 버전 : ", oci.version)


# destination - 경로 설정
destination = cx_Oracle.makedsn(‘서버ip,’, 포트번호, ‘sid’)
# 연결
conn = oci.connect(‘ID’, ‘PW’, destination)

# DB와 연결이 잘 되었는지 확인 -> 버전이 출력되면 연결이 잘 된것
print(conn.version)


# SQL쿼리 실행
cursor = conn.cursor()
cursor.execute('select * from departments')
data = cursor.fetchall()

data