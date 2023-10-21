# Urban_Cleaning (IM45)

## Inspiration:
The inspiration behind our project stems from the pressing issue of urban cleanliness, particularly evident in cities like London. The prevalent presence of garbage not only mars the cityscape but also signifies the inefficiency of current waste management systems. We were motivated to harness data science and technology for good, aiming to revolutionize street cleaning operations worldwide.

## What it does: 
Our solution employs advanced data science techniques to optimize urban cleaning. It integrates image segmentation, garbage identification, and path planning modules to efficiently tackle garbage piles. By utilizing existing surveillance cameras and crowd-sourced images, we identify and categorize garbage objects, allowing for streamlined collection routes and resource allocation. 

## How we built it:
We leveraged the power of IBM Z Cloud infrastructure, combining models like SegFormer (https://huggingface.co/docs/transformers/model_doc/segformer) from Transformer and Convolutional Neural Networks (CNNs) for image analysis. Our platform integrates GPS data for precise localization, ensuring accurate garbage identification and collection. 

## Challenges we ran into: 

1. Limited GPU Availability: One of our primary challenges was the absence of GPU resources on IBM virtual machine, which necessitated innovative approaches for image processing.
2. Data Integration: Collating and processing data from diverse sources posed a significant challenge, requiring meticulous data cleansing and synchronization efforts.
3. Real-time Adaptability: Adapting the system to dynamic city events, rubbish removal companies and varying littering patterns proved to be a complex task, demanding robust algorithms and continuous refinement. 

## Accomplishments that we're proud of: 

1. Overcoming GPU Limitations: Despite the absence of dedicated GPUs, we devised efficient strategies for image processing, showcasing our adaptability and resourcefulness.
2. Seamless Integration: Successfully integrating existing surveillance systems into our solution demonstrated its practical feasibility and potential for widespread implementation.
3. *Data Privacy*: Ensuring citizen privacy while utilizing street surveillance footage was a critical concern.

## What we learned: 

1. Creative Problem-Solving: Addressing the GPU limitation led us to think outside the box, yielding innovative techniques for image processing. 
2. Data Harmonization: Working with diverse data sources enhanced our skills in data cleansing and integration, essential for real-world applications. 
3. Resourcefulness: Overcoming GPU limitations through innovative computational techniques.
4. Privacy Considerations: Implementing stringent data protection measures in public surveillance applications.
5. Adaptability: Designing a system capable of real-time adjustments to changing urban scenarios.

## What's next for Urban Cleaning: 

1. Scalability and Live Deployment: We aim to scale the solution for live deployment, utilizing IBM Cloud's extensive data handling capabilities. 
2. Privacy and Security Enhancements: Further fortifying the platform's security features will ensure citizen privacy and data protection.
3. Adaptive AI: Implementing machine learning algorithms to dynamically adjust to city events and evolving littering behaviors for sustained cleanliness.

By leveraging technology for good, we believe Urban Cleaning can revolutionize urban sanitation, benefitting communities, taxpayers, tourists, environmentalists, and municipal governments worldwide
