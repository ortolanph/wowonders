create table wow_stage (
	id integer not null primary key AUTOINCREMENT,
	wow_country text not null,
	wow_landmark text not null,
	processed integer default 0
);

create table wow_level (
	id integer not null primary key AUTOINCREMENT,
	wow_stage_id integer not null,
	wow_level integer not null,
	wow_letters text not null,
	foreign key(wow_stage_id) references wow_stage(id)
);

create table wow_answer (
	id integer not null primary key AUTOINCREMENT,
	wow_answer text not null
);

create table wow_answer_level (
	id integer not null primary key AUTOINCREMENT,
	wow_level_id integer not null,
	wow_answer_id integer not null,
	foreign key(wow_level_id) references wow_level(id),
	foreign key(wow_answer_id) references wow_answer(id)
);