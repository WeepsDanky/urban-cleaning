# Urban Cleaning (IM45)
## Inspiration:

In cities like London. There is a prevalent presence of street garbage due to the inefficiency of current waste cleaning systems. We harness the power of data science and technology for the good of these cities, aiming to massively optmize street cleaning operations worldwide.

## What it does:

Our solution employs effective data science techniques to optimize urban cleaning. It integrates semantic image segmentation, object classification, and path planning modules to efficiently track garbage piles. By utilizing existing security cameras and crowd-sourced images, we locate garbage piles, generating streamlined collection routes and resource allocation.

## How we built it:

We leveraged the power of IBM Z infrastructure, combining models like SegFormer (https://huggingface.co/docs/transformers/model_doc/segformer) and our own Convolutional Neural Networks (CNNs) for image analysis. By integrates GPS locations of the footage, we ensures accurate garbage identification and then applies mapping with path finding.

## Challenges we ran into:

1. Data Integration: Collecting and processing data from diverse sources posed a significant challenge, requiring meticulous data cleansing, augmentation and synchronization efforts.
2. Real-time data accessibility: Adapting the system to access high quality real time data was challenging.
3. Selecting Models: Finding the most efficient yet accurate pre-trained segmentation model.

## Accomplishments that we're proud of:

1. Reduction in Computing Power Requirement: Finding the optimal model that runs effortlessly on the IBM Z Community Notebook which has limited GPU support.
2. Cohesive Modules: All three modules built by different members are able to work togather to pass artificial street footage data test.
3. *Data Privacy*: Ensuring citizen privacy with IBM Z Encryption while utilizing street security footage.
4. Building a live demo: https://weepsdanky.github.io/urban-cleaning redirected to the IMB Z server.

## What we learned:

1. Creative Problem-Solving: Addressing the GPU limitation pushed us to further our research and found compromise yet optimal pre-trained model.
2. Data Harmonization: Working with diverse data sources enhanced our skills in data cleansing and integration, essential for real-world applications.
3. Privacy Considerations: Understanding the ethical side of image processing.
4. Adaptability: Adapting to scenarials to complete the demo in proper time using existing resources.
5. Decision Making: Weighting time, difficulty and reward to make optimal decisions on our technical stack and actions.

## What's next for Urban Cleaning:

1. Improve Accuracy: Further improve the accuracy to further utilize the Computing Resources on IBM Z system. 
2. Scalability and Live Deployment: We aim to scale the solution for live deployment, utilizing IBM Cloud's extensive data handling capabilities.
3. Privacy and Security Enhancements: Further fortifying the platform's security features will ensure citizen privacy and data protection.
4. Autonomous Robots + Data: Utilizing Autonomous Vehicles and robot arms to perform low cost high efficiency city cleaning systems upon IBM Z where our tech stack stands.

We vision our Urban Cleaning system running on IBM Z can massively improve urban sanitation, saving substantial public funds, benefitting communities, taxpayers, and municipal governments worldwide.

Visit the live demo: https://weepsdanky.github.io/urban-cleaning
