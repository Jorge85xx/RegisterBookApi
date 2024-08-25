USE BOOKPROJECT;
INSERT INTO publisher (publisher_id, name) VALUES
(1, 'Penguin Random House'),
(2, 'HarperCollins'),
(3, 'Simon & Schuster'),
(4, 'Hachette Book Group'),
(5, 'Macmillan'),
(6, 'MIT Press'),
(7, 'Wiley'),
(8, 'O\'Reilly Media'),
(9, 'Addison-Wesley'),
(10, 'McGraw-Hill'),
(11, 'Marvel Comics'),
(12, 'DC Comics');

USE BOOKPROJECT;
-- Inserindo gêneros
INSERT INTO genre (genre_id, name) VALUES
(1, 'Technology and IT'),
(2, 'Comics'),
(3, 'Science Fiction'),
(4, 'Fantasy'),
(5, 'Business'),
(6, 'Romance'),
(7, 'Drama');

INSERT INTO author (author_id, first_name, last_name, bio) VALUES
(1, 'Robert', 'Martin', 'Autor de Clean Code e outros livros sobre desenvolvimento ágil.'),
(2, 'Erich', 'Gamma', 'Um dos autores de Design Patterns.'),
(3, 'Thomas', 'Cormen', 'Co-autor de Introduction to Algorithms.'),
(4, 'Andrew', 'Hunt', 'Co-autor de The Pragmatic Programmer.'),
(5, 'Alfred', 'Aho', 'Co-autor de Compilers: Principles, Techniques, and Tools.'),
(6, 'Charles', 'Petzold', 'Autor de Code: The Hidden Language of Computer Hardware and Software.'),
(7, 'Gerry', 'Conway', 'Roteirista de Spider-Man.'),
(8, 'Frank', 'Miller', 'Autor de Batman: The Dark Knight Returns.'),
(9, 'Alan', 'Moore', 'Autor de Watchmen.'),
(10, 'Frank', 'Miller', 'Autor de Daredevil: Born Again.'),
(11, 'Frank', 'Herbert', 'Autor de Dune.'),
(12, 'William', 'Gibson', 'Autor de Neuromancer.'),
(13, 'Isaac', 'Asimov', 'Autor de Foundation.'),
(14, 'Orson', 'Scott Card', 'Autor de Ender\'s Game.'),
(15, 'J.R.R.', 'Tolkien', 'Autor de The Hobbit.'),
(16, 'Patrick', 'Rothfuss', 'Autor de The Name of the Wind.'),
(17, 'Terry', 'Pratchett', 'Autor de Good Omens.'),
(18, 'Glen', 'Cook', 'Autor de The Black Company.'),
(19, 'Robert', 'Kiyosaki', 'Autor de Rich Dad Poor Dad.'),
(20, 'Jim', 'Collins', 'Autor de Good to Great.'),
(21, 'Eric', 'Ries', 'Autor de The Lean Startup.'),
(22, 'Daniel', 'Kahneman', 'Autor de Thinking, Fast and Slow.'),
(23, 'Jane', 'Austen', 'Autora de Pride and Prejudice.'),
(24, 'Emily', 'Brontë', 'Autora de Wuthering Heights.'),
(25, 'Charlotte', 'Brontë', 'Autora de Jane Eyre.'),
(26, 'F. Scott', 'Fitzgerald', 'Autor de The Great Gatsby.'),
(27, 'Harper', 'Lee', 'Autora de To Kill a Mockingbird.'),
(28, 'J.D.', 'Salinger', 'Autor de The Catcher in the Rye.'),
(29, 'Toni', 'Morrison', 'Autora de Beloved.'),
(30, 'Ken', 'Kesey', 'Autor de One Flew Over the Cuckoo\'s Nest.'),
(31, 'Frank', 'Miller', 'Autor de Batman: Year One.'),
(32, 'Jeph', 'Loeb', 'Autor de Batman: Hush.'),
(33, 'Alan', 'Moore', 'Autor de The Killing Joke.'),
(34, 'Mark', 'Millar', 'Autor de Superman: Red Son.');

USE bookproject;

