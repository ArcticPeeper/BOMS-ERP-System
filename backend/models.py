"""
Database Models for BOMS ERP System
"""

from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    """
    User model - Handles authentication and user roles
    Roles: 'admin', 'staff'
    """
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), default='staff', nullable=False)  # 'admin' or 'staff'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    sales = db.relationship('Sale', backref='staff', lazy=True)
    
    def set_password(self, password):
        """Hash and set password"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Verify password"""
        return check_password_hash(self.password_hash, password)
    
    def is_admin(self):
        """Check if user is admin"""
        return self.role == 'admin'
    
    def __repr__(self):
        return f'<User {self.name} ({self.role})>'


class Product(db.Model):
    """
    Product model - Handles inventory items
    """
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, default=0, nullable=False)
    category = db.Column(db.String(50))
    description = db.Column(db.Text)
    sku = db.Column(db.String(50), unique=True)  # Stock Keeping Unit
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    sales = db.relationship('Sale', backref='product', lazy=True, cascade='all, delete-orphan')
    
    def reduce_stock(self, quantity):
        """Reduce stock and return success status"""
        if self.stock_quantity >= quantity:
            self.stock_quantity -= quantity
            db.session.commit()
            return True
        return False
    
    def increase_stock(self, quantity):
        """Increase stock"""
        self.stock_quantity += quantity
        db.session.commit()
        return True
    
    def is_low_stock(self, threshold=10):
        """Check if stock is below threshold"""
        return self.stock_quantity <= threshold
    
    def __repr__(self):
        return f'<Product {self.name} (Stock: {self.stock_quantity})>'


class Sale(db.Model):
    """
    Sale model - Handles sales transactions
    Automatically reduces stock when sale is created
    """
    __tablename__ = 'sales'
    
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    sale_date = db.Column(db.DateTime, default=datetime.utcnow)
    staff_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    notes = db.Column(db.Text)
    
    def __repr__(self):
        return f'<Sale #{self.id} - {self.quantity}x {self.product.name} for ${self.total_price}>'


class FinancialRecord(db.Model):
    """
    Financial Record model - Stores financial metrics
    """
    __tablename__ = 'financial_records'
    
    id = db.Column(db.Integer, primary_key=True)
    total_revenue = db.Column(db.Float, default=0.0)
    total_sales_count = db.Column(db.Integer, default=0)
    profit_estimate = db.Column(db.Float, default=0.0)
    report_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<FinancialRecord - Revenue: ${self.total_revenue}, Sales: {self.total_sales_count}>'
