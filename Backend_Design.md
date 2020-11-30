# Backend design 

## /api/v1 endpoints 

1. `/api/v1` : Returns nothing 
2. `/api/v1/tasks` : Returns tasks of a user 
    1. `GET /api/v1/tasks` : Returns tasks for a user 
    2. `POST /api/v1/tasks` : Makes a new task 

## API authentication 

1. `/api/token` 
2. `/api/token/refresh` 

## Task Model 

1. `name` : The name of our task 
2. `summary`/`description` : What will I do? 
3. `start_date` : The date you're going to start the task. 
4. `deadline` : The day you need the task to be finished. 