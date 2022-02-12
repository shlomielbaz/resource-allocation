from bottle import route, run, request, static_file, view, response
from data import resources as db


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static')


@route('/new', method='POST')
def new():
    _body = request.json

    _data = db.add_resource({
        'name': _body['name'],
        'type': _body['type'],
        'priority': _body['priority']
    })
    response.status = 200
    return dict(message="OK")


@route('/new', method='GET')
@view('resource-editor')
def new():
    return {'search_tag': '', 'resource': None}


@route('/edit/<id>', method='PUT')
def edit(id: int):
    _body = request.json

    resource = db.get_resource({
        'id': id
    })

    db.set_resource(resource, _body)

    response.status = 200
    return dict(message="OK")


@route('/edit/<id>', method='GET')
@view('resource-editor')
def edit(id: int):
    resource = db.get_resource({
        'id': id
    })
    return {'search_tag': '', 'resource': resource}


@route('/del/<id>', method='GET')
def remove(id: int):
    resource = db.get_resource({
        'id': id
    })

    db.del_resource(resource)

    response.status = 200
    return dict(message="OK")


@route('/release/<id>', method='GET')
def register(id: int):
    resource = db.get_resource({
        'id': id
    })
    db.set_resource(resource, {
        'is_occupied': 0
    })
    return 'OK'


@route('/register/<id>', method='GET')
def register(id: int):
    resource = db.get_resource({
        'id': id
    })
    db.set_resource(resource, {
        'is_occupied': 1
    })
    return 'OK'


@route('/')
@view('index')
def index():
    resources = db.get_resources()
    return {'resources': resources}


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
