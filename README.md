# Workout Planner Django API

---

## 📖 Project Overview

This project is a RESTful API for a **Personalized Workout Planner** system.  
It enables users to create and manage customized workout plans, track fitness goals, and monitor progress.  
Key features include secure authentication, a rich database of exercises, goal tracking, achievements, and guided workout sessions.

## 🧪 Test Credentials 

Use the following credentials and token for API testing:

- **Username:** `trainer`
- **Email:** `trainer@gmail.com`
- **Refresh Token:**  
  ```
  eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc2NTQ0Nzk0MSwiaWF0IjoxNzU5Mzk5OTQxLCJqdGkiOiIyY2RmNzM3YjlhZTE0NjYwODgyNDkyMWI0YWE4MDE4ZSIsInVzZXJfaWQiOiI2In0.JY8-3FcnDAdjT5esETA0dGV78jDCSlOauodF-iopNOg
  ```

You can use this token for testing JWT authentication endpoints and user-specific API features.

### Core Features

- **User Authentication:** Secure registration, login, and logout using JWT.
- **Predefined Exercises Database:** 20+ diverse exercises with details and muscle targeting.
- **Personalized Workout Plans:** Users create and customize plans, select exercises, and set session details.
- **Tracking & Goals:** Weight logs, goal tracking, and achievement recording.
- **API Documentation:** Swagger and Redoc for easy endpoint testing.
- **Bonus:** Guided workout mode.

---

## 📌 Conceptual Relationships

- A __User__ can register, log in, and log out.
- A __User__ 🔗 can create multiple __Workout Plans__ (**One-to-Many**).
- A __User__ 🔗 has one __Profile__ (**One-to-One**).
- A __User__ 🔗 can track multiple __Progress Records__ (**One-to-Many**).
- A __User__ 🔗 can set multiple __Fitness Goals__ (**One-to-Many**).
- A __Workout Plan__ 🔗 contains multiple __Workout Weeks__ (**One-to-Many**).
- A __Workout Week__ 🔗 contains multiple __Workout Days__ (**One-to-Many**).
- A __Workout Day__ 🔗 contains multiple __Workout Exercises__ (**One-to-Many**).
- A __Workout Exercise__ 🔗 references an __Exercise__.



```mermaid
erDiagram
    USER ||--|| PROFILE : "has"
    USER ||--o{ WORKOUT_PLAN : "creates"
    USER ||--o{ PROGRESS_RECORD : "tracks"
    USER ||--o{ GOAL : "sets"
    WORKOUT_PLAN ||--o{ WORKOUT_WEEK : "contains"
    WORKOUT_WEEK ||--o{ WORKOUT_DAY : "contains"
    WORKOUT_DAY ||--o{ WORKOUT_EXERCISE : "contains"
    WORKOUT_EXERCISE }o--|| EXERCISE : "references"
    PROFILE {
        int id PK
        int user_id FK
        float weight
        float height
        string lifestyle
        int age
        string gender
        string bio
        string dietary_preference
    }
    USER {
        int id PK
        string email
        string username
        string first_name
        string last_name
        string phone_number
        string city
        date date_of_birth
        datetime registration_date
        string password
    }
    WORKOUT_PLAN {
        int id PK
        int user_id FK
        string title
        string description
        int frequency_per_week
        int daily_session_duration
        int goal_id FK
        string difficulty
        date start_date
        date end_date
        decimal progress
        bool is_active
        datetime created_at
        datetime updated_at
    }
    WORKOUT_WEEK {
        int id PK
        int workout_plan_id FK
        int week_number
        date start_date
        date end_date
        decimal progress
        bool is_active
        datetime created_at
        datetime updated_at
    }
    WORKOUT_DAY {
        int id PK
        int workout_week_id FK
        string day_of_week
        int order
        string focus_area
        string notes
        bool is_rest_day
        decimal session_rating
        int calories_burned
        datetime created_at
        datetime updated_at
    }
    WORKOUT_EXERCISE {
        int id PK
        int workout_day_id FK
        int exercise_id FK
        int sets
        int repetitions
        int duration_seconds
        int distance_meters
        int rest_seconds
        string notes
        int order
        string intensity
        string tempo
        bool completed
        string feedback
    }
    GOAL {
        int id PK
        string name
        string description
        string goal_type
        int recommended_duration_weeks
        string status
        string feedback
        datetime created_at
        datetime updated_at
    }
    EXERCISE {
        int id PK
        string name
        string description
        string instructions
        string equipment
        string difficulty
        string exercise_type
        int calories_burned
        int duration
        string tips
        datetime created_at
        datetime updated_at
    }
    MUSCLE {
        int id PK
        string name
        string group
        string description
        string origin
        string insertion
        string function
    }
    EXERCISE }o--o{ MUSCLE : "targets"
```


