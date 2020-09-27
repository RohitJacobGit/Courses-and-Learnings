import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_blobs
from sklearn.datasets import make_classification
import inspect
import math
import os


current_directory = inspect.getfile(inspect.currentframe())
# Changed the path to the data folder in mac
data_folder = os.path.realpath(os.path.join("../jacobs-uni-enrichment-analysis/data/"))

production_dataset_filename = os.path.realpath(
    os.path.join(data_folder, "pea_data_2018-08-28_cleaned.csv"))
production_dataset_filename_1000instances = os.path.realpath(
    os.path.join(data_folder, "pea_data_2018-08-28_cleaned_1000instances.csv"))
production_dataset_shuffled_filename = os.path.realpath(
    os.path.join(data_folder, "pea_data_2018-08-28_cleaned_shuffled.csv"))


numeric_columns = ['order_weight_min', 'order_weight_aim', 'order_weight_max',
                   'thickness', 'output_weight_target', 'width',
                   'customer_priority', 'piece_weight_min', 'piece_weight_aim',
                   'piece_weight_max',
                   'value_name', 'due_date', 'date_planned_initial_end',
                   'date_target_end',
                   'first_coil_end_date', 'first_coil_released_date',
                   'first_coil_delivered_date', 'last_coil_end_date',
                   'last_coil_released_date', 'last_coil_delivered_date',

                   ]


def get_default_5_features():
    features = ['order_weight_aim',
                'width',
                'thickness',
                'piece_weight_aim',
                "productionsteps"]
    return features


###############################################################################
def encode_target_features_to_categorical(target_feature_values, borders):
    """Assign the corresponding integer-valued code to the observable falling
    into the bins defined by borders.

    Args:
        target_feature_values: pandas Series
        borders: borders of intervals the observable must be
            divided in, list of numbers

    Returns:
        observable_encoded: pandas Series
        observable_label: list of symmetric integer-valued codes
            (e.g. [-2, -1, 1, 2])
    """

    n_int = len(borders) + 1

    encoded_label_names = [x for x in range(math.ceil(-n_int/2),
                                            math.floor(n_int/2) + 1)]
    if (n_int % 2 == 0):
        encoded_label_names.remove(0)

    bins = sorted(borders + [-math.inf, +math.inf])
    # pd.cut Bin values into discrete intervals.
    encoded_values = pd.cut(target_feature_values,
                            bins=bins,
                            labels=encoded_label_names)
    return encoded_values, encoded_label_names
###############################################################################


def _create_lateness_shuffled_csv_file():
    dt = pd.read_csv(production_dataset_filename, sep=";", decimal=",")
    dt["lateness"] = dt["lateness"].sample(frac=1, random_state=1920)
    dt.to_csv(production_dataset_shuffled_filename, sep=";", decimal=",")


def get_sms_data_csv_shuffled():
    dt = pd.read_csv(production_dataset_shuffled_filename, sep=";",
                     decimal=",")
    return dt


def get_sms_data_csv():
    dt = pd.read_csv(production_dataset_filename, sep=";", decimal=",")
    # dt = get_dataframe_from_csv_shuffled()
    return dt


def get_sms_data_csv1000():
    dt = pd.read_csv(production_dataset_filename_1000instances, sep=";",
                     decimal=",")
    # dt = get_dataframe_from_csv_shuffled()
    return dt


def get_sms_data_csv_for_regression(features=None, borders=None,
                                    target_attribute="lateness", test_size=0.1,
                                    random_state=None):
    target_attribute = "lateness"

    dt = get_sms_data_csv()

    if(random_state is None):
        random_state = np.random.randint(100000)

    if(features is None):
        features = get_default_5_features()

    if(borders is None):
        borders = [-2880, 2880]

    X_full = dt.loc[:, features].reset_index(drop=True)
    y_full = dt.loc[:, target_attribute].reset_index(drop=True)

    X_train, X_test, y_train, y_test = train_test_split(
        X_full, y_full, test_size=0.1, random_state=random_state)
    return(X_train, X_test, y_train, y_test)


