# Measurement update
def update(mean1, var1, mean2, var2):
    new_mean = (var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1 / (1 / var1 + 1 / var2)
    return [new_mean, new_var]

# Prediction Update
def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.


for i in range(len(measurements)):
    # Update cycle
    [mu, sig] = update(mu, sig, measurements[i], measurement_sig)
    
    # Predict cycle
    [mu, sig] = predict(mu, sig, motion[i], motion_sig)
    
    print([mu, sig])