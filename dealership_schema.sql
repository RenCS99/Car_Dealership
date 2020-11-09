CREATE TABLE Employee(
    e_eid INTEGER PRIMARY KEY NOT NULL,
    e_did INTEGER NOT NULL,
    e_admin CHAR(1) NOT NULL,
    e_inventoryId INTEGER NOT NULL,
    FOREIGN KEY (e_did) REFERENCES Dealer(e_did)
);

CREATE TABLE Dealer(
    d_did INTEGER PRIMARY KEY NOT NULL,
    d_name TEXT NOT NULL,
    d_location TEXT NOT NULL,
    d_eid INTEGER NOT NULL,
    FOREIGN KEY (d_eid) REFERENCES Employee(e_eid)
);

CREATE TABLE Inventory(
    i_inventoryId INTEGER PRIMARY KEY NOT NULL,
    i_location TEXT NOT NULL,
    i_did INTEGER NOT NULL,
    i_condition VARCHAR(4) NOT NULL,
    i_oid INTEGER NOT NULL,
    i_vin VARCHAR(17) NOT NULL,
    FOREIGN KEY (i_did) REFERENCES Dealer(d_did),
    FOREIGN KEY (i_location) REFERENCES Dealer(d_location),
    FOREIGN KEY (i_vin) REFERENCES Vehicle(v_vin),
    FOREIGN KEY (i_oid) REFERENCES Options(o_oid)
);

CREATE TABLE Vehicle(
    v_vid INTEGER PRIMARY KEY NOT NULL,
    v_cid INTEGER NOT NULL,
    v_modelName TEXT NOT NULL,
    v_modelYear INTEGER NOT NULL,
    v_brandName TEXT NOT NULL,
    v_bodyStyle TEXT NOT NULL,
    v_color TEXT NOT NULL,
    v_vin VARCHAR(17) NOT NULL,
    v_price INTEGER NOT NULL,
    v_inventoryId INTEGER NOT NULL,
    v_manufacturer TEXT NOT NULL,
    FOREIGN KEY (v_cid) REFERENCES Customer(c_cid),
    FOREIGN KEY (v_inventoryId) REFERENCES Inventory(i_inventoryId)
);

CREATE TABLE Sales(
    s_sid INTEGER PRIMARY KEY AUTOINCREMENT,
    s_eid INTEGER NOT NULL,
    s_did INTEGER NOT NULL,
    s_cid INTEGER NOT NULL,
    s_vin VARCHAR(17) NOT NULL,
    s_date DATE NOT NULL,
    s_price INTEGER NOT NULL,
    FOREIGN KEY (s_eid) REFERENCES Employee(e_eid),
    FOREIGN KEY (s_did) REFERENCES Dealer(d_did),
    FOREIGN KEY (s_cid) REFERENCES Customer(c_cid),
    FOREIGN KEY (s_vin) REFERENCES Vehicle(v_vin),
    FOREIGN KEY (s_price) REFERENCES Vehicle(v_price)
);

