-- Insert sample categories
INSERT INTO categories (name) VALUES ('TVs');
INSERT INTO categories (name) VALUES ('Monitors');
INSERT INTO categories (name) VALUES ('Appliances');
INSERT INTO categories (name) VALUES ('Computers');

-- Insert sample products
INSERT INTO products (name, price, quality, summary, image, category_id) VALUES
('Dryer', '$29.99', 'Hot', 'A dryer that will definitely dry your clothes.', 'http://localhost:8000/images/broken-dryer.jpg', 3),
('Hairdryer', '$3.50', 'Very Nice', 'This is gonna dry your hair real good.', 'http://localhost:8000/images/broken-hairdryer', 3),
('Tower', '$19.99', 'New', 'Very good air flow nice for run fast', 'http://localhost:8000/images/broken-tower', 4),
('TV', '$49.99', 'Almost not broken', 'You can watch all the netflixes on it', 'http://localhost:8000/images/broken-tv', 1),
('Monitor', '$100.00', 'Pretty Good', 'You can use it like a legos', 'http://localhost:8000/images/broken-monitor', 4);