import math;

def calculate_cmp_return_stddev(initial_capital, weights, portfolio_data_2023):
    # construct the portfolio
    portfolio_price_value = []
    
    shares_spy = initial_capital * weights[0] / portfolio_data_2023[0].price_spy
    shares_govt = initial_capital * weights[1] / portfolio_data_2023[0].price_govt
    shares_gsg = initial_capital * weights[2] / portfolio_data_2023[0].price_gsg
    
    for i, elem in enumerate(portfolio_data_2023):
        daily_value = shares_spy * elem.price_spy + shares_govt * elem.price_govt + shares_gsg * elem.price_gsg
        # print(elem.price_spy, ', ', elem.price_govt, ', ', elem.price_gsg, ', ', daily_value, sep='')
        tmp = [elem.price_spy, elem.price_govt, elem.price_gsg, daily_value]
        portfolio_price_value.append(tmp)
        
    # calculate the portfolio return 
    start_value = portfolio_price_value[0][3]
    end_value =  portfolio_price_value[-1][3]
    rtn = (end_value - start_value) / start_value
    
    # calculate the standard deviation of return
    rtn_list = []
    pre_value = 0
    for i, v in enumerate(portfolio_price_value):
        # print(v[3])
        if i > 0:
            rtn_list.append(v[3] / pre_value - 1)
        pre_value = v[3]
    avg_rtn = sum(rtn_list) / len(rtn_list)
    covar = 0
    for r in rtn_list:
        covar += (r - avg_rtn) ** 2
    covar /= (len(rtn_list) - 1)
    std_dev = math.sqrt(covar) * math.sqrt(252)
    
    risk_return_ratio = rtn / std_dev
    
    return rtn, std_dev, risk_return_ratio