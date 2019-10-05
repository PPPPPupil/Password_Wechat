// pages/account/deleteAccount/deleteAccount.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    // 种类的类别
    accountCategoryList: [{
        cateid: 1,
        catename: "QQ",
        tablehidden: true,
        // 当前所选种类的data-list
        currentCategoryDataList: [{
            id: 1,
            username: "张三",
            password: "123456",
            note: "没有备注",
            checked: false
          },
          {
            id: 2,
            username: "李四",
            password: "123456",
            note: "没有备注",
            checked: false
          }
        ]
      },
      {
        cateid: 2,
        catename: "微信",
        tablehidden: true,
        // 当前所选种类的data-list
        currentCategoryDataList: [{
            id: 3,
            username: "张三",
            password: "123456",
            note: "没有备注",
            checked: false
          },
          {
            id: 4,
            username: "李四",
            password: "123456",
            note: "没有备注",
            checked: false
          }
        ]
      },
      {
        cateid: 3,
        catename: "京东",
        tablehidden: true,
        // 当前所选种类的data-list
        currentCategoryDataList: [{
            id: 5,
            username: "张三",
            password: "123456",
            note: "没有备注",
            checked: false
          },
          {
            id: 6,
            username: "李四",
            password: "123456",
            note: "没有备注",
            checked: false
          }
        ]
      },

    ],
    //删除的id序列 默认空
    deleteIdList: [],
    userid: 1



  },
  /**
   * 显示当前accountCategoryList所拥有的 currentCategoryDataList table
   */
  showTable: function(e) {

    var currentCate = e.currentTarget.dataset.id;
    // console.log(currentCate)
    var tempaccountCategoryList = this.data.accountCategoryList;
    // console.log(tempaccountCategoryList)
    //循环找到当前cateid所对应的category 将其hidden属性设置为相反
    for (var index in tempaccountCategoryList) {
      if (tempaccountCategoryList[index].cateid == currentCate) {
        tempaccountCategoryList[index].tablehidden = !tempaccountCategoryList[index].tablehidden;
      }
    }

    // console.log(tempaccountCategoryList)
    this.setData({
      accountCategoryList: tempaccountCategoryList
    })
    // console.log(this.data.accountCategoryList)
  },

  selectDataId: function(e) {
    console.log(e.currentTarget.dataset.id)
  },
  /**
   * 将点击的所有checkbox对应的currentCategoryDataList[index_2].checked变量变为true，其它为false
   */
  checkboxChange: function(e) {
    //每次点击都将deleteIdList置为空 再赋值
    this.setData({
      deleteIdList: []
    })
    // 赋值
    var temp_currentCategoryDataListIndexs = e.detail.value
    console.log(temp_currentCategoryDataListIndexs)
    for (var index_3 in temp_currentCategoryDataListIndexs) {
      this.data.deleteIdList.push(temp_currentCategoryDataListIndexs[index_3])
    }

    // var temp_accountCategoryList = this.data.accountCategoryList; //中间变量
    // for (var index in temp_accountCategoryList) {
    //   for (var index_2 in temp_accountCategoryList[index].currentCategoryDataList) {
    //     temp_accountCategoryList[index].currentCategoryDataList[index_2].checked = false;
    //     for (var index_3 in temp_currentCategoryDataListIndexs) {
    //       if (temp_accountCategoryList[index].currentCategoryDataList[index_2].id == temp_currentCategoryDataListIndexs[index_3]) {
    //         temp_accountCategoryList[index].currentCategoryDataList[index_2].checked = true;
    //         this.data.deleteIdList.push(temp_currentCategoryDataListIndexs[index_3])
    //       }
    //     }

    //   }
    // }
    console.log(this.data.deleteIdList)
  },

  /**
   * 删除所有选中的checkbox对应的date（将id传回后台，后台从数据库删除）
   */
  deletAccount: function() {

    var that = this;
    if (that.data.deleteIdList.length == 0) {
      wx.showToast({
        title: '请勾选要删除的内容()',
        icon: 'none'
      })
    } else {
      console.log(that.data.deleteIdList)
      wx.showModal({
        title: '删除密码记录',
        content: '确定要删除所选密码记录？当前选中个数为:' + JSON.stringify(that.data.deleteIdList.length),
        showCancel: true, //是否显示取消按钮
        cancelText: "否", //默认是“取消”
        cancelColor: 'skyblue', //取消文字的颜色
        confirmText: "是", //默认是“确定”
        confirmColor: 'skyblue', //确定文字的颜色
        success: function(res) {
          if (res.cancel) {
            console.log("删除失败")
            //点击取消,默认隐藏弹框
          } else {
            //点击确定
            //发送要删除的id列表
            wx.request({
              url: 'http://122.51.3.42:5000/delete_account',
              data: {
                W_deleteIdList: JSON.stringify(that.data.deleteIdList)
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
            // 反馈
            console.log("删除成功");
            wx.showToast({
              title: '删除成功',
            })

          }
        },
        fail: function(res) {}, //接口调用失败的回调函数
        complete: function(res) {
          that.onLoad()
        }, //接口调用结束的回调函数（调用成功、失败都会执行）
      })

    }

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function(options) {
    var that = this;
    // 获取当前用户的账户详细信息
    wx.request({
      url: 'http://122.51.3.42:5000/get_account_category_list_detail',
      data: {
        W_userid: JSON.stringify(this.data.userid)
      },
      method: "POST",

      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success: function(res) {
        console.log(res.data.return_data);
        if (typeof(res.data.return_data) != undefined && typeof(res.data.return_data) != null) {
          that.setData({
            accountCategoryList: res.data.return_data
          })
        }

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