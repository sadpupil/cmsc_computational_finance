from portfolio_work import construct_portfolio
from portfolio_work import calculate_return;
from portfolio_work import calculate_risk_and_contribution;
from ew_portfolio_work import construct_ew_portfolio;
from ew_portfolio_work import calculate_return_and_risk;
from ew_portfolio_work import calculate_risk_contribution_ratio;

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

def solution_02():
    number_of_shares, value_pairs, data_list, daily_value_set = construct_portfolio(1000000)
    portfolio_return_list = calculate_return(value_pairs)
    portfolio_risk_list, risk_contribution_ratio_list = calculate_risk_and_contribution(data_list, daily_value_set)
    
    # calculate_risk_dailyValue(daily_value_set)
    
    print('-> no.of shares: ')
    for index, elem in enumerate(number_of_shares):
        print(title2[index], end = '')
        print(elem[0], ', ', elem[2], ', ', elem[4], ', ', elem[1], ', ', elem[3], ', ', elem[5], sep = '')
        
    print('\n-> annualized portfolio risk and return, with risk contribution ratio: ')
    for index, elem in enumerate(portfolio_return_list):
        rtn = elem
        risk = portfolio_risk_list[index]
        contribution_ratio = risk_contribution_ratio_list[index]
        print(title2[index], end = '')
        print('return: ', rtn, '%', '; risk: ', risk, '%; return/risk: ', round((rtn / risk), 2), sep = '')
        spaces = ' ' * (len(title2[index]) - 2)
        print(spaces, '-> ', 'risk contribution ratio of spy: ', contribution_ratio[0], '%, ', 'govt: ', contribution_ratio[1], '%', sep = '')
        
def solution_03_a():
    # total list contains the everyday price of each asset
    # it's a 2D array, each row contains the prices of assets of a praticular year
    total_list, daily_value, number_of_shares = construct_ew_portfolio(1000000)
    return_risk_list = calculate_return_and_risk(daily_value)
    risk_contribution_list = calculate_risk_contribution_ratio(total_list)
    
    print('-> no.of shares: ')
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
        
if __name__ == "__main__":
    if mark == 2:
        solution_02()
    if mark == 3:
        solution_02()
        solution_03_a()