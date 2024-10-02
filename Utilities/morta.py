import Utilities.morta.api as ma
import Utilities.morta.functions as mf


def read_rules_from_morta_table_view(morta_api_key, view_id):
    """Reads a Table View from Morta and returns a DataFrame.

    Args:
        morta_api_key: api key of the user to query Morta
        view_id: table view where the rules reside

    Returns:
        DataFrame: Pandas DataFrame containing the rules data
    """
    try:
        view_rows = ma.get_view_rows(view_id=view_id, api_key=morta_api_key)
        rules_dataframe = mf.morta_rows_to_dataframe(view_rows)
        return rules_dataframe
    except Exception as e:
        print(f"Failed to read rules from Morta table view: {e}")
        return None