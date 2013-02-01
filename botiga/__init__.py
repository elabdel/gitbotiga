# -*- coding: utf-8 -*-
from pyramid.config import Configurator

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application."""
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    settings['mako.directories'] = os.path.join(here, 'templates')
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('productes', '/botiga')
    config.scan()
    return config.make_wsgi_app()
