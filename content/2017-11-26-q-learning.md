---
layout: post
title: Q-Learning
slug: q-learning
author: Martin Thoma
date: 2017-11-26 20:00
category: Machine learning
tags: Machine learning, RL, Reinforcement Learning
featured_image: logos/ml.png
---
Reinforcement Learning (RL) is about finding optimal actions automatically.
So you have an environment `env` which has

* `env.reset() -> None`: Start a new episode. This could be a new game in the
  case of chess.
* `env.step(action) -> observation, reward, is_done, additional_information`:
  Make a step in the environment. The `is_done` says if the episode is over,
  e.g. if a game of chess is over. If it is over, then the environment needs
  a reset.

and an `agent` which has

* `agent.reset() -> agent`: Reset internal variables
* `agent.act(observation, no_exploration) -> action`: Let the agent take an action.
  If you want to evaluate the agent, set `no_exploration` to `True`.
* `agent.remember(prev_state, action, reward, state, is_done) -> agent`: Store
  what is necessary - here the learning happens.
* `agent.save(path) -> agent`: Serialize the agent to `path`
* `agent.load(path) -> agent`: De-serialize the agent from `path`


## The idea of Q-Learning

The following is a mixed introduction to RL / Q-Learning. You might want to
have a look at my [Reinforcement Learning](https://martin-thoma.com/reinforcement-learning/)
post as well.

If there is a limited set of observations $\mathcal{S}$ (states) and a limited
set of actions $\mathcal{A}$, then you have $|\mathcal{S}| \cdot |\mathcal{A}|$
possibilities to rate. For some of the observations you also receive a reward.
But rewards might be delayed:

```text
                      a0 --- s3, r=10
                    /
     a0-- s1, r= 10 - a1 --- s4, r= 0
    /
s0 -
    \a1 -- s2, r=-10 - a0 --- s5, r = 100
```

This shows that you start in state `s0` where you can execute actions `a0` and
`a1`. Action `a0` lives you a reward of 10, action `a1` a reward of `-10`. So
if you take the action greedy, you would take `a0` and end up in state `s1`.
But if you look one step ahead, you can see that `s2` ends up in state `s5`
with a reward of 100 whereas `s1` can only get a reward of 10 or 0.

In many cases, one does not want a greedy action. And one does not want to rely
completely on very high rewards in the very far future. Direct rewards are
prefered, but if it is really high we wait a bit longer. This thought leads to
the **value** of a state / action. The value of a state or a state/action pair
is its current reward plus its reward in future. As we want to prefer rewards
which come directly, we discount the future rewards with a factor $\gamma \in [0, 1]$:

$$V(s) = \max_{a \in \mathcal{A}} (R(s, a) + \gamma \sum_{s'} V(s'))$$

The $\max_{a \in \mathcal{A}}$ means we execute the optimal action all the
time.

Most of the time, the environments are not deterministic. Then you need to take
the transition probability from getting from state $s$ into state $s'$ when
you execute action $a$ into account:

$$V(s) = \max_{a \in \mathcal{A}} (R(s, a) + \gamma \sum_{s' \in \mathcal{S}} T(s, a, s') V(s'))$$

Ok, awesome! But now comes the tricky part: We don't have the function $V$.
If both, $\mathcal{S}$ and $\mathcal{A}$ are finite, we can simply:

* Initialize a table which has the columns (state, value of action 1, value of
  action 2, ..., value of action $n$) and one row per state. You could
  initialize it to zero.
* Run the agent. Update the $(state, action)$ cell with a weighted average of
  what was in the table + what was observed. The weighting factor is
  $\alpha \in (0, 1)$.

That's it.


## Code

You might want to read [Best practice for Machine Learning Projects](https://martin-thoma.com/ml-best-practice/)
to understand why the following code was written as it is.

The latest code can be found on [Github MartinThoma:algorithms/](https://github.com/MartinThoma/algorithms/blob/master/ML/rl/q_table_agent.py)

First, the configuration file:

```yaml
model_name: 'qlearning'
problem:
  gamma: 0.99  # discounting factor
training:
  nb_epochs: 100000
  learning_rate: 0.7  # alpha
  print_score: 500  # each 500 episodes
  exploration:
    name: 'Boltzmann'
    clip: [-500, 500]
testing:
  nb_epochs: 10000
```

Now the code:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Q-Table Reinforcement Learning agent."""

# core modules
import logging
import os
import pickle
import sys
import yaml

# 3rd party modules
import gym
import numpy as np

np.random.seed(280490)

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.DEBUG,
    stream=sys.stdout,
)
np.set_printoptions(formatter={"float_kind": lambda x: "{:.2f}".format(x)})


def main(environment_name, agent_cfg_file):
    """
    Load, train and evaluate a Reinforcment Learning agent.

    Parameters
    ----------
    environment_name : str
    agent_cfg_file : str
    """
    cfg = load_cfg(agent_cfg_file)

    # Set up environment and agent
    env = gym.make(environment_name)
    cfg["env"] = env
    cfg["serialize_path"] = "artifacts/{}-{}.pickle".format(
        cfg["model_name"], environment_name
    )
    agent = load_agent(cfg, env)

    agent = train_agent(cfg, env, agent)
    rewards = test_agent(cfg, env, agent)
    print("Average reward: {:5.3f}".format(rewards))
    print("Trained epochs: {}".format(agent.epoch))


class QTableAgent:
    """
    Q-Table Agent.

    Parameters
    ----------
    cfg : dict
    """

    def __init__(self, agent_cfg, nb_observations, nb_actions):
        self.nb_obs = nb_observations
        self.nb_act = nb_actions
        self.Q = np.zeros([nb_observations, nb_actions])
        self.lr = agent_cfg["training"]["learning_rate"]
        self.gamma = agent_cfg["problem"]["gamma"]  # discount
        self.epoch = 0
        self.exploration = agent_cfg["training"]["exploration"]

    def reset(self):
        """Reset the agent. Call this at the beginning of an episode."""
        self.epoch += 1

    def act(self, observation, no_exploration=False):
        """
        Decide which action to execute.

        Parameters
        ----------
        observation : int
        no_exploration : bool, optional (default: False)

        Returns
        -------
        action : int
        """
        assert self.epoch >= 1, "Reset before you run an episode."
        action = np.argmax(self.Q[observation, :])
        if not no_exploration:
            if self.exploration["name"] == "epsilon-greedy":
                if np.random.uniform() < self.exploration["epsilon"]:
                    action = np.random.random_integers(0, self.nb_act - 1)
            elif self.exploration["name"] == "Boltzmann":
                T = 1
                clip = self.exploration["clip"]
                q_values = self.Q[observation, :].astype("float64")
                q_values = np.clip(q_values / T, clip[0], clip[1])
                exp_values = np.exp(q_values)
                probs = exp_values / np.sum(exp_values)
                action = np.random.choice(range(self.nb_act), p=probs)
            else:
                raise NotImplemented(self.exploration["name"])
        return action

    def remember(self, prev_state, action, reward, state, is_done):
        """
        Store data in the Q-Table. Here, the learning happens.

        Parameters
        ----------
        prev_state : int
        action : int
        reward : float
        state : int
        """
        delta = reward - self.Q[prev_state, action]
        if not is_done:
            delta += self.gamma * np.max(self.Q[state, :])
        self.Q[prev_state, action] += self.lr * delta
        return self

    def save(self, path):
        """Serialize an agent."""
        data = {"Q": self.Q, "epoch": self.epoch}
        with open(path, "wb") as handle:
            pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
        return self

    def load(self, path):
        """Load an agent."""
        with open(path, "rb") as handle:
            data = pickle.load(handle)
            self.Q = data["Q"]
            self.epoch = data["epoch"]
        return self


def load_agent(cfg, env):
    """
    Create (and load) a QTableAgent.

    Parameters
    ----------
    cfg : dict
    env : OpenAI environment
    """
    agent = QTableAgent(cfg, env.observation_space.n, env.action_space.n)
    if os.path.isfile(cfg["serialize_path"]):
        agent.load(cfg["serialize_path"])
    return agent


# General training and testing code
def train_agent(cfg, env, agent):
    """
    Train an agent in environment.

    Parameters
    ----------
    cfg : dict
    env : OpenAI environment
    agent : object

    Return
    ------
    agent : object
    """
    cum_reward = 0.0
    for episode in range(cfg["training"]["nb_epochs"]):
        agent.reset()
        observation_previous = env.reset()
        is_done = False
        while not is_done:
            action = agent.act(observation_previous)
            observation, reward, is_done, _ = env.step(action)
            cum_reward += reward
            agent.remember(observation_previous, action, reward, observation, is_done)
            observation_previous = observation
        if episode % cfg["training"]["print_score"] == 0 and episode > 0:
            agent.save(cfg["serialize_path"])
            print("Average score: {:>5.2f}".format(cum_reward / (episode + 1)))
            print(agent.Q)
    agent.save(cfg["serialize_path"])
    return agent


def test_agent(cfg, env, agent):
    """Calculate average reward."""
    cum_reward = 0.0
    for episode in range(cfg["testing"]["nb_epochs"]):
        agent.reset()
        observation_previous = env.reset()
        is_done = False
        while not is_done:
            action = agent.act(observation_previous, no_exploration=True)
            observation, reward, is_done, _ = env.step(action)
            cum_reward += reward
            observation_previous = observation
    return cum_reward / cfg["testing"]["nb_epochs"]


# General code for loading ML configuration files
def load_cfg(yaml_filepath):
    """
    Load a YAML configuration file.

    Parameters
    ----------
    yaml_filepath : str

    Returns
    -------
    cfg : dict
    """
    # Read YAML experiment definition file
    with open(yaml_filepath, "r") as stream:
        cfg = yaml.load(stream)
    cfg = make_paths_absolute(os.path.dirname(yaml_filepath), cfg)
    return cfg


def make_paths_absolute(dir_, cfg):
    """
    Make all values for keys ending with `_path` absolute to dir_.

    Parameters
    ----------
    dir_ : str
    cfg : dict

    Returns
    -------
    cfg : dict
    """
    for key in cfg.keys():
        if key.endswith("_path"):
            cfg[key] = os.path.join(dir_, cfg[key])
            cfg[key] = os.path.abspath(cfg[key])
            if not os.path.isfile(cfg[key]):
                logging.error("%s does not exist.", cfg[key])
        if type(cfg[key]) is dict:
            cfg[key] = make_paths_absolute(dir_, cfg[key])
    return cfg


def get_parser():
    """Get parser object."""
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

    parser = ArgumentParser(
        description=__doc__, formatter_class=ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--env",
        dest="environment_name",
        help="OpenAI Gym environment",
        metavar="ENVIRONMENT",
        default="FrozenLake-v0",
    )
    parser.add_argument(
        "--agent",
        dest="agent_cfg_file",
        required=True,
        metavar="AGENT_YAML",
        help="Configuration file for the agent",
    )
    return parser


if __name__ == "__main__":
    args = get_parser().parse_args()
    main(args.environment_name, args.agent_cfg_file)
```

## Results

<table class="table">
    <tr>
        <th>Environment</th>
        <th>Config File</th>
        <th>Time</th>
        <th>Score</th>
    </tr>
    <tr>
        <td>FrozenLake-v0</td>
        <td>qlearning.yaml</td>
        <td>50s</td>
        <td>0.166</td>
    </tr>
    <tr>
        <td>FrozenLake-v0</td>
        <td>q-lr10.yaml</td>
        <td>48s</td>
        <td>0.743</td>
    </tr>
    <tr>
        <td>FrozenLake-v0</td>
        <td>q-lr90.yaml</td>
        <td>48s</td>
        <td>0.156</td>
    </tr>
    <tr>
        <td>CliffWalking-v0</td>
        <td>q-lr10.yaml</td>
        <td>128s</td>
        <td>-13.000</td>
    </tr>
    <tr>
        <td>FrozenLake8x8-v0</td>
        <td>q-lr10.yaml</td>
        <td>179s</td>
        <td>0.569</td>
    </tr>
    <tr>
        <td>NChain-v0</td>
        <td>q-lr90.yaml</td>
        <td>4614s</td>
        <td>1760.048</td>
    </tr>
    <tr>
        <td>OneRoundDeterministicReward-v0</td>
        <td>q-lr10.yaml</td>
        <td>5s</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>OneRoundNondeterministicReward-v0</td>
        <td>q-lr10.yaml</td>
        <td>6s</td>
        <td>2.475</td>
    </tr>
    <tr>
        <td>Roulette-v0</td>
        <td>q-lr10.yaml</td>
        <td>533s</td>
        <td>-2.764</td>
    </tr>
    <tr>
        <td>Taxi-v2</td>
        <td>q-lr10.yaml</td>
        <td>68s</td>
        <td>8.471</td>
    </tr>
    <tr>
        <td>TwoRoundDeterministicReward-v0</td>
        <td>q-lr10.yaml</td>
        <td>10s</td>
        <td>3.000</td>
    </tr>
    <tr>
        <td>TwoRoundNondeterministicReward-v0</td>
        <td>q-lr10.yaml</td>
        <td>ERROR</td>
        <td>ERROR</td>
    </tr>
</table>


## See also

* [dennybritz/reinforcement-learning](https://github.com/dennybritz/reinforcement-learning)
* Tijsma, Drugan, Wiering: [Comparing Exploration Strategies for Q-learning in Random Stochastic Mazes](http://www.ai.rug.nl/~mwiering/GROUP/ARTICLES/Exploration_QLearning.pdf)