## 🗄️ Database Seeding

- The initial set of 20+ predefined exercises is provided in JSON files located in the `exercises/fixtures/exercises.json` folder.
- Muscle groups are seeded from `exercises/fixtures/muscles.json`.
- You can populate the database with workout plans, workout weeks, workout days, workout exercises, and goals using the JSON files in `workout_plan/fixtures/`:
  - `workout_plans.json`
  - `workout_days.json`
  - `workout_exercises.json`
  - `goals.json`
- To populate the database, use:
  ```bash
  python manage.py loaddata exercises/fixtures/exercises.json
  python manage.py loaddata exercises/fixtures/muscles.json
  python manage.py loaddata workout_plan/fixtures/goals.json
  python manage.py loaddata workout_plan/fixtures/workout_plans.json
  python manage.py loaddata workout_plan/fixtures/workout_days.json
  python manage.py loaddata workout_plan/fixtures/workout_exercises.json
  ```
- You can customize or extend these seed files as needed.

---

## 🔐 API Authentication

- All sensitive endpoints require JWT authentication.
- Obtain tokens via `/api/users/login/` or `/api/token/`.
- Include the access token in the `Authorization` header:
  ```
  Authorization: Bearer <your_access_token>
  ```
- Endpoints for token management:
  - `/api/token/` – Obtain token pair.
  - `/api/token/refresh/` – Refresh token.
  - `/api/token/verify/` – Verify token.

---


## 📄 API Documentation

