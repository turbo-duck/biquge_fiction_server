# 数据库的一些字段内容
CREATE TABLE "fiction_chapterdetaillist" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "chapter_code" text NOT NULL, "chapter_content" text NOT NULL);

CREATE INDEX "chapter_code"
ON "fiction_chapterdetaillist" (
  "chapter_code"
);

CREATE TABLE "fiction_chapterlist" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "chapter_code" text NOT NULL,
  "chapter_name" text NOT NULL,
  "chapter_order" integer NOT NULL,
  "create_time" datetime NOT NULL,
  "update_time" datetime NOT NULL,
  "fiction_code" text NOT NULL
);

CREATE TABLE "fiction_chapterdetaillist" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "chapter_code" text NOT NULL, "chapter_content" text NOT NULL);

CREATE INDEX "chapter_code"
ON "fiction_chapterdetaillist" (
  "chapter_code"
);
