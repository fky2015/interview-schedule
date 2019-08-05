// pages/Authorize/Authorize.js
const app = getApp()

Page({

    /**
     * 页面的初始数据
     */
    data: {
        hiddenAni: {}
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
                    wx.getUserInfo({
                        success(res) {
                            app.globalData.hasUserInfo = true;
                            app.globalData.userInfo = res.userInfo;
                            console.log("hasUserInfo: ", app.globalData.hasUserInfo);
                            console.log(app.globalData.userInfo);
                        }
                    })
                }

                else {
                    app.globalData.userInfo = res.userInfo;
                    console.log("hasUserInfo: ", app.globalData.hasUserInfo);
                }

                var animation = wx.createAnimation({
                    duration: 200,
                    timingFunction: 'ease',
                    delay: 1800
                })

                that.hiddenAni = animation;
                animation.opacity(1).step();
                that.setData({
                    hiddenAni: animation.export(),
                });

                setTimeout(
                    function () {
                        wx.switchTab({
                            url: '../HomePage/HomePage',
                        })
                    }, 2000
                ) //该部分在完成login页面后要取消注释

                //下面的跳转api要在之后注释掉，此处增加是为了方便调试
                /*wx.navigateTo({
                    url: '../LogIn/LogIn',
                })*/
            }
        })
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