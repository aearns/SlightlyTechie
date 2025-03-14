
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(128) NOT NULL,
    author VARCHAR(128) NOT NULL,
    year_published INT NOT NULL
);

INSERT INTO books (title, author, year_published)
VALUES
    ('The Beauty and the Beast', 'L. Reed', 1825),
    ('Ei, Ghanaman', 'Biibini', 2025),
    ('To Kill a Goat', 'Addo D', 1960),
    ('Pride and Injustice', 'Jane Mary', 1813),
    ('Things Fall Apart', 'Chinua Achebe', 1997);

SELECT * FROM books;

SELECT * FROM books WHERE author = 'Addo D';

UPDATE books SET year_published = 2011 WHERE author = 'Addo D';

Delete from books where title = 'To Kill a Goat'

CREATE TABLE borrowers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    book_id INT,
    borrow_date DATE DEFAULT CURRENT_DATE,
    return_date DATE,
    CONSTRAINT fk_book FOREIGN KEY (book_id) REFERENCES books(id)
);

INSERT INTO borrowers (name, book_id, return_date) VALUES
('Nyaniba Ed', 3, '2024-03-20'),
('John Doe', 2, '2024-03-22'),
('Bill Agyeman', 1, '2024-04-01');

select * from borrowers;

SELECT books.title, books.author, borrowers.name, borrowers.borrow_date, borrowers.return_date
FROM books
LEFT JOIN borrowers ON books.id = borrowers.book_id;