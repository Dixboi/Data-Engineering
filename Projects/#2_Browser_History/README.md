# Browser History
## Checking for my Browser History
| Field | Content |
|:------|:--------|
| Description| Tracking my browser history 
| Field | Data Engineering  | 
| Focus | proper styling, automation, proper docstrings  |
| Other focuses | data processing, ETL, data visualization, profiling  |
| Tools used | Python, pandas, numpy, Google Sheets, MS Excel, Looker, MS Power Automate |
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
