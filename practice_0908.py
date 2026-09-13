

query = """ 
SELECT 
    name,
    salary
FROM 
    employees
"""

df_subset = df[['name','salary']]


query = """ 
SELECT 
    name, 
    salary
FROM 
    employees
WHERE 
    salary > 100000


"""

df_subset = df[df['salary']>100000][['name','salary']]


query = """ 
SELECT 
    name,
    salary
FROM 
    employees 
WHERE 
    department = 'Engineering' 
    AND salary > 100000
"""

df_subset = df[(df['salary']>100000) & (df['department']=='Engineering')][['name','salary']]



query = """ 
SELECT 
    name,
    department
FROM 
    employees
WHERE 
    department = 'Engineering' 
    OR department = 'Sales'

"""

df_subset = df[(df['department']=='Engineering') | (df['department'] == 'Sales')][['name','department']]

df_subset = df[df['department'].isin(['Engineering', 'Sales'])][['name','Sales']]


query = """ 
SELECT 
    name,
    department,
    salary
FROM 
    employees
ORDER BY 
    name ASC

"""

df_subset = df[df['name','department','salary']].sort_values(by = 'name', ascending = True)


query = """ 
SELECT 
    name,
    department,
    salary
FROM 
    employees
ORDER BY 
    name DESC 

"""

df_sbuset = df[['name','department','salary']].sort_values(by = 'name', ascending = False)


query = """ 
SELECT 
    name,
    department,
    salary 
FROM 
    employees 
WHERE 
    salary > 125000
ORDER BY 
    salary DESC

"""

df_subset = df[df['salary'] > 125000][['name','department','salary']].sort_values(by = 'salary', ascending = False )


query = """ 

SELECT 
    name,
    salary
FROM 
    employees 
ORDER BY 
    salary DESC 
LIMIT 2 """


df_subset = df[['name','salary']].sort_values(by = 'salary', ascending = False).head(2)


query = """ 

SELECT DISTINCT 
    departments 
FROM 
    employees"""

df['departments'].unique()

df[['departments']].drop_duplicates()



SELECT 
    COUNT(DISTINCT employee_id)
FROM 
    employees 
WHERE
    departmnet = 'Engineering'

df[df['department']=='Engineering']['employee_id'].nunique()



query = """" 
SELECT 
    department,
    COUNT(DISTINCT employee_id)
FROM
    employees
GROUP BY 
    department 
"""

df_subset = df.groupby('department')['employee_id'].nunique()


query = """ 
SELECT 
    department,
    AVG(salary)
FROM 
    employees 
GROUP BY 
    department

"""

df[['department','salary']].groupby('department').agg({'salary':'mean'})

df.groupby('department').mean()


# MAX salary in each departmetn 


query = """
SELECT 
    department,
    MAX(salary) 
FROM 
    employees
GROUP BY 
    department"""

df.groupby('department').agg({'salary':'max'})


df.groupby('department')['salary'].max()


query = """ 
SELECT 
    department,
    MIN(salary)
FROM 
    employees
GROUP BY 
    department 
"""

df.groupby('department').agg({'salary':'min'})

df.groupby('department')['salary'].min()


query =
""" 
SELECT 
    department,
    AVG(salary) AS avg_salary,
    MAX(salary) AS max_salary,
    COUNT(DISTINCT employee_id)
FROM 
    employees
GROUP BY 
    department
"""



df.groupby('department').agg(
    avg_salary = ('salary','mean'),
    max_salary = ('salary', 'max'),
    unique_employees = ('employee_id','nunique')
)


query = """ 

SELECT 
    department,
    AVG(salary) AS avg_salary
FROM
    employees
GROUP BY 
    department
HAVING 
    AVG(salary) > 10000
"""


df_subset = (
    df.groupby('department')
    .agg(avg_salary = ('salary','mean'))
    .query('avg_salary > 100000')
)


query = """ 
SELECT 
    department,
    COUNT(DISTINCT employee_id)
FROM 
    employees
GROUP BY 
    department
HAVING 
    COUNT(DISTINCT employee_id) > 1


"""

df_subset = (
    df.groupby('department')
    .agg(unique_employees = ('employee_id','nunique'))
    .query('unique_employees > 1')
)