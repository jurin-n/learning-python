from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

resource = Blueprint('sample_page', __name__,
                        template_folder='templates',
                        url_prefix='/sample')

@resource.route('/', defaults={'page': 'index'})
@resource.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)


@resource.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html')