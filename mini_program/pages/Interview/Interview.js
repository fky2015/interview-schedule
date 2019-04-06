// pages/Interview/Interview.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
        showTimeline: 0,
        position: ['relative','fixed'],
        animateMask: '',
        animateTimeline: '',
        interview: [],
        timeline: []
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

    showTimeline: function () {
        var aniMask = ['showMask', 'hideMask'];
        var aniTimeline = ['showTimeline', 'hideTimeline'];

        this.setData ({
            showTimeline: 1
        });

        this.setData ({
            animateMask: aniMask[0],
            animateTimeline: aniTimeline[0]
        });

        wx.setNavigationBarTitle({
            title: '选择时间段'
        })
    },

    hideTimeline: function () {
        var that = this;
        var aniMask = ['showMask', 'hideMask'];
        var aniTimeline = ['showTimeline', 'hideTimeline'];

        this.setData({
            animateMask: aniMask[1],
            animateTimeline: aniTimeline[1]
        });

        setTimeout(
            function () {
                that.setData({
                    showTimeline: 0
                });
                wx.setNavigationBarTitle({
                    title: '面试'
                });
            }, 290
        );
    }
})