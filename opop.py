import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=BNATDBS120;'
                      'Database=portal;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute("SELECT * FROM dbo.Programs where programName like '%Saigon%'")

for i in cursor:
    print(i[0])