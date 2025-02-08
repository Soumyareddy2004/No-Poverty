# No Poverty - AI-Driven Poverty Eradication Platform

## Overview
**No Poverty** is an AI-driven platform that identifies and addresses poverty-prone areas by analyzing real-time data, satellite imagery, and socio-economic indicators. It bridges the gap by connecting people with nearby NGOs, government welfare programs, and job opportunities. The platform offers real-time eligibility checks and step-by-step guidance for accessing aid. By leveraging AI and APIs like Gemini, **No Poverty** ensures that resources are directed efficiently, empowering communities and driving impactful, data-driven poverty eradication efforts.

## Key Features
### 🔍 AI-Powered Poverty Prediction
- Utilizes real-time data, satellite imagery, and socio-economic indicators to identify and predict poverty-prone areas with high accuracy.

### 🎯 Personalized Job & Welfare Recommendations
- AI-driven suggestions connect individuals with employment opportunities, skill-building programs, and government welfare schemes based on their socio-economic profile.

### 🌍 Integration with NGOs & Government Programs
- Seamlessly links users to nearby NGOs, community resources, and social welfare programs, ensuring targeted assistance.

### 🤝 Community Engagement for Donations & Volunteering
- Provides a platform for donors, volunteers, and organizations to contribute directly through financial aid, resource distribution, and skill-based volunteering.

### 🛠️ AI Chatbot for 24/7 Assistance
- Offers multi-language support to guide users in finding job opportunities, accessing welfare programs, and resolving queries about poverty relief initiatives.

### 📊 Automated Report Generation & Insights
- AI-powered analytics generate detailed reports highlighting key poverty trends, challenges, and actionable recommendations for governments and NGOs.

### 🔗 Dual Data Integration for Accuracy
- Combines satellite imagery and census data to provide comprehensive, real-time insights into poverty-stricken areas.

### 💡 User-Friendly Interface
- Designed for easy access to critical information, enabling individuals, NGOs, and policymakers to navigate the platform efficiently and take informed action.

---

## 🚀 How to Clone and Run This Project

### Prerequisites
Ensure you have the following installed:
- Python (3.8+)
- Git
- Virtual Environment (venv)
- PostgreSQL or SQLite (for database management)

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Soumyareddy2004/No-Poverty.git
cd No-Poverty
```

### 2️⃣ Set Up a Virtual Environment
```sh
python -m venv poverty_env
source poverty_env/bin/activate  # On Windows use: poverty_env\Scripts\activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file in the root directory and add:
```env
SECRET_KEY=your_secret_key_here
DATABASE_URL=your_database_url_here
DEBUG=True
```

### 5️⃣ Apply Database Migrations
```sh
python manage.py migrate
```

### 6️⃣ Run the Development Server
```sh
python manage.py runserver
```

The project will now be available at `http://127.0.0.1:8000/`

### 7️⃣ (Optional) Create a Superuser for Admin Access
```sh
python manage.py createsuperuser
```
Follow the prompts to set up an admin account.

---

## 📢 Contribution Guidelines
1. Fork the repository and create a new branch.
2. Commit your changes with meaningful commit messages.
3. Push your branch and submit a pull request.

For any questions, feel free to raise an issue or contribute to discussions.

---

## 📞 Contact
For any queries or suggestions, reach out at:
📧 Email: sowmyareddy1911@gmail.com](mailto:sowmyareddy1911@gmail.com)  
🌐 GitHub: [Soumyareddy2004](https://github.com/Soumyareddy2004)

