import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='Car-v0',
    entry_point='car_race.envs:CarEnv',
    timestep_limit=1000,
    reward_threshold=1.0,
    nondeterministic = True,
)
