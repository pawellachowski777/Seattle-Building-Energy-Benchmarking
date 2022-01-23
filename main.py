import pandas as pd


def convert_columns(df, columns, new_type):
    for column in columns:
        df[column] = df[column].astype(new_type)


def data_processing(path, columns_to_drop, convert_to_float, columns_to_rename,
                    convert_to_int, columns_order, columns_to_add=None):
    # read data
    df = pd.read_csv(path)

    # delete columns
    df.drop(columns_to_drop, axis=1, inplace=True)

    # convert to float
    convert_columns(df=df, columns=convert_to_float, new_type=float)

    # delete Nan and zeros
    to_zero = df.loc[:, 'SiteEUI(kBtu/sf)':'NaturalGas(kBtu)'].columns.tolist()
    df[to_zero] = df[to_zero].fillna(0)
    df = df[df['SiteEnergyUse(kBtu)'] != 0]

    # rename columns
    df.rename(columns=columns_to_rename, inplace=True)

    # convert kBtu to kWh
    converter = 3.4121416
    for column_convert in columns_to_convert:
        df[column_convert[1]] = df[column_convert[0]] * converter

    # convert to int
    convert_columns(df=df, columns=convert_to_int, new_type=int)

    # sort columns
    if columns_to_add is not None:
        df[columns_to_add] = None
    df = df[columns_order]

    return df


# columns_to_convert_19 = [
#     ['SiteEnergyUse(kBtu)', 'SiteEnergyUse(kWh)'],
#     ['SiteEnergyUseWN(kBtu)', 'SiteEnergyUseWN(kWh)'],
#     ['SteamUse(kBtu)', 'SteamUse(kWh)'],
#     ['NaturalGas(kBtu)', 'NaturalGas(kWh)']
# ]
