# For new or empty data base only!!!
# manage.py shell
# >>> import library.fill_db as db
# >>> db.fill_all()



from authentication.models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order
from datetime import datetime, timedelta
from django.utils import timezone
from library import settings


def fill_db_users():
    for i in range(len(names)):
        param = {
            'email': emails[i],
            'password': passwords[i],
            'first_name': names[i],
            'middle_name': middlenames[i],
            'last_name': lastnames[i]
                 }
        CustomUser.create(**param)


def fill_db_authors():
    for author in authors:
        Author.create(**author)


def fill_db_books():
    for book in books:
        Book.create(**book)

def fill_db_orders():
    for i in range(len(names)):
        Order.create(user=CustomUser.get_by_id(i+1),
                     book=Book.get_by_id((i % (len(books)) + 1)),
                     plated_end_at=(timezone.now()+timedelta(days=15)))

def fill_all():
    fill_db_users()
    fill_db_authors()
    fill_db_books()
    fill_db_orders()

authors = [
        {"name": 'J. K.', "surname": 'Rowling' },
        {"name": 'Stephen', "surname": 'King'},
        {"name": 'Mark', "surname": 'Lutz'},
        {"name": 'Steve', "surname": 'McConnell'},
        {"name": 'Nassim Nicholas', "surname": 'Taleb'},
        {"name": 'Yuval Noah', "surname": 'Harari'},
        {"name": 'John Ronald', "surname": 'Tolkien'},
        {"name": 'Ivan', "surname": 'Franko'}
]

