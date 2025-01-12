# {{ cookiecutter.project_name}} -- {{ cookiecutter.description }}
# Copyright: (C) {% now 'local', '%Y' %}  {{ cookiecutter.full_name }}
# License: {{ cookiecutter.open_source_license }}
# See the LICENSE file for more details
"""The main entrypoint for {{ cookiecutter.project_slug }}."""
# pylint bug: https://github.com/PyCQA/pylint/issues/3624
from .cli import main  # pylint: disable=relative-beyond-top-level

if __name__ == '__main__':
    main()
