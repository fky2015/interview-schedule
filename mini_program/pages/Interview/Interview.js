// pages/Interview/Interview.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
        hideTimeline: true,
        animateMask: '',
        animateTimeline: '',
        classInterview: 'foot',
        containDist: 0,
        footDist: 0,
        head: [],
        foot: [],
        interview: [{ title: '秋季面试第一场', dateTime: '2019年9月20日 9:00-11:30', place: '2B-201', id: 1 }, { title: '秋季面试第二场', dateTime: '2019年9月21日 9:00-11:30', place: '2B-202', id: 2 }, { title: '秋季面试第三场', dateTime: '2019年9月22日 9:00-11:30', place: '2B-203', id: 3 }, { title: '秋季面试第四场', dateTime: '2019年9月23日 9:00-11:30', place: '2B-204', id: 4 }, { title: '秋季面试第五场', dateTime: '2019年9月24日 9:00-11:30', place: '2B-205', id: 5 }, { title: '秋季面试第六场', dateTime: '2019年9月25日 9:00-11:30', place: '2B-206', id: 6 }, { title: '秋季面试第七场', dateTime: '2019年9月26日 9:00-11:30', place: '2B-207', id: 7}],
        timeline: ['9:00-9:10', '9:10-9:20', '9:20-9:30', '9:30-9:40', '9:40-9:50', '9:50-10:00'],
        color: ['244,164,180', '150,150,150', '144,212,216', '255,236,180', '137,223,196', '159,221,249'],
        bgcolor: '',
        times: 0
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
        var that = this;
        var interview = [{ title: '秋季面试第一场', dateTime: '2019年9月20日 9:00-11:30', place: '2B-201', id: 1 }, { title: '秋季面试第二场', dateTime: '2019年9月21日 9:00-11:30', place: '2B-202', id: 2 }, { title: '秋季面试第三场', dateTime: '2019年9月22日 9:00-11:30', place: '2B-203', id: 3 }, { title: '秋季面试第四场', dateTime: '2019年9月23日 9:00-11:30', place: '2B-204', id: 4 }, { title: '秋季面试第五场', dateTime: '2019年9月24日 9:00-11:30', place: '2B-205', id: 5 }, { title: '秋季面试第六场', dateTime: '2019年9月25日 9:00-11:30', place: '2B-206', id: 6 }, { title: '秋季面试第七场', dateTime: '2019年9月26日 9:00-11:30', place: '2B-207', id: 7 }];
        var timeline = ['9:00-9:10', '9:10-9:20', '9:20-9:30', '9:30-9:40', '9:40-9:50', '9:50-10:00'];

        this.setData({
            head: interview
        });

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

    /**
     * 显示时间片
     */
    showTimeline: function (e) {

        var that = this;
        var n = e.currentTarget.dataset.id;
        var time = this.data.times;

        if(this.data.hideTimeline == true) {
            var views = { head: [], foot: [] };

            if (this.data.times == 5) {
                this.setData({
                    times: 0
                });
            }
            else {
                this.setData({
                    times: time + 1
                });
            }

            views = this.split(this.data.interview, n);

            this.setData({
                head: views.head,
                foot: views.foot,
                containDist: this.containerDistance(n),
                footDist: this.footDistance(this.data.timeline),
                classInterview: 'footMoved',
                animateMask: 'showMask',
                bgcolor: this.data.color[this.data.times]
            });

            wx.setNavigationBarTitle({
                title: '选择时间段'
            });

            setTimeout (
                function () {
                    that.setData({
                        hideTimeline: false,
                        animateTimeline: 'showTimeline'
                    });
                }, 290
            );
        }

        else {
            this.hideTimeline();
        }
    },

    /**
     *隐藏时间片 
     */
    hideTimeline: function () {
        
        var that = this;

        if(this.data.hideTimeline == false) {
            this.setData({
                animateMask: 'hideMask',
                animateTimeline: 'hideTimeline'
            });

            wx.setNavigationBarTitle({
                title: '面试'
            });

            setTimeout(
                function () {
                    that.setData({
                        hideTimeline: true,
                        classInterview: 'foot',
                        footDist: 0
                    });
                }, 290
            );
        }
    },

    /**
     * 拆分面试数组
     */
    split: function (array, n) {
        var length, i;
        var views = {head: [], foot: []};

        length = array.length;
        views.head.length = n;
        views.foot.length = length - n;

        for (i = 1; i <= length; i++) {
            if (i <= n) {
                views.head[i - 1] = array[i - 1];
            }
            else {
                views.foot[i - n - 1] = array[i - 1];
            }
        }

        return views;
    },

    /**
     * 求得面试栏下半部分需要移动的距离
     */
    footDistance: function (array) {
        var length, dist;

        length = array.length;
        dist = length * 130;

        return dist;
    },

    /**
     * 求得时间片清单相对其父组件的位置
     */
    containerDistance: function (n) {
        var dist;

        dist = n * 255;

        return dist;
    },

    /**
     * 处理用户加入面试请求
     */
    joinInterview: function () {
        wx.showModal({
            title: 'ฅ\'ω\'ฅ~喵',
            content: '确定参加这一场面试吗？',
            confirmColor: '#d92414',
            success(res) {
                if (res.confirm) {
                    wx.showToast({
                        title: '报名成功！',
                        icon: 'success',
                        duration: 2000
                    });
                } 
                else if (res.cancel) {
                    
                }
            }
        });
    }
})

 