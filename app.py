import os

from bottle import route, run, request, static_file, view, response

from data import resources as db

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static')

@route('/new', method='POST')
def new():
    _body = request.json

    print(request)
    _data = db.add_resource({
        'name': _body['name'],
        'type': _body['type'],
        'priority': _body['priority']
    })
    response.status = 200
    return dict(message="OK")

# register
# release


@route('/release/<id>', method='GET')
def register(id):
    resource = db.get_resource({
        'id': id
    })
    db.set_resource(resource, {
        'is_occupied': 0
    })
    return 'OK'

@route('/register/<id>', method='GET')
def register(id):
    resource = db.get_resource({
        'id': id
    })
    db.set_resource(resource, {
        'is_occupied': 1
    })
    return 'OK'

@route('/new', method='GET')
@view('resource-editor')
def new():
    return {'search_tag': '', 'resources': ''}


@route('/resources')
@view('resources')
def index():
    resource = db.get_resources()
    return {'resources': resource}


@route('/')
@view('index')
def index():
    resources = db.get_resources()
    return {'resources': resources}


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
