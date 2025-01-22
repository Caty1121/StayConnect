import sqlite3

conn = sqlite3.connect('stayconnect.db')
cursor = conn.cursor()

cursor.execute('''
    INSERT INTO users (username, email, password)
    VALUES ('testuser', 'test@example.com', 'password123')
''')

cursor.execute('SELECT * FROM users')
users = cursor.fetchall()
for user in users:
    print(user)

conn.commit()
conn.close()
