const config = {
  title: 'Architecture & Analysis Hub',
  tagline: 'Practical resources for analysts and solution architects',
  url: 'https://SergeiBudnik.github.io',
  baseUrl: '/architecture-analysis-hub/',
  organizationName: 'SergeiBudnik',
  projectName: 'architecture-analysis-hub',
  trailingSlash: false,
  onBrokenLinks: 'throw',
  favicon: 'img/favicon.svg',
  i18n: {defaultLocale:'en',locales:['en']},
  markdown: {mermaid:true},
  themes: ['@docusaurus/theme-mermaid'],
  presets: [['classic',{
    docs:{sidebarPath:require.resolve('./sidebars.js'),routeBasePath:'docs'},
    blog:false,
    theme:{customCss:require.resolve('./src/css/custom.css')}
  }]],
  themeConfig:{
    navbar:{
      title:'Architecture & Analysis Hub',
      items:[
        {to:'/docs/intro',label:'Documentation',position:'left'},
        {to:'/docs/templates/catalogue',label:'Resources',position:'left'},
        {to:'/docs/downloads',label:'Downloads',position:'left'},
        {to:'/docs/for-educators-practitioners',label:'Educators',position:'left'},
        {to:'/docs/editable-source-diagrams',label:'HLD & BPMN',position:'left'},
        {to:'/docs/diagram-gallery',label:'Diagrams',position:'left'},
        {to:'/search',label:'Search',position:'left'},
        {to:'/docs/about-the-author',label:'About',position:'left'},
        {href:'https://github.com/SergeiBudnik/architecture-analysis-hub',label:'GitHub',position:'right'}
      ]
    },
    footer:{
      style:'dark',
      links:[
        {title:'Explore',items:[{label:'Payment Architecture',to:'/docs/payments/overview'},{label:'Downloads',to:'/docs/downloads'},{label:'Diagram Gallery',to:'/docs/diagram-gallery'}]},
        {title:'Community',items:[{label:'Author',to:'/docs/about-the-author'},{label:'Educators',to:'/docs/for-educators-practitioners'},{label:'Community Use',to:'/docs/community-adoption'},{label:'Feedback',to:'/docs/contribute'},{label:'CC BY 4.0',to:'/docs/license'},{label:'GitHub',href:'https://github.com/SergeiBudnik/architecture-analysis-hub'}]}
      ],
      copyright:'© 2026 Sergei Budnik. Educational resources.'
    }
  }
};
module.exports=config;
