# Browser History
## Checking for my Browser History
**Description**: <br>
**Field**: Data Engineering <br>
**Focus**: code documentation and profiling <br>
**Other focuses**: unit tests, data processing, ETL, data visualization, proper styling <br>
**Tools used**: Python, pytest, pandas, numpy, Google Sheets, MS Excel, Looker, MS Power Automate
## Pipeline
```mermaid
graph TD
  extract_json-->transform_filter;
  extract_latest_timestamp-->transform_filter;
  transform_filter-->load_new_latest_timestamp;
  transform_filter-->transform_preprocess_dates;
  transform_filter-->transform_preprocess_links;
  transform_filter-->transform_preprocess_titles;
  transform_preprocess_dates-->transform_to_df;
  transform_preprocess_links-->transform_to_df;
  transform_preprocess_titles-->transform_to_df;
  transform_to_df-->load_local_spreadsheet;
  transform_to_df-->load_cloud_spreadsheet;
```
