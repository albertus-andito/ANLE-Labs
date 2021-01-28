import matplotlib.pyplot as plt
import scipy
from nltk.corpus import wordnet as wn, wordnet_ic as wn_ic, lin_thesaurus as lin

brown_ic = wn_ic.ic("ic-brown.dat")


def noun_path_similarity(noun_1, noun_2):
    """
    Returns path similarity of two nouns
    :param noun_1:
    :param noun_2:
    :return: path similarity
    """
    synsets_1 = wn.synsets(noun_1, wn.NOUN)
    synsets_2 = wn.synsets(noun_2, wn.NOUN)
    return round(max([synset_1.path_similarity(synset_2) for synset_1 in synsets_1 for synset_2 in synsets_2]), 4)


def noun_similarity(noun_1, noun_2, sim_measure=None):
    """
    Returns similarity between two nouns using the similarity measure defined.
    :param noun_1:
    :param noun_2:
    :param sim_measure: 'path_similarity', 'res_similarity', 'lin_similarity'
    :return: similarity measure
    """
    synsets_1 = wn.synsets(noun_1, wn.NOUN)
    synsets_2 = wn.synsets(noun_2, wn.NOUN)
    if sim_measure is None or sim_measure == 'path_similarity':
        return round(max([synset_1.path_similarity(synset_2) for synset_1 in synsets_1 for synset_2 in synsets_2]), 4)
    if sim_measure == 'res_similarity':
        return round(
            max([synset_1.res_similarity(synset_2, brown_ic) for synset_1 in synsets_1 for synset_2 in synsets_2]), 4)
    if sim_measure == 'lin_similarity':
        return round(
            max([synset_1.lin_similarity(synset_2, brown_ic) for synset_1 in synsets_1 for synset_2 in synsets_2]), 4)
    raise ValueError('sim_measure value is unexpected')


def plot_scatter_with_regression(dataframe, x_column, y_column):
    """
    Plot a scatter graph between x_column and y_column, with a regression line displayed on the graph.
    Spearman correlation coefficient, p-value, and regression correlation coefficient are also displayed in a textbox.
    :param dataframe:
    :param x_column:
    :param y_column:
    :return:
    """
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

    corr, pvalue = scipy.stats.spearmanr(dataframe[x_column], dataframe[y_column])
    regression = scipy.stats.linregress(dataframe[x_column], dataframe[y_column])
    ax = dataframe.plot.scatter(x=x_column, y=y_column,
                                title='Correlation between ' + x_column + ' and ' + y_column)
    textstr = '\n'.join((
        r'spearman-corr=%.4f' % (corr,),
        r'p-value=%f' % (pvalue,),
        r'regression-corr=%.4f' % (regression.rvalue,)
    ))
    ax.text(0.6, 0.3, textstr, transform=ax.transAxes, fontsize=14,
            verticalalignment='top', bbox=props)
    plt.plot(dataframe[x_column], regression.intercept + regression.slope * dataframe[x_column], 'r')
    plt.show()
