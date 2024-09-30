from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mateorosero30@localhost/dbinventario'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mateorosero30'
db = SQLAlchemy(app)

class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    fecha_vencimiento = db.Column(db.Date, nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            nuevo_producto = Producto(
                nombre=request.form['nombre'],
                descripcion=request.form['descripcion'],
                fecha_vencimiento=datetime.strptime(request.form['fecha_vencimiento'], '%Y-%m-%d')
            )
            db.session.add(nuevo_producto)
            db.session.commit()
            flash('Producto agregado con éxito', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error al agregar producto: {str(e)}', 'error')
        return redirect(url_for('index'))
    
    productos = Producto.query.all()
    return render_template('index.html', productos=productos)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):
    producto = Producto.query.get_or_404(id)
    if request.method == 'POST':
        try:
            producto.nombre = request.form['nombre']
            producto.descripcion = request.form['descripcion']
            producto.fecha_vencimiento = datetime.strptime(request.form['fecha_vencimiento'], '%Y-%m-%d')
            db.session.commit()
            flash('Producto actualizado con éxito', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al actualizar producto: {str(e)}', 'error')
    return render_template('editar_producto.html', producto=producto)

@app.route('/borrar/<int:id>')
def borrar_producto(id):
    producto = Producto.query.get_or_404(id)
    try:
        db.session.delete(producto)
        db.session.commit()
        flash('Producto eliminado con éxito', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar producto: {str(e)}', 'error')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)