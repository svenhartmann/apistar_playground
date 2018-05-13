from apistar import Route
from handler import welcome, template_handler

# maybe https://docs.apistar.com/api-guide/routing/#routing-in-larger-projects
routes_configuration = [
    Route('/', method='GET', handler=welcome),
    Route('/test', method='GET', handler=template_handler),
]
