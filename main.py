import os

from flask import Flask, render_template
from dotenv import load_dotenv
import os

app = Flask(__name__,template_folder='templates',static_folder='static',)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

if os.getenv("FLASK_ENV") == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

@app.route("/")
def index():
    return render_template('pages/index.html', title="Calderas Inecolma SAS - Soluciones innovadoras en generación de vapor")

@app.route("/privacy")
def privacy():
    return render_template('pages/privacy.html', title="Calderas Inecolma SAS - Política de tratamiento de datos")

@app.route("/ecoline")
def ecoline():
    return render_template('pages/ecoline.html', title="Calderas Inecolma SAS - Calderas de alta eficiencia")

@app.route("/heavyline")
def heavyline():
    return render_template('pages/heavyline.html', title="Calderas Inecolma SAS - Calderas de uso industrial")

@app.route("/hybridline")
def hybridline():
    return render_template('pages/hybridline.html', title="Calderas Inecolma SAS - Calderas de gran rendimiento")

@app.route("/boilerlogic")
def boilerlogic():
    return render_template('pages/boilerlogic.html', title="Calderas Inecolma SAS - Sistema integrado IoT")

@app.route("/auxiliary")
def auxiliary():
    return render_template('pages/auxiliary.html', title="Calderas Inecolma SAS - Equipos complementarios")

@app.route("/parts")
def parts():
    return render_template('pages/parts.html', title="Calderas Inecolma SAS - Repuestos y partes")

@app.route("/maintenance")
def maintenance():
    return render_template('pages/maintenance.html', title="Calderas Inecolma SAS - Servicios de mantenimiento")

@app.route("/automation")
def automation():
    return render_template('pages/automation.html', title="Calderas Inecolma SAS - Automatización")

@app.route("/measuring")
def measuring():
    return render_template('pages/measuring.html', title="Calderas Inecolma SAS - Mediciones especializadas")

@app.route("/about")
def about():
    return render_template('pages/about.html', title="Calderas Inecolma SAS - Acerca de nosotros")

@app.route("/contact")
def contact():
    return render_template('pages/contact.html', title="Calderas Inecolma SAS - Contáctanos")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html'), 404  # Create a 404.html template

@app.errorhandler(500)
def internal_server_error(e):
    return "An error occurred", 500

def main():
    app.run(port=int(os.environ.get('PORT', 8000)))

if __name__ == "__main__":
    main()