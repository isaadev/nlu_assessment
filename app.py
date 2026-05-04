from flask import Flask, jsonify, abort, request
import sqlite3
from datetime import datetime

app = Flask(__name__)


@app.route('/property/<address>/', methods=['GET'])
def get_property(address):
    cn = sqlite3.connect('test.db')
    cursor = cn.cursor()

    address = address.strip().upper()
    violations = cursor.execute("SELECT * FROM violations WHERE address = ? ORDER BY violation_date DESC", (address,)).fetchall()
    
    v_list = []
    for v in violations:
        v_list.append({
            "DATE": v[2],
            "CODE": v[6],
            "STATUS": v[3],
            "DESCRIPTION": v[4],
            "INSPECTOR_COMMENTS": v[5]
            })
        
    scofflaw = cursor.execute("SELECT * FROM scofflaws WHERE address = ?", (address,)).fetchone()

    cn.close()

    if not violations and not scofflaw:
        abort(404)

    return jsonify({
        "TOTAL_VIOLATION_COUNT": len(v_list),
        "LAST_VIOLATION_DATE": v_list[0]["DATE"] if v_list else None,
        "VIOLATIONS": v_list,
        "SCOFFLAW": scofflaw is not None

        })



if __name__ == '__main__':
    app.run(debug=True)
