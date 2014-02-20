import os
try:
    from importlib import import_module
except ImportError:
    try:
        from django.utils.importlib import import_module
    except ImportError:
        raise


_rules = []


def get_rules():
    return _rules


def register_rules(rules_file):
    module = import_module('djangocompatlint.rules.%s' % rules_file)
    _rules.extend(module.rules)


def initialize():
    self_dir = os.path.abspath(os.path.dirname(__file__))
    rules_dir = os.path.join(self_dir, 'rules')
    for f in os.listdir(rules_dir):
        if f.endswith('.py') and f != '__init__.py':
            f = f[:-3]  # Nix the .py
            register_rules(f)
