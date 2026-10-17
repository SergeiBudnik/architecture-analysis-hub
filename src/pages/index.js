import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
export default function Home(){
 const cards=[['Requirements & Analysis','Business requirements, SRS, use cases and user stories.','/docs/requirements/overview'],['Architecture & Design','High-level architecture, API and data design.','/docs/architecture/overview'],['Engineering Specifications','Backend, frontend, messaging and sequence diagrams.','/docs/engineering/overview'],['Template Catalogue','A navigable index of planned resources.','/docs/templates/catalogue']];
 return <Layout title="Home" description="Practical architecture and system analysis resources">
 <header className="heroBanner"><div className="container"><h1>Architecture & Analysis Hub</h1><p>Open knowledge resources for business analysts, systems analysts and solution architects. Curated by Sergei Budnik.</p><Link className="button button--secondary button--lg" to="/docs/intro">Explore the library →</Link></div></header>
 <main className="container"><div className="featureGrid">{cards.map(([t,d,l])=><div className="feature" key={t}><h3>{t}</h3><p>{d}</p><Link to={l}>Explore →</Link></div>)}</div><p><strong>Preview release:</strong> introductory guides and documentation structure are available. Original downloadable templates are under review and not published yet.</p></main>
 </Layout>;
}