-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS youtube_db;
USE youtube_db;

-- Drop the table if it already exists
DROP TABLE IF EXISTS youtube_videos;

-- Create the youtube_videos table
CREATE TABLE youtube_videos (
    video_id VARCHAR(100) NOT NULL PRIMARY KEY,
    title TEXT,
    published_at DATETIME,
    view_count BIGINT,
    like_count BIGINT,
    channel_title VARCHAR(255)
);
