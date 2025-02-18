# Reinforcement Learning Examples

This repository contains simple examples of reinforcement learning algorithms implemented in Python using TensorFlow and Keras. One of the core examples is a basic implementation of Deep Q-Networks (DQN) encapsulated in the `DQNWrapper` class, which demonstrates how to create and update a target network, train the model using custom target rewards, and periodically update the target network during training.

## Table of Contents

- [Overview](#overview)
- [Model Summary](#model-summary)
- [Repository Structure](#repository-structure)
- [Installation](#installation)
- [Implementation Details](#implementation-details)


## Overview

This project serves as a simple demonstration of how to implement a Deep Q-Network (DQN) for reinforcement learning using Keras. The `DQNWrapper` class:

- Initializes a Q-network and a target Q-network.
- Updates the target network periodically.
- Implements a training loop where the target rewards are computed using the maximum Q-value from the target network.
- Supports callbacks after each update batch to monitor training progress.

This implementation can be used as a starting point for more advanced reinforcement learning projects or for educational purposes.

### Model Summary

- **Architecture:**  
  A feed-forward neural network (MLP) with:
  - Input layer with shape (2,)
  - Hidden layers with 56, 128, and 256 neurons respectively
  - Output layer with 4 neurons (linear activation)

- **Loss Function:**  
  Uses the log-cosh loss, which is smoother and less sensitive to outliers than MSE.

- **Optimizer:**  
  RMSprop is used for optimization.

- **Metrics:**  
  Tracks Mean Absolute Percentage Error (MAPE) during training.

## Repository Structure

├── activations <br/>
│   ├── activations <br/>
│   └── Funciones de activación.ipynb <br/>
├── LICENSE <br/>
├── Q_learning_rooms <br/>
│   ├── copias.ipynb <br/>
│   ├── Q-Learning.ipynb <br/>
│   ├── Q-Learning_keras.ipynb <br/>
│   └── utils <br/>
│       ├── dqn_wrapper.py <br/>
│       ├── __init__.py <br/>
│       ├── plot_grid.py <br/>
│       ├── requierements.txt <br/>
│       └── Untitled.ipynb <br/>
└── README.md <br/>




- **Q_learning_rooms/utils/dqn_wrapper.py**  
  This module contains the main `DQNWrapper` class, which wraps a Keras-based Q-network model. Key features include:
  - **Model Wrapping:** Initializes both a primary Q-network and a target network (cloned from the primary) to stabilize training.
  - **Training Loop:** Implements a custom training loop that periodically updates the target network. The loop computes target Q-values by taking the maximum Q-value predicted by the target network, scaled by the discount factor (gamma). Callbacks can be used after each update batch to monitor training progress.
  - **Loss & Optimization:** The underlying Q-network is implemented in Keras. For example, the provided model uses several Dense layers and is compiled with the `logcosh` loss function, the `rmsprop` optimizer, and tracks `mape` (Mean Absolute Percentage Error) as a metric.

- **Q_learning_rooms/Q-Learning.ipynb & Q_learning_rooms/Q-Learning_keras.ipynb**  
  These notebooks demonstrate how to apply Q-learning and the DQN implementation on a grid-based environment. They include:
  - Initialization of reward matrices and grid visualization using custom plotting utilities (from `utils/plot_grid.py`).
  - Implementation of an epsilon-greedy strategy for action selection.
  - Functions to calculate state transitions, retrieve rewards, and update action values.

- **activations/Funciones de activación.ipynb**  
  A notebook with examples and visualizations of various activation functions, showcasing their behavior and potential use cases in neural networks.

- **requirements.txt**  
  Lists all required Python packages to run the code, such as TensorFlow, Keras, scikit-learn, pandas, numpy, and matplotlib.

*Note: Autogenerated files (e.g., `__pycache__`) and image files are excluded from the main structure.*



## Installation

To install the required dependencies, clone the repository and run:

```bash
git clone https://github.com/perrosdatos/reinforcement_learning_examples.git
cd reinforcement_learning_examples
pip install -r requirements.txt
```

## Implementation Details

- **Target Network Updates:**  
  The target network is a clone of the Q-network. It is updated periodically to provide stable Q-value estimates.

- **Reward Calculation:**  
  The training method computes new target Q-values using the maximum Q-value predicted by the target network, scaled by the discount factor (gamma). Terminal states are handled by setting the target to the immediate reward.

- **Training Loop:**  
  The training loop divides the total epochs into sub-epochs based on the number of target network updates. After each sub-epoch, the target network weights are updated.

