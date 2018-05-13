from apistar import App, http, types, validators


class Name(types.Type):
    """ A name """
    name = validators.String()


class Greeting(types.Type):
    """ Greeting obj """
    msg = validators.String()


def welcome(name: Name) -> Greeting:
    """ Nice greeting endpoint """

    if name is None:
        response = 'Welcome to API Star!'
    else:
        response = 'Welcome to API Star, %s!' % name
    return Greeting({'msg': response})


def template_handler(app: App, name: Name) -> http.HTMLResponse:
    return http.HTMLResponse(app.render_template('test.html', name=name))
