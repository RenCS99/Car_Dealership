CREATE TABLE Employee(
    e_eid INTEGER PRIMARY KEY AUTOINCREMENT,
    e_did INTEGER NOT NULL,
    e_admin CHAR(1) NOT NULL,
    e_inventoryId INTEGER NOT NULL,
    FOREIGN KEY (e_did) REFERENCES Dealer(e_did)
);

CREATE TABLE Dealer(
    d_did INTEGER PRIMARY KEY AUTOINCREMENT,
    d_name TEXT NOT NULL,
    d_location TEXT NOT NULL,
    d_eid INTEGER NOT NULL,
    FOREIGN KEY (d_eid) REFERENCES Employee(e_eid)
);

CREATE TABLE Inventory(
    i_inventoryId INTEGER PRIMARY KEY AUTOINCREMENT,
    i_name TEXT NOT NULL,
    i_location TEXT NOT NULL,
    i_did INTEGER NOT NULL,
    i_modelName TEXT NOT NULL,
    i_modelYear INTEGER NOT NULL,
    i_brandName TEXT NOT NULL,
    i_vin VARCHAR(17) NOT NULL,
    FOREIGN KEY (i_did) REFERENCES Dealer(d_did),
    FOREIGN KEY (i_modelName) REFERENCES Car_Model(cm_modelName),
    FOREIGN KEY (i_modelYear) REFERENCES Car_Model(cm_modelYear),
    FOREIGN KEY (i_brandName) REFERENCES Car_Model(cm_brandModel),
    FOREIGN KEY (i_vin) REFERENCES Vehicle(m_vin)
);

CREATE TABLE Vehicle(
    v_vid INTEGER PRIMARY KEY AUTOINCREMENT,
    v_cid INTEGER NOT NULL,
    v_oid INTEGER NOT NULL,
    v_vin VARCHAR(17) NOT NULL,
    v_price FLOAT NOT NULL,
    v_inventoryId INTEGER NOT NULL,
    v_manufacturerId INTEGER NOT NULL,
    FOREIGN KEY (v_cid) REFERENCES Customer(c_cid),
    FOREIGN KEY (v_oid) REFERENCES Options(o_oid),
    FOREIGN KEY (v_inventoryId) REFERENCES Inventory(i_inventoryId),
    FOREIGN KEY (v_manufacturerId) REFERENCES Manufacturer(m_manufacturerId)
);

CREATE TABLE Sales(
    s_sid INTEGER PRIMARY KEY AUTOINCREMENT,
    s_eid INTEGER NOT NULL,
    s_did INTEGER NOT NULL,
    s_cid INTEGER NOT NULL,
    s_vin VARCHAR(17) NOT NULL,
    s_date DATE NOT NULL,
    s_price FLOAT NOT NULL,
    FOREIGN KEY (s_eid) REFERENCES Employee(e_eid),
    FOREIGN KEY (s_did) REFERENCES Dealer(d_did),
    FOREIGN KEY (s_cid) REFERENCES Customer(c_cid),
    FOREIGN KEY (s_vin) REFERENCES Vehicle(v_vin),
    FOREIGN KEY (s_price) REFERENCES Vehicle(v_price)
);

CREATE TABLE Customer(
    c_cid INTEGER PRIMARY KEY AUTOINCREMENT,
    c_did INTEGER NOT NULL,
    c_name TEXT NOT NULL,
    c_phone VARCHAR(12) NOT NULL,
    c_gender CHAR(1) NOT NULL,
    FOREIGN KEY (c_did) REFERENCES Dealer(d_did)
);

CREATE TABLE Manufacturer(
    m_manufacturerId INTEGER PRIMARY KEY AUTOINCREMENT,
    m_vin VARCHAR(17) NOT NULL,
    m_manufacturerName TEXT NOT NULL,
    m_location TEXT NOT NULL,
    FOREIGN KEY (m_vin) REFERENCES Vehicle(v_vin)
);

CREATE TABLE Options(
    o_oid INTEGER PRIMARY KEY AUTOINCREMENT,
    o_manufacturerId INTEGER NOT NULL,
    o_transmission CHAR(3) NOT NULL,
    o_engine TEXT NOT NULL,
    o_color VARCHAR(1) NOT NULL,
    o_cmid INTEGER NULL,
    FOREIGN KEY (o_manufacturerId) REFERENCES Manufacturer(m_manufacturerId),
    FOREIGN KEY (o_cmid) REFERENCES Car_Model(cm_cmid)
);

CREATE TABLE Car_Model(
    cm_cmid INTEGER PRIMARY KEY AUTOINCREMENT,
    cm_bodyStyle TEXT NOT NULL,
    cm_manufacturerName TEXT NOT NULL,
    cm_modelName TEXT NOT NULL,
    cm_modelYear INTEGER(4) NOT NULL,
    cm_brandName TEXT NOT NULL,
    FOREIGN KEY (cm_manufacturerName) REFERENCES Manufacturer(m_manufacturerName)
);