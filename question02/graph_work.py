import matplotlib;
import matplotlib.pyplot as plt;

def plot_graph():
    rtn_risk_ratio = [-0.57, -0.36, -0.13, 0.08, 0.24, 0.35, 0.43, 0.48, 0.52, 0.54, 0.57] 
    annualized_risk = [6.53, 6.26, 6.52, 7.24, 8.31, 9.62, 11.07, 12.62, 14.24, 15.91, 17.60]
    annualized_return = [-3.73, -2.27, -0.83, 0.58, 1.98, 3.35, 4.71, 6.04, 7.36, 8.66, 9.95]
    weight_allocation = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    risk_contribution_spy = [0.00, 9.91, 32.47, 56.68, 74.77, 86.12, 92.73, 96.44, 98.47, 99.52, 100]
    risk_contribution_govt = [100, 90.09, 67.53, 43.32, 25.23, 13.88, 7.27, 3.56, 1.53, 0.48, 0]
    colors = ['#B88669', '#9370DB', '#FFA500', '#4B0082', '#1E90FF', '#8B4513', '#800080', '#FF8C00', '#8A2BE2', '#008080', '#FF4500']
    
    # scatter points chart
    size = 50
    plt.scatter(annualized_risk, annualized_return, s=size, c=colors, marker='s')
    plt.xlabel('Annualized Risk (%)')
    plt.ylabel('Annualized Return (%)')
    plt.title('Annualized Risk vs. Annualized Return')
    plt.show()

    # bar chart
    plt.bar(range(len(rtn_risk_ratio)), rtn_risk_ratio, color=colors)
    plt.xlabel('Return/Risk')
    plt.ylabel('Value')
    plt.title('Return/Risk in each portfolio')
    plt.show()
    
    # curve chart
    plt.plot(weight_allocation, risk_contribution_spy)
    plt.plot(weight_allocation, risk_contribution_govt)

    plt.xlabel('Weight Allocation (%)')
    plt.ylabel('Risk Contribution (%)')
    plt.xticks(weight_allocation)
    plt.title('Weight Allocation vs. Risk Contribution')
    
    plt.show()
    
plot_graph()

    