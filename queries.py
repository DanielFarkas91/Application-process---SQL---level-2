import database_common


@database_common.connection_handler
def get_mentor_names(cursor):
    first_name = "László"
    cursor.execute("""SELECT first_name, last_name FROM mentors
                      WHERE first_name = %(f_n)s ORDER BY first_name;""",
                      {'f_n': first_name})
    names = cursor.fetchall()
    return names
