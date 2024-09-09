import unittest
from app import create_app
from extensions import db
from models import User, Book, Author
from services.user_book_service import UserBookService
from services.user_service import UserService
from services.book_service import BookService
from services.author_service import AuthorService
from config.test_config import TestingConfig
import random
import string

class UserBookServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config.from_object(TestingConfig)
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()

    def _generate_random_string(self, length=10):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def _generate_random_cpf(self):
        return ''.join(random.choices(string.digits, k=11))

    def test_add_user_book(self):
        with self.app.app_context():
            author = AuthorService.create_author("Stan", "Lee", "Creathor of spider man")

            user = UserService.create_user(
                first_name="Luke",
                last_name="Skywalker",
                nickname=self._generate_random_string(),
                cpf=self._generate_random_cpf(),
                phone_number="555-5555",
                profile_picture="luke.jpg",
                password="password123",
                quote="May the Force be with you."
            )

            book = BookService.create_book(
                title="Spider-Man: Homecoming",
                publisher_id=1,
                cover_image="spiderman.jpg",
                author_id=author.author_id,
                synopsis="Peter Parker tries to balance high school life with being Spider-Man."
            )

            user_book = UserBookService.add_user_book(
                user_id=user.user_id,
                book_id=book.book_id,
                progress=50,
                rating=8,
                notes="Interesting book",
                favorite=True
            )
            self.assertIsNotNone(user_book)
            self.assertEqual(user_book.user_id, user.user_id)
            self.assertEqual(user_book.book_id, book.book_id)
            self.assertEqual(user_book.progress, 50.0)
            self.assertEqual(user_book.rating, 8)
            self.assertTrue(user_book.favorite)

            BookService.delete_book(book.book_id)
            AuthorService.delete_author(author.author_id)
            UserBookService.delete_user_book(user_book.user_book_id)

    def test_get_user_book(self):
        with self.app.app_context():
            author = AuthorService.create_author("Jack", "Kirby", "beautiful mind of marvel comics")

            user = UserService.create_user(
                first_name="Leia",
                last_name="Organa",
                nickname=self._generate_random_string(),
                cpf=self._generate_random_cpf(),
                phone_number="555-5555",
                profile_picture="leia.jpg",
                password="password123",
                quote="Hope is like the sun."
            )

            book = BookService.create_book(
                title="Fantastic Four: Rise of the Silver Surfer",
                publisher_id=1,
                cover_image="fantastic_four.jpg",
                author_id=author.author_id,
                synopsis="The Fantastic Four face the cosmic entity known as the Silver Surfer."
            )

            user_book = UserBookService.add_user_book(
                user_id=user.user_id,
                book_id=book.book_id,
                progress=50,
                rating=8,
                notes="Interesting book",
                favorite=True
            )
            fetched_user_book = UserBookService.get_user_book(user_book.user_book_id)
            self.assertIsNotNone(fetched_user_book)
            self.assertEqual(fetched_user_book.user_book_id, user_book.user_book_id)


            BookService.delete_book(book.book_id)
            AuthorService.delete_author(author.author_id)
            UserBookService.delete_user_book(user_book.user_book_id)

    def test_update_user_book(self):
        with self.app.app_context():
            author = AuthorService.create_author("Jerry", "Siegel", ".....")

          
            user = UserService.create_user(
                first_name="Han",
                last_name="Solo",
                nickname=self._generate_random_string(),
                cpf=self._generate_random_cpf(),
                phone_number="555-5555",
                profile_picture="han.jpg",
                password="password123",
                quote="Never tell me the odds."
            )

            book = BookService.create_book(
                title="Superman: The Man of Steel",
                publisher_id=1,
                cover_image="superman.jpg",
                author_id=author.author_id,
                synopsis="The origins and rise of Superman, the Man of Steel."
            )

         
            user_book = UserBookService.add_user_book(
                user_id=user.user_id,
                book_id=book.book_id,
                progress=50,
                rating=8,
                notes="Interesting book",
                favorite=True
                
            )
            updated_user_book = UserBookService.update_user_book(
                user_book.user_book_id,
                progress=75.0,
                rating=9,
                favorite=True
            )
            self.assertIsNotNone(updated_user_book)
            self.assertEqual(updated_user_book.progress, 75.0)
            self.assertEqual(updated_user_book.rating, 9)
            self.assertTrue(updated_user_book.favorite)

    
            BookService.delete_book(book.book_id)
            AuthorService.delete_author(author.author_id)
            UserBookService.delete_user_book(user_book.user_book_id)

    def test_delete_user_book(self):
        with self.app.app_context():
            
            author = AuthorService.create_author("Bob", "Kane", "creathor of batman")

            
            user = UserService.create_user(
                first_name="Darth",
                last_name="Vader",
                nickname=self._generate_random_string(),
                cpf=self._generate_random_cpf(),
                phone_number="555-5555",
                profile_picture="vader.jpg",
                password="password123",
                quote="I find your lack of faith disturbing."
            )

            book = BookService.create_book(
                title="Batman: The Dark Knight Returns",
                publisher_id=1,
                cover_image="batman.jpg",
                author_id=author.author_id,
                synopsis="Batman comes out of retirement to fight crime in Gotham City."
            )

            
            user_book = UserBookService.add_user_book(
                user_id=user.user_id,
                book_id=book.book_id,
                progress=50,
                rating=8,
                notes="Interesting book",
                favorite=True
            )
            success = UserBookService.delete_user_book(user_book.user_book_id)
            self.assertTrue(success)
            deleted_user_book = UserBookService.get_user_book(user_book.user_book_id)
            self.assertIsNone(deleted_user_book)

            
            BookService.delete_book(book.book_id)
            AuthorService.delete_author(author.author_id)
           

    def test_get_all_user_books_by_user(self):
        with self.app.app_context():
           
            author = AuthorService.create_author("Bill", "Finger", "...")

            user = UserService.create_user(
                first_name="Yoda",
                last_name="mester",
                nickname=self._generate_random_string(),
                cpf=self._generate_random_cpf(),
                phone_number="555-5555",
                profile_picture="yoda.jpg",
                password="password123",
                quote="Do or do not, there is no try."
            )

            book_1 = BookService.create_book(
                title="Batman: Year One",
                publisher_id=1,
                cover_image="batman_year_one.jpg",
                author_id=author.author_id,
                synopsis="The story of Batman's first year as a crime-fighter."
            )

            book_2 = BookService.create_book(
                title="Batman: Hush",
                publisher_id=1,
                cover_image="batman_hush.jpg",
                author_id=author.author_id,
                synopsis="Batman faces a mysterious new villain known as Hush."
            )

            user_book_1 = UserBookService.add_user_book(
                user_id=user.user_id,
                book_id=book_1.book_id,
                progress=50,
                rating=8,
                notes="Interesting book",
                favorite=True
            )
            user_book_2 = UserBookService.add_user_book(
                user_id=user.user_id,
                book_id=book_2.book_id,
                progress=100,
                rating=8,
                notes="Interesting book",
                favorite=True
            )
            user_books = UserBookService.get_all_user_books_by_user(user.user_id)
            self.assertEqual(len(user_books), 2)
            self.assertIn(user_book_1, user_books)
            self.assertIn(user_book_2, user_books)

            BookService.delete_book(book_1.book_id)
            BookService.delete_book(book_2.book_id)
            AuthorService.delete_author(author.author_id)
            UserBookService.delete_user_book(user_book_1.user_book_id)
            UserBookService.delete_user_book(user_book_2.user_book_id)

    def test_mark_as_favorite(self):
        with self.app.app_context():
        
            author = AuthorService.create_author("Steve",  "Ditko", "Better than stan lee")

          
            user = UserService.create_user(
                first_name="Obi-Wan",
                last_name="Kenobi",
                nickname=self._generate_random_string(),
                cpf=self._generate_random_cpf(),
                phone_number="555-5555",
                profile_picture="obiwan.jpg",
                password="password123",
                quote="The Force will be with you, always."
            )

            book = BookService.create_book(
                title="Doctor Strange: The Oath",
                publisher_id=1,
                cover_image="doctor_strange.jpg",
                author_id=author.author_id,
                synopsis="Doctor Strange uncovers a deadly conspiracy while searching for a cure for Wong."
            )

            
            user_book = UserBookService.add_user_book(
                user_id=user.user_id,
                book_id=book.book_id,
                progress=50,
                rating=8,
                notes="Interesting book",
                favorite=True
            )
            marked_favorite = UserBookService.mark_as_favorite(user_book.user_book_id)
            self.assertIsNotNone(marked_favorite)
            self.assertTrue(marked_favorite.favorite)

            
            BookService.delete_book(book.book_id)
            AuthorService.delete_author(author.author_id)
            UserBookService.delete_user_book(user_book.book_id)

if __name__ == '__main__':
    unittest.main()
