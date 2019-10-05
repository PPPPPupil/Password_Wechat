// pages/account/addAccount/addAccount.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    hiddenName: true,
    userid: 1,
    accountCategoryList: [],
    currentCategory: "QQ",
    newCategory: "null",
    username: "null",
    password: "null",
    note: "null"
  },
  /**
   * 选择要增加的账户种类
   */
  bindPickerChange: function(e) {
    this.setData({
      currentCategory: this.data.accountCategoryList[e.detail.value]
    });
    console.log("current Category is:" + this.data.currentCategory);
  },
  /**
   * 获取输入的新种类
   */
  showAddView: function() {
    this.setData({
      hiddenName: !this.data.hiddenName
    })
  },
  bindPickerTap:function(){
    var that = this;
    // 点击时 获取当前用户的账户种类
    wx.request({
      url: 'http://127.0.0.1:5000/get_account_category_list',
      data: {
        W_userid: JSON.stringify(this.data.userid)
      },
      method: "POST",
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success: function (res) {
        console.log(res.data.return_data);
        that.setData({
          accountCategoryList: res.data.return_data
        })
      }
    })
  },
  bindCategoryInput: function(e) {
    this.setData({
      newCategory: e.detail.value
    })
    console.log(this.data.newCategory)
  },
  addCategorySheet: function() {
    // 点击按钮-将新的accountCategoryList发送到数据库-重新渲染页面使picker实现动态加载


    wx.request({
      url: 'http://127.0.0.1:5000/add_account_category_list',
      data: {
        W_newCategory: JSON.stringify(this.data.newCategory),
        W_userid: JSON.stringify(this.data.userid)
      },
      method: "POST",
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success: function(res) {
        console.log(res.data);
      }
    })

    console.log(this.data.accountCategoryList)
    this.onLoad();
  },
  /**
   * username
   */
  bindUsernameInput: function(e) {
    this.setData({
      username: e.detail.value
    })
    console.log("username:" + this.data.username)
  },
  /**
   * password
   */
  bindPasswordInput: function(e) {
    this.setData({
      password: e.detail.value
    })
    console.log("password:" + this.data.password)
  },
  /**
   * note
   */
  bindNoteInput: function(e) {
    this.setData({
      note: e.detail.value
    })
    console.log("note:" + this.data.note)
  },
  /**
   * 确认增加账户
   */
  ensureAdd: function() {

    wx.request({
      url: 'http://127.0.0.1:5000/add_account_info',
      data: {
        W_accountInfo: JSON.stringify({
          categoryname: this.data.currentCategory,
          userid: this.data.userid,
          username: this.data.username,
          password: this.data.password,
          note: this.data.note
        })
      },
      method: "POST",
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success: function(res) {
        console.log(res.data);
      }
    })

  },
  /**
   * 取消新增账户信息
   */
  cancelAdd: function() {
    wx.navigateBack({
      delta: 1
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function(options) {
    var that = this;
    // 点击时 获取当前用户的账户种类
    wx.request({
      url: 'http://127.0.0.1:5000/get_account_category_list',
      data: {
        W_userid: JSON.stringify(this.data.userid)
      },
      method: "POST",
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success: function (res) {
        console.log(res.data.return_data);
        that.setData({
          accountCategoryList: res.data.return_data
        })
      }
    })


  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function() {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function() {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function() {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function() {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function() {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function() {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function() {

  }
})