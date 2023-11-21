-- creates user user_0d_1 with password user_0d_1_pwd
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to user_0d_1
GRANT ALL ON *.* TO user_0d_1@localhost;

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