- **Swagger UI:** [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- **Redoc UI:** [http://localhost:8000/redoc/](http://localhost:8000/redoc/)
- **OpenAPI Schema:** [http://localhost:8000/swagger.json](http://localhost:8000/swagger.json)

---

## 📌 API Endpoint Overview

### User Endpoints (`users/urls.py`)
- `/api/users/register/` – Register a new user.
- `/api/users/login/` – Obtain JWT tokens for authentication.
- `/api/users/logout/` – Logout and blacklist refresh token.

### Profile Endpoints
- `/api/profiles/` – Manage user profile (weight, height, lifestyle, etc.).

### Exercise & Muscle Endpoints (`exercises/urls.py`)
- `/api/exercises/` – List, create, update, delete, and search exercises.
- `/api/muscles/` – List and retrieve muscle groups and details.

### Workout Plan Endpoints (`workout_plan/urls.py`)
- `/api/plans/` – CRUD for workout plans.
- `/api/weeks/` – CRUD for workout weeks within a plan.
- `/api/workout-days/` – CRUD for workout days within a week.
- `/api/workout-exercises/` – CRUD for exercises within a workout day.

### Tracking & Achievements Endpoints (`tracking/urls.py`)
- `/api/weight-logs/` – Track and manage user's weight history.
- `/api/goal-trackings/` – Track progress toward specific fitness goals.
- `/api/achievements/` – Record exercise achievements and milestones.

### JWT Authentication Endpoints
- `/api/token/` – Obtain JWT token pair.
- `/api/token/refresh/` – Refresh JWT token.
- `/api/token/verify/` – Verify JWT token.

### API Documentation
- `/swagger/` – Swagger UI.
- `/redoc/` – Redoc UI.
- `/swagger.json` – OpenAPI schema.

---


---

## 📌 Exercise Endpoints

- `/api/exercises/` – List, create, update, delete, and search exercises.
    - Supports filtering by: `difficulty`, `exercise_type`, `equipment`, `target_muscles`.
    - Supports searching by: `name`, `description`, `equipment`, `instructions`, `tips`.
    - Supports ordering by: `name`, `difficulty`, `exercise_type`, `created_at`.
    - List endpoint returns a concise summary; detail endpoint returns full info.
- `/api/muscles/` – List and retrieve muscle groups and details.

**Permissions:**  
- Listing and retrieving exercises/muscles is open (`AllowAny`).
- Creating, updating, and deleting exercises requires authentication (`IsAuthenticated`).

---

## 📌 Workout Plan Endpoints

- `/api/workout-plans/` – CRUD for workout plans (title, description, frequency, goal, etc.).
    - Only authenticated users can access and manage their own plans.
- `/api/weeks/` – CRUD for workout weeks within a plan.
    - Each week is linked to a workout plan and has a number, start date, end date, progress, and activity status.
- `/api/workout-days/` – CRUD for workout days within a week.
    - Each day is unique per week and includes focus area, notes, session rating, calories burned, etc.
- `/api/workout-exercises/` – CRUD for exercises within a workout day.
    - Each exercise is linked to a workout day and references an exercise.
    - Includes sets, reps, duration, rest, intensity, tempo, completion, feedback.

**Permissions:**  
- All workout plan/week/day/exercise endpoints require authentication (`IsAuthenticated`).
- Users only see and manage their own plans, weeks, days, and exercises.

---

## 📌 Goal Endpoints

- `/api/goals/` – CRUD for fitness goals (weight loss, muscle gain, etc.).
    - Each goal has a name, type, description, duration, status, and feedback.

---

## 📌 Tracking & Achievements Endpoints

### Weight Log

- `/api/weight-logs/` – Track and manage user's weight history.
    - Fields: `weight_kg`, `bmi`, `body_fat_percent`, `logged_at`, `notes`.
    - Supports searching by `notes` and ordering by `logged_at`, `weight_kg`, `bmi`.
    - Only authenticated users can access their own logs.

### Goal Tracking

- `/api/goal-trackings/` – Track progress toward specific fitness goals.
    - Fields: `goal`, `target_value`, `current_value`, `starting_weight`, `ending_weight`, `progress_percent`, `notes`, `is_achieved`, `started_at`, `achieved_at`.
    - Supports searching by `notes` and ordering by `started_at`, `progress_percent`.
    - Only authenticated users can access their own goal tracking records.

### Achievement

- `/api/achievements/` – Record exercise achievements and milestones.
    - Fields: `exercise`, `description`, `value`, `achieved_at`, `notes`.
    - Supports searching by `description`, `notes` and ordering by `achieved_at`, `value`.
    - Only authenticated users can access their own achievements.

**Permissions:**  
- All tracking and achievement endpoints require authentication (`IsAuthenticated`).
- Users only see and manage their own records.

---

## 🏋️ Guided Workout Mode (Bonus Feature)

- Real-time workout guidance: next exercise, sets, reps, rest periods.
- Users can mark exercises as complete and note adjustments.
- Accessible via `/api/workout-mode/` (see API docs for details).

---

## 🚀 Docker Setup

1. Build and start the containers:
   ```bash
   docker-compose up --build
   ```
2. The Django app will be available at [http://localhost:8000](http://localhost:8000).
3. The PostgreSQL database will be available at port 5432.

**Environment variables** are managed in the `.env` file.

To run migrations and seed data:
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py loaddata <your-fixture>.json
```
