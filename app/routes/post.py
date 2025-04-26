from flask import Blueprint, render_template, request, redirect, url_for, session, flash
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

    user_id = session.get('user_id')

    if not user_id:
        return redirect(url_for('auth.login'))

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT id FROM quarters WHERE user_id = ?', (user_id,))
    existing_quarter = c.fetchone()
    conn.close()

    if request.method == 'POST' and not existing_quarter:
        rank = request.form.get('rank')
        name = request.form.get('name')
        contact = request.form.get('contact')
        building = request.form.get('building')
        floor = request.form.get('floor')
        section = request.form.get('section')
        notice_period = request.form.get('notice_period')

        building_full = f"{building} - Floor {floor} - Section {section}"

        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute(''' 
            INSERT INTO quarters (user_id, rank, name, contact, building, notice_period)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (user_id, rank, name, contact, building_full, notice_period))
        conn.commit()
        conn.close()

        flash('Quarter posted successfully!', 'success')
        return redirect(url_for('post.post_quarter'))

    return render_template(
        'post_quarter.html',
        ranks=ranks,
        buildings=buildings,
        floors=floors,
        sections=sections,
        notice_periods=notice_periods,
        already_posted=bool(existing_quarter)
    )


@post_bp.route('/delete', methods=['POST'])
@login_required
def delete_quarter():
    user_id = session.get('user_id')

    if not user_id:
        return redirect(url_for('auth.login'))

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('DELETE FROM quarters WHERE user_id = ?', (user_id,))
    conn.commit()
    conn.close()

    flash('Your quarter has been deleted successfully!', 'success')
    return redirect(url_for('post.post_quarter'))
