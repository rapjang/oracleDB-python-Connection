# oracleDB-python-Connection
connect oracleDB and python programming

# related link / 관련링크

# 1. install and setting / 설치 및 세팅
https://blog.naver.com/rapjang/222960537481

# 2. source code / 소스코드
https://blog.naver.com/rapjang/222960547589


# DB : Oracle Database 11g Express Edition
# python version : 3.8.8 (anaconda3)


# basic SQL relating database

# 계정 접속
conn 사용자명/비번;
connect 사용자명/비번;

# HR 계정 잠금확인
select username, account_status, lock_date 
from DBA_USERS 
where username='HR'

# hr 계정 잠금해제
alter user hr account unlock

# 패스워드 재설정
alter user hr identified by hr

# 계정생성
create user <유저명> identified by <비밀번호>;

# 생성된 계정에 권한부여
grant <권한>,...,<권한> to <유저명>;
ex) grant connect to hr;

# 현재 접속 사용자 계정 확인
show user

# 종료 
exit