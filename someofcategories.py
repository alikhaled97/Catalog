from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, Item

engine = create_engine('sqlite:///catalog.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


# Create dummy user
User1 = User(name="Ali Khaled", email="example@example.com")
session.add(User1)
session.commit()

# Items for Mammal
category1 = Category(user_id=1, name="Mammal")

session.add(category1)
session.commit()

# First item in mammals
Item1 = Item(user_id=1,
             name="Bats",
             description=("bats are very special mammals.They are the only"
                          "mammals that can fly (without an airplane!)"
                          "Flying squirrels are mammals too, but they"
                          "don't really fly  They jump from high in a"
                          "tree glide through the air like a kite."
                          "Bats flap their wings and fly like a bird."),
             category=category1)

session.add(Item1)
session.commit()

# Second item in mammals
Item2 = Item(user_id=1,
             name="Bears",
             description=("Bears are large strong omnivores Omnivore is a"
                          "fancy word for animals that eat both meat and"
                          "plants  They belong to the mammal class  Why"
                          "Because they are covered in hair they have a "
                          "spine they are warm blooded and they feed milk"
                          "to their babies once they are born"),
             category=category1)

session.add(Item2)
session.commit()

# Third item in mammals
Item3 = Item(user_id=1,
             name="Cats",
             description=("Cats are a very popular group of land mammals"
                          "within the suborder Feliformia, which includes"
                          "anything from lions to domestic cats. Cats are"
                          "often furry, and always carnivorous, animals. "),
             category=category1)

session.add(Item3)
session.commit()


# Items for Birds
category2 = Category(user_id=1, name="Bird")

session.add(category2)
session.commit()

# First item in Birds
Item1 = Item(user_id=1,
             name="Amirican Robin",
             description=("The American Robin is a member of the Bluebird and"
                          "Thrush family.  It's called the 'American' robin"
                          "because it was named after a similar"
                          "(though smaller) bird found in Great Britain."),
             category=category2)

session.add(Item1)
session.commit()

# Second item in Birds
Item2 = Item(user_id=1,
             name="Snowy Owl",
             description=("The snowy owl is one of the largest species of"
                          "owls.  Snowy owls are covered in brilliant white"
                          "feathers which help them blend into their arctic"
                          "surrounding.  The feathers entirely cover the owl"
                          "including the area around the talons."),
             category=category2)

session.add(Item2)
session.commit()

# Third item in Birds
Item3 = Item(user_id=1,
             name="Canada Goose",
             description=("Canada Geese are waterfowl that live throughout"
                          "most of North America.   They are famous for"
                          "their life-long mating, though a widowed goose"
                          "will usually choose another mate."),
             category=category2)

session.add(Item3)
session.commit()


# Item for Fish
category3 = Category(user_id=1, name="Fish")

session.add(category3)
session.commit()

# First item in fishes
Item1 = Item(user_id=1,
             name="Sharks",
             description=("In some form, sharks have been around for about"
                          "400 million years.  They are the top predators"
                          "of the ocean's natural food chain."),
             category=category3)

session.add(Item1)
session.commit()


print "added category items!"
