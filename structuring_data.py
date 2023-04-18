import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import scipy.stats as stats


# y = mx + c

class LinReg:
    def __init__(self, x, y):
        self.x = x  # this separation doesn't check length
        self.y = y
        self.model = LinearRegression().fit(self.x, self.y)
        self.r_sq = self.model.score(x, y)
        self.intercept = self.model.intercept_
        self.slope = self.model.coef_
        x_listed = [v[0] for v in x.tolist()]
        y_listed = y.tolist()
        self.rank_order_correlation = stats.pearsonr(x_listed, y_listed)[0]
        self.p_value = stats.pearsonr(x_listed, y_listed)[1]
        self.x_shapiro_p = stats.shapiro(x)
        self.y_shapiro_p = stats.shapiro(y)
        self.y_pred = self.model.predict(x)

    def give_summary(self):
        return {"coefficient of determination": self.r_sq,
                "intercept": self.intercept,
                "slope": self.slope,
                "rank-order correlation": self.rank_order_correlation,
                "p-value": self.p_value,
                "shapiro tests": {"x": self.x_shapiro_p[1], "y": self.y_shapiro_p[1]}}

    def graph_data(self, x_name="", y_name="", show=False, save=False, output_file=""):
        plt.plot(self.x, self.y, 'o')
        plt.plot(self.x, self.y_pred)
        if show:
            plt.show()
        if save:
            plt.savefig(output_file)


def data_to_array(data, x_col_name, y_col_name):
    x = np.array(data[x_col_name]).reshape((-1, 1))
    y = np.array(data[y_col_name])
    return x, y

