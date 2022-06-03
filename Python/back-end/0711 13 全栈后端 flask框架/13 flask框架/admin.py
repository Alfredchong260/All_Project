from flask import Blueprint

admin_bp = Blueprint('admin', __name__)

sub_bp = Blueprint('sub', __name__)


@admin_bp.route('/admin/home')
def admin_home():
    return 'admin home'


@admin_bp.route('/admin/users')
def admin_users():
    return 'admin users'


@sub_bp.route('/sub')
def sub():
    return 'admin sub'


# admin_bp.register_blueprint(sub_bp)
sub_bp.register_blueprint(admin_bp)

