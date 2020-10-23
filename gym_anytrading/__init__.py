from gym.envs.registration import register
from copy import deepcopy

from . import datasets


DEFAULT_ENV = {'pivot_price_feature': 'Close',
               'pivot_window_size': 50,
               'features': [],
               'action_window_size': 1,
               'action_type': 'discrete',
               'reward_type': 'additive',
               'reward_function': 'return',
               'initial_wealth': 1.0,
               'transaction_cost': 0.0025
               }


def _load_default_env_settings():
    default_kwargs = DEFAULT_ENV.copy()

    default_kwargs['df'] = datasets.STOCKS_GOOGL
    default_kwargs['frame_bound'] = (default_kwargs['pivot_window_size'], len(datasets.STOCKS_GOOGL.index))

    return default_kwargs


### Register of default envs, override of args occurs if other args are passed during initialization ###

register(
    id='stocks-v0',
    entry_point='gym_anytrading.envs:StocksEnv',
    kwargs=_load_default_env_settings()
)

