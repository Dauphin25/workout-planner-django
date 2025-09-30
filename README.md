# Workout Planner Django API

This is a RESTful API for a **Personalized Workout Planner** system.  
Before implementing the database and Django models, I started with a **conceptual design phase**.  
This helps ensure the relationships between entities are clear before moving to code.  

Below, I describe the relationships in **plain sentences**.  
- **Entities (models)** are **underlined**.  
- **Relationships** are 🔗 **highlighted** in words.  
- Each sentence also hints at the **relationship type** (One-to-Many, Many-to-Many, etc.).  

---

## 📌 Conceptual Relationships

1. A __User__ can register, log in, and log out.  
2. A __User__ 🔗 can create multiple __Workout Plans__ (**One-to-Many**).  
3. A __Workout Plan__ 🔗 belongs to exactly one __User__ (**Many-to-One**).  
4. A __Workout Plan__ 🔗 consists of multiple __Workout Sessions__ (**One-to-Many**).  
5. Each __Workout Session__ 🔗 can include multiple __Exercises__ (**Many-to-Many**).  
6. An __Exercise__ is predefined in the database (description, target muscles, instructions).  
7. A __Workout Session Exercise__ 🔗 customizes a predefined __Exercise__ by adding sets, reps, duration, or distance.  
8. A __User__ 🔗 can track multiple __Progress Records__ (**One-to-Many**).  
9. A __User__ 🔗 can set multiple __Fitness Goals__ (**One-to-Many**).  
10. A __Goal__ 🔗 belongs to one __User__ (**Many-to-One**).  
11. A __Workout Plan__ has fields for **frequency** (e.g., 3x/week) and **daily duration**.  
12. A __Workout Plan__ can target different **goal types** (strength, endurance, weight loss).  
13. A __Workout Session__ has a **date** field for when it was performed.  
14. A __Workout Session Exercise__ can be marked as **completed** or **skipped**.  
15. A __User__ 🔗 can view and manage all of their __Workout Plans__, __Goals__, and __Progress Records__.  

---

## 📌 Next Steps

1. Convert these sentences into an **EER diagram** (Entity-Relationship Diagram).  
2. Use this diagram to implement **Django models**.  
3. Implement **REST API endpoints** for CRUD operations on these models.  
