'''
OpenGL
======

Select and use the best OpenGL library available. Depending on your system, the
core provider can select an OpenGL ES or a 'classic' desktop OpenGL library.
'''

# Right now, only PyOpenGL
from os import environ

if 'KIVY_DOC' not in environ:

    from kivy.config import Config
    from kivy.logger import Logger
    from kivy.graphics.opengl import *

    def print_gl_version():
        version = glGetString(GL_VERSION)
        Logger.info('GL: OpenGL version <%s>' % str(version))

    # Disable pyOpenGL auto GL Error Check?
    gl_check = Config.get('kivy', 'gl_error_check')
    if gl_check.lower() in ['0', 'false', 'no']:
        OpenGL.ERROR_CHECKING = False

    # To be able to use our GL provider, we must have a window
    # Automaticly import window auto to ensure the default window creation
    import kivy.core.window
