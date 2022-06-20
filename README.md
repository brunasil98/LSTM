# MODELING CARDIAC CELL BIOPHYSICS USING LONG-SHORT MEMORY NETWORKS 

Accurate numerical biophysical models can be employed to elucidate mechanisms of cardiac rhythm 
disorders and their clinical implications. The predictive modeling has been increasingly used to investigate 
the missing link between experimental observations and clinical translation. Recently, Akwaboah et al.
(Akwaboah et al., 2021) formulated a detailed model of hiPSC-CMs which is able to accurately reproduce 
the biophysical dynamics of hiPSC-CMs. HiPSC-derived cardiomyocytes (hiPSC-CMs) have recently been used successfully in studying cardiac safety pharmacology and various inherited as well as acquired cardiac arrhythmia disorders (Moretti et al., 2010). The model consists of ionic current formulations of 14 key channels, pumps and exchangers along with intracellular calcium homeostasis. The model was used to 
provide insights into the causes of the experimentally observed suppression of automaticity in hiPSC-CMs 
during cholinergic stimulation.

In this study, we propose a LSTM model for predicting the AP of an hiPSC-CM. A 
LSTM consists of multiple cascaded LSTM layers operating at different time scales (Pascanu et al., 
2014). This method can perform an ordered process for capturing data patterns in a complex temporal task. 
We utilized two different DLSTM architectures to compare the performance of AP time series prediction.

Our deep neural network architecture uses a combination of LSTM layers,and fully connected dense layers. To achieve the most effective network, we implemented two different architectures. The first architecture used two back-to-back LSTM layers followed by three fully-connected dense layers. This network will be referred to as LSTM2. The second architecture, shown in Figure 3B, composed of three back-to-back LSTM layers,  and three fully-connected dense layers. This network will be referred to as LSTM3.

![image](https://user-images.githubusercontent.com/75848451/174668712-4861deb7-3512-4c83-9fd7-a539b15e688f.png)
 
Training and testing data was created by simulating the original Akwaboah et al. model (Akwaboah et al., 2021). The maximum channel conductance values of ICaL, IK1, IKr, IKur, and INa currents were scaled in the range of 0% (complete block) to 200% (100% enhancement) in steps of 20%. Simulations were performed by manipulating single current conductances as well as combinations of changing multiple current conductances in each run, which produced a total of 341 simulations.  However, some current combinations failed to generate an AP (e.g. INa conductance reduced by more than 50%) (Akwaboah et al., 2021). Such non-physiological current scaling combinations were removed from the training/testing data which resulted into a final dataset consisting of 252 unique simulations. Each simulation was run for a duration of 5000 ms with a time step of 0.05 ms, generating a total of 100,000 time points per simulation. To keep the computations tractable, each AP time series was split into smaller segments each consisting of 12000 time points. Each data sample was adjusted to contain a complete AP signal as shown in Figure 4. Next, the data was resampled using a Fourier method in SciPy library to 5000 time points per sample. Lastly, we deleted the first 50 and last 50 points due to susceptibility of noise. In all, the processed dataset consisted of 971 samples with 4900 time points each.

![image](https://user-images.githubusercontent.com/75848451/161893640-72992b98-33c6-43b1-bc96-a5e73d4f10b9.png)


We trained the LSTM2 model for 923 epochs and LSTM3 model for 834 epochs. Each epoch was completed in an average 150s and 380s for LSTM2 and LSTM3 models, respectively,using a CPU environment. Table below lists the performance metrics MAPE for the outcome of models when compared with the Akwaboah et al. model (Akwaboah et al., 2021). MAPE measures the difference between the predicted and actual values of APD50, APD75, APD90 and APDall. The Gaussian σ values for smoothing out the predicted signal were varied between 1 to 7 in steps of 0.1. The best value of σ was found to be 2.2 for LSTM2 and 7.6 for LSTM3 model.

![image](https://user-images.githubusercontent.com/75848451/174669215-992f7583-87d2-456e-a99f-5f89db151f33.png)

The Figures below representative examples of the AP produced by the LSTM models for various scaling of ionic currents. The predictions of LSTM3 model were smoother than the LSTM2 model. However, in both models some noise was observed during AP plateau (Phase 2-3) and diastolic interval (Phase 0) despite Gaussian smoothing.

![image](https://user-images.githubusercontent.com/75848451/174669343-948b3696-b835-4fb6-87e5-32325b995dde.png)

 In this study, LSTM-based models were developed to describe the biophysical response of human induced pluripotent stem cell-derived cardiomyocytes. The models were trained with data from alterations in five main ionic current components that contribute to the action potentials in these cells. The model with 3 cascaded LSTM layers achieved an overall MSE of 14.803 and the action potential morphology was reproduced with accuracy close to 99%. These models were able to faithfully reproduce experimentally observed behaviors of ion channel blocks and drug interactions in cardiomyocytes. Further study should involve creating further finetuned models with the capacity to manipulate more currents, stimulus conditions, and refractory periods. 

