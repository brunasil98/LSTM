import numpy as np
from scipy.ndimage import gaussian_filter1d
from scipy.signal import peak_widths, find_peaks
from sklearn.metrics import mean_absolute_percentage_error


#Genererate APD50, APD, APD75 for the data
def gaussian(data,w,i,ls_APD50, ls_APD75, ls_APD90, ls_APDall):
    sx = 0
    time = np.arange(0,4900,1)
    Vmem = data
    Vmx = Vmem[sx:]
    tmx = time[sx:]
    peaks, _ = find_peaks(Vmx,distance=3500)
    valleys, _ = find_peaks(-Vmx,distance=3500)
    t_pks = tmx[peaks]
    V_pks = Vmx[peaks]
    t_vlys = tmx[valleys]
    V_vlys = Vmx[valleys]


    #APD90
    APD90 = peak_widths(Vmx, peaks, rel_height=0.9)
    V_min = APD90[1]
    peaks_indx_arr = APD90[2:]
    pks_indx_int = np.uint16(np.around(peaks_indx_arr))
    pks_times = time[pks_indx_int]
    APD90_hl_arr = np.zeros((3, len(peaks)))
    APD90_hl_arr[0] = APD90[1]
    APD90_hl_arr[1:] = pks_times
    APD90_vl_arr = np.zeros((3, len(peaks)))
    APD90_vl_arr[0] = t_pks
    APD90_vl_arr[1] = APD90[1]
    APD90_vl_arr[2] = V_pks
    APD90s = pks_times[1] - t_pks #actual APDs

    #APD75
    APD75 = peak_widths(Vmx, peaks, rel_height=0.75)
    V_min = APD90[1]
    peaks_indx_arr = APD75[2:]
    pks_indx_int = np.uint16(np.around(peaks_indx_arr))
    pks_times = time[pks_indx_int]
    APD75_hl_arr = np.zeros((3, len(peaks)))
    APD75_hl_arr[0] = APD75[1]
    APD75_hl_arr[1:] = pks_times
    APD75_vl_arr = np.zeros((3, len(peaks)))
    APD75_vl_arr[0] = t_pks
    APD75_vl_arr[1] = APD75[1]
    APD75_vl_arr[2] = V_pks
    APD75s = pks_times[1] - t_pks #actual APDs
    
    #APD50
    APD50 = peak_widths(Vmx, peaks, rel_height=0.5)
    V_min = APD90[1]
    peaks_indx_arr = APD50[2:]
    pks_indx_int = np.uint16(np.around(peaks_indx_arr))
    pks_times = time[pks_indx_int]
    APD50_hl_arr = np.zeros((3, len(peaks)))
    APD50_hl_arr[0] = APD50[1]
    APD50_hl_arr[1:] = pks_times
    APD50_vl_arr = np.zeros((3, len(peaks)))
    APD50_vl_arr[0] = t_pks
    APD50_vl_arr[1] = APD50[1]
    APD50_vl_arr[2] = V_pks
    APD50s = pks_times[1] - t_pks #actual APDs

########## Calculating the values  ###########

    v_APD50 = np.mean(APD50s)
    v_APD75 = np.mean(APD75s)
    v_APD90 = np.mean(APD90s)

###### ADDING IN THE LISTs  ######################

    ls_APD50[w][i] = v_APD50
    ls_APD75[w][i] = v_APD75
    ls_APD90[w][i] = v_APD90
    v = i
    v = v*3
    ls_APDall[w][v] = v_APD50
    ls_APDall[w][v+1] = v_APD75
    ls_APDall[w][v+2] = v_APD90
    return ls_APD50, ls_APD75, ls_APD90, ls_APDall


