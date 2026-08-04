
#python
# ==========================================================
# STUDENT PERFORMANCE ANALYTICS SYSTEM
# REPORT GENERATION MODULE
# Python + Oracle + CSV Export
# ==========================================================

import pandas as pd
import oracledb

import warnings
warnings.simplefilter("ignore", UserWarning)

# ==========================================================
# DATABASE CONNECTION
# ==========================================================

conn = oracledb.connect(
    user="Aridhan",
    password="Oracle123@",
    dsn="localhost/XEPDB1"
)

print("=" * 60)
print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
print("=" * 60)

# ==========================================================
# STUDENT PERFORMANCE REPORT
# ==========================================================

print("\nGenerating Student Performance Report...")

performance_query = """
SELECT
    s.student_id,
    s.student_name,
    s.department,
    ROUND(AVG(m.marks),2) AS average_marks
FROM students s
JOIN marks m
ON s.student_id = m.student_id
GROUP BY
    s.student_id,
    s.student_name,
    s.department
ORDER BY average_marks DESC
"""

performance_df = pd.read_sql(performance_query, conn)

print("\nSTUDENT PERFORMANCE REPORT")
print(performance_df)

performance_df.to_csv(
    "Student_Performance_Report.csv",
    index=False
)

print("Student_Performance_Report.csv Exported Successfully")

# ==========================================================
# ATTENDANCE PERCENTAGE REPORT
# ==========================================================

print("\nGenerating Attendance Report...")

attendance_query = """
SELECT
    a.student_id,
    s.student_name,
    a.total_classes,
    a.attended_classes,
    ROUND(
        (a.attended_classes * 100) /
        a.total_classes,2
    ) AS attendance_percentage
FROM attendance a
JOIN students s
ON a.student_id = s.student_id
"""

attendance_df = pd.read_sql(attendance_query, conn)

print("\nATTENDANCE REPORT")
print(attendance_df)

attendance_df.to_csv(
    "Attendance_Report.csv",
    index=False
)

print("Attendance_Report.csv Exported Successfully")

# ==========================================================
# GRADE CALCULATION REPORT
# ==========================================================

print("\nGenerating Grade Report...")

grade_query = """
SELECT
    s.student_id,
    s.student_name,
    ROUND(AVG(m.marks),2) AS average_marks
FROM students s
JOIN marks m
ON s.student_id = m.student_id
GROUP BY
    s.student_id,
    s.student_name
"""

grade_df = pd.read_sql(grade_query, conn)

def calculate_grade(avg_marks):

    if avg_marks >= 90:
        return "A+"
    elif avg_marks >= 80:
        return "A"
    elif avg_marks >= 70:
        return "B"
    elif avg_marks >= 60:
        return "C"
    elif avg_marks >= 50:
        return "D"
    else:
        return "FAIL"

grade_df["GRADE"] = grade_df["AVERAGE_MARKS"].apply(
    calculate_grade
)

print("\nGRADE REPORT")
print(grade_df)

grade_df.to_csv(
    "Grade_Report.csv",
    index=False
)

print("Grade_Report.csv Exported Successfully")

# ==========================================================
# TOP STUDENT REPORT
# ==========================================================

print("\nGenerating Top Student Report...")

top_student = grade_df.sort_values(
    by="AVERAGE_MARKS",
    ascending=False
).head(1)

print(top_student)

top_student.to_csv(
    "Top_Student_Report.csv",
    index=False
)

print("Top_Student_Report.csv Exported Successfully")

# ==========================================================
# SUMMARY STATISTICS REPORT
# ==========================================================

marks_query = """
SELECT marks
FROM marks
"""

marks_df = pd.read_sql(marks_query, conn)

summary = pd.DataFrame({
    "Metric": [
        "Average Marks",
        "Maximum Marks",
        "Minimum Marks",
        "Median Marks",
        "Standard Deviation"
    ],
    "Value": [
        marks_df["MARKS"].mean(),
        marks_df["MARKS"].max(),
        marks_df["MARKS"].min(),
        marks_df["MARKS"].median(),
        marks_df["MARKS"].std()
    ]
})

print("\nSUMMARY STATISTICS")
print(summary)

summary.to_csv(
    "Summary_Statistics_Report.csv",
    index=False
)

print("Summary_Statistics_Report.csv Exported Successfully")

# ==========================================================
# CLOSE CONNECTION
# ==========================================================

conn.close()

print("\nAll Reports Generated Successfully")
