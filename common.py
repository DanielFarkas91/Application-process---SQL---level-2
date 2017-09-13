import data_manager


@data_manager.connection_handler
def show_mentors(cursor):
    cursor.execute("""SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                    FROM mentors JOIN schools ON mentors.city = schools.city
                    ORDER BY mentors.id""")
    answers = cursor.fetchall()
    return answers


@data_manager.connection_handler
def all_school(cursor):
    cursor.execute("""SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                    FROM mentors FULL JOIN schools ON mentors.city = schools.city
                    ORDER BY mentors.id""")
    answers = cursor.fetchall()
    return answers


@data_manager.connection_handler
def mentors_by_country(cursor):
    cursor.execute("""SELECT COUNT(mentors.id), schools.country
                    FROM mentors JOIN schools ON mentors.city = schools.city
                    GROUP BY schools.country""")
    answers = cursor.fetchall()
    return answers


@data_manager.connection_handler
def contacts(cursor):
    cursor.execute("""SELECT schools.name, mentors.first_name, mentors.last_name
                FROM mentors JOIN schools ON (mentors.id = schools.contact_person)
                ORDER BY schools.name""")
    answers = cursor.fetchall()
    return answers


@data_manager.connection_handler
def applicants(cursor):
    cursor.execute("""SELECT applicants.first_name, applicants.application_code,
                    applicants_mentors.creation_date
                    FROM applicants JOIN applicants_mentors ON (applicants.id = 
                    applicants_mentors.applicant_id)
                    WHERE applicants_mentors.creation_date > '20160101'
                    ORDER BY creation_date DESC; """)
    answers = cursor.fetchall()
    return answers
