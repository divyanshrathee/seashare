from flask import Blueprint, redirect, url_for, session, flash
import sqlite3
from app.utils.security import login_required

post_bp = Blueprint('post', __name__)
DB_FILE = 'database.db'

@post_bp.route('/delete_quarter', methods=['POST'])
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
