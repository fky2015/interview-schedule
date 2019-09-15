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

        function animationAndJump() {
            var animation = wx.createAnimation({
                duration: 300,
                timingFunction: 'ease',
                delay: 3700
            });

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
                }, 4000
            );
        }

        wx.showLoading({
            title: '加载中...',
        })

        wx.getSetting({
            success(res) {
                //console.log(res.authSetting);
                if(res.authSetting['scope.userInfo']) {
                    wx.getUserInfo({
                        success(res) {
                            app.globalData.hasUserInfo = true;
                            app.globalData.userInfo = res.userInfo;
                            console.log("hasUserInfo: ", app.globalData.hasUserInfo);
                            console.log(app.globalData.userInfo);
                        }
                    })

                    wx.login({
                        success: function (res) {
                            console.log('code: ', res.code);
                            wx.request({
                                url: "https://dev.fkynjyq.com/api_token_auth/",
                                method: "POST",
                                data: {
                                    code: res.code
                                },

                                success: function (res) {
                                    wx.hideLoading();
                                    animationAndJump();
                                    console.log(res.data);
                                },

                                fail: function (res) {
                                    wx.hideLoading();
                                    wx.showToast({
                                        title: '请检查网络',
                                        icon: 'none',
                                        duration: 2000
                                    })
                                }
                            })
                        }
                    })
                }

                else {
                    app.globalData.userInfo = res.userInfo;
                    console.log("hasUserInfo: ", app.globalData.hasUserInfo);
                    wx.hideLoading();
                    animationAndJump();
                }
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