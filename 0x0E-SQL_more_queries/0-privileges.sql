-- 0-privileges.sql
SELECT CONCAT('SHOW GRANTS FOR ''', user, '''@''', host, ''';') FROM mysql.user WHERE user IN ('user_0d_1', 'user_0d_2') INTO OUTFILE '/tmp/privileges.sql';
SOURCE /tmp/privileges.sql;
