"""Unit tests for the multiple dataframes prompt class"""


import pandas as pd

from pandasai.prompts import MultipleDataframesPrompt


class TestMultipleDataframesPrompt:
    """Unit tests for the multiple dataframes prompt class"""

    def test_str_with_args(self):
        """Test that the __str__ method is implemented"""

        df1 = pd.DataFrame(
            {"A": [10, 20, 30, 40, 50], "B": [1, 2, 3, 4, 5], "C": [2, 3, 4, 5, 6]}
        )
        df2 = pd.DataFrame(
            {"A": [10, 20, 30, 40, 50], "B": [1, 2, 3, 4, 5], "C": [2, 3, 4, 5, 6]}
        )

        assert (
            str(MultipleDataframesPrompt(dataframes=[df1, df2]))
            == """
You are provided with the following pandas dataframes:
This is the metadata of the dataframe df1:
    A  B  C
0  10  1  2
1  20  2  3
2  30  3  4
3  40  4  5
4  50  5  6
This is the metadata of the dataframe df2:
    A  B  C
0  10  1  2
1  20  2  3
2  30  3  4
3  40  4  5
4  50  5  6
When asked about the data, your response should include a python code that describes the dataframes provided.
Using the provided dataframes and no other dataframes, return the python code and make sure to prefix the requested python code with <startCode> exactly and suffix the code with <endCode> exactly to get the answer to the following question:
"""  # noqa: E501
        )
