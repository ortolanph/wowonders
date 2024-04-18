# -------------------------- STAGE --------------------------
COUNT_STAGE = "SELECT count(*) as total_stage FROM WOW_STAGE WHERE wow_country = ? and wow_landmark = ?"
SELECT_STAGE_ID = "SELECT id FROM WOW_STAGE WHERE wow_country = ? and wow_landmark = ?"
INSERT_STAGE = "INSERT INTO WOW_STAGE (wow_country, wow_landmark) values (?, ?)"
IS_STAGE_PROCESSED = "SELECT processed FROM WOW_STAGE WHERE wow_country = ? and wow_landmark = ?"
UPDATE_PROCESSED = "UPDATE WOW_STAGE SET processed = 1 WHERE id = ?"

# -------------------------- LEVEL --------------------------
COUNT_LEVEL = "SELECT count(*) as total_level FROM WOW_LEVEL WHERE wow_level = ?"
SELECT_LEVEL_ID = "SELECT id FROM WOW_LEVEL WHERE wow_level = ?"
INSERT_LEVEL = "INSERT INTO WOW_LEVEL (wow_stage_id, wow_level, wow_letters) values (?, ?, ?)"

# -------------------------- ANSWERS --------------------------
COUNT_ANSWER = "SELECT count(*) as total_answer FROM WOW_ANSWER WHERE wow_answer = ?"
SELECT_ANSWER_ID = "SELECT id FROM WOW_ANSWER WHERE wow_answer = ?"
INSERT_ANSWER = "INSERT INTO WOW_ANSWER (wow_answer) values (?)"

# -------------------------- LEVEL X ANSWERS --------------------------
LINK_ANSWER_TO_LEVEL = "INSERT INTO wow_answer_level (wow_level_id, wow_answer_id) VALUES (?, ?)"

# QUERIES
ALL_STAGES = "SELECT id, wow_country, wow_landmark FROM wow_stage WHERE processed = 1 ORDER BY id;"
LEVEL_BY_STAGE_ID = "SELECT id, wow_level, wow_letters FROM wow_level WHERE wow_stage_id = ? ORDER BY id;"
ANSWERS_BY_LEVEL_ID = """
    select a.wow_answer
      from wow_answer_level al
           inner join main.wow_answer a on a.id = al.wow_answer_id
           inner join main.wow_level l on al.wow_level_id = l.id
     where l.wow_level = ?;
"""
LEVEL_BY_LEVEL_ID = """
select l.wow_level, l.wow_letters, s.id, s.wow_country, s.wow_landmark
  from wow_level l inner join main.wow_stage s on s.id = l.wow_stage_id
 where l.wow_level = ?;
"""
STAGE_BY_COUNTRY_LIKE = """
select id, wow_country, wow_landmark
  from wow_stage
 where wow_country like ?
 order by id;
"""
LEVEL_ID_BY_COUNTRY_IDS = """
select s.id, l.id
  from wow_stage s
         inner join main.wow_level l on s.id = l.wow_stage_id
 where s.id in (%s)
"""
#
# select *
#   from wow_stage
#  where wow_landmark like '%Big Ben%';
#
# select *
#   from wow_stage
#  where wow_landmark like '%blue%'
#     or wow_country like '%blue%';
#
# select *
#   from wow_level
#  where wow_letters like '%STARS%';
