from apistar import App
from dynaconf import settings

from routes import routes_configuration

app = App(
        routes=routes_configuration,
        schema_url=settings.APP['schema_url'],
        template_dir=settings.TEMPLATE['dir'],
        static_dir=settings.TEMPLATE['static']
    )

if __name__ == '__main__':
    app.serve(settings.SERVER['address'], settings.SERVER['port'], debug=settings.SERVER['debug'])
