DROP TABLE IF EXISTS BIDS;
CREATE TABLE BIDS (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  petID INTEGER  NOT NULL,
  userID INTEGER  NOT NULL,
  money INTEGER  NOT NULL
);
INSERT into BIDS(petID,userID, money) values (1,1,110);
INSERT into BIDS(petID,userID, money) values (2,2,220);
INSERT into BIDS(petID,userID, money) values (3,3,330);