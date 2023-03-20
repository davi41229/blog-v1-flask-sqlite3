from app import app 
from flask import render_template, request, url_for, redirect


from app import app, db
from app.models.models import Blogger



# rota inicial
@app.route('/') #VULNERABILIDADE XSS CORRIGIDA, COM A CHAMADA DE TEMPLATE
def index():
    posts = Blogger.query.all()
    return render_template("inicial.html", posts=posts)


# rota para criar novo post
@app.route('/post/add', methods=["POST"])
def add_post():
    try:        
        form = request.form
        post = Blogger(title=form['title'], content=form['content'], author=form['author'])
        db.session.add(post)
        db.session.commit()
    except Exception as error:
        print("Error", error)
        
    return redirect(url_for("index"))

# rota para deletar post
@app.route('/post/<id>/del')
def delete_post(id):
    try:        
        post = Blogger.query.get(id)
        db.session.delete(post)
        db.session.commit()
    except Exception as error:
        print("Error", error)
        
    return redirect(url_for("index"))
    
# rota para editar post
@app.route('/post/<id>/edit', methods=["POST", "GET"])
def edit_post(id):
    if request.method == "POST":
        try:
            post = Blogger.query.get(id)        
            form = request.form
            post.title = form["title"]
            post.content = form["content"]
            post.author = form["author"]
            db.session.commit()
        except Exception as error:
            print("Error", error)
            
        return redirect(url_for("index")) 
    else:
        try:
            post = Blogger.query.get(id)        
            return render_template("editar.html", post=post) 
        except Exception as error:
            print("Error", error)
            
    return redirect(url_for("index"))

