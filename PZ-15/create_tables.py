import sqlite3 as sq


with sq.connect('decanat.db') as con:
    # Факультеты
    con.execute(
    '''
    CREATE TABLE IF NOT EXISTS faculty (
        id INTEGER PRIMARY KEY,
        faculty_name VARCHAR   
    )                       
    '''
    )
    # Кафедры
    con.execute(
        '''
    CREATE TABLE IF NOT EXISTS departments (
        id INTEGER PRIMARY KEY,
        depatment_name VARCHAR,
        id_faculty INTEGER   
    )                       
    '''
    )
    # Специальности
    con.execute(
        '''
    CREATE TABLE IF NOT EXISTS specialties (
        id INTEGER PRIMARY KEY,
        specialty_name VARCHAR,
        id_department INTEGER   
    )                       
    '''
    )
    # Предметы
    con.execute(
        '''
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY,
        subject_name VARCHAR
    )                       
    '''
    )
    # Форма сдачи предмета
    con.execute(
        '''
    CREATE TABLE IF NOT EXISTS subject_methods (
        id INTEGER PRIMARY KEY,
        subject_method_name VARCHAR
    )                       
    '''
    )
    # Учебный план
    con.execute(
        '''
    CREATE TABLE IF NOT EXISTS study_program (
        id INTEGER PRIMARY KEY,
        id_specialtie INTEGER,
        id_subject INTEGER,
        id_subject_method INTEGER,
        num_lecture_hours INTEGER,
        num_practical_hours INTEGER,
        num_lab_hours INTEGER,
        final_task BOOL  
    )                       
    '''
    )
    # Абитуриенты
    con.execute(
        '''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        surname VARCHAR,
        student_name VARCHAR,
        fathers_name VARCHAR,
        gender VARCHAR,
        date_birth VARCHAR,
        address VARCHAR,
        phone VARCHAR,
        email VARCHAR,
        entry_date VARCHAR, 
        student_specialty INT,
        group_num VARCHAR
    )                       
    '''
    )
    # Учебная карточка
    con.execute(
        '''
    CREATE TABLE IF NOT EXISTS study_card (
        id INTEGER PRIMARY KEY,
        id_student INT,
        id_specialty INT,
        id_subject INT,
        subject_method VARCHAR,
        mark INTEGER
    )                       
    '''
    )
