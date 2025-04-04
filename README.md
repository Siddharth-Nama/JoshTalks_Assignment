# 🚀 Task Management API - Django Backend Assignment

## 📌 Candidate Details
**👤 Name:** Siddharth Nama  
**🔗 GitHub:** [Siddharth-Nama](https://github.com/Siddharth-Nama)  
**💼 LinkedIn:** [linkedin.com/in/siddharth-nama](https://www.linkedin.com/in/siddharth-nama/)  
**📧 Email:** siddharthnama.work@gmail.com  
**📱 Phone:** +91 8000694996  
**📂 Assignment Repository:** [JoshTalks_Assignment](https://github.com/Siddharth-Nama/JoshTalks_Assignment)  

## 👨‍💻 About the Candidate
Siddharth Nama is a **tech enthusiast** and **full-stack developer** with expertise in **Django, REST APIs, React, and System Architecture**. Pursuing a **B.Tech in Computer Science at IIIT Bhagalpur (2022-2026)**, he specializes in building scalable and high-performance applications. With hands-on experience in **backend optimization, database design, and API development**, Siddharth is passionate about problem-solving and creating impactful software solutions.

---

## 💼 Experience
### 🎯 **Esaral Ventures Pvt. Ltd.** *(May 2024 – July 2024)*  
**Role:** Full-Stack Developer Intern  
✅ Built **3+ full-stack web and mobile applications** using **Django, React, React Native, and REST APIs**.  
✅ Enhanced backend services, reducing response time by **15%** and improving app responsiveness by **20%**.  
✅ Optimized database queries, increasing user engagement by **30%**.

### 🏗 **Mercato Agency** *(Jan 2024 - Feb 2024)*  
**Role:** Freelance Web Developer  
✅ Developed high-performance web solutions, serving **10,000+ users** and boosting site performance by **30%**.  
✅ Reduced page load times by **40%**, improving cross-platform compatibility.

---

## 🛠 Tech Stack & Skills
🔹 **Languages:** Python, C++, JavaScript, C  
🔹 **Developer Tools:** VS Code, Git, GitHub, Postman  
🔹 **Frameworks:** Django, React.js, React Native, Bootstrap, Tailwind CSS  
🔹 **Databases:** SQLite, PostgreSQL  
🔹 **Core Concepts:** Data Structures & Algorithms, OOPS, DBMS  
🔹 **Specialization:** Full-Stack Development, System Design, Competitive Programming  

---

## 📜 Project Overview
This **Task Management API** allows users to **create, assign, and retrieve tasks** efficiently. Developed using **Django and Django REST Framework (DRF)**, it ensures a **scalable and robust task management system**.

---

## ⚡ Features & API Endpoints
### 🔹 1. Task Creation API
**🔗 Endpoint:** `POST /api/tasks/`  
**📝 Description:** Creates a new task with a name and description.  
📤 **Request Body:**
```json
{
    "name": "Task Name",
    "description": "Task Description",
    "task_type": "general"
}
```
📥 **Response:**
```json
{
    "id": 1,
    "name": "Task Name",
    "description": "Task Description",
    "created_at": "2024-03-25T12:00:00Z",
    "task_type": "general",
    "status": "pending"
}
```

### 🔹 2. Assign Task to Users API
**🔗 Endpoint:** `POST /api/tasks/assign/`  
**📝 Description:** Assigns a task to one or multiple users.  
📤 **Request Body:**
```json
{
    "task_id": 1,
    "user_ids": [2, 3]
}
```
📥 **Response:**
```json
{
    "message": "Task assigned successfully"
}
```

### 🔹 3. Fetch Tasks Assigned to a Specific User
**🔗 Endpoint:** `GET /api/users/{user_id}/tasks/`  
**📝 Description:** Retrieves all tasks assigned to a particular user.  
📥 **Response:**
```json
[
    {
        "id": 1,
        "name": "Task Name",
        "description": "Task Description",
        "created_at": "2024-03-25T12:00:00Z",
        "status": "pending"
    }
]
```

---

## 🔄 Project Workflow
1️⃣ **User Registration (If Needed):** Users can be manually added or authenticated.  
2️⃣ **Task Creation:** Tasks are created via API.  
3️⃣ **Assigning Tasks:** Tasks are assigned to users.  
4️⃣ **Fetching Tasks:** Users can retrieve assigned tasks.  

---

## 🏗 Project Specifications
✅ **Framework:** Django, Django REST Framework (DRF)  
✅ **Database:** PostgreSQL / SQLite  
✅ **Authentication:** Basic Authentication or JWT (if implemented)  
✅ **Serialization:** DRF Serializers  
✅ **Validation:** Strong input validation  
✅ **Error Handling:** Custom error messages & status codes  

---

## ⚙ Installation & Setup
1️⃣ **Clone the Repository:**
```bash
git clone https://github.com/Siddharth-Nama/JoshTalks_Assignment.git
cd JoshTalks_Assignment
```
2️⃣ **Create & Activate Virtual Environment:**
```bash
python -m venv env
source env/bin/activate  # Mac/Linux
env\Scripts\activate  # Windows
```
3️⃣ **Install Dependencies:**
```bash
pip install -r requirements.txt
```
4️⃣ **Run Migrations:**
```bash
python manage.py migrate
```
5️⃣ **Start the Server:**
```bash
python manage.py runserver
```

---

## 🛠 API Testing
Use **Postman** or **cURL** to test API endpoints.

---

## 📦 Deliverables
📂 A well-structured GitHub repository.  
📜 Comprehensive README documentation.  
✅ Sample API requests & responses.  

---

## 📞 Contact
For any queries, feel free to reach out:  
📧 **Email:** siddharthnama.work@gmail.com  
📱 **Phone:** +91 8000694996  
🔗 **GitHub:** [Siddharth-Nama](https://github.com/Siddharth-Nama)  
💼 **LinkedIn:** [Siddharth Nama](https://www.linkedin.com/in/siddharth-nama/)  

---
🚀 **Thank you for reviewing my assignment!**

