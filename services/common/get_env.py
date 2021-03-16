import os
from typing import Union, Callable

EnvVarType = Union[str, int, bool]


def get_env_var(name: str, default: EnvVarType = None,
                cast_function: Callable[[EnvVarType], EnvVarType] = str) -> EnvVarType:
    env_var = os.getenv(name, default)
    try:
        return cast_function(env_var) or env_var
    except ValueError:
        raise EnvironmentError(f'Cannot cast {name} variable with value {env_var} using {cast_function}')
