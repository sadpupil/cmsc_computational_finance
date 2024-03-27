from portfolio_work import construct_portfolio
from portfolio_work import calculate_return_and_risk;
from portfolio_work import calculate_risk_contribution_ratio;
from ew_portfolio_work import construct_ew_portfolio;
from ew_portfolio_work import calculate_ew_return_and_risk;
from ew_portfolio_work import calculate_ew_risk_contribution_ratio;

# change this value to perform the calculation of different questions
mark = 2

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
    price_value_list, number_of_shares = construct_portfolio(1000000)
    rtn_list, stand_dev_list = calculate_return_and_risk(price_value_list)
    contribution_ratio = calculate_risk_contribution_ratio(price_value_list)
    
    print('-> no.of shares: ')
    for index, elem in enumerate(number_of_shares):
        print(title2[index], end = '')
        print(elem[0], ', ', elem[2], ', ', elem[4], ', ', elem[1], ', ', elem[3], ', ', elem[5], sep = '')
        
    print('\n-> annualized portfolio risk and return, with risk contribution ratio: ')
    for index, elem in enumerate(rtn_list):
        rtn = elem
        risk = stand_dev_list[index]
        print(title2[index], end = '')
        print('return: ', round(rtn * 100, 2), '%', '; risk: ', round(risk * 100, 2), '%; return/risk: ', round((rtn / risk), 2), sep = '')
        spaces = ' ' * (len(title2[index]) - 2)
        print(spaces, '-> ', 'risk contribution ratio of spy: ', contribution_ratio[index][0], '%, ', 'govt: ', contribution_ratio[index][1], '%', sep = '')
        
def solution_03_a():
    # total list contains the everyday price of each asset
    # it's a 2D array, each row contains the prices of assets of a praticular year
    total_list, daily_value, number_of_shares = construct_ew_portfolio(1000000)
    return_risk_list = calculate_ew_return_and_risk(daily_value)
    risk_contribution_list = calculate_ew_risk_contribution_ratio(total_list)
    
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
        # solution_02()
        solution_03_a()