CREATE TABLE IF NOT EXISTS "t_teachers" (
"id"  INTEGER,
"name"  TEXT(16),
"remark"  TEXT(32)
);

CREATE TABLE IF NOT EXISTS "t_students" (
"id"  INTEGER,
"name"  TEXT(16),
"remark"  TEXT(32)
);

CREATE TABLE IF NOT EXISTS "t_employers" (
"id"  INTEGER,
"name"  TEXT(16),
"remark"  TEXT(32)
);

CREATE TABLE IF NOT EXISTS "t_employees" (
"id"  INTEGER,
"name"  TEXT(16),
"remark"  TEXT(32)
);


INSERT INTO "t_teachers" VALUES (1, 'apple_1', 'aaa_1');
INSERT INTO "t_teachers" VALUES (2, 'boy_1', 'bbb_1');
INSERT INTO "t_teachers" VALUES (3, 'cat_1', 'ccc_1');

INSERT INTO "t_students" VALUES (1, 'apple_2', 'aaa_2');
INSERT INTO "t_students" VALUES (2, 'boy_2', 'bbb_2');
INSERT INTO "t_students" VALUES (3, 'cat_2', 'ccc_2');

INSERT INTO "t_employers" VALUES (1, 'apple_3', 'aaa_3');
INSERT INTO "t_employers" VALUES (2, 'boy_3', 'bbb_3');
INSERT INTO "t_employers" VALUES (3, 'cat_3', 'ccc_3');

INSERT INTO "t_employees" VALUES (1, 'apple_4', 'aaa_4');
INSERT INTO "t_employees" VALUES (2, 'boy_4', 'bbb_4');
INSERT INTO "t_employees" VALUES (3, 'cat_4', 'ccc_4');
