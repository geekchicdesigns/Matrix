import sys

def get_base_prefix_compat():
    """Get base/real prefix, or sys.prefix if there is none."""
    return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix

def in_virtualenv():
    return get_base_prefix_compat() != sys.prefix

#def is_venv():
#    return (hasattr(sys, 'real_prefix') or
#            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

if in_virtualenv():
    print('inside virtualenv or venv')
else:
    print('outside virtualenv or venv')
