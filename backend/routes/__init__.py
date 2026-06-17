"""
Routes Module - Blueprint definitions for BOMS
"""

from flask import Blueprint

# Define blueprints
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
inventory_bp = Blueprint('inventory', __name__, url_prefix='/inventory')
sales_bp = Blueprint('sales', __name__, url_prefix='/sales')
reports_bp = Blueprint('reports', __name__, url_prefix='/reports')
api_bp = Blueprint('api', __name__, url_prefix='/api')

# Import route handlers (avoid circular imports)
from backend.routes import auth, inventory, sales, reports, api_routes
