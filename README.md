지원자 백준형입니다
cd wanted-pre-onboarding-backend
pip install -r requirements.txt

project/settings.py 열어서 아래와 같이 DATABASES 값들을 로컬 DB에맞게 수정합니다.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'xxx', 
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

python manage.py makemigrations board
python manage.py migrate board
python manage.py runserver

아래와 같이 원하는 엔드포인트 호출합니다.
ex) http http://127.0.0.1:8000/board/

DB 테이블은 user, board 두개이며
user 테이블은 id(pk), email, password 로 구성되고
board 테이블은 id(pk), content(게시글), created(게시글 만들어진 시간),owner_id(fk, 작성자 id) 
로 구성됩니다.

데모영상링크입니다 : 

**회원가입**
* **URL**
  /signup

* **Method:**

  `POST`
  
*  **URL Params**
      None

* **Data Params**
  email, password

* **Success Response:**

  * **Code:** 201 <br />
    **Content:** `None`
 
* **Error Response:**

  * **Code:** 400 NOT FOUND <br />
    **Content:** `{ error : "User doesn't exist" }`

  OR

  * **Code:** 400 UNAUTHORIZED <br />
    **Content:** `{ error : "You are unauthorized to make this request." }`

