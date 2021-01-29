from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)

# 404: Page not found
@errors.app_errorhandler(404)
def error_404(error):
	return render_template('errors/404.html'), 404

# 403: No Appropriate permissions
@errors.app_errorhandler(403)
def error_403(error):
	return render_template('errors/403.html'), 403

# 500: Server error
@errors.app_errorhandler(500)
def error_500(error):
	return render_template('errors/500.html'), 500

