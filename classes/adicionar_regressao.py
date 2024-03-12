from sklearn.linear_model import LinearRegression

class RegressionLineAdder:
    def add_regression_line(self, ax, x, y):
        model = LinearRegression()
        model.fit(x, y)
        Y_pred = model.predict(x)
        ax.plot(x, Y_pred, color='red')
        return ax