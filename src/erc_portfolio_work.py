import math;
import numpy as np;

def calculate_annualized_stddev_single_asset(data_list):
    rtn_list = []
    pre_value = data_list[0]
    
    for i, elem in enumerate(data_list):
        if i > 0:
            rtn_list.append(elem / pre_value - 1)
        pre_value = elem
    
    avg_rtn = sum(rtn_list) / len(rtn_list)
    
    variance = 0
    for rtn in rtn_list:
        variance += (rtn - avg_rtn) ** 2
    variance /= (len(rtn_list) - 1)
    
    std_dev = math.sqrt(variance)
    annual_std_dev = math.sqrt(252) * std_dev
    return annual_std_dev

def calculate_annualized_covariance_two_assets(data_list_1, data_list_2):
    rtn_list_1 = []
    rtn_list_2 = []
    
    pre_value_1 = data_list_1[0]
    pre_value_2 = data_list_2[0]
    
    for i, elem in enumerate(data_list_1):
        if i > 0:
            rtn_list_1.append(elem / pre_value_1 - 1)
        pre_value_1 = elem
    
    for j, elem in enumerate(data_list_2):
        if j > 0:
            rtn_list_2.append(elem / pre_value_2 - 1)
        pre_value_2 = elem
        
    avg_rtn_1 = sum(rtn_list_1) / len(rtn_list_1)
    avg_rtn_2 = sum(rtn_list_2) / len(rtn_list_2)
        
    covariance= 0
    
    for i in range(len(rtn_list_1)):
        covariance += ((rtn_list_1[i] - avg_rtn_1) * (rtn_list_2[i] - avg_rtn_2))
    
    annual_covar = covariance * (252 / (len(rtn_list_1) - 1))
    # covariance /= len(rtn_list_1)
    return annual_covar
    # return covariance

def calculate_stddev_correlation(portfolio_data_2022):
    data_list_spy = []
    data_list_govt = []
    data_list_gsg = []
    for elem in portfolio_data_2022:
        data_list_spy.append(elem.price_spy)
        data_list_govt.append(elem.price_govt)
        data_list_gsg.append(elem.price_gsg)

    std_dev_spy = calculate_annualized_stddev_single_asset(data_list_spy)
    std_dev_govt = calculate_annualized_stddev_single_asset(data_list_govt)
    std_dev_gsg = calculate_annualized_stddev_single_asset(data_list_gsg)
    
    covar_spy_spy = calculate_annualized_covariance_two_assets(data_list_spy, data_list_spy)
    covar_govt_govt = calculate_annualized_covariance_two_assets(data_list_govt, data_list_govt)
    covar_gsg_gsg = calculate_annualized_covariance_two_assets(data_list_gsg, data_list_gsg)
    covar_spy_govt = calculate_annualized_covariance_two_assets(data_list_spy, data_list_govt)
    covar_spy_gsg = calculate_annualized_covariance_two_assets(data_list_spy, data_list_gsg)
    covar_govt_gsg = calculate_annualized_covariance_two_assets(data_list_govt, data_list_gsg)
    
    corr_spy_spy =  covar_spy_spy / (std_dev_spy * std_dev_spy)
    corr_spy_govt = covar_spy_govt / (std_dev_spy * std_dev_govt)
    corr_spy_gsg = covar_spy_gsg / (std_dev_spy * std_dev_gsg)
    
    corr_govt_spy = covar_spy_govt / (std_dev_spy * std_dev_govt)
    corr_govt_govt = covar_govt_govt / (std_dev_govt * std_dev_govt)
    corr_govt_gsg = covar_govt_gsg / (std_dev_govt * std_dev_gsg)
    
    corr_gsg_spy = covar_spy_gsg / (std_dev_spy * std_dev_gsg)
    corr_gsg_govt = covar_govt_gsg / (std_dev_govt * std_dev_gsg)
    corr_gsg_gsg = covar_gsg_gsg / (std_dev_gsg * std_dev_gsg)
    
    corr_matrix = [
        [corr_spy_spy, corr_spy_govt, corr_spy_gsg],
        [corr_govt_spy, corr_govt_govt, corr_govt_gsg],
        [corr_gsg_spy, corr_gsg_govt, corr_gsg_gsg]
    ]
    
    # calculate the covariance matrix for ii
    covar_matrix = [
        [covar_spy_spy, covar_spy_govt, covar_spy_gsg],
        [covar_spy_govt, covar_govt_govt, covar_govt_gsg],
        [covar_spy_gsg, covar_govt_gsg, covar_gsg_gsg]
    ]
    
    return [std_dev_spy, std_dev_govt, std_dev_gsg], corr_matrix, covar_matrix

def calculate_number_of_shares(portfolio_data_2022, weights, initial_capital):
    shares_spy = initial_capital * weights[0] / portfolio_data_2022[0].price_spy
    shares_govt = initial_capital * weights[1] / portfolio_data_2022[0].price_govt
    shares_gsg = initial_capital * weights[2] / portfolio_data_2022[0].price_gsg
    
    return [shares_spy, shares_govt, shares_gsg]

def calculate_portfolio_std_dev(weights, covar_matrix):
    w = np.array(weights)
    covar = np.array(covar_matrix)
    sig_p = np.dot(np.dot(np.transpose(w), covar), w)
    return math.sqrt(sig_p)