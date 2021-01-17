from flask import render_template as render, flash, send_from_directory
from app import create_app
from app.migrate import init_db
from app.services import list_public_ideas

app = create_app()

@app.errorhandler(404)
def not_found(error):
    """ Método para error 404. """
    return render('errors/error404.html', error=error)

@app.errorhandler(500)
def internal_server_error(error):
    """ Método para error 500. """
    return render('errors/error500.html')

@app.route('/')
def index():
    context = {
        'public_ideas': list_public_ideas()
    }
    return render('index.html', **context)

@app.template_filter()
def visibility_public_or_private(visibility):
    """ Filtro de visibilidad de ideas. """
    return 'Pública'  if visibility == True else 'Privada'

@app.route('/profile/picture/<path:filename>')
def picture_profile(filename):
    base_url = 'uploads/profile_pictures'
    if filename == 'none':
        filename = 'user_default.JPG'
        
    return send_from_directory(base_url, filename)

@app.route('/database')
def database():
    init_db()
    return "base de datos creada correctamente. """