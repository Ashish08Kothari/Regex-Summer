CREATE EXTERNAL TABLE IF NOT EXISTS youtube_db.youtube_videos (
  video_id        string,
  title           string,
  published_at    timestamp,
  view_count      bigint,
  like_count      bigint,
  channel_title   string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
  "separatorChar" = ",",
  "quoteChar"     = "\"",
  "escapeChar"    = "\\"
)
LOCATION 's3://your-bucket-name/path/to/processed/'
TBLPROPERTIES ('has_encrypted_data'='false');
