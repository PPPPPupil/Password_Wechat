// pages/mainWindow/mainWindow.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    itemsList: [{
      id: 1,
      title: "账户密码"
      // img: "none"
    }, {
      id: 2,
      title: "身份信息"
      // img: "none"
    }, {
      id: 3,
      title: "其他备注"
      // img: "none"
    }]

  },

  navigate2ItemPage: function(e) {
    var tempId = e.currentTarget.dataset.id
    if (tempId == 1) {
      console.log("1");
      wx.navigateTo({
        url: '../account/account'
      });
    } else if (tempId == 2) {
      console.log("2");
      wx.navigateTo({
        url: '../account/account'
      });
    } else {
      console.log("other");
      wx.navigateTo({
        url: '../account/account'
      });
    }


  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function(options) {

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