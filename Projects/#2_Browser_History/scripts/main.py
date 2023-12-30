
from etl.etl import *

import line_profiler

profile = line_profiler.LineProfiler()


@profile
def main():
    old_latest_ts = extract_latest_timestamp()

    jfile = extract_json()

    dates = transform_filter(jfile, latest_timestamp=old_latest_ts)[0]
    preprocessed_date = transform_preprocess_dates(dates)
    dates_ = preprocessed_date[0]
    times = preprocessed_date[1]

    new_latest_timestamp = transform_filter(jfile,
                                            latest_timestamp=old_latest_ts)[1]
    load_new_latest_timestamp(file='..\\data\\raw\\latest_timestamp.txt',
                              new_time=new_latest_timestamp)

    links = transform_filter(jfile, latest_timestamp=old_latest_ts)[2]

    websites = transform_preprocess_links(links)

    titles = transform_filter(jfile, latest_timestamp=old_latest_ts)[3]

    all_titles = transform_preprocess_titles(titles)

    df = transform_to_df(dates_, times, websites, all_titles)

    load_local_spreadsheet(df, extract_latest_timestamp())
    load_cloud_spreadsheet(df)

    transform_change_data_name(old_file='..\\data\\raw\\history.json',
                               name=extract_latest_timestamp())


if __name__ == "__main__":
    main()
    profile.print_stats()
