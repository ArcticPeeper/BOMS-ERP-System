# Business Operations Management System (BOMS)
## ERP Simulation Platform

**BOMS** is an enterprise-grade Business Operations Management System built as an ERP simulation platform designed to manage core business workflows including user management, inventory tracking, sales transactions, and financial reporting.

---

## 📋 Project Overview

BOMS is a complete ERP system that demonstrates:
- **Business Process Automation**: Automated stock management and sales workflows
- **Role-Based Access Control**: Admin and Staff user roles
- **Real-Time Dashboard**: Sales metrics and inventory insights
- **Database Integrity**: Relational database with transaction logging
- **RESTful API Architecture**: Modern backend API design

---

## 🧩 Core ERP Modules

### 📦 Module 1: User Management
- User registration and authentication
- Secure login system with role-based access
- User roles: Admin, Staff
- Session management

### 📦 Module 2: Inventory System
- Add, update, and delete products
- Real-time stock tracking
- Low stock alerts
- Product categorization

### 📦 Module 3: Sales System
- Create sales transactions
- Automatic stock reduction on sale
- Sales history tracking
- Invoice generation

### 📦 Module 4: Reporting Dashboard
- Total sales metrics
- Available stock overview
- Revenue summary
- Sales trends and analytics

### 📦 Module 5: Basic Finance Logic
- Total revenue calculation
- Sales count tracking
- Profit estimation
- Financial reports

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────┐
│                  FRONTEND                        │
│         (HTML/CSS/JavaScript/Bootstrap)         │
│                                                 │
│  ┌─────────────────────────────────────────┐   │
│  │  Dashboard | Inventory | Sales | Users  │   │
│  └─────────────────────────────────────────┘   │
└────────────────┬────────────────────────────────┘
                 │ (AJAX/REST API Calls)
                 ▼
┌─────────────────────────────────────────────────┐
│              BACKEND (Flask)                    │
│                                                 │
│  ┌──────────────────────────────────────────┐  │
│  │  API Routes & Business Logic             │  │
│  │  • Authentication                        │  │
│  │  • Inventory Management                  │  │
│  │  • Sales Processing                      │  │
│  │  • Reporting & Analytics                 │  │
│  └──────────────────────────────────────────┘  │
└────────────────┬────────────────────────────────┘
                 │ (SQLAlchemy ORM)
                 ▼
┌─────────────────────────────────────────────────┐
│            DATABASE (PostgreSQL)                │
│                                                 │
│  ┌──────────────────────────────────────────┐  │
│  │  • users (Authentication & Roles)        │  │
│  │  • products (Inventory)                  │  │
│  │  • sales (Transactions)                  │  │
│  │  • financial_records (Reports)           │  │
│  └──────────────────────────────────────────┘  │
└─────────────────────────────────────────────────┘
```

---

## 💾 Database Schema

### Users Table
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL,  -- 'admin' or 'staff'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Products Table
```sql
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 0,
    category VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Sales Table
```sql
CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    staff_id INT,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (staff_id) REFERENCES users(id)
);
```

### Financial Records Table
```sql
CREATE TABLE financial_records (
    id SERIAL PRIMARY KEY,
    total_revenue DECIMAL(15, 2),
    total_sales_count INT,
    profit_estimate DECIMAL(15, 2),
    report_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🔌 API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout

### User Management
- `GET /api/users` - List all users (Admin only)
- `GET /api/users/<id>` - Get user details
- `PUT /api/users/<id>` - Update user
- `DELETE /api/users/<id>` - Delete user (Admin only)

### Inventory Management
- `GET /api/products` - List all products
- `POST /api/products` - Create new product (Admin/Staff)
- `PUT /api/products/<id>` - Update product
- `DELETE /api/products/<id>` - Delete product (Admin only)
- `GET /api/products/<id>/stock` - Get product stock level

### Sales Management
- `GET /api/sales` - List all sales
- `POST /api/sales` - Create new sale (Auto-reduces stock)
- `GET /api/sales/<id>` - Get sale details
- `GET /api/sales/history` - Get sales history

### Reporting & Dashboard
- `GET /api/dashboard` - Get dashboard metrics
- `GET /api/reports/revenue` - Revenue report
- `GET /api/reports/inventory` - Inventory report
- `GET /api/reports/sales-trends` - Sales trends

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | HTML5, CSS3, JavaScript, Bootstrap 5 |
| **Backend** | Python 3.9+, Flask 2.0+ |
| **Database** | PostgreSQL 12+ (or SQLite for development) |
| **ORM** | SQLAlchemy |
| **Authentication** | Flask-Login, Werkzeug |
| **API** | Flask-RESTful |
| **Containerization** | Docker (Optional) |

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.9+
- PostgreSQL 12+ (or SQLite)
- Git

### Step 1: Clone Repository
```bash
git clone https://github.com/ArcticPeeper/BOMS-ERP-System.git
cd BOMS-ERP-System
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Database
Edit `config.py` with your database credentials:
```python
DATABASE_URL = 'postgresql://user:password@localhost:5432/boms_db'
```

