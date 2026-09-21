@app.route('/v2/etudiants/<int:id>', methods=['GET'])
def getEtudiant(id):
    req = f"SELECT * FROM etudiant WHERE idetudiant = {id}"
    try:
        cursor.execute(req)
        print(req)
        row = cursor.fetchone()
        etudiant = {
            "idetudiant": row[0],
            "nom": row[1],
            "prenom": row[2],
            "email": row[3],
            "telephone": row[4]
        }
        return jsonify(etudiant), 200
    except TypeError:
        return jsonify({'erreur': 'id invalide'}), 404