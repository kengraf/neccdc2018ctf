import pandas
import MySQLdb
from time import gmtime, strftime

DEBUG = True


class Insert_Questions():
    print "Reading questions.csv file..."
    data = None
    try:
        data = pandas.read_csv('questions.csv')
    except ValueError:
        print "Invalid questions.csv file."
        exit()
    question_list = []
    answer_list = []
    point_list = []
    hint_list = []
    hint_penalty_list = []
    country_list = []
    title_list = []
    category_list = []
    try:
        question_list = data['Question'].tolist()
        answer_list = data['Answer'].tolist()
        point_list = data['Points'].tolist()
        hint_list = data['Hint'].tolist()
        hint_penalty_list = data['HintPenalty'].tolist()
        country_list = data['Country'].tolist()
        title_list = data['Title'].tolist()
        category_list = data['Category'].tolist()
        print "Successfully retrieved all data from questions.csv"
    except KeyError:
        print """You have an incorrect column name in your CSV file. Please use the following headers in any order:
Question
Answer
Points
Hint
Penalty
Country
Title
Category
"""
    db = None
    cur = None
    try:
        db = MySQLdb.connect(host="localhost",
                             user="root",
                             passwd="root",
                             db="fbctf")
        cur = db.cursor()
        cur.execute("SELECT 'Connection to the database established'")
        print cur.fetchall()[0][0]
    except:
        print "There was an error connecting to the database"


    print "Removing all current questions from the database..."
    try:
        cur.execute("DELETE FROM levels;") #Not for testing if SQL works. Counter-productive.
        db.commit()
        print "Successfully removed all current questions from the database."
        #print "Not removiing questions"
    except:
        print "There was an error removing all questions from the database"
        
        
    print "Reading country_iso.csv file..."
    iso_data = None
    try:
        iso_data = pandas.read_csv('country_iso.csv')
        print "Received all data from country_iso.csv"
    except:
        print "Invalid country_iso.csv file."
        exit()
        
    country_name = iso_data['Country']
    fb_country_id = iso_data['Fbid']
    countryname_fbid = dict(zip(country_name, fb_country_id))
    
    if DEBUG:
        for k,v in countryname_fbid.items():
            print "Key: {}, Value: {}".format(k,v)
    
        
    
    country_entity_list = []
    for country in country_list:
        if DEBUG:
            print country
            print countryname_fbid[country.upper()]
            #print iso_countryid_dict[countryname_iso[country]]
            print "{} has an FB country id of {}".format(country, countryname_fbid[country.upper()])
        country_entity_list.append(countryname_fbid[country.upper()])
        
        
    rows = zip(question_list, answer_list, point_list, hint_list, hint_penalty_list, country_entity_list, title_list, category_list)

    sql_statements = []
    for row in rows:
        sql_start = "INSERT INTO levels (active, type, title, description, entity_id, category_id, points, flag, hint, penalty, bonus, bonus_dec, bonus_fix) VALUES "
        sql_values = "({}, '{}', '{}', '{}', {}, {}, {}, '{}', '{}', {}, {}, {}, {}); ".format(1, 'quiz', db.escape_string(str(row[6]).strip()), db.escape_string(str(row[0]).strip()), row[5], db.escape_string(str(row[7]).split('-')[0]), row[2], db.escape_string(str(row[1])), db.escape_string(str(row[3])), row[4], 0, 0, 0)
        sql_statements.append(sql_start + sql_values)

    print "Attempting to add questions to the database..."
    try:
        i = 0
        for sql in sql_statements:
            if DEBUG:
                print sql
            cur.execute(sql)
            db.commit()
            i += 1
            print "Successfully added {} questions to the database.".format(i)
    except:
        print "There was an error inserting the data into the database"


if __name__ == "__main__":
    my_thing = Insert_Questions()
