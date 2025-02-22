"""Unit tests for the correct error prompt class"""


from pandasai.prompts import CorrectErrorPrompt


class TestCorrectErrorPrompt:
    """Unit tests for the correct error prompt class"""

    def test_str_with_args(self):
        """Test that the __str__ method is implemented"""
        assert (
            str(
                CorrectErrorPrompt(
                    question="What is the correct code?",
                    error_message="Error message",
                    code="df.head()",
                    answer="df.head(5)",
                    num_rows=5,
                    num_columns=5,
                    df_head="df.head()",
                    error_returned="error",
                )
            )
            == """
You are provided with a pandas dataframe (df) with 5 rows and 5 columns.
This is the metadata of the dataframe:
df.head().

The user asked the following question:
What is the correct code?

You generated this python code:
df.head()

It fails with the following error:
error

Correct the python code and return a new python code (do not import anything) that fixes the above mentioned error. Do not generate the same code again.
Make sure to prefix the requested python code with <startCode> exactly and suffix the code with <endCode> exactly.
"""  # noqa: E501
        )
