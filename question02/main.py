from workout_a import construct_portfolio
from workout_a import calculate_return;
from workout_a import calculate_risk;


def solution_02():
    portfolio_value_pairs, data_list = construct_portfolio(1000000)
    calculate_return(portfolio_value_pairs)
    calculate_risk(data_list)
    
if __name__ == "__main__":
    solution_02()