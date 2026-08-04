# Student Performance Analytics Dashboard

An end-to-end data analytics project that tracks student academic performance 
and attendance, from database design through to an interactive Power BI dashboard.

## Overview

This project simulates a real-world academic analytics workflow: a relational 
database stores student, subject, marks, and attendance data; a Python + Oracle 
SQL pipeline cleans and aggregates that data into performance reports; and an 
interactive Power BI dashboard visualizes the results for decision-making.

## Tech Stack

- **Database:** Oracle SQL
- **ETL / Scripting:** Python (Pandas, oracledb)
- **Visualization:** Power BI, DAX

## Features

- Designed a 4-table relational schema (Students, Subjects, Marks, Attendance) 
  with proper primary/foreign key relationships
- Built Python + Oracle SQL scripts to extract, clean, and aggregate exam and 
  attendance data into performance reports
- Calculated average marks, attendance %, and letter grades using automated logic
- Built a 2-page interactive Power BI dashboard with filters, drill-downs, and tooltips
- Exported reusable CSV reports (performance summary, attendance %, grade distribution, top students)


## Live Walkthrough

Watch the interactive dashboard in action: [Loom Demo](https://www.loom.com/share/3a1b5d0f36b3484eb7c3c42073848694)

## Data Model

- **Students** — student ID, name, gender, department, contact info
- **Subjects** — subject ID, name, credits
- **Marks** — links students to subjects with exam scores
- **Attendance** — tracks total vs attended classes per student

## Files in this Repository

- `schema.sql` — database schema and sample data
- `report_generator.py` — Python script for ETL and report generation
- `*.csv` — exported performance, attendance, and grade reports

## Author

Thulasee Anbazhagan  
[LinkedIn](https://www.linkedin.com/in/thulasee-a-9b9824416/) | Email : thulasee97@gmail.com