def best_gausian(predicted):
    
    #Create Numpy and design value for c
    gaus = np.zeros((70,194,1,4900))
    c = 0
    
    #Values for sigma from 1 to 8 with step of 0.1
    
    for a in np.arange(1,8,0.1):
        a = round(a,1)
        
    # Apply gaussian fiter with each value of sigma
    
    for i in range(predicted.shape[0]):
        gaus[c][i] = gaussian_filter1d(predicted[i], sigma=a)
    c = c + 1
    
    # Create the Numpys
    
    pred_apd50_ls = np.zeros((1,194))
    pred_apd75_ls = np.zeros((1,194))
    pred_apd90_ls = np.zeros((1,194))
    pred_apd_ls = np.zeros((1,582))

    act_apd50_ls = np.zeros((1,194))
    act_apd75_ls = np.zeros((1,194))
    act_apd90_ls = np.zeros((1,194))
    act_apd_ls = np.zeros((1,582))

    gau_apd50_ls = np.zeros((70,194))
    gau_apd75_ls = np.zeros((70,194))
    gau_apd90_ls = np.zeros((70,194))
    gau_apd_ls = np.zeros((70,582))
    
    #Generate the APDs values for each occasion calling the gaussian function 
    
    for w in range(0,70):
        for i in range(predicted.shape[0]):
            pre = predicted[i].reshape(-1)
            act = y_test[i].reshape(-1)
            pred_apd50_ls, pred_apd75_ls, pred_apd90_ls, pred_apd_ls = gaussian(pre,0,i,pred_apd50_ls, pred_apd75_ls, pred_apd90_ls, pred_apd_ls)
            act_apd50_ls, act_apd75_ls, act_apd90_ls, act_apd_ls = gaussian(act,0,i,act_apd50_ls, act_apd75_ls, act_apd90_ls, act_apd_ls)
            gus = gaus[w][i].reshape(-1)
            gau_apd50_ls, gau_apd75_ls, gau_apd90_ls, gau_apd_ls = gaussian(gus,w,i,gau_apd50_ls, gau_apd75_ls, gau_apd90_ls, gau_apd_ls)

    MBPE_apd50_pa = []
    MBPE_apd75_pa = []
    MBPE_apd90_pa = []
    MBPE_apd_pa = []

    MBPE_apd50_ga = []
    MBPE_apd75_ga = []
    MBPE_apd90_ga = []
    MBPE_apd_ga = []
    
    # Calculate the Mean Absolute error for each value of APDs generated between prediction and actual
    
    p = act_apd50_ls[0].tolist()
    q = pred_apd50_ls[0].tolist()
    MBPE_apd50_pa.append(mean_absolute_percentage_error(p,q))

    p = act_apd75_ls[0].tolist()
    q = pred_apd75_ls[0].tolist()
    MBPE_apd75_pa.append(mean_absolute_percentage_error(p,q))

    p = act_apd90_ls[0].tolist()
    q = pred_apd90_ls[0].tolist()  
    MBPE_apd90_pa.append(mean_absolute_percentage_error(p,q))

    p = act_apd_ls[0].tolist()
    q = pred_apd_ls[0].tolist()
    MBPE_apd_pa.append(mean_absolute_percentage_error(p,q))

    # Calculate the Mean Absolute error for each value of APDs generated between actual and each gaussian values
    
    for k in range(0,70):
        p = act_apd50_ls[0].tolist()
        q = gau_apd50_ls[k].tolist()  
        MBPE_apd50_ga.append(mean_absolute_percentage_error(p,q))

        p = act_apd75_ls[0].tolist()
        q = gau_apd75_ls[k].tolist()  
        MBPE_apd75_ga.append(mean_absolute_percentage_error(p,q))

        p = act_apd90_ls[0].tolist()
        q = gau_apd90_ls[k].tolist()  
        MBPE_apd90_ga.append(mean_absolute_percentage_error(p,q))

        p = act_apd_ls[0].tolist()
        q = gau_apd_ls[k].tolist()  
        MBPE_apd_ga.append(mean_absolute_percentage_error(p,q))
    
    #Find the best value of sigma for each APDs
    
    Sigma_value_min_apd50 = MBPE_apd50_ga.index(min(MBPE_apd50_ga)) * 0.1 + 1 
    MBPE_apd50_ga = min(MBPE_apd50_ga)
    Sigma_value_min_apd75 = MBPE_apd75_ga.index(min(MBPE_apd75_ga))* 0.1 + 1 
    MBPE_apd75_ga = min(MBPE_apd75_ga)
    Sigma_value_min_apd90 = MBPE_apd90_ga.index(min(MBPE_apd90_ga))* 0.1 + 1 
    MBPE_apd90_ga = min(MBPE_apd90_ga)
    Sigma_value_min_apdall = MBPE_apd_ga.index(min(MBPE_apd_ga))* 0.1 + 1
    MBPE_apd_ga = min(MBPE_apd_ga)

    return (MBPE_apd50_pa, MBPE_apd75_pa, MBPE_apd90_pa, MBPE_apd_pa, 
    Sigma_value_min_apd50, MBPE_apd50_ga, Sigma_value_min_apd75, MBPE_apd75_ga,
    Sigma_value_min_apd90, MBPE_apd90_ga, Sigma_value_min_apdall, MBPE_apd_ga)

def most_frequent(List):
    return max(set(List), key = List.count)
