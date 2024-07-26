import sqlite3

def search_database(search_string):
    # Connect to the SQLite database
    conn = sqlite3.connect('assignment.db')
    cursor = conn.cursor()

    # Perform a case-insensitive search
    query = "SELECT name, marks FROM students WHERE name LIKE ? COLLATE NOCASE"
    cursor.execute(query, ('%' + search_string + '%',))
    rows = cursor.fetchall()

    # Check if any rows were returned
    if rows:
        total_marks = 0
        print("Results found:")
        for row in rows:
            name, marks = row
            total_marks += marks
            print(f"Name: {name}, Marks: {marks}")
        
        average_marks = total_marks / len(rows)
        print(f"Total Marks: {total_marks}")
        print(f"Average Marks: {average_marks:.2f}")
    else:
        print("No results found.")

    # Close the connection to the database
    conn.close()

def main():
    while True:
        search_string = input("Enter a search string (or type 'exit' to quit): ")
        if search_string.lower() == 'exit':
            break
        search_database(search_string)

if __name__ == "__main__":
    main()
