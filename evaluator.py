__author__ = 'Ajay Thampi'

import numpy as np
import matplotlib.pyplot as plt

def compute_ape(y_pred, y_test):
    return np.abs(np.array(y_pred) - np.array(y_test)) / np.array(y_test) * 100

def compute_accuracy(y_pred, y_test):
    accuracies = 100 - compute_ape(y_pred, y_test)
    return accuracies.clip(0)

def compute_ae(y_pred, y_test):
    return np.abs(np.array(y_pred) - np.array(y_test))

def compute_se(y_pred, y_test):
    return np.abs(np.array(y_pred) - np.array(y_test)) ** 2

def plot_pc_distribution(values, xlabel, title, bin_width=5):
    hist, bins = np.histogram(values, bins=np.arange(0, 101, bin_width))
    hist = hist / len(values) * 100
    width = np.diff(bins)
    center = (bins[:-1] + bins[1:]) / 2

    fig, ax = plt.subplots(figsize=(8,3))
    ax.bar(center, hist, align='center', width=width)
    ax.grid(True)
    ax.set_xticks(bins)
    ax.set_xlabel(xlabel)
    ax.set_ylabel('% of cases')
    ax.set_title(title)
    return fig, ax

def plot_feature_importance(feature_importance, feature_names=None, title='Feature Importance', rotation=90, xlabel='Features'):
    indices = np.argsort(feature_importance)[::-1]
    fig, ax = plt.subplots()
    ax.bar(range(len(indices)), feature_importance[indices])
    if feature_names is None:
        names = indices
    else:
        names = [feature_names[i] for i in indices]
    plt.xticks(range(len(indices)), names, rotation=rotation, fontsize=10)
    ax.set_title(title)
    ax.grid(True)
    ax.set_ylabel('Feature Importance')
    ax.set_xlabel(xlabel)
    return fig, ax

def interpret_principal_components(pca, feature_names, top=5):
    ev_ratio = pca.explained_variance_ratio_
    ev_indices = np.argsort(ev_ratio)[::-1]
    components = range(len(ev_ratio))
    print('EXPLANATION OF VARIANCE')
    for idx, ev_idx in enumerate(ev_indices):
        print('\tComponent %d explains %.4f%% of variance' % (components[ev_idx], ev_ratio[ev_idx] * 100))

    pca_components = pca.components_
    for idx, component in enumerate(components):
        pca_component = pca_components[idx, :]
        top_feature_indices = np.argsort(pca_component)[::-1]
        top_features = []
        for i in range(top):
            top_feature_index = top_feature_indices[i]
            top_features.append(feature_names[top_feature_index])
        print(f'Top {top} features for component {component}: {top_features}')