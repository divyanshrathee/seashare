from flask import Blueprint, render_template, request
import sqlite3
from app.utils.security import login_required

search_bp = Blueprint('search', __name__)
DB_FILE = 'database.db'

@search_bp.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    buildings = [f"R{i}" for i in range(1, 31)]
    return render_template('search.html', buildings=buildings)

@search_bp.route('/search/rank', methods=['POST'])
@login_required
def search_by_rank():
    rank = request.form['rank']
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT * FROM quarters WHERE rank = ?', (rank,))
    quarters = c.fetchall()
    conn.close()
    return render_template('view_results.html', quarters=quarters)

@search_bp.route('/search/building', methods=['POST'])
@login_required
def search_by_building():
    building = request.form['building']
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT * FROM quarters WHERE building LIKE ?', (f"{building}%",))
    quarters = c.fetchall()
    conn.close()
    return render_template('view_results.html', quarters=quarters)
