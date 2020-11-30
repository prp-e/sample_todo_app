# Backend design 

## /api/v1 endpoints 

1. `/api/v1` : Returns nothing 
2. `/api/v1/tasks` : Returns tasks of a user 
    1. `GET /api/v1/tasks` : Returns tasks for a user 
    2. `POST /api/v1/tasks` : Makes a new task 

## API authentication 

1. `/api/token` 
2. `/api/token/refresh` 