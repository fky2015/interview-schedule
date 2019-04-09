module.exports = {
	title: '项目文档',
	description: 'Interview-schedule 文档',
	themeConfig: {
		navbar: false,
		sidebar: [{
			title: '前端开发', // required
			collapsable: false, // optional, defaults to true
			sidebarDepth: 1, // optional, defaults to 1
			children: [
				['/小程序页面目录树及页面简介.md', "小程序页面目录树及页面简介"],
				['/小程序调用api.md', "小程序调用api"],
			]
		},{
			title: '需求文档以及技术选型', // required
			collapsable: false, // optional, defaults to true
			sidebarDepth: 1, // optional, defaults to 1
			children: [
				["/docs/1开发流程.md","开发流程"],
				["/docs/2需求分析.md","需求分析"],
				["/docs/3开发流程建议.md","开发流程建议"],
				["/社团面试系统需求文档.md","社团面试系统需求文档"],
			]
		},
		
		{
				title: '后端开发', // required
				collapsable: false, // optional, defaults to true
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
							['/showdoc/datadict/users/UserProfileClub.md', '用户-社团'],
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
				children: [{
					title: "普通用户相关",
					path: '/showdoc/api/user/',
					children: [
						["/showdoc/api/user/user.md", "user"],
						["/showdoc/api/user/club.md", "club"],
						["/showdoc/api/user/interview.md", "interview"],
						["/showdoc/api/user/interviewTimeline.md", "interviewTimeline"],
						["/showdoc/api/user/timeline.md", "timeline"],
					]
				},
				{
					title: "社团管理相关",
					path: '/showdoc/api/admin/',
					children: [
						["/showdoc/api/admin/user.md", "user"],
						["/showdoc/api/admin/club.md", "club"],
						["/showdoc/api/admin/interview.md", "interview"],
						["/showdoc/api/admin/interviewTimeline.md", "interviewTimeline"],
						["/showdoc/api/admin/timeline.md", "timeline"],
						["/showdoc/api/admin/membership.md", "membership"],
						["/showdoc/api/admin/instate.md", "instate"],
					]
				}
			]
			},

		]
	},

}