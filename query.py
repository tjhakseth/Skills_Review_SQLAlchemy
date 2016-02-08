"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

db.session.query(Brand).get(8).one()

db.session.query(Model).filter(Model.name=='Corvette', Brand.name=='Chevrolet').all()

db.session.query(Model).filter(Model.year>1960).all()

db.session.query(Brand).filter(Brand.founded>1920).all()

db.session.query(Model).filter(Model.name.like("%Cor%")).all()

db.session.query(Brand).filter(Brand.founded==1903, Brand.discontinued==None).all()

#these two didn't work but they should!

db.session.query(Brand).filter(db.or_(Brand.founded < 1950, Brand.discontinued != None)).all()

db.session.query(Model).filter(Model.brand_name != 'Chevrolet').all()




# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    year_input = raw_input("Enter a year: ")
    year_input = int(year_input)
    
    query_year = db.session.query(Model, Brand).filter(Model.year == year_input).all()

    for year in query_year:
        if year is not None:
            print year.name, year.brand_name, year.headquarters



def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

     brand_input = raw_input("Enter brand name: ")


     brand_check = db.session.query(Model).filter(Model.brand_name == brand_input).all()

    for brand in brand_check:
        if brand is not None:
            print brand.name, brand.brand_name

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

    #This is an object of the class Brand 

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
        #An associate table is a table in which the "middle table" hold no valuable 
        #information other than the fact that it stategically joins two tables together.
        #Associate tables have a one to one relationship!
