# # task sql table (
#     id integer
#     name varchar(255) not null
#     unique (id)
#  )

# reports (
#     id integer
#     task_id integer not null
#     candidate varchar(255) not null
#     score integer not null
#     unique (id)

# )

for x in task:
    task_id = x[0]
    task_name = x[1]
    avg_score = 0
    count = 0
    for y in reports:
        if y[1] == task_id:
            avg_score += y[3]
            count += 1
    avg_score = avg_score/count
    if(avg_score <= 20):
        task_difficulty = "Hard"
    elif(avg_score <= 60):
        task_difficulty = "Medium"
    else:
        task_difficulty = "Easy"

    table = [task_id, task_name, task_difficulty]            

    
SELECT t.id, t.name, 
        CASE 
            WHEN AVG(r.score) <= 20 THEN 'Hard'
            WHEN AVG(r.score) <= 60 THEN 'Medium'
            ELSE 'Easy'
        END AS task_difficulty
    FROM task t
    JOIN reports r ON t.id = r.task_id
    GROUP BY t.id, t.name;
