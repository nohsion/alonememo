from flask import Flask

# flask Web Server 생성하기
app = Flask(__name__)

# app.py 파일을 직접 실행시킬 때 동작시킴
if __name__ == '__main__':
    app.run(
        '0.0.0.0',  # 모든 IP 에서 오는 요청을 허용
        7000,  # flask Web Server 는 7000번 포트 사용
        debug=True,  # Error 발생 시 에러 로그 보여줌
    )
