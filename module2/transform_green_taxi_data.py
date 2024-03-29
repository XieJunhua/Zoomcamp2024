if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    print(f"Preprocessing: rows with zero passengers: {data['passenger_count'].isin([0]).sum()}")
    print(f"Preprocessing: rows with zero passengers: {data['trip_distance'].isin([0]).sum()}")
    df = data[(data.passenger_count > 0) & (data.trip_distance > 0)]
    df['lpep_pickup_date'] = df['lpep_pickup_datetime'].dt.date
    print(df.columns)
    print(df['VendorID'].unique())
    df.rename(columns = {'VendorID':'vendor_id','RatecodeID':'ratecode_id','PULocationID':'pu_locationid','DOLocationID':'do_location_id'},
       inplace=True)
    print(df['passenger_count'].isin([0]).sum())
    print(df.shape[0] == df['vendor_id'].isin([1,2]).sum())
    return df



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['passenger_count'].isin([0]).sum() == 0, 'The passenger count greater than 0'
    assert output.trip_distance.isin([0]).sum() == 0, 'The trip distance greater than 0'
    assert output['vendor_id'].isin([1,2]).sum() == output.shape[0], 'The trip distance greater than 0'
    