-- Inserindo livros com IDs de autores corrigidos
INSERT INTO book (book_id, title, publisher_id, cover_image, author_id, synopsis) VALUES
-- Tecnologia e TI
(1, 'Clean Code', 6, 'url_to_cover_image1', 1, 'A handbook of agile software craftsmanship.'),
(2, 'Design Patterns', 6, 'url_to_cover_image2', 2, 'A book on reusable object-oriented software design patterns.'),
(3, 'Introduction to Algorithms', 6, 'url_to_cover_image3', 3, 'A comprehensive textbook on algorithms.'),
(4, 'The Pragmatic Programmer', 6, 'url_to_cover_image4', 4, 'A guide to software development best practices.'),
(5, 'Compilers: Principles, Techniques, and Tools', 6, 'url_to_cover_image5', 5, 'A definitive book on compiler design.'),
(6, 'Code: The Hidden Language of Computer Hardware and Software', 7, 'url_to_cover_image6', 6, 'An introduction to how computers work.'),
-- Quadrinhos
(7, 'Spider-Man: The Night Gwen Stacy Died', 11, 'url_to_cover_image7', 7, 'A Spider-Man storyline where Gwen Stacy dies.'),
(8, 'Batman: The Dark Knight Returns', 12, 'url_to_cover_image8', 8, 'A graphic novel about Batman in his later years.'),
(9, 'Watchmen', 12, 'url_to_cover_image9', 9, 'A graphic novel exploring the lives of superheroes in an alternate history.'),
(10, 'Daredevil: Born Again', 12, 'url_to_cover_image10', 10, 'A storyline about Daredevil facing his greatest challenges.'),
-- Ficção Científica
(11, 'Dune', 4, 'url_to_cover_image11', 11, 'A science fiction epic set on the desert planet Arrakis.'),
(12, 'Neuromancer', 4, 'url_to_cover_image12', 12, 'A novel that defined the cyberpunk genre.'),
(13, 'Foundation', 4, 'url_to_cover_image13', 13, 'A novel about the fall and rise of a galactic empire.'),
(14, 'Ender\'s Game', 4, 'url_to_cover_image14', 14, 'A story about a young boy training to be a military leader.'),
-- Fantasia
(15, 'The Hobbit', 4, 'url_to_cover_image15', 15, 'A fantasy novel about Bilbo Baggins\' adventure.'),
(16, 'The Name of the Wind', 4, 'url_to_cover_image16', 16, 'A novel about a young man\'s rise to legend.'),
(17, 'Good Omens', 4, 'url_to_cover_image17', 17, 'A comedic fantasy novel about the apocalypse.'),
(18, 'The Black Company', 4, 'url_to_cover_image18', 18, 'A dark fantasy novel about a mercenary company.'),
-- Negócios
(19, 'Rich Dad Poor Dad', 5, 'url_to_cover_image19', 19, 'A personal finance book about wealth building.'),
(20, 'Good to Great', 5, 'url_to_cover_image20', 20, 'Insights into what makes companies successful.'),
(21, 'The Lean Startup', 5, 'url_to_cover_image21', 21, 'A guide to launching successful startups.'),
(22, 'Thinking, Fast and Slow', 5, 'url_to_cover_image22', 22, 'A book about the two systems of thinking that drive our decisions.'),
-- Romance
(23, 'Pride and Prejudice', 1, 'url_to_cover_image23', 23, 'A classic novel about love and social class.'),
(24, 'Wuthering Heights', 1, 'url_to_cover_image24', 24, 'A novel about the tumultuous relationship between Heathcliff and Catherine.'),
(25, 'Jane Eyre', 1, 'url_to_cover_image25', 25, 'A novel about a young woman’s experiences and her love for Mr. Rochester.'),
(26, 'The Great Gatsby', 1, 'url_to_cover_image26', 26, 'A novel about the American Dream and love in the 1920s.'),
-- Drama
(27, 'To Kill a Mockingbird', 1, 'url_to_cover_image27', 27, 'A novel about racial injustice in the Deep South.'),
(28, 'The Catcher in the Rye', 1, 'url_to_cover_image28', 28, 'A novel about adolescent angst and alienation.'),
(29, 'Beloved', 1, 'url_to_cover_image29', 29, 'A novel about slavery and its impact on a woman’s life.'),
(30, 'One Flew Over the Cuckoo\'s Nest', 1, 'url_to_cover_image30', 30, 'A novel about a man’s rebellion against institutional oppression.'),
-- Adicionar HQs Marvel e DC
(31, 'Batman: Year One', 12, 'url_to_cover_image31', 31, 'A retelling of Batman\'s origin story.'),
(32, 'Batman: Hush', 12, 'url_to_cover_image32', 32, 'A Batman storyline involving a mysterious figure known as Hush.'),
(33, 'The Killing Joke', 12, 'url_to_cover_image33', 33, 'A graphic novel that delves into the Joker\'s origin story.'),
(34, 'Superman: Red Son', 12, 'url_to_cover_image34', 34, 'A graphic novel where Superman lands in the Soviet Union.');
