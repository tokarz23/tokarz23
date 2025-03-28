import great_expectations as gx
import pandas as pd


class GreatExpectationsPOC:
    def __init__(self, source_file_path, expectation_suite_name):
        self.source_file_path = source_file_path
        self.expectation_suite_name = expectation_suite_name

    def data_load(self):
        # Loading source data provided in .csv file format
        context = gx.get_context()
        df = pd.read_csv(self.source_file_path)
        df_ge = gx.from_pandas(df)
        # TODO: double check lines 15-20
        data_source = context.data_sources.add_pandas("pandas")
        data_asset = data_source.add_dataframe_asset(name="pd dataframe asset")

        batch_definition = data_asset.add_batch_definition_whole_dataframe("batch definition")
        batch = batch_definition.get_batch(batch_parameters={"dataframe": df})

        return df_ge

    def load_expectations_test_suite(self):
        pass
