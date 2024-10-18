import os
import smtplib


LOGIN = os.environ["LOGIN"]
PASSWORD = os.environ["PASSWORD"]
website = 'https://dvmn.org/referrals/rROk3zOStDIkOgD2CNhYGKMTfWV69TBMC91RzZfo/'
friend_name = 'Petya'
subject = "Приглашение!"
my_name = 'Timur'
mail = "devmanorg@yandex.ru"
mail1 = "t.suleymanoff@yandex.ru"
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(LOGIN , PASSWORD)
letter = """From: {0}
To: {1}
Subject: Приглашение! 
Content-Type: text/plain; charset="UTF-8";
\n\nПривет, {2} {4} приглашает тебя на сайт {3}!
{3} — это  новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 
Как будет проходить ваше обучение на {3}? 
→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 
Регистрируйся → {3}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл""".format(mail,mail1,friend_name,website,my_name)
letter = letter.encode("UTF-8")
server.sendmail(mail, mail1, letter)
server.quit()