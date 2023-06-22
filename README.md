# MPPT Experiment Scheduler
**Scheduling experiments and testing MPPT (Maximum Power Point Tracking) algorithms for solar energy systems.**

Developing, training, and evaluating a machine learning algorithm for tracking the maximum power point is a task that is influenced by external factors, particularly the weather conditions. This repository provides a tool for scheduling and conducting tests based on weather forecasts to evaluate the performance of the algorithm under various climate scenarios.

## Conditions of interest
- **Evaluation under ideal conditions**: Assess the algorithm's speed and accuracy under ideal weather conditions.
- **Partial shading analysis**: Evaluate the algorithm's ability to distinguish between partially shaded local minima.
- **Stability assessment in rainy conditions**: Test the system's stability and performance during rainy weather conditions.
- **Data collection for prediction models and reinforcement learning**: Gather data required for training prediction models and reinforcement learning algorithms.

## Functionality
This tool utilizes weather forecasts to schedule and automate tests based on the predicted weather conditions, including the percentage of clouds, ultraviolet radiation, and general weather information. The scheduled experiment details are sent as WhatsApp messages at specified times of interest. The script can be executed from an Amazon EC2 instance or a Raspberry Pi.

## Overview
The general architecture of the project consists of using a weather API to obtain up-to-date weather conditions, while Twilio is used for sending WhatsApp messages to notify and schedule the experiments.

## Instructions
To set up and run the project, follow these steps:

1. Install the required packages listed in `requirements.txt`.
2. Create accounts on the weather API and Twilio platforms.
3. Obtain the necessary API tokens, phone numbers, and user information.
4. Save the obtained credentials as environment variables.
5. Run the `main.py` script to initiate the experiment scheduling process.

## License
This project is licensed under the MIT License.