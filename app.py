from flask import Flask, jsonify, abort, request
import os
import sqlite3
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "API is running!"})

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

@app.route('/property/<address>/comments/', methods=['POST'])
def add_comment(address):
    cn = sqlite3.connect('test.db')
    cursor = cn.cursor()

    address = address.strip().upper()
    data = request.get_json()
    
    author = data.get("author", "").strip()
    comment = data.get("comment", "").strip()
    curr_time = datetime.now().isoformat()

    cursor.execute("""
                   INSERT INTO comments (address, author, comment, datetime) 
                   VALUES (?, ?, ?, ?)
                   """, (address, author, comment, curr_time))
    cn.commit()
    cn.close()

    return jsonify({"message": "Comment added"}), 201

@app.route('/property/scofflaws/violations', methods=['GET'])
def get_recent_violations():
    cn = sqlite3.connect('test.db')
    cursor = cn.cursor()

    since = request.args.get('since')

    # not in spec, but for good measure -> handles case where since is missing or empty string
    if not since:
        cn.close()
        return jsonify({"error": "Missing 'since' query parameter"}), 400

    try:
        since_date = datetime.strptime(since, "%Y-%m-%d").date()
        recent_violations = cursor.execute("""
            SELECT DISTINCT v.address
            FROM violations v
            JOIN scofflaws s ON v.address = s.address
            WHERE v.violation_date >= ?
            ORDER BY v.violation_date DESC
        """, (since_date.isoformat(),)).fetchall()

        cn.close()
    except (ValueError, TypeError):
        cn.close()
        abort(400, description="Invalid date format. Use YYYY-MM-DD.")

    addresses = [v[0] for v in recent_violations]

    return jsonify(addresses)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5001)), debug=True)
