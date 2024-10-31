import pytest
import pandas as pd
from excel_utility import ExcelUtility  # assuming the file is named excel_utility.py


# Create a sample test Excel file for testing
@pytest.fixture
def create_test_excel_file(tmp_path):
    file_path = tmp_path / "test_data.xlsx"
    data = {
        "Column1": [1, 2, 3, 4, 5],
        "Column2": ["A", "B", "C", "D", "E"],
        "Column3": [True, False, True, False, True]
    }
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)
    return file_path


def test_convert_to_csv(create_test_excel_file, tmp_path):
    file_path = create_test_excel_file
    output_csv = tmp_path / "test_data.csv"
    excel_util = ExcelUtility(file_path)

    # Run convert_to_csv
    excel_util.convert_to_csv(output_csv)

    # Verify CSV file creation and contents
    assert output_csv.exists()
    df_csv = pd.read_csv(output_csv)
    df_excel = pd.read_excel(file_path)
    pd.testing.assert_frame_equal(df_csv, df_excel)


def test_remove_rows(create_test_excel_file, tmp_path):
    file_path = create_test_excel_file
    output_excel = tmp_path / "modified_data.xlsx"
    excel_util = ExcelUtility(file_path)

    # Remove rows and save to a new file
    excel_util.remove_rows([0, 1], output_excel)

    # Verify rows are removed
    df_modified = pd.read_excel(output_excel)
    df_expected = pd.DataFrame({
        "Column1": [3, 4, 5],
        "Column2": ["C", "D", "E"],
        "Column3": [True, False, True]
    })
    pd.testing.assert_frame_equal(df_modified, df_expected)


def test_read_file(create_test_excel_file):
    file_path = create_test_excel_file
    excel_util = ExcelUtility(file_path)

    # Run read_file and verify DataFrame content
    df = excel_util.read_file()
    expected_data = {
        "Column1": [1, 2, 3, 4, 5],
        "Column2": ["A", "B", "C", "D", "E"],
        "Column3": [True, False, True, False, True]
    }
    df_expected = pd.DataFrame(expected_data)
    pd.testing.assert_frame_equal(df, df_expected)


def test_export_distinct_values(create_test_excel_file, tmp_path):
    file_path = create_test_excel_file
    output_csv = tmp_path / "distinct_values.csv"
    excel_util = ExcelUtility(file_path)

    # Run export_distinct_values
    excel_util.export_distinct_values(output_csv)

    # Verify distinct values file contents
    df_distinct = pd.read_csv(output_csv)
    expected_data = {
        "Column1": [1, 2, 3, 4, 5],
        "Column2": ["A", "B", "C", "D", "E"],
        "Column3": [True, False, None, None, None]
    }
    df_expected = pd.DataFrame(expected_data)
    pd.testing.assert_frame_equal(df_distinct, df_expected, check_dtype=False)


def test_get_headers(create_test_excel_file):
    file_path = create_test_excel_file
    excel_util = ExcelUtility(file_path)

    # Run get_headers and verify output
    headers = excel_util.get_headers()
    expected_headers = ["Column1", "Column2", "Column3"]
    assert headers == expected_headers
