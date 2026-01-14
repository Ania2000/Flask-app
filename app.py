from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

import sqlite3

def get_db_connection():
    conn = sqlite3.connect("movies.db")
    return conn

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        movies_to_remove_ids = request.form.getlist('movieToRemove')

        if movies_to_remove_ids:
            conn = get_db_connection()
            cur = conn.cursor()

            placeholders = ",".join(["?"] * len(movies_to_remove_ids))
            query = f"DELETE FROM movies WHERE id IN ({placeholders})"
            cur.execute(query, movies_to_remove_ids)

            conn.commit()
            conn.close()

        return redirect(url_for('home'))


    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, title, year, actors FROM movies")
    movies = cur.fetchall()

    conn.close()
    return render_template('home.html', movies=movies)


@app.route('/addMovie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        title = request.form.get('title')
        year = request.form.get('year')
        actors = request.form.get('actors')

        conn = get_db_connection()
        cursor = conn.cursor()

        query = "INSERT INTO movies (title, year, actors) VALUES (?, ?, ?)"
        cursor.execute(query, (title, year, actors))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))


    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)