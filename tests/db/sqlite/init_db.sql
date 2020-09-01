CREATE TABLE IF NOT EXISTS "t_teachers" (
"i_id"  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
"s_name"  TEXT(16),
"s_remark"  TEXT(64)
);

CREATE TABLE IF NOT EXISTS "t_students" (
"i_id"  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
"s_name"  TEXT(16),
"s_remark"  TEXT(64)
);

CREATE TABLE IF NOT EXISTS "t_employers" (
"i_id"  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
"s_name"  TEXT(16),
"s_remark"  TEXT(64)
);

CREATE TABLE IF NOT EXISTS "t_employees" (
"i_id"  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
"s_name"  TEXT(16),
"s_remark"  TEXT(64)
);


INSERT INTO "t_teachers"("s_name", "s_remark") VALUES ('apple_1', 'aaa_1');
INSERT INTO "t_teachers"("s_name", "s_remark")  VALUES ('boy_1', 'bbb_1');
INSERT INTO "t_teachers"("s_name", "s_remark")  VALUES ('cat_1', 'ccc_1');

INSERT INTO "t_students"("s_name", "s_remark")  VALUES ('apple_2', 'aaa_2');
INSERT INTO "t_students"("s_name", "s_remark")  VALUES ('boy_2', 'bbb_2');
INSERT INTO "t_students"("s_name", "s_remark")  VALUES ('cat_2', 'ccc_2');

INSERT INTO "t_employers"("s_name", "s_remark")  VALUES ('apple_3', 'aaa_3');
INSERT INTO "t_employers"("s_name", "s_remark")  VALUES ('boy_3', 'bbb_3');
INSERT INTO "t_employers"("s_name", "s_remark")  VALUES ('cat_3', 'ccc_3');

INSERT INTO "t_employees"("s_name", "s_remark")  VALUES ('apple_4', 'aaa_4');
INSERT INTO "t_employees"("s_name", "s_remark")  VALUES ('boy_4', 'bbb_4');
INSERT INTO "t_employees"("s_name", "s_remark")  VALUES ('cat_4', 'ccc_4');
