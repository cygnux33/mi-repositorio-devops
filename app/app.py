@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "servidor": "AWS EC2 - Jenkins Node",
        "developer": "Ricardo Isai",
        "version": "2.0.5",
        "mensaje": "Despliegue automático desde la rama mejora-python al 100",
        "ubicacion": "Puebla, MX"
    })