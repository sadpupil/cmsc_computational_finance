import matplotlib;
import matplotlib.pyplot as plt;
from matplotlib import patches;
from matplotlib.font_manager import FontProperties;

def plot_graph():
    rtn_risk_ratio = [-0.57, -0.36, -0.13, 0.08, 0.24, 0.35, 0.42, 0.48, 0.52, 0.54, 0.56] 
    annualized_risk = [6.53, 6.24, 6.50, 7.24, 8.32, 9.64, 11.09, 12.64, 14.26, 15.91, 17.60]
    annualized_return = [-3.73, -2.27, -0.83, 0.58, 1.98, 3.35, 4.71, 6.04, 7.36, 8.66, 9.95]
    weight_allocation = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    risk_contribution_spy = [0.00, 9.91, 32.47, 56.68, 74.77, 86.12, 92.73, 96.44, 98.47, 99.52, 100]
    risk_contribution_govt = [100, 90.09, 67.53, 43.32, 25.23, 13.88, 7.27, 3.56, 1.53, 0.48, 0]
    legend_set = ['0% SPY : 100% GOVT', '10% SPY : 90% GOVT', '20% SPY : 80% GOVT', '30% SPY : 70% GOVT', '40% SPY : 60% GOVT', '50% SPY : 50% GOVT',
                  '60% SPY : 40% GOVT', '70% SPY : 30% GOVT', '80% SPY : 20% GOVT', '90% SPY : 10% GOVT', '100% SPY : 0% GOVT']
    colors = ['#B88669', '#9370DB', '#FFA500', '#4B0082', '#1E90FF', '#8B4513', '#800080', '#FF8C00', '#8A2BE2', '#008080', '#FF4500']
    
    # scatter points chart
    # plt.subplots(figsize=(12, 8))
    plt.scatter(annualized_risk, annualized_return, s=50, c=colors, marker='s')
    plt.xlabel('Annualized Risk (%)')
    plt.ylabel('Annualized Return (%)')
    plt.title('Annualized Risk vs. Annualized Return')
    # legend_patches = [patches.Patch(color=color, label=str(category)) for category, color in zip(legend_set, colors)]
    # font_prop = FontProperties(size=8)
    # plt.legend(handles=legend_patches, loc='center left', bbox_to_anchor=(1, 0.5), prop=font_prop)
    plt.show()

    # bar chart
    # plt.subplots(figsize=(16, 8))
    plt.bar(range(len(rtn_risk_ratio)), rtn_risk_ratio, color=colors)
    plt.xlabel('Return/Risk')
    plt.xticks([])
    # plt.ylabel('Value')
    plt.title('Return/Risk in each portfolio')
    # legend_patches = [patches.Patch(color=color, label=str(category)) for category, color in zip(legend_set, colors)]
    # font_prop = FontProperties(size=8)
    # plt.legend(handles=legend_patches, loc='center left', bbox_to_anchor=(1, 0.5), prop=font_prop)
    plt.show()

    
    # curve chart
    line1, = plt.plot(weight_allocation, risk_contribution_spy)
    line2, = plt.plot(weight_allocation, risk_contribution_govt)
    plt.xlabel('Weight Allocation (%)')
    plt.ylabel('Risk Contribution (%)')
    plt.xticks(weight_allocation)
    plt.title('Weight Allocation vs. Risk Contribution')
    plt.legend((line1,line2),['SPY','GOVT'])
    plt.show()
    
plot_graph()

    