### Step 5: Initialize Database
```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

### Step 6: Run Application
```bash
python app.py
```
Access at: `http://localhost:5000`

---

## 🔄 System Workflow Example

```
1. USER LOGIN
   └─ Staff member logs in
   └─ System validates credentials
   └─ Session created with role permissions

2. INVENTORY MANAGEMENT
   └─ Staff adds new product: "Widget A" (Price: $50, Stock: 100)
   └─ Product stored in database
   └─ Dashboard shows new inventory

3. SALES TRANSACTION
   └─ Customer purchases 5x Widget A
   └─ Staff creates sales record
   └─ System automatically:
      ├─ Reduces stock (100 → 95)
      ├─ Calculates total ($250)
      ├─ Logs transaction
      └─ Updates financial metrics

4. DASHBOARD UPDATE
   └─ Dashboard shows:
      ├─ Total Revenue: $250
      ├─ Sales Count: 1
      ├─ Available Stock: 95 units
      └─ Profit Estimate: $150 (assuming 40% margin)
```

---

## 📊 Features Highlight

✅ **Business Logic Automation**
- Automatic stock reduction on sales
- Real-time revenue calculation
- Transaction logging

✅ **Enterprise Security**
- Password hashing with Werkzeug
- Session-based authentication
- Role-based access control

✅ **Data Integrity**
- Relational database with foreign keys
- ACID-compliant transactions
- Audit trail for all operations

✅ **API-First Design**
- RESTful API endpoints
- JSON request/response
- Easy frontend integration

✅ **Scalability**
- Modular Flask blueprint structure
- Database connection pooling
- Prepared statements for SQL injection prevention

---

## 🚀 Deployment

### Docker Deployment
```bash
docker-compose up -d
```

### Production Checklist
- [ ] Set `FLASK_ENV = production`
- [ ] Configure strong `SECRET_KEY`
- [ ] Enable HTTPS
- [ ] Set up database backups
- [ ] Configure environment variables
- [ ] Enable logging and monitoring

---

## 📚 Project Structure
```
BOMS-ERP-System/
├── app.py                 # Flask application entry point
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── database.sql           # Database schema
├── docker-compose.yml     # Docker configuration
│
├── backend/
│   ├── __init__.py
│   ├── models.py          # Database models
│   ├── routes/
│   │   ├── auth.py        # Authentication routes
│   │   ├── inventory.py   # Inventory management
│   │   ├── sales.py       # Sales transactions
│   │   └── reports.py     # Reporting & dashboard
│   └── utils.py           # Utility functions
│
├── frontend/
│   ├── index.html         # Dashboard
│   ├── login.html         # Login page
│   ├── inventory.html     # Inventory management
│   ├── sales.html         # Sales transactions
│   ├── css/
│   │   └── style.css      # Styling
│   └── js/
│       ├── auth.js        # Authentication logic
│       ├── inventory.js   # Inventory functions
│       ├── sales.js       # Sales functions
│       └── dashboard.js   # Dashboard updates
│
└── tests/
    ├── test_auth.py
    ├── test_inventory.py
    └── test_sales.py
```

---

## 🧪 Testing

```bash
pytest tests/ -v
```

---

## 📝 License

MIT License - See LICENSE file for details

---

## 👤 Author

**ArcticPeeper**

---

## 🤝 Contributing

Contributions are welcome! Please follow the standard GitHub fork and pull request workflow.

---

## 📞 Support

For issues or questions, please open a GitHub issue.
