지원자 백준형입니다<br /><br />
**데모영상링크입니다 : https://youtu.be/kz5zGXfpRPo** <br /> <br />
**실행 방법**
* git clone https://github.com/backjune/wanted-pre-onboarding-backend.git <br />
* cd wanted-pre-onboarding-backend <br />
* pip install -r requirements.txt <br />
* DB 생성
* project/settings.py 열어서 위에서 만든 DB에 맞게 DATABASES값을 수정합니다. <br />
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'xxx',  # DB이름 입력
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

* python manage.py makemigrations board <br />
* python manage.py migrate board <br />
* python manage.py runserver <br />

* 아래와 같이 원하는 엔드포인트 호출합니다.
```
curl -d "email=test@naver.com&password=12345678" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://127.0.0.1:8000/user/signup
```
**API 명세**

**회원가입**
* **URL**
  /user/signup  

* **Method:**
  `POST`
  
* **Data Params**
  email, password

* **Success Response:**
  * **Code:** 201 <br />

* **Error Response:**

  * **Code:** 400 BAD Request <br />
    **Contents:** `{email: "Email must contain the @ symbol."}`<br />
    `{email: "user with this email already exists."}`<br />
    `{password: "Password must be at least 8 characters long."}`<br />
    `{email: "This field may not be blank."}`<br />
 `{password: "This field may not be blank."}`<br />
    

**로그인**
* **URL**
  /user/signin  

* **Method:**
  `POST`
  
* **Data Params**
  email, password

* **Success Response:**
  * **Code:** 200 <br />
    **Contents:** `{token: jwt토큰값}`
* **Error Response:**
  * **Code:** 400 BAD Request <br />
**Contents:** `{email: "Email must contain the @ symbol."}`<br />
    `{email: "user with this email already exists."}`<br />
    `{password: "Password must be at least 8 characters long."}`<br />
    `{email: "This field may not be blank."}`<br />
 `{password: "This field may not be blank."}`<br />

**게시글 생성**
* **URL**
  /board/create  

* **Method:**
  `POST`
  
* **Data Params**
  user_id, content

* **Success Response:**
  * **Code:** 201 <br />

* **Error Response:**
  * **Code:** 400 BAD Request <br />
**Contents:** `{error: "No user found."}`<br />
    `{error: "Please enter the content."}`<br />

**게시글 목록 조회**
* **URL**
  /board/  

* **Method:**
  `GET`
  
* **URL Params**
  /?page={페이지번호} `ex) /board/?page=2`

* **Success Response:**
  * **Code:** 200 <br />
    * **Content:**
  ```{
    "count": 7,  #총 게시글 수
    "next": "http://127.0.0.1:8000/board/?page=2", #다음 페이지 url
    "previous": null, #이전 페이지 url
    "results": [
        {
            "id": 2, #게시글 id
            "owner": "test@", #작성자 이메일
            "content": "test2@", #게시글
            "created": "2023-08-15T02:35:09.157451Z" #게시글 생성날짜
        },
          {
            "id": 3,
            "owner": "test2@",
            "content": "x",
            "created": "2023-08-15T02:35:22.433230Z"
        },
  ]
* **Error Response:**
  * **Code:** 404 Not Found <br />
**Contents:** `{detail: "Invalid page"}`<br />

**게시글 조회**
* **URL**
  /board/  

* **Method:**
  `GET`
  
* **URL Params**
  /{게시글id} `ex) /board/1`

* **Success Response:**
  * **Code:** 200 <br />
    * **Content:**
  ```
  {
            "id": 2, #게시글 id
            "owner": "test@", #작성자 이메일
            "content": "test2@", #게시글
            "created": "2023-08-15T02:35:09.157451Z" #게시글 생성날짜
  }
* **Error Response:**
  * **Code:** 404 Not Found <br />
**Contents:** `{detail: "Not found."}`<br />

**게시글 수정**
* **URL**
  /board/  

* **Method:**
  `PUT`
* **Data Params**
  user_id, content
* **URL Params**
  /{게시글id} `ex) /board/1`

* **Success Response:**
  * **Code:** 200 <br />
    * **Content:**
  ```
  {
            "id": 2, #게시글 id
            "owner": "test@", #작성자 이메일
            "content": "changed", #게시글
            "created": "2023-08-15T02:35:09.157451Z" #게시글 생성날짜
  }
* **Error Response:**
  * **Code:** 400 Bad Request <br />
**Contents:** `{user_id: "This field may not be blank."}`<br />
 `{content: "This field is required."}`<br />
`{error: "Only the author can make modifications."}`<br />
`{detail: "Not found."}`<br />


**게시글 삭제**
* **URL**
  /board/  

* **Method:**
  `DELETE`
* **Data Params**
  user_id
* **URL Params**
  /{게시글id} `ex) /board/1`

* **Success Response:**
  * **Code:** 204 <br />

* **Error Response:**
  * **Code:** 400 Bad Request <br />
**Contents:** `{user_id: "This field may not be blank."}`<br />
`{detail: "Not found."}`<br />
`{error: "Only the author can delete."}`<br />


**데이터베이스 테이블 구조** 
* DB는 user, board 테이블 두개로 구성되며,
* user 테이블은 id(pk), email, password 로 구성되고
* board 테이블은 id(pk), content(게시글), created(게시글 만들어진 시간), owner_id(fk, 작성자 id) 로 구성됩니다.


