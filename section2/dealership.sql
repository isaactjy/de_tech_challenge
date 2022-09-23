CREATE TABLE cars (
    car_id integer PRIMARY KEY NOT NULL,
    manufacturer text NOT NULL,
    model_name text NOT NULL,
    serial_number text NOT NULL,
    weight float NOT NULL,
    price float NOT NULL
);

CREATE TABLE transactions (
    transaction_id integer PRIMARY KEY NOT NULL,
    transaction_date timestamp NOT NULL,
    car_id integer NOT NULL,
    customer_id integer NOT NULL,
    salesperson_id integer NOT NULL
);

CREATE TABLE customers (
    customer_id integer PRIMARY KEY NOT NULL,
    customer_firstname text NOT NULL,
    customer_lastname text NOT NULL,
    customer_phone text NOT NULL,
    customer_address text NOT NULL
);

CREATE TABLE salespersons (
    salesperson_id integer PRIMARY KEY NOT NULL,
    salesperson_firstname text NOT NULL,
    salesperson_lastname text NOT NULL
);

COMMIT;