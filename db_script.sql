CREATE DATABASE discord_bot;

CREATE TABLE search_history(
    id INT AUTO_INCREMENT PRIMARY KEY,
    discord_user VARCHAR(100),
    term VARCHAR(250),
    results TEXT,
    created_date datetime
);