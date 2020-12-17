CREATE TABLE Employee(
    e_eid INTEGER PRIMARY KEY NOT NULL,
    e_did INTEGER NOT NULL
);

CREATE TABLE Dealer(
    d_did INTEGER PRIMARY KEY AUTOINCREMENT,
    d_name TEXT NOT NULL,
    d_location TEXT NOT NULL
);

CREATE TABLE Inventory(
    i_inventoryId INTEGER PRIMARY KEY AUTOINCREMENT,
    i_location TEXT NOT NULL,
    i_did INTEGER NOT NULL,
    i_condition VARCHAR(4) NOT NULL,
    i_oid INTEGER NOT NULL,
    i_vin VARCHAR(17) NOT NULL,
    FOREIGN KEY (i_did) REFERENCES Dealer(d_did),
    FOREIGN KEY (i_location) REFERENCES Dealer(d_location),
    FOREIGN KEY (i_oid) REFERENCES Options(o_oid)
);

CREATE TABLE Vehicle(
    v_vid INTEGER PRIMARY KEY AUTOINCREMENT,
    v_modelName TEXT NOT NULL,
    v_modelYear INT(4) NOT NULL,
    v_brandName TEXT NOT NULL,
    v_bodyStyle TEXT NOT NULL,
    v_color TEXT NOT NULL,
    v_price INTEGER NOT NULL,
    v_inventoryId INTEGER NOT NULL,
    v_manufacturer TEXT NOT NULL,
    FOREIGN KEY (v_inventoryId) REFERENCES Inventory(i_inventoryId)
);

CREATE TABLE Sales(
    s_sid INTEGER PRIMARY KEY AUTOINCREMENT,
    s_eid INTEGER NOT NULL,
    s_did INTEGER NOT NULL,
    s_cid INTEGER NOT NULL,
    s_vin VARCHAR(17) NOT NULL,
    s_date DATE NOT NULL,
    s_saleMethod CHAR(1) NOT NULL,
    s_price INTEGER NOT NULL,
    FOREIGN KEY (s_eid) REFERENCES Employee(e_eid),
    FOREIGN KEY (s_did) REFERENCES Dealer(d_did),
    FOREIGN KEY (s_cid) REFERENCES Customer(c_cid),
    FOREIGN KEY (s_vin) REFERENCES Inventory(v_vin),
    FOREIGN KEY (s_price) REFERENCES Vehicle(v_price)
);

CREATE TABLE Customer(
    c_cid INTEGER PRIMARY KEY AUTOINCREMENT,
    c_did INTEGER,
    c_name TEXT NOT NULL,
    c_phone VARCHAR(12) NOT NULL,
    c_gender CHAR(1) NOT NULL,
    FOREIGN KEY (c_did) REFERENCES Dealer(d_did)
);

CREATE TABLE Options(
    o_oid INTEGER PRIMARY KEY NOT NULL,
    o_transmission CHAR(3) NOT NULL,
    o_engine VARCHAR(4) NOT NULL
);


-- Populating Employee Table
INSERT INTO Employee VALUES(1, 5);
INSERT INTO Employee VALUES(2, 4);
INSERT INTO Employee VALUES(3, 3);
INSERT INTO Employee VALUES(4, 6);
INSERT INTO Employee VALUES(5, 7);
INSERT INTO Employee VALUES(6, 2);
INSERT INTO Employee VALUES(7, 1);
INSERT INTO Employee VALUES(8, 10);
INSERT INTO Employee VALUES(9, 9);
INSERT INTO Employee VALUES(10, 8);

-- Populating Dealer Table

INSERT INTO Dealer(d_name, d_location) VALUES('Choice Vehicles', 'ALABAMA');
INSERT INTO Dealer(d_name, d_location) VALUES('Auto Mart', 'CALIFORNIA');
INSERT INTO Dealer(d_name, d_location) VALUES('Anycar', 'WASHINGTON');
INSERT INTO Dealer(d_name, d_location) VALUES('Auto Sales', 'TEXAS');
INSERT INTO Dealer(d_name, d_location) VALUES('Discount Motors', 'FLORIDA');
INSERT INTO Dealer(d_name, d_location) VALUES('Used Cars 4 You', 'COLORADO');
INSERT INTO Dealer(d_name, d_location) VALUES('Auto Wizard', 'ARIZONA');
INSERT INTO Dealer(d_name, d_location) VALUES('Village Auto', 'MASSACHUSETTS');
INSERT INTO Dealer(d_name, d_location) VALUES('Vance Ford', 'UTAH');
INSERT INTO Dealer(d_name, d_location) VALUES('Grand Touring Cars INC', 'NEVADA');     

