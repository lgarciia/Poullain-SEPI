from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Assurez-vous que le dossier de téléchargement existe
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Vérifiez si le fichier fait partie de la requête
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        # Si l'utilisateur ne sélectionne pas de fichier, le navigateur envoie un champ de fichier vide sans nom de fichier
        if file.filename == '':
            return 'No selected file'
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            # Lire le fichier Excel
            df = pd.read_excel(file_path)
            return render_template('index.html', tables=[df.to_html(classes='data')], titles=df.columns.values)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
