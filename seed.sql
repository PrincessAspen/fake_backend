-- Insert categories
INSERT INTO categories (name) VALUES ('TVs');
INSERT INTO categories (name) VALUES ('Monitors');
INSERT INTO categories (name) VALUES ('Appliances');
INSERT INTO categories (name) VALUES ('Computers');

--Insert products
INSERT INTO products (name, price, quality, summary, image, category_id) VALUES
('Dryer', '$29.99', 'Hot', 'A dryer that will definitely dry your clothes.', 'http://localhost:8000/images/broken-dryer.jpg', 3),
('Hairdryer', '$3.50', 'Very Nice', 'This is gonna dry your hair real good.', 'http://localhost:8000/images/broken-hairdryer.webp', 3),
('Tower', '$19.99', 'New', 'Very good air flow nice for run fast', 'http://localhost:8000/images/broken-tower.jpg', 4),
('TV', '$49.99', 'Almost not broken', 'You can watch all the netflixes on it', 'http://localhost:8000/images/broken-tv.jpg', 1),
('Monitor', '$100.00', 'Pretty Good', 'You can use it like a legos', 'http://localhost:8000/images/broken-monitor.jpg', 4);

--More products
INSERT INTO products (name, price, quality, summary, image, category_id) VALUES
('Screen', '$5.00', 'Shiny', 'The screen is very bright for to see real good', 'http://localhost:8000/images/broken-screen.webp', 1),
('PC', '$3000.00', 'Nice', 'You ever seen a computer this good?', 'http://localhost:8000/images/tower-two.webp)', 4),
('Washer', '$20.00', 'Only a little brown', 'It''s got to be good, look how much dirt it removed', 'http://localhost:8000/images/broken-washer.jpg', 3),
('Television', '$422.83', 'Still good', 'So colorful, your face will love to see it', 'http://localhost:8000/images/broken-tv-two.jpg', 1),
('Telly', '$1.50', 'That''ll buff out', 'It would look great on your table', 'http://localhost:8000/images/broken-tv-three.jpg')