########################################################################################################################
# Training
learning_rate = 1e-6
batch_size = 32
observation_time = 5e5
rand_observation_time = 5e4
prob_random = 1
gamma = 0.99
n_plays = 10000
fit_epochs = 1
decay = 0.75
weight_init = 0.01
########################################################################################################################
# Agent Model
conv_1 = [3, 3, 2, 16]
stride_1 = [1, 2, 2, 1]
conv_2 = [3, 3, 16, 32]
stride_2 = [1, 2, 2, 1]
conv_3 = [3, 3, 32, 64]
stride_3 = [1, 1, 1, 1]
dense_1 = 1024
dense_2 = 1024
dense_3 = 1024
dense_4 = 1024
dense_5 = 4


########################################################################################################################
# Control
train_model = False
show_ui = True
show_action = False

########################################################################################################################
# Paths
logdir = "./Results/Breakout/"  # Use: "./Results/CartPole/", "./Results/Breakout/"