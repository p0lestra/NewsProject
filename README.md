# 1. Создать двух пользователей
```
from news.models import User

user1 = User.objects.create_user('Alex Kolom')
user2 = User.objects.create_user('Bob Calhoun')
```

# 2. Создать два объекта модели Author, связанные с пользователями.
```
from news.models import Author

Author.objects.create(author = user1)
Author.objects.create(author = user2)
```

# 3. Добавить 4 категории в модель Category.
```
from news.models import Category
Category.objects.create(article_category = 'sports') 
Category.objects.create(article_category = 'weather')
Category.objects.create(article_category = 'exploring')
Category.objects.create(article_category = 'culture')

# 4 Добавить 2 статьи и 1 новость.
from news.models import Post
author = Author.objects.get(id=1)

Post.objects.create(
post_author = author, 
category = 'A', 
title = 'Sun Explosion', 
content = 'Long text'
)

Post.objects.create(
post_author = author, 
category = 'A', 
title = 'Story Tale', 
content = 'Not very long story'
)

Post.objects.create(
post_author = author, 
category = 'N', 
title = 'Some news', 
content = 'CocaCola closing'
)
```
# 5. Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
1 cтатье присваиваем категорию 1 - sports
```
Post.objects.get(id=1).post_category.add(Category.objects.get(id=1))
```
2 статье присваеваем категорию 3 - exploring
```
Post.objects.get(id=1).post_category.add(Category.objects.get(id=3))
```

# 6. Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
```
from news.models import *
Comment.objects.create(
                      comment_post=Post.objects.get(id=1),
                      comment_user=Author.objects.get(id=1).author, 
                      feedback_text = 'interesting'
                      )

Comment.objects.create(
                      comment_post=Post.objects.get(id=2), 
                      comment_user = Author.objects.get(id=1).author,
                      feedback_text = 'not bad'
                      )

Comment.objects.create(
                      comment_post = Post.objects.get(id=3), 
                      comment_user = Author.objects.get(id=2).author, feedback_text = "very cool"
                      )

Comment.objects.create(
                      comment_post=Post.objects.get(id=1), 
                      comment_user = Author.objects.get(id=2).author, feedback_text = 'niceee'
                      )
```                      
# 7. Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
```
Comment.objects.get(id=1).like()
Post.objects.get(id=1).dislike()
Post.objects.get(id=3).like()
```

# 8. Обновить рейтинги пользователей.
```
u1 = Author.objects.get(id=1)
u1.update_rating()
u1.user_rate
```

# 9. Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
```
>>> s = Author.objects.order_by('user_rate')
>>> for i in s:
...     i.user_rate
...     i.author.username
```

# 10. Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
```
>>> p = Post.objects.order_by('-post_rate')
for i in p[:1]:
...     i.date_created
...     i.post_author.author
...     i.post_rate
...     i.title
...     i.preview()
```
# 11. Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
```
>>> Post.objects.all().order_by('-post_rate')[0].comment_set.values(
'comment_date_created', 
'comment_user', 
'comment_rate', 'feedback_text'
)
```