def get_sms_data_csv_for_classification(features=None, borders=None,
                                        test_size=0.1, random_state=None):

    target_attribute = "lateness"

    dt = get_sms_data_csv()

    if(random_state is None):
        random_state = np.random.randint(100000)

    if(features is None):
        features = get_default_5_features()

    if(borders is None):
        borders = [-2880, 2880]

    X_full = dt.loc[:, features].reset_index(drop=True)
    y_full = dt.loc[:, target_attribute].reset_index(drop=True)

    #print(y_full)

    (y_full_encoded_values, Y_full_encoded_class_labels) = encode_target_features_to_categorical(y_full, borders)

    #print(Y_full_encoded_class_labels)

    X_train, X_test, y_train, y_test = train_test_split(
        X_full, y_full_encoded_values, test_size=0.1, random_state=random_state)
    return(X_train, X_test, y_train, y_test)


def get_sms_data_csv_for_classification_all_categorical_DataFrame(features=None, borders=None, feature_labels=[1, 2, 3]):

    target_attribute = "lateness"

    dt = get_sms_data_csv()

    if(random_state is None):
        random_state = np.random.randint(100000)

    if(features is None):
        features = get_default_5_features()

    if(borders is None):
        borders = [-2880, 2880]

    for column in features:
        if column in numeric_columns:
            dt[column] = pd.qcut(dt[column], q=len(feature_labels), labels=feature_labels)

    X_full = dt.loc[:, features].reset_index(drop=True)
    y_full = dt.loc[:, target_attribute].reset_index(drop=True)

    (y_full_encoded_values, Y_full_encoded_class_labels) = encode_target_features_to_categorical(y_full, borders)

    return (X_full, y_full_encoded_values)


def get_sms_data_csv_for_classification_all_categorical(features=None, borders=None, test_size=0.1, random_state=None, feature_labels=[1, 2, 3]):

    (X_full, y_full_encoded_values) = get_sms_data_csv_for_classification_all_categorical_DataFrame(features=features,
                                                                                                    borders=borders, feature_labels=feature_labels
                                                                                                    )

    X_train, X_test, y_train, y_test = train_test_split(
        X_full, y_full_encoded_values, test_size=0.1, random_state=random_state)
    return(X_train, X_test, y_train, y_test)


def get_sms_data_csv_for_classification_all_categorical_1000(features=None, borders=None, test_size=0.1, random_state=None, feature_labels=[1, 2, 3]):

    target_attribute = "lateness"

    dt = get_sms_data_csv()

    if(random_state is None):
        random_state = np.random.randint(100000)

    dt = dt.sample(n=1000, random_state=random_state)

    if(features is None):
        features = get_default_5_features()

    if(borders is None):
        borders = [-2880, 2880]

    for column in features:
        if column in numeric_columns:
            dt[column] = pd.qcut(dt[column], q=len(feature_labels), labels=feature_labels)

    X_full = dt.loc[:, features].reset_index(drop=True)
    y_full = dt.loc[:, target_attribute].reset_index(drop=True)

    (y_full_encoded_values, Y_full_encoded_class_labels) = encode_target_features_to_categorical(y_full, borders)

    X_train, X_test, y_train, y_test = train_test_split(
        X_full, y_full_encoded_values, test_size=0.1, random_state=random_state)
    return(X_train, X_test, y_train, y_test)


def get_sms_data_csv_for_classification_all_categorical_qcut3(borders=[-2880, 2880]):
    target_attribute = "lateness"
    df = pd.read_csv(production_dataset_filename, sep=";", decimal=",")

    for column in df:
        if column in numeric_columns:
            df[column] = pd.qcut(df[column], q=3, labels=[1, 2, 3])

    if(borders is None):
        borders = [-2880, 2880]

    X_full = df.loc[:, df.columns != target_attribute].reset_index(drop=True)
    y_full = df.loc[:, target_attribute].reset_index(drop=True)

    (y_full_encoded_values, Y_full_encoded_class_labels) = encode_target_features_to_categorical(y_full, borders)

    X_train, X_test, y_train, y_test = train_test_split(
        X_full, y_full_encoded_values, test_size=0.1)
    return(X_train, X_test, y_train, y_test)


if __name__ == "__main__":
    pass
    # create_lateness_shuffled_csv_file()
    #dt = get_dataframe_from_csv_shuffled()
    # print(production_dataset_filename)
    #get_random_data(random_state = 1)
