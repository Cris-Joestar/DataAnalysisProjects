import numpy as np

def calculate(lista):
    if len(lista) != 9:
        raise ValueError('List must contain nine numbers.')

    numbers = np.array(lista).reshape(3, 3)
    means = [
        np.mean(numbers, axis=0).tolist(),
        np.mean(numbers, axis=1).tolist(),
        np.mean(numbers).tolist()
    ]
    variances = [
        np.var(numbers, axis=0).tolist(),
        np.var(numbers, axis=1).tolist(),
        np.var(numbers).tolist()
    ]
    stddevs = [
        np.std(numbers, axis=0).tolist(),
        np.std(numbers, axis=1).tolist(),
        np.std(numbers).tolist()
    ]
    maxs = [
        np.max(numbers, axis=0).tolist(),
        np.max(numbers, axis=1).tolist(),
        np.max(numbers).tolist()
    ]
    mins = [
        np.min(numbers, axis=0).tolist(),
        np.min(numbers, axis=1).tolist(),
        np.min(numbers).tolist()
    ]
    sums = [
        np.sum(numbers, axis=0).tolist(),
        np.sum(numbers, axis=1).tolist(),
        np.sum(numbers).tolist()
    ]
    
    stats = {
        'mean': means,
        'variance': variances,
        'standard deviation': stddevs,
        'max': maxs,
        'min': mins,
        'sum': sums
    }
    
    return stats
    stats = {
        'mean': means,
        'variance': variances,
        'standart deviation': desviations,
        'max': maximums,
        'min': minima,
        'sum': sums
    }
    return stats
