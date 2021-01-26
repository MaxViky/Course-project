CREATE TABLE IF NOT EXISTS rooms (
	id	INTEGER AUTO_INCREMENT,
	name	TEXT,
	type	INTEGER,
	cost	INTEGER,
	bed_count	INTEGER,
	breakfast	INTEGER,
	busy	INTEGER,
	photo	TEXT,
	PRIMARY KEY(id) 
);
CREATE TABLE IF NOT EXISTS clients (
	id	INTEGER AUTO_INCREMENT,
	name	TEXT,
	phone	TEXT,
	passport	INTEGER,
	photo	TEXT,
	PRIMARY KEY(id)
);
CREATE TABLE IF NOT EXISTS users (
	id	INTEGER AUTO_INCREMENT,
	username	TEXT,
	password	TEXT,
	role	TEXT,
	PRIMARY KEY(id )
);
CREATE TABLE IF NOT EXISTS roomtype (
	id	INTEGER AUTO_INCREMENT,
	type	TEXT,
	discription	TEXT,
	PRIMARY KEY(id)
);
CREATE TABLE IF NOT EXISTS reservation (
	id	INTEGER AUTO_INCREMENT,
	client	INTEGER,
	room	INTEGER,
	arrival_date	TEXT,
	departure_date	TEXT,
	payment_day	TEXT,
	amount	REAL,
	FOREIGN KEY(client) REFERENCES clients(id),
	FOREIGN KEY(room) REFERENCES rooms(id),
	PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS discounts (
	id	INTEGER AUTO_INCREMENT,
	room	INTEGER,
	discount	INTEGER,
	FOREIGN KEY(room) REFERENCES rooms(id),
	PRIMARY KEY(id)
);
INSERT INTO rooms VALUES (1,'Стандарт малый',1,2500,1,350,0,'E:/Projects/Курсовая 2020-2021/Hostel/Images/Hotels/1267_room-type.jpg');
INSERT INTO rooms VALUES (2,'Стандарт с двуспальной кроватью',2,2800,1,350,0,'E:/Projects/Курсовая 2020-2021/Hostel/Images/Hotels/cafb9642143c4ded87d8cf219a3233fd.jpg');
INSERT INTO rooms VALUES (3,'Стандарт с раздельными кроватями',3,2800,3,350,0,'C:/Users/MaxNet/Downloads/index.jpg');
INSERT INTO rooms VALUES (4,'Люкс Imperial',2,3900,1,0,0,'');
INSERT INTO rooms VALUES (5,'Люкс Deluxe',3,4100,2,0,0,'');
INSERT INTO rooms VALUES (6,'Стандарт с раздельными кроватями',2,2800,2,180,0,'');
INSERT INTO rooms VALUES (7,'Гостиная',1,1200,1,120,0,'');
INSERT INTO users VALUES (1,'max','1','admin');
INSERT INTO users VALUES (2,'vika','1','manager');
INSERT INTO users VALUES (3,'stas','0','manager');
INSERT INTO clients VALUES (1,'Ефремова Виктория Владмировна','+7(937)-251-12-24','7125 154005','');
INSERT INTO clients VALUES (2,'Якунин Максим Константинович','+7(937)-270-59-82','7125 324458','');
INSERT INTO clients VALUES (3,'Кулибякин Александр Филиппович','+7(906)-265-48-21','7125 636541','');
INSERT INTO clients VALUES (4,'Шишкина Елизавета Станиславовна','+7(960)-364-15-21','7585 362541','');
INSERT INTO clients VALUES (5,'Фролов Александр Иванович','+7(354)-341-23-23','7025 300125','');
INSERT INTO clients VALUES (6,'Лавров Евгений Викторович','+7(584)-142-25-45','7585 458563','');
INSERT INTO clients VALUES (7,'Дьячков Илларион Валерьянович','+5(845)-123-54-66','5748 453123','');
INSERT INTO clients VALUES (8,'Константинов Игнат Рудольфович','+1(223)-546-84-12','4561 234548','');
INSERT INTO clients VALUES (9,'Антонов Гордей Тимурович','+4(568)-123-54-86','1235 451321','');
INSERT INTO clients VALUES (10,'Никитин Адриан Гордеевич','+5(468)-451-32-54','5413 213546','');
INSERT INTO clients VALUES (11,'Афанасьев Сергей Анатольевич','+7(958)-545-13-24','2135 469132','');
INSERT INTO clients VALUES (12,'Шилова Белла Улебовна','+7(645)-124-56-43','1254 513546','');
INSERT INTO clients VALUES (13,'Кондратьева Динара Филатовна','+7(585)-585-58-55','4546 545131','');
INSERT INTO clients VALUES (14,'Сорокина Виктория Ивановна','+1(235)-468-74-53','2345 678423','');
INSERT INTO clients VALUES (15,'фыв','','','');
INSERT INTO roomtype VALUES (1,'Single','однокомнатный, для размещения одного отдыхающего. Спальное место одно');
INSERT INTO roomtype VALUES (2,'Double','однокомнатный номер для двоих. Может быть с одной большой кроватью или с двумя раздельными кроватями.');
INSERT INTO roomtype VALUES (3,'Triple','номер для троих отдыхающих. Обычно в номере две кровати и одно дополнительное спальное место.');
INSERT INTO reservation VALUES (1,1,1,'05.01.2021','14.01.2021','05.01.2021',2565.0);
INSERT INTO reservation VALUES (2,2,4,'11.01.2021','11.01.2021','11.01.2021',3900.0);
INSERT INTO reservation VALUES (3,13,7,'22.01.2021','24.01.2021','22.01.2021',1320.0);

INSERT INTO discounts VALUES (1,1,10);
COMMIT;
