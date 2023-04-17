import numpy as np
import scipy.stats
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import stats, ttest_ind


# y = mx + c

class LinReg:
    def __init__(self, x, y):  # currently: x and y would be dataframe columns
        self.x = x  # this separation doesn't check length
        self.y = y
        self.model = LinearRegression().fit(self.x, self.y)
        self.r_sq = self.model.score(x, y)
        self.intercept = self.model.intercept_
        self.slope = self.model.coef_
        self.rank_order_correlation = stats.spearmanr(x, y).correlation
        self.p_value = stats.spearmanr(x, y).pvalue

    def give_summary(self):
        return {"coefficent of determiniation": self.r_sq,
                "intercept": self.intercept,
                "slope": self.slope,
                "rank-order correlation": self.rank_order_correlation,
                "p-value": self.p_value}


def data_to_array(data, x_col_name, y_col_name):
    x = np.array(data[x_col_name]).reshape((-1, 1))
    y = np.array(data[y_col_name])
    return x, y


def generate_linear_regression_model(x, y):
    model = LinearRegression().fit(x, y)


def generate_metrics(x, y):
    model = LinearRegression().fit(x, y)
    r_sq = model.score(x, y)
    intercept = model.intercept_  # = c
    slope = model.coef_  # = m
    spearman_nums = stats.spearmanr(x, y)
    return {"coefficient of determination": r_sq,
            "intercept": intercept,
            "slope": slope,
            "spearman rank-order correlation": spearman_nums.correlation,
            "p-value": spearman_nums.pvalue}


def generate_predicted_line(x, y):
    model = LinearRegression().fit(x, y)
    y_pred = model.predict(x)
    return y_pred


def graph_data(x, y, show=False, save=False, output_file=""):
    plt.plot(x, y, 'o')
    y_pred = generate_predicted_line(x, y)
    plt.plot(x, y_pred)
    if show:
        plt.show()
    if save:
        plt.savefig(output_file)
