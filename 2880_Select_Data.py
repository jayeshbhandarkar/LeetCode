import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    student = students[students['student_id'] == 101]
    result = student[['name', 'age']]
    return result
