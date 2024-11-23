user1 = User.objects.create_user(username='user1', email='user1@example.com', password='1')
user2 = User.objects.create_user(username='user2', email='user2@example.com', password='2')

author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)

category1 = Category.objects.create(name='Sports')
category2 = Category.objects.create(name='Politics')
category3 = Category.objects.create(name='Education')
category4 = Category.objects.create(name='Technology')

post1 = Post.objects.create(author=author1, post_type=Post.ARTICLE, title='Article 1', text='This is the text of Article 1.')
post2 = Post.objects.create(author=author2, post_type=Post.ARTICLE, title='Article 2', text='This is the text of Article 2.')
post3 = Post.objects.create(author=author1, post_type=Post.NEWS, title='News 1', text='This is the text of News 1.')

post1.categories.add(category1, category2)
post2.categories.add(category3, category4)
post3.categories.add(category2)

comment1 = Comment.objects.create(post=post1, author=user1, text='good!')
comment2 = Comment.objects.create(post=post1, author=user2, text='good.')
comment3 = Comment.objects.create(post=post2, author=user1, text='good.')
comment4 = Comment.objects.create(post=post3, author=user2, text='Nice.')

post1.like()
post2.dislike()
comment1.like()
comment2.dislike()

author1.update_rating()
author2.update_rating()

best_author = Author.objects.order_by('-rating').first()
print(f"Best author: {best_author.user.username}, Rating: {best_author.rating}")

best_post = Post.objects.order_by('-rating').first()
print(f"Best post: \nDate: {best_post.created_at.strftime('%Y-%m-%d %H:%M:%S')}, \nAuthor: {best_post.author.user.username}, \nRating: {best_post.rating}, \nTitle: {best_post.title}, \nPreview: {best_post.preview()}")

for comment in best_post.comments.all():
    print(f"Comment: \nDate: {comment.created_at.strftime('%Y-%m-%d %H:%M:%S')}, \nAuthor: {comment.author.username}, \nRating: {comment.rating}, \nText: {comment.text}")
