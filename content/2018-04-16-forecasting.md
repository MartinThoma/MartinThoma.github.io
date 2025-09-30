---
layout: post
lang: en
title: Forecasting
slug: forecasting
author: Martin Thoma
date: 2018-04-16 20:00
category: Machine Learning
tags: Machine Learning, Regression, Time Series
featured_image: logos/ml.png
---
Today, I played a bit with the [International airline passengers dataset](https://datamarket.com/data/set/22u3/international-airline-passengers-monthly-totals-in-thousands-jan-49-dec-60#!ds=22u3&display=line).

It's only feature is a date given by year and month. One should predict the
number of passengers (in thousands).


## Code

See [Github](https://github.com/MartinThoma/algorithms/blob/master/ML/regression/airline-passengers/main.py).


## Results

See the scoring functions are explained in the <a href="https://martin-thoma.com/regression/">regression article</a>.

<table class="table">
<tr>
    <th>name</th>
    <th>training time</th>
    <th>testing time</th>
    <th><a href="https://en.wikipedia.org/wiki/Mean_absolute_error" title="Mean absolute error">MAE</a></th>
    <th><a href="https://en.wikipedia.org/wiki/Median_absolute_deviation" title="Median absolute deviation">MAD</a></th>
    <th><a href="https://en.wikipedia.org/wiki/Coefficient_of_determination">$R^2$</a></th>
    <th><a href="http://scikit-learn.org/stable/modules/generated/sklearn.metrics.explained_variance_score.html">explained variance</a></th>
    <th><a href="https://en.wikipedia.org/wiki/Mean_squared_error" title="Mean squared error">MSE</a></th>
<tr>
<tr>
    <td>GradientBoostingRegressor</td>
    <td>11.6ms</td>
    <td> 0.1ms</td>
    <td style="background-color: green;">40.0</td>
    <td style="background-color: green;">31.0</td>
    <td style="background-color: green;">0.5689</td>
    <td style="background-color: green;">0.6246</td>
    <td style="background-color: green;">2631.9</td>
</tr>
<tr>
    <td>GaussianProcessRegressor</td>
    <td> 8.4ms</td>
    <td> 0.2ms</td>
    <td style="background-color: red;">150.9</td>
    <td>85.9</td>
    <td style="background-color: red;">-8.0324</td>
    <td style="background-color: red;">-6.7089</td>
    <td style="background-color: red;">55138.3</td>
</tr>
<tr>
    <td>AdaBoostRegressor</td>
    <td style="background-color: red;">69.3ms</td>
    <td> 1.1ms</td>
    <td>60.1</td>
    <td>53.3</td>
    <td style="background-color: green;">0.1240</td>
    <td>0.5812</td>
    <td style="background-color: red;">5347.3</td>
</tr>
<tr>
    <td>SGDRegressor</td>
    <td> 0.8ms</td>
    <td> 0.1ms</td>
    <td style="background-color: red;">106.5</td>
    <td>84.8</td>
    <td style="background-color: red;">-1.7081</td>
    <td style="background-color: red;">0.1471</td>
    <td>16531.5</td>
</tr>
<tr>
    <td><a href="http://scikit-learn.org/stable/modules/linear_model.html#ransac-random-sample-consensus">RANSACRegressor</a></td>
    <td> 4.1ms</td>
    <td style="background-color: green;"> 0.0ms</td>
    <td>68.5</td>
    <td>39.4</td>
    <td style="background-color: red;">-0.4294</td>
    <td style="background-color: red;">0.1479</td>
    <td>8726.0</td>
</tr>
<tr>
    <td><a href="http://scikit-learn.org/stable/modules/linear_model.html#passive-aggressive">PassiveAggressiveRegressor</a></td>
    <td style="background-color: green;"> 0.2ms</td>
    <td style="background-color: green;"> 0.0ms</td>
    <td style="background-color: red;">115.8</td>
    <td style="background-color: red;">115.5</td>
    <td style="background-color: red;">-1.8841</td>
    <td style="background-color: red;">0.1268</td>
    <td>17606.2</td>
</tr>
<tr>
    <td>BaggingRegressor</td>
    <td>13.4ms</td>
    <td> 0.9ms</td>
    <td>46.7</td>
    <td>37.1</td>
    <td>0.4162</td>
    <td>0.4912</td>
    <td>3564.0</td>
</tr>
<tr>
    <td><a href="http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html">HuberRegressor</a></td>
    <td> 8.0ms</td>
    <td style="background-color: green;"> 0.0ms</td>
    <td>65.4</td>
    <td>59.8</td>
    <td style="background-color: red;">-0.0745</td>
    <td>0.0395</td>
    <td>6559.5</td>
</tr>
<tr>
    <td>RandomForestRegressor</td>
    <td style="background-color: red;">18.6ms</td>
    <td> 5.2ms</td>
    <td>48.3</td>
    <td>38.5</td>
    <td>0.4336</td>
    <td style="background-color: green;">0.6535</td>
    <td>3457.7</td>
</tr>
    <tr>
        <td><a href="http://xgboost.readthedocs.io/en/latest/python/python_api.html">XGBoost</a></td>
        <td> 5.5ms</td>
        <td> 0.1ms</td>
        <td>49.3</td>
        <td>37.7</td>
        <td>0.4139</td>
        <td>0.7215</td>
        <td>3578.1</td>
    </tr>
<tr>
    <td>ExtraTreesRegressor</td>
    <td style="background-color: red;">17.2ms</td>
    <td> 4.7ms</td>
    <td>44.1</td>
    <td>33.2</td>
    <td>0.4744</td>
    <td>0.5036</td>
    <td>3208.6</td>
</tr>
<tr>
    <td><a href="https://martin-thoma.com/svm-with-sklearn/">RBF SVR</a></td>
    <td> 2.1ms</td>
    <td> 0.3ms</td>
    <td style="background-color: red;">202.2</td>
    <td style="background-color: red;">182.0</td>
    <td style="background-color: red;">-6.6885</td>
    <td style="background-color: red;">0.0105</td>
    <td style="background-color: red;">46934.4</td>
</tr>
<tr>
    <td>Linear SVR + Standardscaler</td>
    <td> 1.4ms</td>
    <td> 0.2ms</td>
    <td>84.1</td>
    <td>60.6</td>
    <td style="background-color: red;">-0.9573</td>
    <td style="background-color: red;">0.1338</td>
    <td>11948.3</td>
</tr>
<tr>
    <td><a href="http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html">LinearRegression</a></td>
    <td>10.8ms</td>
    <td> 0.1ms</td>
    <td>55.9</td>
    <td>41.9</td>
    <td>0.1068</td>
    <td style="background-color: red;">0.1700</td>
    <td>5452.5</td>
</tr>
<tr>
    <td><a href="http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html">ElasticNet</a></td>
    <td> 0.3ms</td>
    <td style="background-color: green;"> 0.0ms</td>
    <td>56.0</td>
    <td>41.7</td>
    <td>0.1069</td>
    <td style="background-color: red;">0.1698</td>
    <td>5452.0</td>
</tr>
<tr>
    <td><a href="http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html">Lasso</a></td>
    <td> 0.4ms</td>
    <td style="background-color: green;"> 0.0ms</td>
    <td>56.0</td>
    <td>41.5</td>
    <td>0.1069</td>
    <td style="background-color: red;">0.1698</td>
    <td>5451.8</td>
</tr>
</table>

I like the median absolute error best, because it tells me how many passengers
my prediction is typically away from the true prediction.

Please note that bad results here do not mean the regressor is bad. Some might
just use their full potential with more data, some might be better suited to
different regression problems, e.g. interpolation instead of extrapolation or
working with higher dimensional data.


## Graphs

Plotting the prediction is crucial for extrapolation. What we can see in those
images is that there are two things to match: A global trend and local
seasonality-effects. To make it easier to digest, I already put them in the
table. Just click on them to see them in full size:


<table class="table">
    <thead>
    <tr>
        <th>Model</th>
        <th>Trend</th>
        <th>Seasonality</th>
        <th>Graph</th>
        <th>Comment</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>RBF SVR</td>
        <td><span style="color:red;" title="No">&#10008;</span></td>
        <td><span style="color:red;" title="No">&#10008;</span></td>
        <td><figure class="wp-caption aligncenter img-thumbnail">
    <a href="../images/2018/04/airline-passengers-train-SVR.png"><img src="../images/2018/04/airline-passengers-train-SVR.png" alt="RBF SVR for extrapolation." style="width: 128px;"/></a></figure></td>
        <td>Doesn't learn anything useful at all</td>
    </tr>
    <tr>
        <td>GaussianProcessRegressor</td>
        <td><span style="color:red;" title="No">&#10008;</span></td>
        <td>Kind of</td>
        <td><a href="../images/2018/04/airline-passengers-train-GaussianProcessRegressor.png"><figure class="wp-caption aligncenter img-thumbnail">
    <img src="../images/2018/04/airline-passengers-train-GaussianProcessRegressor.png" alt="GaussianProcessRegressor for extrapolation." style="width: 128px;"/></figure></a></td>
        <td>Overshoots extremely</td>
    </tr>
    <tr>
        <td>AdaBoostRegressor</td>
        <td><span style="color:red;" title="No">&#10008;</span></td>
        <td><span style="color:green;" title="Yes">&#10004;</span></td>
        <td><figure class="wp-caption aligncenter img-thumbnail">
    <a href="../images/2018/04/airline-passengers-train-AdaBoostRegressor.png"><img src="../images/2018/04/airline-passengers-train-AdaBoostRegressor.png" alt="AdaBoostRegressor for extrapolation." style="width: 128px;"/></a></figure></td>
        <td></td>
    </tr>
    <tr>
        <td>BaggingRegressor</td>
        <td><span style="color:red;" title="No">&#10008;</span></td>
        <td><span style="color:green;" title="Yes">&#10004;</span></td>
        <td><a href="../images/2018/04/airline-passengers-train-BaggingRegressor.png"><figure class="wp-caption aligncenter img-thumbnail">
    <img src="../images/2018/04/airline-passengers-train-BaggingRegressor.png" alt="BaggingRegressor for extrapolation." style="width: 128px;"/></figure></a></td>
        <td></td>
    </tr>
    <tr>
        <td>XGBoost</td>
        <td><span style="color:red;" title="No">&#10008;</span></td>
        <td><span style="color:green;" title="Yes">&#10004;</span></td>
        <td><a href="../images/2018/04/airline-passengers-train-XGBoost.png"><figure class="wp-caption aligncenter img-thumbnail">
    <img src="../images/2018/04/airline-passengers-train-XGBoost.png" alt="XGBoost for extrapolation." style="width: 128px;"/></figure></a></td>
        <td></td>
    </tr>
    <tr>
        <td>ExtraTreesRegressor</td>
        <td><span style="color:red;" title="No">&#10008;</span></td>
        <td><span style="color:green;" title="Yes">&#10004;</span></td>
        <td><a href="../images/2018/04/airline-passengers-train-ExtraTreesRegressor.png"><figure class="wp-caption aligncenter img-thumbnail">
    <img src="../images/2018/04/airline-passengers-train-ExtraTreesRegressor.png" alt="ExtraTreesRegressor for extrapolation." style="width: 128px;"/></figure></a></td>
        <td>Note the extreme overfitting</td>
    </tr>
    <tr>
        <td>RandomForestRegressor</td>
        <td><span style="color:red;" title="No">&#10008;</span></td>
        <td><span style="color:green;" title="Yes">&#10004;</span></td>
        <td><a href="../images/2018/04/airline-passengers-train-RandomForestRegressor.png"><figure class="wp-caption aligncenter img-thumbnail">
    <img src="../images/2018/04/airline-passengers-train-RandomForestRegressor.png" alt="RandomForestRegressor for extrapolation." style="width: 128px;"/></figure></a></td>
        <td></td>
    </tr>
    <tr>
        <td>GradientBoostingRegressor</td>
        <td><span style="color:red;" title="No">&#10008;</span></td>
        <td><span style="color:green;" title="Yes">&#10004;</span></td>
        <td><a href="../images/2018/04/airline-passengers-train-GradientBoostingRegressor.png"><figure class="wp-caption aligncenter img-thumbnail">
    <img src="../images/2018/04/airline-passengers-train-GradientBoostingRegressor.png" alt="GradientBoostingRegressor for extrapolation." style="width: 128px;"/></figure></a></td>
        <td></td>
    </tr>
    <tr>
        <td>Lasso</td>
        <td><span style="color:green;" title="Yes">&#10004;</span></td>
        <td><span style="color:red;" title="No">&#10008;</span></td>
        <td><a href="../images/2018/04/airline-passengers-train-Lasso.png"><figure class="wp-caption aligncenter img-thumbnail">
    <img src="../images/2018/04/airline-passengers-train-Lasso.png" alt="Lasso for extrapolation." style="width: 128px;"/></figure></a></td>
        <td></td>
    </tr>
    <tr>
        <td>Linear SVR</td>
        <td><span style="color:green;" title="Yes">&#10004;</span></td>
        <td><span style="color:red;" title="No">&#10008;</span></td>
        <td><a href="../images/2018/04/airline-passengers-train-Linear SVR.png"><figure class="wp-caption aligncenter img-thumbnail">
    <img src="../images/2018/04/airline-passengers-train-Linear SVR.png" alt="Linear SVR for extrapolation." style="width: 128px;"/></figure></a></td>
        <td></td>
    </tr>
    <tr>
        <td>RANSACRegressor</td>
        <td><span style="color:green;" title="Yes">&#10004;</span></td>
        <td><span style="color:red;" title="No">&#10008;</span></td>
        <td><a href="../images/2018/04/airline-passengers-train-RANSACRegressor.png"><figure class="wp-caption aligncenter img-thumbnail">
    <img src="../images/2018/04/airline-passengers-train-RANSACRegressor.png" alt="RANSACRegressor for extrapolation." style="width: 128px;"/></figure></a></td>
        <td></td>
    </tr>
    <tr>
        <td>LinearRegression</td>
        <td><span style="color:green;" title="Yes">&#10004;</span></td>
        <td><span style="color:red;" title="No">&#10008;</span></td>
        <td><a href="../images/2018/04/airline-passengers-train-LinearRegression.png"><figure class="wp-caption aligncenter img-thumbnail">
    <img src="../images/2018/04/airline-passengers-train-LinearRegression.png" alt="LinearRegression for extrapolation." style="width: 128px;"/></figure></a></td>
        <td></td>
    </tr>
    <tr>
        <td>ElasticNet</td>
        <td><span style="color:green;" title="Yes">&#10004;</span></td>
        <td><span style="color:red;" title="No">&#10008;</span></td>
        <td><a href="../images/2018/04/airline-passengers-train-ElasticNet.png"><figure class="wp-caption aligncenter img-thumbnail">
    <img src="../images/2018/04/airline-passengers-train-ElasticNet.png" alt="ElasticNet for extrapolation." style="width: 128px;"/></figure></a></td>
        <td></td>
    </tr>
    <tr>
        <td>SGDRegressor</td>
        <td><span style="color:green;" title="Yes">&#10004;</span></td>
        <td><span style="color:red;" title="No">&#10008;</span></td>
        <td><figure class="wp-caption aligncenter img-thumbnail"><a href="../images/2018/04/airline-passengers-train-SGDRegressor.png"><img src="../images/2018/04/airline-passengers-train-SGDRegressor.png" alt="SGDRegressor for extrapolation." style="width: 128px;"/></a>
    </figure></td>
        <td></td>
    </tr>
    <tr>
        <td>HuberRegressor</td>
        <td><span style="color:green;" title="Yes">&#10004;</span></td>
        <td><span style="color:green;" title="Yes">&#10004;</span></td>
        <td><a href="../images/2018/04/airline-passengers-train-HuberRegressor.png"><figure class="wp-caption aligncenter img-thumbnail">
    <img src="../images/2018/04/airline-passengers-train-HuberRegressor.png" alt="HuberRegressor for extrapolation." style="width: 128px;"/></figure></a></td>
        <td>Both are captured pretty bad</td>
    </tr>
    <tr>
        <td>PassiveAggressiveRegressor</td>
        <td><span style="color:green;" title="Yes">&#10004;</span></td>
        <td><span style="color:green;" title="Yes">&#10004;</span></td>
        <td><a href="../images/2018/04/airline-passengers-train-PassiveAggressiveRegressor.png"><figure class="wp-caption aligncenter img-thumbnail">
    <img src="../images/2018/04/airline-passengers-train-PassiveAggressiveRegressor.png" alt="PassiveAggressiveRegressor for extrapolation." style="width: 128px;"/></figure></a></td>
        <td>Both are captured pretty bad</td>
    </tr>
</tbody>
</table>

Seeing this result, I decided to have two models: One which predicts the trend
and one which predicts seasonality effects.

## Combining models

The simplest way to combine two regression models is by

$$f(x) = f_1(x) + f_2(x)$$

But I also want to simpify the training. So I decided to have the following
training setup:

1. Fit $f_1$ on the training dataset, where $f_1$ has to predict the global
   trend and thus solve the extrapolation problem. Lasso seems to be a good
   choice.
2. Transform the training data $(X, y)$: $$y' = y - f_1(X)$$
3. Fit $f_2$ on $(X, y')$. So $f_2$ has to solve an interpolation problem.

I call this model `TrendSeasonRegressor`. Let's try a few combinations:

<table class="table" id="combinedModelScores">
    <thead>
    <tr>
        <th>$f_1$</th>
        <th>$f_2$</th>
    <th><a href="https://en.wikipedia.org/wiki/Mean_absolute_error" title="Mean absolute error">MAE</a></th>
    <th><a href="https://en.wikipedia.org/wiki/Median_absolute_deviation" title="Median absolute deviation">MAD</a></th>
    <th><a href="https://en.wikipedia.org/wiki/Coefficient_of_determination">$R^2$</a></th>
    <th><a href="http://scikit-learn.org/stable/modules/generated/sklearn.metrics.explained_variance_score.html">explained variance</a></th>
    <th><a href="https://en.wikipedia.org/wiki/Mean_squared_error" title="Mean squared error">MSE</a></th>
        <th>Image</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td colspan="2">GradientBoostingRegressor</td>
        <td style="background-color: red;">40.0</td>
        <td style="background-color: red;">31.0</td>
        <td style="background-color: red;">0.5689</td>
        <td style="background-color: red;">0.6246</td>
        <td style="background-color: red;">2631.9</td>
        <td><figure class="wp-caption aligncenter img-thumbnail">
            <a href="../images/2018/04/airline-passengers-train-GradientBoostingRegressor.png"><img src="../images/2018/04/airline-passengers-train-GradientBoostingRegressor.png" alt="Gradient Boosting Regressor" style="width: 128px;"/></a>
        </figure></td>
    </tr>
    <tr>
        <td>Linear Regression</td>
        <td>ExtraTrees</td>
        <td style="background-color: green;">19.1</td>
        <td style="background-color: green;">14.5</td>
        <td style="background-color: green;">0.8958</td>
        <td style="background-color: green;">0.9096</td>
        <td style="background-color: green;">636.1</td>
        <td><figure class="wp-caption aligncenter img-thumbnail">
            <a href="../images/2018/04/airline-passengers-train-ResidualRegressor-LinearExtra.png"><img src="../images/2018/04/airline-passengers-train-ResidualRegressor-LinearExtra.png" alt="Linear Regression combined with Extra Trees" style="width: 128px;"/></a>
        </figure></td>
    </tr>
    <tr>
        <td>Lasso</td>
        <td>ExtraTrees</td>
        <td style="background-color: green;">20.8</td>
        <td style="background-color: green;">16.6</td>
        <td style="background-color: green;">0.8803</td>
        <td style="background-color: green;">0.8992</td>
        <td style="background-color: green;">730.9</td>
        <td><figure class="wp-caption aligncenter img-thumbnail">
            <a href="../images/2018/04/airline-passengers-train-TrendSeasonRegressor_Lasso_ExtraTrees.png"><img src="../images/2018/04/airline-passengers-train-TrendSeasonRegressor_Lasso_ExtraTrees.png" alt="Text" style="width: 128px;"/></a>
        </figure></td>
    </tr>
    <tr>
        <td>ElasticNet</td>
        <td>ExtraTrees</td>
        <td>25.2</td>
        <td>24.4</td>
        <td>0.8382</td>
        <td>0.8403</td>
        <td>988.0</td>
        <td><figure class="wp-caption aligncenter img-thumbnail">
            <a href="../images/2018/04/airline-passengers-train-TrendSeasonRegressor_ElasticNet_ExtraTrees.png"><img src="../images/2018/04/airline-passengers-train-TrendSeasonRegressor_ElasticNet_ExtraTrees.png" alt="Text" style="width: 128px;"/></a>
        </figure></td>
    </tr>
    <tr>
        <td>LinearSVR</td>
        <td>ExtraTrees</td>
        <td>36.4</td>
        <td style="background-color: red;">31.1</td>
        <td style="background-color: red;">0.6841</td>
        <td style="background-color: red;">0.7081</td>
        <td style="background-color: red;">1928.2</td>
        <td><figure class="wp-caption aligncenter img-thumbnail">
            <a href="../images/2018/04/airline-passengers-train-TrendSeasonRegressor_LinearSVR_ExtraTrees.png"><img src="../images/2018/04/airline-passengers-train-TrendSeasonRegressor_LinearSVR_ExtraTrees.png" alt="Text" style="width: 128px;"/></a>
        </figure></td>
    </tr>
    <tr>
        <td>LinearSVR</td>
        <td>Adaboost</td>
        <td>33.7</td>
        <td style="background-color: red;">32.6</td>
        <td style="background-color: red;">0.6918</td>
        <td style="background-color: red;">0.7849</td>
        <td style="background-color: red;">1881.5</td>
        <td><figure class="wp-caption aligncenter img-thumbnail">
            <a href="../images/2018/04/airline-passengers-train-TrendSeasonRegressor_LinearSVR_Adaboost.png"><img src="../images/2018/04/airline-passengers-train-TrendSeasonRegressor_LinearSVR_Adaboost.png" alt="Text" style="width: 128px;"/></a>
        </figure></td>
    </tr>
    <tr>
        <td>Lasso</td>
        <td>Adaboost</td>
        <td>26.5</td>
        <td>18.9</td>
        <td>0.8034</td>
        <td>0.8143</td>
        <td style="background-color: red;">1200.4</td>
        <td><figure class="wp-caption aligncenter img-thumbnail">
            <a href="../images/2018/04/airline-passengers-train-TrendSeasonRegressor_Lasso_Adaboost.png"><img src="../images/2018/04/airline-passengers-train-TrendSeasonRegressor_Lasso_Adaboost.png" alt="Text" style="width: 128px;"/></a>
        </figure></td>
    </tr>
    <tr>
        <td>ElasticNet</td>
        <td>Adaboost</td>
        <td>26.5</td>
        <td>19.4</td>
        <td>0.8098</td>
        <td>0.8229</td>
        <td style="background-color: red;">1161.2</td>
        <td><figure class="wp-caption aligncenter img-thumbnail">
            <a href="../images/2018/04/airline-passengers-train-TrendSeasonRegressor_ElasticNet_Adaboost.png"><img src="../images/2018/04/airline-passengers-train-TrendSeasonRegressor_ElasticNet_Adaboost.png" alt="Text" style="width: 128px;"/></a>
        </figure></td>
    </tr>
</tbody>
</table>

This looks a lot better! Note how the best model before is now the worst!

However, even with this combination the Gaussian Processes were really bad.
Overshooting like hell.

Next thing to improve: The scaling of the the seasonal trend is not captured so
far.

Another idea I want to dig into is that of residual learning. Where I have only
one model learning the residual of another model, you can chain arbitary many.
The `ResidualRegressor` is a meta-regressor. If it is given one model, it
behaves exactly like that model. If it is given two models, then it behaves
exactly like the `TrendSeasonRegressor`.

Sadly, for the given data and the models I've tried, three models behaved not
better than two in the `ResidualRegressor`.


## Human Performance

An interesting excercise is to get a human baseline. This gives you some
insights in how good the models are.

<table>
    <thead>
    <tr>
        <th>Label</th>
        <th>Truth</th>
        <th>Martin</th>
        <th>Person 2</th>
        <th>Person3</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>1958-08</td>
        <td>505</td>
        <td>490 (+15)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1958-09</td>
        <td>404</td>
        <td>440 (+36)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1958-10</td>
        <td>359</td>
        <td>370 (+11)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1958-11</td>
        <td>310</td>
        <td>340 (+30)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1958-12</td>
        <td>337</td>
        <td>360 (+23)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1959-01</td>
        <td>360</td>
        <td>375 (+15)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1959-02</td>
        <td>342</td>
        <td>365 (+23)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1959-03</td>
        <td>406</td>
        <td>410 (+4)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1959-04</td>
        <td>396</td>
        <td>365 (+31)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1959-05</td>
        <td>420</td>
        <td>410 (+10)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1959-06</td>
        <td>472</td>
        <td>500 (+28)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1959-07</td>
        <td>548</td>
        <td>570 (+22)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1959-08</td>
        <td>559</td>
        <td>570 (+11)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1959-09</td>
        <td>463</td>
        <td>490 (+27)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1959-10</td>
        <td>407</td>
        <td>433 (+26)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1959-11</td>
        <td>362</td>
        <td>375 (+13)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1959-12</td>
        <td>405</td>
        <td>400 (+5)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1960-01</td>
        <td>417</td>
        <td>410 (+7)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1960-02</td>
        <td>391</td>
        <td>395 (+4)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1960-03</td>
        <td>419</td>
        <td>460 (+41)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1960-04</td>
        <td>461</td>
        <td>450 (+11)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1960-05</td>
        <td>472</td>
        <td>510 (+38)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1960-06</td>
        <td>535</td>
        <td>570 (+35)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1960-07</td>
        <td>622</td>
        <td>630 (+8)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1960-08</td>
        <td>606</td>
        <td>630 (+24)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1960-09</td>
        <td>508</td>
        <td>550 (+42)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1960-10</td>
        <td>461</td>
        <td>480 (+19)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1960-11</td>
        <td>390</td>
        <td>410 (+20)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1960-12</td>
        <td>432</td>
        <td>440 (+8)</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <th>MAE</th>
        <td>0</td>
        <td>20.24</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <th>MAD</th>
        <td>0</td>
        <td>20.0</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <th>MSE</th>
        <td>0</td>
        <td>539.8</td>
        <td></td>
        <td></td>
    </tr>
    </tbody>
</table>

```text
absolute_errors = [15, 36, 11, 30, 23, 15, 23, 4, 31, 10, 28,22,11,27,26,13,5,7,4,41,11,38,35,8,24,42,19,20,8]
```


## Circular Features

Having the month as a single feature with values from 1 to 12 seems not to be
the best choice. Either a one-hot encoding or a circular encoding (two features
with the trigonometric functions `sin` and `cos`) seem to be the better choice.

Using the circular encoding was interesting. It made the prediction to get
"bumps":

<figure class="wp-caption aligncenter img-thumbnail">
    <img src="../images/2018/04/airline-passengers-train-LinearRegressionCircularBumps.png" alt="Linear Regression with two circular-encoded features for the month" style="width: 512px;"/>
    <figcaption class="text-center">Linear Regression with two circular-encoded features for the month</figcaption>
</figure>

However, both encodings did not yield better results than the simple integer
encoding of a month for this dataset and all tried regressors.


## TODOs

* Make a hand-crafted model
* Get a human baseline
* Make a neural network model


## Learnings

The following should have become clear from reading this blog post:

* L1: SGDRegressor without scaling is crazy bad.
* L2: Without hyperparameter optimization (e.g. [twiddling](https://martin-thoma.com/twiddle/)),
  SVR is shitty.
* L3: Without scaling, linear SVR runs many hours for training. On a dataset with
  3&nbsp;features and less than 150&nbsp;data points.
* L4: Visualizations are powerful for model evaluation and improvement in
      low-dimensional regression problems.


## See also

* [Comparing Classifiers](https://martin-thoma.com/comparing-classifiers/)
* Sklearn: [Choosing the right estimator](http://scikit-learn.org/stable/tutorial/machine_learning_map/index.html)
