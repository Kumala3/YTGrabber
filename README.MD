This template is used for development Telegram bots on [`aiogram v3.0+`](https://github.com/aiogram/aiogram/tree/dev-3.x) + MiniApp on [`React`](https://github.com/facebook/react) & [`TypeScript`](https://github.com/microsoft/typescript)

<!-- ## SQLAlchemy + Alembic
В коді є приклади таблички User з використанням SQLAlchemy 2.0, та скрипти для алембіку (ініціалізація алембік, створення та застосування міграцій).

Але, якщо ви з цими інструментами ніколи не працювали, то зверніться до документації і дізнайтесь про ці інструменти. 
Також, в мене є англомовний [курс по цим інструментам на Udemy](https://www.udemy.com/course/sqlalchemy-alembic-bootcamp/?referralCode=E9099C5B5109EB747126). -->

## To start using it:
1. Register the account on ngrok(if you haven't yet): [Sign Up Ngrok](https://dashboard.ngrok.com/signup)
2. Create `ngrok.yml` by data from ngrok-example.yml and fill out required data: `authtoken` and `domain`.
3. Create `.env` by data from `.end.dist` and fill out required data.
4. **Run with Docker:**
    1. Download and install `Docker desktop` (if you haven't yet): [Download Docker Desktop](https://docs.docker.com/get-docker/).
    2. Run project with next command in terminal:  
        `docker-compose up --build`
