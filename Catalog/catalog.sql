CREATE TABLE catalog(id SERIAL PRIMARY KEY, 
                    title VARCHAR(80) NOT NULL,
                    category VARCHAR(80), 
                    description VARCHAR(250),
                    TIMESTAMP,
                      );

