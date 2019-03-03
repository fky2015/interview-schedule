// pages/Authorize/Authorize.js
const app = getApp()

Page({

    /**
     * 页面的初始数据
     */
    data: {
        userInfo: {},
        hasUserInfo: false,
    },

    bindGetUserInfo(e) {
        console.log(e.detail.userInfo)
        if(e.detail.userInfo) {
            wx.navigateTo({
                url: '../LogIn/LogIn',
            })
        }
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
        var that = this;

        wx.getSetting({
            success(res) {
                console.log(res.authSetting);
                if(res.authSetting['scope.userInfo']) {
                    that.setData({
                        hasUserInfo: true
                    })

                    wx.getUserInfo({
                        success(res) {
                            console.log(res.userInfo)
                        }
                    })

                    /*setTimeout(
                        function () {
                            wx.switchTab({
                                url: '../HomePage/HomePage',
                            })
                        }, 2000
                    )*/ //该部分在完成login页面后要取消注释

                    //下面的跳转api要在之后删除，此处增加是为了方便调试
                    wx.navigateTo({
                        url: '../LogIn/LogIn',
                    })
                }
            }
        })
    },

    /**
     * 生命周期函数--监听页面初次渲染完成
     */
    onReady: function () {
        wx.getSetting({
            success(res) {
                console.log(res.authSetting);
                if (res.authSetting['scope.userInfo']) {
                    wx.getUserInfo({
                        success(res) {
                            console.log(res.userInfo)
                        }
                    })
                }
            }
        })
    },

    /**
     * 生命周期函数--监听页面显示
     */
    onShow: function () {
        
    },

    /**
     * 生命周期函数--监听页面隐藏
     */
    onHide: function () {

    },

    /**
     * 生命周期函数--监听页面卸载
     */
    onUnload: function () {

    },

    /**
     * 页面相关事件处理函数--监听用户下拉动作
     */
    onPullDownRefresh: function () {

    },

    /**
     * 页面上拉触底事件的处理函数
     */
    onReachBottom: function () {

    },

    /**
     * 用户点击右上角分享
     */
    onShareAppMessage: function () {

    }
})