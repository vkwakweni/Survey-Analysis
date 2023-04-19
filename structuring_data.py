import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd


class LinReg:
    def __init__(self, x, y, x_name, y_name):
        self.x = x
        self.y = y
        self.x_var = x_name
        self.y_var = y_name
        self.model = LinearRegression().fit(self.x, self.y)
        self.r_sq = self.model.score(x, y)
        self.intercept = self.model.intercept_
        self.slope = self.model.coef_
        x_listed = [v[0] for v in x.tolist()]
        y_listed = y.tolist()
        self.rank_order_correlation = stats.spearmanr(x_listed, y_listed).correlation
        self.p_value = stats.spearmanr(x_listed, y_listed).pvalue
        self.x_shapiro_p = stats.shapiro(x)
        self.y_shapiro_p = stats.shapiro(y)
        self.y_pred = self.model.predict(x)

    def give_summary(self):
        summary = pd.DataFrame(data={"coefficient of determination": self.r_sq,
                                     "intercept": self.intercept,
                                     "slope": self.slope,
                                     "rank-order correlation (spearman)": self.rank_order_correlation,
                                     "p-value": self.p_value,
                                     "shapiro p-value tests for x": self.x_shapiro_p[1],
                                     "shapiro p-value tests for y": self.y_shapiro_p[1],
                                     "min for x": np.min(self.x),
                                     "Q1 for x": np.percentile(self.x, 25),
                                     "median for x": np.percentile(self.x, 50),
                                     "Q3 for x": np.percentile(self.x, 75),
                                     "max for x": np.max(self.y),
                                     "standard deviation for x": np.std(self.x),
                                     "mean for x": np.mean(self.x),
                                     "min for y": np.min(self.y),
                                     "Q1 for y": np.percentile(self.y, 25),
                                     "median for y": np.percentile(self.y, 50),
                                     "Q3 for y": np.percentile(self.y, 75),
                                     "max for y": np.max(self.y),
                                     "standard deviation for y": np.std(self.y),
                                     "mean for y": np.mean(self.y)})
        summary = summary.T
        summary.columns = [f"x = {self.x_var}; y = {self.y_var}"]
        return summary

    def graph_data(self, show=False, save=False, output_file=""):
        plt.xlabel(self.x_var)
        plt.ylabel(self.y_var)
        plt.plot(self.x, self.y, 'o')
        plt.plot(self.x, self.y_pred)
        if show:
            plt.show()
        if save:
            plt.savefig(output_file)
        plt.clf()


def data_to_array(data, x_col_name, y_col_name):
    x = np.array(data[x_col_name]).reshape((-1, 1))
    y = np.array(data[y_col_name])
    return x, y
