import subprocess

# Démarrer le serveur Flask
subprocess.Popen(['python', 'app.py'])

# Ouvrir le navigateur sur l'adresse du serveur Flask
subprocess.Popen(['start', 'http://127.0.0.1:5000'])
