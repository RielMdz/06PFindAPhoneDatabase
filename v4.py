import sqlite3,csv

try:
    conn = sqlite3.connect('phones.db', uri=True)
    cur = conn.cursor()
# gawa ng table tangalin if wala
    cur.execute("""CREATE TABLE phoneTable(
        id TEXT,
        battery_power INTEGER,
        blue INTEGER,
        clock_speed INTEGER,
        dual_sim INTEGER,
        fc INTEGER,
        four_g INTEGER,
        int_memory INTEGER,
        m_dep INTEGER,
        mobile_wt INTEGER,
        n_cores INTEGER,
        pc INTEGER,
        px_height INTEGER,
        px_width INTEGER,
        ram INTEGER,
        sc_h INTEGER,
        sc_w INTEGER,
        talk_time INTEGER,
        three_g INTEGER,
        touch_screen INTEGER,
        wifi INTEGER,
        primary key(id)
        )""")

    #pag write sa table
    with open ('test.csv','r') as file:
        no_records = 0
        for row in file:
            cur.execute("INSERT INTO phoneTable VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",row.split(","))
            no_records += 1
    print ("complete")     
    conn.commit()
    conn.close()
#pag meron nang table  
except sqlite3.OperationalError as err:
    conn = sqlite3.connect('phones.db')
    cur = conn.cursor()
    print ("good")