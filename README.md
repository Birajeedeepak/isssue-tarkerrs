Path: E:\Project06\README.md (This file should be in the root directory of your project, alongside the backend and frontend folders).

Action: Create this file and add the content below.

Markdown

# 🚀 Modern Issue Tracker
A full-stack, feature-rich issue tracking application built with a Python (Flask) backend and an Angular frontend. This project demonstrates a clean architecture, a modern UI, and a comprehensive set of features for managing development tasks effectively.

![Issue Tracker Screenshot](https://i.imgur.com/g0P2g77.png)  <!-- You can replace this link with your own screenshot if you upload it -->

---

## ✨ Key Features

* **📄 Create, Read, Update**: Full CRUD functionality for managing issues.
* **🔍 Live Search**: Instantly find issues by title with a responsive search bar.
* **🚦 Dynamic Filtering**: Filter issues by their `status`, `priority`, or `assignee`.
* **🔃 Column Sorting**: Sort the issue list by any key metric (`status`, `priority`, `updatedAt`, etc.).
* **📖 Pagination**: Efficiently navigate through a large number of issues with page controls and adjustable page sizes.
* **🎨 Modern & Responsive UI**: A clean, intuitive, and visually appealing interface built for a great user experience.
* **✅ Robust Backend API**: A well-structured REST API serves all data and handles business logic.

---

## 🛠️ Technology Stack

| Backend                               | Frontend                               |
| ------------------------------------- | -------------------------------------- |
| **Python 3** | **TypeScript** |
| **Flask** (for the REST API)          | **Angular 17+** (Standalone Components)|
| **Flask-CORS** (for cross-origin requests) | **Angular CLI** |
| In-Memory Data Store (for simplicity) | **HTML5** & **CSS3** |

---

## 🏁 Getting Started
Follow these instructions to set up and run the project on your local machine.
### Prerequisites

* **Python 3.8+**
* **Node.js 18+** and **npm**
* **Angular CLI** (`npm install -g @angular/cli`)

### 1. Backend Setup

First, set up and run the Python Flask server.

```bash
# 1. Navigate to the backend directory
cd backend

# 2. Create and activate a virtual environment
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
# source venv/bin/activate

# 3. Install the required packages
pip install -r requirements.txt

# 4. Run the server
python app.py
✅ The backend API is now running at http://127.0.0.1:5000 and provides the following key endpoints:

/health: For checking the server status.

/issues: For fetching and managing all issue data.




2. Frontend Setup
In a new, separate terminal, set up and run the Angular application.

Bash

# 1. Navigate to the frontend directory
cd frontend

# 2. Install npm packages
npm install

# 3. Run the development server
ng serve
✅ The frontend application will be available at http://localhost:4200.

🔌 API Endpoints
The backend provides the following RESTful API endpoints:

Method	Endpoint	Description
GET	/health	Health check endpoint. Returns {"status": "ok"}.
GET	/issues	Retrieves a list of issues. Supports search, filtering, sorting, and pagination via query parameters.
GET	/issues/:id	Retrieves a single issue by its unique ID.
POST	/issues	Creates a new issue. The backend auto-generates id, createdAt, and updatedAt.
PUT	/issues/:id	Updates an existing issue. The updatedAt field is refreshed.