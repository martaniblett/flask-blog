# import render_template function from the flask module
from flask import render_template
# import the app object from the ./application/__init__.py
from application import app
from application.models import Posts

#forms:
from flask import render_template, redirect, url_for
from application import app, db
from application.models import Posts
from application.forms import PostForm


# define routes for / & /home, this function will be called when these are accessed
blogData = [
    {  
        "name": {"first":"John", "last":"Doe"},
        "title":"First Post",
        "content":"This is some blog data for Flask lectures"
    },
    {   
        "name": {"first":"Jane", "last":"Doe"},
        "title":"Second Post",
        "content":"This is even more blog data for Flask lectures"
    }
]
@app.route('/')
@app.route('/home')
def home():
 postData = Posts.query.all()
 return render_template('home.html', title='Home Page', post=postData)

@app.route('/about')
def about():
 return render_template('about.html', title='About Page')

@app.route('/login')
def login():
 return render_template('login.html', title='Login Page')

@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        postData = Posts(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            title=form.title.data,
            content=form.content.data
        )

        db.session.add(postData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('post.html', title='Post', form=form)