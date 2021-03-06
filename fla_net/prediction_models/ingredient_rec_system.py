import pandas as pd
import os
import numpy as np

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
from collections import OrderedDict
from math import isnan

path = os.path.dirname(__file__)

def get_top_replacements(ingredient_name: str, top_n: int = 5):
    if not os.path.exists(os.path.join(path, "cos_compounds.pkl")):
        save_cos_similarities_to_pkl() # This creates both files even though I need just one of them

    cos_comp_ingr = pd.read_pickle(os.path.join(path,"cos_compounds.pkl"))[ingredient_name]

    d_descending = OrderedDict(sorted(cos_comp_ingr.items(), key=lambda kv: kv[1], reverse=True))

    result = {}

    i = 0
    for k, v in d_descending.items():
        i += 1
        if (i > top_n + 1):
            break
        if (k != ingredient_name):
            result[k] = v

    return result


def get_top_recommendations_multiple(ingredient_names: [str], top_n: int = 5):

    top_results = {}

    for ingredient_name in ingredient_names:
        result = get_top_matches(ingredient_name, top_n)

        for k, v in result.items():
            if k in top_results.keys():
                top_results[k] = (top_results[k] + v) / 2 #Keeping the overall value under 1 with '/ 2'
            else:
                top_results[k] = v

    top_results = OrderedDict(sorted(top_results.items(), key=lambda kv: kv[1], reverse=True))
    if top_n < 0:
        [top_results.pop(name) for name in ingredient_names]
        return top_results
    top_results_sliced = {}
    i=0
    for k, v in top_results.items():
        i += 1
        if (i > top_n + 1):
            break
        top_results_sliced[k] = v

    return top_results_sliced


def get_recipe_ingredients_cos_similarity(ingrX_bin: np.ndarray):
    """
    Makes a tf-idf transformation of a binary matrix and it feeds it to a cosine similarity algorithm.
    :param ingrX_bin:
    A numpy ndarray containing binary representation of ingredients.
    :return:
    Returns cosine similarity matrix based on the tf-idf of the inputted ingrX_bin.
    """
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(ingrX_bin).toarray()
    cos = cosine_similarity(tfidf)

    return cos


def get_top_matches(ingredient_name: str, top_n: int = 5):
    """
    Gets the top ingredient matches for given ingredient based on the F1 of the cosine similarity between
    the ingredients, compounds and recipes.
    :param ingredient_name:
    The name of the target ingredient.
    :param top_n:
    The number of ingredients that should be returned.
    :return:
    Returns a dictionary containing the top N ingredients with their similarity value.
    """

    if not os.path.exists(os.path.join(path,"cos_compounds.pkl")) or not os.path.exists(os.path.join(path,"cos_recipes.pkl")):
        save_cos_similarities_to_pkl()

    cos_comp_ingr = pd.read_pickle(os.path.join(path,"cos_compounds.pkl"))[ingredient_name]
    cos_recipe_ingr = pd.read_pickle(os.path.join(path,"cos_recipes.pkl"))[ingredient_name]

    f1_paired = {}

    for k, v in cos_comp_ingr.items():
        f1_paired[k] = (2 * cos_comp_ingr[k] * cos_recipe_ingr[k]) / (cos_comp_ingr[k] + cos_recipe_ingr[k])

    f1_paired = {k: f1_paired[k] for k in f1_paired if not isnan(f1_paired[k])}

    d_descending = OrderedDict(sorted(f1_paired.items(), key=lambda kv: kv[1], reverse=True))

    if top_n < 0:
        d_descending.pop(ingredient_name)
        return d_descending

    result = {}
    i = 0
    for k, v in d_descending.items():
        i += 1
        if (i > top_n+1):
            break
        if (k != ingredient_name):
            result[k] = v

    return result


def save_cos_similarities_to_pkl():
    """
    Gets and saves in pickle files the cosine similarities of the ingredients for both compounds and recipes and includes the
    ingredient labels for the columns and rows. The format of the sets is pandas DataFrame.
    """

    recipe_ingrX_bin = np.transpose(pd.read_pickle(os.path.join(path,"data/recipe_ingr_bin.pkl")))

    ingr_comp_bin = pd.read_pickle(os.path.join(path,"data/ingr_comp_bin.pkl"))
    ingr_inters = pd.read_pickle(os.path.join(path,"data/ingr_inters.pkl"))

    cos_recipes = pd.DataFrame(get_recipe_ingredients_cos_similarity(recipe_ingrX_bin))
    cos_compounds = pd.DataFrame(get_recipe_ingredients_cos_similarity(ingr_comp_bin))

    cos_recipes.columns = ingr_inters.values[:, 0]
    cos_recipes.index = ingr_inters.values[:, 0]
    print(cos_recipes)
    cos_compounds.columns = ingr_inters.values[:, 0]
    cos_compounds.index = ingr_inters.values[:, 0]

    cos_recipes.to_pickle(os.path.join(path,"cos_recipes.pkl"))
    cos_compounds.to_pickle(os.path.join(path,"cos_compounds.pkl"))



if __name__ == "__main__":
    print("Top Matches:")
    print(get_top_matches(input("Ingredient: "), int(input("Top n: "))))

    print("Top Replacements")
    print(get_top_replacements(input("Ingredient: "), int(input("Top n: "))))

    ingredients_list = ["beer", "potato"]

    print("Top Recommendations: (For a list of ingredients)")
    print(ingredients_list)
    print(get_top_recommendations_multiple(ingredients_list, int(input("Top n: "))))