CREATE TABLE Customer(
    c_cid INTEGER PRIMARY KEY NOT NULL,
    c_did INTEGER NOT NULL,
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
INSERT INTO Employee VALUES(1, 3, 'N', 6);
INSERT INTO Employee VALUES(2, 1, 'N', 2);
INSERT INTO Employee VALUES(3, 1, 'N', 10);
INSERT INTO Employee VALUES(4, 5, 'Y', 5);
INSERT INTO Employee VALUES(5, 5, 'Y', 1);
INSERT INTO Employee VALUES(6, 4, 'N', 7);
INSERT INTO Employee VALUES(7, 2, 'N', 9);
INSERT INTO Employee VALUES(8, 2, 'N', 4);
INSERT INTO Employee VALUES(9, 5, 'N', 3);
INSERT INTO Employee VALUES(10, 3, 'Y', 1);

-- Populating Dealer Table

INSERT INTO Dealer VALUES(1, 'Choice Vehicles', 'ALABAMA', 3);
INSERT INTO Dealer VALUES(2, 'Auto Mart', 'CALIFORNIA', 7);
INSERT INTO Dealer VALUES(3, 'Anycar', 'WASHINGTON', 1);
INSERT INTO Dealer VALUES(4, 'Auto Sales', 'TEXAS', 6);
INSERT INTO Dealer VALUES(5, 'Discount Motors', 'NEVADA', 9);

-- Populating Inventory Table

INSERT INTO Inventory VALUES(1, 'NEVADA', 5, 'USED', 1, 'WVWAK73CX7P035949');
INSERT INTO Inventory VALUES(2, 'CALIFORNIA', 2, 'NEW', 2, '1N4AL21E78C153699');
INSERT INTO Inventory VALUES(3, 'WASHINGTON', 3, 'NEW', 2, '1G1AK55F177302951');
INSERT INTO Inventory VALUES(4, 'WASHINGTON', 3, 'USED', 3, '1XP7DB9XX5D823709');
INSERT INTO Inventory VALUES(5, 'CALIFORNIA', 2, 'NEW', 4, '5FNYF38649B059594');
INSERT INTO Inventory VALUES(6, 'TEXAS', 4, 'USED', 1, '1GCEC19V64E399880');
INSERT INTO Inventory VALUES(7, 'NEVADA', 5, 'NEW', 3, '4T1BF28B43U202258');
INSERT INTO Inventory VALUES(8, 'ALABAMA', 1, 'USED', 2, '1GDGG31V531905513');
INSERT INTO Inventory VALUES(9, 'TEXAS', 4, 'USED', 1, 'WAUAF78E68A119556');
INSERT INTO Inventory VALUES(10, 'ALABAMA', 1, 'NEW', 3, '1J4HR48N85C594885');

-- Populating Vehicle Table

INSERT INTO Vehicle VALUES(1, 7, 'MUSTANG', 2017, 'FORD', 'SPORTS', 'BROWN', '1XP7DB9XX5D823709', 40458, 4, 'FORD');
INSERT INTO Vehicle VALUES(2, 2, 'ILX', 2019, 'ACURA', 'COMPACT', 'GREEN', '5FNYF38649B059594', 43806, 5, 'HONDA');
INSERT INTO Vehicle VALUES(3, 8, 'CRONOS', 2108, 'FIAT', 'COMPACT', 'PURPLE', '4T1BF28B43U202258', 35680, 7, 'FIAT CHRYSLER AUTOMOBILES');
INSERT INTO Vehicle VALUES(4, 4, 'CAMERO', 2018, 'CHEVROLET', 'SPORTS', 'GRAY', '1GCEC19V64E399880', 50000, 6, 'GENERAL MOTORS');
INSERT INTO Vehicle VALUES(5, 9, 'QASHQAI', 2017, 'INFINITY', 'SUV', 'MANGO', 'WVWAK73CX7P035949', 43541, 1, 'NISSAN');
INSERT INTO Vehicle VALUES(6, 5, 'UX', 2019, 'LEXUS', 'WHITE', 'COMPACT', '1N4AL21E78C153699', 69521, 2, 'TOYOTA');
INSERT INTO Vehicle VALUES(7, 6, '8 SERIES', 2018, 'BMW', 'BLUE', 'LUXURY', '1G1AK55F177302951', 49583, 3, 'BMW');
INSERT INTO Vehicle VALUES(8, 1, 'MIRAGE G4', 2020, 'MITSUBISHI', 'SUBCOMPACT', 'WHITE', 'WAUAF78E68A119556', 26854, 9, 'MMC');
INSERT INTO Vehicle VALUES(9, 10, '1500 TRX', 2021, 'RAM', 'BLACK', 'TRUCK', '1GDGG31V531905513', 34140, 8, 'FIAT CHRYSLER AUTOMOBILES');
INSERT INTO Vehicle VALUES(10, 3, 'CX-3', 2021, 'MAZDA', 'RED', 'SUBCOMPACT', '1J4HR48N85C594885', 30913, 10, 'MAZDA MOTOR CORPORATION');

-- Populating Sales Table

INSERT INTO Sales(s_eid, s_did, s_cid, s_vin, s_date, s_price) VALUES(6, 3, 7, '1XP7DB9XX5D823709', '2020-03-18', 40458);
INSERT INTO Sales(s_eid, s_did, s_cid, s_vin, s_date, s_price) VALUES(7, 2, 2, '5FNYF38649B059594', '2019-02-02', 43806);
INSERT INTO Sales(s_eid, s_did, s_cid, s_vin, s_date, s_price) VALUES(2, 1, 3, '1J4HR48N85C594885', '2020-09-20', 30913);
INSERT INTO Sales(s_eid, s_did, s_cid, s_vin, s_date, s_price) VALUES(1, 4, 4, '1GCEC19V64E399880', '2018-05-15', 50000);
INSERT INTO Sales(s_eid, s_did, s_cid, s_vin, s_date, s_price) VALUES(1, 2, 9, 'WVWAK73CX7P035949', '2019-01-19', 43541);
INSERT INTO Sales(s_eid, s_did, s_cid, s_vin, s_date, s_price) VALUES(4, 1, 10, '1GDGG31V531905513', '2019-06-17', 34140);
INSERT INTO Sales(s_eid, s_did, s_cid, s_vin, s_date, s_price) VALUES(4, 4, 1, 'WAUAF78E68A119556', '2020-12-05', 26854);
INSERT INTO Sales(s_eid, s_did, s_cid, s_vin, s_date, s_price) VALUES(9, 2, 5, '1N4AL21E78C153699', '2020-08-06', 69521);
INSERT INTO Sales(s_eid, s_did, s_cid, s_vin, s_date, s_price) VALUES(2, 3, 6, '1G1AK55F177302951', '2020-06-02', 49583);
INSERT INTO Sales(s_eid, s_did, s_cid, s_vin, s_date, s_price) VALUES(5, 5, 8, '4T1BF28B43U202258', '2017-05-01', 35680);
 
-- Populating Customer Table

INSERT INTO Customer VALUES(1, 5, 'John Mike', '615-535-8189', 'F');
INSERT INTO Customer VALUES(2, 2, 'Nathan Cornish', '917-349-4358', 'F');
INSERT INTO Customer VALUES(3, 1, 'Sanah George', '209-816-5386', 'F');
INSERT INTO Customer VALUES(4, 3, 'Strom Frank', '716-566-6933', 'M');
INSERT INTO Customer VALUES(5, 5, 'Helen Larsen', '580-995-0188', 'F');
INSERT INTO Customer VALUES(6, 1, 'Alya Griffith', '781-231-2633', 'M');
INSERT INTO Customer VALUES(7, 4, 'Catherine Parry', '251-679-2169', 'M');
INSERT INTO Customer VALUES(8, 5, 'Mateo Peters', '401-440-8521', 'M');
INSERT INTO Customer VALUES(9, 3, 'Kay Mcdowell', '580-995-5285', 'F');
INSERT INTO Customer VALUES(10, 5, 'Blessing Whittaker', '478-278-3544', 'M');

-- Populating Options Table

INSERT INTO Options VALUES(1, 'TAT', 'V-6');
INSERT INTO Options VALUES(2, 'AMT', 'V-8');
INSERT INTO Options VALUES(3, 'CVT', 'V-4');

