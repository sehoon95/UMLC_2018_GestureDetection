UMLC_2018_GestureDetection
====================
Gesture Detection for Home Automation
--------------------------------------------

### Overview

- Not switching to control home devices but just an action anywhere you are 
- Convenient user interface in easy way
- Using your own smart phone and gyroscope sensor(cheap and easy)

### Gesture Definition

- TV on (up) -> Lowering after lifting - grip horizontally
- TV off (down) -> Lifting after lowering - grip horizontally 
- AC on (left) -> Lowering after lifting - grip vertically
- AC off (light) -> Lifting after lowering - grip vertically
- Light on (on) -> Turning left after turning right
- Light off (off) -> Turning right after turning left

### Use Inception_v3 model

- I can use basic provided codes by just changing these parameters.
- 80% of the data for training, 10% for validation, 10% for testing

### Collecting Data Method

- 1. Gesture with a smartphone
- 2. Collect sensor data by using an app (CSV file)
- 3. Convert a CSV file to images with python codes

### How to Improve Accuracy

- Collected more data about the less accuracy class
- Adjusted the parameters (focused on step and learning rate)
- Deleted invalid learning data

### Future Works

- Add sensors to recognize more gestures
- Make it into an app that you can actually try
- Consider items that are better to use than the smartphone

### Concluding Remarks

- By defining and recognizing six gestures, I could achieve acceptable results.
- Using a gesture UI, you will be able to control your home devices more conveniently. 
