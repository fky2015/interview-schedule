// pages/LogIn/LogIn.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
        windowWidth: 0,
        times: 0,
        sweepAni: {},
        hiddenAni: {},
        zIndex: 1,
        imgUrls: [
            '/lib/1.jpg',
            '/lib/2.jpg',
            '/lib/3.jpg',
            '/lib/4.jpg',
            '/lib/5.jpg',
        ],
        btn: '继续',
        hideBackwardBtn: 1,
        btnOpacity: 0
    },

    /**
     * 点击前进按钮
     */
    forward: function () {
        var that = this;
        var time = this.data.times;

        this.setData({
            times: time + 1
        })

        time = time + 1;

        if(time != 4){

            if(time != 3){
                this.setData({
                    btn: '继续'
                });
            }
            else{
                this.setData({
                    btn: '完成!'
                });
            }
            
            var distance = - this.data.windowWidth * this.data.times;

            var animation = wx.createAnimation({
                duration: 300,
                timingFunction: 'ease'
            });

            this.sweepAni = animation;
            animation.translateX(distance).step();
            this.setData({
                sweepAni: animation.export()
            });
        }

        else{
            var animation = wx.createAnimation({
                duration: 300,
                timingFunction: 'ease',
            })

            this.setData({
                zIndex: 3
            })

            this.hiddenAni = animation;
            animation.opacity(1).step();
            this.setData({
                hiddenAni: animation.export()
            });

            setTimeout(
                function () {
                    wx.switchTab({
                        url: '../HomePage/HomePage',
                    })
                }, 300
            );
        }

        if (time == 1) {
            this.setData({
                hideBackwardBtn: 0
            })

            var animation = wx.createAnimation({
                duration: 300,
                timingFunction: 'ease',
            })

            this.btnBackwardAni = animation;
            animation.opacity(1).step();
            this.setData({
                btnBackwardAni: animation.export()
            });

            setTimeout(
                function () {
                    that.setData({
                        btnOpacity: 1
                    })
                }, 300
            );
        }
    },

    /**
     * 点击后退按钮
     */
    backward: function () {
        var that = this;
        var time = this.data.times;

        this.setData({
            times: time - 1
        })

        time = time - 1;

        if (time != 3) {
            this.setData({
                btn: '继续'
            });
        }
        else {
            this.setData({
                btn: '完成!'
            });
        }

        var distance = - this.data.windowWidth * this.data.times;

        var animation = wx.createAnimation({
            duration: 300,
            timingFunction: 'ease'
        });

        this.sweepAni = animation;
        animation.translateX(distance).step();
        this.setData({
            sweepAni: animation.export()
        });

        if(time == 0){
            var animation = wx.createAnimation({
                duration: 300,
                timingFunction: 'ease',
            })

            this.btnBackwardAni = animation;
            animation.opacity(0).step();
            this.setData({
                btnBackwardAni: animation.export()
            });

            setTimeout(
                function () {
                    that.setData({
                        btnOpacity: 0,
                        hideBackwardBtn: 1
                    })
                }, 300
            );
        }
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
        var that = this;

        wx.getSystemInfo({
            success: function (res) {
                that.data.windowWidth = res.windowWidth;
                console.log(that.data.windowWidth);
            },
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

    }
})