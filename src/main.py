from portfolio_work import construct_portfolio
from portfolio_work import calculate_return_and_risk;
from portfolio_work import calculate_risk_contribution_ratio;
from ew_portfolio_work import construct_ew_portfolio;
from ew_portfolio_work import calculate_ew_return_and_risk;
from ew_portfolio_work import calculate_ew_risk_contribution_ratio;
from erc_portfolio_work import calculate_stddev_correlation;
from erc_portfolio_work import calculate_number_of_shares;
from erc_portfolio_work import calculate_portfolio_std_dev;
from comparison_portfolio_work import calculate_cmp_return_stddev;

# change this value to perform the calculation of different questions
mark = 3

title2 = [    "      [spy-0% / govt-100%]: ", 
             "      [spy-10% / govt-90%]: ",
             "      [spy-20% / govt-80%]: ",
             "      [spy-30% / govt-70%]: ",
             "      [spy-40% / govt-60%]: ",
             "      [spy-50% / govt-50%]: ",
             "      [spy-60% / govt-40%]: ",
             "      [spy-70% / govt-30%]: ",
             "      [spy-80% / govt-20%]: ",
             "      [spy-90% / govt-10%]: ",
             "      [spy-100% / govt-0%]: "    ]

title3 = [
    "       year 2021: ",
    "       year 2022: ",
    "       year 2023: "
]

title3_b = [
    "       spy: ",
    "       govt: ",
    "       gsg: "
]

title3_b_1 = [
    "       spy - govt: ",
    "       spy - gsg: ",
    "       govt - gsg: "
]

initial_capital = 1000000

def solution_02():
    price_value_list, number_of_shares = construct_portfolio(initial_capital)
    
    # the parameter price_value_list is a list which contains: 
    # the daily price of spy, govt and the portfolio value accordingly
    rtn_list, stand_dev_list = calculate_return_and_risk(price_value_list)
    
    contribution_ratio = calculate_risk_contribution_ratio(price_value_list)
    
    print('-> no.of shares: ')
    for index, elem in enumerate(number_of_shares):
        print(title2[index], end = '')
        print(elem[0], ', ', elem[2], ', ', elem[4], ', ', elem[1], ', ', elem[3], ', ', elem[5], sep = '')
        
    print('\n-> annualized portfolio standard deviations and returns, with risk contribution ratio: ')
    for index, elem in enumerate(rtn_list):
        rtn = elem
        risk = stand_dev_list[index]
        print(title2[index], end = '')
        print('return: ', round(rtn * 100, 2), '%', '; risk: ', round(risk * 100, 2), '%; return/risk: ', round((rtn / risk), 2), sep = '')
        spaces = ' ' * (len(title2[index]) - 2)
        print(spaces, '-> ', 'risk contribution ratio of spy: ', contribution_ratio[index][0], '%, ', 'govt: ', contribution_ratio[index][1], '%', sep = '')

def solution_03_a():
    portfolio_data_2022 = []
    portfolio_data_2023 = []
    # total list contains the everyday price of each asset
    # it's a 2D array, each row contains the prices of assets of a praticular year
    total_list, daily_value, number_of_shares, portfolio_data_2022, portfolio_data_2023 = construct_ew_portfolio(initial_capital)
    return_risk_list = calculate_ew_return_and_risk(daily_value)
    risk_contribution_list = calculate_ew_risk_contribution_ratio(total_list)
    
    print('Answers for (a)', end='')
    print('\n-> no.of shares: ')
    for index, elem in enumerate(number_of_shares):
        print(title3[index], end = '')
        print('[spy]', elem[0], ', [govt]', elem[1], ', [gsg]', elem[2], sep = '')
    
    print('\n-> [return], [standard deviation of return] and [return/risk ratio]')
    for index, elem in enumerate(return_risk_list):
        print(title3[index], end = '')
        print(elem[0], '%, ', elem[1], '%, ', elem[2], sep = '')
        
    print('\n-> risk contribution ratio')
    for index, elem in enumerate(risk_contribution_list):
        print(title3[index], end = '')
        print(elem[0], '%, ', elem[1], '%, ', elem[2], '%', sep = '')
    
    return portfolio_data_2022, portfolio_data_2023

def solution_03_b(portfolio_data_2022):
    weights = [0.187, 0.66, 0.153]
    std_dev_rtn, corr_coeff_matrix, covar_matrix = calculate_stddev_correlation(portfolio_data_2022)
    shares_list = calculate_number_of_shares(portfolio_data_2022, weights, initial_capital)
    portfolio_std_dev = calculate_portfolio_std_dev([[0.187],[0.66],[0.153]], covar_matrix)
    
    print('\nAnswers for (b)', end='')
    print('\n-> annualized standard deviations of returns: ')
    for i, elem in enumerate(std_dev_rtn):
        print(title3_b[i], end = '')
        print(round(elem, 4))
    
    print('\n-> correlation coefficients between each pair of assets: ')
    for i in range(len(corr_coeff_matrix)):
        print('      ', end='')
        for j in range(len(corr_coeff_matrix[0])):
            print(round(corr_coeff_matrix[i][j], 4), ', ', sep='', end = '')
        print('\n')
        
    print('\n-> covariance matrix: ')
    for i in range(len(covar_matrix)):
        print('      ', end='')
        for j in range(len(covar_matrix[0])):
            print(round(covar_matrix[i][j], 8), ', ', sep='', end = '')
        
    print('\n-> no.of shares: ')
    for index, elem in enumerate(shares_list):
        print(title3_b[index], end = '')
        print(round(elem, 2))
        
    print('\n-> Portfolio standard deviation:')
    print('      ', round(portfolio_std_dev, 4), sep='')
    
def solution_03_c(portfolio_data_2023):
    weights = [0.187, 0.66, 0.153]
    rtn, std_dev, ratio = calculate_cmp_return_stddev(initial_capital, weights, portfolio_data_2023)
    print('\nAnswers for (c)', end='')
    print('\n-> [return], [standard deviation of return] and [return/risk ratio]')
    print('      ', round((rtn * 100), 2), '%, ', round((std_dev * 100), 2), '%, ', round(ratio, 2), sep = '')
        
if __name__ == "__main__":
    if mark == 2:
        solution_02()
    if mark == 3:
        portfolio_data_2022, portfolio_data_2023 = solution_03_a()
        solution_03_b(portfolio_data_2022)
        solution_03_c(portfolio_data_2023)