// pages/HomePage/HomePage.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
        showAni: {},
        showMask: 1
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
        var that = this;
        var animation = wx.createAnimation({
            duration: 200,
            timingFunction: 'ease',
            delay: 0
        })

        that.showAni = animation;
        animation.opacity(0).step();
        that.setData({
            showAni: animation.export()
        });

        setTimeout(
            function () {
                that.setData({
                    showMask: 0
                })
            }, 200
        )
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

    },

    gotoClubList: function () {
        wx.navigateTo({
            url: '../ClubList/ClubList',
        })
    },

    gotoNotice: function () {
        wx.navigateTo({
            url: '../Notice/Notice',
        })
    }
})