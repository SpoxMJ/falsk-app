CREATE DATABASE heroes;
use heroes;

CREATE TABLE favorite_colors (
  name VARCHAR(200),
  color VARCHAR(100)
);

INSERT INTO favorite_colors
  (name, color)
VALUES
  ('waterman', 'blue'),
  ('star', 'yellow');

