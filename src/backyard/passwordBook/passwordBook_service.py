from flask import render_template, jsonify, request, session
from src import app
import json
from flask_wtf import CSRFProtect
from src.backyard.passwordBook import passwordBook_db as AMP

csrf = CSRFProtect()


def selectDataWithCategoryId(accountDatas, cateid):
    new_accountDatas = []
    for accountData in accountDatas:
        if AMP.query_accountData_byCateName(accountData["category_name"])["id"] == cateid:
            new_accountDatas.append({
                "id": accountData["id"], "username": accountData["username"], "password": accountData["password"],
                "note": accountData["note"], "checked": False
            })
    return new_accountDatas


@app.route("/add_account_category_list", methods=["POST"])
def add_account_category():
    """增加账户种类 """
    print("add_account_category_list")
    newCategory = request.form["W_newCategory"]
    userid = request.form["W_userid"]
    # data = request.form.get('wei_data')
    # data = request.values.get('wei_data')
    newCategory = json.loads(newCategory)
    userid = json.loads(userid)
    print(newCategory)

    AMP.add_account_category(userid, newCategory, tablehidden=True)

    return jsonify({
        "success": True,
        "return_data": "种类添加成功"
    })


@app.route("/get_account_category_list", methods=["POST"])
def get_account_category_list():
    """从数据库获取当前用户的账户种类"""
    print("get_account_category_list")
    userid = int(request.form["W_userid"])
    accountCategoryList = []
    categorynames = AMP.query_accountCategory_byUserID(userid)
    for categoryname in categorynames:
        accountCategoryList.append(categoryname["category_name"])
    print(accountCategoryList)
    return jsonify({
        "success": True,
        "return_data": accountCategoryList
    })


@app.route("/add_account_info", methods=["POST"])
def add_account_info():
    """向account表中增加当前用户的新账户信息"""
    print("adding")
    accountInfo = request.form["W_accountInfo"]
    accountInfo = json.loads(accountInfo)
    categoryname = accountInfo["categoryname"]
    userid = accountInfo["userid"]
    username = accountInfo["username"]
    password = accountInfo["password"]
    note = accountInfo["note"]
    AMP.add_account_data(categoryname, userid, username, password, note)
    print(accountInfo)
    return jsonify({
        "success": True,
        "return_data": "账户信息添加成功"
    })


@app.route("/get_account_category_list_detail", methods=["POST"])
def get_account_category_list_detail():
    """从数据库获取当前用户的账户种类 包括详细信息"""
    print("getting")
    userid = int(request.form["W_userid"])
    accountCategoryList = AMP.query_accountCategory_byUserID(userid)
    accountDatas = AMP.query_accountData_byUserID(userid)
    accountCategoryListDetail = []
    for accountCategoryName in accountCategoryList:
        temp_cateid = AMP.query_accountData_byCateName(accountCategoryName["category_name"])["id"]
        temp_cateid_Datas = selectDataWithCategoryId(accountDatas, temp_cateid)
        accountCategoryListDetail.append({
            "cateid": temp_cateid, "catename": accountCategoryName["category_name"], "tablehidden": True,
            "currentCategoryDataList": temp_cateid_Datas
        })
    # for accountData in accountDatas:
    #     temp_cateid = AMP.query_accountData_byCateName(accountData["category_name"])["id"]
    #     temp_cateid_Datas = selectDataWithCategoryId(accountDatas, temp_cateid)
    #     accountCategoryListDetail.append({
    #         "cateid": temp_cateid, "catename": accountData["category_name"], "tablehidden": True,
    #         "currentCategoryDataList": temp_cateid_Datas
    #     })
    # accountCategoryListDetail = [
    #     {
    #         "cateid": 1, "catename": "QQ", "tablehidden": True,
    #         "currentCategoryDataList": [{
    #             "id": 1, "username": "张三", "password": "123456", "note": "无", "checked": False
    #         }]
    #     }
    # ]
    return jsonify({
        "success": True,
        "return_data": accountCategoryListDetail
    })


@app.route("/delete_account", methods=["POST"])
def delete_account():
    """从account表中删除当前用户传来的的账户信息（基于id）"""
    print("delete_account")
    idList = json.loads(request.form["W_deleteIdList"])
    for id in idList:
        AMP.delete_accountData_byID(int(id))
    # deleteIdList = json.loads(deleteIdList)
    return jsonify({
        "success": True,
        "return_data": "账户信息删除成功"
    })
