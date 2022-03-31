MACHINE LEARNING-BASED SIMULATION OF CARDIAC ELECTROPHYSIOLOGY

 Over the years, various attempts have been made towards explaining and reproducing the electrical activity of the heart. A variety of models has been proposed, ranging from mechanistic to empirical, and considering the heart at the cellular level through to tissues or even the organ as a whole. While some of these models answered some “big questions” in the field, one major challenge that persists is the computational complexity of these models. With the emergence of deep learning techniques, it has become relatively easy to build and deploy empirical “data-driven” models. This offers a wealth of opportunities for gaining new insight into the workings of the heart that current models are unable to offer.

 The data used to train this model was synthetically generated by an in silico hiPSC-Derived Cardiomyocyte Model built with a genetic algorithm created by Akwasi D. Akwaboah, Bright Tsevi, Pascal Yamlome, Jacqueline A. Treat, Maila Brucal-Hallare, Jonathan M. Cordeiro and Makarand Deo. Using the hiPSC model, we blocked  and raised the values of  ICaL, IK1, IKr, IKur and INa currents from 0% to 200% in steps of 20% to generate our data.  In each interaction, it was produced 100,000 ms of action potential. To train our model, we collected 3 samples of 10,000 ms from the 100,000 ms created due to the high memory 100,000 ms takes to be training  in a LSTM model.  

![image](https://user-images.githubusercontent.com/75848451/152657932-dd97c201-a003-4f5c-8140-21455ac0a4d1.png)

To create the network architecture, we built a model with three layers. First, we used a Long Short-Term Memory (LSTM) network with 5 input neurons, each representing the current values, and 12,000 output neurons; Second, it was a Dense layer with 12,000 input and output neurons; My last layer was Dense layer with 12,000 input neurons and 10,0000 out neurons which represented the action potential predicted.  To compile, we used loss as mean squared error and optimizer as RMSprop. In total the model had 840,310,000 parameters.

![image](https://user-images.githubusercontent.com/75848451/152658540-86672575-2988-4548-a335-d5438fc04d44.png)

The results collected so far have been very promising, and we are still adjusting the number of epochs and the location of the action potential start point on each sample.
 
 ![image](https://user-images.githubusercontent.com/75848451/152658514-ab86a948-8f52-46da-85c8-964ad2caf739.png)
