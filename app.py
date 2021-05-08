from flask import Flask, render_template, jsonify, request

from pymongo import MongoClient

# flask Web Server 생성하기
app = Flask(__name__)

# mongoDB 추가
client = MongoClient('localhost', 27017)
db = client.get_database('sparta')

# API 추가
@app.route('/', methods=['GET'])  # 데코레이터 문법 @
def index():
    return render_template('index.html', test='테스트')


# 아티클 추가 API
@app.route('/memo', methods=['POST'])
def save_memo():
    form = request.form
    url_receive = form['url_give']
    comment_receive = form['comment_give']

    print(url_receive, comment_receive)
    document = {
        'url': url_receive,
        'comment': comment_receive,
    }
    db.articles.insert_one(document)

    return jsonify(
        {'result': 'success'}
    )


# app.py 파일을 직접 실행시킬 때 동작시킴. 이 코드가 가장 아랫부분이어야 함!
if __name__ == '__main__':
    app.run(
        '0.0.0.0',  # 모든 IP 에서 오는 요청을 허용
        7000,  # flask Web Server 는 7000번 포트 사용
        debug=True,  # Error 발생 시 에러 로그 보여줌
    )
