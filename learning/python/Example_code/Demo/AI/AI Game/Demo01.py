# -*- coding: utf-8 -*-
# @Time : 2020/12/31 0:57
# @Author : MYH
# @File : Demo01.py
# @Software: PyCharm

from environment import Environment
from train import Trainer
from dqn import DQN

env = Environment(args)
agent = DQN(env,args)

Trainer(agent).run()

env.gym.monitor.start(args.out, force=True)
agent.play()
env.gym.monitor.close()