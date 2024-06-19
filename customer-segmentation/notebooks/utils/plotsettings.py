import matplotlib.pyplot as plt
import seaborn as sns

def settings():
    plt.rcdefaults()
    sns.set_style('whitegrid')

    # Set custom figure parameters
    plt.rcParams.update({
        'axes.labelcolor':      '#4C4C4C',   # label parameters
        'axes.labelpad':        20, 

        'axes.spines.top':      False,       # border parameters
        'axes.spines.right':    False,     
        'axes.spines.bottom':   False,    
        'axes.spines.left':     False,    

        'axes.titlecolor':      '#4C4C4C',   # title parameters
        'axes.titlepad':        20,            
        'axes.titlesize':       20,           

        "figure.dpi":           200,         # figure parameter

        'grid.linewidth':       0.5,         # grid parameter

        'xtick.color':          "#89939C",   # ticks parameters
        'xtick.labelcolor':     "#89939C",  
        'xtick.major.width':    1,
        'ytick.color':          "#89939C",
        'ytick.labelcolor':     "#89939C",
        'ytick.major.width':    1,
    })