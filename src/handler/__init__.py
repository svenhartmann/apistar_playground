from apistar import App, http


def welcome(name=None) -> http.JSONResponse:
    if name is None:
        response = {'message': 'Welcome to API Star!'}
    response = {'message': 'Welcome to API Star, %s!' % name}
    return http.JSONResponse(response, status_code=200)


def template_handler(app: App, name=None) -> http.HTMLResponse:
    return http.Response(app.render_template('test.html', name=name))
