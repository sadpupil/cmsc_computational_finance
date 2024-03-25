from portfolio_work import construct_portfolio
from portfolio_work import calculate_return;
from portfolio_work import calculate_risk_and_contribution;

title = [    "      [spy-0% / govt-100%]: ", 
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

def solution_02():
    number_of_shares, value_pairs, data_list = construct_portfolio(1000000)
    portfolio_return_list = calculate_return(value_pairs)
    portfolio_risk_list, risk_contribution_ratio_list = calculate_risk_and_contribution(data_list)
    
    print('-> no.of shares: ')
    for index, elem in enumerate(number_of_shares):
        print(title[index], end = '')
        print(elem[0], ', ', elem[2], ', ', elem[4], ', ', elem[1], ', ', elem[3], ', ', elem[5], sep = '')
        
    print('\n-> annualized portfolio risk and return, with risk contribution ratio: ')
    for index, elem in enumerate(portfolio_return_list):
        rtn = elem
        risk = portfolio_risk_list[index]
        contribution_ratio = risk_contribution_ratio_list[index]
        print(title[index], end = '')
        print('return: ', rtn, '%', '; risk: ', risk, '%; return/risk: ', round((rtn / risk), 2), sep = '')
        spaces = ' ' * (len(title[index]) - 2)
        print(spaces, '-> ', 'risk contribution ratio of spy: ', contribution_ratio[0], '%, ', 'govt: ', contribution_ratio[1], '%', sep = '')
        
if __name__ == "__main__":
    solution_02()