from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite///test.db'
db=SQLAalchemy(app)

class Todo(db.Model):
    id= db.Collumn(db.Integer, primary_key=True)
    content = db.Collumn(db.String(200), nullable=False)
    completed = db.Collum(db.Integer, default=0)
    date_created=db.Collum(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.comit()
            return redirect('/')
        except:
            return 'Tem problema'
        
    else:
        tasks=Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
       db.session.delete(task_to_delete)
        db.session.comit()
        return redirect('/')
    except:
            return 'Tem problema'
    
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
            

if __name__ == "__main__":
    app.run(debug=True)