-- Populating Inventory Table

-- INSERT INTO Inventory(i_location, i_did, i_condition, i_oid, i_vin) VALUES('NEVADA', 5, 'USED', 1, 'WVWAK73CX7P035949');
-- INSERT INTO Inventory(i_location, i_did, i_condition, i_oid, i_vin) VALUES('CALIFORNIA', 2, 'NEW', 2, '1N4AL21E78C153699');
-- INSERT INTO Inventory(i_location, i_did, i_condition, i_oid, i_vin) VALUES('WASHINGTON', 3, 'NEW', 2, '1G1AK55F177302951');
-- INSERT INTO Inventory(i_location, i_did, i_condition, i_oid, i_vin) VALUES('WASHINGTON', 3, 'USED', 3, '1XP7DB9XX5D823709');
-- INSERT INTO Inventory(i_location, i_did, i_condition, i_oid, i_vin) VALUES('CALIFORNIA', 2, 'NEW', 3, '5FNYF38649B059594');
-- INSERT INTO Inventory(i_location, i_did, i_condition, i_oid, i_vin) VALUES('TEXAS', 4, 'USED', 1, '1GCEC19V64E399880');
-- INSERT INTO Inventory(i_location, i_did, i_condition, i_oid, i_vin) VALUES('NEVADA', 5, 'NEW', 3, '4T1BF28B43U202258');
-- INSERT INTO Inventory(i_location, i_did, i_condition, i_oid, i_vin) VALUES('ALABAMA', 1, 'USED', 2, '1GDGG31V531905513');
-- INSERT INTO Inventory(i_location, i_did, i_condition, i_oid, i_vin) VALUES('TEXAS', 4, 'USED', 1, 'WAUAF78E68A119556');
-- INSERT INTO Inventory(i_location, i_did, i_condition, i_oid, i_vin) VALUES('ALABAMA', 1, 'NEW', 3, '1J4HR48N85C594885');

-- Populating Vehicle Table

-- INSERT INTO Vehicle(v_modelName, v_modelYear, v_brandName, v_bodyStyle, v_color, v_price, v_inventoryId, v_manufacturer) VALUES('MUSTANG', 2017, 'FORD', 'SPORTS', 'BROWN', 40458, 4, 'FORD');
-- INSERT INTO Vehicle(v_modelName, v_modelYear, v_brandName, v_bodyStyle, v_color, v_price, v_inventoryId, v_manufacturer) VALUES('ILX', 2019, 'ACURA', 'COMPACT', 'GREEN', 43806, 5, 'HONDA');
-- INSERT INTO Vehicle(v_modelName, v_modelYear, v_brandName, v_bodyStyle, v_color, v_price, v_inventoryId, v_manufacturer) VALUES('CRONOS', 2108, 'FIAT', 'COMPACT', 'PURPLE', 35680, 7, 'FIAT CHRYSLER AUTOMOBILES');
-- INSERT INTO Vehicle(v_modelName, v_modelYear, v_brandName, v_bodyStyle, v_color, v_price, v_inventoryId, v_manufacturer) VALUES('CAMERO', 2018, 'CHEVROLET', 'SPORTS', 'GRAY', 50000, 6, 'GENERAL MOTORS');
-- INSERT INTO Vehicle(v_modelName, v_modelYear, v_brandName, v_bodyStyle, v_color, v_price, v_inventoryId, v_manufacturer) VALUES('QASHQAI', 2017, 'INFINITY', 'SUV', 'MANGO', 43541, 1, 'NISSAN');
-- INSERT INTO Vehicle(v_modelName, v_modelYear, v_brandName, v_bodyStyle, v_color, v_price, v_inventoryId, v_manufacturer) VALUES('UX', 2019, 'LEXUS', 'WHITE', 'COMPACT', 69521, 2, 'TOYOTA');
-- INSERT INTO Vehicle(v_modelName, v_modelYear, v_brandName, v_bodyStyle, v_color, v_price, v_inventoryId, v_manufacturer) VALUES('8 SERIES', 2018, 'BMW', 'BLUE', 'LUXURY', 49583, 3, 'BMW');
-- INSERT INTO Vehicle(v_modelName, v_modelYear, v_brandName, v_bodyStyle, v_color, v_price, v_inventoryId, v_manufacturer) VALUES('MIRAGE G4', 2020, 'MITSUBISHI', 'SUBCOMPACT', 'WHITE', 26854, 9, 'MMC');
-- INSERT INTO Vehicle(v_modelName, v_modelYear, v_brandName, v_bodyStyle, v_color, v_price, v_inventoryId, v_manufacturer) VALUES('1500 TRX', 2021, 'RAM', 'BLACK', 'TRUCK', 34140, 8, 'FIAT CHRYSLER AUTOMOBILES');
-- INSERT INTO Vehicle(v_modelName, v_modelYear, v_brandName, v_bodyStyle, v_color, v_price, v_inventoryId, v_manufacturer) VALUES('CX-3', 2021, 'MAZDA', 'RED', 'SUBCOMPACT', 30913, 10, 'MAZDA MOTOR CORPORATION');

