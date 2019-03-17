module.exports = {
	title: '项目文档',
	description: 'Interview-schedule 文档',
	themeConfig: {
		navbar: false,
		sidebar: [{
				title: '后端开发', // required
				path: '/社团面试系统需求文档.md', // optional, which should be a absolute path.
				collapsable: true, // optional, defaults to true
				sidebarDepth: 1, // optional, defaults to 1
				children: [
					['/后端开发日志.md', "后端开发日志"],
					['/后端开发文档.md', '后端开发文档'],
					['/后端开发踩坑.md', '后端开发踩坑']
				]
			},
			{
				title: '数据字典', // required
				// path: '/', // optional, which should be a absolute path.
				collapsable: false, // optional, defaults to true
				sidebarDepth: 1, // optional, defaults to 1
				children: [{
						title: "用户相关",
						children: [
							['/showdoc/datadict/users/UserProfile.md', '用户'],
							['/showdoc/datadict/users/Club.md', '社团'],
							['/showdoc/datadict/users/UserProfileClub.md','用户-社团'],
							['/showdoc/datadict/users/Membership.md', '关系']
						]
					}, {
						title: "面试相关",
						children: [
							['/showdoc/datadict/interview/Interview.md', "面试"],
							['/showdoc/datadict/interview/InState.md', "准入状态"],
							['/showdoc/datadict/interview/InterviewTimelines.md', "面试表"],
							['/showdoc/datadict/interview/Timeline.md', "时间片"],

						]
					}


				]
			},
			{
				title: 'api接口', // required
				path: '/showdoc/api/', // optional, which should be a absolute path.
				collapsable: false, // optional, defaults to true
				sidebarDepth: 1, // optional, defaults to 1
				children: [
					{
						title: "用户相关",
						path: '/showdoc/api/user/',
						children:[
							["/showdoc/api/user/info.md","info"],
							["/showdoc/api/user/club.md","club"],
							["/showdoc/api/user/membership.md","membership"],
						]
					}	
					,
					{
						title: "公共接口",
						path: "/showdoc/api/public",
						children:[
							["/showdoc/api/public/club.md","club"]
						]
					}
				]
			},

		]
	},

}
