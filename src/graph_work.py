import matplotlib;
import matplotlib.pyplot as plt;

def plot_graph():
    rtn_risk_ratio = [-0.57, -0.36, -0.13, 0.08, 0.24, 0.35, 0.42, 0.48, 0.52, 0.54, 0.57] 
    annualized_risk = [6.53, 6.26, 6.50, 7.24, 8.32, 9.64, 11.09, 12.64, 14.26, 15.91, 17.60]
    annualized_return = [-3.73, -2.27, -0.83, 0.58, 1.98, 3.35, 4.71, 6.04, 7.36, 8.66, 9.95]
    weight_allocation = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    risk_contribution_spy = [0.00, 9.97, 32.64, 56.72, 74.57, 86.78, 92.36, 96.14, 98.27, 99.43, 100]
    risk_contribution_govt = [100, 90.66, 67.87, 43.35, 25.16, 13.82, 7.24, 3.54, 1.52, 0.48, 0]
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

    