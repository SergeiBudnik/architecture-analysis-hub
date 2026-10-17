const config = {
 title: 'Architecture & Analysis Hub',
 tagline: 'Practical resources for business analysts and solution architects',
 url: 'https://SergeiBudnik.github.io',
 baseUrl: '/architecture-analysis-hub/',
 organizationName: 'SergeiBudnik',
 projectName: 'architecture-analysis-hub',
 trailingSlash: false,
 onBrokenLinks: 'throw',
 favicon: 'img/favicon.svg',
 i18n: {defaultLocale:'en',locales:['en']},
 presets: [['classic',{docs:{sidebarPath:require.resolve('./sidebars.js'),routeBasePath:'docs'},blog:false,theme:{customCss:require.resolve('./src/css/custom.css')}}]],
 themeConfig:{navbar:{title:'Architecture & Analysis Hub',items:[{to:'/docs/intro',label:'Documentation',position:'left'},{href:'https://github.com/SergeiBudnik/architecture-analysis-hub',label:'GitHub',position:'right'}]},footer:{style:'dark',copyright:'© 2026 Sergei Budnik. Educational resources.'}}
};
module.exports=config;