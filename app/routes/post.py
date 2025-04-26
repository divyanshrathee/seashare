from flask import Blueprint, render_template, request, redirect, url_for, session
import sqlite3
from app.utils.security import login_required

post_bp = Blueprint('post', __name__)
DB_FILE = 'database.db'

@post_bp.route('/post', methods=['GET', 'POST'])
@login_required
def post_quarter():
    ranks = ["Leading Seaman", "Petty Officer", "Chief Petty Officer", "Master Chief Petty Officer (MCPO)"]
    buildings = [f"R{i}" for i in range(1, 31)]
    floors = [str(i) for i in range(1, 15)]
    sections = ['A', 'B', 'C', 'D']
    notice_periods = ["1 month", "2 months", "3 months"]

    user_id = session['user_id']

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT * FROM quarters WHERE user_id = ?', (user_id,))
    existing_quarter = c.fetchone()
    conn.close()

    if existing_quarter:
        return render_template('post_quarter.html', already_posted=True)

    if request.method == 'POST':
        rank = request.form['rank']
        name = request.form['name']
        contact = request.form['contact']
        building_name = request.form['building']
        floor = request.form['floor']
        section = request.form['section']
        notice_period = request.form['notice_period']

        building_full = f"{building_name} - Floor {floor} - Section {section}"

        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute('INSERT INTO quarters (user_id, rank, name, contact, building, notice_period) VALUES (?, ?, ?, ?, ?, ?)',
                  (user_id, rank, name, contact, building_full, notice_period))
        conn.commit()
        conn.close()

        return redirect(url_for('post.post_quarter'))

    return render_template('post_quarter.html', ranks=ranks, buildings=buildings, floors=floors, sections=sections, notice_periods=notice_periods, already_posted=False)
