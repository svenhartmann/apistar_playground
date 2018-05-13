from apistar import App, http, types, validators


class Name(types.Type):
    """ A name """
    pass


class Greeting(types.Type):
    """ Greeting obj """
    msg = validators.String()


def welcome(name: str=None) -> Greeting:
    """ Nice greeting endpoint """

    if name is None:
        response = 'Welcome to API Star!'
    else:
        response = 'Welcome to API Star, %s!' % name
    return Greeting({'msg': response})


def template_handler(app: App, name: str=None) -> http.HTMLResponse:
    return http.HTMLResponse(app.render_template('test.html', name=name))