books = [
    {
       "name": 'Harry Potter Complete Book Series Special Edition Boxed Set',
       "description": "The box itself is beautifully designed with new artwork by "
                       "Kazu Kibuishi, and the books create a gorgeous, magical vista "
                       "when the spines are lined up together. The Harry Potter series "
                       "has been hailed as \"one for the ages\" by Stephen King and \"a "
                       "spellbinding saga\" by USA Today. Now is your chance to give "
                       "this set to a reader who is ready to embark on the series that "
                       "has changed so many young readers' lives.",
        'authors': [1]
    },
            {"name": 'Fantastic Beasts and Where to Find Them',
     "description": "Inspired by the original Hogwart's textbook by Newt Scamander, "
                     "Fantastic Beasts and Where to Find Them: The Original screenplay "
                     "marks the screenwriting debut of J.K. Rowling, author of the beloved "
                     "and internationally bestselling Harry Potter books. A feat of "
                     "imagination and featuring a cast of remarkable characters and "
                     "magical creatures, this is epic adventure-packed storytelling at "
                     "its very best. Whether an existing fan or new to the wizarding world, "
                     "this is a perfect addition for any film lover or reader's bookshelf.",
        'authors': [1]      },
    {
        "name": "The Shining",
        "description": "Jack Torrance's new job at the Overlook Hotel is the perfect "
                        "chance for a fresh start. As the off-season caretaker at the "
                        "atmospheric old hotel, he'll have plenty of time to spend "
                        "reconnecting with his family and working on his writing. But "
                        "as the harsh winter weather sets in, the idyllic location feels "
                        "ever more remote...and more sinister. And the only one to notice "
                        "the strange and terrible forces gathering around the Overlook "
                        "is Danny Torrance, a uniquely gifted five-year-old",
        'authors': [2]
    },
    {
        "name": "Learning Python, 5th Edition",
        "description": "Get a comprehensive, in-depth introduction to the core Python language "
                        "with this hands-on book. Based on author Mark Lutz’s popular training "
                        "course, this updated fifth edition will help you quickly write efficient, "
                        "high-quality code with Python. It’s an ideal way to begin, whether you’re "
                        "new to programming or a professional developer versed in other languages.",
        'authors': [3]
    },
    {
        "name": "Code Complete: A Practical Handbook of Software Construction, Second Edition",
        "description": "Widely considered one of the best practical guides to programming, "
                        "Steve McConnell’s original CODE COMPLETE has been helping developers "
                        "write better software for more than a decade. Now this classic book "
                        "has been fully updated and revised with leading-edge practices—and "
                        "hundreds of new code samples—illustrating the art and science of "
                        "software construction. Capturing the body of knowledge available from "
                        "research, academia, and everyday commercial practice, McConnell "
                        "synthesizes the most effective techniques and must-know principles "
                        "into clear, pragmatic guidance. No matter what your experience level, "
                        "development environment, or project size, this book will inform and "
                        "stimulate your thinking—and help you build the highest quality code.",
        'authors': [4]
    },
    {
        "name": "Antifragile: Things That Gain from Disorder",
        "description": "Antifragile is a standalone book in Nassim Nicholas Taleb’s landmark "
                        "Incerto series, an investigation of opacity, luck, uncertainty, "
                        "probability, human error, risk, and decision-making in a world we "
                        "don’t understand. The other books in the series are Fooled by "
                        "Randomness, The Black Swan, Skin in the Game, and The Bed of "
                        "Procrustes.",
        'authors': [5]
    },
    {
        "name": "Sapiens: A Brief History of Humankind",
        "description": "From a renowned historian comes a groundbreaking "
                        "narrative of humanity’s creation and evolution—a #1 i"
                        "nternational bestseller—that explores the ways in which "
                        "biology and history have defined us and enhanced our understanding "
                        "of what it means to be “human.”",
        'authors': [6]
    },
    {
        "name": "The Hobbit",
        "description": "Like every other hobbit, Bilbo Baggins likes nothing better "
                        "than a quiet evening in his snug hole in the ground, dining "
                        "on a sumptuous dinner in front of a fire. But when a wandering "
                        "wizard captivates him with tales of the unknown, Bilbo becomes "
                        "restless. Soon he joins the wizard’s band of homeless dwarves "
                        "in search of giant spiders, savage wolves, and other dangers. "
                        "Bilbo quickly tires of the quest for adventure and longs for "
                        "the security of his familiar home. But before he can return to "
                        "his life of comfort, he must face the greatest threat of all - a "
                        "treasure-troving dragon named Smaug.",
        'authors': [7]
    },
    {
        "name": "Zakhar Berkut",
        "description": "The story \"Zakhar Berkut\" is the most famous work of art by "
                        "Ivan Franko on a historical theme. Reproducing the historical "
                        "past, the struggle of the people of Tukhlya against the Mongol-Tatars,"
                        " the writer intertwines artistic fiction and folk art, based on the "
                        "well-known legend in Galicia and Transcarpathia about how the Tukhol "
                        "community flooded the Mongol army in the spring of 1241. And whatever"
                        " it was, but today this story is perceived as surprisingly modern when "
                        "it comes to the liberation of our homeland from invaders.",
        'authors': [8]
    }
]

names = [
    'Isaac',
    'Albert',
    'Marie',
    'Charles',
    'Nikola',
    'Galileo',
    'Ada',
    'Pythagoras',
    'Rosalind',
    'Carl',
    'Neil'
]

middlenames = [
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    'deGrasse'
]

lastnames =[
    'Newton',
    'Einstein',
    'Curie',
    'Darwin',
    'Tesla',
    'Galilei',
    'Lovelace',
    '',
    'Franklin',
    'Sagan',
    'Tyson'
]

emails = [
    'principia@gmail.com',
    'eequalmc2@gmail.com',
    'polonia@gmail.com',
    'apeisnotmygrandpa@gmail.com',
    'tunguskaeventnotmyfault@gmail.com',
    'andyetitmoves@gmail.com',
    'bestprogerever@gmail.com',
    'allthingsarenumbers@gmail.com',
    'doublespiral@gmail.com',
    'wearestardust@gmail.com',
    'whereareyourproof@gmail.com'
]
passwords =[
    '12345678',
    '12345678',
    '12345678',
    '12345678',
    '12345678',
    '12345678',
    '12345678',
    '12345678',
    '12345678',
    '12345678',
    '12345678',
]