-- Populating Sales Table

-- INSERT INTO Sales(s_eid, s_did, s_cid, s_vin, s_date, s_saleMethod, s_price) VALUES(6, 3, 7, '1XP7DB9XX5D823709', '2020-03-18', 'S', 40458);
-- INSERT INTO Sales(s_eid, s_did, s_cid, s_vin, s_date, s_saleMethod, s_price) VALUES(7, 2, 2, '5FNYF38649B059594', '2019-02-02', 'S', 43806);
-- INSERT INTO Sales(s_eid, s_did, s_cid, s_vin, s_date, s_saleMethod, s_price) VALUES(2, 1, 3, '1J4HR48N85C594885', '2020-09-20', 'S', 30913);
-- INSERT INTO Sales(s_eid, s_did, s_cid, s_vin, s_date, s_saleMethod, s_price) VALUES(1, 4, 4, '1GCEC19V64E399880', '2018-05-15', 'S',50000);
--INSERT INTO Sales(s_eid, s_did, s_cid, s_vin, s_date, s_saleMethod, s_price) VALUES(1, 2, 9, 'WVWAK73CX7P035949', '2019-01-19', 'S', 43541);
--INSERT INTO Sales(s_eid, s_did, s_cid, s_vin, s_date, s_saleMethod, s_price) VALUES(4, 1, 10, '1GDGG31V531905513', '2019-06-17', 'S', 34140);
--INSERT INTO Sales(s_eid, s_did, s_cid, s_vin, s_date, s_saleMethod, s_price) VALUES(4, 4, 1, 'WAUAF78E68A119556', '2020-12-05', 'S', 26854);
--INSERT INTO Sales(s_eid, s_did, s_cid, s_vin, s_date, s_saleMethod, s_price) VALUES(9, 2, 5, '1N4AL21E78C153699', '2020-08-06', 'S', 69521);
--INSERT INTO Sales(s_eid, s_did, s_cid, s_vin, s_date, s_saleMethod, s_price) VALUES(2, 3, 6, '1G1AK55F177302951', '2020-06-02', 'S', 49583);
--INSERT INTO Sales(s_eid, s_did, s_cid, s_vin, s_date, s_saleMethod, s_price) VALUES(5, 5, 8, '4T1BF28B43U202258', '2017-05-01', 'S', 35680);
 
-- Populating Customer Table

INSERT INTO Customer(c_did, c_name, c_phone, c_gender) VALUES(NULL, 'John Mike', '615-535-8189', 'F');
INSERT INTO Customer(c_did, c_name, c_phone, c_gender) VALUES(NULL, 'Nathan Cornish', '917-349-4358', 'F');
INSERT INTO Customer(c_did, c_name, c_phone, c_gender) VALUES(NULL, 'Sanah George', '209-816-5386', 'F');
INSERT INTO Customer(c_did, c_name, c_phone, c_gender) VALUES(NULL, 'Strom Frank', '716-566-6933', 'M');
INSERT INTO Customer(c_did, c_name, c_phone, c_gender) VALUES(NULL, 'Helen Larsen', '580-995-0188', 'F');
INSERT INTO Customer(c_did, c_name, c_phone, c_gender) VALUES(NULL, 'Alya Griffith', '781-231-2633', 'M');
INSERT INTO Customer(c_did, c_name, c_phone, c_gender) VALUES(NULL, 'Catherine Parry', '251-679-2169', 'M');
INSERT INTO Customer(c_did, c_name, c_phone, c_gender) VALUES(NULL, 'Mateo Peters', '401-440-8521', 'M');
INSERT INTO Customer(c_did, c_name, c_phone, c_gender) VALUES(NULL, 'Kay Mcdowell', '580-995-5285', 'F');
INSERT INTO Customer(c_did, c_name, c_phone, c_gender) VALUES(NULL, 'Blessing Whittaker', '478-278-3544', 'M');

-- Populating Options Table

INSERT INTO Options VALUES(1, 'AT', 'V-6');
INSERT INTO Options VALUES(2, 'MT', 'V-8');
INSERT INTO Options VALUES(3, 'CVT', 'V-4');