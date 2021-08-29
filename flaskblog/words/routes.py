from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post,Word,Example
import  csv
from flaskblog.words.forms import SearchWordForm
from googletrans import Translator

words = Blueprint('words', __name__,url_prefix = '/words')

@words.route("/add", methods=['GET', 'POST'])
def add_word_csv_to_db():
    with open('./flaskblog/words/words.csv', 'r') as file:
        reader = csv.reader(file)
        for index,row in enumerate(reader):
            if index == 0 :
                continue
            word =  Word(word = row[0].lower(),translation=row[1])
            for example in row[2:] :
                if example :
                    my_example = Example(example=example,word = word)
                    word.examples.append(my_example)
            

            db.session.add(word)
            print(index)
            
        db.session.commit()

    return 'this code works '



@words.route("/", methods=['GET', 'POST'])
def index():
    form = SearchWordForm()
    query_word = ''
    g_trans = ''
    if form.validate_on_submit():
        translator = Translator()
        print(form.word)
        print(form.word.data)
        word = form.word.data
        query_word = Word.query.filter(Word.word.like(f'%{word.lower()}%')).all()
        print(query_word)
       
        print('i done it')
        try:
            t=translator.translate(word, dest='fa')
            g_trans = {'text':t.text}

        except expression as identifier:
            print('error occour')
            

   
    return render_template('words/words.html'
                    ,form=form
                    ,res_words=query_word
                    ,g_trans = g_trans
                    )    

# TODO : change with ajax
def word_ajax ():
    pass



# @words.route("/post/new", methods=['GET', 'POST'])
# @login_required
# def new_post():
#     form = PostForm()
#     if form.validate_on_submit():
#         post = Post(title=form.title.data, content=form.content.data, author=current_user)
#         db.session.add(post)
#         db.session.commit()
#         flash('Your post has been created!', 'success')
#         return redirect(url_for('main.home'))
#     return render_template('create_post.html', title='New Post',
#                            form=form, legend='New Post')


# @words.route("/post/<int:post_id>")
# def post(post_id):
#     post = Post.query.get_or_404(post_id)
#     return render_template('post.html', title=post.title, post=post)


# @words.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
# @login_required
# def update_post(post_id):
#     post = Post.query.get_or_404(post_id)
#     if post.author != current_user:
#         abort(403)
#     form = PostForm()
#     if form.validate_on_submit():
#         post.title = form.title.data
#         post.content = form.content.data
#         db.session.commit()
#         flash('Your post has been updated!', 'success')
#         return redirect(url_for('posts.post', post_id=post.id))
#     elif request.method == 'GET':
#         form.title.data = post.title
#         form.content.data = post.content
#     return render_template('create_post.html', title='Update Post',
#                            form=form, legend='Update Post')


# @words.route("/post/<int:post_id>/delete", methods=['POST'])
# @login_required
# def delete_post(post_id):
#     post = Post.query.get_or_404(post_id)
#     if post.author != current_user:
#         abort(403)
#     db.session.delete(post)
#     db.session.commit()
#     flash('Your post has been deleted!', 'success')
#     return redirect(url_for('main.home'))
