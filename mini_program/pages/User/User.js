// pages/User/User.js
const app = getApp();

Page({

    /**
     * 页面的初始数据
     */
    data: {
        hasUserInfo: false,
        firstTimeGetUserInfo: false,
        userInfo: {},
        name: '火云邪神',
        avatarUrl: ''
    },

    /**
     * 用户第一次登陆授权及获取微信用户信息
     */
    bindGetUserInfo(e) {
        var that = this;

        wx.getSetting({
            success(res) {
                console.log(res.authSetting);
                if (res.authSetting['scope.userInfo']) {
                    wx.getUserInfo({
                        success(res) {
                            app.globalData.hasUserInfo = true;
                            app.globalData.userInfo = res.userInfo;
                            console.log("hasUserInfo: ", app.globalData.hasUserInfo);
                            console.log(app.globalData.userInfo);

                            that.setData({
                                firstTimeGetUserInfo: true,
                                hasUserInfo: true
                            })
                        }
                    })
                }
            }
        })

        if (e.detail.userInfo) {
            wx.redirectTo({
                url: '../LogIn/LogIn',
            })
        }
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {      
        if(app.globalData.hasUserInfo){
            this.setData({
                hasUserInfo: true,
                avatarUrl: app.globalData.userInfo.avatarUrl
            });
        }
        else{
            this.setData({
                avatarUrl: '../../lib/unAuthAvatar.jpeg'
            });
        }
    },

    /**
     * 生命周期函数--监听页面初次渲染完成
     */
    onReady: function () {

    },

    /**
     * 生命周期函数--监听页面显示
     */
    onShow: function () {
        if(this.data.firstTimeGetUserInfo){
            this.setData({
                avatarUrl: app.globalData.userInfo.avatarUrl
            })
        }
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

    },

    gotoMyInterview: function () {
        wx.navigateTo({
            url: '../MyInterview/MyInterview',
        })
    },
})