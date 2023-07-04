# create users table
def create_users_table(mycursor):
    query = """
        CREATE TABLE IF NOT EXISTS `users` (
            `id` INT AUTO_INCREMENT PRIMARY KEY,
            `chat_id` VARCHAR(255) NOT NULL UNIQUE,
            `language` VARCHAR(2) DEFAULT NULL,
            `currencies` JSON DEFAULT NULL,
            `updates` BOOLEAN DEFAULT 1
        )
    """

    mycursor.execute(query)


# create groups table
def create_groups_table(mycursor):
    query = """
        CREATE TABLE IF NOT EXISTS `groups` (
            `id` INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
            `chat_id` VARCHAR(255) NOT NULL UNIQUE,
            `name` VARCHAR(255) NOT NULL 
        )
    """

    mycursor.execute(query)


# create admins table
def create_admins_table(mycursor):
    query = """
        CREATE TABLE IF NOT EXISTS admins (
            id INT AUTO_INCREMENT PRIMARY KEY,
            chat_id VARCHAR(255) NOT NULL UNIQUE
        )
    """
    mycursor.execute(query)



# create all tables
def create_all_tables(mycursor):
    create_users_table(mycursor) # create user tables
    create_groups_table(mycursor) # create groups table
    mycursor.close()