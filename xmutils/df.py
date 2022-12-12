import typing
import pandas as pd


def flatten_json_columns(df: pd.DataFrame, columns: typing.List) -> pd.DataFrame:
    """
    Take a Pandas dataframe and a set a JSON columns, normalizes the JSON into columns
    and concatenates the result dataframes into a single dataframe
    """
    dfs = [df]
    for column in columns:
        result_df = pd.json_normalize(df[column])
        dfs.append(result_df)
    return pd.concat(dfs, axis=1)


def columns_as_json(
    df: pd.DataFrame, new_column: str, columns: typing.List
) -> pd.DataFrame:
    """
    Creates a new column named `new_column` that contains json with the column names
    as keys and the column values as values.

    For example, if you have an existing dataframe with the structure of:
    property_id | property_name
    prop_123    | Acme Way

    Calling columns_as_json(df, "property", ["property_id", "property_name", "property_url"]) will give you:
    property_id | property_name | property
    prop_123    | Acme Way      | '{"property_id": "prop_123, "property_name": "Acme Way"}'
    """
    df[new_column] = df[columns].apply(lambda x: x.to_json(), axis=1)
    return df


def columns_as_dict(
    df: pd.DataFrame, new_column: str, columns: typing.List
) -> pd.DataFrame:
    """
    Creates a new column named `new_column` that contains a dictionary with the column names
    as dictionary keys and the column values as dictionary values.

    For example, if you have an existing dataframe with the structure of:
    property_id | property_name
    prop_123    | Acme Way

    Calling columns_as_dict(df, "property", ["property_id", "property_name", "property_url"]) will give you:
    property_id | property_name | property
    prop_123    | Acme Way      | {"property_id": "prop_123, "property_name": "Acme Way"}
    """
    df[new_column] = df[columns].apply(lambda x: x.to_dict(), axis=1)
    return df
