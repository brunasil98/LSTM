# MODELING CARDIAC CELL BIOPHYSICS USING DEEP LONG-SHORT MEMORY NETWORKS 

Accurate numerical biophysical models can be employed to elucidate mechanisms of cardiac rhythm 
disorders and their clinical implications. The predictive modeling has been increasingly used to investigate 
the missing link between experimental observations and clinical translation. Recently, Akwaboah et al.
(Akwaboah et al., 2021) formulated a detailed model of hiPSC-CMs which is able to accurately reproduce 
the biophysical dynamics of hiPSC-CMs. HiPSC-derived cardiomyocytes (hiPSC-CMs) have recently been used successfully in studying cardiac safety pharmacology and various inherited as well as acquired cardiac arrhythmia disorders (Moretti et al., 2010). The model consists of ionic current formulations of 14 key channels, pumps and exchangers along with intracellular calcium homeostasis. The model was used to 
provide insights into the causes of the experimentally observed suppression of automaticity in hiPSC-CMs 
during cholinergic stimulation.

In this study, we propose a deep LSTM (DLSTM) model for predicting the AP of an hiPSC-CM. A 
DLSTM consists of multiple cascaded LSTM layers operating at different time scales (Pascanu et al., 
2014). This method can perform an ordered process for capturing data patterns in a complex temporal task. 
We utilized two different DLSTM architectures to compare the performance of AP time series prediction.

Our deep neural network architecture uses a combination of LSTM layers, dropout (to decrease 
overfitting), and fully connected dense layers. To achieve the most effective network, we implemented
two different architectures. The first architecture used two back-to-back LSTM layers followed by three fully-connected dense layers. This network will be referred to as DLSTM2. The second architecture, shown in Figure 3B, composed of three back-to-back LSTM layers, one dropout, and three fully-connected dense layers. This network will be referred to as DLSTM3.

![image](https://user-images.githubusercontent.com/75848451/161892305-fe9fd730-dc74-4bde-ad82-ab096c336a5d.png)
 
Training and testing data was created by simulating the original Akwaboah et al. model (Akwaboah et al., 2021). The maximum channel conductance values of INa, IKur, IKr, IK1 and ICaL currents were scaled in the range of 0% (complete block) to 200% (100% enhancement) in steps of 20%. Each simulation was run for a duration of 5000 ms with a time step of 0.05 ms, generating a total of 100,000 points. This strategy gave us a total of 321 scenarios. However, we invalidated some of the data for not producing an AP due to non-physiological values of the current conductance. As a result, our final data set consisted of 252 samples with 100,000 time points each. To facilitate analysis, we selected four samples of 12000 output points each, capturing a complete AP signal in each sample as shown in Figure below. Next, we downscaled the data using a Fourier method in SciPy library to transform the samples into 5000 points each. Lastly, we deleted the first 50 and last 50 points due to susceptibility of noise. 

![image](https://user-images.githubusercontent.com/75848451/161893640-72992b98-33c6-43b1-bc96-a5e73d4f10b9.png)


We trained the DLSTM2 model for 923 epochs and DLSTM3 model for 1175 epochs. Each epoch was 
completed in an average 2.5 minutes and 6 minutes for DLSTM2 and DLSTM3 models, respectively,
using a CPU environment. Table below lists the performance metrics MAPE for the outcome of 
models when compared with the Akwaboah et al. model (Akwaboah et al., 2021). MAPE measures the difference between the predicted and actual values of APD50, APD75, APD90 and APDall. The Gaussian σ values for smoothing out the predicted signal were varied between 1 to 7 in steps of 0.1. The best value of σ was found to be 2.2 for DLSTM2 and 2.1 for DLSTM3 model.

![image](https://user-images.githubusercontent.com/75848451/161892923-c4a2f961-7938-4624-a469-419420ae85f0.png)

The Figuressbelow representative examples of the AP produced by the DLSTM models for various scaling of ionic currents. The predictions of DLSTM3 model were smoother than the DLSTM2 model. However, in both models some noise was observed during AP plateau (Phase 2-3) and diastolic interval (Phase 0) despite Gaussian smoothing.
![image](https://user-images.githubusercontent.com/75848451/161892969-23bc3812-16ed-4b19-9e36-1cdd45efaefc.png)

The models were trained with data from alterations in five main ionic current components that contribute to the action potentials in these cells. The model with 3 cascaded LSTM layers reproduce the action potential morphology with accuracy closer to 99%. These models were able to faithfully reproduce experimentally observed behaviors of ion channel blocks and drug interactions in cardiomyocytes. Further study should involve creating further finetuned models with the capacity to manipulate more currents, stimulus conditions, and refractory periods. 


