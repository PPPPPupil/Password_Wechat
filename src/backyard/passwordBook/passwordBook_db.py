from flask import current_app


def add_account_category(user_id, category_name, tablehidden=True):
    cp = current_app.config["CONNECTION_POOL"]
    # 添加
    r = cp.insert(
        """
        INSERT INTO `account_category` (`user_id`,`category_name`,`tablehidden`)
        VALUES (
            %s, %s, %s
        )
        """, (user_id, category_name, tablehidden)
    )
    return r


def query_accountCategory_byUserID(user_id):
    cp = current_app.config["CONNECTION_POOL"]
    r = cp.fetch_all(
        """
        SELECT 
            `category_name`
        FROM
            `account_category`
        WHERE
            `user_id` = %s 
        """, (user_id,)
    )
    return r


def add_account_category(user_id, category_name, tablehidden=True):
    cp = current_app.config["CONNECTION_POOL"]
    # 添加
    r = cp.insert(
        """
        INSERT INTO `account_category` (`user_id`,`category_name`,`tablehidden`)
        VALUES (
            %s, %s, %s
        )
        """, (user_id, category_name, tablehidden)
    )
    return r


def add_account_data(categoryname,userid, username, password, note):
    cp = current_app.config["CONNECTION_POOL"]
    # 添加
    r = cp.insert(
        """
        INSERT INTO `account_data` (`category_name`,`user_id`,`username`,`password`,`note`)
        VALUES (
            %s, %s, %s,%s, %s
        )
        """, (categoryname, userid, username,password,note)
    )
    return r


def query_accountData_byUserID(user_id):
    cp = current_app.config["CONNECTION_POOL"]
    r = cp.fetch_all(
        """
        SELECT 
            `id`,`category_name`,`username`,`password`,`note`
        FROM
            `account_data`
        WHERE
            `user_id` = %s 
        """, (user_id,)
    )
    return r



def query_accountData_byCateName(category_name):
    cp = current_app.config["CONNECTION_POOL"]
    r = cp.fetch_one(
        """
        SELECT 
            `id`
        FROM
            `account_category`
        WHERE
            `category_name` = %s 
        """, (category_name,)
    )
    return r

def delete_accountData_byID(id):
    cp = current_app.config["CONNECTION_POOL"]
    # 删除
    r = cp.delete(
        """
        DELETE FROM
            `account_data`
            WHERE
            `id` = %s
        """,(id,)
    )
    return r