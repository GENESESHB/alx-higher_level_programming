-- creats the use user_0d_1 for all privileges in MYSQL
CREATE USER
    IF NOT EXISTS 'user_0d_1'@'localhost'
    IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES
    ON *.*
    TO 'user_0d_1'@'localhost'
    IDENTIFIED BY 'user_0d_1_pwd';
FLUSH PRIVILEGES;
