# TraffiKAI (powered by Intel oneAPI)

A-EYE on ROADS!
An AI & ML solution to solve one of the basic but most important traffic problems in day to day life.  

Problem Statement:- The increasing number of vehicles in cities can cause high volume of traffic, and implies that traffic congestion has become more critical nowadays. In addition to that, fatalities due to traffic delays of emergency vehicles such as ambulance & fire brigade is a huge problem. In daily life, we often see that emergency vehicles face difficulty in passing through traffic.

Objective:- Objective of proposed solution is to improve efficiency of existing traffic signaling system. The goal of the project is to automate the traffic signal system and make it easy for the traffic police department to monitor the traffic.

Solution:- The solution to solve the above problems as proposed are Dynamic Traffic Signaling and Emergency Vehicle Detection through both audio and video. The aim is to keep the same infrastructure and making delta changes in the system using the power of AI & ML.

https://user-images.githubusercontent.com/80829447/205123673-82164b3f-d8cd-4d97-8265-f1de680698a2.mp4  

# The Intel oneAPI Edge  
## Toolkit used: Intel® AI Analytics Toolkit (AI Kit) - oneDNN (Deep Neural Network Library)
TraffiKAI uses multiple memory intensive machine learning models which increases the runtime by a significant amount causing a delay in the processing of the input videos on the systems with limited processing power. The Intel® AI Analytics Toolkit (AI Kit) helps in achieving better results by optimising the models with the help of oneAPI Deep Neural Network Library (oneDNN). TraffiKAI uses state-of-the-art deep learning frameworks like PyTorch and Tensorflow which are optimized for the Intel architecture by the oneAPI platform and further boosts the inference of the models. scikit-learn is an important library which provides various algorithms of machine learning as functions. Intel(R) Extension for Scikit-Learn is also enabled to improve the performance. The toolkit also has support for a number of pre-trained models such as DenseNet-169, YOLOv3, LSTM (audio) which are used in TraffiKAI and help to improve the performance. Using the pre-trained models, transfer learning has been implemented on the Intel DevCloud for oneAPI which improvises the performance and accuracy. Intel® Distribution of OpenVINO™ Toolkit is also used to boost the object detection models.

![WhatsApp Image 2023-03-17 at 19 12 03](https://user-images.githubusercontent.com/80829447/225927241-274a2524-7f6c-4070-a0d9-98c323a91e4d.jpg)

The Emergency Vehicle Detection model is executed on Intel DevCloud where the Tensorflow is optimised by oneDNN and the Intel Extension for Scikit-Learn is enabled.  

![WhatsApp Image 2023-03-17 at 17 53 27](https://user-images.githubusercontent.com/80829447/225928507-7d0b7666-016e-48f8-b62b-60177941fcbf.jpg)  
The base environment contains a version of Python which is not installed through the Intel channel. The environment named oneapi contains the libraries which are installed through the Intel channel. 

![WhatsApp Image 2023-03-17 at 17 48 27](https://user-images.githubusercontent.com/80829447/225928512-ef24a2a3-c707-41c1-a6eb-76fbf5d2eeef.jpg)  
The Dynamic Traffic Signalling model uses Tensorflow which is optimised using oneDNN.  

## Time Elapsed  


![base](https://user-images.githubusercontent.com/80829447/225929189-425d3277-11e8-4cdb-a4c6-8e8ceb4b07d7.jpg)  
Time taken for the project to execute without oneAPI(base environment) : 49.82 seconds

![oneapi](https://user-images.githubusercontent.com/80829447/225929182-e8ed05c0-374d-4fcf-997f-c4b00f38904d.jpg)  
Time taken for the project to execute with oneAPI(oneapi environment) : 36.77 seconds  

Hence, we observe a difference of 13.05 seconds which is obtained with the help of oneAPI libraries.  

  
  
## Dynamic Traffic Signaling
Dynamic Traffic Signaling is implemented by calculating the density of traffic in each lane in a multi lane system and using this information it turns the signal lights green or red accordingly. It allocates the least time to the lane which has less density traffic and the time saved here is allocated to the lane which has high density traffic.  
Object detection alogorithm: Single Shot Detector (trained on COCO dataset)  
Teck Stack: Python, PyQT, OpenCV, Streamlit

## Emergency Vehicle Detection
Emergency Vehicle is detected by two methods in order to ensure the certainity of presence of an emergency vehicle in the input medium. The two methods include audio and video. Firstly, the video is processed frame by frame and the presence of emergency vehicles are found out and returns the confidence level and it returns a probability score.
The detection is also preformed through audio and the video's audio is passed through a CNN model which gives a probability score.
The probability scores from each models is obtained and ensemble learning is performed to get the final verdict.
Image Classification alogorithm: DenseNet-169 
Teck Stack: Python, PyQT, OpenCV, Streamlit

System Workflow:-  

![Workflow](https://user-images.githubusercontent.com/80829447/205130227-27c7a87d-dcd4-44b2-a248-9f9dc7bbba03.jpg)

GUI:  


https://user-images.githubusercontent.com/80829447/205130444-28d5a190-54b9-424e-b6b2-5154ea2337d0.mp4  

## Usage 

Steps to run this project:  
STEP 1: Download the models, resources and test folders from the drive link provided below.  
STEP 2: Clone the GitHub repository.  
STEP 3: Create a new Conda environment and install the required libraries present in the requirements.txt through the Intel channel.
STEP 4: Run the code provided below in the terminal of the project folder.

Install the requirements:
```
pip install -r requirements.txt
```

Run the app:
```
streamlit run app.py
```

Drive Link: https://drive.google.com/drive/folders/1TAgqHR8HnlVbFOhKwOagTckX0T06pOVv?usp=sharing 

