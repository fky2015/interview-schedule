// pages/LogIn/LogIn.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
        hiddenAni: {},
        zIndex: 0
    },

    //该函数用于跳转至主页便于调试，请在上线之前将其注释掉
    skipToHome: function () {
        var that = this;
        var animation = wx.createAnimation({
            duration: 300,
            timingFunction: 'ease',
        })

        that.setData({
            zIndex: 1
        })

        that.hiddenAni = animation;
        animation.opacity(1).step();
        that.setData({
            hiddenAni: animation.export()
        });

        setTimeout(
            function () {
                wx.switchTab({
                    url: '../HomePage/HomePage',
                })
            }, 300
        )
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {

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
        console.log(this.data.hideMask);
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