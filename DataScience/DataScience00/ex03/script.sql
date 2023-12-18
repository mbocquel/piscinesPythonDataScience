DO $$ BEGIN
    CREATE TYPE event AS ENUM ('cart', 'view', 'remove_from_cart');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

CREATE TABLE IF NOT EXISTS data_2022_oct
(
	event_time timestamp,
	event_type event,
	product_id INT,
	price money,
	user_id BIGINT,
	user_session UUID
);


COPY data_2022_oct
FROM '/tmp/data_2022_oct.csv'
DELIMITER ','
CSV HEADER;